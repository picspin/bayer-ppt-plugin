# Bayer Brand Visual System (from source assets)

**Sources**
- Color system PDF: `source/color-system.pdf` — *Bayer Color Guide*, Bayer AG Communications & Public Affairs, Leverkusen (InDesign PDF, dated 2018-03-19).
- Structured graphics PPTX theme: `source/structured-graphics.pptx` — *BC Chart Library* (Business Consulting), September 2018; theme scheme **Bayer 2017**.
- Official corporate template: `source/official-template.pptx` — *Bayer Chart pool* / *Bayer 16:9 Template Chart Pool*, August 2019 (“Updated version”); theme `PR_BG_Chart-Pool_16-9_2019-08-27`, clrScheme **Bayer 2017**.
- Icon expression POTX: `source/icon-language.potx` — *Bayer in Radiology Icon Library*, September 2020; theme name **Radiology**, clrScheme **Bayer 2017**.

**No Chinese body copy** appears in these assets (Official Template master includes a **内容** layout alias; German master placeholders exist). Extracted terminology is otherwise English (German place names on maps/flags only).

---

## Brand / product line

| Asset | Stated identity |
|-------|-----------------|
| Color Guide | Corporate Bayer color system (all divisions; colors are **not** assigned to specific divisions/departments) |
| Chart Library PPTX | Bayer **Business Consulting** chart/template library; closing layouts for **Bayer Pharmaceuticals**, **Bayer Crop Science**, **Bayer Animal Health** |
| Icon POTX | **Bayer in Radiology** / Bayer Radiology Icon Library (contrast media, injectors, workflow, IMCM, services) — product lines include Ultravist®, Gadovist®, Primovist®, Radimetrics®, MEDRAD® (Centargo, Stellant, etc.), Equipment Service |
| Official Chart Pool | Corporate **Bayer 16:9 Template Chart Pool** (Aug 2019); icon chapters include Business / Science / Medical & Pharma / **Crop Science**; closing slides cover Logos, Color, Gradient, Contact, **Information classification labeling** (Identity Net) |

---

## Color palette (authoritative HEX from Color Guide)

Citation: Color Guide overview pages (PDF text extract pp. ~3–4 of the guide: “The Bayer color palette consists of 12 colors plus white…”), plus one detail page per hue.

### Rules (do / don’t) — Color Guide overview

- **Must** use only the precise hues/tones defined in the guide.
- Palette = **12 colors + white**, in three families: **blues, greens, purples**.
- Each color has four hues: **bright / core / mid / dark**.
- Opacity: colors must stay within **20%–80%** for general tinting guidance in the overview; block color may be **100%**; on photography use **100% or 90%**.
- **Dark** hues: backgrounds or text. **Body text is usually set in dark blue** (Bayer Dark Blue).
- **Bright** tones: smaller background areas and text where appropriate.
- Lighter tints support/complement bright and dark tones.
- Colors are **not** mapped to divisions/departments.

**Theme custClr alignment:** Official Chart Pool MidGreen `#2B6636` matches this Guide; BC Chart Library theme MidGreen custClr `#2B6640` drifted — **Guide HEX wins**. Chart Pool also documents Traffic Light Red/Yellow/Green for status only.

**Internal classification (Chart Pool slide 330):** use the PowerPoint **CLASSIFICATION RIBBON** at Bayer; further info on Bayer Identity Net (URL printed on that slide). Do not invent classification marks.

### Blues

| Name | Hue | Pantone | RAL | RGB | HEX | CMYK | PDF section |
|------|-----|---------|-----|-----|-----|------|-------------|
| Bayer Bright Blue | Bright | 298C | 240 70 30 | 0/188/255 | `#00BCFF` | 71/0/0/0 | Bright Blue detail page |
| Bayer Blue | Core | 2192C | 5012 | 0/145/223 | `#0091DF` | 93/17/6/0 | Blue detail page |
| Bayer Mid Blue | Mid | 2152C | 240 40 30 | 0/97/127 | `#00617F` | 84/32/13/22 | Mid Blue detail page |
| Bayer Dark Blue | Dark | 2380C | 5011 | 16/56/79 | `#10384F` | 80/33/0/80 | Dark Blue detail page |

### Greens

| Name | Hue | Pantone | RAL | RGB | HEX | CMYK | PDF section |
|------|-----|---------|-----|-----|-----|------|-------------|
| Bayer Bright Green | Bright | 2299C | 110 80 70 | 137/211/41 | `#89D329` | 40/0/100/0 | Bright Green detail page |
| Bayer Green | Core | 376C | 120 70 75 | 102/181/18 | `#66B512` | 57/0/100/0 | Green detail page |
| Bayer Mid Green | Mid | 7742C | 6001 | 43/102/54 | `#2B6636` | 71/5/92/45 | Mid Green detail page |
| Bayer Dark Green | Dark | 553C | 160 30 15 | 0/68/34 | `#004422` | 82/30/65/76 | Dark Green detail page |

### Purples / magentas

| Name | Hue | Pantone | RAL | RGB | HEX | CMYK | PDF section |
|------|-----|---------|-----|-----|-----|------|-------------|
| Bayer Fuchsia | Bright | 1785C | 3018 | 255/49/98 | `#FF3162` | 0/88/62/0 | Fuchsia detail page |
| Bayer Raspberry | Core | 1925C | *(not listed on Raspberry detail)* | 211/15/75 | `#D30F4B` | 0/100/55/0 | Raspberry detail page |
| Bayer Mid Purple | Mid | 5135C | 4001 | 98/73/99 | `#624963` | 36/68/24/31 | Mid Purple detail page |
| Bayer Dark Purple | Dark | 518C | 330 20 20 | 68/50/71 | `#443247` | 55/88/32/63 | Dark Purple detail page |

### Neutrals / backgrounds / text

| Role | Value | Source |
|------|-------|--------|
| White | `#FFFFFF` | Color Guide (“12 colors plus white”); theme `lt1` |
| Black | `#000000` | Theme `dk1` (PPTX/POTX) — **not** named as a Bayer palette color in the Color Guide body |
| Body / dark text | Bayer Dark Blue `#10384F` | Color Guide: “Body text is usually set in dark blue” |
| Link (theme) | `#00BCFF` | Theme `hlink` |
| Followed link (theme) | `#89D329` | Theme `folHlink` |

Each color detail page also shows **coated/uncoated** swatches at 10%–100% transparency steps (for proofing).

### Theme scheme mapping (Bayer 2017 in PPTX/POTX)

| Scheme slot | HEX | Notes |
|-------------|-----|-------|
| dk1 | `#000000` | Black |
| lt1 | `#FFFFFF` | White |
| dk2 | `#FF3162` | Fuchsia |
| lt2 | `#624963` | Mid Purple |
| accent1 | `#10384F` | Dark Blue (primary dark) |
| accent2 | `#00BCFF` | Bright Blue |
| accent3 | `#004422` | Dark Green |
| accent4 | `#89D329` | Bright Green |
| accent5 | `#443247` | Dark Purple |
| accent6 | `#D30F4B` | Raspberry |

### Extra colors in theme `custClrLst` (not in the 12-color Color Guide)

Use only when building Radiology/product decks; do **not** treat as corporate palette defaults:

| Name (theme) | HEX |
|--------------|-----|
| Traffic Light Red | `#CC0000` |
| Traffic Light Yellow | `#FFCC00` |
| Traffic Light Green | `#66B512` (= Bayer Green) |
| Certegra | `#307A33` |
| Devices and Accessories | `#E46C0A` |
| Equipment Service / Urografin | `#6BC200` |
| Gadovist | `#BD197A` |
| Gastrografin | `#008264` |
| Iopamiron | `#C60B47` |
| Isovist | `#B1B3B3` |
| Magnevist | `#4E287E` |
| Primovist / Biliscopin | `#DA2B3E` |
| Radimetrics | `#2C5697` |
| Ultravist | `#0095C0` |

**Note:** Chart Library theme custom MidGreen is stored as `#2B6640`; Color Guide Mid Green is `#2B6636`. Prefer **`#2B6636`** from the Color Guide.

### Radiology icon color rules (POTX slide 4 — Color)

- Illustrative elements primarily in **Radiology Dark Blue** (`#10384F`).
- A **product-specific primary color** is used as outline/fill accent (default overview accent = **MEDRAD® orange** `#E46C0A` from Devices and Accessories / SVG strokes).
- Recolor only the product-accent shapes in PPT; **do not** recolor shapes/outlines set in Radiology Dark Blue.

---

## Typography

- Color Guide PDF: **no dedicated typeface specification** extracted.
- PPTX + POTX theme `fontScheme` name **Arial**: major/minor Latin **Arial**, East Asian **Arial Unicode MS**, complex script **Arial**.
- Corporate presentation tone implies clean sans-serif UI; product wordmarks (e.g. stylized “medrad”) appear as logo art, not as body fonts.
- Icon font reference in some SVGs: `BayerSymbolsIconsPositive` (symbol glyphs for Quality “S” marks, etc.).

---

## Contrast, backgrounds, presentation tone

- Prefer **Dark Blue (`#10384F`) text on white**, or **white/light text on dark blue/dark green/dark purple** backgrounds.
- Bright hues (`#00BCFF`, `#89D329`, `#FF3162`) for accents, callouts, small fills — not large body text blocks.
- Mid hues for secondary structure / supporting shapes.
- Tone: **professional consulting / life-science corporate** — structured charts, clear hierarchy, selective icon support, English placeholder labels like “Subtitle – Unit”, “Headline”, “Text / Level 1 / Level 2”.
- Radiology decks: clinical, product-accented (orange/blue/green product colors) on Dark Blue line icons.

---

## Gaps / unknowns

- Official Bayer display/body fonts beyond Arial theme fallback: **not stated** in these three files (refer to full Bayer Brand Guideline / Veeva Content Factory as noted on POTX slide 3).
- Chinese localization rules: **not present**.
- Exact opacity policy vs “100% block color” nuance: follow Color Guide overview + proofing swatch pages.
