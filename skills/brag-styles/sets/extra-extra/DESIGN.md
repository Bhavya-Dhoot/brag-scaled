---
name: Broadsheet Editorial
colors:
  surface: '#fff9ea'
  surface-dim: '#dfdaca'
  surface-bright: '#fff9ea'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f9f3e3'
  surface-container: '#f4eedd'
  surface-container-high: '#eee8d8'
  surface-container-highest: '#e8e2d2'
  on-surface: '#1e1c12'
  on-surface-variant: '#444748'
  inverse-surface: '#333026'
  inverse-on-surface: '#f7f0e0'
  outline: '#747878'
  outline-variant: '#c4c7c7'
  surface-tint: '#5f5e5e'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#1c1b1b'
  on-primary-container: '#858383'
  inverse-primary: '#c8c6c5'
  secondary: '#b71f27'
  on-secondary: '#ffffff'
  secondary-container: '#fe5453'
  on-secondary-container: '#5c0009'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#1c1c18'
  on-tertiary-container: '#86847f'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474746'
  secondary-fixed: '#ffdad7'
  secondary-fixed-dim: '#ffb3ae'
  on-secondary-fixed: '#410004'
  on-secondary-fixed-variant: '#930015'
  tertiary-fixed: '#e6e2dc'
  tertiary-fixed-dim: '#c9c6c0'
  on-tertiary-fixed: '#1c1c18'
  on-tertiary-fixed-variant: '#484742'
  background: '#fff9ea'
  on-background: '#1e1c12'
  surface-variant: '#e8e2d2'
typography:
  masthead:
    fontFamily: Playfair Display
    fontSize: 84px
    fontWeight: '900'
    lineHeight: 84px
    letterSpacing: -1.5px
  headline-monumental:
    fontFamily: Playfair Display
    fontSize: 64px
    fontWeight: '900'
    lineHeight: 64px
    letterSpacing: -0.5px
  headline-lead:
    fontFamily: Playfair Display
    fontSize: 42px
    fontWeight: '700'
    lineHeight: 44px
  headline-secondary:
    fontFamily: Playfair Display
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 32px
  deck-subhead:
    fontFamily: Libre Franklin
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 24px
  body-lead:
    fontFamily: Libre Franklin
    fontSize: 13px
    fontWeight: '500'
    lineHeight: 17px
  body-column:
    fontFamily: Libre Franklin
    fontSize: 11.5px
    fontWeight: '400'
    lineHeight: 15px
  dateline:
    fontFamily: Courier Prime
    fontSize: 11px
    fontWeight: '700'
    lineHeight: 13px
    letterSpacing: 0.5px
  caption-telemetry:
    fontFamily: Courier Prime
    fontSize: 9.5px
    fontWeight: '400'
    lineHeight: 12px
  ear-masthead:
    fontFamily: Courier Prime
    fontSize: 10px
    fontWeight: '700'
    lineHeight: 12px
  pull-quote:
    fontFamily: Playfair Display
    fontSize: 22px
    fontWeight: '700'
    lineHeight: 26px
  classified-title:
    fontFamily: Libre Franklin
    fontSize: 10.5px
    fontWeight: '700'
    lineHeight: 12px
    letterSpacing: 1px
spacing:
  gutter: 16px
  margin: 32px
  space-xs: 4px
  space-sm: 8px
  space-md: 12px
  space-lg: 16px
  space-xl: 24px
---

## Brand & Style

This design system translates authentic early-to-mid 20th century broadsheet print journalism into high-density 16:9 widescreen editorial broadcasts, video storyboards, and interactive archives. The aesthetic abandons all modern software ornamentation—there are no drop shadows, no border-radii, no backdrop blurs, and no synthetic gradients. 

The visual identity relies entirely on tactile ink-on-paper mechanics: mechanical letterpress ink density, visible vertical ink rules, double-line horizontal registers, typographic tension between massive serif titling and disciplined column body text, weathered weather/edition ear panels, and coarse halftone photo engraving. 

The emotional tone evokes urgent investigative gravity, historical permanence, and unfiltered mechanical documentation. Every visual surface simulates unbleached rag paper stock kissed by rapid rotary press cylinders.

## Colors

The palette is strictly restricted to five mechanical values replicating chemical ink applied to low-acid newsprint paper stock:

- **Paper Canvas (`#ece6d6`)**: The unbleached, warm-toned fibrous newsprint substrate serving as the universal root background and inverted surface.
- **Dense Black Ink (`#161616`)**: The primary ink state. Used for monumental mastheads, primary lead headlines, thick structural borders, and intense line cuts.
- **Muted Newspaper Ink (`#3b3a36`)**: Secondary ink state indicating secondary subheadings, deck copy, justified column body text, and line-screened illustrations.
- **Rule Grey (`#b5aea0`)**: Hairline ink matrix color for 1px column separators, dateline frames, boxed classified grids, and horizontal registration rules.
- **Spot Red (`#c1272d`)**: Strictly reserved as an editorial alert accent. Used solely for the masthead "EXTRA" banner, urgent breaking bulletin flashes, stamp seals, and urgent telegraphic telemetry markers. Never to be diluted into tints or soft gradients.

## Typography

The typography system relies on three distinct functional voices reflecting physical metal and wood types:

- **Playfair Display**: The voice of editorial hierarchy. Rendered in Black (900) and Bold (700) for the primary masthead, monumental multi-column spanning headlines, and italicized pull quotes. Headlines must sit tightly on their baselines with compact line-height mimicking manual typesetters packing lead blocks.
- **Libre Franklin**: The workhorse editorial face. Used for deck subheads, photo credits, classifieds, and column body copy. In column settings, body copy is tightly set and justified with hyphenation enabled to mimic dense broadsheet columns.
- **Courier Prime**: The technical, mechanical print marker. Used strictly for telegraphic captions, edition markers, timestamps, pricing boxes, stock index listings, and weather ear indicators. It brings the precision of hot-metal teletype machines and typewriter press passes into the layout.

## Layout & Spacing

Designed precisely around a 1920x1080 fixed-frame widescreen canvas emulating an unfolded broadsheet front page:

- **5-Column Editorial System**: The primary viewport is partitioned into five equal columns spanning 345.6px per column (inclusive of 16px column gutters) bounded by outer canvas margins of 32px.
- **Vertical Separators**: Every column is demarcated by a continuous 1px solid hairline rule in `#b5aea0` running between elements. When an article or photograph spans 2, 3, or 5 columns, the internal column rules are interrupted only within that module's rectangular bounds.
- **Horizontal Crease & Folds**: A subtle visual centerfold paper crease divides the upper and lower halves of the screen at precisely `y = 540px`, marked by horizontal double rules (`3px solid #161616`, `2px gap`, `1px solid #161616`) separating "Above the Fold" from "Below the Fold."
- **Ear Panels**: Flanking the 84px masthead, the top-left and top-right grid corners contain bordered 180px-wide ear boxes housing the daily weather summary, price, and edition registry.

## Elevation & Depth

This system utilizes zero z-axis blur elevation, zero cast drop shadows, and zero translucent blurs. Physical depth is achieved solely through physical letterpress and printing press techniques:

- **Ink Rules & Hairlines**: Hierarchical separation uses 1px solid rules (`#b5aea0`) for internal grid columns, 2px solid rules (`#161616`) for secondary article division, and classic newspaper double rules (a thick 3px rule paired with a parallel 1px hairline rule separated by 2px of paper ground) for section titles and masthead framing.
- **Boxed Insets & Hairline Frames**: Prominent sidebars, classifieds, and urgent bulletins use a complete 1px or 2px bounding box with 6px internal padding.
- **Inverted Mechanical Banners**: Depth and high-priority emphasis are created through high-contrast ink fills—solid `#161616` background ribbons with negative `#ece6d6` typography, or urgent `#c1272d` spot red blocks with crisp `#ece6d6` lettering.
- **Halftone Lithography**: Visual media does not appear as clean digital pixels; photos are processed through coarse black-and-white stipple/halftone dot patterns directly screening onto `#ece6d6`.

## Shapes

The shape system is strictly **Sharp (0)**. There are zero rounded corners on any surface, card, badge, rule, or button. 

Every visual container conforms to strict rectangular perimeters cut along horizontal and vertical metal rules. Frames are defined by sharp 90-degree right angles, evoking cut paper, wood blocks, lead spacing slugs, and razor-cut paste-up boards.

## Components

### Masthead & Ear Panels
- **Masthead Plate**: Positioned top-center. Centered monumental title set in Playfair Display 900. Flanked by left and right ear panels. Framed above and below by double rules (thick top/thin bottom rule below, thin top/thick bottom rule above).
- **Ear Panels**: Rectangular 1px boxed compartments in the top corners. Left Ear: Weather forecast, tide data, and solar charts set in `Courier Prime` 10px bold. Right Ear: Edition number, price ($0.15 / ONE PENNY), and dateline stamp.

### Editorial Article Modules
- **Spanning Headlines**: Sits directly atop columns. Multi-line titles set in `Playfair Display` with zero bottom margin to the deck rule.
- **Deck & Byline**: Below headline, bordered by a top-and-bottom hairline rule. Contains uppercase byline ("BY OUR CORRESPONDENT") and location dateline in `Courier Prime` followed by justified body text.
- **Column Columns**: Justified alignment, hyphenated, with a 2-line drop-cap letter pressed in `#161616` introducing the initial paragraph.

### Buttons & Interactive Controls (Broadsheet Press Style)
- **Action Triggers**: Flat rectangular blocks bordered by 2px `#161616` ink borders. Background `#ece6d6`, text in uppercase `Libre Franklin` 11px Bold with 1.5px letter-spacing.
- **Active / Pressed State**: Solid inversion to dense black (`#161616` background with `#ece6d6` paper text).
- **Urgent Action Buttons**: Filled completely with spot red (`#c1272d`) with unbleached paper-white text.

### Classified Ads & Market Tickers
- **Classified Block**: Dense rectangular boxes with 1px solid `#b5aea0` borders. Header rendered in centered uppercase bold within an inverted black bar. Content set in tight 10px `Libre Franklin` with bold categorical lead-ins ("FOR SALE:", "NOTICE:", "WANTED:").
- **Financial Telemetry Strip**: Single horizontal ticker pinned to the page base, formatted in `Courier Prime` with 1px hairline top and bottom rules.

### Editorial Alerts & Breaking Stamps
- **EXTRA Stamp Badge**: Angled rectangular stamp or solid `#c1272d` ribbon reading "LATE EXTRA" or "WAR BULLETIN" in bold Courier Prime or Playfair Display. Bounded by double-lined spot-red rules.