---
name: motion-kit
description: Makes a browser-rendered video move like a product being used instead of playing like a slideshow. It gives the named moves (pop, count-up, tick, drag, hold-to-fill, dive and more), the pacing rules that remove dead air, a cursor-and-camera demo engine, a beat grid, code-made sound effects, safe zones for vertical video and for graphics over someone's own footage, and an activity audit that measures whether the picture is actually changing. Use it for every /brag-slim build before writing scenes, whenever a video is called a slideshow, slow, static, boring or full of awkward pauses, when the user asks for something interactive, engaging or dopamine-inducing, for text-only script videos, screenshot promos, and motion graphics added to a recorded clip.
---

# motion-kit

A launch video fails in one of two ways: nothing on screen is the real thing, or the real
thing sits still. `brag-styles` decides how it looks. This skill decides how it moves,
sounds and keeps going.

## The test

Run the audit before every full render. It samples the page four times a second and reports
how much of the picture changes:

```
python <fast-render>/scripts/fastrender.py video.html --audit
```

(`<fast-render>`, `<narrate>` and `<motion-kit>` are the skill folders beside each other: this
one is `<motion-kit>`. Run every command from the project's work folder with the full path to
the script.)

It prints the median activity, the share of the time that is quiet (under 1% of pixels
changing), and every quiet stretch of 1.5 s or longer. Calibration so far is one viewer and
four videos: two he called "a slide show" measured 52% and 42% quiet; a cursor-driven demo he
accepted measured 5%. Fix every listed stretch unless it is the held end card. The number is
a prompt to look, not a score to chase: do not add a drifting background to quiet it, give
the scene something to do.

## Rules that remove the slideshow

1. **Something acts.** Every scene has a performer: a cursor, a pen, a hand, a character, a
   camera. Text that fades in is not a performer. A sparse style (line drawings, a printed page)
   needs this most: put a pencil on every stroke and let the camera follow it. That alone took
   a hand-drawn intro from 52% quiet to 10%, and a newspaper from 43% to 33%.
2. **Cause, then effect, at once.** A click is followed within 0.3 s by what it caused, and
   the effect is bigger than the click.
3. **Nothing waits after its payoff.** When the action of a scene has landed, leave within
   one beat. A scene that finishes at 3.5 s inside a 5 s slot is 1.5 s of dead air; five of
   those is what "awkward breaks" means.
4. **Overlap.** The cursor travels while the camera travels. The next thing starts before the
   last has settled. Two things in sequence with a gap between them read as slides.
5. **One space.** Move a camera across one board, or dive through one world into the next.
   A hard cut to a new full-screen layout is a page turn.
6. **Reading time has motion in it.** When a line must be held to be read (about 0.3 s a
   word), the frame keeps pushing in, or a secondary element keeps moving.
7. **A reward for every completion.** A counter climbs, a pip fills, a tile changes colour, a
   small burst of confetti: the viewer sees progress add up.
8. **Short lines.** A narration line over an action beat is under 2 s. A longer line needs
   several actions under it, not one.
9. **The first two seconds state the pain in large type**, and the last frame holds the
   outcome and the call to action for about 3 s. Most social video is watched muted, so
   burn in captions for every spoken line.

## Beat grid

Pick a tempo and cut on it: at `bpm`, a beat is `60 / bpm` s and a bar is four beats. Make
each action scene a whole number of bars and land its payoff on a beat (the reference demo
uses 140 BPM, 2 bars a scene, payoff on beat 7 of 8). Then the music needs no editing to
fit, and every fix arrives where the ear expects it. Write the narration first, measure it
with `narrate`, then round each scene up to the grid: `<motion-kit>/scripts/fit_scenes.py` does
both steps and writes the `layout.js` the engines read. For a film cut to music, give a line
`{"text": ..., "at": 22}` to start it on that beat, so each spoken word can trigger its own action. The page's first scene must start on
a beat (time 0, or one beat in), or everything after it is off the grid.

## Moves

Name the move and build it as a pure function of time. The table of 41 moves, each with its
timing and the one-line formula, is in `references/moves.md`. The ones that carry a demo:

| Move | Use it for |
|---|---|
| press, hover-lift | every button: it lifts as the cursor arrives and sinks on the click |
| drag and drop | a file into a zone, a card into a machine: the object follows the cursor |
| hold-to-fill, slider scrub | a bar or a value that answers the cursor live |
| count-up, bar fill, tick | any number, any progress, any list |
| fly-chip | a value leaving a document and landing in a table |
| stamp, slam | a verdict: CAUGHT, APPROVED, the headline word |
| dive | leaving one world through the middle of the frame |

## Engines to lift from (open only the one you need)

| File | What it is |
|---|---|
| `../brag-styles/sets/ops-desk/ref/engine.html` | One board, a camera that flies between tiles, a cursor that clicks, drags and scrubs, a fixed-count HUD, confetti, everything on a beat grid. The reference for a product or service demo. |
| `ref/worlds.html` | Eight short worlds in eight styles joined by zoom-through dives, one cursor acting in each. The reference for an intro or a story that changes mood. |
| `../brag-styles/sets/kinetic-type/ref/engine.html` | A script in, one sentence per screen, set as large as fits, words slamming in on the beat. Works at any frame size. The reference for a text-only video. |
| `../brag-styles/sets/brutal-bento/ref/engine.html` | A page smashed into shards, a board of live miniature rooms, a camera that flies into a tile until it fills the frame, an indexing conveyor, a readout falling through units, and tiles that fold into a QR code. Every time is in beats. The reference for a loud personal intro. |
| `ref/overlay.html` | Transparent graphics over a recorded clip, each starting on the spoken word. See "Graphics on footage" below. |

Each engine carries its helpers (`seg`, `eo`, `spring`, `bump`, the cursor track, `press`).
Copy the helpers and the mechanism; replace every word and number with the project's own.

## Sound

`<motion-kit>/scripts/soundkit.py` makes every sound in code, so nothing needs a licence
(`pip install numpy scipy`).

```
python <fast-render>/scripts/fastrender.py video.html --dump-sfx sfx.json                 # the page's cues, and its marks
python <motion-kit>/scripts/soundkit.py sfx.json --out score.wav --bed pulse --bpm 120    # cues + a backing groove
python <motion-kit>/scripts/soundkit.py --pack sfx/                                       # the sounds as WAV files
```

Three beds ship: `pulse` (four-on-the-floor, clap, plucked arpeggio), `boombap` (swung kick
and snare, piano) and `phonk` (808, claps and a cowbell line; it stops dead instead of resolving). Give `--bpm` the page's own tempo and `--t0` the time of its first beat.
The groove resolves `--tail` seconds before the end: 2.5 by default for a held end card,
0.5 when the last scene runs to the end.

A page lists its cues in `window.SFX` as `{t, type, x}`; the names are in the script's
header. For a score of your own, `from soundkit import Mix, kick, marimba, pad, play_cues`.

- Beyond the quiet interface sounds there is a louder set for a film that plays for laughs:
  `shatter slam crash boom lock ratchet motor ping cash coins payout squawk quack step`.
- Put a sound on a thing that matters: a tick on each list item, a rising run while a bar
  fills, a chime on the last card. Not on every slide-in.
- Pitched cues climb with `x`, so progress is audible.
- Add a layer of the music for each completion; the track should be fullest at the outcome.
- Effects sit about 20 dB under a voice (`--peak -22` for a track laid over speech). Over
  narration from `narrate`, the mix ducks the music for you.

## Safe zones

| Frame | Keep clear |
|---|---|
| Landscape 1920x1080 | 120 px on every side; the bottom 130 px if captions are burned in |
| Vertical 1080x1920 | text inside the middle 80% of the width; the top 12% and bottom 20% belong to the app's own buttons and captions |
| Graphics on footage | the speaker's face, the bottom third (captions), the outer 10% left and right, and the first 3 s (the speaker's hook) |

## Graphics on footage

1. `python <narrate>/scripts/transcribe.py clip.mp4` writes `clip.words.json` and
   `clip.words.js` (word timings, offline). `--find "40 a week"` prints when a phrase is said.
2. Watch the clip: pull a few frames, find the face, and choose a zone it never enters.
3. Copy `ref/overlay.html` and the `fonts/` folder, load the words file, and write `CUES`:
   a spoken list becomes a checklist that ticks on each word, a spoken number becomes a
   counter that rolls between the two numbers, a before and after becomes a comparison.
   Use solid cards: frosted glass has nothing to blur on a transparent page.
4. `fastrender.py overlay.html --over clip.mp4 --out with-graphics.mp4 [--audio sfx.wav]`
   keeps the clip's size, frame rate, cut and audio and lays the graphics on top. For an
   editor instead: `--transparent --out card.mov --png-dir card-png` (ProRes 4444 with alpha).
5. To change one moment later, name it by the words spoken ("when I say forty a week"), not
   by the timestamp, change only that cue, and render to the same file.

## A code people must scan

`python <motion-kit>/scripts/qr.py https://example.com --out qr.js` writes the module grid
(`pip install opencv-python`). Draw each module as a solid dark square on a light card with
four modules of margin. Bring it in however you like, then hold it flat, still and uncovered
for the last three seconds: a code that spins, glows or is built from texture does not scan.
Pull a frame from the encoded video and run `qr.py --check frame.png` before delivering.

## Fonts

`fonts/` holds six open-licence families (Inter, Archivo Black, Instrument Serif, Bricolage
Grotesque, Space Grotesk, JetBrains Mono; SIL OFL 1.1) and a `fonts.css`. Copy the folder
beside the page and link it when a render must not depend on the network.
