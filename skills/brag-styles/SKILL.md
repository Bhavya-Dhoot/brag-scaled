---
name: brag-styles
description: Twenty-one art-directed visual systems for launch videos, each with a signature motion trick and a matching sound palette. The general sets are doodle, ops desk (a bento board operated by a cursor), kinetic type, quant terminal, riso zine, blueprint, stop-motion collage, newsprint, arcade, receipt, transit map, title sequence and museum placard. The royal sets are Mughal court, Jaipur block print, Versailles, illuminated manuscript, Forbidden City, Ottoman firman, Byzantine mosaic and Maharaja Deco. It recommends a set and waits for a pick when asked for options; it builds straight away when told to. Use when /brag-slim gets --style, when the user asks for style options or a recommendation, when they name a look ("make it royal", "like a newspaper", "arcade style"), or when a video needs a stronger identity than the project's own UI.
---

# brag-styles

Each set in `sets/<slug>/` is a complete look: palette, type, texture, one signature move,
transitions and sound. A set changes how the video looks and sounds. The tone preset still
sets the pacing.

| slug | set | best for |
|---|---|---|
| `doodle` | Doodle | pitches, services and consulting, how-it-works explainers, friendly B2B, education |
| `ops-desk` | Ops Desk | B2B tools, services and automation, dashboards; a demo that is operated on screen |
| `kinetic-type` | Kinetic Type | a script with no footage, hooks, opinions, vertical video for phones |
| `exchange-floor` | Exchange Floor | fintech, data tools, dev infrastructure, anything with real metrics |
| `riso-zine` | Riso Zine | indie apps, creative tools, community products, anything with personality |
| `patent-office` | Patent Office | hardware, APIs, developer tools, anything architectural |
| `stop-motion-collage` | Stop-Motion Collage | consumer apps, food, lifestyle, education, kids' products |
| `extra-extra` | Extra! Extra! | big announcements, B2B launches, data or insight products |
| `insert-coin` | Insert Coin | games, playful consumer apps, dev tools with a sense of humour |
| `the-receipt` | The Receipt | fintech, commerce, productivity ("time saved"), anything you can itemise |
| `transit-map` | Transit Map | workflows, pipelines, onboarding, integrations, multi-step products |
| `title-sequence` | Title Sequence | cinematic launches, security, AI, anything with drama |
| `museum-placard` | Museum Placard | design tools, premium products, anything that deserves to be taken seriously |
| `shahi-darbar` | Shahi Darbar | premium products and Indian-market launches; anything worth announcing like an imperial *farman* |
| `jaipur-block-print` | Jaipur Block Print | consumer, fashion and craft brands, D2C, anything tactile or handmade |
| `court-of-versailles` | Court of Versailles | luxury, premium SaaS with a sense of humour, "launch-day gala" moments |
| `illuminated-manuscript` | Illuminated Manuscript | knowledge tools, writing apps, docs products, AI that "writes", anything with a history to tell |
| `forbidden-city` | Forbidden City | launches aimed at China or Asia, craft and precision products, calm and confident brands |
| `sultans-firman` | The Sultan's Firman | bold announcements, fintech and legal tech ("decreed"), anything that should feel official |
| `byzantine-gold` | Byzantine Gold | community and social products, "built piece by piece" stories, data made of many parts |
| `maharaja-deco` | Maharaja Deco | premium launches, hospitality and finance, anything glamorous with rigour |

## Choosing: recommend first, build second

Work out which mode the request is in before doing anything else.

| The user… | Do this |
|---|---|
| names a set (`--style <slug>`, "the receipt one") | Use it. Say which in one line, then build. |
| names a vibe ("royal", "retro", "like a newspaper") | Map it to the closest set, say which in one line, then build. |
| asks for options in any wording: options, choices, suggestions, "which style/look?", "what would work?", "show me looks", `--style options` | **Recommend, then stop.** Present the options below and wait for their pick. Build nothing. |
| says to go straight ahead ("just make it", "create it directly", "your call", `--style auto`) | Pick the recommended set, say which and why in one line, then build. |
| asks for a video and says nothing about style | **Recommend, then stop**, unless the project's own UI is strong enough to carry the video. In that case, build in the project's look and mention in one line that styles are available. |

**How to present options.** Read the project first, so the recommendation is about this
project and not generic. Then give:

1. **Recommended:** the set that best fits the project's audience and material, with one
   sentence of reasoning that cites something real from the project.
2. **Safer alternative:** the set closest to the project's own brand.
3. **Bolder alternative:** a set that makes the video memorable at some risk to fit.
4. **Or keep the project's own look.** This is always an option.

Give each option one line: its name, its signature move, and why it fits. End with
"Which one? (or say 'go' for the recommendation)". When the user picks, build with that set.
Don't ask again.

**Reading the fit.** Numbers-heavy fintech, data or infrastructure → `exchange-floor`,
`the-receipt`, `patent-office`. A workflow or pipeline → `transit-map`, `patent-office`.
A pitch, service or explainer → `doodle`. A product or service whose value is something broken now working → `ops-desk`. A script and nothing else → `kinetic-type`. Consumer, with personality → `riso-zine`,
`stop-motion-collage`, `insert-coin`. A big announcement → `extra-extra`, `sultans-firman`,
`title-sequence`. Premium or luxury → `court-of-versailles`, `maharaja-deco`,
`museum-placard`. An Indian audience → `shahi-darbar`, `jaipur-block-print`,
`maharaja-deco`. An Asian audience → `forbidden-city`. Writing or knowledge tools →
`illuminated-manuscript`. Community, or "built piece by piece" → `byzantine-gold`.
A royal set only fits when the project can carry grandeur, or plays it as knowing humour.
On a tie, prefer the set whose signature move acts out the project's core action (a matcher → lines converging, a ledger → a receipt printing). Put the runner-up in as the safer or bolder alternative.

**Once a set is chosen,** read **only** `sets/<slug>/set.md`, which is about 25 lines. Open
the rest only when you need it: the webp frames for composition, `DESIGN.md` for an exact
token, and `ref/*.html` to lift an ornament. Never load another set.

**A set is the look, not the motion.** Every build also follows the `motion-kit` skill beside
this one: a performer in every scene, nothing waiting after its payoff, an activity audit
before the render. A set applied to still pages is a slideshow in costume.

## Rules
- **It's a video, not a website.** The Stitch frames are dressed as web pages. Drop their
  chrome: navigation, buttons, tiny labels, side panels, "dossier" and spec blocks.
  Keep the palette, type, ornament and composition.
- **Frame:** 1920x1080 unless the brief is vertical (1080x1920; `kinetic-type` and the motion-kit safe zones cover it). Every reference frame the audit flagged as overflowing must be recomposed.
  Don't shrink them to fit. Readable text is at least 28px, mono labels at least 22px. Keep
  about 12 words on screen per beat, and one focal element per frame.
- **Copy:** every word and number comes from the project. The Stitch copy is placeholder
  (NEXUS, nexus.example, 99.999%, 840 ns, SOC 2, "certified", "granted") and never ships.
- **Signature move:** the set's hook. Play it in full at the reveal, then at most once more
  per scene. Transitions may borrow its mechanism in a short form (under 0.4 s); that
  doesn't count as a repeat.
- **Safe area:** keep all text inside a 120px margin. Inside an arch, frame, card or medallion,
  keep text at least 48px from the ornament, and scale the ornament to the text, never the
  other way round. The focal element should fill 40–60% of the safe area, with no empty
  half-frames.
- **Metallics (gold, gilt, brass, silver):** never a flat yellow or grey. Use a linear gradient
  (dark stop, light stop, dark stop) as `background-clip: text` or as a fill, and sweep its
  position once when the claim lands. Metallic text must still reach 4.5:1 contrast against
  its ground. Add a darker outline or shadow of the same hue if it doesn't.
- **Type from the set:** load it from `https://fonts.googleapis.com/css2?family=<Name+With+Pluses>:wght@<weights>&display=block`.
  In `window.ready`, `await document.fonts.load('<weight> 48px "<Name>"')` for each face. If
  a face fails to load, fix the link; never render with fallback fonts.
- **Imagery:** the `assets/` images are Stitch-generated mood references, and some show fake
  claims. Never put them in the video. Draw the look with CSS, SVG and the project's real UI.
- **Royal and heritage sets:** invent the regalia, and build crests, seals and monograms
  from the project's initials. No real coats of arms, royal warrants, "By Appointment"
  wording, government offices, or transit-authority marks. No script you can't verify
  (Chinese, Arabic, Devanagari) used as ornament. No religious figures, symbols or text,
  and no copied historical figures.
- **Sound:** follow the set's **Sound** line, in the music's key. Effects sit under the
  music; narration, if any, ducks both.

## Building it so it renders fast
- Use plain CSS with the set's hex values as custom properties. Don't put the Tailwind CDN in
  the video page: it fetches over the network and runs a JIT compiler on every load.
- Link the Google Fonts from the **Type** line, and wait for `document.fonts.ready` before the
  first frame.
- Use static textures: grain, paper, halftone and mosaic as a single pre-rendered image or
  canvas drawn once. Don't animate an SVG filter over the whole frame. Keep to one canvas at most.
- Render stills and the final video with the `fast-render` skill, and run its `--audit` first.

## Adding a set
Write a Stitch prompt modelled on any `sets/*/stitch.md` and export the result from Stitch.
Add its folders to the `SETS` table in `scripts/import_stitch.py`, then run it on the export.
The importer localises images, sanitises the markup, re-renders the frames and writes the
import report. Then write the set's `set.md`, following the others.
