# brag-scaled

**You built it. Now brag — and render it in minutes.**

[![The brag-scaled launch video, silent preview. Click to play it with sound.](docs/assets/brag-scaled-preview.webp)](https://cdn.jsdelivr.net/gh/Bhavya-Dhoot/brag-scaled@87d204e/docs/assets/brag-scaled.mp4)

*This launch video was made with brag-scaled itself: the `patent-office` style, offline
narration from `narrate`, and 1,500 frames at 60 fps rendered by `fast-render` in 38 s.
The loop above is a silent preview. **[Play the full 25 s video with sound](https://cdn.jsdelivr.net/gh/Bhavya-Dhoot/brag-scaled@87d204e/docs/assets/brag-scaled.mp4)**,
or see the [poster frame](docs/assets/brag-scaled.jpg).*

`brag-scaled` is a set of agent skills that turn the project you built into a short, shareable launch video, with music, motion, optional narration and share copy. It also makes text-only videos from a script, promos from screenshots, and motion graphics laid over a clip you recorded.

| Skill | What it does |
|---|---|
| `/brag-slim` | The model builds the whole video itself: story, visuals, soundtrack, share copy. It is the default on Claude Opus 5.5. |
| `/brag` | The classic workflow, which builds and renders through [Hyperframes](https://hyperframes.heygen.com/). |
| `fast-render` | Renders any `window.render(t)` page to MP4 on the GPU with parallel browsers. Also 4K, transparent ProRes, graphics over footage, a setup check and an activity audit. `/brag-slim` uses it for stills and the final render. |
| `motion-kit` | Keeps a video from playing like a slideshow: 41 named moves, pacing rules, cursor-and-camera demo engines, a beat grid, code-made sound and three backing grooves, a QR code that is checked to scan, safe zones, and bundled open-licence fonts. |
| `narrate` | Offline voiceover with a bundled 82M-parameter TTS model (Kokoro). It gives exact line timings and ducks the music under the voice. `transcribe.py` goes the other way: word timings from a recorded clip. |
| `brag-styles` | 34 art-directed looks, each with a signature motion trick and a matching sound palette. Ask for options and it recommends one before building anything. |

## Why it's fast

![Frame cost and whole-film render time](docs/assets/scaled/render-speed.svg)

![Render pipeline, before and after](docs/assets/scaled/pipeline.svg)

The whole-film test was a 130-second, 60 fps video (7,800 frames at 1080p) on Windows 11,
with an i9-11950H, an RTX A2000 Laptop GPU and an NVMe drive:

| | time |
|---|---|
| Playwright PNG screenshots to disk, then x264 | ~45 min (estimated from the observed ~3 fps) |
| `fast-render`, default settings (4 encoder sessions) | 4 min 46 s |
| 12 parallel encoder sessions (same as `--encode-jobs 12`) | 3 min 46 s |

Short clips get their own browser count (60+ frames per browser), so a 6-second clip went
from 34 s to 22 s. The output decodes within 43.6 dB PSNR of a lossless capture of the same
frame. Only the Windows + NVIDIA path is measured so far. The macOS and Linux GPU flags are
the documented ANGLE backends, and the renderer line shows what actually ran.

## It moves like a demo, not a slideshow

| Ops Desk: a board operated by a cursor | Kinetic Type: a script, one sentence a screen |
|---|---|
| ![A bento board with five tiles fixed by a cursor](skills/brag-styles/sets/ops-desk/frames/f4.webp) | ![Large type with one accent word](skills/brag-styles/sets/kinetic-type/frames/f1.webp) |

A video made of good frames can still be a slideshow. `fast-render --audit` samples the page four
times a second and measures how much of the picture is changing. Four videos made with this repo,
and what one viewer said about each:

| Video | Median activity | Quiet (under 1% changing) | Verdict from the viewer |
|---|---|---|---|
| Doodle intro, scene by scene | 0.9% | 52% of the time | "feels like a slide show" |
| Newspaper, page by page | 1.2% | 43% | "feels like a slide show" |
| Ops Desk demo, recut on a beat grid | 6.9% | 5% | accepted |
| Kinetic Type reference | 7.0% | 2% | not yet judged |
| The doodle intro again, with a pencil on every stroke and a camera following it | 11.7% | 10% | not yet judged |
| Brutal Bento reference: rooms inside tiles, cut to 140 BPM | 8.0% | 9% | chosen as the author's introduction |

That is one viewer and a handful of videos, so read it as a prompt to look, not a score. `motion-kit`
holds what changed between the first two and the third: a performer in every scene, effect straight
after cause, nothing waiting after its payoff, scenes cut to whole bars, a reward for every completion.

## Graphics on your own footage

```text
/brag-slim clip.mp4 "add graphics to my video"
```

`transcribe.py` gets word timings offline, the overlay page puts a checklist or a counter on the exact
spoken word inside the safe zone (off the face, above the captions), and `fast-render --over` lays it on
the clip with its size, frame rate, cut and audio untouched. An 18 s, 1080x1920 clip (434 frames) was
composited in 24 s on the reference laptop. For an editor instead, `--transparent` writes ProRes 4444
with alpha and a PNG sequence.

## 34 looks, recommended before anything is built

![Nineteen of the 34 brag-styles looks; Ops Desk and Kinetic Type are shown above, Brutal Bento below](docs/assets/scaled/styles.jpg)

| Brutal Bento: the smash | a room inside a tile | the end card |
|---|---|---|
| ![A headline slammed over a bento board](skills/brag-styles/sets/brutal-bento/frames/f1.webp) | ![A conveyor room with PERFECT across it](skills/brag-styles/sets/brutal-bento/frames/f2.webp) | ![A QR code beside SCAN and DEPLOY](skills/brag-styles/sets/brutal-bento/frames/f4.webp) |

### Ask for a style by name

Twelve of the sets exist because people ask for a design style, not a set: claymorphism, glassmorphism,
neumorphism, Swiss and minimal, luxury typography, cybercore, synthwave, Y2K, surrealism, ethereal, bohemian and
wabi-sabi. Each has a ten-second working reference (`ref/look.html`) that passed the activity audit. The other
names map to sets that already existed: neo-brutalism and bento grid, editorial, pixel art, scrapbook, sketch, maximalism.

| | | |
|---|---|---|
| ![Swiss Grid](skills/brag-styles/sets/swiss-grid/frames/f3.webp)<br>`swiss-grid` | ![Cyber Core](skills/brag-styles/sets/cyber-core/frames/f3.webp)<br>`cyber-core` | ![Glass Layers](skills/brag-styles/sets/glass-layers/frames/f2.webp)<br>`glass-layers` |
| ![Clay Toys](skills/brag-styles/sets/clay-toys/frames/f3.webp)<br>`clay-toys` | ![Soft Press](skills/brag-styles/sets/soft-press/frames/f2.webp)<br>`soft-press` | ![Y2K Chrome](skills/brag-styles/sets/y2k-chrome/frames/f3.webp)<br>`y2k-chrome` |
| ![Synthwave Drive](skills/brag-styles/sets/synthwave-drive/frames/f3.webp)<br>`synthwave-drive` | ![Luxe Type](skills/brag-styles/sets/luxe-type/frames/f2.webp)<br>`luxe-type` | ![Dream Logic](skills/brag-styles/sets/dream-logic/frames/f2.webp)<br>`dream-logic` |
| ![Ethereal Haze](skills/brag-styles/sets/ethereal-haze/frames/f2.webp)<br>`ethereal-haze` | ![Boho Market](skills/brag-styles/sets/boho-market/frames/f3.webp)<br>`boho-market` | ![Wabi-Sabi](skills/brag-styles/sets/wabi-sabi/frames/f3.webp)<br>`wabi-sabi` |

| You say | brag-scaled does |
|---|---|
| `/brag-slim --style options`, "give me some style options" | Recommends one look for your project, with a safer and a bolder alternative plus your own look, then **waits for your pick** |
| `/brag-slim` (no style mentioned) | Same: it recommends, then waits, unless your project's own UI can carry the video |
| `/brag-slim --style auto`, "just make it", "your call" | Picks the best look, says why in one line, then builds |
| `/brag-slim --style shahi-darbar`, "make it royal" | Uses that look (or the closest one) straight away |

![What a styled run has to read](docs/assets/scaled/style-context.svg)

## Offline narration

![How far the music drops under the voice](docs/assets/scaled/narration-ducking.svg)

`/brag-slim --voice` writes a short voiceover and synthesizes it locally with Kokoro-82M
(54 voices, no API key). It times each scene to the real length of its line and ducks the
music under the voice.

## Install

**Claude Code:**

```bash
claude plugin marketplace add Bhavya-Dhoot/brag-scaled
claude plugin install brag-scaled@brag-scaled
```

**Any other agent**, through the [`skills`](https://github.com/vercel-labs/skills) CLI (Cursor, Codex, Copilot, Gemini CLI, opencode and more):

```bash
npx skills add https://github.com/Bhavya-Dhoot/brag-scaled --skill brag-slim
npx skills add https://github.com/Bhavya-Dhoot/brag-scaled --skill fast-render
npx skills add https://github.com/Bhavya-Dhoot/brag-scaled --skill narrate
npx skills add https://github.com/Bhavya-Dhoot/brag-scaled --skill motion-kit
npx skills add https://github.com/Bhavya-Dhoot/brag-scaled --skill brag-styles
```

**Python tools** (`fast-render`, `narrate`, `motion-kit`):

```bash
pip install playwright imageio-ffmpeg kokoro-onnx soundfile numpy scipy pillow
playwright install chromium
pip install faster-whisper   # only for graphics on recorded footage
pip install opencv-python    # only for a QR code on screen
```

Then check the machine, including whether frames will be drawn on the GPU:

```bash
python skills/fast-render/scripts/fastrender.py --doctor
```

The TTS model (about 120 MB) downloads once on the first narration, from this repo's [`tts-v1` release](https://github.com/Bhavya-Dhoot/brag-scaled/releases/tag/tts-v1). It is checked against a SHA-256 and cached in `~/.cache/brag-scaled/`.

### Also works with

This repo exposes the skill at every agent's standard discovery path via symlinks. No extra config needed.

| Agent | How it discovers |
|---|---|
| **Google Antigravity** | Auto-detects from `.agents/skills/brag/` at project root or `~/.gemini/config/skills/brag/` globally |
| **opencode** | Auto-detects from `.opencode/skills/brag/` at project root |
| **Codex CLI** | Reads `.agents/skills/brag/`, walking up to repo root |
| **Claude Code** | Also reads `.claude/skills/brag/` (in addition to the `.claude-plugin/` marketplace install above) |
| **Other agents** | Point custom instructions at `skills/brag/SKILL.md` — see [`docs/other-agents.md`](docs/other-agents.md) |

> **Windows users:** Git requires `git config core.symlinks true` (or `git clone -c core.symlinks=true`) and Windows Developer Mode or Administrator privileges to create symlinks. If symlinks don't work on your system, copy `skills/brag/` to the agent's skill directory manually instead.

## Use it

From any project directory, ask your agent:

```text
let's /brag
```

Steer the tone, or add narration:

```text
/brag --tone "fake Series A launch from 2016"
/brag-slim --voice
/brag-slim --voice bf_emma
/brag-slim --style options
/brag-slim --style shahi-darbar
/brag-slim --style the-receipt --tone deadpan
/brag-slim --style ops-desk --voice
/brag-slim "Nobody watches a slideshow. Show the thing working." --format vertical
/brag-slim screenshots/
/brag-slim clip.mp4
```

After a render, say what to change in plain words ("make the counter start when it says forty", "render it in 4K", "give me a transparent version for Premiere"). One thing changes; the rest stays.

The set list, with what each is best for, is in [`skills/brag-styles/SKILL.md`](skills/brag-styles/SKILL.md). Each set has reference frames, and a Stitch prompt for regenerating it (`sets/<slug>/stitch.md`). Import a new Stitch export with `python scripts/import_stitch.py <export-dir>`.

You get a `brag-output/` folder with the plan, share copy, and the rendered `brag.mp4` with its poster frame.

## Requirements

- An agent that supports Agent Skills (Claude Code, opencode, Codex CLI, or any agent with custom instructions)
- Python 3.9+ for `fast-render`, `narrate` and `motion-kit`
- Node.js 22+ and the Hyperframes CLI, for the classic `/brag` only

## What's in this repo

- `skills/brag-slim/`: the single-file skill
- `skills/fast-render/`: the GPU renderer (`scripts/fastrender.py`)
- `skills/motion-kit/`: the moves and pacing rules, `scripts/soundkit.py` (sound made in code), `scripts/fit_scenes.py` (scenes fitted to narration on a beat grid, lines placed on beats), `scripts/qr.py` (a QR grid, and a check that a rendered frame scans), reference engines in `ref/`, and bundled fonts
- `skills/narrate/`: offline narration (`scripts/narrate.py`) and word timings from a clip (`scripts/transcribe.py`)
- `skills/brag-styles/`: the 34 visual systems. Each has a `set.md`, which is all a run reads, plus reference frames, `DESIGN.md` tokens and reference markup.
- `scripts/import_stitch.py`: turns a Google Stitch export into sanitised sets
- `skills/brag/`: the classic workflow, with its references and bundled music and SFX
- `examples/`: fake product sites used as a benchmark suite
- `docs/`: the launch site
- `.claude-plugin/`: the plugin manifest and marketplace catalog
- `.claude/skills/`, `.agents/skills/`, `.opencode/skills/`: symlinks into `skills/` for each agent's discovery path

## Credits

- Music: "Happy Beats / Business Moves" by Sascha Ende, [ende.app](https://ende.app/en) (CC BY 4.0)
- Sound effects: [Kenney](https://kenney.nl/) (CC0)
- Fonts in `skills/motion-kit/fonts/`: Inter, Archivo Black, Instrument Serif, Bricolage Grotesque, Space Grotesk and JetBrains Mono (SIL Open Font License 1.1)
- Voice: [Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M) (Apache-2.0), run through [kokoro-onnx](https://github.com/thewh1teagle/kokoro-onnx) (MIT)
- Video generation, in the classic `/brag`: [Hyperframes](https://hyperframes.heygen.com/)

Licences: the code is MIT (see `LICENSE`). Bundled audio, font and model terms are in [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).

## Contributing

Ideas, fixes and new demo brags are welcome. Open an issue or a PR.
