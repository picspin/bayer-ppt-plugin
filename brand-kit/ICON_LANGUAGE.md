# Bayer Icon Language

**Primary source:** `source/icon-language.potx` — *Bayer in Radiology Icon Library* (September 2020), “For Use in PowerPoint and Beyond”.  
**Secondary:** BC Chart Library PPTX Chapter 4 (*How to use icons*, slides 198–239) — broader Business Consulting icon categories.

Slide size (POTX): same as chart library — `12190413 × 6858000` EMU (16:9).  
Theme: **Radiology** / clrScheme **Bayer 2017**; theme family id references `ALL.AA.Illustrative_Elements.Icon_Library_Overview`.

---

## How icons are styled

### Color (POTX slide 4 — Color)

- **Primary stroke/fill:** Radiology **Dark Blue** `#10384F`.
- **Accent:** product-specific primary color as outline or fill for emphasis. Default overview accent = **MEDRAD® orange** `#E46C0A` (theme: Devices and Accessories). Other product accents seen in extracted SVGs: Radimetrics `#2C5697`, Equipment Service green `#6BC200`.
- **Recolor rule:** in PPT, recolor only the product-accent portion (Shape Fill / Shape Outline). **Do not** recolor any shape or outline set in Bayer Radiology Dark Blue.

### Line / fill geometry (from extracted SVG media)

- Artboard typically **`viewBox="0 0 256 256"`**.
- Dominant style: **outline / line icons** with `fill="none"`, `stroke="#10384F"`, **`stroke-width="8"`**, `stroke-linecap="round"`, `stroke-linejoin="round"`.
- Some icons are **filled** Dark Blue (e.g. organ silhouettes, denser device glyphs) or **outline+fill** hybrids.
- Accent strokes/fills use product orange (or other product HEX) on selected paths only.
- Occasional symbol font glyphs: `font-family="BayerSymbolsIconsPositive"` (e.g. Quality “S” marks in communication-pillar variants).

### BC Chart Library guiding principles (PPTX slide 198)

1. Use icons as a **supporting element, not a replacement** (for key messages).
2. Strive for **selective and purposeful** use.
3. Ensure **stylistic consistency and uniformity** of icons.

### File formats (POTX slide 3)

Official library distributes **EPS (CMYK)**, **SVG (RGB)**, **PNG (RGB)** plus Illustrator master files (RGB/CMYK) via Veeva Content Factory. Full layout/spec rules point to *Bayer in Radiology Brand Guideline* on Veeva (not included in this digest).

---

## Categories present

### A. Radiology Icon Library (POTX TOC — slide 2)

| Category | POTX slides (approx.) | Example labels |
|----------|----------------------|----------------|
| Communication Pillars (all product colors) | 6–11 | Confidence, Efficiency, Innovation, Partnership, Quality, Science |
| Communication Funnel | 12 | Awareness → Interest/Preference → Consideration → Conversion/Trial → Advocacy/Loyalty |
| Target Groups | 13 | Radiologist, Administrator, Technician, Hygiene Department, OEM |
| Patients | 14 | Adult Patient, Child Patient, Person |
| Sales | 15 | Sales Force, Face to Face, Sales Representative |
| Indications | 16 | Heart, Kidneys, Liver, Lungs, Brain, Breast |
| Contrast Media Research | 17 | Certificates, Clinic Study, Compliant, Guideline, Hydration, Lab, Safety, … |
| Workflow | 18 | Prepare/Bottle, Plan, Manage, Report, Bill, Perform, QR Code, Documentation, … |
| Product Benefits | 19 | Cost Saving, Set Up, Speed, Time Saving |
| Workstations and Scanners | 20 | Protocols, PACS Interface, Scanner Connectivity, Workstation, Barcode Scanner |
| Features | 21 | Touchscreen, Plug, Settings, Speech Interface, Wireless, Battery Powered, … |
| Injectors and Disposables | 22 | Syringe, Stellant, Flex, Centargo, Day Set, Multi-Patient, Smart Injector, … |
| Product hardware views | 23–26 | Centargo / Stellant / SSEP / MRXperion — Close Up, Front, Side, In Use |
| IMCM Assets | 27 | Apps, Digital Banner, eDetailer, Newsletter, Social Media, Webinar, Website, … |
| Brand Planning | 28 | Analytics, Insight, Content Factory, Data, Research, Reporting, Strength |
| Services | 29 | Congress, Tech Assistance, Virtual Care, Chat, Direct Care, Maintenance, Upgrade |
| Objects | 30 | Clock, Magnifying Glass, Phone, Hourglass, Hospital |
| Training & Education | 31 | Training, Doctor, Certificate |
| Contact | 32 | Escalation for new icons (email contact on slide) |

Product-colored pillar sets: Ultravist®, Gadovist®, Primovist®, Radimetrics®, Service Green, MEDRAD®.

### B. BC Chart Library icon topics (PPTX Ch. 4)

Business (Documents and data, People, Finance, Signs and Figures, IT, Business Basics) · Nature and Energy · Medical · Leisure (Food, Nature and Animals, Sports, Travel) · Visuals (Manufacturing equipment, Production facilities, Smart factory, Analytics screens, Customer Interaction Channels, Silhouettes).

---

## How icons combine with shapes/text

- Catalog slides: icon grid + **category title** + short English labels under/ beside each glyph.
- Communication pillars: icon + single-word concept (Confidence, Efficiency, …) often with product accent.
- Workflow / features: icon as node in process or feature lists.
- Chart Library: icons sit inside **Elements** tiles, process nodes, or as decorative support beside Level 1/2 text — never replacing the message (per slide 198).
- Product logos (MEDRAD Centargo/Stellant lockups, etc.) appear as separate PNG/WMF media on master layouts, distinct from line icons.

---

## Extracted media inventory

All files originally extracted under local install `icons/` (example: Grok Bot `/home/box/tools/bayer-ppt/icons/`) (**71 files**: 45 PNG, 23 SVG, 2 WMF, 1 EMF).

### SVG icons (line language — preferred for style reference)

| File | Inferred meaning (from active SVG group / slide context) | Style | Accent |
|------|----------------------------------------------------------|-------|--------|
| `image46.svg` | Efficiency (pillar example, slide 3) | Outline SW 8 | Dark Blue + orange arcs |
| `image47.svg` | Confidence | Outline | Dark Blue only |
| `image48.svg` | Innovation | Outline | Dark Blue + orange |
| `image51.svg` | Efficiency (Radimetrics accent set, slide 9) | Outline | `#2C5697` accent |
| `image52.svg` | Quality (Radimetrics + BayerSymbols “S”) | Outline + symbol | `#2C5697` |
| `image53.svg` | Science (Radimetrics) | Outline | `#2C5697` |
| `image54.svg` | Quality (Service Green set, slide 10) | Outline + symbol | `#6BC200` |
| `image55.svg` | Science (Service Green) | Outline | `#6BC200` |
| `image56.svg` | Heart (Indications, slide 16) | Outline | Dark Blue |
| `image57.svg` | Heart (alt) | Outline+fill | Dark Blue |
| `image58.svg` | Lungs | Outline | Dark Blue |
| `image59.svg` | Liver | Outline | Dark Blue |
| `image60.svg` | Kidneys | Outline | Dark Blue |
| `image61.svg` | Person / patient | Outline | Dark Blue |
| `image62.svg` | Brain | Filled | Dark Blue |
| `image63.svg` | Feature / speech-interface cluster (slide 21) | Filled | Dark Blue + orange |
| `image64.svg` | Injector / disposable related (slide 22) | Filled | Dark Blue + orange |
| `image65.svg`–`image68.svg` | SSEP Injector views (slide 25) | Mixed outline/fill | Dark Blue + orange |
| `image69.svg` | Magnifying glass (Objects, slide 30) | Outline | Dark Blue |
| `image70.svg` | Personalized Protocols / object (slide 30) | Outline | Dark Blue + orange |

### PNG / WMF / EMF (mostly logos, UI chrome, layout art)

| Files | Role |
|-------|------|
| `image1.png`, `image8.png`, `image11.png`, `image14.png`, `image17.png` | Small Bayer/cross marks (~100×155) on layouts |
| `image3.png`, `image4.png`, `image7.png`, `image9–15.png`, etc. | Wordmarks / banners for Radiology & product title layouts |
| `image16.png`, `image18–30.png` | Product lockups (e.g. MEDRAD Centargo, Stellant CT Injection System) |
| `image31–45.png` | Additional product/service logos for master layouts |
| `image49.png`, `image50.png` | PPT UI screenshots illustrating Shape Fill recolor steps (green vs orange indicator) |
| `image5.wmf`, `image6.wmf` | Vector logo marks on layouts |
| `image71.emf` | Contact/end slide graphic (slide 32) |

Many PNGs are **layout chrome/logos**, not the line-icon system. For Bayer-ppt generation, prefer **SVG outline language** (`#10384F`, SW≈8 on 256 canvas) + optional product accent.

---

## Mapping notes: ppt-master Tabler / Phosphor → Bayer style

| Bayer trait | Tabler / Phosphor default | Skill constraint |
|-------------|---------------------------|------------------|
| Stroke ~8 on 256 viewBox (≈ **3%** of canvas) | Often 1.5–2px on 24 viewBox | Scale stroke to ~**2px on 24** or use **bold/outline** variants; avoid ultra-thin hairlines |
| Round caps/joins | Tabler: round; Phosphor regular: similar | Prefer **outline / regular**, not duotone/fill unless matching filled Bayer organs/devices |
| Monochrome Dark Blue `#10384F` | Usually currentColor/black | Force color `#10384F`; optional second color only for product accent |
| Dual-color accents | Limited in Tabler | Compose: base icon Dark Blue + small accent shape in product HEX, **or** use Phosphor duotone sparingly with Dark Blue + `#E46C0A` |
| Clinical radiology metaphors | Generic business set | Map: heart→`heart`, lungs→`lungs`, brain→`brain`, syringe→`syringe`, shield→`shield-check`, workflow→`//flow`/`route`, users→`user`/`users` |
| BC business icons | Strong Tabler coverage | documents, users, chart, currency, cloud, leaf/energy — keep uniform outline weight |
| Do not | Mixed fill weights, colored gradients, 3D, emoji | Reject decorative icon styles that break uniformity (BC principle 3) |

**Practical rule for Bayer-ppt:** default icon pack = **outline**, color `#10384F`, one accent color max per slide (from Bayer bright/core or product custClr), icons support text — never replace headlines.

---

## Official Template (2019 Chart Pool) — icon / element language

**Source:** `source/official-template.pptx` (*Bayer 16:9 Template Chart Pool*, August 2019).  
**Extracted assets:** `icons/official/` (do **not** overwrite Radiology SVGs in `icons/` root).  
**Detail catalog:** [`OFFICIAL_TEMPLATE.md`](OFFICIAL_TEMPLATE.md).

### How these icons differ from Radiology POTX

| Trait | Radiology POTX | Official Chart Pool |
|-------|----------------|---------------------|
| Media | Embedded **SVG** (+ PNG logos) | Mostly **grouped native shapes**; JPEG 3D characters; map/post-it PNG; few EMF/WMF |
| Stroke system | viewBox 256, SW≈8, Dark Blue outline | Shape fills/outlines in Bayer 2017 palette (not a single SVG stroke spec) |
| Accent | Product accents (e.g. MEDRAD orange) | Corporate multi-hue; traffic-light / trend chrome on IT slides |
| Domain | Radiology / contrast / injectors | Business, science, medical/pharma, **Crop Science**, logistics |

### Categories (slides 195–238 in this file)

Computer network (devices, locks, email, traffic light, trend) · Nature & energy · Business General (6) · Devices · Data tools · Charts and Lists · People · Communication · Finance · Timeline · Science R&D / Microorganisms / General · Medical & Pharma · Organs · Animals · Cancer & Gynecological Diseases · **Crop Science** (Farming/Insects/People, Crops/Seeds/Food, Plants, Science/Technology/Structures/Transportation, Environment/Weather, R&D) · Logistic Icons · Circles/Arrows/LIFE/SWOT/Bars/Tracker.

**Approx. density:** ~973 top-level groups on icon catalog slides 195–239 (many multi-glyph groups).

### Other element languages in the same file

- **Silhouettes** (239), **Puzzle / Cubes / Gears** (240–243) — decorative metaphors  
- **Post-it / Sticky notes** + **Hand drawn shapes** (244–245) — workshop markup  
- **Timer – animated** (246) — facilitation chrome  
- **3D characters** (247–325) — photographic; optional only; **do not** treat as the default Bayer icon system  
- **Maps** PNG bases under `icons/official/maps/`  
- **Bayer Logos / Color / Gradient** (326–328)

### Extracted paths

```
icons/official/
  maps/           # world & regional map bases
  3d_sample/      # sample 3D character JPEGs
  postit/         # sticky-note PNGs
  media_png_vector/  # all PNG + EMF/WMF from OOXML media
  photo_usage/ org_pics/ logos_colors/
  MANIFEST.json
```

### Skill guidance

1. Default generated icons → still **Radiology-style outline** (`#10384F`, SW≈8/256) or Tabler/Phosphor mapped per table above.  
2. When the user asks for **Crop Science / general business / network / disease** metaphors present only in Chart Pool, approximate with outline icons in the same Dark Blue language (do not paste random 3D JPEGs into executive decks unless requested).  
3. Traffic-light and trend icons = **status semantics only**.  
4. Prefer `icons/official/maps/` as geographic bases when building map slides from this kit.
