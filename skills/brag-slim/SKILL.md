---
name: brag-slim
description: Turn a project directory, a website URL, a script, a folder of screenshots or a recorded clip into a short, shareable video with music, motion, and share copy. One file, no bundled assets — built entirely by the model with the tools already on the machine. Use when someone says "/brag-slim", "let's /brag about this", "brag about <url>", "make a launch video", or wants to show off what they built. If the /brag skill is also installed, let /brag handle those phrases; it hands off here on Opus 5.5.
---

# /brag-slim

You built it. Now brag. You make the whole video yourself — story, visuals, audio, render — with whatever tools are on the machine.

Whatever the tone, it should feel like a modern, slick, polished launch video: nothing on screen or in the soundtrack that doesn't earn its place.

Usage: `/brag-slim [input] [options]`. Options (flags or plain language):

| Option | Default |
|---|---|
| `--tone <preset or freeform>` | inferred; `default` if nothing clearly fits |
| `--format landscape\|vertical\|square` | landscape (1920×1080; vertical 1080×1920, square 1080×1080), 30fps |
| `--fps <n>`, `--4k`, `--transparent` | 30 fps, 1080p, opaque MP4. `--4k` renders at twice the size; `--transparent` writes ProRes 4444 with alpha (and a PNG sequence) for an editor |
| `--duration <s>` | about 20s |
| `--voice [voice]` | off; narration with the `narrate` skill (default voice `af_heart`) |
| `--style <set \| options \| auto>` | recommend, then wait for a pick. A set name builds with it; `options` only recommends; `auto` picks the best set and builds. There are 21 sets in `brag-styles`, including doodle, ops desk, kinetic type, quant terminal, riso, arcade, Mughal court and Versailles |

## What's in the box

Four more skills ship beside this one. Every run can use them, and the user should know they exist:

| Skill | What it adds | How to ask |
|---|---|---|
| `brag-styles` | 21 art-directed looks, each with a signature move and its own sound palette; recommends before building | `--style`, "give me style options", "make it royal" |
| `motion-kit` | The moves, pacing rules, cursor-and-camera engines, code-made sound and the activity audit that keep a video from playing like a slideshow | automatic for every build; "make it interactive", "it feels like slides" |
| `narrate` | Offline voiceover (bundled Kokoro-82M, no API key), with the music ducked under the voice; also word timings from a recorded clip | `--voice`, "narrate it" |
| `fast-render` | GPU frame capture in parallel browsers; stills, poster, 4K, transparent export, graphics laid over footage, and a setup check (`--doctor`) | automatic for every render |

Longer pieces work too. Past about a minute (an explainer, a pitch, a YouTube video) the Short law below gives way: write and synthesize the narration first, cut the piece into chapters fitted to the voice, burn in captions timed to each line, and give each chapter its own set if a mix of looks suits it.

In your first reply of a run, say in one line which of these you're using and which are available but off, e.g. "Narration is off; say `--voice` to add it."

Write the deliverables to `brag-output/` in the current directory (timestamped `brag-output-YYYY-MM-DD-HHmmss/` if it already exists). Keep every intermediate file (frames, downloads, scripts, stems) in a `work/` subfolder inside it.

## 1. Inspect

First decide what the input is, then gather material from it. Only the source changes; everything from the questions below onward is the same for every input.

| Input | How to recognize it | Where the material comes from |
|---|---|---|
| Project | No input given, and the current directory is a project | The code |
| Website | An `http(s)://` URL, or a bare domain like `example.com` | The live site |
| Script | Quoted text, a text file, or "a video of just these words" | The words themselves |
| Screenshots | A folder of images of the product | The screens as they are |
| Clip | A video file, or "add graphics to my video" | The recording and what is said in it |

If the input matches no type, or there's no input and the current directory isn't a project, ask the user what to brag about.

### Project

Read the code: the main page, styles (exact colors and fonts), README, routes and key components. The best material is the product **in use** — find its 2–3 beats: entry → key action → result.

You have the source, so use it directly: import or render the project's real components, stylesheets, fonts, images and animations in the video instead of rebuilding them.

### Website

Get the site as a visitor sees it. Many sites build their page with JavaScript, so a plain download can come back as an almost empty shell. If it does, load the page in a headless browser to get the rendered result. Dismiss cookie banners and other overlays, and scroll section by section, since content that animates in on scroll stays blank in a single full-page capture.

- **Copy:** headline, tagline, section headings, feature names, calls to action, testimonials. Also check the title, meta description and social-preview tags.
- **Identity:** exact colors from the site's CSS and the fonts it loads.
- **Visuals:** the logo, product screenshots, hero images, demo videos. Download the ones you'll use into `work/`.
- **Screenshots:** capture the page at the video's aspect ratio to understand the layout. In the video, reuse the site's real markup, CSS and assets and animate those, rather than panning over flat screenshots.
- **The product in use:** check the demo videos, how-it-works sections and linked docs for the entry → key action → result flow.

### Script

Use the exact words: do not rewrite, shorten or reorder them. One sentence per screen, large enough to read on a phone, wrapped over more lines rather than shrunk. The `kinetic-type` set in `brag-styles` is built for this and carries a working engine; another set can dress it if the user picks one.

### Screenshots

Look at every image first and work out what each one shows and which part matters (the number, the chart, the button). Use the screens as they are: never redraw them. The video is a camera moving over real screens: zoom into the part that matters, say in a short line what it does for the customer, move on. Open with a hook and end on the name, one line and the call to action.

### Clip

The recording stays exactly as it is: same size, frame rate, cut and audio. You add graphics on top, each made for what is being said at that moment and starting on the exact word: a spoken number becomes a counter, a list becomes a checklist, a before and after becomes a comparison. Follow "Graphics on footage" in `motion-kit` (`../motion-kit/SKILL.md`): transcribe for word timings, keep one style throughout, add nothing in the first 3 seconds, and keep off the speaker's face, the bottom third and the outer 10% of the width. Deliver `with-graphics.mp4`; skip the poster and music steps unless asked.

### Then, for every input

Before planning, answer: What is it (one sentence)? Who is it for, and what does it do for them? What sets it apart? What's the most impressive or funniest claim? What's the visual hook? What real UI or flow should be shown? What tone fits? What's the one-line share caption?

## 2. Plan

Write `brag-plan.md`: the angle, the hook, 2–3 highlights, the punchline, tone, visual identity, and a scene-by-scene storyboard with durations that sum to the target.

If the user points at one part — a new version, a new feature, one angle — make this the focus of the video.

**Shape:** Hook (2–3s) → Reveal (2–4s) → 2–3 sharp highlights → Punchline/outro (2–4s). A starting shape, not a template.

**Style.** After inspecting and before writing `brag-plan.md`, follow the Choosing protocol in the `brag-styles` skill beside this one (`../brag-styles/SKILL.md`). If the user named a set or a vibe, or said to go straight ahead ("just make it", `--style auto`), pick, say which in one line, and continue. If they asked for options, or said nothing about style, recommend one set, a safer and a bolder alternative, and "keep the project's own look", each with a reason drawn from the project, then stop and wait for their pick. The one exception is a project whose own UI can clearly carry the video: then build in its look. Once a set is chosen, read only that set's `set.md`; it sets palette, type, texture, signature move and sound, while the project supplies every word and number. If `brag-styles` isn't installed, say so and design from the project itself.

## Creative laws

- **Short.** 15–25 seconds; 18–22 is the sweet spot.
- **Clear to a stranger.** After one viewing, someone who's never heard of it knows what it does, who it's for, and how to get it. Lead with that, not with how it's built.
- **The hook is everything.** The first 2 seconds decide whether anyone keeps watching. Plan it first.
- **Show the thing.** Reuse the real thing from the source — its UI, components, copy, images, videos and animations — rather than re-creating it. Rebuild only what you can't reuse. Prefer the working app doing its job over a landing page describing it. Small illustrative UI text is fine when showing the product in use (a filename, an "Exported" toast); invented claims, numbers, or testimonials are not. Never abstract filler.
- **Specific.** It must feel made for this exact project. Use its own copy and claims; no generic SaaS language ("streamline your workflow" is banned).
- **Readable.** Pace comes from motion and cuts, not from pulling text away early. Any line the viewer is meant to read stays fully visible and settled long enough to read it (roughly 0.3s per word), counted from when the whole line is on screen. Text that's only texture doesn't need to be read.
- **Never a slideshow.** A scene with nothing performing in it is a slide. Give every scene a performer (a cursor, a pen, a camera), make each action cause something at once, and leave a scene within a beat of its payoff. The `motion-kit` skill beside this one (`../motion-kit/SKILL.md`) has the moves, the engines and the rules; read it before writing scenes.
- **Funny earns its place.** Humor comes from the project's own absurdity, not from trying.
- **Every frame postable.** Any frozen frame should be worth sharing.

## Tones

Presets are defaults; freeform direction ("fake Series A launch from 2016") refines or overrides them.

| Tone | Feel | Pacing / transitions |
|---|---|---|
| `default` | Punchy, playful, clean | 4–5 scenes; soft transitions |
| `polished` | Serious, elegant, restrained | 3–4 scenes, long holds; soft fades |
| `yc-parody` | Deadpan startup launch, played straight | 4–5 scenes, one claim each; hard cuts |
| `chaotic` | FAST, LOUD, ALL CAPS | 6–8 scenes, some under 2s; flash/zoom cuts |
| `deadpan` | Calm, dry, nothing is a joke | 3–4 scenes, big empty space; slow fades |
| `cinematic` | Trailer-scale, epic claims | 4–5 scenes, big type; dramatic wipes |
| `app-store` | Clean feature cards | 4–6 scenes; smooth slides |

## Sound

Write the music and sound effects as one piece: effects in the same key and the same space as the music, blended in rather than laid on top. `motion-kit` ships `scripts/soundkit.py`, which makes every sound in code and turns the page's cue list into a track; use it rather than writing synth code again. Put a sound on what matters (a tick, a count, the last card), not on every slide-in, and let the music gain a layer as things complete. Give it a basic, proper mix, the way a real track is mixed: effects sit softly under the music, nothing harsh or spiky, and repeated little sounds stay in the background.

Narration is off unless asked for (`--voice`, "narrate it", "add a voiceover"). When it's on, use the `narrate` skill beside this one (`../narrate/`). Write the voiceover while planning — one short line per beat, saying what the screen can't — then synthesize it *before* timing scenes, and fit each scene to its line's real duration. Mix the music and effects under the voice (the skill ducks the music); nothing should compete with a spoken word. If `narrate` isn't installed, say so and deliver without narration.

## 3. Build, check, render

Build it with whatever works on this machine. If you draw the video in a browser, make every frame a pure function of time and wait for fonts and images to load before capturing each one.

Frame capture is usually the slowest step, so set it up for speed before the full render. If the `fast-render` skill sits beside this one (`../fast-render/scripts/fastrender.py`), use it for stills and the render and skip the rest of this paragraph; it does all of the following. Headless Chromium often rasterizes on the CPU: read the WebGL renderer string, and if it says SwiftShader, relaunch on the GPU (on Windows, `--use-angle=d3d11 --force_high_performance_gpu`; elsewhere, the platform's ANGLE GPU backend) and confirm the string changed. Render contiguous chunks of the timeline in parallel browsers, pipe each captured frame straight into the video tool instead of writing images to disk, and run the final encode after capture finishes — a hardware encoder sharing the GPU with rasterization can cut throughput by more than half.

Before the full render, run `fastrender.py video.html --audit` and fix every quiet stretch it lists that is not the held end card: a video that is quiet a third of the time plays like a slideshow, however good each frame looks. Then look at stills from every scene *and* from mid-transition, and fix overflow, collisions, and low contrast. A plain crossfade between two busy layouts makes a muddy double exposure; stagger it (old content out, then new content in) or dip through the background. Then render `brag.mp4`.

## 4. Deliver

- **Poster:** pull the strongest *settled* frame (text fully in, not mid-transition) to `brag.jpg`, and bake it in as frame 0 of `brag.mp4` so every platform's thumbnail shows it. Replace frame 0 rather than adding a frame, so the duration and audio sync stay the same.
- **`share-copy.txt`:** 1–3 sentences, postable as-is, specific, matching the tone. No "excited to share."
- **Tell the user** where the video and copy are, give one sentence on the creative angle, and offer to re-roll a scene, try another tone, or add whatever this run left off (a style set, narration, another format).

## 5. Revise

A change request after a render is a change to one thing. Change that thing, keep everything else exactly as it was, and render to the same file. When the user names a moment, they name it by what is on screen or what is said ("when it says forty a week"), not by a timestamp: find it, change it, leave the rest. If a font shows as a plain fallback, the file did not load: fix the link or bundle the font, never ship the fallback. If the file is too large to share, render again with `--crf 23`.
