---
name: Metro Signage & Transit Wayfinding
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e5e2e1'
  on-surface: '#1b1b1b'
  on-surface-variant: '#5d3f3b'
  inverse-surface: '#313030'
  inverse-on-surface: '#f3f0ef'
  outline: '#926f69'
  outline-variant: '#e7bdb6'
  surface-tint: '#c00004'
  primary: '#bb0004'
  on-primary: '#ffffff'
  primary-container: '#e32017'
  on-primary-container: '#fffbfa'
  inverse-primary: '#ffb4a9'
  secondary: '#00658e'
  on-secondary: '#ffffff'
  secondary-container: '#50c0fe'
  on-secondary-container: '#004c6d'
  tertiary: '#006b25'
  on-tertiary: '#ffffff'
  tertiary-container: '#1d8636'
  on-tertiary-container: '#f6fff1'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad5'
  primary-fixed-dim: '#ffb4a9'
  on-primary-fixed: '#410000'
  on-primary-fixed-variant: '#930002'
  secondary-fixed: '#c7e7ff'
  secondary-fixed-dim: '#85cfff'
  on-secondary-fixed: '#001e2e'
  on-secondary-fixed-variant: '#004c6c'
  tertiary-fixed: '#94f99a'
  tertiary-fixed-dim: '#78dc80'
  on-tertiary-fixed: '#002106'
  on-tertiary-fixed-variant: '#00531a'
  background: '#fcf9f8'
  on-background: '#1b1b1b'
  surface-variant: '#e5e2e1'
typography:
  display-signage:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 52px
    letterSpacing: 0.06em
  display-signage-mobile:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 36px
    letterSpacing: 0.04em
  station-headline-lg:
    fontFamily: Space Grotesk
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: 0.04em
  station-headline-lg-mobile:
    fontFamily: Space Grotesk
    fontSize: 26px
    fontWeight: '700'
    lineHeight: 30px
    letterSpacing: 0.03em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 30px
    letterSpacing: 0.02em
  headline-sm:
    fontFamily: Space Grotesk
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 26px
    letterSpacing: 0.01em
  body-lg:
    fontFamily: Space Grotesk
    fontSize: 16px
    fontWeight: '500'
    lineHeight: 24px
  body-md:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  body-sm:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 16px
  signage-pill-label:
    fontFamily: Space Grotesk
    fontSize: 13px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.08em
  metadata-label:
    fontFamily: Space Grotesk
    fontSize: 11px
    fontWeight: '700'
    lineHeight: 14px
    letterSpacing: 0.1em
spacing:
  gutter: 1.5rem
  margin: 2rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.5rem
---

## Brand & Style

This design system translates the legendary discipline of mid-century civic transit wayfinding and schematic rail diagrams into a contemporary digital product interface. It rejects ephemeral web trends—no soft blurs, no ambient dropshadows, and no synthetic gradients. Instead, it embodies high-legibility, municipal clarity, and infrastructural permanence.

### Design Principles
- **Diagrammatic Precision:** Layouts operate under the rules of iconic schematic transit maps. Connectors and layout dividing lines follow strict horizontal, vertical, or 45-degree trajectories.
- **Enamelled Vitreous Realism:** Surfaces evoke baked enamel steel, screenprinted directional plates, and architectural station pylons. Contrast is absolute and surfaces are matte.
- **Civic Wayfinding Clarity:** Information hierarchy mirrors physical terminal navigation: primary routes, transfer interchanges, platform numbers, and operational statuses must be decipherable in an instant from variable distances.
- **Structural Brutalism meets High Functionality:** Heavy graphic weights, prominent boundaries, and universal iconography deliver an uncompromising, authoritative user experience.

## Colors

The color palette is modeled directly on universal metropolitan transit signage systems. Every color carries navigational and operational semantics rather than decorative weight.

### Palette Architecture
- **Signage Ink (`neutral_color_hex`: `#1c1c1c`):** Deep carbon black used for high-contrast typography, heavy graphic frames, terminal headers, and primary interchange rings.
- **Subway Red (`primary_color_hex`: `#e32017`):** The primary focal accent; commands immediate attention for express lines, emergency indicators, transfer roundels, and primary action triggers.
- **Metro Blue (`secondary_color_hex`: `#0098d4`):** Secondary navigation color; used for core lines, structural sub-headers, directional badges, and informational status modules.
- **Transit Green (`tertiary_color_hex`: `#00782a`):** Signifies standard route branches, active service statuses, accessibility confirmations, and on-time departures.
- **Line Yellow (`#ffd300`):** Specialized attention color; reserved for interchange warnings, caution plates, platform edge demarcations, and rapid disruption alerts. Always paired with `#1c1c1c` text for absolute legibility.
- **Enamel White (`#ffffff`):** The default pure ground canvas replicating architectural vitreous cladding panels.

### Application Rules
- Never blend or tint primary transit colors into ambient pastels.
- Color coding must remain stable: red, blue, green, and yellow correspond to discrete lines, platform zones, or categorical modes.
- Maintain a minimum WCAG AAA contrast ratio on all directional text and symbols.

## Typography

Typography functions as signage infrastructure. Space Grotesk provides the geometric proportions, open apertures, and industrial rigor reminiscent of classic transport fonts like Johnston and Neue Haas Grotesk.

### Typographic Directives
- **Uppercase Hierarchy:** All station names, track labels, platform zones, and primary terminal banners must be set in uppercase (`text-transform: uppercase`) with widened letter spacing to ensure rapid glance recognition.
- **Tabular Numerics:** Schedules, train arrival counters, platform bays, and route numbering require fixed-width alignment where possible.
- **Purity:** Font scaling avoids decorative sizing jumps; size changes reflect concrete structural divisions in physical infrastructure.

## Layout & Spacing

Layouts follow an uncompromising, industrial grid system inspired by printed transit maps, architectural sign totems, and platform schematics.

### Spatial Model
- **Grid Structure:** A 12-column desktop grid with a firm `24px` (`1.5rem`) gutter and `32px` (`2rem`) outer margin. On mobile, this condenses into a 4-column layout with `16px` gutters and `16px` outer margins.
- **The 8px Baseline Unit:** Component paddings and vertical alignments adhere strictly to multiples of 8px (utilizing the `space-*` scale) to maintain rigid tabular balance across screens.
- **Diagrammatic Line Alignments:** Content containers frequently integrate with explicit route-line borders. Spacing between containers and structural transit line dividers must directly accommodate standard 12px route tracks without visual clipping.
- **Reflow Behavior:** On narrower screens, multidirectional route schematics reflow to linear vertical trunks, maintaining 90-degree branch indicators rather than diagonal layouts.

## Elevation & Depth

This system operates entirely without shadows, blurs, or faux lighting sources. Depth and visual hierarchy are communicated strictly through flat, layered physical sign mechanics.

### Depth Mechanics
- **Zero Elevation Shadow Policy:** `box-shadow` values are strictly `none`. 
- **Enamelled Steel Borders:** Layers and module frames are established using flat solid borders in `#1c1c1c` (ranging from 2px for standard panels to 4px for terminal headers).
- **Physical Sign Plates:** Higher hierarchy modules emulate metal signage plates attached to structural beams: white background `#ffffff`, enclosed in a 3px `#1c1c1c` perimeter stroke, anchored by solid high-contrast header bands.
- **Interchange Overlays:** Floating contextual sheets (e.g., station detail drawouts, disruption alerts) appear as stacked plates bounded by crisp black boundaries with a solid black offset line or 100% opaque contrast backing.

## Shapes

The geometric framework is predominantly sharp (`0`), reflecting the clean shear-cut geometry of physical metal signage and architectural display boards.

### Geometric Exceptions
- **Panels & Containers:** Absolute rectangular precision (`0px` border radius).
- **Interchange Nodes:** Exact circular forms (`50%` / circular pill) reserved specifically for map station rings, interchange junctions, and iconic roundel emblems.
- **Directional Chevrons & Connectors:** Angular geometric forms constrained to 0, 45, and 90-degree vector cuts.

## Components

### Buttons & Action Bars
- **Primary Wayfinding Button:** Solid `#1c1c1c` background, `#ffffff` uppercase Space Grotesk text, 0px border radius, with a minimum height of 48px. Active/hover state flips inversion: `#ffffff` background with 3px solid `#1c1c1c` border and `#1c1c1c` text.
- **Transit Route Action Button:** Background in line colors (`#e32017`, `#0098d4`, `#00782a`), bold white uppercase typography, zero border radius, accompanied by an explicit directional arrow icon.

### Route Lines & Connectors
- **12px Diagrammatic Track:** Vector tracks rendered with an exact 12px stroke weight, constrained strictly to 0°, 45°, and 90° orientation.
- **Interchange Station Rings:** White circular rings (`#ffffff`) with a 4px solid black (`#1c1c1c`) border, centered directly over or terminating the 12px route lines. Minimum outer diameter of 24px.
- **Standard Stop Ticks:** Solid rectangular bars (`4px` wide by `12px` long) protruding perpendicularly (90°) from the route line.

### Station Enamel Cards & Wayfinding Totems
- Pure `#ffffff` ground enclosed by a 2px or 3px `#1c1c1c` perimeter stroke.
- Top of the card features a solid color bar (12px height) matching the line identity (e.g., `#e32017`).
- Station names rendered in bold uppercase `station-headline-lg`.
- Bottom rail hosts zone pills, transfer route indicators, and step-free accessibility symbols.

### Chips & Route Badges
- **Roundel & Route Bullets:** 28px square or circular badges with a solid transit color background (`#e32017`, `#0098d4`, `#00782a`, `#ffd300`) and bold central alphanumeric line identifiers in white (or `#1c1c1c` on yellow).
- **Platform Badges:** Crisp rectangular tags with a 2px black outline, displaying "PLATFORM X" in uppercase tabular lettering.

### Lists & Timetable Displays
- Striped, high-contrast rows bounded by horizontal 1px or 2px solid `#1c1c1c` dividing rules.
- Arrival countdowns rendered in high-visibility bold numbers with minutes label ("2 MIN", "ON TIME", "DELAYED").
- No alternating soft zebra striping; division is maintained purely through explicit vector lines.

### Inputs & Search Fields
- Crisp rectangular input boxes with 2px solid `#1c1c1c` borders and white backgrounds.
- Placeholder text in `#1c1c1c` at 50% opacity.
- Focus state thickens border to 4px solid `#0098d4` (Metro Blue) or `#1c1c1c` with zero outline blur.
- Station search autosuggest items formatted as transit line badges with transfer interchange icons.