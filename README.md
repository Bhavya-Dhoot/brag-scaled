# /brag

**You built it. Now brag.**

[![the /brag launch site — you built it, now brag](docs/assets/hero.png)](https://latent-spaces.github.io/brag/)

`/brag` is a Claude Code skill that turns the project you created into a short, shareable launch video — music, motion, and share copy included. One command, powered by [Hyperframes](https://hyperframes.heygen.com/).

The looping video on the [launch site](https://latent-spaces.github.io/brag/) was made by `/brag` on this very repo. 

## Install

```bash
/plugin marketplace add latent-spaces/brag
/plugin install brag@brag
```

Then run `/brag` inside any project.

<details>
<summary>No plugin system? Install the skill directly.</summary>

```bash
rsync -a --exclude '.DS_Store' skills/brag/ ~/.claude/skills/brag/
```

Restart Claude Code after copying.
</details>

### Also works with

| Agent | How |
|---|---|
| **opencode** | `git clone ... ~/.config/opencode/skills/brag/` or point `opencode.json` at [`adapters/opencode/`](adapters/opencode/) |
| **Codex, Cursor, Aider, etc.** | Load [`AGENT.md`](AGENT.md) into custom instructions; see [`adapters/generic/`](adapters/generic/) |

## Use it

From any project directory, ask Claude:

```text
let's /brag
```

Or steer the tone:

```text
/brag --tone "fake Series A launch from 2016"
```

You get a `brag-output/` folder with the plan, a composition brief, share copy, and the rendered `brag.mp4`.

## How it works

`/brag` owns the story — the product angle, tone, and which moments to show. It hands a focused brief to [Hyperframes](https://hyperframes.heygen.com/), which builds, times, and renders the video.

## Requirements

- Claude Code (with skill/plugin support)
- Node.js 22+
- FFmpeg on `PATH`
- Hyperframes CLI — `npx hyperframes` (check it with `npx hyperframes doctor`)

## What's in this repo

- `skills/brag/` — the skill, references, and bundled music + SFX
- `examples/` — fake product sites used as a benchmark suite
- `docs/` — the launch site (GitHub Pages)
- `.claude-plugin/` — plugin manifest + marketplace catalog
- `adapters/` — config for opencode, Codex, and other agents

## Credits

- Music — [ende.app](https://ende.app/en) "Happy Beats / Business Moves"
- Sound effects — [Kenney](https://kenney.nl/)
- Video generation — [Hyperframes](https://hyperframes.heygen.com/)
- Fake demo sites — built with [Impeccable](https://impeccable.style/)

## Contributing

Contributions, ideas, and new demo brags are welcome — open an issue or a PR.
