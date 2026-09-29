---
name: Thermal Till
colors:
  surface: '#121412'
  surface-dim: '#121412'
  surface-bright: '#383937'
  surface-container-lowest: '#0d0f0d'
  surface-container-low: '#1b1c1a'
  surface-container: '#1f201e'
  surface-container-high: '#292a28'
  surface-container-highest: '#343533'
  on-surface: '#e3e2df'
  on-surface-variant: '#c4c7c7'
  inverse-surface: '#e3e2df'
  inverse-on-surface: '#2f312e'
  outline: '#8e9192'
  outline-variant: '#444748'
  surface-tint: '#c8c6c5'
  primary: '#c8c6c5'
  on-primary: '#303030'
  primary-container: '#1e1e1e'
  on-primary-container: '#878585'
  inverse-primary: '#5f5e5e'
  secondary: '#d6c953'
  on-secondary: '#363100'
  secondary-container: '#9e9320'
  on-secondary-container: '#2f2a00'
  tertiary: '#c7c6c6'
  on-tertiary: '#2f3031'
  tertiary-container: '#1d1e1e'
  on-tertiary-container: '#858686'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1b1b1c'
  on-primary-fixed-variant: '#474746'
  secondary-fixed: '#f3e56c'
  secondary-fixed-dim: '#d6c953'
  on-secondary-fixed: '#1f1c00'
  on-secondary-fixed-variant: '#4e4800'
  tertiary-fixed: '#e3e2e2'
  tertiary-fixed-dim: '#c7c6c6'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#464747'
  background: '#121412'
  on-background: '#e3e2df'
  surface-variant: '#343533'
typography:
  headline-xl:
    fontFamily: Space Mono
    fontSize: 2rem
    fontWeight: '700'
    lineHeight: 2.25rem
    letterSpacing: -0.02em
  headline-xl-mobile:
    fontFamily: Space Mono
    fontSize: 1.5rem
    fontWeight: '700'
    lineHeight: 1.75rem
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: Space Mono
    fontSize: 1.25rem
    fontWeight: '700'
    lineHeight: 1.5rem
    letterSpacing: 0em
  headline-md:
    fontFamily: Space Mono
    fontSize: 1rem
    fontWeight: '700'
    lineHeight: 1.375rem
    letterSpacing: 0.05em
  body-lg:
    fontFamily: Space Mono
    fontSize: 0.9375rem
    fontWeight: '400'
    lineHeight: 1.375rem
    letterSpacing: 0em
  body-md:
    fontFamily: Space Mono
    fontSize: 0.8125rem
    fontWeight: '400'
    lineHeight: 1.25rem
    letterSpacing: 0.01em
  body-sm:
    fontFamily: Space Mono
    fontSize: 0.6875rem
    fontWeight: '400'
    lineHeight: 1rem
    letterSpacing: 0.02em
  label-lg:
    fontFamily: Space Mono
    fontSize: 0.8125rem
    fontWeight: '700'
    lineHeight: 1.125rem
    letterSpacing: 0.08em
  label-md:
    fontFamily: Space Mono
    fontSize: 0.6875rem
    fontWeight: '700'
    lineHeight: 1rem
    letterSpacing: 0.06em
  label-sm:
    fontFamily: Space Mono
    fontSize: 0.5625rem
    fontWeight: '400'
    lineHeight: 0.75rem
    letterSpacing: 0.08em
spacing:
  gutter: 1rem
  margin: 1rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 0.75rem
  space-lg: 1.25rem
  space-xl: 2rem
---

## Brand & Style

This design system draws direct inspiration from point-of-sale thermal receipts resting atop a matte, non-reflective slate desk. The aesthetic is tactile, utilitarian, and strictly analog-inspired: every layout, divider, container, and glyph honors the mechanical restrictions of a 58mm–80mm continuous thermal paper roll. 

The emotional response should evoke tactile satisfaction, hyper-clarity, and structured physical permanence within a digital canvas. Contrast is deliberate and stark. Digital UI components borrow physical artifacts: sawtooth tear edges, perforated folds, dot-leader pricing tracks, mono-spaced line lengths, and single-stroke fluorescent felt-tip highlighting. It is designed for transactional software, ledger audit tools, fintech dashboards, inventory manifests, and point-of-sale applications where data honesty and immediate legibility supersede decorative fluff.

## Colors

The system operates on an inverted skeuomorphic dynamic: a persistent dark substrate (`#1b1b1b`) supporting a warm, high-opacity off-white paper canvas (`#fbfaf6`). Information hierarchy relies strictly on ink density, dot degradation, and an occasional fluorescent highlighter stroke.

- **Desk Substrate (`#1b1b1b`):** The default environment background. Deep, matte, and neutral to eliminate glare and push the thermal roll into high-contrast focus.
- **Receipt Paper Surface (`#fbfaf6`):** The warm, non-glare canvas for all interactive elements, modules, itemizations, and readouts.
- **Thermal Carbon Black (`#1e1e1e`):** The primary ink. Used for headlines, key figures, active states, borders, and barcoding. Never pure digital `#000000`.
- **Thermal Carbon Faded Grey (`#8c8c8c`):** Secondary ink simulation. Applied to timestamps, dot leaders (`............`), auxiliary labels, secondary actions, and minor transaction metadata.
- **Fluorescent Highlighter (`#fff176`):** The exclusive chromatic accent. Used sparingly as a marker-swipe highlight backing for totals, success indicators, critical alerts, or user focus states.

## Typography

The typographic hierarchy is unapologetically monospaced, anchored entirely by `Space Mono`. Typographic emphasis is achieved not by switching font families or variable weights, but via physical terminal methods: capitalization, double-strike emulation (weight 700), double-height displays, and character tracking.

- **Scale & Rhythm:** Typography is strictly locked to character grids. Headlines in all caps (`headline-md`, `label-lg`) emulate 32-character receipt header feeds.
- **Barcode & Stub Typography:** Barcodes are represented using continuous monospace symbol fonts or ASCII bar approximations (`||| | ||||| || | |||`) paired with tracking numbers set in `body-sm`.
- **Text Alignment:** Financial figures and tabulation columns must always be right-aligned with fixed character counts, linked to line-item labels via dot leaders (`. . . . . .`).

## Layout & Spacing

Layout conforms to the dimensions of a physical receipt scroll centered on the viewport. Rather than stretching across wide viewports, the primary interaction column simulates continuous paper rolls with fixed structural constraints.

- **Container Model:** On desktop and tablet viewports, the application canvas locks the paper width to a maximum of `440px` (standard receipt roll presentation) or `780px` (dual ledger roll layout). It is horizontally centered within the `#1b1b1b` desk backdrop.
- **Mobile Fluidity:** On mobile viewports (< 480px), the receipt paper takes full width with `margin: 0.5rem` to keep the desk surface visible at outer margins, maintaining the illusion of paper placed onto a counter.
- **Vertical Flow:** Vertical rhythm mimics continuous line-feeds. Sections are delimited by character strokes (`- - - - - - - -` or `= = = = = = = =`) spaced at `space-md` intervals.

## Elevation & Depth

Depth is tactile and grounded: flat receipt paper resting immediately on a hard surface. Layering does not rely on synthetic blurred elevations or high Z-index tiers.

- **Primary Paper Drop Shadow:** The paper strip casts an authentic, tight, multi-layered ambient occlusion shadow directly onto the `#1b1b1b` surface: `0 2px 4px rgba(0, 0, 0, 0.4), 0 12px 28px rgba(0, 0, 0, 0.6)`. No colored shadow tints are permitted.
- **Paper Curl & Tears:** Top and bottom boundaries employ CSS masking (`clip-path`) to generate micro-sawtooth perforated tear patterns (`polygon` repeating peaks at 4px intervals).
- **Ink Elevation:** Pure flat print. Text and line elements sit flush on `#fbfaf6` with zero text-shadows or emboss effects, perfectly emulating head-transfer heat printing.

## Shapes

The design system enforces strict industrial geometry with a roundedness value of `0` (Sharp). 

Physical paper rolls have crisp 90-degree guillotine cuts or micro-serrations. Buttons, input fields, checkboxes, data tables, and badges must never use rounded corners. Everything is built with razor edges, clean orthogonal lines, and hard box frames. Any perimeter softening conflicts with the mechanical print metaphor.

## Components

### Buttons
- **Primary Action:** Solid `#1e1e1e` background, `#fbfaf6` monospaced text, 0px border radius, sharp 1px `#1e1e1e` border. On hover, invert to `#fbfaf6` background with `#1e1e1e` text.
- **Secondary Action:** Transparent background with a dashed `1px dashed #1e1e1e` border and `#1e1e1e` text.
- **Highlighter Action:** `#fff176` background with `#1e1e1e` text, surrounded by a tight `1px solid #1e1e1e` border.

### Input Fields
- Single-line baseline borders (`1px solid #1e1e1e`) or boxed ASCII brackets: `[  Enter Query  ]`. Background is pure `#fbfaf6`. Text inputs feature a blinking solid block cursor (`█`).

### Checkboxes & Radios
- **Checkbox:** Rendered as square bracket characters: `[ ]` for unchecked, `[X]` or `[■]` for checked.
- **Radio:** Rendered as parentheses: `( )` for unselected, `(•)` for selected.

### Lists & Ledger Rows
- Tabular two-column layout. Left column holds item descriptors (`body-md`), right column holds values. Space between is spanned automatically by repeated dot leaders (`. . . . . . . . . . . .`) in `#8c8c8c`.

### Cards & Grouping Containers
- Framed with double line rules (`border: 3px double #1e1e1e`) or single hairline borders (`1px solid #1e1e1e`). 
- Dividers between sections use ASCII thermal print simulations: standard dashed lines (`--------------------------------`), thick equal lines (`================================`), or zig-zags.

### Highlighter Swipes (Accent States)
- Highlight tags, critical metrics, and active filters use a skewed background banner in `#fff176` with a slight natural tilt (`transform: rotate(-0.5deg)`), sitting directly behind carbon black text with `mix-blend-mode: multiply`.

### Barcodes & Stubs
- Terminal vouchers and scan points feature a high-density vertical barcode element rendered along the full receipt width, flanked above and below by tear perforation lines (`border-top: 2px dashed #8c8c8c`).