# Bayer BC Chart Library — Structure Patterns

**Source:** `source/structured-graphics.pptx`  
**Title (slide 1):** Business Consulting — Chart Library — Welcome — September, 2018  
**Slide count:** 271  
**Dimensions:** width `12190413` EMU × height `6858000` EMU ≈ **13.33" × 7.5"** (widescreen **16:9**)

## Masters / layouts

Single slide master with layouts:

| # | Layout name |
|---|-------------|
| 0 | Title slide |
| 1 | Agenda |
| 2 | Text |
| 3 | Title only |
| 4 | Chapter |
| 5 | Chapter 2 |
| 6 | Chapter 3 |
| 7 | Image |
| 8 | Final Slide |
| 9 | Content area & Guides |
| 10 | Blank |
| 11 | Title only (color) |

Most chart templates use **Title only** (or **Title only (color)** for icon catalog pages). Section dividers use **Title slide**. Chapter TOC pages use **Agenda**.

## Document chapters (TOC slide 2)

1. **Project basics** — Meeting objectives, Agenda slides, Project charters, Organization charts, Project phases, Status updates, Next steps, Decision templates, Evaluation  
2. **Structures** — Alternatives, Structuring, Cycles, Elements, Influencing factors, Controversy, Hierarchy, Causality, Process, Directions, Summary, Other  
3. **Frameworks** — BCG, ABC, Ansoff, Porter’s 5 forces, RACI, ADKAR, SWOT, Logic tree, Product life cycle, …  
4. **Icons** — Business, Nature and Energy, Medical, Leisure, Silhouette  
5. **Maps & Flags** — World / continents / country maps, Flags  

Closing slides: Thank you; Bayer Pharmaceuticals / Crop Science / Animal Health title variants.

---

## Pattern catalog

Index = 1-based slide number. AntV Infographic mappings are **recommended** for a future Bayer-ppt → infographic-creator bridge (template family prefixes: `list-*`, `sequence-*`, `compare-*`, `hierarchy-*`, `relation-*`, `chart-*`).

### A. Project management / meeting basics

| Pattern | Slides | Purpose / anatomy | AntV mapping |
|---------|--------|-------------------|--------------|
| Chapter divider | 5, 48, 177, 197, 240 | Full-bleed chapter title + library subtitle | — |
| Section agenda (TOC) | 6, 9, 14, 19, 24, 35, 38, 40, 42, 49, … | Left/center agenda list highlighting current section | `list-row-simple` / `list-vertical` |
| Objectives (5 cards) | 7 | Title + 5 equal text cards | `list-grid-card` / `list-row-card-compact` |
| Goals (nested levels) | 8 | Goal header + Level 1 / Level 2 bullets | `hierarchy-tree-basic` / `list-row-simple` |
| Agenda 1 / Agenda 2 | 10–11 | Simple numbered/outline agenda | `list-row-simple` |
| Multilayered agenda | 12–13 | Top page grid of agenda cells; deep dive with Sub agenda item / Objective / Responsible columns | `list-grid-card`; deep dive ≈ `compare-table` / `hierarchy-tree` |
| Project scope / in vs out | 15–16 | Project objectives + **What’s in** / **What’s not in** (or What’s out) columns | `compare-binary-horizontal` / `compare-vs` |
| Work stream charter | 17–18 | Hypotheses, objectives, organization, leader, team members fields | `list-row-simple` + custom form layout |
| Project organization / org chart | 20–23 | Workstreams, leaders, members; structure plan; governance (Roles/Responsibilities/Steering Committee); teams by function | `hierarchy-org-tree` / `hierarchy-tree-basic` |
| Project timeline (Gantt-like) | 25–31 | Month headers (Jan–Dec) + phase bars / workstream rows | `sequence-timeline-horizontal` / `chart-*` custom |
| Approach & deliverables | 32 | Stage columns: Discovery… Strategy… Org. alignment… | `sequence-steps-horizontal` / `list-column-vertical` |
| Project phases | 33–34 | Phase headlines; detail with duration (“… weeks”), Phase I / II | `sequence-steps-horizontal` / `sequence-timeline` |
| Status overview / report | 36–37 | Status cells; Decisions and issues / Recent achievements | `list-grid-card` / `compare-table` |
| Next steps | 39 | Ordered next-step cards | `sequence-steps-vertical` / `list-row-simple` |
| Decision template | 41 | Recommendations checklist (ü marks) | `list-row-simple` |
| Pros & cons | 43 | Multi-header comparison columns | `compare-binary-horizontal` / `compare-table` |
| Recommendations | 44 | Stacked recommendation items | `list-row-card` |
| Decision matrix | 45–47 | Priority matrix / scored options / “?” decision cells | `chart-quadrant` / `compare-table` |

**Labels:** Meeting objectives, Agenda item, Sub agenda item, Objective, Responsible, Project scope, What’s in / What’s not in, Work stream charter, Initial working hypotheses, Project organization, Steering Committee, Project Lead, Status, Decisions and issues, Recent achievements, Next steps, Pros & cons, Priority.

### B. Structures — alternatives, funnels, buckets, lists

| Pattern | Slides | Anatomy | AntV mapping |
|---------|--------|---------|--------------|
| Photo + text layouts | 50–52 | Placeholder image + Level 1/2 text | — (layout, not infographic) |
| Key facts | 53 | 4 fact cards + supporting text | `list-grid-card` |
| Structuring / best-fit alternative | 55–56 | Deduction tree toward preferred option | `hierarchy-tree-basic` / `relation-flow` |
| Funnel horizontal | 57 | Horizontal narrowing stages | `sequence-funnel` / `sequence-steps-horizontal` |
| Funnel vertical | 58–59 | Vertical funnel stages | `sequence-funnel` |
| Buckets | 60–62 | 3+ headline buckets with body text | `list-column-vertical` / `list-grid-card` |
| Increasing list | 63 | Ascending emphasis list | `sequence-ascending` / `list-row-simple` |
| Multi-dimension list | 64 | Cross-tab style (e.g. FLEX in progress / not in progress) | `compare-table` |

### C. Cycles / circles

| Pattern | Slides | Anatomy | AntV mapping |
|---------|--------|---------|--------------|
| Circles 1–6 | 66–71 | Circular / orbital node arrangements | `relation-circle` / `sequence-circle-process` |
| Circle with content blocks | 72 | Central circle + surrounding blocks | `relation-circle` |

### D. Elements / cards / factors / intersections

| Pattern | Slides | Anatomy | AntV mapping |
|---------|--------|---------|--------------|
| Elements 1–12 (+ Overviews) | 74–90 | Multi-node element maps; Category 1…n; Icon + text tiles; overview variants | `list-grid-card` / `relation-network` / `hierarchy-mindmap` |
| Factors 1–3 | 91–93 | Factor columns / spokes | `list-column-vertical` / `relation-circle` |
| Intersection 1–2 | 94–95 | Overlapping sets | `relation-venn` / `compare-overlap` |
| Puzzle (+ Overview) | 96–97 | Interlocking pieces | `relation-puzzle` / `list-grid` |
| Gear wheels | 98, 174 | Interlocking gears + labels | `relation-circle` (stylized) |

### E. Influencing factors / controversy

| Pattern | Slides | Anatomy | AntV mapping |
|---------|--------|---------|--------------|
| Influencing factors | 100–104 | Headers + Level 1/2; alternatives; multiple layers | `hierarchy-tree` / `relation-flow` |
| Bottom up / top down | 105 | Bidirectional hierarchy | `hierarchy-tree-basic` |
| Pressure | 106 | Pressure/force diagram | `relation-flow` |
| Time, costs, quality | 108 | Triple-constraint triangle | `relation-triangle` / `compare-triple` |
| Controversy / tension | 109–110 | Opposing poles / tension bars | `compare-binary-horizontal` |
| Conflict | 111 | Conflict nodes | `relation-conflict` / `compare-vs` |

### F. Hierarchy

| Pattern | Slides | Anatomy | AntV mapping |
|---------|--------|---------|--------------|
| Temple | 113 | Pillar/base hierarchy | `hierarchy-pyramid` / `hierarchy-tree` |
| Pyramid 1–2 (+ Overview) | 114–117 | Layered pyramid | `hierarchy-pyramid` |
| Clustering pyramid | 118 | Pyramid with clusters | `hierarchy-pyramid` |
| Factors (numbered 1–3) | 119–120 | Stacked factor bands | `list-row-simple` / `hierarchy-pyramid` |

### G. Causality / process / directions

| Pattern | Slides | Anatomy | AntV mapping |
|---------|--------|---------|--------------|
| Changes – From… To… | 122 | Before/after | `compare-binary-horizontal` / `sequence-from-to` |
| Consequences 1–3 (+ Overview) | 123–127 | Cause → effect chains | `relation-flow` / `sequence-steps` |
| Process 1–9 | 129–137 | Linear process steps (arrows/chevrons) | `sequence-steps-horizontal` / `sequence-arrow-flow` |
| Process Decreasing / Increasing | 138–139 | Sized steps | `sequence-ascending` / `sequence-descending` |
| Process mapping | 140 | Process map grid | `relation-flow` / `chart-process` |
| Target list / matrix | 142–143 | Targets list; 2-axis target matrix | `list-row`; `chart-quadrant` |
| Directions 1–4 | 144–147 | Directional arrows / strategic directions | `relation-flow` / `sequence-steps` |

### H. Summary / roadmap / other structures

| Pattern | Slides | Anatomy | AntV mapping |
|---------|--------|---------|--------------|
| Overview | 149 | Multi-block overview | `list-grid-card` |
| Strategy roadmap | 150 | Phased roadmap | `sequence-timeline-horizontal` |
| Summary 1–6 | 151–157 | 5 / 7 / 10 element summary layouts | `list-grid-card` / `list-circle` |
| Interrelation 1–4 | 159–162 | Linked nodes | `relation-network` |
| Logical dimensions | 163 | Elements mapped to dimensions | `compare-table` / `chart-matrix` |
| Chances / risks | 164 | Chances vs Risks columns | `compare-binary-horizontal` |
| Imbalance | 165 | Unequal columns | `compare-binary` |
| Dependence | 166 | Dependency links | `relation-flow` |
| Plus / minus | 167–168 | + / − columns | `compare-binary-horizontal` |
| Characteristics and impact | 169 | Long-term / impact axes | `chart-quadrant` |
| Clustering | 170 | Cluster groups | `relation-cluster` |
| Iceberg | 171 | Above/below surface | `hierarchy-iceberg` / `compare-layers` |
| Cubes | 172 | 3D cube stack metaphor | `hierarchy-cubes` |
| Exemplary tracker | 173 | Status tracker | `sequence-timeline` / `list-row` |
| Post-it / sticky notes | 175 | Sticky note grid | `list-grid-card` |
| Bayer logos | 176 | Logo lockups | — |

### I. Frameworks (textbook)

| Pattern | Slides | Anatomy | AntV mapping |
|---------|--------|---------|--------------|
| Situation – Complication – Solution | 178 | SCS three columns | `sequence-steps-horizontal` / `list-column` |
| BCG matrix | 179 | 2×2 High/Low | `chart-quadrant` / `compare-quadrant` |
| ABC analysis | 180 | A/B/C cumulative % | `chart-*` / `sequence-funnel` |
| RACI chart | 181 | R/A/C/I responsibility matrix | `compare-table` |
| Value Chain | 182 | Sequential value stages | `sequence-steps-horizontal` |
| ADKAR model | 183 | Awareness → Desire → Knowledge → Ability → Reinforcement | `sequence-steps-horizontal` |
| SWOT | 184 | Strengths / Weaknesses / Opportunities / Threats | `compare-quadrant` |
| Strengths and weaknesses | 185 | Two columns | `compare-binary-horizontal` |
| Logic tree 1–2 | 186–187 | Issue tree branches | `hierarchy-tree-basic` |
| Cluster & prioritize matrix | 188 | High/Low axes | `chart-quadrant` |
| Porter’s 5 forces | 189 | Center rivalry + four forces | `relation-force-diagram` |
| Ansoff Matrix | 190 | Old/New × Old/New | `chart-quadrant` |
| Process framework – High-level flow | 191 | Main vs supporting processes | `relation-flow` |
| Swim lane diagram | 192 | Functional lanes + interfaces | `relation-swimlane` |
| Risk matrix | 193 | Likelihood × Negative impact | `chart-quadrant` |
| Stakeholder analysis | 194 | Owners / Facilitators / Followers… | `chart-quadrant` / `list-grid` |
| Product life cycle | 195–196 | Introduction → Growth → Maturity → Decline (± fill) | `chart-line` / `sequence-curve` |

### J. Icons chapter (catalog, not structural charts)

| Pattern | Slides | Notes |
|---------|--------|-------|
| How to use icons | 198 | Guiding principles (see ICON_LANGUAGE.md) |
| Icon structure TOC | 199, 208, 214, 220, 232 | Business / Nature and Energy / Medical / Leisure / Visuals |
| BC Icon Library pages | 200–239 | Category catalogs: Documents and data, People, Finance, Signs and Figures, IT, Business Basics, Energy, Nature, Medical, Food, Animals, Sports, Travel, Manufacturing, Smart factory, Silhouettes, etc. |

### K. Maps & Flags

| Pattern | Slides | Notes |
|---------|--------|-------|
| World / regional maps | 242–259 | Abstract ball, detailed, country lines; continents; USA; Germany (cities: Kiel, Hamburg, Berlin, …) |
| Flags | 261–267 | Country/region flag grids (7 pages) |

---

## Recurring placeholder terminology (EN)

`Subtitle – Unit` · `Headline` · `Text` · `Level 1` / `Level 2` · `Topic` · `Category n` · `Header` · `Placeholder image` · `ILLUSTRATIVE EXAMPLE` · `What’s in` / `What’s not in` / `What’s out` · `Chances` / `Risks` · `High` / `Low` · month abbreviations `Jan`…`Dec` · `Phase I` / `Phase II`

**Chinese:** none found in this PPTX.

## Design anatomy notes for Bayer-ppt skill

- Prefer **flat filled rectangles / rounded cards** in Bayer blues/greens/purples with Dark Blue text.
- Process patterns: horizontal chevrons or numbered nodes with arrows.
- Matrices: explicit axis labels (High/Low, Old/New, Likelihood/Impact).
- Many slides pair a **detail** layout with an **Overview** sibling for executive summary.
- Page number + title bar conventions from master layouts should be preserved when generating decks.

---

## Official Template (2019) — Bayer 16:9 Chart Pool

**Source:** `source/official-template.pptx`  
**Identity:** *Bayer Chart pool* / */// Bayer 16:9 Template Chart Pool /// August 2019* (“Updated version”)  
**Full catalog:** [`OFFICIAL_TEMPLATE.md`](OFFICIAL_TEMPLATE.md)  
**Slide count in this copy:** 330 (agenda still cites original pool indices up to ~438; Flags / Flags-on-pin / some Layout & Placeholder chapters are **not** present here)

Use this section for **corporate layout + diagram families that expand beyond** the BC Chart Library. For consulting textbook frameworks (BCG, Porter, ADKAR, RACI, Ansoff, swimlane, stakeholder…), **prefer the BC Chart Library sections above** and only cross-link here when the Chart Pool has a practical twin.

### Preferred master layouts (authoring)

Title Slide / Title slide 2–3 / Titelfolie · Agenda · Chapter 1–3 · Content / 内容 / Content (2) · Text (4) · Text (2) & Images (2) · **Title only (color)** (default working canvas) · Quote · Image / Image color* · Text & Image* / transparent* · Final Slide 1–3

### New / expanded pattern families (this file’s indices)

| Pattern | Slides | Anatomy | AntV mapping | vs BC Chart Library |
|---------|--------|---------|--------------|---------------------|
| Native chart strip | 10–21 | Column / stacked / bar / waterfall / pie / doughnut / line / spider | `chart-column` `chart-bar` `chart-pie` `chart-line` `chart-radar` | Overlap — Chart Pool has cleaner Excel-native strip |
| Org / spheres tree / connected spheres | 27–40 | Classic org + sphere hierarchy/network | `hierarchy-org-tree` `hierarchy-tree-basic` `relation-network` | Org overlaps BC; **spheres** visual is Chart Pool–strong |
| **Butterfly diagrams** | 41–48 | Mirrored L/R stacks (2+2…6+6; asymmetric) | `compare-binary-horizontal` / dual `list-column-vertical` | **New family** |
| Venn 2–6 + intersection | 49–56 | Multi-circle overlap | `relation-venn` / `compare-overlap` | Overlap with BC cycles/overlap |
| Pyramid + pyramid toolbox | 57–65 | 3–6 layers + parts toolkit | `hierarchy-pyramid` | Overlap; toolbox is Chart Pool–strong |
| Photo + text usage | 71–77 | Photography placement guidance | — (layout) | Complements BC photo+text; richer master layouts |
| Process steps / triangle / options / road | 78–94 | N-steps, triangle process, 3–4 options, road to success | `sequence-steps-*` `sequence-roadmap` `hierarchy-pyramid` | Overlap + **road/triangle** variants |
| PM toolbox (SWOT, scope, status, matrices, PLC…) | 95–138 | Meeting/project practicals | See BC §A / §I mappings | **Heavy overlap** — treat BC as framework authority; Chart Pool as alt layouts |
| **Circular shapes toolkits** | 139–165 | Ring segments 3–6+, arrow cycles, design samples | `relation-circle` `sequence-cycle` `chart-pie` | **Major expansion** vs BC cycles |
| Project timelines / trend | 166–173 | Gantt-like, arrow timelines, trend | `sequence-timeline-horizontal` | Overlap |
| Maps & globes | 174–194 | World/regions/Germany/continents/globes | — / map overlay | Overlap maps; **Flags missing** in this copy |
| Icon catalogs (business/science/medical/crop) | 195–238 | Grouped-shape icon grids | — (icons) | Overlap categories; **Crop Science** + disease set are Chart Pool–strong → see ICON_LANGUAGE |
| Silhouettes / puzzle / cubes / gears | 239–243 | Decorative metaphors | — | Overlap; decorative only |
| Post-it / hand-drawn / **timer** | 244–246 | Workshop UI; animated timer | `list-grid-card` | Post-it overlaps; **Timer** new |
| **3D characters** | 247–325 | Photographic 3D people/props (~79 slides) | — | **New asset class** — optional illustration, not default icon language |
| Logos / Color / Gradient | 326–328 | Logo lockups; 12 named hues; gradients | — | Color names align with Color Guide |
| Contact / classification | 329–330 | Contact card; Identity Net classification ribbon | — | Corporate compliance |

### AntV quick picks unique to Official Template

- Options / pros sides → **Butterfly** → `compare-binary-horizontal`
- Cycle / segmented ring → **Circular shapes toolkit** → `relation-circle` / `sequence-cycle`
- Sphere org → `hierarchy-tree-basic` or `relation-network`
- Workshop facilitation → post-it grid `list-grid-card` (+ timer as non-AntV chrome)

### Precedence when patterns collide

1. **Consulting frameworks / named models** → BC Chart Library  
2. **Corporate layouts, butterflies, circular toolkits, maps-without-flags, 3D people, classification** → Official Template  
3. **Radiology outline SVG icons** → Radiology POTX (`icons/` root)
