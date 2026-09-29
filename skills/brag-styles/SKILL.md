---
name: brag-styles
description: Eighteen art-directed visual systems for launch videos, each with a signature motion trick and a matching sound palette. The general sets are quant terminal, riso zine, blueprint, stop-motion collage, newsprint, arcade, receipt, transit map, title sequence and museum placard. The royal sets are Mughal court, Jaipur block print, Versailles, illuminated manuscript, Forbidden City, Ottoman firman, Byzantine mosaic and Maharaja Deco. Use when /brag-slim gets --style, when the user names a look ("make it royal", "like a newspaper", "arcade style"), or when a video needs a stronger identity than the project's own UI.
---

# brag-styles

Each set in `sets/<slug>/` is a complete look: palette, type, texture, one signature move,
transitions and sound. A set changes how the video looks and sounds. The tone preset still
sets the pacing.

| slug | set | best for |
|---|---|---|
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

## Choosing
1. `--style <slug>` wins. Next, a look the user names (match it to the closest slug).
   Otherwise, only if the project's own UI is too plain to carry the video, pick from the
   "best for" column. Say which set you chose in one line.
2. Read **only** `sets/<slug>/set.md`, which is about 25 lines. Open the rest only when you
   need it: the webp frames for composition, `DESIGN.md` for an exact token, and
   `ref/*.html` to lift an ornament. Never load another set.

## Rules
- **It's a video, not a website.** The Stitch frames are dressed as web pages. Drop their
  chrome: navigation, buttons, tiny labels, side panels, "dossier" and spec blocks.
  Keep the palette, type, ornament and composition.
- **Frame:** 1920x1080. Every reference frame the audit flagged as overflowing must be recomposed.
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
- Render stills and the final video with the `fast-render` skill.

## Adding a set
Write a Stitch prompt modelled on any `sets/*/stitch.md` and export the result from Stitch.
Add its folders to the `SETS` table in `scripts/import_stitch.py`, then run it on the export.
The importer localises images, sanitises the markup, re-renders the frames and writes the
import report. Then write the set's `set.md`, following the others.
