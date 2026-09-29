"""Fast frame-by-frame renderer for HTML motion pages (brag-scaled).

Page contract: window.render(t) draws the frame at t seconds as a pure function of t,
window.ready is a promise that resolves once fonts and assets are loaded, and
window.DURATION (optional) gives the length in seconds.

Pipeline:
  1. Chromium is pushed onto the GPU (ANGLE backend for the platform). Default headless
     Chromium often rasterises on the CPU through SwiftShader, which was 0.5-1.7 s per
     1080p frame on the reference laptop, against ~75 ms on its GPU.
  2. N browsers render contiguous chunks of the timeline in parallel. Frames are captured
     over raw CDP and stream-copied into MJPEG segments, so nothing is written as images
     and nothing is encoded while the GPU is rasterising.
  3. Segments are encoded in parallel with the best working H.264 encoder (NVENC, Quick
     Sync, AMF, VideoToolbox, else libx264), joined with a stream copy, and the audio is
     muxed.

Reference run (Windows 11, i9-11950H 8C/16T, RTX A2000 Laptop, NVMe): a 130 s, 60 fps
video (7,800 frames at 1920x1080) went from ~45 min (Playwright PNG screenshots to disk,
then x264) to 3 min 46 s (capture 162 s at 48 fps, encode 54 s, mux 9 s).

Requires: python 3.9+, `pip install playwright imageio-ffmpeg`, `playwright install chromium`.

Usage:
  python fastrender.py video.html --stills 1.5 7 12.25 --still-dir stills
  python fastrender.py video.html --out brag.mp4 --fps 30 --audio score.wav \
      --poster 18.5 --poster-jpg brag.jpg
"""
import argparse, base64, os, pathlib, shutil, subprocess, sys, tempfile, time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

COMMON = ["--force-color-profile=srgb", "--font-render-hinting=none", "--allow-file-access-from-files",
          "--disable-background-timer-throttling", "--disable-renderer-backgrounding"]
GPU = ["--enable-gpu", "--ignore-gpu-blocklist", "--enable-gpu-rasterization", "--enable-zero-copy"]
# Verified on Windows + NVIDIA. The macOS and Linux backends are the documented ANGLE
# ones but unmeasured; the renderer check below reports what actually ran.
PLATFORM_GPU = {
    "win32": ["--use-angle=d3d11", "--force_high_performance_gpu"],
    "darwin": ["--use-angle=metal"],
    "linux": ["--use-angle=vulkan", "--enable-features=Vulkan"],
}

# Captured JPEGs are full-range BT.601. Convert the range only and tag the matrix as BT.601:
# converting to BT.709 forces a YUV->RGB->YUV path that halved encode throughput on the
# reference machine, and the tagged output decodes within 0.94/255 mean (43.6 dB PSNR) of
# a lossless PNG capture of the same frame.
TV = ["-vf", "scale=out_range=tv,format=yuv420p"]
TAGS = ["-colorspace", "smpte170m", "-color_primaries", "bt709", "-color_trc", "iec61966-2-1", "-color_range", "tv"]
ENCODERS = {  # tried in order; each is test-encoded before use
    "h264_nvenc": ["-preset", "p7", "-tune", "hq", "-rc", "vbr", "-cq", "14", "-b:v", "0", "-profile:v", "high"],
    "h264_qsv": ["-preset", "slower", "-global_quality", "18", "-profile:v", "high"],
    "h264_amf": ["-quality", "quality", "-rc", "cqp", "-qp_i", "16", "-qp_p", "16", "-profile:v", "high"],
    "h264_videotoolbox": ["-b:v", "30M", "-profile:v", "high"],
    "libx264": ["-preset", "slow", "-crf", "14", "-profile:v", "high"],
}


def ffmpeg_exe():
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        return shutil.which("ffmpeg") or sys.exit("ffmpeg not found: pip install imageio-ffmpeg")


def pick_encoder(ff, want):
    names = [want] if want != "auto" else list(ENCODERS)
    for name in names:
        ok = subprocess.run([ff, "-v", "error", "-f", "lavfi", "-i", "color=c=gray:s=256x256:d=0.2", "-c:v", name,
                             *ENCODERS[name], "-pix_fmt", "yuv420p", "-f", "null", "-"], capture_output=True).returncode == 0
        if ok:
            return name
    sys.exit(f"no working encoder among {names}")


def launch(p, gpu):
    args = COMMON + (GPU + PLATFORM_GPU.get(sys.platform, []) if gpu else [])
    return p.chromium.launch(args=args)


def open_page(p, url, w, h, gpu=True):
    b = launch(p, gpu)
    pg = b.new_page(viewport={"width": w, "height": h})
    pg.goto(url)
    pg.evaluate("window.ready || document.fonts.ready")
    pg.evaluate("document.fonts.ready")
    return b, pg, pg.context.new_cdp_session(pg)


def renderer_name(pg):
    return pg.evaluate("""(() => { const c = document.createElement('canvas').getContext('webgl');
      const d = c && c.getExtension('WEBGL_debug_renderer_info');
      return d ? c.getParameter(d.UNMASKED_RENDERER_WEBGL) : 'unknown'; })()""")


def grab(cdp, t, fmt):
    cdp.send("Runtime.evaluate", {"expression": f"window.render({t!r})", "awaitPromise": True})
    opts = {"format": fmt, "optimizeForSpeed": True}
    if fmt == "jpeg":
        opts["quality"] = 100
    return base64.b64decode(cdp.send("Page.captureScreenshot", opts)["data"])


def capture(job):
    url, w, h, fps, fmt, lo, hi, seg, poster_t, ff, gpu = job
    from playwright.sync_api import sync_playwright
    # stream-copy frames into the segment: no encoding while the GPU rasterises
    # (12 concurrent NVENC sessions during capture cut throughput from ~45 to ~17 fps)
    enc = subprocess.Popen([ff, "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(fps),
                            "-c:v", "mjpeg" if fmt == "jpeg" else "png", "-i", "-", "-c:v", "copy", seg],
                           stdin=subprocess.PIPE)
    with sync_playwright() as p:
        b, pg, cdp = open_page(p, url, w, h, gpu)
        grab(cdp, 0.0, fmt)  # warm-up: the first capture compiles shaders
        for i in range(lo, hi):
            enc.stdin.write(grab(cdp, poster_t if (i == 0 and poster_t is not None) else i / fps, fmt))
        b.close()
    enc.stdin.close()
    if enc.wait() != 0:
        raise RuntimeError(f"segment writer failed: {seg}")
    return hi - lo


def main():
    cpu = os.cpu_count() or 4
    ap = argparse.ArgumentParser(description="Render a window.render(t) page to MP4, fast.")
    ap.add_argument("page")
    ap.add_argument("--out", default="brag.mp4")
    ap.add_argument("--fps", type=int, default=30)
    ap.add_argument("--duration", type=float, help="seconds; defaults to window.DURATION")
    ap.add_argument("--width", type=int, default=1920)
    ap.add_argument("--height", type=int, default=1080)
    ap.add_argument("--workers", type=int, default=max(2, min(12, cpu * 3 // 4)),
                    help="parallel browsers (reference knee: 12 on 16 threads)")
    ap.add_argument("--encode-jobs", type=int, default=4,
                    help="parallel encoder sessions; consumer GPUs may cap hardware sessions")
    ap.add_argument("--capture", choices=["jpeg", "png"], default="jpeg",
                    help="jpeg q100 is visually lossless and ~40%% faster; png for fine gradients")
    ap.add_argument("--encoder", choices=["auto", *ENCODERS], default="auto")
    ap.add_argument("--no-gpu", action="store_true", help="force CPU rasterisation (debugging)")
    ap.add_argument("--audio")
    ap.add_argument("--poster", type=float, help="t (s) of the settled frame baked in as frame 0")
    ap.add_argument("--poster-jpg", help="also save that frame as a JPEG")
    ap.add_argument("--stills", type=float, nargs="*", help="only save PNG stills at these times")
    ap.add_argument("--still-dir", default="stills")
    ap.add_argument("--keep", action="store_true", help="keep intermediate segments")
    a = ap.parse_args()

    url = pathlib.Path(a.page).resolve().as_uri()
    ff = ffmpeg_exe()
    gpu = not a.no_gpu
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        try:
            b, pg, cdp = open_page(p, url, a.width, a.height, gpu)
        except Exception as e:  # a GPU flag this platform rejects: fall back rather than fail
            print(f"GPU launch failed ({str(e)[:80]}); falling back to default rasteriser")
            gpu = False
            b, pg, cdp = open_page(p, url, a.width, a.height, gpu)
        rend = renderer_name(pg)
        dur = a.duration or pg.evaluate("window.DURATION || 0")
        if a.poster_jpg and a.poster is not None:
            pathlib.Path(a.poster_jpg).write_bytes(grab(cdp, a.poster, "jpeg"))
        if a.stills:
            d = pathlib.Path(a.still_dir); d.mkdir(parents=True, exist_ok=True)
            for t in a.stills:
                (d / f"t{t:07.2f}.png").write_bytes(grab(cdp, t, "png"))
                print(f"still t={t}s -> {d / f't{t:07.2f}.png'}")
        b.close()
    print(f"renderer: {rend}")
    if "SwiftShader" in rend:
        print("WARNING: CPU rasteriser (SwiftShader) in use; expect roughly 10x slower frames")
    if a.stills is not None:
        print(f"stills -> {a.still_dir}")
        return
    if not dur:
        sys.exit("no duration: pass --duration or set window.DURATION")

    encoder = pick_encoder(ff, a.encoder)
    # a browser costs ~2 s to start, so give each one 60+ frames
    n = int(round(dur * a.fps)); W = max(1, min(a.workers, n // 60)); step = -(-n // W)
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="fastrender_", dir=pathlib.Path(a.out).resolve().parent))
    jobs = [(url, a.width, a.height, a.fps, a.capture, lo, min(n, lo + step), str(tmp / f"seg{k:03d}.mkv"),
             a.poster if k == 0 else None, ff, gpu) for k, lo in enumerate(range(0, n, step))]
    print(f"{n} frames @ {a.fps} fps, {len(jobs)} browsers, capture={a.capture}, encoder={encoder}")

    t0 = time.perf_counter()
    with ProcessPoolExecutor(len(jobs)) as ex:
        frames = sum(ex.map(capture, jobs))
    cap = time.perf_counter() - t0
    print(f"captured {frames} frames in {cap:.1f}s = {frames / cap:.1f} fps")

    # Encode segments in parallel: MJPEG decode and the range conversion are single-threaded
    # per ffmpeg process, so one process per segment keeps the cores and the encoder busy.
    t1 = time.perf_counter()
    jobs_n = len(jobs) if encoder == "libx264" else max(1, min(a.encode_jobs, len(jobs)))
    vargs = [*TV, "-c:v", encoder, *ENCODERS[encoder], "-g", str(a.fps * 2), *TAGS]
    if encoder == "libx264":
        vargs += ["-threads", str(max(1, cpu // len(jobs)))]

    def encode(j):
        out = j[7].replace(".mkv", ".mp4")
        subprocess.run([ff, "-y", "-loglevel", "error", "-i", j[7], *vargs, "-an", out], check=True)
        return out

    with ThreadPoolExecutor(jobs_n) as ex:
        outs = list(ex.map(encode, jobs))
    print(f"encoded {len(outs)} segments in {time.perf_counter() - t1:.1f}s ({jobs_n} at a time)")

    lst = tmp / "list.txt"
    lst.write_text("".join(f"file '{o}'\n" for o in outs))
    cmd = [ff, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst)]
    if a.audio:
        cmd += ["-i", a.audio]
    # concat drops the colour tags; restore them in the bitstream without re-encoding
    cmd += ["-c:v", "copy", "-bsf:v",
            "h264_metadata=colour_primaries=1:transfer_characteristics=13:matrix_coefficients=6:video_full_range_flag=0"]
    if a.audio:
        cmd += ["-c:a", "aac", "-b:a", "256k", "-af", "loudnorm=I=-16:TP=-1.5", "-ar", "48000", "-shortest"]
    cmd += ["-movflags", "+faststart", a.out]
    subprocess.run(cmd, check=True)
    if not a.keep:
        shutil.rmtree(tmp, ignore_errors=True)
    print(f"wrote {a.out} in {time.perf_counter() - t0:.1f}s total")


if __name__ == "__main__":
    main()
