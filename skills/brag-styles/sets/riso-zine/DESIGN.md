---
name: Riso Underground
colors:
  surface: '#fff8f4'
  surface-dim: '#dfd9d5'
  surface-bright: '#fff8f4'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f9f2ef'
  surface-container: '#f3ede9'
  surface-container-high: '#ede7e3'
  surface-container-highest: '#e7e1de'
  on-surface: '#1d1b19'
  on-surface-variant: '#58404a'
  inverse-surface: '#32302e'
  inverse-on-surface: '#f6efec'
  outline: '#8b707a'
  outline-variant: '#dfbeca'
  surface-tint: '#b60077'
  primary: '#b60077'
  on-primary: '#ffffff'
  primary-container: '#ff48b0'
  on-primary-container: '#5a0039'
  inverse-primary: '#ffafd2'
  secondary: '#395baa'
  on-secondary: '#ffffff'
  secondary-container: '#89a9fe'
  on-secondary-container: '#103b89'
  tertiary: '#7a499b'
  on-tertiary: '#ffffff'
  tertiary-container: '#b27dd4'
  on-tertiary-container: '#430f64'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffd8e7'
  primary-fixed-dim: '#ffafd2'
  on-primary-fixed: '#3d0025'
  on-primary-fixed-variant: '#8b005a'
  secondary-fixed: '#dae2ff'
  secondary-fixed-dim: '#b2c5ff'
  on-secondary-fixed: '#001847'
  on-secondary-fixed-variant: '#1c4291'
  tertiary-fixed: '#f4daff'
  tertiary-fixed-dim: '#e3b5ff'
  on-tertiary-fixed: '#2f004c'
  on-tertiary-fixed-variant: '#613082'
  background: '#fff8f4'
  on-background: '#1d1b19'
  surface-variant: '#e7e1de'
typography:
  headline-xl:
    fontFamily: Rubik
    fontSize: 48px
    fontWeight: '900'
    lineHeight: 52px
    letterSpacing: -0.03em
  headline-xl-mobile:
    fontFamily: Rubik
    fontSize: 32px
    fontWeight: '900'
    lineHeight: 36px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Rubik
    fontSize: 36px
    fontWeight: '900'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-lg-mobile:
    fontFamily: Rubik
    fontSize: 26px
    fontWeight: '900'
    lineHeight: 30px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Rubik
    fontSize: 24px
    fontWeight: '800'
    lineHeight: 28px
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Rubik
    fontSize: 18px
    fontWeight: '800'
    lineHeight: 22px
    letterSpacing: 0em
  body-lg:
    fontFamily: Space Mono
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
    letterSpacing: -0.01em
  body-md:
    fontFamily: Space Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
    letterSpacing: 0em
  body-sm:
    fontFamily: Space Mono
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 16px
    letterSpacing: 0.01em
  label-lg:
    fontFamily: Space Mono
    fontSize: 13px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.05em
  label-md:
    fontFamily: Space Mono
    fontSize: 11px
    fontWeight: '700'
    lineHeight: 14px
    letterSpacing: 0.08em
  label-sm:
    fontFamily: Space Mono
    fontSize: 10px
    fontWeight: '700'
    lineHeight: 12px
    letterSpacing: 0.1em
spacing:
  gutter: 1.25rem
  gutter-sm: 0.75rem
  margin: 2rem
  margin-sm: 1rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.5rem
---

## Brand & Style

The design system channels the tactile immediacy, DIY urgency, and mechanical quirks of vintage Risograph duplicator printing and underground zine culture. Targeted at creative subcultures, indie publishers, independent record labels, and subversive tech collectives, the aesthetic rejects the polished homogeneity of corporate SaaS.

The personality is intentionally physical, imperfect, and raw:
- **Mechanical Imperfection:** Celebrates the artifacts of physical reproduction—plate shift misregistration, ink bleed, grain, and manual paper handling.
- **Physical Metaphor:** Interfaces are constructed like assembled physical artifacts—bound leaflets, collaged scraps, pasted halftone prints, and stamped receipts.
- **Graphic Contrast:** High-impact spot ink impressions laid directly over porous, unbleached pulp paper.
- **Zero Digital Artifice:** Absolutely no modern ambient blurs, glassy backdrops, or interpolated multi-stop vector gradients. All depth and separation are produced via mechanical offset drop-shadows, paper collages, staples, and heavy linework.

## Colors

The palette simulates a strict physical spot-color print run on uncoated cream paper stock:

- **Paper Canvas (`#f4f1e8`):** Unbleached, warm-fibered pulp base used as the default screen background and substrate surface.
- **Fluoro Pink (`#ff48b0` - Primary Spot Drum):** Piercing, fluorescent neon pink ink layer. Used for urgent calls-to-action, primary structural highlights, and rogue accents.
- **Federal Blue (`#3255a4` - Secondary Spot Drum):** Dense, authoritative ink layer. Used for dominant typography, structural frames, dark buttons, and active states.
- **Overprint Violet (`#6b3a8c` - Overprint Blend):** The optical multiplication of Fluoro Pink and Federal Blue passing through the same registration coordinates (`mix-blend-mode: multiply`). Used for intersecting boundaries, stamped accents, and badges.
- **Newsprint Black (`#1b1917` - Neutral Dark):** Carbon-based density for deep text blocks, barcode strips, and staple hardware.
- **Muted Cream (`#e8e4d5`):** Substrate shade used for sunken panels, ticket stubs, and secondary card containers.

### Ink Emulation Rules
1. Never render gradients with transparent fade stops. Transitions must be simulated via CSS halftone dot radial patterns (`radial-gradient(#3255a4 1.5px, transparent 1.5px)` with a repeating grid pattern).
2. Elements styled with the overprint effect must apply `mix-blend-mode: multiply` against underlying elements or paper textures.
3. Interactive hover states do not fade opacity; they flip ink drums (e.g., Pink swaps to Federal Blue or inverts to solid paper ground).

## Typography

The typography system sets up a clash between heavy industrial block letterforms and utilitarian monospace typesetting.

- **Display & Headlines (`Rubik` weight 800–900):** Emulates ink-saturated woodblock or dense phototypesetting. Rendered tight, compressed, and predominantly in all-caps for `headline-xl` and `headline-lg`.
- **Body & Telemetry (`Space Mono`):** Directly recalls typewritten fanzines, stencil-cut instructions, and terminal receipts. Used strictly for continuous narrative, metadata, specs, and tabular information.

### Typographic Treatments
- **Misregistered Shadow Effect:** Important display titles can implement an offset duplicate layer in Fluoro Pink behind Federal Blue (`text-shadow: 3px 3px 0px #ff48b0`), replicating second-pass print misalignment.
- **Text Selection:** Text highlighted by the user must take an inverted fill: background `#ff48b0`, foreground `#f4f1e8`.

## Layout & Spacing

The layout is grounded in a modular cut-and-paste grid inspired by pasted editorial dummies and newspaper layouts:

- **Desktop (1024px+):** 12-column column structure with 2rem margins and 1.25rem gutters. Panels can break the grid intentionally via slight rotational skewing (-0.75deg to +1.25deg) to simulate hand-glued paste-ups.
- **Tablet (768px - 1023px):** 6-column grid with 1.5rem margins and 1rem gutters.
- **Mobile (< 768px):** Single-column stacked stream with 1rem margin boundaries and 0.75rem gaps. Skew transforms are disabled or restricted to decorative tape banners to prevent horizontal scroll bleed.

### Rhythm & Alignment
Spacing follows an 8-base monospace rhythm: 4px (`space-xs`), 8px (`space-sm`), 16px (`space-md`), 24px (`space-lg`), and 40px (`space-xl`). Components use dense, direct spacing rather than expansive corporate whitespace. Content cards butt up against one another with visible black/blue parting borders instead of invisible gutter margins.

## Elevation & Depth

Modern ambient blur shadows and soft z-index elevations are strictly prohibited. Depth is rendered via physical assembly metaphors:

1. **Plate Misregistration (Hard Drop Blocks):**
   - Objects sit elevated by throwing a sharp, unblurred, 100% opaque color block.
   - Primary Elevation: `box-shadow: 4px 4px 0px #3255a4`.
   - Offset Pink Misregistration: `box-shadow: 3px 3px 0px #ff48b0, 6px 6px 0px #3255a4`.
2. **Paper Collage Cutouts:**
   - Overlapping cards mimic paper fragments pasted on top of one another.
   - Distinct layers receive high-contrast borders (`2px solid #1b1917` or `2px dashed #3255a4`).
3. **Physical Bindings (Staples & Tape):**
   - Modals and focal cards feature visual hardware: dark charcoal metallic staple bars (`8px × 2px #1b1917` centered over top edges) or diagonal semi-translucent washi tape strips (`rgba(255, 72, 176, 0.45)`) across corners.
4. **Stamp Impressions:**
   - De-elevated or inset states (pressed inputs, checked items) use a negative cut-in border or a solid fill of `#e8e4d5` with inset solid shadow (`inset 2px 2px 0px #1b1917`).

## Shapes

The shape system is strictly zero-radius (`roundedness: 0`). Guillotine paper cutters and razor blades produce sharp 90-degree corners:

- **Rectilinear Precision:** Buttons, cards, modals, tabs, and tags carry hard, unfilleted corners (`border-radius: 0px`).
- **Rough Stamp Borders:** Selected callouts and badges use irregular stamped borders achieved via jagged SVG masks or jagged zig-zag borders (`border-image` simulating stamp perforations).
- **Sticker Cutouts:** Floating badges or novelty buttons may use an intentional angled cut corner (`clip-path: polygon(...)`) to mimic manually scissors-snipped cardstock.

## Components

### Buttons
- **Primary Button:** Solid Fluoro Pink (`#ff48b0`) background, 2px solid Newsprint Black (`#1b1917`) border, Federal Blue hard drop block (`box-shadow: 4px 4px 0px #3255a4`). Space Mono bold uppercase text. Hover shifts the button 2px down and right (`transform: translate(2px, 2px); box-shadow: 2px 2px 0px #3255a4`). Active state collapses shadow entirely (`translate(4px, 4px); box-shadow: none`).
- **Secondary Button:** Solid Cream (`#f4f1e8`) background, 2px solid Federal Blue (`#3255a4`) border, Fluoro Pink hard shadow (`4px 4px 0px #ff48b0`). Text in Federal Blue.
- **Destructive/Caution:** Alternating 45-degree diagonal warning stripes generated via CSS (`repeating-linear-gradient(45deg, #ff48b0, #ff48b0 10px, #f4f1e8 10px, #f4f1e8 20px)`).

### Cards & Pasteboard Tiles
- Background in Warm Paper (`#f4f1e8`) or Muted Cream (`#e8e4d5`).
- 2px solid Newsprint Black or Federal Blue framing.
- Header bars feature a reversed solid strip (e.g. solid Federal Blue block with white/cream Space Mono typography).
- Optional visual accents: Top center staple graphic (`4px × 12px` Newsprint Black rectangle) or a misregistered corner stamp reading `ISSUE №` or `APPROVED`.

### Input Fields & Controls
- **Text Inputs:** Monospace font, 2px solid Newsprint Black outline, `#f4f1e8` fill. On focus: thickens to 3px solid Federal Blue with a `3px 3px 0px #ff48b0` offset ring. No soft glow. Placeholder text in muted blue-grey ink.
- **Checkboxes:** Square 18×18px frame with a 2px solid border. Checked state displays a hand-drawn or heavy "X" mark rendered in Fluoro Pink overprint.
- **Radio Buttons:** Square outer boundary containing a solid nested square when selected (no circles).

### Chips, Badges & Labels
- Pill shapes are prohibited. Badges resemble perforated dispatch stamps or snipped masking tape strips.
- Typography is strictly uppercase `label-md` or `label-sm`.
- Accent badges apply `mix-blend-mode: multiply` against underlying content to simulate instant multi-pass printing.

### Lists & Navigation
- Grouped list items are delimited by dotted horizontal rules (`2px dotted #3255a4`) or zigzag invoice lines.
- Navigation links take an unvarnished underline on hover with a 4px Fluoro Pink marker-highlighter background sweep (`box-shadow: inset 0 -8px 0 0 #ff48b0`).

### Halftone Image Frames
- Photography and imagery must run through a two-color duotone matrix (Federal Blue shadows, Fluoro Pink midtones, Paper Cream highlights) with an explicit coarse halftone dot overlay screen.