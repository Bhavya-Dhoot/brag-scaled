---
name: Gallery Deadpan
colors:
  surface: '#faf9f5'
  surface-dim: '#dbdad6'
  surface-bright: '#faf9f5'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f4f0'
  surface-container: '#efeeea'
  surface-container-high: '#e9e8e4'
  surface-container-highest: '#e3e2df'
  on-surface: '#1b1c1a'
  on-surface-variant: '#444748'
  inverse-surface: '#30312e'
  inverse-on-surface: '#f2f1ed'
  outline: '#747878'
  outline-variant: '#c4c7c7'
  surface-tint: '#5f5e5e'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#1c1b1b'
  on-primary-container: '#858383'
  inverse-primary: '#c8c6c5'
  secondary: '#5f5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e2dfde'
  on-secondary-container: '#636262'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#241a00'
  on-tertiary-container: '#9e8028'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474646'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#474746'
  tertiary-fixed: '#ffe08f'
  tertiary-fixed-dim: '#e6c364'
  on-tertiary-fixed: '#241a00'
  on-tertiary-fixed-variant: '#584400'
  background: '#faf9f5'
  on-background: '#1b1c1a'
  surface-variant: '#e3e2df'
typography:
  display:
    fontFamily: Inter
    fontSize: 3.5rem
    fontWeight: '300'
    lineHeight: '1.08'
    letterSpacing: -0.04em
  display-mobile:
    fontFamily: Inter
    fontSize: 2.25rem
    fontWeight: '300'
    lineHeight: '1.12'
    letterSpacing: -0.03em
  headline-lg:
    fontFamily: Inter
    fontSize: 2.25rem
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.03em
  headline-lg-mobile:
    fontFamily: Inter
    fontSize: 1.75rem
    fontWeight: '400'
    lineHeight: '1.25'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 1.5rem
    fontWeight: '400'
    lineHeight: '1.3'
    letterSpacing: -0.02em
  headline-sm:
    fontFamily: Inter
    fontSize: 1.125rem
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 1.125rem
    fontWeight: '300'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: Inter
    fontSize: 0.9375rem
    fontWeight: '400'
    lineHeight: '1.55'
    letterSpacing: 0.005em
  body-sm:
    fontFamily: Inter
    fontSize: 0.8125rem
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0.01em
  label-lg:
    fontFamily: Space Mono
    fontSize: 0.8125rem
    fontWeight: '400'
    lineHeight: '1.4'
    letterSpacing: 0.06em
  label-md:
    fontFamily: Space Mono
    fontSize: 0.6875rem
    fontWeight: '400'
    lineHeight: '1.3'
    letterSpacing: 0.08em
  label-sm:
    fontFamily: Space Mono
    fontSize: 0.625rem
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: 0.12em
spacing:
  gutter: 1.5rem
  gutter-desktop: 2.5rem
  margin: 1.25rem
  margin-tablet: 2.5rem
  margin-desktop: 4rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 2rem
  space-xl: 3.5rem
---

## Brand & Style

This design system embodies the clinical authority and spatial quietude of the high-contemporary white-cube gallery. Built around institutional deadpan minimalism, the interface treats the screen as architectural surface rather than software chrome. Information presents itself with the calculated detachment of a curator’s wall text: stark, unhurried, and devoid of ornamental distraction.

The audience encompasses blue-chip collectors, institutional curators, critics, and art advisory figures who prioritize spatial purity, absolute clarity, and deliberate typographic rhythm. The design rejects common consumer UI patterns—avoiding rounded pills, decorative badges, and saturated accents—in favor of hairline grid lines, precise typographic hierarchy, and generous negative space that honors the visual weight of fine art.

## Colors

The palette directly models the physical components of an immaculate gallery exhibition space:
- **Canvas Base (`#f5f4f0`):** The lime-washed, chalky white-cube gallery wall. Used across primary backdrops and spatial fields.
- **Placard Ink (`#222222`):** Dense, matte carbon ink used for didactic descriptions, catalog numbers, and supporting text.
- **Framed Artwork Black (`#111111`):** The primary graphic anchor; an absolute, obsidian black defining titles, core action targets, and rigid perimeter framing.
- **Shadow Tone (`#d9d6ce`):** Natural cast shadow on primed plaster, providing muted hairline dividers, inactive borders, and structural grid rules without adding artificial grayness.
- **Burnished Gold (`#c9a84c`):** Institutional brass patina, used sparingly for provenance stamps, edition numbers, acquisition states, and curated milestones.
- **Warm Spotlight (`#fff4d6`):** Ambient accent for soft state highlights, selected object indicators, and subtle illuminated planes.

## Typography

The typographic strategy pairs a tightly tracked, neutral neo-grotesque (`Inter`) set with light weights for editorial headings and didactic texts, offset by a calibrated monospaced engine (`Space Mono`) for archival metadata, accession numbers, dimensions, and placard ledgers.

Headers reject dramatic weights, favoring architectural lightness (`300` and `400`) at scale. Case styles are rigorously disciplined: headings employ sentence case, while archival classifications and cataloging indices are presented in monospaced uppercase with generous tracking.

## Layout & Spacing

The layout is structured upon a strict 12-column architectural grid on desktop (4 columns on mobile, 8 on tablet). Rather than packing content, the grid enforces wide perimeter framing, recreating the generous clearance around wall-hung canvas installations.

Key architectural layout rules:
- **Asymmetric Offsets:** Placards and metadata hang offset from artwork containers, aligning strictly with bottom edges rather than centering.
- **Fixed Marginal Anchors:** Header and status ledgers sit on 1px physical borders at screen perimeters, locking the viewer into a formal gallery vitrine.
- **Section Rhythm:** Vertical section breaks rely on `space-xl` increments, allowing the eye to reset between viewing sequences without card enclosures.

## Elevation & Depth

This system avoids layered dropshadows, blurs, or skeuomorphic z-planes. Depth is articulated exclusively through structural contact:
- **Plaster Flush (Flat):** All panels and viewports share the foundational plane of `#f5f4f0`.
- **Structural Inset / Boundary:** 1px hairline rules using `#d9d6ce` articulate boundaries. Raised surfaces do not cast blurred shadows; instead, active overlays or modal inspections use a crisp 1px border in `#111111` accompanied by a flat, unblurred 2px offset keyline in `#d9d6ce`.
- **Spotlight Hover:** Surface hover states employ a subtle wash of `#fff4d6` at 40% opacity across targeted cells, evoking a ceiling fixture focusing upon an exhibit.

## Shapes

The geometry of this design system is absolute and razor-sharp (`roundedness: 0`). Zero corner radii apply to every visual primitive, including buttons, dialogs, inputs, thumbnail viewports, and wall placards. Forms reflect the physical cut edges of heavy archival board, cut museum glass, and metal picture frames.

## Components

### Wall Placards (Art Labels)
- Rectangular containers rendered in `#f5f4f0` with a 1px border in `#d9d6ce`.
- Internal arrangement mimics standard museum wall labeling: artist name in `headline-sm`, work title in italicized `body-md`, year/medium/dimensions in `body-sm`, and catalog acquisition code in `label-sm` monospaced type aligned bottom-right.
- Optional provenance or brass status badge set in `#c9a84c` hairline border with matching uppercase micro-text.

### Buttons & Interactive Triggers
- **Primary:** Obsidian `#111111` fill with `#f5f4f0` text. Sharp corners, 0.75rem vertical padding, 1.75rem horizontal padding. No shadow. Active state shifts background to `#222222`.
- **Secondary (The Folio Outline):** Transparent fill, 1px `#111111` hairline stroke, uppercase `label-md` lettering.
- **Placard Action / Curatorial Link:** Inline text link styled with a continuous 1px bottom border in `#c9a84c`, shifting to `#111111` on hover.

### Inputs & Inquiries
- Flat `#f5f4f0` background with a solitary 1px bottom rule in `#d9d6ce`.
- Focus state transforms the bottom rule to a 1px solid `#111111`.
- Input text renders in `body-md` (`#111111`), placeholder text sits quietly in `#d9d6ce` uppercase mono.

### Lists & Inventory Registers
- Linear rows partitioned by 1px `#d9d6ce` dividers with zero horizontal padding outside the grid margin.
- Information structured in strict columns: Lot / Accession ID (`label-md`), Artist / Title (`body-md`), Medium (`body-sm`), Price / Status (`label-md`). Hovering any row casts a quiet `#fff4d6` ambient fill across the entire line.

### Checkboxes & Selectors
- Rigid square boxes (16x16px), 1px `#111111` stroke, unrounded.
- Selected state fills completely with `#111111` leaving an unadorned, centered 6x6px interior cutout in `#f5f4f0`.

### Exhibition Vitrine & Framing Cards
- Image frames use zero overflow radius and are bounded by 1px borders in `#d9d6ce` or a double hairline boundary evoking museum matting.
- Artwork retains uninhibited scale; metadata remains strictly exterior to the image frame.