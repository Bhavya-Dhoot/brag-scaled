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

Every machine is different, so `--tune` calibrates this one, once: it finds the GPU flags that
really put Chromium on the GPU, the number of parallel browsers where capture stops getting
faster, and how many encoder sessions the hardware takes. It uses the whole machine for a
minute or two and is only right on an idle one, so it never starts by itself: until it has
been run, a render uses safe defaults and says so, and `--tune` refuses when the machine is
busy. Restart or close heavy applications first. Settings live in
~/.cache/brag-scaled/tune.json, one entry per GPU, and any flag on the command line wins.

Requires: python 3.9+, `pip install playwright imageio-ffmpeg`, `playwright install chromium`.
`--audit` also needs `pip install pillow`.

Usage:
  python fastrender.py --doctor
  python fastrender.py --tune
  python fastrender.py video.html --stills 1.5 7 12.25 --still-dir stills
  python fastrender.py video.html --audit
  python fastrender.py video.html --out brag.mp4 --fps 30 --audio score.wav \
      --poster 18.5 --poster-jpg brag.jpg
  python fastrender.py video.html --out brag-4k.mp4 --scale 2
  python fastrender.py overlay.html --transparent --out card.mov --png-dir card-png
  python fastrender.py overlay.html --over clip.mp4 --out with-graphics.mp4
"""
import argparse, base64, importlib.util, json, os, pathlib, re, shutil, subprocess, sys, tempfile, time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

COMMON = ["--force-color-profile=srgb", "--font-render-hinting=none", "--allow-file-access-from-files",
          "--disable-background-timer-throttling", "--disable-renderer-backgrounding"]
GPU = ["--enable-gpu", "--ignore-gpu-blocklist", "--enable-gpu-rasterization", "--enable-zero-copy"]
# The first entry for each platform is the default. Only Windows + NVIDIA was measured by the
# author; --tune tries each entry on the machine it runs on and keeps the first one whose
# renderer is real hardware, so the others are verified where they are used.
GPU_TRY = {
    "win32": [["--use-angle=d3d11", "--force_high_performance_gpu"], ["--use-angle=d3d11"], ["--use-angle=gl"], []],
    "darwin": [["--use-angle=metal"], ["--use-angle=gl"], []],
    "linux": [["--use-angle=vulkan", "--enable-features=Vulkan"], ["--use-angle=gl-egl"], ["--use-gl=egl"], []],
}
PLATFORM_GPU = {k: v[0] for k, v in GPU_TRY.items()}
SOFTWARE = ("SwiftShader", "llvmpipe", "softpipe", "Basic Render")   # renderer names that mean the CPU is drawing
TUNE_FILE = pathlib.Path.home() / ".cache" / "brag-scaled" / "tune.json"
TUNE_V = 1
# A page of about the weight of a real scene: 96 bordered, shadowed, rotating cards and a counter.
BENCH = """<!doctype html><meta charset="utf-8"><style>html,body{margin:0;width:1920px;height:1080px;overflow:hidden;background:#f0ede8;font:700 34px sans-serif}
.c{position:absolute;width:150px;height:96px;border:3px solid #111;border-radius:14px;background:#fff;box-shadow:8px 8px 0 #111;display:flex;align-items:center;justify-content:center}
#h{position:absolute;left:80px;top:60px;font-size:120px}</style><div id="h">0</div><script>
const els=[];for(let i=0;i<96;i++){const e=document.createElement('div');e.className='c';e.textContent=i;document.body.append(e);els.push(e)}
window.DURATION=4;window.ready=Promise.resolve();
window.render=t=>{document.getElementById('h').textContent=Math.round(t*1000);els.forEach((e,i)=>{const a=t*2+i*.4;
e.style.transform=`translate(${885+Math.cos(a)*(200+i*7)}px,${492+Math.sin(a*1.3)*(120+i*4)}px) rotate(${Math.sin(a)*20}deg) scale(${1+.2*Math.sin(a*2)})`;
e.style.background=`hsl(${(i*9+t*60)%360} 80% 70%)`})};</script>"""

# Captured JPEGs are full-range BT.601. Convert the range only and tag the matrix as BT.601:
# converting to BT.709 forces a YUV->RGB->YUV path that halved encode throughput on the
# reference machine, and the tagged output decodes within 0.94/255 mean (43.6 dB PSNR) of
# a lossless PNG capture of the same frame.
TV = "scale=out_range=tv,format=yuv420p"
TAGS = ["-colorspace", "smpte170m", "-color_primaries", "bt709", "-color_trc", "iec61966-2-1", "-color_range", "tv"]
ENCODERS = {  # tried in order; each is test-encoded before use
    "h264_nvenc": ["-preset", "p7", "-tune", "hq", "-rc", "vbr", "-cq", "14", "-b:v", "0", "-profile:v", "high"],
    "h264_qsv": ["-preset", "slower", "-global_quality", "18", "-profile:v", "high"],
    "h264_amf": ["-quality", "quality", "-rc", "cqp", "-qp_i", "16", "-qp_p", "16", "-profile:v", "high"],
    "h264_videotoolbox": ["-b:v", "30M", "-profile:v", "high"],
    "libx264": ["-preset", "slow", "-crf", "14", "-profile:v", "high"],
}
QUALITY_KEYS = {"h264_nvenc": ["-cq"], "h264_qsv": ["-global_quality"], "h264_amf": ["-qp_i", "-qp_p"], "libx264": ["-crf"]}
PRORES = ["-c:v", "prores_ks", "-profile:v", "4444", "-pix_fmt", "yuva444p10le", "-vendor", "apl0"]


def ffmpeg_exe():
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        return shutil.which("ffmpeg") or sys.exit("ffmpeg not found: pip install imageio-ffmpeg")


def encoder_works(ff, name):
    return subprocess.run([ff, "-v", "error", "-f", "lavfi", "-i", "color=c=gray:s=256x256:d=0.2", "-c:v", name,
                           *ENCODERS[name], "-pix_fmt", "yuv420p", "-f", "null", "-"], capture_output=True).returncode == 0


def pick_encoder(ff, want):
    names = [want] if want != "auto" else list(ENCODERS)
    for name in names:
        if encoder_works(ff, name):
            return name
    sys.exit(f"no working encoder among {names}")


def encoder_args(name, quality):
    """Encoder settings, with --crf mapped onto each encoder's own quality knob (lower is better)."""
    args = list(ENCODERS[name])
    if quality is not None:
        for key in QUALITY_KEYS.get(name, []):
            args[args.index(key) + 1] = str(quality)
    return args


def probe(ff, clip):
    """Size, frame rate and length of a video file, read from ffmpeg's own banner."""
    err = subprocess.run([ff, "-hide_banner", "-i", clip], capture_output=True, text=True, errors="replace").stderr
    size = re.search(r"Video:.*?\b(\d{2,5})x(\d{2,5})\b", err)
    fps = re.search(r"([\d.]+) fps", err)
    dur = re.search(r"Duration: (\d+):(\d+):([\d.]+)", err)
    if not (size and fps and dur):
        sys.exit(f"could not read size, frame rate and duration from {clip}")
    h, m, s = dur.groups()
    return int(size.group(1)), int(size.group(2)), float(fps.group(1)), int(h) * 3600 + int(m) * 60 + float(s), "Audio:" in err


def launch(p, gpu):
    """gpu: False for Chromium's default rasteriser, True for this platform's usual GPU flags,
    or a list of flags (the ones --tune found to work here)."""
    extra = gpu if isinstance(gpu, list) else PLATFORM_GPU.get(sys.platform, []) if gpu else None
    return p.chromium.launch(args=COMMON + (GPU + extra if extra is not None else []))


def open_page(p, url, w, h, gpu=True, transparent=False):
    b = launch(p, gpu)
    pg = b.new_page(viewport={"width": w, "height": h})
    errors = []
    pg.on("pageerror", lambda e: errors.append(str(e)))
    pg.goto(url)
    pg.evaluate("window.ready || document.fonts.ready")
    pg.evaluate("document.fonts.ready")
    if not pg.evaluate("typeof window.render === 'function'"):
        b.close()
        sys.exit("the page has no window.render(t)" + (f"; its script failed with: {errors[0]}" if errors else ""))
    cdp = pg.context.new_cdp_session(pg)
    if transparent:  # the page must leave html and body without a background of their own
        cdp.send("Emulation.setDefaultBackgroundColorOverride", {"color": {"r": 0, "g": 0, "b": 0, "a": 0}})
    return b, pg, cdp


def renderer_name(pg):
    return pg.evaluate("""(() => { const c = document.createElement('canvas').getContext('webgl');
      const d = c && c.getExtension('WEBGL_debug_renderer_info');
      return d ? c.getParameter(d.UNMASKED_RENDERER_WEBGL) : 'unknown'; })()""")


def grab(cdp, t, fmt, clip=None):
    r = cdp.send("Runtime.evaluate", {"expression": f"window.render({t!r})", "awaitPromise": True})
    if "exceptionDetails" in r:  # a frame the page could not draw must stop the render, not ship as a stale picture
        d = r["exceptionDetails"]
        raise RuntimeError(f"window.render({t:g}) threw: {d.get('exception', {}).get('description') or d.get('text')}")
    opts = {"format": fmt, "optimizeForSpeed": True}
    if fmt == "jpeg":
        opts["quality"] = 100
    if clip:
        opts["clip"] = clip
    return base64.b64decode(cdp.send("Page.captureScreenshot", opts)["data"])


def scaled(w, h, scale):
    """A capture clip that re-rasterises the page at `scale`: the page keeps its own layout size
    and the frame comes out sharper, not stretched. (A device pixel ratio set on the page did
    not change the captured size in testing; the clip scale did: 1920x1080 -> 3840x2160.)"""
    return {"x": 0, "y": 0, "width": w, "height": h, "scale": scale} if scale != 1 else None


def warm(cdp, fmt, dur=None):
    """Paint sample frames across the whole timeline before capturing anything.
    Chromium paints a font face lazily: the first frame that uses a new face comes out
    without its text (measured: 0 text pixels, then 2,211 on the next capture of the same
    frame). Visiting frames from every part of the video first puts every face in use."""
    if not dur:
        dur = cdp.send("Runtime.evaluate", {"expression": "window.DURATION || 0", "returnByValue": True})["result"].get("value") or 0
    for k in range(25):
        grab(cdp, (dur * k / 24) if dur else 0.0, fmt)


def capture(job):
    url, w, h, fps, fmt, lo, hi, seg, poster_t, ff, gpu, scale, transparent = job
    from playwright.sync_api import sync_playwright
    # stream-copy frames into the segment: no encoding while the GPU rasterises
    # (12 concurrent NVENC sessions during capture cut throughput from ~45 to ~17 fps)
    enc = subprocess.Popen([ff, "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", f"{fps:g}",
                            "-c:v", "mjpeg" if fmt == "jpeg" else "png", "-i", "-", "-c:v", "copy", seg],
                           stdin=subprocess.PIPE)
    with sync_playwright() as p:
        b, pg, cdp = open_page(p, url, w, h, gpu, transparent)
        warm(cdp, fmt)  # warm-up: shaders and every font face
        clip = scaled(w, h, scale)
        for i in range(lo, hi):
            enc.stdin.write(grab(cdp, poster_t if (i == 0 and poster_t is not None) else i / fps, fmt, clip))
        b.close()
    enc.stdin.close()
    if enc.wait() != 0:
        raise RuntimeError(f"segment writer failed: {seg}")
    return hi - lo


def audit(cdp, dur, w, h, step, still, mask_bottom):
    """Measure how much of the picture changes, to catch a video that plays like a slideshow.
    Every `step` seconds a small greyscale frame is compared with the one before; activity is
    the share of pixels that changed clearly (by more than 24/255). A sample under 1% is quiet:
    at most a slow drift or a caret blinking. The bottom `mask_bottom` of the frame is left out
    so burned-in captions do not pass for action.

    Calibration, four videos judged by one viewer: two called "a slide show" measured a median
    of 0.9% and 1.3% with 52% and 42% of the time quiet; a cursor-driven demo recut until it
    no longer dragged measured 6.9% and 5%. Treat the verdict as a prompt to look, not a score."""
    try:
        from PIL import Image, ImageChops
    except ImportError:
        sys.exit("--audit needs Pillow: pip install pillow")
    import io
    clip = {"x": 0, "y": 0, "width": w, "height": int(h * (1 - mask_bottom)), "scale": 320 / w}
    prev, act = None, []
    for k in range(int(dur / step) + 1):
        im = Image.open(io.BytesIO(grab(cdp, min(k * step, dur), "png", clip))).convert("L")
        if prev is not None:
            act.append(100 * sum(ImageChops.difference(im, prev).histogram()[25:]) / (im.width * im.height))
        prev = im
    runs, start = [], None
    for k, v in enumerate(act + [100]):
        if v < 1 and start is None:
            start = k
        elif v >= 1 and start is not None:
            if (k - start) * step >= still:
                runs.append((start * step, k * step))
            start = None
    median = sorted(act)[len(act) // 2]; quiet = 100 * sum(v < 1 for v in act) / len(act)
    verdict = "plays like a slideshow" if quiet >= 35 else "lively" if quiet <= 15 else "mixed: check the quiet stretches"
    print(f"audit: median activity {median:.1f}% of pixels per {step}s, quiet {quiet:.0f}% of the time -> {verdict}")
    for s, e in runs:
        tail = "  (ends the video: fine if it is the held end card)" if e >= dur - step else ""
        print(f"audit: quiet {s:6.2f}s -> {e:6.2f}s  ({e - s:.2f}s){tail}")
    if not runs:
        print(f"audit: no quiet stretch of {still}s or longer")
    return median, quiet, runs


def ram_gb():
    try:
        if sys.platform == "win32":
            import ctypes
            class Mem(ctypes.Structure):
                _fields_ = [("size", ctypes.c_ulong), ("load", ctypes.c_ulong)] + [(n, ctypes.c_ulonglong) for n in "abcdefg"]
            m = Mem(); m.size = ctypes.sizeof(m); ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m))
            return m.a / 2 ** 30
        return os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES") / 2 ** 30
    except Exception:
        return None


def cpu_busy(sample=0.6):
    """Share of the CPU already in use (0..1), or None when it cannot be read. Measuring a busy
    machine saves the wrong settings: the first tuning run on the author's laptop happened while
    another render was going and recorded 9 frames/s where the idle machine does about 45."""
    try:
        if sys.platform == "win32":
            import ctypes
            def times():
                i, k, u = (ctypes.c_ulonglong() for _ in range(3))
                ctypes.windll.kernel32.GetSystemTimes(ctypes.byref(i), ctypes.byref(k), ctypes.byref(u))
                return i.value, k.value + u.value                    # kernel time includes idle time
        elif sys.platform.startswith("linux"):
            def times():
                v = [int(x) for x in open("/proc/stat").readline().split()[1:]]
                return v[3] + v[4], sum(v)
        else:
            return min(1.0, os.getloadavg()[0] / (os.cpu_count() or 1))
        i0, t0 = times(); time.sleep(sample); i1, t1 = times()
        return 1 - (i1 - i0) / max(1, t1 - t0)
    except Exception:
        return None


BUSY = 0.30   # above this share of CPU in use, do not measure
ADVICE = "restart the computer or close heavy applications (other renders, games, video calls, big builds), then run fastrender.py --tune"


def fingerprint(rend):
    return {"platform": sys.platform, "cores": os.cpu_count() or 4, "renderer": rend}


def load_tune(rend=None):
    """Saved settings for this machine: the entry for this renderer when it is known, otherwise
    the most recent entry (its GPU flags are needed before any renderer can be read)."""
    try:
        runs = [r for r in json.loads(TUNE_FILE.read_text()) if r.get("v") == TUNE_V
                and r["fingerprint"]["platform"] == sys.platform and r["fingerprint"]["cores"] == (os.cpu_count() or 4)]
    except (OSError, ValueError, KeyError, TypeError, AttributeError):
        return None
    if rend is not None:
        runs = [r for r in runs if r["fingerprint"]["renderer"] == rend]
    return runs[-1] if runs else None


def bench_capture(job):
    """One browser drawing the benchmark page; returns its frames per second inside the capture loop."""
    url, frames, seg, ff, gpu = job
    from playwright.sync_api import sync_playwright
    enc = subprocess.Popen([ff, "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", "30", "-c:v", "mjpeg",
                            "-i", "-", "-c:v", "copy", seg], stdin=subprocess.PIPE)
    with sync_playwright() as p:
        b, pg, cdp = open_page(p, url, 1920, 1080, gpu)
        for k in range(6):
            grab(cdp, k / 30, "jpeg")
        t0 = time.perf_counter()
        for i in range(frames):
            enc.stdin.write(grab(cdp, i / 30, "jpeg"))
        dt = time.perf_counter() - t0
        b.close()
    enc.stdin.close(); enc.wait()
    return frames / dt


def tune(ff):
    """Measure this machine and save what a render should use here. Three questions, each answered
    by trying it: which GPU flags give a hardware renderer, how many parallel browsers until capture
    stops getting faster, and how many encoder sessions the hardware accepts and benefits from.
    The smallest setting within 5% of the best is kept, since extra browsers only cost memory."""
    from playwright.sync_api import sync_playwright
    busy = cpu_busy()
    if busy is not None and busy > BUSY:
        print(f"tune: this machine is busy ({busy:.0%} of the CPU in use), so nothing was measured or saved.\n"
              f"      {ADVICE[0].upper() + ADVICE[1:]}.")
        return None
    cpu, t_start = os.cpu_count() or 4, time.perf_counter()
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="fastrender_tune_"))
    try:
        page = tmp / "bench.html"; page.write_text(BENCH, encoding="utf-8"); url = page.as_uri()
        gpu, rend = False, "unknown"
        with sync_playwright() as p:
            for flags in GPU_TRY.get(sys.platform, [[]]):
                try:
                    b = launch(p, flags); r = renderer_name(b.new_page()); b.close()
                except Exception:
                    continue
                rend = r
                if r != "unknown" and not any(x in r for x in SOFTWARE):
                    gpu = flags; break
        print(f"tune: renderer {rend}" + ("" if gpu is not False else "  (no GPU rasteriser found: frames will be slow)"))

        ram = ram_gb(); top = max(2, min(16, cpu, int(ram) if ram else 16))      # a browser needs most of a gigabyte
        cap_fps, best = {}, None
        for w in sorted({max(2, min(top, c)) for c in (cpu // 4, cpu // 2, cpu * 3 // 4, cpu)}):
            with ProcessPoolExecutor(w) as ex:
                fps = sum(ex.map(bench_capture, [(url, 24, str(tmp / f"b{w}_{k}.mkv"), ff, gpu) for k in range(w)]))
            cap_fps[w] = round(fps, 1); print(f"tune: {w:2d} browsers          -> {fps:6.1f} frames/s captured")
            if best and fps < cap_fps[best] * 1.05:
                break                                                             # past the knee
            best = w
        workers = min(w for w, f in cap_fps.items() if f >= max(cap_fps.values()) * .95)

        encoder, enc_fps, encode_jobs = pick_encoder(ff, "auto"), {}, None
        if encoder != "libx264":                                                  # x264 uses one process per segment already
            test = str(tmp / "test.mkv")
            subprocess.run([ff, "-y", "-loglevel", "error", "-stream_loop", "7", "-i", str(tmp / f"b{best}_0.mkv"), "-c", "copy", test], check=True)
            one = None                                                            # seconds for a single session
            for j in [c for c in (1, 2, 4, 8, 12, 16) if c <= max(2, cpu)]:
                t0 = time.perf_counter()
                ps = [subprocess.Popen([ff, "-y", "-loglevel", "error", "-i", test, "-vf", TV, "-c:v", encoder, *ENCODERS[encoder],
                                        "-an", "-f", "null", "-"], stderr=subprocess.DEVNULL) for _ in range(j)]
                try:  # j sessions that gain nothing take j times as long; well past that, the hardware has stalled
                    limit = t0 + (one or 60) * j * 1.5 + 10
                    ok = all([q.wait(timeout=max(1, limit - time.perf_counter())) == 0 for q in ps])
                except subprocess.TimeoutExpired:
                    ok = False
                    for q in ps:
                        q.kill(); q.wait()
                if not ok:  # 16 sessions at once never finished on the author's laptop
                    print(f"tune: {j:2d} encoder sessions  -> refused or stalled"); break
                dt = time.perf_counter() - t0; one = one or dt
                enc_fps[j] = round(192 * j / dt, 1)
                print(f"tune: {j:2d} encoder sessions  -> {enc_fps[j]:6.1f} frames/s encoded")
                if enc_fps[j] < max(enc_fps.values()) * 1.05 and j > 1 and enc_fps[j] < max(enc_fps.values()):
                    break                                                         # past the knee
            if enc_fps:
                encode_jobs = min(j for j, f in enc_fps.items() if f >= max(enc_fps.values()) * .95)

        out = {"v": TUNE_V, "fingerprint": fingerprint(rend), "gpu_args": gpu if gpu is not False else None, "workers": workers,
               "encode_jobs": encode_jobs, "encoder": encoder, "measured": {"capture_fps": cap_fps, "encode_fps": enc_fps},
               "tuned_at": time.strftime("%Y-%m-%d"), "seconds": round(time.perf_counter() - t_start)}
        try:
            old = [r for r in json.loads(TUNE_FILE.read_text()) if r.get("fingerprint") != out["fingerprint"]]
        except (OSError, ValueError, AttributeError):
            old = []
        TUNE_FILE.parent.mkdir(parents=True, exist_ok=True)
        TUNE_FILE.write_text(json.dumps((old + [out])[-4:], indent=1))
        print(f"tune: {workers} browsers, {encode_jobs or 'one per segment'} encoder sessions, {encoder}; saved to {TUNE_FILE} ({out['seconds']} s)")
        return out
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def doctor():
    """Report what this machine can do, in plain words. Changes nothing."""
    ok = lambda b: "ok     " if b else "MISSING"
    has = lambda m: importlib.util.find_spec(m) is not None
    print(f"python          {sys.version.split()[0]}  ({'ok' if sys.version_info >= (3, 9) else 'needs 3.9+'})")
    ff = None
    try:
        ff = ffmpeg_exe(); print(f"ffmpeg          ok      {ff}")
    except SystemExit:
        print("ffmpeg          MISSING  pip install imageio-ffmpeg")
    if ff:
        good = [n for n in ENCODERS if encoder_works(ff, n)]
        print(f"h264 encoders   {', '.join(good) or 'none'}  (first one is used)")
        pr = subprocess.run([ff, "-v", "error", "-f", "lavfi", "-i", "color=c=gray:s=64x64:d=0.1", *PRORES, "-f", "null", "-"], capture_output=True).returncode == 0
        print(f"prores 4444     {ok(pr)} (needed for --transparent .mov)")
    if not has("playwright"):
        print("playwright      MISSING  pip install playwright && playwright install chromium")
    else:
        from playwright.sync_api import sync_playwright
        try:
            with sync_playwright() as p:
                b = launch(p, True); pg = b.new_page(); rend = renderer_name(pg); b.close()
            cpu = "SwiftShader" in rend or "llvmpipe" in rend
            print(f"chromium        ok      renderer: {rend}")
            print(f"gpu rasteriser  {'NO: frames will be about 10x slower; check GPU drivers' if cpu else 'yes'}")
        except Exception as e:
            print(f"chromium        MISSING  playwright install chromium   ({str(e)[:70]})")
    t = load_tune()
    print("tuned           " + (f"yes     {t['workers']} browsers, {t['encode_jobs'] or 'one per segment'} encoder sessions, {t['encoder']} ({t['tuned_at']}); run --tune again after a GPU or driver change"
                                if t else f"no      renders use safe defaults. To calibrate (a minute or two, once): {ADVICE}"))
    print(f"pillow          {ok(has('PIL'))} (for --audit)")
    print(f"narration       {ok(has('kokoro_onnx') and has('soundfile'))} (narrate skill: pip install kokoro-onnx soundfile)")
    print(f"transcription   {ok(has('faster_whisper') or has('whisper'))} (transcribe script: pip install faster-whisper)")
    print(f"sound kit       {ok(has('numpy') and has('scipy'))} (motion-kit soundkit: pip install numpy scipy)")


def main():
    cpu = os.cpu_count() or 4
    sys.stdout.reconfigure(line_buffering=True)   # progress line by line, also when the output is piped
    ap = argparse.ArgumentParser(description="Render a window.render(t) page to video, fast.")
    ap.add_argument("page", nargs="?")
    ap.add_argument("--out", default="brag.mp4")
    ap.add_argument("--fps", type=float, default=30)
    ap.add_argument("--duration", type=float, help="seconds; defaults to window.DURATION")
    ap.add_argument("--width", type=int, default=1920)
    ap.add_argument("--height", type=int, default=1080)
    ap.add_argument("--scale", type=float, default=1, help="render sharper than the page size: 2 turns a 1920x1080 page into 3840x2160")
    ap.add_argument("--workers", type=int, help="parallel browsers (default: what --tune measured, else 3/4 of the cores, up to 12)")
    ap.add_argument("--encode-jobs", type=int, help="parallel encoder sessions (default: what --tune measured, else 4)")
    ap.add_argument("--tune", action="store_true", help="calibrate for this machine and save the settings; run it on an idle machine")
    ap.add_argument("--no-tune", action="store_true", help="ignore saved settings")
    ap.add_argument("--capture", choices=["jpeg", "png"], default="jpeg",
                    help="jpeg q100 is visually lossless and ~40%% faster; png for fine gradients")
    ap.add_argument("--encoder", choices=["auto", *ENCODERS], default="auto")
    ap.add_argument("--crf", type=int, help="quality, lower is better (default 14-18 by encoder); 23 roughly halves the file")
    ap.add_argument("--no-gpu", action="store_true", help="force CPU rasterisation (debugging)")
    ap.add_argument("--audio")
    ap.add_argument("--lufs", type=float, default=-16, help="loudness target for --audio (-14 for YouTube)")
    ap.add_argument("--poster", type=float, help="t (s) of the settled frame baked in as frame 0")
    ap.add_argument("--poster-jpg", help="also save that frame as a JPEG")
    ap.add_argument("--stills", type=float, nargs="*", help="only save PNG stills at these times")
    ap.add_argument("--still-dir", default="stills")
    ap.add_argument("--transparent", action="store_true", help="keep alpha: --out must be .mov (ProRes 4444)")
    ap.add_argument("--png-dir", help="with --transparent, also write a PNG sequence here")
    ap.add_argument("--over", help="footage to lay the page over; size, frame rate, length and audio come from it")
    ap.add_argument("--dump-sfx", help="write window.SFX and window.MARKS to this JSON file and exit")
    ap.add_argument("--audit", action="store_true", help="measure on-screen activity and list quiet stretches, then exit")
    ap.add_argument("--audit-still", type=float, default=1.5, help="seconds of quiet that are worth listing")
    ap.add_argument("--audit-mask-bottom", type=float, default=0.14, help="fraction of the frame bottom to ignore (captions)")
    ap.add_argument("--doctor", action="store_true", help="report what is installed and whether the GPU is used")
    ap.add_argument("--keep", action="store_true", help="keep intermediate segments")
    a = ap.parse_args()
    if a.doctor:
        return doctor()
    if a.tune:
        done = tune(ffmpeg_exe())
        if not a.page:
            sys.exit(0 if done else 1)
    if not a.page:
        ap.error("page is required")

    url = pathlib.Path(a.page).resolve().as_uri()
    ff = ffmpeg_exe()
    saved = None if a.no_tune else load_tune()
    gpu = False if a.no_gpu else saved["gpu_args"] if saved and saved.get("gpu_args") is not None else True
    clip_audio = False
    if a.over:  # the footage decides the canvas; the page only adds graphics
        a.width, a.height, a.fps, clip_dur, clip_audio = probe(ff, a.over)
        a.duration = a.duration or clip_dur
        a.transparent = True
    if a.transparent:
        a.capture = "png"
        if not a.over and not a.out.lower().endswith(".mov"):
            sys.exit("--transparent writes ProRes 4444: use an --out ending in .mov")
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        try:
            b, pg, cdp = open_page(p, url, a.width, a.height, gpu, a.transparent)
        except Exception as e:  # a GPU flag this platform rejects: fall back rather than fail
            print(f"GPU launch failed ({str(e)[:80]}); falling back to default rasteriser")
            gpu = False
            b, pg, cdp = open_page(p, url, a.width, a.height, gpu, a.transparent)
        rend = renderer_name(pg)
        dur = a.duration or pg.evaluate("window.DURATION || 0")
        if a.dump_sfx:
            data = pg.evaluate("({dur: window.DURATION || 0, events: window.SFX || [], marks: window.MARKS || {}})")
            pathlib.Path(a.dump_sfx).write_text(json.dumps(data))
            print(f"{len(data['events'])} sound cues -> {a.dump_sfx}")
        if a.stills or a.poster_jpg or a.audit:
            warm(cdp, "jpeg", dur)
        if a.poster_jpg and a.poster is not None:
            pathlib.Path(a.poster_jpg).write_bytes(grab(cdp, a.poster, "jpeg", scaled(a.width, a.height, a.scale)))
        if a.stills:
            d = pathlib.Path(a.still_dir); d.mkdir(parents=True, exist_ok=True)
            for t in a.stills:
                (d / f"t{t:07.2f}.png").write_bytes(grab(cdp, t, "png", scaled(a.width, a.height, a.scale)))
                print(f"still t={t}s -> {d / f't{t:07.2f}.png'}")
        if a.audit:
            if not dur:
                sys.exit("no duration: pass --duration or set window.DURATION")
            audit(cdp, dur, a.width, a.height, 0.25, a.audit_still, a.audit_mask_bottom)
        b.close()
    print(f"renderer: {rend}")
    if "SwiftShader" in rend:
        print("WARNING: CPU rasteriser (SwiftShader) in use; expect roughly 10x slower frames")
    if a.stills is not None or a.audit or a.dump_sfx:
        if a.stills is not None:
            print(f"stills -> {a.still_dir}")
        return
    if not dur:
        sys.exit("no duration: pass --duration or set window.DURATION")

    saved = None if a.no_tune else load_tune(rend)      # settings measured for this very renderer, if any
    workers = a.workers or (saved or {}).get("workers") or max(2, min(12, cpu * 3 // 4))
    encode_jobs = a.encode_jobs or (saved or {}).get("encode_jobs") or 4
    encoder = saved["encoder"] if a.encoder == "auto" and saved and encoder_works(ff, saved["encoder"]) else pick_encoder(ff, a.encoder)
    print("settings: " + (f"calibrated for this machine on {saved['tuned_at']}" if saved else "safe defaults" if a.no_tune
                          else f"safe defaults, not calibrated. For full speed, once: {ADVICE}"))
    # a browser costs ~2 s to start, so give each one 60+ frames
    n = int(round(dur * a.fps)); W = max(1, min(workers, n // 60)); step = -(-n // W)
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="fastrender_", dir=pathlib.Path(a.out).resolve().parent))
    jobs = [(url, a.width, a.height, a.fps, a.capture, lo, min(n, lo + step), str(tmp / f"seg{k:03d}.mkv"),
             a.poster if k == 0 else None, ff, gpu, a.scale, a.transparent) for k, lo in enumerate(range(0, n, step))]
    mode = "over footage" if a.over else "transparent" if a.transparent else encoder
    print(f"{n} frames @ {a.fps:g} fps, {int(a.width * a.scale)}x{int(a.height * a.scale)}, {len(jobs)} browsers, capture={a.capture}, {mode}")

    t0 = time.perf_counter()
    with ProcessPoolExecutor(len(jobs)) as ex:
        frames = sum(ex.map(capture, jobs))
    cap = time.perf_counter() - t0
    print(f"captured {frames} frames in {cap:.1f}s = {frames / cap:.1f} fps")

    t1 = time.perf_counter()
    lst = tmp / "list.txt"
    gop = ["-g", str(max(1, int(round(a.fps * 2))))]
    loud = ["-c:a", "aac", "-b:a", "256k", "-af", f"loudnorm=I={a.lufs:g}:TP=-1.5", "-ar", "48000"]

    if a.over:
        # One pass: footage underneath, the transparent segments on top. The clip's own audio is
        # kept; --audio (sound effects) is mixed under it without touching its level.
        lst.write_text("".join(f"file '{j[7]}'\n" for j in jobs))
        cmd = [ff, "-y", "-loglevel", "error", "-i", a.over, "-f", "concat", "-safe", "0", "-i", str(lst)]
        graph = f"[0:v][1:v]overlay=format=auto:shortest=1,{TV}[v]"
        maps = ["-map", "[v]"]
        if a.audio and clip_audio:
            cmd += ["-i", a.audio]
            graph += ";[0:a][2:a]amix=inputs=2:duration=first:normalize=0[a]"
            maps += ["-map", "[a]", "-c:a", "aac", "-b:a", "256k"]
        elif a.audio:
            cmd += ["-i", a.audio]; maps += ["-map", "2:a", *loud]
        elif clip_audio:
            maps += ["-map", "0:a", "-c:a", "copy"]
        cmd += ["-filter_complex", graph, *maps, "-c:v", encoder, *encoder_args(encoder, a.crf), *gop, *TAGS,
                "-movflags", "+faststart", a.out]
        subprocess.run(cmd, check=True)
    else:
        # Encode segments in parallel: decode and the range conversion are single-threaded per
        # ffmpeg process, so one process per segment keeps the cores and the encoder busy.
        jobs_n = len(jobs) if (encoder == "libx264" or a.transparent) else max(1, min(encode_jobs, len(jobs)))
        if a.transparent:
            ext, vargs = ".mov", PRORES
        else:
            ext, vargs = ".mp4", ["-vf", TV, "-c:v", encoder, *encoder_args(encoder, a.crf), *gop, *TAGS]
            if encoder == "libx264":
                vargs += ["-threads", str(max(1, cpu // len(jobs)))]

        def encode(j):
            out = j[7].replace(".mkv", ext)
            subprocess.run([ff, "-y", "-loglevel", "error", "-i", j[7], *vargs, "-an", out], check=True)
            return out

        with ThreadPoolExecutor(jobs_n) as ex:
            outs = list(ex.map(encode, jobs))
        print(f"encoded {len(outs)} segments in {time.perf_counter() - t1:.1f}s ({jobs_n} at a time)")

        lst.write_text("".join(f"file '{o}'\n" for o in outs))
        cmd = [ff, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst)]
        if a.audio:
            cmd += ["-i", a.audio]
        cmd += ["-c:v", "copy"]
        if not a.transparent:  # concat drops the colour tags; restore them without re-encoding
            cmd += ["-bsf:v", "h264_metadata=colour_primaries=1:transfer_characteristics=13:matrix_coefficients=6:video_full_range_flag=0"]
        if a.audio:
            cmd += [*loud, "-shortest"]
        cmd += ["-movflags", "+faststart", a.out]
        subprocess.run(cmd, check=True)
        if a.png_dir and a.transparent:
            d = pathlib.Path(a.png_dir); d.mkdir(parents=True, exist_ok=True)
            for j in jobs:  # the segments already hold PNG frames: copy them out, no re-encode
                subprocess.run([ff, "-y", "-loglevel", "error", "-i", j[7], "-c:v", "copy", "-start_number", str(j[5]),
                                str(d / "frame_%06d.png")], check=True)
            print(f"png sequence -> {a.png_dir}")
    if not a.keep:
        shutil.rmtree(tmp, ignore_errors=True)
    print(f"wrote {a.out} in {time.perf_counter() - t0:.1f}s total")


if __name__ == "__main__":
    main()
