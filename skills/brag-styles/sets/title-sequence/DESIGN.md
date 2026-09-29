---
name: Kinetic Cut
colors:
  surface: '#fff8ef'
  surface-dim: '#e3d9c3'
  surface-bright: '#fff8ef'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fdf3dc'
  surface-container: '#f7edd6'
  surface-container-high: '#f1e7d0'
  surface-container-highest: '#ece2cb'
  on-surface: '#201b0d'
  on-surface-variant: '#5b403b'
  inverse-surface: '#353021'
  inverse-on-surface: '#faf0d9'
  outline: '#8f706a'
  outline-variant: '#e4beb7'
  surface-tint: '#b7210c'
  primary: '#b41f09'
  on-primary: '#ffffff'
  primary-container: '#d83922'
  on-primary-container: '#fffbff'
  inverse-primary: '#ffb4a6'
  secondary: '#7c5800'
  on-secondary: '#ffffff'
  secondary-container: '#fdbf40'
  on-secondary-container: '#6f4e00'
  tertiary: '#5d5c5b'
  on-tertiary: '#ffffff'
  tertiary-container: '#767474'
  on-tertiary-container: '#f7feff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad4'
  primary-fixed-dim: '#ffb4a6'
  on-primary-fixed: '#3f0300'
  on-primary-fixed-variant: '#900e00'
  secondary-fixed: '#ffdea8'
  secondary-fixed-dim: '#fabc3e'
  on-secondary-fixed: '#271900'
  on-secondary-fixed-variant: '#5e4200'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474646'
  background: '#fff8ef'
  on-background: '#201b0d'
  surface-variant: '#ece2cb'
typography:
  display-hero:
    fontFamily: Oswald
    fontSize: 96px
    fontWeight: '700'
    lineHeight: 96px
    letterSpacing: -0.02em
  display-hero-mobile:
    fontFamily: Oswald
    fontSize: 52px
    fontWeight: '700'
    lineHeight: 54px
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: Oswald
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 52px
    letterSpacing: 0em
  headline-lg-mobile:
    fontFamily: Oswald
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 36px
    letterSpacing: 0em
  headline-md:
    fontFamily: Oswald
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: 0.02em
  headline-sm:
    fontFamily: Oswald
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 24px
    letterSpacing: 0.04em
  body-lg:
    fontFamily: Space Grotesk
    fontSize: 18px
    fontWeight: '500'
    lineHeight: 28px
  body-md:
    fontFamily: Space Grotesk
    fontSize: 15px
    fontWeight: '400'
    lineHeight: 22px
  body-sm:
    fontFamily: Space Grotesk
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 18px
  label-lg:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.08em
  label-md:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 14px
    letterSpacing: 0.06em
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 10px
    fontWeight: '500'
    lineHeight: 12px
    letterSpacing: 0.1em
spacing:
  gutter: 1.5rem
  margin: 2rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 2rem
  space-xl: 3.5rem
---

## Brand & Style

This design system channels the mid-century cinematic title sequence mastery of Saul Bass. It embodies suspense, graphic economy, and tactile geometry. Designed for avant-garde cultural platforms, film distribution services, and archival cinema applications, the interface evokes the raw tension of construction paper sliced with an X-Acto blade.

The design movement is an unyielding synthesis of **High-Contrast Brutalism** and **Mid-Century Graphic Modernism**. The visual language discards digital polish in favor of visceral, physical collage:
- Every shape suggests an intentional cut: jagged, deliberate, sharp, and unbalanced.
- Dramatic scale contrasts evoke classic opening credit typography—shifting radically from towering condensed titling to stark, precise body copy.
- Negative space is treated as an active cutting mat rather than passive void.
- Animation and transitions must mimic mechanical stop-motion, rapid cell cuts, and sudden slide transformations rather than soft fades or smooth easing.

## Colors

The palette is strictly restricted to four foundational screen-print tones. No tints, no translucencies, and no intermediate opacities are permitted.

- **Primary (`#e8452c` - Vermilion):** The color of pure visceral impact, urgent focal points, active states, and focal title bars.
- **Secondary (`#e0a526` - Mustard):** A counter-accent evoking mid-century industrial paper stocks, secondary tags, and highlighted states.
- **Tertiary (`#111111` - Pitch Black):** The silhouette tone. Used for dominant typographic mass, heavy structural framing, and foundational framing cutouts.
- **Neutral (`#f3e9d2` - Cream):** The base newsprint canvas. Warm, fibrous, and unbleached, providing an organic counterweight to harsh geometries.

Contrast rules require pure flat collisions: Vermilion over Cream, Cream over Pitch Black, or Pitch Black against Mustard. Avoid placing Vermilion directly on Mustard without a Black silhouette separator to preserve visual legibility.

## Typography

Typography functions as visual architecture rather than mere text. Headings utilize `Oswald` in heavy weights, rendered predominantly in uppercase to evoke screen-printed poster graphics. Baselines should occasionally feature subtle stepped vertical offsets (via span transforms or irregular margins) to mimic hand-placed woodblock or cut-out lettering.

Body text uses `Space Grotesk`, offering angular, functional legibility that complements the geometric framing. Technical annotations, metadata, indices, and timecodes leverage `JetBrains Mono`, establishing a stark contrast between raw theatrical titling and clinical production notes.

## Layout & Spacing

The layout operates on an asymmetric, dynamic grid system inspired by cinematic framing and modular montage sequences.

- **Desktop (12 Columns):** Asymmetrical alignments. Content blocks group into alternating bands of high-density text and expansive, empty cut fields. Columns feature deliberate diagonal and staggered offsets.
- **Tablet (8 Columns):** Standardized collapse of diagonal offsets into stacked horizontal bands with high-contrast dividing bars.
- **Mobile (4 Columns):** Monolithic, full-bleed cards separated by solid bars. Gutters shrink to `1rem` and canvas margins to `1rem`.

Elements do not conform to soft fluid scaling; they snap hard across breakpoints. Layout transitions should feel like direct film splices: abrupt, confident, and unapologetic.

## Elevation & Depth

True to the cut-paper mandate: **Drop shadows, blur radii, and luminous gradients are strictly banned.**

Visual depth is conveyed through:
1. **Collage Layering:** Structural shapes physically overlap. A red quadrilateral laps over a black block, which slices beneath cream text.
2. **Hard Silhouettes:** High-contrast structural boundaries produce the sensation of paper layers resting directly against the frame.
3. **Hard Offset Casts:** When spatial displacement is required (such as hover states or active overlays), an element renders a duplicate silhouette offset by exactly 4px horizontally and 4px vertically in solid `#111111` with no blur.
4. **Tactile Grain:** An SVG-based monochromatic noise mask applied across the canvas simulating heavyweight 80lb archival paper.

## Shapes

The roundedness level is strictly `0` (Sharp). 

Every border radius is `0px`. Forms are characterized by:
- Razor-sharp 90-degree corners.
- Asymmetrical diagonal corner trims (achieved through CSS `clip-path: polygon(...)`) to simulate angled shears from shears or razor blades.
- Jagged horizontal dividers and asymmetrical wedges slicing across panels to define content zones.

## Components

### Buttons
- **Primary:** Background `#e8452c`, text `#f3e9d2`, zero radius, heavy uppercase Oswald tracking. On hover: shifts by `-2px, -2px` with a flat `#111111` 4px solid backing block.
- **Secondary:** Solid `#111111` fill with `#f3e9d2` text. Hover turns the background to `#e0a526` with immediate snap.
- **Ghost/Tertiary:** 2px solid `#111111` frame with no fill; text in `#111111`. Invert completely on hover.

### Chips & Badges
- Sharp-edged rectangles framed in 1.5px solid `#111111`.
- Backgrounds are strictly solid `#e0a526` or `#f3e9d2`.
- Text styled in `JetBrains Mono` bold uppercase with high tracking.

### Cards & Panels
- Constructed using thick, framing outer borders (`2px` to `4px` solid `#111111`).
- Card headers utilize inverted black cut bars (`#111111` background with `#f3e9d2` text).
- Asymmetrical bottom-right bevels or angled edge cuts via clip paths provide the iconic cut-paper profile.

### Form Inputs
- Flat `#f3e9d2` surface bounded by a heavy 2px `#111111` underline or full frame.
- Focus state: Outline snaps to 3px solid `#e8452c` with zero transition delay.
- Placeholder text in `#111111` with 50% solid pattern or monospace brackets (`[ TYPE HERE ]`).

### Checkboxes & Radios
- Checkboxes: Rigid 18px by 18px square, 2px `#111111` border. Checked state displays a solid inner `#e8452c` square or diagonal slash.
- Radios: Kept strictly diamond-shaped (square rotated 45 degrees) rather than circles to preserve angular brutality.

### Title Sequences & Slates (Domain-Specific)
- **The Marquee Bar:** Full-width `#e8452c` or `#111111` horizontal ribbons containing ticker-style metadata.
- **The Split Slate:** A split-screen 50/50 block slicing cream and vermilion with opposing high-contrast text locked across the division line.