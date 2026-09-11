# Bayer-ppt Skill Digest / 执行摘要

## What these assets collectively define

| Asset | Role | Defines |
|-------|------|---------|
| **Color Guide PDF** (*Bayer Color Guide*, Bayer AG Communications & Public Affairs, 2018) | Corporate color system | 12 named hues + white across blue / green / purple families (bright→dark); Pantone / RAL / RGB / HEX / CMYK; opacity & usage rules; body text = Dark Blue |
| **Structured graphics PPTX** (*BC Chart Library*, Business Consulting, Sep 2018) | Consulting slide structure & chart taxonomy | 271 widescreen 16:9 templates: project mgmt, structural diagrams, textbook frameworks, icon catalogs, maps/flags; master layouts; Arial + Bayer 2017 theme |
| **Official Template PPTX** (*Bayer 16:9 Template Chart Pool*, Aug 2019, “Updated version”) | Corporate chart pool + layout masters | 330 slides in this copy (agenda cites larger original ~438): native charts, butterflies, circular toolkits, PM toolbox, maps/globes, business/science/medical/**Crop Science** icon grids, silhouettes/puzzle/cubes, post-it/timer, **3D characters**, logos/color/gradient, contact + **classification labeling**; rich photo Text & Image masters |
| **Icon expression POTX** (*Bayer in Radiology Icon Library*, Sep 2020) | Illustrative SVG icon language | Dark Blue outline icons (SW≈8 / 256), product accent recolor rules, radiology/clinical category taxonomy, product layout masters |

Together they specify a **Bayer corporate presentation system**: Color Guide for palette truth, Chart Pool for *corporate layouts & diagram chrome*, Chart Library for *consulting frameworks*, Radiology Icon Library for *how supporting outline icons look* (especially pharma/radiology). Theme scheme **Bayer 2017** bridges PPTX/POTX/Chart Pool.

**English terms (as found):** Bayer Dark Blue, Bright Blue, Mid Blue; Bayer Green / Bright Green; Fuchsia, Raspberry, Mid/Dark Purple; Chart Library; Chart Pool; Butterfly diagram; Circular shapes; Project Management Toolbox; Crop Science; Classification Ribbon; Confidence / Efficiency / Innovation / Partnership / Quality / Science; Radiology Dark Blue; MEDRAD® orange accent.

**Chinese terms:** Layout name **内容** appears on Official Template master 2; no Chinese body copy in the digested slides. BC/Radiology assets: none. A Bayer-ppt skill serving CN audiences must supply its own bilingual glossary without claiming it came from these assets (except noting the `内容` layout alias).

---

## Precedence rules (skill)

1. **Brand hues (12 + white):** Color Guide HEX wins always. Do not invent colors. Official Chart Pool custClr MidGreen `#2B6636` **matches** the Guide; BC Chart Library MidGreen custClr `#2B6640` **drifted** — ignore the drift.
2. **Corporate layouts / photo+text masters / butterflies / circular toolkits / 3D people / classification:** Official Template (Chart Pool).
3. **Consulting frameworks** (BCG, Porter, ADKAR, RACI, Ansoff, swimlane, stakeholder, SCS…): BC Chart Library.
4. **Outline SVG icon language + radiology product accents:** Radiology POTX (`icons/` root). Chart Pool icons live as grouped shapes + `icons/official/` rasters — approximate with outline icons unless the user wants Pool-specific art.
5. **Traffic lights / trend icons:** status semantics only (documented in Chart Pool + Radiology themes), not decorative brand colors.
6. **Fonts:** Arial (+ Arial Unicode MS for EA) until an official Bayer webfont/package is supplied.

---

## Gaps (updated)

1. **Typography:** Still no Bayer proprietary type ramp; Arial only across all four assets.
2. **Chinese / localization:** Only a layout alias `内容` + German master placeholders in Chart Pool; no bilingual content system.
3. **Icon completeness:** Radiology POTX = sample SVG set (full library on Veeva). Chart Pool icons are native groups (not SVG). BC Chapter 4 icons mostly embedded in slides.
4. **Mid Green mismatch:** Only BC Chart Library drifted (`#2B6640`); Guide + Official Template = `#2B6636`.
5. **Division colors:** Color Guide forbids mapping palette to divisions; Radiology product accents remain *product* colors; Crop Science in Chart Pool is an **icon chapter**, not a division palette.
6. **Motion / photography / logo clearspace:** Chart Pool adds photo-usage slides + 3D characters + Identity Net classification URL; full clearspace/logo rules still incomplete vs a full brand book.
7. **Official Template completeness:** This file is an **Updated** subset — agenda references Flags / Flags-on-pin / Pictures for Placeholders / full Layouts gallery that are **missing** here. Do not assume agenda indices == file indices.
8. **AntV / ppt-master:** Mappings remain skill recommendations (see `STRUCTURE_PATTERNS.md` / `THEME.json`).

---

## How a Bayer-ppt skill should constrain ppt-master + infographic-creator

### Hard constraints

1. **Palette:** Only HEX from Color Guide 12 + white (+ black for theme compatibility). Optional Radiology `custClr` accents only when the user asks for Radiology/product decks. Traffic lights only for status.
2. **Primary text:** `#10384F` on `#FFFFFF` by default; reverse on dark blue/green/purple grounds.
3. **Slide size:** 12190413 × 6858000 EMU (16:9).
4. **Fonts:** Arial (until official Bayer fonts are provided).
5. **Icons:** Outline style, Dark Blue; do not recolor Dark Blue strokes; max one accent color; icons support, don’t replace, titles (BC principles). Do not default to Chart Pool 3D JPEGs.
6. **No invented brand colors.**

### Soft / structural constraints

1. Prefer Chart Library **framework** families and Chart Pool **corporate diagram** families when choosing layouts: process → `sequence-*`; butterfly/matrix/SWOT → `compare-*` / `chart-quadrant`; org/pyramid/spheres → `hierarchy-*`; circular/cycles → `relation-*` / `sequence-cycle`; cards/summary → `list-*`.
2. Prefer Official Template master names for corporate decks (`Title only (color)`, `Agenda`, `Content`, `Text & Image`, `Final Slide`…).
3. Infographic-creator `antv_theme.palette` should follow `THEME.json` order (Dark Blue first).
4. For Radiology content: allow MEDRAD orange `#E46C0A` (or named product accent) on icon accents only.
5. For Crop Science / general business icon needs from Chart Pool: keep outline Dark Blue language.
6. Classification: when producing internal Bayer decks, remind use of the classification ribbon (Identity Net) if appropriate — do not invent classification marks.

### Suggested skill I/O

- Read `THEME.json` + `BRAND.md` for color/font.
- Read `STRUCTURE_PATTERNS.md` (BC + **Official Template (2019)** section) to pick pattern → AntV template.
- Read `OFFICIAL_TEMPLATE.md` for Chart Pool layout/diagram inventory.
- Read `ICON_LANGUAGE.md` when placing icons; Radiology SVGs in `icons/`, Chart Pool rasters in `icons/official/`.
- Keep `source/` originals for human reference.

---

## Deliverable index

| Path | Contents |
|------|----------|
| `source/structured-graphics.pptx` | Copied BC Chart Library |
| `source/color-system.pdf` | Copied Color Guide |
| `source/icon-language.potx` | Copied Radiology Icon Library |
| `source/official-template.pptx` | Copied Bayer 16:9 Chart Pool (Aug 2019 Updated) |
| `BRAND.md` | Color/type/tone rules with citations |
| `STRUCTURE_PATTERNS.md` | BC patterns + Official Template (2019) merge section |
| `OFFICIAL_TEMPLATE.md` | Full Chart Pool catalog (layouts, diagrams, icons, theme) |
| `ICON_LANGUAGE.md` | Radiology + Chart Pool icon/element language |
| `THEME.json` | Machine-readable theme + official_template hints |
| `DIGEST.md` | This executive digest |
| `icons/` | Radiology POTX media (SVG/PNG/…) |
| `icons/official/` | Chart Pool maps, post-its, 3D samples, PNG/EMF/WMF |
