"""Fit scenes to the narration, on a beat grid, and write the layout the page reads.

A video is timed to its voice, not the other way round. Describe the scenes once:

    {"bpm": 110, "snap": 2,
     "scenes": [{"id": "hook", "lines": ["Monday, nine A.M. Three reports."], "lead": 0.6},
                {"id": "fix",  "lines": ["Reports write themselves."], "beats": 8},
                {"id": "end",  "lines": ["Ask for a demo."], "hold": 3.2}]}

then run it twice around the `narrate` skill:

    python fit_scenes.py scenes.json --probe            # writes probe.json: every line, spaced apart
    python <narrate>/scripts/narrate.py probe.json --timings probe_timings.json --out probe.wav
    python fit_scenes.py scenes.json                    # writes script.json and layout.js
    python <narrate>/scripts/narrate.py script.json     # the real narration, lines already cached

Per scene: `lead` seconds before its first line (default 0.4), `gap` between lines (0.45),
`tail` after the last (0.3), `hold` extra time at the end (an end card), `min` seconds, and
`beats` to force an exact length in beats. With `bpm` set, every scene is rounded up to a
multiple of `snap` beats (default 2), so each scene starts on a beat and the music never
needs cutting. A scene with no lines takes `dur` seconds.

Without probe timings, lines are estimated at 2.7 words a second and a warning is printed:
fine for a first layout, not for the final render.

layout.js sets window.LAYOUT = {scenes: {id: {t0, t1, lines: [{t, dur, text}]}}, order, dur, beat}.
"""
import argparse, json, math, pathlib, sys


def main():
    ap = argparse.ArgumentParser(description="Fit scenes to narration on a beat grid.")
    ap.add_argument("spec")
    ap.add_argument("--probe", action="store_true", help="write probe.json for narrate, then stop")
    ap.add_argument("--timings", default="probe_timings.json")
    ap.add_argument("--out-dir", default=".")
    a = ap.parse_args()
    spec = json.loads(pathlib.Path(a.spec).read_text(encoding="utf-8")); out = pathlib.Path(a.out_dir)
    lines = [tx for sc in spec["scenes"] for tx in sc.get("lines", [])]
    if a.probe:
        (out / "probe.json").write_text(json.dumps([{"t": i * 14.0, "text": tx} for i, tx in enumerate(lines)], indent=1), encoding="utf-8")
        print(f"{len(lines)} lines -> {out / 'probe.json'}"); return
    tim = pathlib.Path(a.timings)
    if tim.exists():
        dur = {x["text"]: x["dur"] for x in json.loads(tim.read_text(encoding="utf-8"))}
        missing = [tx for tx in lines if tx not in dur]
        if missing:
            sys.exit(f"{len(missing)} line(s) are not in {tim} (edited since the probe?): {missing[0][:60]!r}. Run --probe and narrate again.")
    else:
        print(f"WARNING: no {tim}; estimating line lengths at 2.7 words a second")
        dur = {tx: len(tx.split()) / 2.7 for tx in lines}
    beat = 60 / spec["bpm"] if spec.get("bpm") else None
    snap = spec.get("snap", 2)
    t, scenes, script = 0.0, {}, []
    for sc in spec["scenes"]:
        t0, placed = t, []
        u = t0 + sc.get("lead", .4)
        for k, tx in enumerate(sc.get("lines", [])):
            placed.append({"t": round(u, 3), "dur": round(dur[tx], 3), "text": tx}); script.append({"t": round(u, 3), "text": tx})
            u += dur[tx] + (sc.get("gap", .45) if k < len(sc["lines"]) - 1 else 0)
        need = (u - t0 + sc.get("tail", .3) + sc.get("hold", 0)) if placed else sc.get("dur", 2.0)
        need = max(need, sc.get("min", 0))
        if beat and sc.get("beats"):
            if need > sc["beats"] * beat + 1e-6:
                print(f"WARNING: scene {sc['id']} needs {need:.2f}s but {sc['beats']} beats is {sc['beats'] * beat:.2f}s: shorten its line")
            need = sc["beats"] * beat
        elif beat:
            need = math.ceil(need / (snap * beat) - 1e-9) * snap * beat
        scenes[sc["id"]] = {"t0": round(t0, 3), "t1": round(t0 + need, 3), "lines": placed}; t = t0 + need
    (out / "script.json").write_text(json.dumps(script, indent=1), encoding="utf-8")
    layout = {"scenes": scenes, "order": [sc["id"] for sc in spec["scenes"]], "dur": round(t, 3), "beat": beat}
    (out / "layout.js").write_text("window.LAYOUT = " + json.dumps(layout) + ";", encoding="utf-8")
    print(f"{len(scenes)} scenes, {t:.2f}s" + (f", beat {beat:.4f}s" if beat else ""))
    for sid, v in scenes.items():
        print(f"  {sid:12s} {v['t0']:7.2f} -> {v['t1']:7.2f}")


if __name__ == "__main__":
    main()
