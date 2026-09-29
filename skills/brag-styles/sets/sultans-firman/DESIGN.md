---
name: Imperial Firman Storyboard
colors:
  surface: '#fdf8f6'
  surface-dim: '#ddd9d7'
  surface-bright: '#fdf8f6'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f7f3f0'
  surface-container: '#f2edeb'
  surface-container-high: '#ece7e5'
  surface-container-highest: '#e6e2df'
  on-surface: '#1c1b1a'
  on-surface-variant: '#434751'
  inverse-surface: '#31302f'
  inverse-on-surface: '#f4f0ee'
  outline: '#737782'
  outline-variant: '#c3c6d3'
  surface-tint: '#315cab'
  primary: '#00377d'
  on-primary: '#ffffff'
  primary-container: '#1f4e9c'
  on-primary-container: '#aac3ff'
  inverse-primary: '#aec6ff'
  secondary: '#755b00'
  on-secondary: '#ffffff'
  secondary-container: '#fed255'
  on-secondary-container: '#735a00'
  tertiary: '#731500'
  on-tertiary: '#ffffff'
  tertiary-container: '#9c2000'
  on-tertiary-container: '#ffb09d'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d8e2ff'
  primary-fixed-dim: '#aec6ff'
  on-primary-fixed: '#001a43'
  on-primary-fixed-variant: '#0e4491'
  secondary-fixed: '#ffe08e'
  secondary-fixed-dim: '#ecc246'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#584400'
  tertiary-fixed: '#ffdad2'
  tertiary-fixed-dim: '#ffb4a3'
  on-tertiary-fixed: '#3d0700'
  on-tertiary-fixed-variant: '#8a1b00'
  background: '#fdf8f6'
  on-background: '#1c1b1a'
  surface-variant: '#e6e2df'
typography:
  display-lg:
    fontFamily: EB Garamond
    fontSize: 56px
    fontWeight: '700'
    lineHeight: 64px
    letterSpacing: 0.06em
  display-lg-mobile:
    fontFamily: EB Garamond
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 44px
    letterSpacing: 0.04em
  display-md:
    fontFamily: EB Garamond
    fontSize: 40px
    fontWeight: '600'
    lineHeight: 48px
    letterSpacing: 0.05em
  display-md-mobile:
    fontFamily: EB Garamond
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 36px
    letterSpacing: 0.04em
  headline-lg:
    fontFamily: EB Garamond
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: 0.03em
  headline-md:
    fontFamily: EB Garamond
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: 0.02em
  headline-sm:
    fontFamily: EB Garamond
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
    letterSpacing: 0.02em
  body-lg:
    fontFamily: EB Garamond
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: EB Garamond
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: EB Garamond
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-lg:
    fontFamily: EB Garamond
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 18px
    letterSpacing: 0.12em
  label-md:
    fontFamily: EB Garamond
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.14em
  label-sm:
    fontFamily: EB Garamond
    fontSize: 10px
    fontWeight: '700'
    lineHeight: 14px
    letterSpacing: 0.16em
spacing:
  gutter: 1.5rem
  gutter-sm: 1rem
  gutter-lg: 2rem
  margin: 2.5rem
  margin-sm: 1.5rem
  margin-lg: 4rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.5rem
---

## Brand & Style

This design system translates the monumental gravitas, manuscript illumination (*tezhip*), and ceramic mastery of the high Ottoman court into a cinematic production dashboard and storyboard interface. Designed specifically for creative directors, cinematographers, and production designers directing an imperial historical narrative, the UI reconciles manuscript pageantry with digital production precision.

The design movement combines **Classical Manuscript Illuminism** with **Restrained Editorial Structure**:
- **Parchment Architecture:** The canvas behaves like treated rag paper (*aharli kagit*), offering calm ivory central work areas framed by layered filigree borders, gilded rules, and subtle marbled framing strips.
- **Controlled Ornamentation:** Ornamental complexity is relegated to the perimeter—Ebru marbled margins (*ebru pervaz*), saz-leaf motifs, and Seljuk star markers—while interactive working zones remain pure, sharp, and legibly architectural.
- **Cinematic Production Utilitarianism:** Shot parameters, aspect ratio frames (2.39:1 / 16:9), focal lengths, and scene cues are held in structured, sharp panels rendered in deep iron-gall ink lines and illuminated gold tags.

## Colors

The palette directly references the imperial workshops of Topkapı and the master kilns of Iznik:

- **Ivory Paper Ground (`#f4ecda`):** The non-emissive base canvas of the entire interface. It mimics sized and burnished egg-white/starch paper, providing high readability without the ocular fatigue of stark digital white.
- **Iznik Cobalt (`#1f4e9c` - Primary):** The authoritative, intense blue found under deep quartz glazes. Used for key structural anchors, active states, timeline scrubbers, and primary calls-to-action.
- **Metallic Gilt / Gold Foil (`#c9a227` - Secondary):** The color of powdered leaf gold (*zerkari*). Reserved for frame embellishments, focus indicators, active scene markers, shot numbers, and high-status badges.
- **Tomato Red / Iznik Cinnabar (`#c73e1d` - Tertiary):** An assertive, slightly textured red derived from iron-rich Armenian bole. Used strictly for directorial warnings, critical timeline notes, live-recording indicators, and imperial stamp vectors.
- **Turquoise (`#2aa3a8`):** Complementary accent representing copper-oxide Iznik glaze. Applied to camera move vectors, lighting callouts, and audio layer tags.
- **Deep Charcoal / Iron Ink (`#1a1918` - Neutral):** Pure carbon and iron-gall ink. Used for crisp typographic hierarchy, borders, fine double rules, and primary metadata.

Surfaces use slight opacity shifts (`rgba(244, 236, 218, 0.92)`) overlaid against Ebru marbled backdrop plates for navigation ribbons and floating inspector panels.

## Typography

The typographic hierarchy uses classical proportions rooted in high Renaissance and monumental Latin engraving:

- **EB Garamond** acts as the unified system typeface across all roles, selected for its authentic humanistic book weight, classical Roman proportions, and authoritative capital forms that echo monument inscriptions.
- **Display & Headline Levels:** Headlines employ generous letter-spacing (`0.03em` to `0.06em`) and small-caps formatting where appropriate to evoke the permanence of stone-carved dedications and imperial edicts.
- **Labels & Film Slate Metadata:** Shot numbers, focal lengths, camera tags, and scene timecodes use uppercase `label-sm` and `label-md` variants with tracking up to `0.16em`. This maintains crisp, ledger-style clarity without needing anachronistic monospaced typefaces.
- **Editorial Text Panels:** Storyboard narrative beats, directorial commentary, and voiceover scripts are rendered in `body-lg` (18px) with a generous 1.55 line-height ratio, honoring the open cadence of classical illuminated manuscripts.

## Layout & Spacing

The layout is structured around an **Illuminated Columnar Grid** inspired by codex layout canons:

- **Master Composition:** A 12-column dynamic desktop grid with wide outer margins (`2.5rem` to `4rem`) resembling the expansive unwritten borders of a royal firman. Inner work panes sit inside double-ruled gold and ink boundaries.
- **Storyboard Viewport:** Central canvas cards maintain fixed cinematic aspect ratios (16:9 for composition previews, 2.39:1 for widescreen epic framing) resting within ivory reading enclosures surrounded by metadata sidecars.
- **Breakpoint Logic:**
  - **Desktop (≥ 1280px):** 12 columns, `1.5rem` gutters, `2.5rem` margins. Three-pane setup: Scene Navigator (left, 2 cols), Main Frame & Animatics (center, 7 cols), Script & Camera Inspector (right, 3 cols).
  - **Tablet (768px - 1279px):** 8 columns, `1rem` gutters, `2rem` margins. The Inspector drops into a collapsible side-drawer; storyboard frames stack horizontally with scroll-snap.
  - **Mobile (< 768px):** 4 columns, `1rem` gutters, `1.5rem` margins. Single-column card stack with top-anchored scene controls.

## Elevation & Depth

Visual hierarchy rejects synthetic digital drop shadows in favor of **Manuscript Layering & Inlaid Relief**:

- **Tonal Stepping:** Depth is achieved by placing pale ivory work panels (`#fbf8f0`) above the raw parchment base (`#f4ecda`), separated by fine rules instead of heavy blur shadows.
- **Double-Rule Boundaries:** Panels use a distinctive framing device: an outer `1px` rule of deep iron ink (`#1a1918`), an interior spacing gap of `3px`, and an inner `1px` rule of metallic gilt (`#c9a227`). This replicates the framed *cedvel* borders of Ottoman miniature paintings.
- **Illuminated Overlays:** Floating contextual menus and playhead heads cast an ambient, highly diffuse warm glow: `box-shadow: 0 4px 20px -2px rgba(26, 25, 24, 0.12), 0 0 12px 1px rgba(201, 162, 39, 0.18)`.
- **Gilt Accents & Stamping:** Active selections and hovered storyboard cards receive an inset border highlight (`inset 0 0 0 1px #c9a227`) along with an eight-pointed Seljuk star badge at the top-right corner.

## Shapes

The interface embraces a **Sharp architectural geometry (`roundedness: 0`)**:

- **Strict Orthodoxy:** Corners across cards, buttons, badges, viewports, and modals remain strictly at `0px`. This reflects the sharp-edged trimming of handmade royal parchment sheets and the architectural masonry of the Topkapı pavilions.
- **Corner Notching & Chamfers:** Specific featured panels (such as active shot animatics or key script cues) incorporate a 45-degree `4px` chamfered or notched corner, referencing stone-carved cartouches and ceramic tile edge bevels.
- **Medallion Motifs:** Geometric eight-pointed Seljuk stars (`polygon` SVG masks) are employed as scene anchor tags, shot number medallions, and status glyphs.

## Components

### Buttons
- **Primary (Imperial Command):** Iznik Cobalt background (`#1f4e9c`), crisp white/ivory text, framed with an outer `1px` metallic gold border (`#c9a227`). Hover state brightens to `#265cb8` with a warm gold ambient halo.
- **Secondary (Scribe's Action):** Ivory ground (`#f4ecda`), deep iron ink text (`#1a1918`), double-line border (iron outer, gilt inner).
- **Destructive / Alert:** Tomato red (`#c73e1d`) ground with gold serif lettering.

### Chips & Shot Badges
- Hexagonal or rectangular sharp badges with `1px` gold foil outlines.
- Camera focal length chips (e.g., `35MM`, `ANAMORPHIC`) sit in `#1a1918` background with `#f4ecda` text and `#c9a227` corner pips.
- Scene mood tags use turquoise (`#2aa3a8`) or cinnabar (`#c73e1d`) tint fills at 12% opacity with solid text.

### Storyboard Cards
- Composed of three tiers:
  1. **Header Bar:** Scene index, Seljuk star sequence marker, shot timecode.
  2. **Viewport Frame:** 16:9 or 2.39:1 letterboxed video/sketch canvas bordered by fine double rules.
  3. **Script Footer:** Direction notes, camera motion vectors (pan/tilt indicated by gilded arrows), and dialogue lines set in `body-sm`.
- Active state draws a complete outer perimeter of Ebru-patterned hairline trim (`2px`).

### Lists & Scene Outliners
- Horizontal scene ribbons with alternating subtly tinted parchment bands (`#f4ecda` to `#ede3cd`).
- Left indicator strips use Iznik Cobalt for dialogue scenes, Tomato Red for action sequences, and Turquoise for exterior/ambient sequences.
- Dividers are fine ornamental gilt rules terminating in tiny diamond rosettes.

### Checkboxes & Radio Elements
- Custom square markers (`14px × 14px`) with `1px` iron ink borders.
- Checked state fills with Iznik Cobalt and reveals a centered, sharp gold four-point star glyph instead of a conventional checkmark.

### Input Fields & Director Slates
- Pristine ivory fields bordered with a single `1px` line in `#1a1918` that transitions to a double gold line on focus.
- Labels sit above the field in uppercase `label-md` accompanied by roman numeral numbering.

### Invented Latin Monogram Stamp
- An imperial signet placed on key storyboard approvals: an intricate, bespoke calligraphic Latin monogram (composed of interlaced Roman capitals) enclosed within an eight-pointed gilded cartouche, serving as an authentic seal of scene sign-off.