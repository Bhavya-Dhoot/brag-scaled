"""Offline narration for brag videos: Kokoro-82M TTS -> timed voice track -> ducked mix.

Script format (JSON): [{"t": 0.6, "text": "Your AI demo works on stage."}, ...]
  t     start time in seconds on the video timeline
  text  one line of narration

Usage:
  python narrate.py script.json --voice af_heart            # narration.wav + timings.json
  python narrate.py script.json --music score.wav --mix final.wav
  python narrate.py --list-voices

Timings: every line's real duration and end are written to timings.json, and any line
that runs into the next one is reported, so scene lengths can be fitted to the voice
before the render. Lines are cached by (text, voice, speed, model), so re-running after
retiming only moves audio and never re-synthesises it.

The model downloads once from this repo's `tts-v1` release (SHA-256 checked) into
~/.cache/brag-scaled/kokoro, or $BRAG_SCALED_CACHE. Requires: pip install kokoro-onnx soundfile imageio-ffmpeg
"""
import argparse, hashlib, json, os, pathlib, shutil, subprocess, sys, urllib.request

RELEASE = "https://github.com/Bhavya-Dhoot/brag-scaled/releases/download/tts-v1/"
FILES = {
    # fp32 is the default: on the reference CPU (i9-11950H) it synthesises at 0.79x real
    # time, while the int8 build ran at 2.9x (slower than playback), despite being smaller.
    "fp32": ("kokoro-v1.0.onnx", "7d5df8ecf7d4b1878015a32686053fd0eebe2bc377234608764cc0ef3636a6c5"),
    "int8": ("kokoro-v1.0.int8.onnx", "6e742170d309016e5891a994e1ce1559c702a2ccd0075e67ef7157974f6406cb"),
}
VOICES = ("voices-v1.0.bin", "bca610b8308e8d99f32e6fe4197e7ec01679264efed0cac9140fe9c29f1fbf7d")
SR = 24000


def cache_dir():
    d = pathlib.Path(os.environ.get("BRAG_SCALED_CACHE", pathlib.Path.home() / ".cache" / "brag-scaled")) / "kokoro"
    d.mkdir(parents=True, exist_ok=True)
    return d


def fetch(name, sha):
    path = cache_dir() / name
    if path.exists() and sha256(path) == sha:
        return path
    tmp = path.with_suffix(path.suffix + ".part")
    print(f"downloading {name} (once) ...", file=sys.stderr)
    with urllib.request.urlopen(RELEASE + name) as r, open(tmp, "wb") as f:
        shutil.copyfileobj(r, f, 1 << 20)
    if sha256(tmp) != sha:
        tmp.unlink()
        sys.exit(f"checksum mismatch for {name}; refusing to use it")
    tmp.replace(path)
    return path


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def ffmpeg_exe():
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        return shutil.which("ffmpeg") or sys.exit("ffmpeg not found: pip install imageio-ffmpeg")


def load(model):
    from kokoro_onnx import Kokoro
    name, sha = FILES[model]
    return Kokoro(str(fetch(name, sha)), str(fetch(*VOICES)))


def synth(tts, text, voice, speed, lang, model, cache):
    import numpy as np, soundfile as sf
    key = hashlib.sha1(f"{model}|{voice}|{speed}|{lang}|{text}".encode()).hexdigest()[:16]
    f = cache / f"{key}.wav"
    if f.exists():
        return sf.read(f, dtype="float32")[0]
    audio, sr = tts.create(text, voice=voice, speed=speed, lang=lang)
    assert sr == SR
    # trim the model's leading/trailing silence so timings mean what they say
    nz = np.flatnonzero(np.abs(audio) > 0.01)
    audio = audio[max(0, nz[0] - 240): nz[-1] + 1200] if len(nz) else audio
    sf.write(f, audio, SR)
    return audio


def main():
    ap = argparse.ArgumentParser(description="Narrate a brag video offline with Kokoro-82M.")
    ap.add_argument("script", nargs="?", help="JSON list of {t, text}")
    ap.add_argument("--voice", default="af_heart", help="see --list-voices; af_/am_ US, bf_/bm_ UK")
    ap.add_argument("--speed", type=float, default=1.0)
    ap.add_argument("--lang", default="en-us")
    ap.add_argument("--model", choices=list(FILES), default="fp32", help="int8 is a smaller download but slower on most CPUs")
    ap.add_argument("--out", default="narration.wav")
    ap.add_argument("--timings", default="timings.json")
    ap.add_argument("--music", help="music/score to duck under the voice")
    ap.add_argument("--mix", default="mix.wav", help="output of --music mixing")
    ap.add_argument("--duck", type=float, default=0.02, help="sidechain threshold; lower ducks more")
    ap.add_argument("--list-voices", action="store_true")
    a = ap.parse_args()

    tts = load(a.model)
    if a.list_voices:
        print(" ".join(sorted(tts.get_voices())))
        return
    if not a.script:
        sys.exit("pass a script JSON (or --list-voices)")
    import numpy as np, soundfile as sf

    lines = sorted(json.loads(pathlib.Path(a.script).read_text(encoding="utf-8")), key=lambda x: x["t"])
    cache = pathlib.Path(a.out).resolve().parent / ".narration-cache"
    cache.mkdir(exist_ok=True)
    clips, out = [], []
    for ln in lines:
        audio = synth(tts, ln["text"], a.voice, a.speed, a.lang, a.model, cache)
        clips.append(audio)
        dur = len(audio) / SR
        out.append({"t": round(ln["t"], 3), "end": round(ln["t"] + dur, 3), "dur": round(dur, 3), "text": ln["text"]})
    for cur, nxt in zip(out, out[1:]):
        if cur["end"] > nxt["t"] - 0.15:
            print(f"OVERLAP: line at {cur['t']}s ends {cur['end']}s, next starts {nxt['t']}s "
                  f"(move it to >= {cur['end'] + 0.25:.2f}s or shorten)", file=sys.stderr)
    total = max(o["end"] for o in out) + 0.5
    track = np.zeros(int(total * SR), dtype="float32")
    for o, clip in zip(out, clips):
        i = int(o["t"] * SR)
        track[i:i + len(clip)] += clip
    peak = np.abs(track).max() or 1.0
    track *= 0.89 / peak
    sf.write(a.out, track, SR)
    pathlib.Path(a.timings).write_text(json.dumps(out, indent=1), encoding="utf-8")
    words = sum(len(o["text"].split()) for o in out)
    print(f"{len(out)} lines, {words} words, voice ends at {max(o['end'] for o in out):.2f}s -> {a.out}, {a.timings}")

    if a.music:
        ff = ffmpeg_exe()
        graph = ("[1:a]aresample=48000,aformat=channel_layouts=stereo,volume=1.4,asplit=2[v][sc0];"
                 "[sc0]apad[sc];"  # pad the key so the music keeps its full length after the last line
                 "[0:a]aresample=48000,aformat=channel_layouts=stereo[m];"
                 f"[m][sc]sidechaincompress=threshold={a.duck}:ratio=10:attack=15:release=400[duck];"
                 "[duck][v]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95")
        subprocess.run([ff, "-y", "-loglevel", "error", "-i", a.music, "-i", a.out,
                        "-filter_complex", graph, a.mix], check=True)
        print(f"mixed with ducked music -> {a.mix}")


if __name__ == "__main__":
    main()
