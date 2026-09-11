# Bayer Official Template — Chart Pool Catalog

**Source file:** `source/official-template.pptx`  
**Stated identity (title slides):** **Bayer Chart pool** / **/// Bayer 16:9 Template Chart Pool /// August 2019**  
**Cover mark:** “Updated version”  
**Date on deck:** August 2019  
**Author metadata (file props):** Xiaolei Zhu (file timestamps reflect local copy, not original publish date)  
**Division / product:** Corporate **Chart Pool** (not Radiology-specific; includes **Crop Science** icon chapter and general Medical & Pharma icons). Closing guidance references Bayer classification labeling (Identity Net).

**Slide count (this file):** **330**  
**Dimensions:** `12190413 × 6858000` EMU ≈ **13.33" × 7.5"** (widescreen **16:9**) — same as BC Chart Library / Radiology POTX.

**Theme OOXML names:**
- `PR_BAG_PPT-master_16-9` (theme1)
- `PR_BG_Chart-Pool_16-9_2019-08-27` (theme2) — Chart Pool build stamp **2019-08-27**
- theme3 / theme4: “Office Theme” shells still carrying **Bayer 2017** scheme

**Important TOC caveat:** Agenda slides 3–4 list **original Chart Pool slide numbers** (up to ~438: Flags, Flags on pin, etc.). **Those numbers do not match this file’s 1-based indices.** This digest catalogs **what is actually present** in the 330-slide “Updated version” copy.

---

## Masters / layouts

**2 slide masters**, **69 layout XML parts** (python-pptx reports 22 + 47 layouts across masters; many are duplicates / language variants).

### Master A — core corporate layouts (22)

| # | Layout name | Typical placeholders |
|---|-------------|----------------------|
| 0 | Title Slide | ctrTitle, subTitle, body, dt, ftr, sldNum |
| 1 | 1_Title slide 2 | same family |
| 2 | 1_Title slide 3 | same family |
| 3 | Agenda | title, body, dt, ftr, sldNum |
| 4 | Chapter | title, subTitle, dt, ftr, sldNum |
| 5 | Chapter 2 | title, subTitle, … |
| 6 | Chapter 3 | title, subTitle, … |
| 7 | Content | title, subTitle, body/content |
| 8 | Content (2) | dual content |
| 9 | Text (2) & Images (2) | title, subTitle, 2× body + images |
| 10 | Title only (color) | title, subTitle — **dominant slide layout in this file** |
| 11 | Quote | title, subTitle |
| 12 | Image | pic + chrome |
| 13–15 | Final Slide / Final Slide 2 / Final Slide 3 | closing variants |
| 16 | Titelfolie | German title-slide alias |
| 17–19 | Title slide 3 / Title slide 2 / Title slide (3) | title variants |
| 20 | Text (4) | four body columns |
| 21 | Title slide 3 (3) | extended title |

### Master B — extended photo / bilingual set (47)

Adds / duplicates above plus:
- **内容** (Chinese “Content”)
- Title slide 2/3 variants `(2)` / `(3)`
- **Image color**, **Image color 2–4**
- **Text & Image**, **Text & Image 2–6**
- **Text & Image small** / **small 3–5**
- **Image & Text**
- **Text & Image transparent** / **transparent 2–4**
- **Image (4)** / **Image 2 (4)** / **Image 3 (4)**

### Layout usage in this 330-slide file

| Layout | Count | Example slides |
|--------|------:|----------------|
| Title only (color) | 321 | Most chart / diagram / icon pages |
| Agenda | 4 | 3–6 |
| Content | 2 | 7, 330 |
| Title slide (3) | 1 | 1 |
| Title slide 3 (3) | 1 | 2 |
| Text (4) | 1 | 8 |

Most **photo / Quote / Final / Chapter** layouts exist on the master for authoring but are **not used** by the stock chart-pool pages in this copy.

**Master chrome (both masters):** German placeholder ladder (*Textmasterformat bearbeiten* / *Zweite…Fünfte Ebene*), footer `/// Bayer 16:9 Template Chart Pool /// August 2019`, date + slide number.

---

## Chapter / TOC structure

### Agenda as printed (original pool indices — reference only)

**Agenda A (slide 3):** Pictures for Placeholders (4) · Chapter & Agenda Samples (34) · Layouts (39) · Diagrams (77) · Tables (89) · Organigrams (94) · Butterfly diagrams (108) · Venn diagrams (116) · Pyramid charts (124) · Text boxes (134) · Picture charts (138) · Processes (145) · Project Management Toolbox (157)

**Agenda B (slide 4):** Circular shapes (206) · Timelines (233) · Maps & globes (241) · Flags (262) · Flags on pin (283) · Icons (304) · Silhouettes (348) · Puzzle, Cubes and Gear wheels (349) · Post-it / Sticky notes / Hand drawn shapes (353) · Timer (355) · 3D characters (356) · Logos, Colors and Gradients (435) · Contact & Secret content (438)

### Actual content map in *this* file (1-based)

| Range | Section | Notes vs original TOC |
|------:|---------|------------------------|
| 1–2 | Title / Welcome | “Bayer Chart pool”, “Updated version”, Welcome Statement |
| 3–4 | Agenda | Lists original indices |
| 5–6 | Agenda – two columns | Sample agendas (placeholders / Morning–Afternoon) |
| 7–9 | Content / Text (4) / Title-only text | Body text demos |
| 10–21 | Native charts | Column, stacked column, bar+text, waterfall, pie, doughnut, line, spider |
| 22–26 | Tables | Table + textbox / key-fact table hybrids |
| 27–40 | Organigrams / spheres | Org charts, **Spheres tree**, **Connected spheres** |
| 41–48 | Butterfly diagrams | 2+2 … 6+6 and asymmetric 2+3, 3+5, 4+3 |
| 49–56 | Venn diagrams | 2–6 circles + intersection |
| 57–65 | Pyramid charts + toolbox | 3–6 layers + Pyramid toolbox 1–5 |
| 66–70 | Text boxes | Three/two/four blocks, header boxes vertical |
| 71–77 | Picture / photo usage | “Usage of photographs and images on a slide” |
| 78–94 | Processes | Factor results, N-steps, triangle process, options, road to success, status quo |
| 95–138 | Project Management Toolbox | Key facts/achievements, SWOT, scope in/out, status, matrices, PLC, barriers… |
| 139–165 | Circular shapes | Templates 3–6 pieces, toolkits, design samples, arrow variants |
| 166–173 | Timelines | Project timelines, arrows, trend chart |
| 174–194 | Maps & globes | World / regions / Germany / continents / globes (**Flags / Flags-on-pin sections absent**) |
| 195–198 | Computer network icons | Devices + traffic-light / trend UI chrome |
| 199–200 | Nature energy icons | |
| 201–216 | Business icons | General 1–6, Devices, Data tools, Charts/Lists, People, Communication, Finance, Timeline |
| 217–221 | Science icons | R&D, Microorganisms, General 1–3 |
| 222–230 | Medical & Pharma / Organs / Animals / Cancer & Gyn | |
| 231–236 | Crop Science icons | Farming, Crops/Seeds/Food, Plants, Sci/Tech, Environment, R&D |
| 237–238 | Logistic Icons · Circles/Arrows/LIFE/SWOT/Bars | Decorative tracker toolkit |
| 239–243 | Silhouettes · Puzzle · Cubes · Gears | |
| 244–245 | Post-it / Sticky notes · Hand drawn shapes | |
| 246 | Timer – animated | 3–20 minutes + “Time over” |
| 247–325 | **3D characters** | ~79 slides of photographic 3D people/props |
| 326–328 | Bayer Logos · Color · Gradient | Color slide lists all **12** brand hues by name |
| 329 | Contact | NAME / Position / Phone / Fax / e-mail |
| 330 | Information classification labeling | Points to Bayer Identity Net classification ribbon |

**Missing vs agenda (not in this Updated copy):** Pictures for Placeholders chapter, Chapter & Agenda Samples, full Layouts gallery as stock slides, **Flags**, **Flags on pin**, and other original pages beyond ~438.

---

## Layout catalog (corporate authoring)

| Family | Master layouts | Used in stock slides? |
|--------|----------------|------------------------|
| Title | Title Slide, Title slide 2/3/(3), Titelfolie, 1_Title slide * | Yes (1–2) |
| Agenda / TOC | Agenda | Yes (3–6) |
| Section / Chapter | Chapter, Chapter 2, Chapter 3 | Available, unused here |
| Content / multi-column text | Content, Content (2), 内容, Text (4), Text (2) & Images (2) | Partially (7–9) |
| Title-only working canvas | Title only (color) | Yes (vast majority) |
| Quote | Quote | Available |
| Photo / image | Image, Image color 1–4, Image (4) family, Text & Image *, transparent variants | Mostly via Title-only photo demos 71–77 |
| Closing | Final Slide 1–3 | Available |
| Contact / compliance | (Content on 329–330) | Yes |

---

## Diagram / chart / structure patterns

### Native Excel charts (slides 10–21)

Column · Stacked column · Bar + text · Waterfall + text · Bar · Pie · Doughnut · Line · Line + text · Spider/radar.

### New or strongly expanded vs BC Chart Library (Sep 2018)

| Family | Slides | Anatomy | AntV mapping | Overlap note |
|--------|--------|---------|--------------|--------------|
| **Butterfly diagrams** | 41–48 | Left/right mirrored option stacks (2+2…6+6; asymmetric) | `compare-binary-horizontal` / `list-column-vertical` ×2 | **New family** vs BC |
| **Spheres tree / Connected spheres** | 32–40 | Hierarchical / networked spheres | `hierarchy-tree-basic` / `relation-network` | Related to BC hierarchy; distinct visual |
| **Circular shapes toolkits** | 139–165 | Segmented rings 3–6+, arrow cycles, design samples | `relation-circle` / `sequence-cycle` / `chart-pie` | Far larger toolkit than BC cycles |
| **Triangle / divided triangle process** | 85–86 | Layered triangle process | `hierarchy-pyramid` / `sequence-steps` | Related to BC pyramid/process |
| **Road to success / Status quo → Concept** | 93–94 | Path + conclusion callout | `sequence-roadmap` | Narrative process variant |
| **Temple / Imbalance / Controversy** | 112–114 | Structural metaphors | `hierarchy-*` / `compare-vs` | Overlaps BC “Controversy / tension” |
| **Splitter / filter · Resistance / barrier** | 137–138 | Funnel/filter metaphors | `sequence-funnel` | Overlaps BC funnel/barrier |
| **Post-it / Hand-drawn / Timer** | 244–246 | Workshop facilitation UI | `list-grid-card` | Overlaps BC post-it; **Timer animated** is new |
| **Puzzle / Cubes / Gears** | 240–243 | 3D-ish metaphor objects | — (decorative) | Present in both libraries; keep as accent only |
| **3D characters** | 247–325 | Photographic staged characters | — | **Major new asset class**; use sparingly vs outline icon language |
| **Classification labeling** | 330 | Security ribbon instruction | — | Process/compliance, not a chart |
| **Gradient showcase** | 328 | Brand gradient strip | — | Visual reference only |

### Overlaps with BC Chart Library (cross-link — do not re-digest)

Prefer **BC Chart Library** (`STRUCTURE_PATTERNS.md` §A–I) for consulting frameworks (BCG, Porter, ADKAR, RACI, Ansoff, swimlane, stakeholder…). This Chart Pool still includes practical twins:

| Pattern here | Slides | BC counterpart |
|--------------|--------|----------------|
| Org charts | 27–31 | Project organization / org chart |
| Venn 2–6 | 49–56 | BC cycles/overlap structures |
| Pyramid 3–6 + toolbox | 57–65 | BC pyramid |
| Process N-steps / options | 80–91 | BC process / alternatives |
| SWOT / Chances–Risks / Pros–cons | 97–101 | BC SWOT / pros–cons |
| In-scope vs out-of-scope | 104 | BC What’s in / What’s out |
| Status report / next steps | 107–108 | BC status / next steps |
| Decision / 2×2 / 3×3 matrices | 122–131 | BC decision matrix / BCG-like |
| Product life cycle | 132–133 | BC PLC |
| Project timelines | 166–172 | BC Gantt-like timelines |
| Maps & globes | 174–194 | BC Maps chapter (Flags missing here) |
| Icon catalogs | 195–238 | BC Ch.4 Icons (different cut + Crop Science) |

---

## Icon / element assets

### Style

- Catalog icons are primarily **native grouped shapes** (≈**973** top-level groups on slides 195–239), **not** embedded SVG media.
- Color language follows **Bayer 2017** / Dark Blue–led fills and outlines (see Color slide 327).
- Separate element classes: **silhouettes**, **puzzle/cubes/gears**, **post-it PNGs**, **hand-drawn strokes**, **animated timer**, **3D character JPEGs**, **map PNGs**, small **EMF/WMF** logo marks, classification **WMF**.

### Categories (slides 195–238)

| Category | Slides | Notes |
|----------|--------|-------|
| Computer network | 195–198 | Monitor, laptop, server, lock, email, traffic light, trend icons |
| Nature & energy | 199–200 | |
| Business — General | 201–206 | 6 pages |
| Business — Devices / Data tools / Charts & Lists | 207–211 | |
| Business — People / Communication / Finance / Timeline | 212–216 | |
| Science — R&D / Microorganisms / General | 217–221 | |
| Medical & Pharma | 222–226 | Incl. chemistry fragments |
| Organs | 227–228 | |
| Animals | 229 | |
| Cancer & Gynecological Diseases | 230 | Named disease labels |
| Crop Science | 231–236 | Farming, crops/seeds/food, plants, tech, weather, R&D |
| Logistic Icons | 237 | |
| Circles / Arrows / LIFE / SWOT / Bars / Tracker | 238 | Decorative toolkit |

### Extracted media → `icons/official/`

| Subfolder | Contents |
|-----------|----------|
| `maps/` | World / regional map PNG bases |
| `3d_sample/` | Representative 3D character JPEGs |
| `postit/` | Sticky-note PNGs |
| `media_png_vector/` | All embedded PNG + EMF/WMF from the PPTX |
| `photo_usage/`, `org_pics/`, `logos_colors/` | Sparse exemplars |
| `MANIFEST.json` | Extraction index |

**No SVGs** in this PPTX. For outline SVG language, continue using Radiology POTX extracts under `icons/` (root), not `icons/official/`.

---

## Theme colors / fonts

### Scheme: **Bayer 2017** (same bridge as Chart Library / Radiology)

| Slot | HEX |
|------|-----|
| dk1 | `#000000` |
| lt1 | `#FFFFFF` |
| dk2 | `#FF3162` |
| lt2 | `#624963` |
| accent1–6 | `#10384F`, `#00BCFF`, `#004422`, `#89D329`, `#443247`, `#D30F4B` |
| hlink / folHlink | `#00BCFF` / `#89D329` |

### custClrLst (theme1/theme2)

| Name | HEX | vs Color Guide |
|------|-----|----------------|
| BrightBlue … DarkBlue (4) | `#00BCFF` `#0091DF` `#00617F` `#10384F` | Match |
| BrightGreen … DarkGreen (4) | `#89D329` `#66B512` **`#2B6636`** `#004422` | **MidGreen matches Color Guide** (unlike BC Chart Library custClr `#2B6640`) |
| Fuchsia / Raspberry / MidPurple / DarkPurple | `#FF3162` `#D30F4B` `#624963` `#443247` | Match |
| TrafficLight Red/Yellow/Green | `#CC0000` `#FFCC00` `#66B512` | Status only |

**Precedence:** Color Guide remains authoritative for the 12 brand hues; this template’s custClr does **not** invent new brand hues. Traffic lights are semantic extras (also seen in Radiology theme).

### Fonts

- fontScheme **Arial**: major/minor latin **Arial**, ea **Arial Unicode MS**, cs **Arial**
- No new corporate display font in this file
- Master body copy includes German UI strings (authoring locale remnant)

### Color slide (327)

Explicitly names all 12: Bayer Fuchsia, Raspberry, Mid/Dark Purple, Bright/Green/Mid/Dark Green, Bright/Blue/Mid/Dark Blue.

---

## Reusable placeholders / guides / content areas

- Footer lockup: `/// Bayer 16:9 Template Chart Pool /// August 2019` + slide number + date
- Common title stack: **Subheadline** + **Headline** (Title only color)
- Chart pages: **Source** caption
- Agenda two-column: nested Placeholder 1 / 1.1 / … or Morning/Afternoon
- Contact fields: NAME, Position, Phone, Fax, e-mail (`Your.name@bayer.com`)
- Classification: use Bayer PowerPoint **CLASSIFICATION RIBBON**; docs at Identity Net (`https://idnet.bayer.com/en/security-labeling.aspx` as printed on slide 330)
- Photo guidance slides (71–77): how to place photography with text
- Circular / pyramid **toolkits**: parts libraries for assembling custom diagrams

---

## Comparison summary vs prior kit assets

| Topic | Official Chart Pool (this file) | BC Chart Library | Radiology POTX |
|-------|---------------------------------|------------------|----------------|
| Role | Corporate 16:9 chart/element pool | Consulting frameworks + charts | Illustrative icon language |
| Date stamp | Aug 2019 / theme 2019-08-27 | Sep 2018 | Sep 2020 |
| Slides | 330 (subset of larger pool) | 271 | Template + icon pages |
| Best for | Butterflies, circular toolkits, maps, crop/medical icon grids, 3D people, corporate layouts | BCG/Porter/ADKAR/RACI/etc. | SVG outline icons + product accents |
| MidGreen custClr | `#2B6636` (= Guide) | `#2B6640` (drift) | Guide-aligned via Bayer 2017 |
