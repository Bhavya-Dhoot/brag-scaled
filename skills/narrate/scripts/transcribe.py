"""Word timings from a video or audio file, offline, for graphics that land on the exact word.

    python transcribe.py clip.mp4                 # writes clip.words.json and clip.words.js
    python transcribe.py clip.mp4 --find "40 a week"

Output: {"text": ..., "duration": s, "words": [{"w": "sales", "t0": 14.82, "t1": 15.10}, ...]}

Uses faster-whisper when it is installed, otherwise openai-whisper (either one:
`pip install faster-whisper`). The first run downloads the model (base: about 145 MB).
Speech-to-text timing can be off by a few tenths of a second, and by more on noisy clips:
check the words you build on with --find before placing a graphic on them.
"""
import argparse, importlib.util, json, pathlib, re, subprocess, sys, tempfile


def to_wav(src):
    """16 kHz mono WAV, so no system ffmpeg is needed on PATH."""
    import imageio_ffmpeg
    out = pathlib.Path(tempfile.mkdtemp(prefix="transcribe_")) / "audio.wav"
    subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), "-y", "-loglevel", "error", "-i", src, "-vn", "-ac", "1", "-ar", "16000", str(out)], check=True)
    return out


def load(wav):
    import numpy as np, wave
    with wave.open(str(wav)) as w:
        return np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype("float32") / 32768.0


def run(wav, model, lang):
    audio = load(wav)
    words = []
    if importlib.util.find_spec("faster_whisper"):
        from faster_whisper import WhisperModel
        segs, _ = WhisperModel(model, compute_type="int8").transcribe(audio, language=lang, word_timestamps=True)
        for s in segs:
            words += [(w.word, w.start, w.end) for w in s.words]
    elif importlib.util.find_spec("whisper"):
        import whisper
        res = whisper.load_model(model).transcribe(audio, language=lang, word_timestamps=True, fp16=False)
        for s in res["segments"]:
            words += [(w["word"], w["start"], w["end"]) for w in s.get("words", [])]
    else:
        sys.exit("no speech-to-text library: pip install faster-whisper")
    return [{"w": w.strip(), "t0": round(float(a), 2), "t1": round(float(b), 2)} for w, a, b in words if w.strip()], len(audio) / 16000


def find(words, phrase):
    """Every place the phrase is spoken, matched on letters and digits only."""
    norm = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())
    want = [norm(x) for x in phrase.split() if norm(x)]
    got = [norm(w["w"]) for w in words]
    return [(words[i]["t0"], words[i + len(want) - 1]["t1"]) for i in range(len(got) - len(want) + 1) if got[i:i + len(want)] == want]


def main():
    ap = argparse.ArgumentParser(description="Word timings from a clip, offline.")
    ap.add_argument("clip")
    ap.add_argument("--out", help="default: <clip>.words.json")
    ap.add_argument("--model", default="base", help="tiny, base, small, medium: bigger is slower and more exact")
    ap.add_argument("--lang", default=None, help="for example en; default is auto-detect")
    ap.add_argument("--find", help="print when this phrase is spoken")
    a = ap.parse_args()
    out = pathlib.Path(a.out or pathlib.Path(a.clip).with_suffix(".words.json"))
    if a.find and out.exists():
        data = json.loads(out.read_text(encoding="utf-8"))
    else:
        words, dur = run(to_wav(a.clip), a.model, a.lang)
        data = {"text": " ".join(w["w"] for w in words), "duration": round(dur, 2), "words": words}
        out.write_text(json.dumps(data, indent=1), encoding="utf-8")
        out.with_suffix(".js").write_text("window.WORDS = " + json.dumps(data) + ";", encoding="utf-8")  # for a page to load
        print(f"{len(words)} words over {dur:.1f}s -> {out}")
    if a.find:
        hits = find(data["words"], a.find)
        print("\n".join(f'"{a.find}" at {t0:.2f}s -> {t1:.2f}s' for t0, t1 in hits) or f'"{a.find}" not found; the transcript is: {data["text"]}')


if __name__ == "__main__":
    main()
