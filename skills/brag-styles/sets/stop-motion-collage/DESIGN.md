---
name: Stop-Motion Paper Collage
colors:
  surface: '#fff8f4'
  surface-dim: '#fdd2a7'
  surface-bright: '#fff8f4'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fff1e7'
  surface-container: '#ffead8'
  surface-container-high: '#ffe3ca'
  surface-container-highest: '#ffdcbb'
  on-surface: '#2c1700'
  on-surface-variant: '#59413b'
  inverse-surface: '#442b0d'
  inverse-on-surface: '#ffeee0'
  outline: '#8d7169'
  outline-variant: '#e1bfb6'
  surface-tint: '#ae3108'
  primary: '#ab2f05'
  on-primary: '#ffffff'
  primary-container: '#cd471f'
  on-primary-container: '#fffbff'
  inverse-primary: '#ffb5a0'
  secondary: '#006a63'
  on-secondary: '#ffffff'
  secondary-container: '#81f6e9'
  on-secondary-container: '#007169'
  tertiary: '#605b52'
  on-tertiary: '#ffffff'
  tertiary-container: '#797469'
  on-tertiary-container: '#fffbff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdbd1'
  primary-fixed-dim: '#ffb5a0'
  on-primary-fixed: '#3b0900'
  on-primary-fixed-variant: '#872100'
  secondary-fixed: '#81f6e9'
  secondary-fixed-dim: '#62d9cd'
  on-secondary-fixed: '#00201d'
  on-secondary-fixed-variant: '#00504a'
  tertiary-fixed: '#e9e2d5'
  tertiary-fixed-dim: '#cdc6b9'
  on-tertiary-fixed: '#1e1b14'
  on-tertiary-fixed-variant: '#4b463d'
  background: '#fff8f4'
  on-background: '#2c1700'
  surface-variant: '#ffdcbb'
typography:
  display-lg:
    fontFamily: Bricolage Grotesque
    fontSize: 56px
    fontWeight: '800'
    lineHeight: 64px
    letterSpacing: -0.03em
  display-lg-mobile:
    fontFamily: Bricolage Grotesque
    fontSize: 36px
    fontWeight: '800'
    lineHeight: 44px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Bricolage Grotesque
    fontSize: 36px
    fontWeight: '800'
    lineHeight: 44px
    letterSpacing: -0.02em
  headline-lg-mobile:
    fontFamily: Bricolage Grotesque
    fontSize: 28px
    fontWeight: '800'
    lineHeight: 36px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Bricolage Grotesque
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Bricolage Grotesque
    fontSize: 20px
    fontWeight: '700'
    lineHeight: 28px
  body-lg:
    fontFamily: Courier Prime
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Courier Prime
    fontSize: 15px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Courier Prime
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 20px
  label-lg:
    fontFamily: Space Mono
    fontSize: 14px
    fontWeight: '700'
    lineHeight: 20px
    letterSpacing: 0.05em
  label-md:
    fontFamily: Space Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.06em
  label-sm:
    fontFamily: Space Mono
    fontSize: 10px
    fontWeight: '700'
    lineHeight: 14px
    letterSpacing: 0.08em
spacing:
  gutter: 1.5rem
  gutter-mobile: 1rem
  margin: 2.5rem
  margin-mobile: 1.25rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.5rem
---

## Brand & Style

This design system draws its soul from stop-motion paper animation, physical zines, and handcrafted collage boards. It deliberately rejects cold, sterile digital minimalism in favor of tangible craft, paper weight, and human touch. 

The aesthetic is built on raw material reality: warm, fibrous kraft cardboard serves as the underlying worktable, layered with hand-cut paper stock, torn edges, and masking tape mending. Visual rhythm is derived from deliberate imperfection—subtle letter rotations, uneven paper scraps, postage stamp badges, and stamped ink impressions.

The audience consists of creative professionals, storytellers, makers, and indie platforms seeking an interface with tactile presence, warmth, and expressive physical storytelling. Every screen should feel like a physical workspace captured frame by frame under warm studio lighting.

## Colors

The palette simulates physical paper stocks laid over a corrugated kraft work surface.

- **Neutral Base (`#c9a27a`)**: Corrugated kraft cardboard. Used for the foundational viewport background, drawer trays, and deep canvas containers.
- **Tertiary / Paper Cream (`#f7efe2`)**: Uncoated, warm fibrous paper stock. Used as the primary surface container for cards, sheets, inputs, and modaled canvases.
- **Primary / Tomato Red Paper (`#e4572e`)**: Vibrant matte construction paper. Reserved for high-priority actions, critical highlights, stamped accents, and expressive emphasis.
- **Secondary / Vibrant Teal Paper (`#17a398`)**: Saturated cyan-teal cardstock. Used for secondary actions, interactive toggles, success notes, and contrasting cutout badges.
- **Ink Black (`#1d1d1d`)**: Dense offset printing ink, replacing digital pure black for all typography, stamp strokes, and outlines. Never use `#000000`.
- **Washi / Masking Tape (`rgba(235, 225, 185, 0.85)`)**: Translucent cream tape with fibrous borders, layered across corners and top edges to physically anchor elements to the cardboard base.

## Typography

The typographic hierarchy is inspired by ransom notes, DIY zines, and mechanical typewriter receipts.

- **Display & Headlines (`Bricolage Grotesque`)**: Heavy, quirky, condensed characters mimicking thick letterpress blocks and magazine cutouts. For hero headlines, apply the "ransom cutout" pattern: wrap individual letters or words in alternating paper background scraps (`#f7efe2`, `#e4572e`, `#17a398`) with alternating slight CSS rotations (`-2deg`, `1.5deg`, `-1deg`, `2.5deg`).
- **Body & Longform (`Courier Prime`)**: Simulates direct monospaced mechanical typing directly onto paper sheets. Delivers high legibility while sustaining physical manuscript warmth.
- **Labels, Stamps & Data (`Space Mono`)**: Used in uppercase for technical identifiers, metadata tags, badges, and luggage label stamps, echoing archival library index cards and punch cards.

## Layout & Spacing

The layout behaves like an art director's multi-layered cutting table using an offset 12-column grid.

- **Desktop (1024px+)**: 12 columns with `2.5rem` outer margins and `1.5rem` gutters. Elements are intentionally nudged off absolute grid lines using micro-rotations (`-0.75deg` to `+1deg`) and staggered vertical offsets to prevent sterile alignments.
- **Tablet (768px - 1023px)**: 8 columns with `2rem` outer margins and `1.25rem` gutters. Stacks collapse into two-column staggered card assemblies.
- **Mobile (< 768px)**: 4 columns with `1.25rem` outer canvas margin and `1rem` gutters. Cards snap into single-column flows; tilt angles are restricted to `<= 0.5deg` to maximize readable horizontal screen area.
- **Whitespace & Overlap**: Spacing is generous (`space-lg` to `space-xl`) to allow realistic paper dropshadows and washi tape pieces to overlap neighboring cards without clipping boundaries.

## Elevation & Depth

Depth in this system is strictly physical: the casting of light onto real paper stocks laid on kraft cardboard. Never employ digital gradients, glow blurs, or glassy backdrop filters.

- **Level 0 (Worktable Kraft Base)**: Flat `#c9a27a`. No shadows.
- **Level 1 (Direct Cutout Surface - Cards & Sticky Notes)**:
  `box-shadow: 0 2px 4px -2px rgba(29, 29, 29, 0.2), 0 4px 6px -1px rgba(29, 29, 29, 0.25);`
  Represents flat cardstock sitting right atop cardboard.
- **Level 2 (Lifted Paper / Floating Modules / Hover States)**:
  `box-shadow: 0 10px 15px -3px rgba(29, 29, 29, 0.22), 0 4px 6px -2px rgba(29, 29, 29, 0.18);`
  Applied during hover interactions accompanied by a subtle physical lift (`transform: translateY(-2px) scale(1.01)`).
- **Level 3 (Modals, Overlays & Dragging Cutouts)**:
  `box-shadow: 0 20px 25px -5px rgba(29, 29, 29, 0.28), 0 10px 10px -5px rgba(29, 29, 29, 0.2);`
  Simulates a paper slip picked up high above the board.
- **Tape Physicality**: Masking tape overlays sit on Level 2 with a flat, semi-transparent cast: `box-shadow: 0 1px 2px rgba(29, 29, 29, 0.15);` and jagged CSS mask-image torn ends.

## Shapes

The shape system is strictly sharp (`roundedness: 0`), reflecting straight guillotine cuts, hand scissors, and torn paper grain.

- **Cuts**: All borders are `0px` border-radius by default. Rounded pill shapes are prohibited.
- **Torn Edge Borders**: Specific bottom borders of cards and badges utilize CSS `clip-path` polygon zigzag patterns or rough SVG mask edges to emulate hand-torn deckle paper.
- **Washi Tape Strips**: Rectangles (`height: 24px`, variable width) fixed at `-3deg` to `3deg` across corners or centered top edges, featuring serrated or torn vertical edges (`clip-path: polygon(...)`).
- **Postage Stamps**: Badges use perforated border edges created via radial-gradient mask cutout patterns.
- **Grommets**: Circular punched holes (`width: 14px`, `height: 14px`, border: 2px solid `#1d1d1d`, background: transparent) for tag-style components, complete with a drawn vertical hangline.

## Components

### Buttons
- **Primary**: Solid tomato red paper (`#e4572e`), cream ink text (`#f7efe2`), ink black solid 1.5px border (`#1d1d1d`). Sharp corners. Flat paper shadow (Level 1). Hover: slight rotate (`-1deg`) and lift (Level 2). Active: depressed shadow (`0 1px 2px rgba(0,0,0,0.3)`) and downward translation (`translate(1px, 1px)`).
- **Secondary**: Teal paper cut (`#17a398`), ink black text (`#1d1d1d`), sharp 1.5px solid border.
- **Ghost / Cardboard Plain**: Cream paper swatch with dashed 1.5px border, ink black text.

### Cards & Sheets
- Built from cream paper stock (`#f7efe2`) or craft brown stock.
- Decorated with a washi tape strip (`rgba(235, 225, 185, 0.85)`) affixed across the top edge or top-right corner extending beyond the card boundary.
- Default resting rotation: alternating cards receive `transform: rotate(-0.5deg)` or `transform: rotate(0.75deg)`.
- Shadows conform strictly to Level 1 elevation tokens.

### Input Fields
- Monospaced typography (`Courier Prime`) inside a flat cream cutout panel with an inset stamped shadow (`box-shadow: inset 0 2px 4px rgba(29,29,29,0.12)`).
- Border: 1.5px solid `#1d1d1d`.
- Focus state: Replaces outline with a high-contrast offset border resembling an ink pen underline or double stamp mark.

### Checkboxes & Radio Buttons
- **Checkbox**: Hand-drawn square aesthetic (`18x18px`), cream background, 2px `#1d1d1d` border. Checked state renders a bold ink "X" or handwritten scribble mark in tomato red (`#e4572e`).
- **Radio Button**: Octagonal or diamond-clipped paper swatch (`clip-path`). Selected state features an irregular solid ink blot center.

### Chips & Badges
- **Postage Stamp**: Serrated scalloped edges with monospaced uppercase text (`Space Mono`), stamped date/icon, and subtle ink fade.
- **Scrap Confetti**: Tiny irregular rectangular slips pinned in primary tomato red or secondary teal.

### Lists
- Ruled memo paper styling: subtle horizontal lines in light ink tint (`rgba(29, 29, 29, 0.15)`).
- List markers use stamped numerals or cutout square dots rotated at random angles.