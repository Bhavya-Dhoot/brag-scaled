---
name: Quant Brutalism
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#c4caac'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8e9479'
  outline-variant: '#434933'
  surface-tint: '#a8d700'
  primary: '#ffffff'
  on-primary: '#273500'
  primary-container: '#c0f500'
  on-primary-container: '#546d00'
  inverse-primary: '#4f6600'
  secondary: '#c7c6c6'
  on-secondary: '#303031'
  secondary-container: '#464747'
  on-secondary-container: '#b5b5b5'
  tertiary: '#ffffff'
  on-tertiary: '#1f333f'
  tertiary-container: '#d0e5f5'
  on-tertiary-container: '#536774'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#c0f500'
  primary-fixed-dim: '#a8d700'
  on-primary-fixed: '#161f00'
  on-primary-fixed-variant: '#3b4d00'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c7c6c6'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#d0e5f5'
  tertiary-fixed-dim: '#b5c9d9'
  on-tertiary-fixed: '#081e29'
  on-tertiary-fixed-variant: '#364956'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-xl:
    fontFamily: Space Grotesk
    fontSize: 56px
    fontWeight: '700'
    lineHeight: 60px
    letterSpacing: -0.04em
  display-xl-mobile:
    fontFamily: Space Grotesk
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.03em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 44px
    letterSpacing: -0.03em
  headline-lg-mobile:
    fontFamily: Space Grotesk
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 32px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 28px
    letterSpacing: -0.02em
  body-lg:
    fontFamily: JetBrains Mono
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
    letterSpacing: -0.01em
  body-md:
    fontFamily: JetBrains Mono
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 18px
    letterSpacing: 0em
  label-mono-lg:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '700'
    lineHeight: 18px
    letterSpacing: 0.08em
  label-mono-sm:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '500'
    lineHeight: 14px
    letterSpacing: 0.12em
  metric-huge:
    fontFamily: JetBrains Mono
    fontSize: 64px
    fontWeight: '700'
    lineHeight: 64px
    letterSpacing: -0.03em
  metric-huge-mobile:
    fontFamily: JetBrains Mono
    fontSize: 38px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.02em
spacing:
  gutter: 0px
  gutter-desktop: 16px
  margin: 16px
  margin-desktop: 32px
  space-xs: 4px
  space-sm: 8px
  space-md: 16px
  space-lg: 24px
  space-xl: 32px
---

## Brand & Style

This design system delivers an uncompromising, terminal-grade visual language calibrated for high-impact launch sequences, algorithmic command centers, and dense financial engineering interfaces. Built strictly for the 16:9 cinematic storyboard format, it fuses technical brutality with algorithmic precision.

### Identity & Atmosphere
- **Aesthetic:** Brutalist Technical / HUD Terminal. Raw, high-density, mathematical, and unsparing.
- **Tone:** Sovereign, authoritative, cold, hyper-performant.
- **Visual Discipline:** Zero soft gradients, zero organic blurs, zero rounded corners. Precision drafting rules, explicit container lines, mono telemetry, and abrupt high-contrast state transitions.
- **Target Audience:** Quantitative traders, systems architects, institutional risk analysts, and technical operators demanding instant data legibility over decorative comfort.

## Colors

The palette operates on absolute values to preserve terminal starkness and rapid visual parsing. Contrast ratios meet extreme verification thresholds against deep black.

### Palette Architecture
- **Primary (`#c8ff00` - Signal Lime):** Reserved exclusively for active execution states, high-priority telemetry, focus vectors, active tickers, and real-time execution markers. Never applied as a passive decorative wash.
- **Secondary (`#8a8a8a` - Muted Steel):** Metadata, structural labels, static timestamps, secondary indices, inactive axes, and unselected data paths.
- **Neutral Surface (`#0a0a0a` - Ink Black):** The universal root canvas and primary container base. Provides zero-reflection background contrast.
- **Content Primary (`#f0ede8` - Paper White):** Display headlines, critical value readouts, primary metric digits, and terminal system prompts.
- **Structural Grid (`#1e1e1e` - Cold Slate):** Universal 1px to 2px bounding boxes, coordinate axes, frame dividers, and cell matrices.

### Functional Rules
- Surfaces do not elevate through tint shifts; they maintain `#0a0a0a` and delineate strictly via `#1e1e1e` borders or inverse fills.
- Hover or active selections invert content instantly (Paper on Ink transitions abruptly to Ink on Signal Lime).

## Typography

Typography establishes an uncompromising hierarchy between structural announcements and live machine telemetry.

### Type Pairings
- **Headlines & Narrative Impact:** Rendered in Space Grotesk (Bold 700) with compressed, tight tracking (`-0.02em` to `-0.04em`) to project mass, industrial weight, and raw presence.
- **Data, Labels, Readouts & Clocks:** Rendered in JetBrains Mono. Numbers are strictly tabular lining. Micro-labels, telemetry metadata, status tags, and coordinate stamps are strictly uppercase with wide letter-spacing (`+0.08em` to `+0.12em`).

### Formatting Constraints
- Never apply synthetic italics.
- Metric values must never break lines or use proportional numbers; always align tabular numerals across order books and time series.

## Layout & Spacing

Layout geometry follows an explicit, coordinate-driven framework built inside a fixed 16:9 cinematic aspect ratio (optimized for 3840×2160 and 1920×1080 display viewports).

### Layout System
- **Grid Structure:** Modular 16-column matrix with zero default gutter gaps (`0px`), separated instead by shared `2px solid #1e1e1e` architectural dividers. This produces an uninterrupted tiled instrument panel.
- **Storyboards & Framing:** Outer boundary enforces a strict padding margin (`32px` on desktop/16:9 frame, `16px` on scaled down displays) enclosed by an absolute outer viewport border stamped with screen coordinate callouts (e.g., `[X:000, Y:000]`).
- **Data Density:** Layout favors tightly packed arrays with standard inner cell padding (`space-sm` to `space-md`). Padding must remain consistent across horizontal and vertical axes to reinforce modular tiling.

## Elevation & Depth

This design system rejects simulated physical light, atmospheric drops, and Gaussian blurs. Visual depth is entirely structural, flat, and cartographic.

### Structural Depth Principles
- **No Shadows:** Shadows (`box-shadow`) are prohibited across all UI states and overlays.
- **Borders as Structure:** Elevation tiers are expressed solely through `2px solid #1e1e1e` structural outlines. Focus and active tiers upgrade their border directly to `2px solid #c8ff00`.
- **Z-Index Layering:** Tooltips, command palettes, and execution confirmation modals overlay baseline viewports using a solid, opaque `#0a0a0a` fill with a `2px solid #c8ff00` bounding box.
- **HUD Reticles:** Viewports and sub-modules utilize technical corner ticks (`+` markers, corner L-brackets) to indicate modular containment without requiring multi-layering.

## Shapes

Every component, panel, interactive state, and boundary is rigidly geometric.

### Geometry Specifications
- **Border Radius:** Absolute zero (`0px`). No rounded pills, no softened borders, no curved corners.
- **Cut Corners (Chambered Edges):** Permitted only on specialized terminal tabs or tactical buttons, using a strict `45deg` mechanical chamfer (`4px` or `8px`), drawn mathematically without curve interpolations.
- **Rule Lines:** All dividing lines and strokes are uniform `2px solid` vectors. No dashed lines except for speculative predictive chart axes.

## Components

Components function as instrumentation modules inside an algorithmic trading terminal.

### Buttons & Triggers
- **Primary Execution Button:** Solid `#c8ff00` background, `#0a0a0a` text in uppercase JetBrains Mono bold. No border-radius. Zero transition ease—instant color swap on hover (`#f0ede8` background, `#0a0a0a` text).
- **Secondary / Command Button:** Transparent background, `2px solid #1e1e1e` border, `#f0ede8` text. Hover upgrades border directly to `2px solid #c8ff00` with text colored `#c8ff00`.
- **System Destructive Trigger:** Transparent background, `2px solid #f0ede8` with an embedded indicator tag `[KILL]`.

### Data Chips & Status Badges
- Constructed as tight typographic blocks.
- Outline: `1px solid #1e1e1e`, padding `2px 6px`.
- Inactive: `#8a8a8a` text.
- Live / Operational: `#c8ff00` text with an inline leading unicode glyph `● [ACTIVE]`.

### Lists & Order Book Matrix
- Tabular lists with strict row heights (`28px` or `32px`).
- Alternating rows do not use alternating background fills; rows are divided by `1px solid #1e1e1e`.
- Alignment: Alphabetic tickers and IDs align strictly left; quantities, spreads, and currency values align strictly right.

### Checkboxes, Switches & Radios
- Checkboxes: `14px × 14px` square boxes, `2px solid #1e1e1e`. Checked state: filled completely with `#c8ff00` displaying a solid inner square or direct `X` in black.
- Toggle Switches: Dual-cell binary rectangles `[ OFF | ON ]`. The active cell inverts to solid `#c8ff00` fill with `#0a0a0a` text.

### Input Fields
- Outer boundary: `2px solid #1e1e1e`. Background: `#0a0a0a`.
- Text: `#f0ede8` in JetBrains Mono.
- Cursor: Block cursor (`█`) blinking at a 1Hz frequency.
- Focused state: Border changes to `2px solid #c8ff00` with an uppercase coordinate label pinned to the top-left border intersection (e.g., `SRC_VAL//`).

### Quant Cards & Viewport Modules
- Monolithic data boxes enclosed by `2px solid #1e1e1e`.
- Headers are hard-separated from the card body with a horizontal `2px solid #1e1e1e` rule.
- Header contains an uppercase module title (e.g., `ORDER_FLOW_MONITOR`) on the left, and micro timestamp telemetry (`UTC 14:02:19.492`) on the right in `#8a8a8a`.