---
name: Patent Blueprint Drafting System
colors:
  surface: '#00132f'
  surface-dim: '#00132f'
  surface-bright: '#0a3870'
  surface-container-lowest: '#000e26'
  surface-container-low: '#001b3e'
  surface-container: '#001f45'
  surface-container-high: '#002958'
  surface-container-highest: '#02346c'
  on-surface: '#d6e3ff'
  on-surface-variant: '#c5c6cb'
  inverse-surface: '#d6e3ff'
  inverse-on-surface: '#002f64'
  outline: '#8e9196'
  outline-variant: '#44474b'
  surface-tint: '#bec7d5'
  primary: '#ffffff'
  on-primary: '#28313c'
  primary-container: '#dae3f1'
  on-primary-container: '#5c6571'
  inverse-primary: '#565f6b'
  secondary: '#f4be4e'
  on-secondary: '#412d00'
  secondary-container: '#b8891a'
  on-secondary-container: '#382700'
  tertiary: '#ffffff'
  on-tertiary: '#002a78'
  tertiary-container: '#dbe1ff'
  on-tertiary-container: '#1359e2'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dae3f1'
  primary-fixed-dim: '#bec7d5'
  on-primary-fixed: '#131c26'
  on-primary-fixed-variant: '#3f4853'
  secondary-fixed: '#ffdea4'
  secondary-fixed-dim: '#f4be4e'
  on-secondary-fixed: '#261900'
  on-secondary-fixed-variant: '#5d4200'
  tertiary-fixed: '#dbe1ff'
  tertiary-fixed-dim: '#b4c5ff'
  on-tertiary-fixed: '#00174b'
  on-tertiary-fixed-variant: '#003ea8'
  background: '#00132f'
  on-background: '#d6e3ff'
  surface-variant: '#02346c'
typography:
  headline-xl:
    fontFamily: Archivo Narrow
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 44px
    letterSpacing: 0.08em
  headline-xl-mobile:
    fontFamily: Archivo Narrow
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 32px
    letterSpacing: 0.08em
  headline-lg:
    fontFamily: Archivo Narrow
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 32px
    letterSpacing: 0.06em
  headline-md:
    fontFamily: Archivo Narrow
    fontSize: 20px
    fontWeight: '700'
    lineHeight: 24px
    letterSpacing: 0.05em
  headline-sm:
    fontFamily: Archivo Narrow
    fontSize: 16px
    fontWeight: '700'
    lineHeight: 20px
    letterSpacing: 0.05em
  body-lg:
    fontFamily: Space Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 22px
    letterSpacing: 0.01em
  body-md:
    fontFamily: Space Mono
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 18px
    letterSpacing: 0.01em
  body-sm:
    fontFamily: Space Mono
    fontSize: 11px
    fontWeight: '400'
    lineHeight: 16px
    letterSpacing: 0.01em
  label-lg:
    fontFamily: Space Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.08em
  label-md:
    fontFamily: Space Mono
    fontSize: 10px
    fontWeight: '700'
    lineHeight: 14px
    letterSpacing: 0.1em
  label-sm:
    fontFamily: Space Mono
    fontSize: 9px
    fontWeight: '400'
    lineHeight: 12px
    letterSpacing: 0.12em
spacing:
  gutter: 1.5rem
  gutter-mobile: 0.75rem
  margin: 2rem
  margin-mobile: 1rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.5rem
---

## Brand & Style

This design system translates the rigorous, archival discipline of 20th-century patent office technical disclosures and engineering cyanotypes into an interactive, sequence-driven storyboard platform. Built specifically for technical schematics, dimensioning, and structural sequencing, the aesthetic rejects digital skeuomorphism, soft blurs, and volumetric renders in favor of precise, uncompromising vector drafting.

The emotional signature is clinical, calculated, and legally authoritative. Every line behaves as a functional vector with structural intent. Key visual hallmarks include:
- Technical border zones with corner alignment targets and coordinate margins (A–D, 1–8).
- Orthographic projection logic: clear section planes, exploded assemblies, dimension extension lines, and 45° cross-hatch fills.
- High-visibility amber leader lines terminate in numbered callout rings for component identification.
- Monolithic drafting title blocks in the lower-right quadrant anchoring sheet indexing, scale parameters, and approval signatures.

## Colors

The palette reproduces chemical blueprint reproduction processes (cyanotype), operating entirely in a dedicated drafting environment:

- **Blueprint Ground (`#0f3b73`)**: The absolute canvas and viewport background. Subordinate surfaces and container fills utilize lower-opacity variants (10%–20%) or remain entirely transparent to expose the base drafting grid.
- **Technical Line White (`#e8f1ff`)**: The primary vector stroke, framing border, dimension line, and textual data display. All schematics, text labels, and structural enclosures are drafted in this tint.
- **Callout Amber (`#ffc857`)**: The high-priority focus accent. Used sparingly and exclusively for critical inspection targets, leader line terminals, delta notes, revision indicators, and interactive focus states.
- **Grid Substrate (`rgba(232, 241, 255, 0.08)`)**: Faint major and minor coordinate grid overlays that sit beneath all interactive surfaces.

No drop shadows, blurred glows, or solid multi-color fills are permitted. Transparency is restricted to hatched vector patterns and technical ground layering.

## Typography

The typography reinforces formal patent filing specifications and architectural blue-line standards:

- **Headlines (Archivo Narrow)**: Set in all-caps, heavy weights (700). Employed strictly for figure classifications (`FIG. 1`, `FIG. 2`), sectional designations, and primary document titling. Characterized by high legibility, compact letterforms, and generous tracking to maintain clarity at high drawing densities.
- **Body & Labels (Space Mono)**: Monospaced numerical values, patent claims, dimensional annotations, coordinates, and leader-line indices. The monospaced rhythm ensures that decimal points, tolerances (e.g., `±0.05mm`), and reference numerals align flush across columns and callout arrays.
- Text must consistently render in uppercase when functioning as title block fields, drawing identifiers, status indicators, and dimensional metadata.

## Layout & Spacing

The blueprint layout relies on an architectural coordinate grid enclosed inside a double technical border:

- **Master Canvas**: Outer canvas bound by an absolute margin containing coordinate marks (A, B, C, D along the vertical axis; 1, 2, 3, 4 along the horizontal axis). The inner active drafting area is bounded by a continuous 2.5px white rule.
- **Grid Substrate**: A persistent 32px major and 8px minor grid underlies the sheet. Components, frames, and figure cards snap to multiples of the grid (using `space-sm` / 8px increments).
- **Responsive Adaptations**:
  - *Desktop*: 4-quadrant layout (`FIG. 1` through `FIG. 4`) with the title block locked to the bottom-right corner of quadrant 4 or overlapping the lower margin.
  - *Tablet*: 2-column stacked layout with persistent top metadata bar and floating architectural sheet title footer.
  - *Mobile*: Single vertical drafting reel (`FIG. 1` through `FIG. 4` stacked sequentially). Border coordinates collapse to minimal corner ticks. The title block condenses into an anchored accordion at the bottom of the viewport.

## Elevation & Depth

This system is strictly two-dimensional and planar. Z-index does not convey elevation through dropshadows, blurred depth-of-field, or surface extrusion. Instead, spatial hierarchy is communicated through line weighting, hatching, and stroke density:

- **Base Line Weight (1px)**: Drafting gridlines, construction guidelines, centerlines, and dimension extension bounds.
- **Standard Structural Stroke (2px–2.5px)**: Component boundaries, schematic silhouettes, UI frames, and interactive inputs.
- **Primary Section Stroke (3px)**: Enclosing sheet border, active figure boundaries, and selected structural assemblies.
- **Surface Contrast (Hatching)**: Instead of tonal fills or semi-transparent layering, overlapping spatial volumes are filled with 45-degree single-hatch or double-hatch line vectors spaced 4px apart.
- **Active / Layer Selection**: Signaled by an inverted fill of `#e8f1ff` with `#0f3b73` foreground typography, or by switching the perimeter vector stroke to Callout Amber (`#ffc857`).

## Shapes

In keeping with rigorous technical engineering standards, the radius token is locked at 0 across all elements:

- **Zero Curvature**: All panels, buttons, cards, tags, and sheet dividers have crisp 90-degree square corners (`roundedness: 0`).
- **Corner Registration Marks**: Major drafting frames and active modules display 8px outer corner crosshairs (+) or L-shaped alignment brackets.
- **Callout Circles**: The sole exception to square geometry is circular leader callout nodes (diameter: 24px) consisting of an unrounded circular stroke with a centered reference number.
- **Arrowheads & Dimension Ticks**: Terminators for dimension strings use sharp 45-degree oblique tick lines or unfilled, acute vector arrows.

## Components

### Title Block (Architectural Cartouche)
Positioned in the lower-right corner of the sheet frame. Constructed of a 2.5px white border subdivided into a modular grid:
- **Upper Zone**: Document identification (`"NEXUS // PATENT FILING"`), sheet count (`"SHEET 1 OF 4"`), and scale designation (`"SCALE 1:1"`).
- **Lower Data Fields**: Revision dates, drafting author initials, filing reference IDs, and authorization checkboxes.
- Typography is strictly Space Mono, uppercase, separated by thin 1px horizontal and vertical dividers.

### Figure Containers (FIG. 1 - FIG. 4)
- **Frame**: Bounded by a 2px `#e8f1ff` outline. Top-left corner features an integrated tab carrying the figure headline label (`FIG. 1`, `FIG. 2`, etc.) in Archivo Narrow Bold.
- **Canvas Interior**: Transparent background showing the continuous blueprint grid. Schematics rendered in vector line art with zero fills.

### Dimension Strings & Extension Lines
- Composed of two thin projection lines extending from the object, an unbroken dimension line perpendicular to them, and an embedded monospaced label (e.g., `420.00 mm`).
- Ends terminate in crisp 45° drafting slash marks or precise double-ended vector arrows.

### Callout Nodes & Leader Lines
- Leader lines are 1.5px lines running from key component geometries at 45° angles, dog-legging horizontally into a 24px circular identifier ring.
- In resting state: 1.5px `#e8f1ff` line and ring with white numeral.
- In highlighted/active state: 2px `#ffc857` stroke, with amber numeral and filled amber terminal anchor dot.

### Buttons & Operational Switches
- **Primary Action**: 2px `#e8f1ff` rectangular outline, transparent fill, uppercase Space Mono label. On hover, inverts to a solid `#e8f1ff` fill with `#0f3b73` text.
- **Accent Action**: 2px `#ffc857` outline with amber text. Inverts to solid amber on press.
- **Toggle / Radio**: Square brackets `[ ]` and `[X]` rendered in monospaced typography with sharp vector crosshair ticks.

### Input Fields & Data Readouts
- Transparent ground, framed on all four sides by a 1.5px line (or alternatively, a classic technical underline with corner tick marks).
- Top-left label sits on the border in micro-caps (`label-sm`).
- Focus state switches stroke color to `#ffc857` with an active block cursor (`█`).