"""Sound for browser-rendered video, made entirely in code: no samples, no licences.

Three ways to use it.

1. Turn a page's sound cues into a track (the page lists them in window.SFX; get the JSON
   with `fastrender.py page.html --dump-sfx sfx.json`):

       python soundkit.py sfx.json --out sfx.wav
       python soundkit.py sfx.json --out score.wav --bed boombap --bpm 110
       python soundkit.py sfx.json --out score.wav --bed phonk --bpm 140 --t0 0.86 --tail 2.6

   The groove's downbeat is at --t0 (default 0) and it resolves --tail seconds before the
   end (default 2.5, for a held end card; 0.5 when the last scene runs to the end).

2. Write the standard sounds out as WAV files for an editor:

       python soundkit.py --pack sfx/

3. Import it and compose a score of your own:

       from soundkit import Mix, kick, marimba, pad, play_cues, hz

Cue format: {"t": seconds, "type": name, "x": optional number}. Names this file knows:
pop tick click thud stamp drop whoosh dive alert ding chime success confetti scribble type
count switch glitch brush final, and the louder set for a film that plays for laughs:
shatter slam crash boom lock ratchet motor ping cash coins payout squawk quack step.
`x` picks the pitch step for pop, tick, success and ping, and the length in seconds for
scribble and type.

Rule of thumb for levels: effects sit about 20 dB under a voice (`--peak -22` when the track
goes over someone speaking), and a click belongs on a thing that matters (a tick, a count,
the last card), not on every slide.

Requires: pip install numpy scipy
"""
import argparse, json, pathlib, sys, wave
import numpy as np
from scipy.signal import butter, lfilter

SR = 48000
rng = np.random.default_rng(7)
hz = lambda m: 440 * 2 ** ((m - 69) / 12)            # MIDI note number to frequency
tt = lambda d: np.arange(int(d * SR)) / SR
PENTA = [60, 62, 64, 67, 69, 72, 74, 76, 79, 81, 84, 86, 88, 91, 93]   # C major pentatonic: any two notes agree


def bp(x, lo, hi):
    b, a = butter(2, [lo / (SR / 2), min(hi, SR / 2 - 100) / (SR / 2)], "band"); return lfilter(b, a, x)


def lpf(x, f):
    b, a = butter(2, min(f, SR / 2 - 100) / (SR / 2)); return lfilter(b, a, x)


def noise(d):
    return rng.standard_normal(int(d * SR))


# ---------------------------------------------------------------- instruments
def kick(): t = tt(.32); return np.tanh(2 * np.sin(2*np.pi*np.cumsum(48 + 85*np.exp(-t*36))/SR)) * np.exp(-t*10)
def snare(): t = tt(.22); return .7*bp(noise(.22), 1200, 7000)*np.exp(-t*22) + .5*np.sin(2*np.pi*190*t)*np.exp(-t*30)
def clap(): t = tt(.18); return bp(noise(.18), 900, 4000) * (np.exp(-t*30) + .6*np.exp(-np.abs(t-.012)*220) + .5*np.exp(-np.abs(t-.024)*220))
def hat(d=.05): t = tt(d); return bp(noise(d), 6500, 12000) * np.exp(-t*80)
def rim(): t = tt(.06); return np.sin(2*np.pi*1700*t)*np.exp(-t*90) + .4*bp(noise(.06), 2000, 6000)*np.exp(-t*120)
def bass(f, d=.5): t = tt(d); return lpf(np.tanh(1.7*np.sin(2*np.pi*f*t)) + .3*np.sin(4*np.pi*f*t), 450) * np.exp(-t*2.8) * np.minimum(1, t/.008)
def marimba(f, d=.8): t = tt(d); return np.exp(-t*7) * (np.sin(2*np.pi*f*t) + .3*np.sin(8*np.pi*f*t)*np.exp(-t*30))
def pluck(f, d=.5): t = tt(d); return (np.sin(2*np.pi*f*t) + .35*np.sin(4*np.pi*f*t)*np.exp(-t*14) + .2*np.sin(6*np.pi*f*t)*np.exp(-t*30)) * np.exp(-t*8) * np.minimum(1, t/.003)
def piano(f, d=1.6): t = tt(d); return lpf(sum(a*np.sin(2*np.pi*f*k*t) for k, a in [(1, 1), (2, .5), (3, .22), (4, .1)]), 2200) * np.exp(-t*2.4) * np.minimum(1, t/.004)
def chip(f, d=.11): t = tt(d); return lpf(np.sign(np.sin(2*np.pi*f*t)), 5500) * np.minimum(1, (d - t)/.01) * np.minimum(1, t/.002)
def saw(f, d): t = tt(d); return 2 * ((t * f) % 1) - 1
def stab(notes, d=.35, cut=2600): t = tt(d); return lpf(sum(saw(hz(m), d) + saw(hz(m)*1.006, d) for m in notes) / (2*len(notes)), cut) * np.exp(-t*8) * np.minimum(1, t/.005)
def pad(notes, d, cut=1500): t = tt(d); e = np.minimum(1, t/.5) * np.minimum(1, (d - t)/.5); return lpf(e * sum(saw(hz(m), d) + saw(hz(m)*1.004, d) for m in notes) / (2*len(notes)), cut)
def string(f, d=1.8):
    """Plucked string (Karplus-Strong): koto, harp, sitar-ish depending on pitch."""
    n = max(2, int(SR / f)); buf = lpf(rng.uniform(-1, 1, n), 5000); out = np.empty(int(d * SR))
    for i in range(len(out)):
        v = buf[i % n]; out[i] = v; buf[i % n] = .997 * .5 * (v + buf[(i + 1) % n])
    return out


# ---------------------------------------------------------------- effects
def blip(f, d=.07): t = tt(d); return np.sin(2*np.pi*f*t) * np.exp(-t*45) * np.minimum(1, t/.002)
def click(): t = tt(.04); return bp(noise(.04), 1500, 6000)*np.exp(-t*220) + .8*np.sin(2*np.pi*900*t)*np.exp(-t*160)
def thud(): t = tt(.4); return np.sin(2*np.pi*np.cumsum(58 + 70*np.exp(-t*40))/SR)*np.exp(-t*10) + .3*lpf(noise(.4), 1200)*np.exp(-t*26)
def whoosh(d=.6): t = tt(d); x = noise(d); return (lpf(x, 800)*(1 - t/d) + bp(x, 1300, 4500)*(t/d)) * np.sin(np.pi*t/d)**2
def dive(d=.5): t = tt(d); x = noise(d); f = t/d; return (lpf(x, 600)*(1 - f) + bp(x, 1000, 7000)*f) * f**1.4 + .3*np.sin(2*np.pi*np.cumsum(120 + 700*f**2)/SR) * f**2
def riser(d=2.5): t = tt(d); f = t/d; return bp(noise(d), 400, 9000) * f**2.2 + .25*np.sin(2*np.pi*np.cumsum(180 + 900*f**2)/SR) * f**2
def scribble(d=.5): t = tt(d); return bp(noise(d), 1500, 5500) * (.5 + .5*np.abs(np.sin(2*np.pi*11*t))) * np.minimum(1, t/.03) * np.minimum(1, (d - t)/.05)
def switch(): t = tt(.09); return .8*np.sin(2*np.pi*1300*t)*np.exp(-t*120) + np.concatenate([np.zeros(int(.035*SR)), .9*np.sin(2*np.pi*900*tt(.055))*np.exp(-tt(.055)*110)])[:len(t)]
def chime():
    out = np.zeros(int(1.5 * SR))
    for k, m in enumerate([84, 88, 91]):
        s = pluck(hz(m), 1.2); i = int(k * .09 * SR); out[i:i + len(s)] += s[: len(out) - i]
    return out
def success(step=0):
    r = PENTA[int(step) % len(PENTA)] + 12; out = np.zeros(int(1.1 * SR))
    for k, m in enumerate([r, r + 4, r + 7, r + 12]):
        s = marimba(hz(m), .8); i = int(k * .06 * SR); out[i:i + len(s)] += s[: len(out) - i]
    return out
def counter(d=.7, steps=10):
    out = np.zeros(int((d + .1) * SR))
    for k in range(steps):
        s = blip(hz(PENTA[k % len(PENTA)] + 12), .06); i = int(k * d / steps * SR); out[i:i + len(s)] += s
    return out
def glitch(): t = tt(.3); return bp(noise(.3), 800, 9000) * (np.sin(2*np.pi*40*t) > 0) * np.exp(-t*8)
def confetti(): t = tt(.35); return bp(noise(.35), 4000, 11000) * np.exp(-t*9)
def alert(): return np.concatenate([blip(740), blip(622)])
def _env(t, d, a=.004, r=.03): return np.minimum(1, t / a) * np.minimum(1, (d - t) / r)
def _over(base, s, at=0.0, g=1.0):
    i = int(at * SR); s = s[: len(base) - i]; base[i:i + len(s)] += s * g; return base
def cowbell(f, d=.2): t = tt(d); x = np.sign(np.sin(2*np.pi*f*t)) + np.sign(np.sin(2*np.pi*f*1.504*t)); return bp(x, 450, 6500) * (.6*np.exp(-t*60) + .4*np.exp(-t*14)) * _env(t, d)
def shatter():
    x = bp(noise(.7), 2500, 12000) * np.exp(-tt(.7)*8)
    for _ in range(10): _over(x, blip(rng.uniform(2600, 6200), .14), rng.uniform(0, .45), .5)
    return x
def crash(): return _over(bp(noise(.6), 300, 5200) * np.exp(-tt(.6)*7), thud())
def boom(): d = 1.8; t = tt(d); return 1.4*np.sin(2*np.pi*np.cumsum(34 + 60*np.exp(-t*5))/SR)*np.exp(-t*2.6) + lpf(noise(d), 520)*np.exp(-t*3) + .5*bp(noise(d), 800, 5000)*np.exp(-t*9)
def lock(): t = tt(.55); return _over(sum(a*np.sin(2*np.pi*f*t)*np.exp(-t*(7 + 3*i)) for i, (f, a) in enumerate([(620, 1), (918, .6), (1283, .45), (1798, .3)])) * np.minimum(1, t/.002), thud())
def motor(d=.26): t = tt(d); return lpf(2*((np.cumsum(90 + 70*t/d)/SR) % 1) - 1, 900) * _env(t, d, .02, .05)
def ratchet():
    x = motor(.34)
    for k in range(7): _over(x, click(), k * .045, .6)
    return x
def ping(step=0): t = tt(.3); return np.sin(2*np.pi*1150*2**(step/24)*t) * np.exp(-t*13) * np.minimum(1, t/.002)
def coins(n=9, d=.5):
    x = np.zeros(int((d + .2) * SR))
    for k in range(n): _over(x, blip(rng.uniform(3200, 5200), .12), k * d / n)
    return x
def cash(): t = tt(.7); u = np.maximum(t - .09, 0); return _over(.6*np.sin(2*np.pi*2093*t)*np.exp(-t*9) + .5*np.sin(2*np.pi*2637*u)*np.exp(-u*8)*(t > .09), click())
def payout():
    x = np.zeros(int(1.3 * SR))
    for k, n in enumerate([72, 76, 79, 84, 76, 79, 84, 88, 79, 84, 88, 91]): _over(x, chip(hz(n), .075), k * .052, .5)
    return _over(x, coins(12, .6), .55)
def squawk(): d = .4; t = tt(d); f = 620 + 760*np.sin(np.pi*t/d)**.5 + 40*np.sin(2*np.pi*31*t); return bp(np.tanh(3*np.sin(2*np.pi*np.cumsum(f)/SR)), 900, 4200) * _env(t, d, .01, .08)
def quack():
    d = .17; t = tt(d); q = bp(2*((np.cumsum(560 - 240*t/d)/SR) % 1) - 1, 650, 2800) * np.sin(np.pi*t/d)**.5
    return _over(np.concatenate([q, np.zeros(int(.2 * SR))]), q, .2, .85)


# ---------------------------------------------------------------- mixing
class Mix:
    """A stereo timeline. add() places a mono sound at a time, with a gain and a pan (-1..1)."""
    def __init__(self, dur):
        self.dur = dur; self.n = int(SR * dur); self.L = np.zeros(self.n); self.R = np.zeros(self.n)

    def add(self, sig, t, gain=1.0, pan=0.0):
        i = int(t * SR)
        if i >= self.n or i < 0:
            return
        s = np.asarray(sig)[: self.n - i] * gain
        self.L[i:i + len(s)] += s * np.sqrt(1 - max(pan, 0)); self.R[i:i + len(s)] += s * np.sqrt(1 + min(pan, 0))

    def save(self, path, peak_db=-1.5, fade=1.5):
        mix = np.stack([self.L, self.R], 1)
        f = min(int(fade * SR), self.n)
        if f:
            mix[-f:] *= np.linspace(1, 0, f)[:, None]
        mix = np.tanh(mix * 1.15) / 1.15                      # soft clip, so a stack of hits never crackles
        top = np.abs(mix).max()
        if top > 0:
            mix *= 10 ** (peak_db / 20) / top
        with wave.open(str(path), "wb") as w:
            w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix * 32767).astype(np.int16).tobytes())
        return path


def play_cues(mix, events, gain=1.0):
    """Place the standard sound for each cue. Pitched cues climb the pentatonic scale with x,
    so a run of ticks or fixes rises as it goes: the ear hears progress."""
    for e in events:
        t, ty, x = e["t"], e["type"], e.get("x") or 0
        g = lambda v: v * gain
        if ty == "pop": mix.add(marimba(hz(PENTA[(3 + int(x)) % 15] + 12), .3), t, g(.12), (int(x) % 2 - .5) * .4)
        elif ty == "tick": mix.add(blip(hz(PENTA[int(x) % 15] + 12), .06), t, g(.08), .25)
        elif ty == "click": mix.add(click(), t, g(.2))
        elif ty in ("thud", "stamp", "drop"): mix.add(thud(), t, g(.28))
        elif ty == "whoosh": mix.add(whoosh(), t, g(.07))
        elif ty == "dive": mix.add(dive(), t - .2, g(.13))
        elif ty == "alert": mix.add(alert(), t, g(.09))
        elif ty in ("ding", "chime"): mix.add(chime(), t, g(.11))
        elif ty == "success": mix.add(success(x), t, g(.14))
        elif ty == "confetti": mix.add(confetti(), t, g(.05))
        elif ty == "scribble": mix.add(scribble(max(.3, float(x) or .5)), t, g(.06))
        elif ty == "type": mix.add(scribble(max(.3, float(x) or .4)) * .5, t, g(.03))
        elif ty == "count": mix.add(counter(max(.3, float(x) or .7)), t, g(.08))
        elif ty == "switch": mix.add(switch(), t, g(.2))
        elif ty == "glitch": mix.add(glitch(), t, g(.12))
        elif ty == "brush": mix.add(whoosh(1.6), t, g(.05))
        elif ty == "final": mix.add(thud(), t, g(.5)); mix.add(chime(), t + .05, g(.16))
        elif ty == "shatter": mix.add(shatter(), t, g(.5)); mix.add(thud(), t, g(.6))
        elif ty == "slam": mix.add(thud(), t, g(.34)); mix.add(bp(noise(.1), 200, 2400) * np.exp(-tt(.1) * 40), t, g(.2))
        elif ty == "crash": mix.add(crash(), t, g(.42))
        elif ty == "boom": mix.add(boom(), t, g(.75)); mix.add(chime(), t + .05, g(.12))
        elif ty == "lock": mix.add(lock(), t, g(.26))
        elif ty == "ratchet": mix.add(ratchet(), t, g(.13))
        elif ty == "motor": mix.add(motor(), t, g(.1))
        elif ty == "ping": mix.add(ping(x), t, g(.1), -.2)
        elif ty == "cash": mix.add(cash(), t, g(.16))
        elif ty == "coins": mix.add(coins(), t, g(.09))
        elif ty == "payout": mix.add(payout(), t, g(.13))
        elif ty == "squawk": mix.add(squawk(), t, g(.2), .3)
        elif ty == "quack": mix.add(quack(), t, g(.26), .3)
        elif ty == "step": mix.add(blip(480, .04), t, g(.07), .4)


def bed(mix, style="pulse", bpm=120, t0=0.0, t1=None, root=48, tail=2.5):
    """A plain backing groove between t0 and t1, so a cue track is not left bare.
    pulse: four-on-the-floor with a plucked arpeggio. boombap: swung kick and snare with piano.
    phonk: an 808 on a broken kick pattern, claps, and a cowbell line that enters after two bars;
    it stops dead at t1 instead of resolving, so put the last hit of the film there.
    Scenes cut on whole bars (4 beats) land on the beat: bar length is 240 / bpm seconds."""
    t1 = mix.dur - tail if t1 is None else t1
    beat = 60 / bpm; prog = [(0, [12, 16, 19]), (-3, [9, 12, 16]), (-7, [9, 12, 17]), (-5, [11, 14, 19])]
    if style == "phonk":
        r, step, n = root - 3, beat / 4, 0                    # the relative minor of `root`, on a sixteenth-note grid
        while t0 + n * step < t1 - .01:
            t, pos, bar = t0 + n * step, n % 16, n // 16
            if pos in (0, 6, 10) or (pos == 14 and bar % 2):
                mix.add(kick(), t, .5); mix.add(bass(hz(r - 12 if pos != 10 else r - 9), beat * (1.3 if pos == 0 else .7)), t, .3)
            if pos in (4, 12): mix.add(clap(), t, .17)
            if pos % 2 == 0: mix.add(hat(), t, .05, .3)
            if bar % 2 and pos >= 12: mix.add(hat(.03), t + step / 2, .035, -.3)
            m = PHONK[n % 32]
            if m is not None and (bar >= 2 or pos < 8): mix.add(cowbell(hz(r + 36 + m)), t, .085, .2)
            n += 1
        mix.add(pad([r, r + 7, r + 12, r + 15], mix.dur - t1, 900), t1, .05); return
    b, bar = t0, 0
    while b < t1 - .05:
        off, ch = prog[bar % 4]; ch = [root + c for c in ch]
        for q in range(4):
            tb = b + q * beat
            if tb >= t1:
                break
            if style == "pulse":
                mix.add(kick(), tb, .42); mix.add(hat(), tb + beat / 2, .05, .3)
                mix.add(bass(hz(root + off - 12 + (12 if q == 3 else 0)), beat * .9), tb, .2)
                for e in range(4): mix.add(pluck(hz(ch[(q + e) % 3] + 12)), tb + e * beat / 4, .045, -.3 + e * .2)
                if q in (1, 3): mix.add(clap(), tb, .07)
            else:
                if q == 0: mix.add(kick(), tb, .5); mix.add(bass(hz(root + off - 12), beat * 1.6), tb, .28)
                if q == 2: mix.add(kick(), tb + beat * .5, .32)
                if q in (1, 3): mix.add(snare(), tb, .24)
                mix.add(hat(), tb, .05, .3); mix.add(hat(.03), tb + beat * .62, .03, .3)
                if q in (0, 2): [mix.add(piano(hz(m)), tb + k * .012, .065, (k - 1) * .25) for k, m in enumerate(ch)]
        mix.add(pad(ch, beat * 4 + .5), b, .035)
        b += beat * 4; bar += 1
    mix.add(pad([root, root + 7, root + 12, root + 16, root + 19], mix.dur - t1), t1, .08)


PHONK = [0, None, 0, None, 3, None, 0, None, -2, None, 0, None, -5, None, -2, None,   0, None, 0, None, 3, None, 5, None, 3, None, 0, None, -2, 0, None, None]
PACK = {"shatter": shatter, "boom": boom, "lock": lock, "cash": cash, "payout": payout, "squawk": squawk, "quack": quack, "ping": ping, "pop": lambda: marimba(hz(84), .3), "tick": lambda: blip(hz(96), .06), "click": click, "thud": thud, "switch": switch,
        "chime": chime, "success": success, "counter": counter, "whoosh": whoosh, "scribble": scribble, "alert": alert}


def main():
    ap = argparse.ArgumentParser(description="Code-made sound effects and backing for rendered video.")
    ap.add_argument("cues", nargs="?", help="JSON from `fastrender.py page.html --dump-sfx`")
    ap.add_argument("--out", default="sfx.wav")
    ap.add_argument("--bed", choices=["none", "pulse", "boombap", "phonk"], default="none")
    ap.add_argument("--bpm", type=float, default=120)
    ap.add_argument("--t0", type=float, default=0, help="when the groove's first downbeat falls (the page's first beat)")
    ap.add_argument("--tail", type=float, default=2.5, help="seconds before the end where the groove resolves; 0.5 for a video with no end card")
    ap.add_argument("--peak", type=float, default=-1.5, help="peak level in dBFS; about -22 to sit under a voice")
    ap.add_argument("--pack", help="write each standard sound as a WAV in this folder")
    a = ap.parse_args()
    if a.pack:
        d = pathlib.Path(a.pack); d.mkdir(parents=True, exist_ok=True)
        for name, fn in PACK.items():
            s = fn(); m = Mix(len(s) / SR + .05); m.add(s, 0); m.save(d / f"{name}.wav", peak_db=-3, fade=0)
        print(f"{len(PACK)} sounds -> {d}"); return
    if not a.cues:
        ap.error("give a cue file, or --pack DIR")
    data = json.loads(pathlib.Path(a.cues).read_text(encoding="utf-8"))
    events = data["events"] if isinstance(data, dict) else data
    dur = (data.get("dur") if isinstance(data, dict) else 0) or (max(e["t"] for e in events) + 2)
    mix = Mix(dur)
    if a.bed != "none":
        bed(mix, a.bed, a.bpm, t0=a.t0, tail=a.tail)
    play_cues(mix, events)
    mix.save(a.out, peak_db=a.peak, fade=min(1.5, a.tail) if a.bed != "none" else 0)
    print(f"{len(events)} cues over {dur:.1f}s -> {a.out}")


if __name__ == "__main__":
    main()
