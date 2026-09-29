# brag-scaled

**You built it. Now brag — and render it in minutes.**

[![The brag-scaled launch video, silent preview. Click to play it with sound.](docs/assets/brag-scaled-preview.webp)](https://cdn.jsdelivr.net/gh/Bhavya-Dhoot/brag-scaled@87d204e/docs/assets/brag-scaled.mp4)

*This launch video was made with brag-scaled itself: the `patent-office` style, offline
narration from `narrate`, and 1,500 frames at 60 fps rendered by `fast-render` in 38 s.
The loop above is a silent preview. **[Play the full 25 s video with sound](https://cdn.jsdelivr.net/gh/Bhavya-Dhoot/brag-scaled@87d204e/docs/assets/brag-scaled.mp4)**,
or see the [poster frame](docs/assets/brag-scaled.jpg).*

`brag-scaled` is a set of agent skills that turn the project you built into a short, shareable launch video, with music, motion, optional narration and share copy.

| Skill | What it does |
|---|---|
| `/brag-slim` | The model builds the whole video itself: story, visuals, soundtrack, share copy. It is the default on Claude Opus 5.5. |
| `/brag` | The classic workflow, which builds and renders through [Hyperframes](https://hyperframes.heygen.com/). |
| `fast-render` | Renders any `window.render(t)` page to MP4 on the GPU with parallel browsers. `/brag-slim` uses it for stills and the final render. |
| `narrate` | Offline voiceover with a bundled 82M-parameter TTS model (Kokoro). It gives exact line timings and ducks the music under the voice. |
| `brag-styles` | 19 art-directed looks, each with a signature motion trick and a matching sound palette. Ask for options and it recommends one before building anything. |

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

## 19 looks, recommended before anything is built

![The 19 brag-styles looks](docs/assets/scaled/styles.jpg)

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
```

**Python tools** (`fast-render`, `narrate`):

```bash
pip install playwright imageio-ffmpeg kokoro-onnx soundfile
playwright install chromium
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
```

The set list, with what each is best for, is in [`skills/brag-styles/SKILL.md`](skills/brag-styles/SKILL.md). Each set has reference frames, and a Stitch prompt for regenerating it (`sets/<slug>/stitch.md`). Import a new Stitch export with `python scripts/import_stitch.py <export-dir>`.

You get a `brag-output/` folder with the plan, share copy, and the rendered `brag.mp4` with its poster frame.

## Requirements

- An agent that supports Agent Skills (Claude Code, opencode, Codex CLI, or any agent with custom instructions)
- Python 3.9+ for `fast-render` and `narrate`
- Node.js 22+ and the Hyperframes CLI, for the classic `/brag` only

## What's in this repo

- `skills/brag-slim/`: the single-file skill
- `skills/fast-render/`: the GPU renderer (`scripts/fastrender.py`)
- `skills/narrate/`: offline narration (`scripts/narrate.py`)
- `skills/brag-styles/`: the 19 visual systems. Each has a `set.md`, which is all a run reads, plus reference frames, `DESIGN.md` tokens and reference markup.
- `scripts/import_stitch.py`: turns a Google Stitch export into sanitised sets
- `skills/brag/`: the classic workflow, with its references and bundled music and SFX
- `examples/`: fake product sites used as a benchmark suite
- `docs/`: the launch site
- `.claude-plugin/`: the plugin manifest and marketplace catalog
- `.claude/skills/`, `.agents/skills/`, `.opencode/skills/`: symlinks into `skills/` for each agent's discovery path

## Credits

- Music: "Happy Beats / Business Moves" by Sascha Ende, [ende.app](https://ende.app/en) (CC BY 4.0)
- Sound effects: [Kenney](https://kenney.nl/) (CC0)
- Voice: [Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M) (Apache-2.0), run through [kokoro-onnx](https://github.com/thewh1teagle/kokoro-onnx) (MIT)
- Video generation, in the classic `/brag`: [Hyperframes](https://hyperframes.heygen.com/)

Licences: the code is MIT (see `LICENSE`). Bundled audio and model terms are in [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).

## Contributing

Ideas, fixes and new demo brags are welcome. Open an issue or a PR.
