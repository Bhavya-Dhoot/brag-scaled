---
name: 8-Bit Arcade CRT Terminal
colors:
  surface: '#13131a'
  surface-dim: '#13131a'
  surface-bright: '#393841'
  surface-container-lowest: '#0e0e15'
  surface-container-low: '#1b1b22'
  surface-container: '#1f1f26'
  surface-container-high: '#2a2931'
  surface-container-highest: '#34343c'
  on-surface: '#e4e1ec'
  on-surface-variant: '#bacaca'
  inverse-surface: '#e4e1ec'
  inverse-on-surface: '#303038'
  outline: '#849494'
  outline-variant: '#3b494a'
  surface-tint: '#00dce5'
  primary: '#edfeff'
  on-primary: '#003739'
  primary-container: '#34f5ff'
  on-primary-container: '#006d72'
  inverse-primary: '#00696e'
  secondary: '#ffb0ce'
  on-secondary: '#63003a'
  secondary-container: '#cd017e'
  on-secondary-container: '#ffe6ed'
  tertiary: '#fffaf7'
  on-tertiary: '#393000'
  tertiary-container: '#fcde4a'
  on-tertiary-container: '#726100'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#67f6ff'
  primary-fixed-dim: '#00dce5'
  on-primary-fixed: '#002021'
  on-primary-fixed-variant: '#004f53'
  secondary-fixed: '#ffd9e5'
  secondary-fixed-dim: '#ffb0ce'
  on-secondary-fixed: '#3e0022'
  on-secondary-fixed-variant: '#8c0054'
  tertiary-fixed: '#ffe256'
  tertiary-fixed-dim: '#e2c633'
  on-tertiary-fixed: '#211b00'
  on-tertiary-fixed-variant: '#534600'
  background: '#13131a'
  on-background: '#e4e1ec'
  surface-variant: '#34343c'
typography:
  display-lg:
    fontFamily: Space Mono
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: 0.1em
  display-lg-mobile:
    fontFamily: Space Mono
    fontSize: 20px
    fontWeight: '700'
    lineHeight: 28px
    letterSpacing: 0.08em
  headline-lg:
    fontFamily: Space Mono
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
    letterSpacing: 0.05em
  headline-md:
    fontFamily: Space Mono
    fontSize: 18px
    fontWeight: '700'
    lineHeight: 24px
    letterSpacing: 0.04em
  headline-sm:
    fontFamily: Space Mono
    fontSize: 15px
    fontWeight: '700'
    lineHeight: 20px
    letterSpacing: 0.02em
  body-lg:
    fontFamily: Space Mono
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
    letterSpacing: 0.02em
  body-md:
    fontFamily: Space Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
    letterSpacing: 0.01em
  body-sm:
    fontFamily: Space Mono
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 16px
    letterSpacing: '0'
  label-lg:
    fontFamily: JetBrains Mono
    fontSize: 13px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.06em
  label-md:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '500'
    lineHeight: 14px
    letterSpacing: 0.05em
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 10px
    fontWeight: '500'
    lineHeight: 12px
    letterSpacing: 0.08em
spacing:
  gutter: 1rem
  margin: 1.5rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2rem
---

## Brand & Style

This design system channels the electrified kinetic tension of 1980s coin-operated arcade machines and early microcomputer phosphor displays. Built for developer tools, retro gaming hubs, competitive leaderboards, and telemetry HUDs, the emotional signature evokes late-night arcade basements, glowing cathode tubes, and unyielding mechanical precision. 

The aesthetic is aggressively Retro Brutalist and Tactile Skeuomorphic:
- **Rasterized Reality:** Strict avoidance of vector gradients, fluid blurs, and organic anti-aliasing. Surfaces utilize dither patterns and stepped pixel stepping.
- **CRT Emulation:** Visual depth is produced through chromatic phosphor emission, simulated horizontal scanline interlacing, and deep curved vignette perimeters.
- **High-Contrast Digital Impact:** Electric cyan, hot magenta, and pixel yellow flash against pitch-black cathode glass, commanding immediate focus and urgent legibility.

## Colors

The color palette is derived directly from classic high-contrast arcade color palettes and calibrated phosphor values:

- **Phosphor Core / CRT Black (`#0b0b12`):** Primary canvas base representing non-energized cathode tube space.
- **Neon Cyan (`#34f5ff`):** Primary action color, core system HUD data, links, and high-frequency active indicators.
- **Neon Magenta (`#ff3fa4`):** Secondary interactive accents, player-2 telemetry, warnings, and arcade highlight badges.
- **Pixel Yellow (`#ffe14d`):** High scores, bonus metrics, warnings, and attention hooks.
- **Phosphor Green (`#00ff66`):** System status online, positive metrics, power states, and raw telemetry readouts.
- **Arcade White (`#ffffff`):** Unfiltered primary text, crisp terminal heads, flash pulses, and highest-contrast icons.
- **Scanline Bar (`#141424`):** Sub-surface panels, inactive slot containers, and interlaced raster bands.

Gradients are strictly prohibited unless constructed using explicit 2-color pixel dithering (checkerboard thresholds). Never use translucent alpha ramps for depth; use high-contrast binary state switches.

## Typography

Typography prioritizes monospace technical alignment, fixed tabular metrics, and retro arcade character. 

- **Display & Headlines:** Set in uppercase with wide letter-spacing to reproduce early coin-op ROM character tables. Kerning is locked to fixed grid steps.
- **Body & Continuous Copy:** Set in monospaced geometry with strong baseline anchoring, ensuring clean horizontal and vertical scanline compatibility.
- **HUD & Labels:** Tight, technical readouts utilizing fixed-width tabular numbers for real-time counters, currency tallies, and system registers.
- **Text Rendering:** Disable subpixel anti-aliasing via CSS (`-webkit-font-smoothing: none; -moz-osx-font-smoothing: unset; image-rendering: pixelated;`) on display tiers where supported to retain authentic pixel-grid edges.

## Layout & Spacing

The layout is anchored to an uncompromising 4px / 8px grid, mimicking physical display pixel banks.

- **Grid Framework:** A 12-column fixed-gutter layout encased inside an absolute-ratio CRT bezel container. The canvas simulates a curved 4:3 or 16:9 arcade monitor with fixed physical margins.
- **Spatial Rhythm:** Distances between elements are strictly discrete jumps based on the `0.25rem` (4px) base scale. Floating-point rem paddings (e.g., `0.333rem`) are forbidden.
- **Responsive Adaptations:**
  - **Mobile (< 768px):** Single-column stacked HUD modules. Scanline overlays drop from alternating 2px intervals to a lighter 1px raster step to protect line readability. Margins compress to `space-md` (1rem).
  - **Tablet (768px - 1024px):** 6-column split layout. Primary control surfaces take 4 columns, persistent telemetry HUD occupies 2 columns.
  - **Desktop (> 1024px):** 12-column cockpit terminal. Canvas utilizes fixed-centering within an arcade bezel wrap, anchoring global meters to top/bottom peripheral ribbons.

## Elevation & Depth

Soft Gaussian blurs and ambient dropshadows are non-existent. Depth is produced purely through retro-mechanical layers and CRT optics:

- **Stepped Pixel Offset:** Elevated surfaces project hard-edged, stepped drop-shadows with zero blur radius (e.g., `box-shadow: 4px 4px 0px #000000`).
- **Phosphor Bloom:** Focus targets, active inputs, and neon typography generate a high-intensity dual hard glow (e.g., `0 0 2px #34f5ff, 0 0 8px rgba(52, 245, 255, 0.65)`).
- **Cathode Interlacing:** The entire layout is topped with a persistent pointer-events-none SVG/CSS scanline layer: horizontal lines repeating every 4px alternating between transparent and `rgba(20, 20, 36, 0.45)`.
- **Bezel Vignette:** Outer screen edges employ an inset radial mask (`box-shadow: inset 0 0 64px rgba(0, 0, 0, 0.85)`) to generate the organic curvature of rounded CRT vacuum glass.

## Shapes

Rounded geometric corners contradict authentic 8-bit architecture. Therefore:
- The standard border-radius across all containers, inputs, buttons, and badges is strictly `0px`.
- Where chamfered or mock-rounded corners are required, they must be constructed using pixel-stepped clip-paths or nested block borders (e.g., 2px corner drop-in cutouts) to simulate discrete pixel stepped edges.
- Outlines and borders must default to crisp 2px or 4px solid borders; 1px fractional hairline strokes are disallowed on primary structural blocks.

## Components

### Buttons
- **Style:** Chunky 8-bit rectangular push-buttons with 2px solid arcade white borders and CRT black fill.
- **States:**
  - *Default:* `#0b0b12` background, Neon Cyan text, 4px solid `#000000` bottom-right hard shadow.
  - *Hover / Focus:* Invert colors—`#34f5ff` background with `#0b0b12` text. Chromatic bloom glow applied to border.
  - *Active:* 0px hard shadow with a 4px translation down and right (`transform: translate(4px, 4px)`), mimicking a microswitch bottoming out.

### Chips & Badges
- **Style:** Compact badges with 2px stepped borders. Text set exclusively in `label-sm` uppercase.
- **Variants:**
  - *Player 1 / Primary:* Neon Cyan border, black fill, Cyan text.
  - *Warning / Alert:* Neon Magenta border, black fill, Magenta text.
  - *Score / Bonus:* Pixel Yellow border, black fill, Yellow text.

### Input Fields
- **Style:** Solid `#141424` background with a 2px `#34f5ff` lower baseline or complete enclosing box.
- **Caret:** Chunky blinking solid block cursor (`width: 8px; height: 16px; background-color: #34f5ff; animation: blink 1s steps(2, start) infinite`).
- **Placeholder:** Dim arcade gray (`#4a4a68`) in monospaced uppercase.

### Checkboxes & Radios
- **Checkboxes:** 16x16px square boxes with a 2px solid Neon Cyan border. Checked state renders a solid 8x8px centered neon pixel square or an "X" formed of 2px square dot matrices.
- **Radios:** Diamond-shaped containers (achieved via a 45-degree rotated square, `clip-path`, or pixel-art diamond asset). Checked state renders a solid central glowing pixel dot.

### Cards & Panels
- **Style:** Heavy CRT console plates with `#141424` background and `#34f5ff` or `#ff3fa4` outer frame borders.
- **Header Plate:** Distinct upper title bar separated by a 2px horizontal solid rule, carrying tabular system metadata (e.g., `SEC-01 // INSERT COIN`).
- **Texture:** Panels optionally display a 50% dither pattern along header edges.

### Data Tables & Scoreboards
- **Rows:** Alternating rows of transparent and `rgba(20, 20, 36, 0.5)`.
- **Rank Indicators:** Left-aligned rank indicators in Pixel Yellow, scores aligned to the right in tabular monospace with zero-padded prefixes (e.g., `0048290`).