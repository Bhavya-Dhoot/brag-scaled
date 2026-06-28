# /brag

You built it. Now let's brag about it.

`/brag` turns the current project website or app into a short, polished, shareable launch video using Hyperframes. It is narrow, opinionated, and fun.

**This file is the single source of truth for the /brag workflow.** It is written for any AI coding agent (opencode, Claude Code, Codex, Cursor, Aider, or any LLM that can execute CLI commands and read files). No plugin-system-specific assumptions.

## When to trigger

An agent should use this skill when the user says any of:
- `/brag` or `let's /brag`
- `make a launch video` / `turn this into a video`
- `brag about this project`
- `let me share what I built`

## How to invoke

The user may pass options inline or as natural language:

```
/brag
/brag --tone chaotic
/brag --tone polished --format vertical
/brag this. Make it feel like a ridiculous startup launch.
```

| Option | Values | Default |
|---|---|---|
| `--tone` | preset or freeform description | inferred |
| `--format` | `landscape`, `vertical`, `square` | `landscape` |
| `--duration` | seconds | auto (15-25s) |
| `--no-music` | flag | music on |
| `--no-sfx` | flag | sfx on |
| `--title` | string | inferred from project |

Tone presets: `default`, `polished`, `yc-parody`, `chaotic`, `deadpan`, `cinematic`, `app-store`. A freeform creative direction like "fake Series A launch from 2016" is always accepted — map it to the nearest preset for pacing and structure, but preserve the specific direction in the plan and brief.

## What this skill does

1. Reads the current project code to understand the app.
2. Plans a short brag concept specific to this project.
3. Scripts and storyboards the video.
4. Hands a focused composition brief to Hyperframes.
5. Validates, renders, and writes share copy.

## Output directory

Default: `brag-output/`. To avoid overwriting, use a timestamp: `brag-output-2026-05-04-143022/`. Use a timestamp when the user asks for a new run without overriding previous results, or when `brag-output/` already exists. Generate the timestamp at start (`YYYY-MM-DD-HHmmss`) and use it consistently.

---

## Step 1: Inspect the project

**Read:** `skills/brag/references/step-1-inspect.md`

Scan the project directory and extract the information needed to plan the brag video.

**Gate:** You can answer all 9 questions in the brag planning rubric.

---

## Step 2: Plan and storyboard

**Read:** `skills/brag/references/step-2-plan.md`

Write `<output-dir>/brag-plan.md`. Answer the planning rubric. Commit to a creative angle. Write the beat-by-beat storyboard including scenes, text, timing, transitions, and SFX cues.

When music is selected, include a compact `Music cue guidance` section: read the bundled track's cue preset from `skills/brag/assets/music/cues/` if present, otherwise note cues will be detected at composition time (any track now supports beat sync — see `skills/brag/references/audio.md`). Cue metadata is optional timing guidance only.

**Gate:** `<output-dir>/brag-plan.md` exists with a full storyboard. Scene durations sum to 15–25 seconds.

---

## Step 3: Hand off to Hyperframes

**Prerequisite:** Hyperframes CLI must be installed (`npx hyperframes doctor`).

**Read:** `skills/brag/references/step-3-compose.md`
**Read:** `skills/brag/references/audio.md`

Write the composition brief and use Hyperframes to create the video implementation in `<output-dir>/composition/`.

The agent owns the product angle, source material, storyboard, tone, format, audio selection, music cue guidance, and delivery expectations. Hyperframes owns the concrete composition structure, exact animation timing, animation mechanics, runtime choices, linting rules, and render workflow.

Implementation steps:
1. Write `<output-dir>/composition-brief.md` using the template in `skills/brag/references/step-3-compose.md`.
2. Copy planned music into `<output-dir>/composition/assets/music/` from `skills/brag/assets/music/`.
3. Run `npx hyperframes` to create the composition directory.
4. Let Hyperframes choose implementation details (animation, timing, SFX selection).
5. Run `npx hyperframes lint` and validate inside `<output-dir>/composition/`.

**Gate:** `npx hyperframes lint` passes with zero errors inside `<output-dir>/composition/`.

---

## Step 4: Validate, render, and deliver

**Read:** `skills/brag/references/step-4-deliver.md`

Validate, preview, render to `<output-dir>/brag.mp4`, and write `<output-dir>/share-copy.txt`.

**Gate:** `<output-dir>/brag.mp4` exists. Share copy is written.

---

## Tone system

Seven tone presets. Each changes scripting energy, pacing, typography personality, and transition style.

Full definitions: `skills/brag/references/tones.md`

| Tone | Energy | One-liner |
|---|---|---|
| `default` | Playful, clean, postable | The good-vibes default |
| `polished` | Serious, elegant | For projects that are not jokes |
| `yc-parody` | Deadpan startup energy | Fake seriousness applied to absurd projects |
| `chaotic` | Fast, loud, aggressive | Over-the-top and unhinged |
| `deadpan` | Calm, dry, understated | The joke is that nothing is a joke |
| `cinematic` | Dramatic, trailer-scale | Big motion, bigger claims |
| `app-store` | Smooth, feature-card clean | Corporate but not boring |

Always allow a freeform creative direction to refine or override the preset.

---

## Creative laws

These apply to every brag video regardless of tone.

**Short.** 15–25 seconds. Not one second more without a reason.

**Readable.** Keep the pace high through motion and cuts, never by flashing text. Every line a viewer must read holds long enough to read it (short label ~0.8s settled; a sentence ~0.3s per word). Fast-in, then hold — never fast-in, then gone.

**Specific.** The video must feel like it was made for this exact project, not any project.

**Show the thing.** At least one scene must display actual UI, copy, or a key visual from the product. No abstract filler.

**No generic SaaS language.** "Streamline your workflow" is banned. Use the project's actual copy and claims.

**The hook is everything.** The first 2 seconds determine whether someone keeps watching. Plan the hook before anything else.

**Funny earns its place.** Humor should come from the project's absurdity, not from trying to be funny.

**Pattern:**
```
Hook (2-3s) → Reveal (2-4s) → 2-3 sharp highlights (5-12s) → Punchline/outro (2-4s)
```

Adapt this. Not every project needs exactly 3 highlights. The pattern is a starting shape, not a template.

## Asset reference

All skill assets live under `skills/brag/`:
- `skills/brag/assets/music/` — bundled music tracks (MP3)
- `skills/brag/assets/music/cues/` — beat cue presets per track
- `skills/brag/assets/sfx/` — sound effects (OGG, WAV)
- `skills/brag/references/` — step-by-step guides, tone definitions, audio docs
- `skills/brag/scripts/` — analysis tools (music cue analyzer via Python/uv)

## Requirements (for the user's environment)

- Node.js 22+
- FFmpeg on `PATH`
- Hyperframes CLI (`npx hyperframes doctor` to verify)
