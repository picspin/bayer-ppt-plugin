---
name: Bayer-ppt
description: >-
  Use when building Bayer / company decks that must follow Color Guide, Chart
  Pool layouts, BC Chart Library frameworks, and Bayer icon language — with
  ppt-master + AntV Infographic. For Radiology/Centargo, use Icon Library POTX
  as slide master. Also covers academic-promotion (学术推广) deck mode: Bayer
  Radiology decks for research-minded physicians that present frontier
  research, adoptable study protocols, and the product as a research platform.
  This mode uses an assertion-title arc, keeps compliance notes off the slide
  face, and includes a slide-face lint step.
---
# Bayer-ppt

Use this for **any Bayer / company presentation** that must follow Bayer brand templates. This includes corporate Chart Pool layouts, consulting frameworks, pharma/radiology, Crop Science, general pitches and **academic-promotion (学术推广) decks**.

This skill is a brand layer on top of [ppt-master](sand-workflow:ppt-master) and [infographic-creator](sand-workflow:infographic-creator). Load those after this skill and the brand assets.

## Brand asset root

`/home/box/tools/bayer-ppt/`

| File | Use |
|------|-----|
| `THEME.json` | Palette, fonts, slide size, AntV palette, layout hints |
| `BRAND.md` | Color rules, typography, tone |
| `DIGEST.md` | Four-asset model + **precedence** |
| `OFFICIAL_TEMPLATE.md` | Bayer 16:9 Chart Pool (Aug 2019): layouts, diagrams, icons, elements |
| `STRUCTURE_PATTERNS.md` | BC Chart Library + Official Template (2019) section → AntV maps |
| `ICON_LANGUAGE.md` | Radiology SVG outline language + Chart Pool element language |
| `source/color-system.pdf` | Bayer Color Guide |
| `source/structured-graphics.pptx` | BC Chart Library (2018, 271 slides) |
| `source/official-template.pptx` | Chart Pool Updated (2019, 330 slides in this copy) |
| `source/icon-language.potx` | **Radiology Icon Library POTX**: primary slide-master backbone for Radiology/Centargo decks (`ALL.AA.Illustrative_Elements.Icon_Library_Overview`) |
| `icons/` | Radiology SVG/PNG exemplars |
| `icons/official/` | Chart Pool maps, post-its, 3D samples, rasters |
| `references/academic-promotion-mode.md` | Full playbook for academic-promotion (学术推广) decks |
| `references/chart-intent-map.md` | Slide intent → Chart Pool / BC indices / AntV templates; diversity rules |
| `references/cover-and-density.md` | Global-thesis cover procedure, 70–80% density proxy, cited-content source-crop rule |
| `scripts/lint_slide_face.py` | Slide-face lint: banned words, text load, visuals, **density 0.70–0.80**, **SRC_ crops on cited slides**, cover fit, pattern diversity |
| `scripts/fit_cover_image.py` | Center-crop an image to the cover picture placeholder aspect and insert at exact bounds (`COVER_IMG`) |
| `scripts/chart_pool_index.py` | Search/show Chart Pool (`--lib cp`) or BC Chart Library (`--lib bc`) slides by keyword |

Working master copy for python-pptx (content-type patched): often `/workspace/.../bayer-radiology-master.pptx`, derived from the POTX.

**Before designing:** read `THEME.json` and the `DIGEST.md` precedence, then the pattern docs that match the ask. Never invent HEX.

## Slide master backbone (Radiology / Centargo)

For Bayer Radiology and especially **Centargo** decks, do **not** build blank custom slides as the chrome. Start from `source/icon-language.potx` and use the product layouts so the Bayer logo and frame styles stay on the master:

| Role | Layout name (examples) |
|------|------------------------|
| Title | `MEDRAD Centargo Title Slide 3` (or MEDRAD Title Slide 1/2) |
| Content | `MEDRAD Centargo Text Slide with logo` |
| Agenda | `MEDRAD Agenda` |
| Color BG content | `MEDRAD Centargo Text Color Background Logo` |

Other product families (Gadovist, Ultravist, Primovist, Radimetrics, Equipment Service, …) have parallel layouts on the same master. Pick the matching product set when the deck is product-specific.

Fill the title/subtitle/footer/date/slide-number placeholders. Add structure cards in the content area **without removing** the layout logo graphics.

## Precedence (critical)

1. **Brand hues (12 + white):** Color Guide wins. Mid Green = `#2B6636` (ignore BC `#2B6640` drift).
2. **Radiology/Centargo slide chrome (logo/frame):** Icon Library POTX masters/layouts.
3. **Corporate layouts / photo+text / butterflies / circular toolkits / spheres / 3D people / classification:** Official Chart Pool (`OFFICIAL_TEMPLATE.md`).
4. **Consulting frameworks** (BCG, Porter, ADKAR, RACI, Ansoff, swimlane, stakeholder, SCS…): BC Chart Library.
5. **Outline SVG icons + radiology product accents:** Radiology POTX (`icons/`). Chart Pool icons are grouped shapes + `icons/official/`. Approximate them with outline Dark Blue unless the user wants Pool art.
6. **Traffic lights / trend icons:** status only, not decoration.
7. **Fonts:** Arial / Arial Unicode MS until official Bayer fonts are provided.

## Hard constraints

1. Palette only from Color Guide 12 + white (+ black as theme `dk1`). Body text: `#10384F` on `#FFFFFF`.
2. Do not map palette colors to divisions/departments. Crop Science in Chart Pool is an **icon chapter**, not a division palette.
3. Slide size 16:9: `12190413 × 6858000` EMU.
4. Icons: outline, ~SW 8 on 256, `#10384F`, max one accent. Icons support titles and never replace them. Do not recolor Dark Blue strokes. **Do not default to Chart Pool 3D JPEGs**.
5. Radiology / product accents (e.g. MEDRAD `#E46C0A`) only when asked for Radiology/product decks.
6. Classification ribbon (Identity Net): remind the user for internal decks when appropriate. Do not invent marks.
7. The Chart Pool copy may be an **Updated subset**. Prefer the file indices in `OFFICIAL_TEMPLATE.md` over agenda numbers.

## Default pipeline

1. Clarify the deliverable if needed (outline / full draft / tighten). Ask whether this is an **academic-promotion** deck. If it is, load `references/academic-promotion-mode.md`.
2. Open the Icon Library POTX (or Chart Pool for non-Radiology corporate) as the presentation backbone.
3. **Per slide, pick the structure by intent** (`references/chart-intent-map.md`): write the one-sentence message → classify intent → choose 1–2 CP/BC/AntV candidates (inspect with `scripts/chart_pool_index.py`) → assemble. Record `INTENT: <id> | PATTERN: CP##/BC##/antv` in the notes. No pattern family on >30% of content slides; no identical pattern on adjacent slides; card grids are the fallback, not the default.
4. For dense structure, use [infographic-creator](sand-workflow:infographic-creator) with `THEME.json` → `antv_theme.palette` (Dark Blue first).
5. **Cover last, from the whole deck** (`references/cover-and-density.md`): list every slide's assertion → one-sentence deck thesis + 3 visual motifs → route A: generate a 16:9 image via [image-gen-router](sand-workflow:image-gen-router) (MGA `mga_image.py -a 16:9 -q high`; flat corporate, Bayer palette, no text/logos/faces, negative space under the title) or Grok `GenerateImage` where available; route B: one global cover schema from Chart Pool / Icon Library. Fit with `scripts/fit_cover_image.py deck.pptx img --slide 1` (exact crop to the picture placeholder; never tile or stretch). Note `COVER: thesis=… | route=A/B | prompt=…`.
5a. **Cited content = source crop.** Any slide citing a paper (arXiv/doi/PMID/et al./[n]/Fig./Table) must show ≥1 crop of the cited figure/table/page region, shape name `SRC_<id>`, with a caption `Source: Author Year, Venue, Fig./Table N, license`. Our infographics/tables supplement it, never replace it.
5b. **Density 70–80%.** Keep gutters and margins, but no empty quadrants. Too low → enlarge the hero visual / add the source crop / KPI chips; too high → cut text into notes, split the slide.
6. Compose on master layouts with python-pptx and `/home/box/tools/ppt-master/.venv/bin/python`. Use the full [ppt-master](sand-workflow:ppt-master) flow when generating from documents (`SKILL_DIR=/home/box/tools/ppt-master/skills/ppt-master`).
7. **Lint before delivery:**
   ```
   /home/box/tools/ppt-master/.venv/bin/python /home/box/agent-data/workflows/bayer-ppt/scripts/lint_slide_face.py deck.pptx [--json]
   ```
   - Any Python with python-pptx also works.
   - Fix every banned-word hit (exit code 1) before delivery.
   - Bring every content slide's `dens=` into 0.70–0.80 (cover, agenda, section, references, closing are skipped; tag others `DENSITY: skip` in notes).
   - Fix every `CITE:` violation (add an `SRC_` crop); use `--strict` to make them fail the build.
   - Fix `cover:` warnings (image must be `COVER_IMG`, aspect = box) and `DIVERSITY` warnings.
   - Review text-load and no-visual warnings.
   - This step is mandatory for academic-promotion decks and recommended for all decks.

## Academic-promotion deck mode (学术推广)

**Context:** Bayer Radiology, typically Centargo / P3T® / PAT.

**Audience:** physicians hungry for frontier research.

**Purpose:**
- Show frontier research.
- Offer study protocols the department can adopt.
- Position the product as a **research platform**.

The full playbook is in `references/academic-promotion-mode.md`.

### Narrative arc (page-by-page template)

| # | Slide | Content |
|---|-------|---------|
| 1 | Title | Frontier question as the title, product + department as the subtitle |
| 2 | Frontier question | Why this matters now, with a hero visual |
| 3–4 | Evidence landscape | Key studies in a literature-figure grid or timeline, with cited numbers only |
| 5 | Unresolved clinical question | The gap the evidence leaves open |
| 6–7 | Product as research platform | The capability, the parameters it controls/records, and why that enables studies |
| 8–N | Adoptable proposals (one block per proposal) | Hypothesis → design schematic → endpoints → literature figure → value to the department |
| N+1 | Rollout roadmap | Phased timeline (pilot → cohort → publication) |
| N+2 | Collaboration invitation | Clear ask, contact, and next step |

### Copy rules

- **Titles are assertions**, not topics. For example: 「个体化对比剂方案可降低剂量变异」, not 「对比剂方案」.
- **Product names are confident and registered only:** P3T®, PAT, Centargo. Never use invented names such as "Smart Protocol".
- **Compliance constraints go only in speaker notes.** Never put 红线 / 合规 / 规避 / "red line" / "compliance" on the slide face.
- **Phrase factual boundaries positively.** Use 「探索…能否…」 or "investigator-defined protocol" rather than prohibitions.
- **No promised percentages** beyond locked or cited numbers. Every number on the slide carries a source.
- **Facts must stay accurate.** Off-label uses are framed as research questions, never as product features.

### Visual rules

- Use a hero visual, fewer text boxes, and **image + text on every slide**.
- Build charts in the Bayer palette with matplotlib or AntV infographics (Dark Blue first).
- Literature figure screenshots need a source caption + license. Prefer CC BY and note the license in the caption or notes.

### Self-check before delivery

- [ ] The arc follows the template, and every proposal has hypothesis / design / endpoints / literature figure / department value.
- [ ] Every title is an assertion.
- [ ] Only registered product names are used.
- [ ] Compliance language appears only in speaker notes.
- [ ] All numbers are locked or cited, and no off-label use is presented as a feature.
- [ ] Every slide has an image or chart, and literature figures carry a source + license.
- [ ] Cover derived from the deck thesis (notes `COVER:` line), fitted with `fit_cover_image.py`, no tiling/stretching/letterbox.
- [ ] Each content slide density 0.70–0.80 (lint `dens=`); whitespace = gutters/margins, not empty areas.
- [ ] Each slide has `INTENT | PATTERN` in notes; ≥4 intents in decks with ≥10 content slides; no family >30%.
- [ ] Every slide with cited content shows an `SRC_` source crop + caption (source, Fig./Table no., license).
- [ ] `python3 scripts/lint_slide_face.py deck.pptx [--json]` has been run (ppt-master venv python or any python with python-pptx). It flags:
  - banned slide-face words (exit 1)
  - more than 8 substantive text boxes
  - more than 220 CJK chars
  - more than 90 latin words
  - no image/chart

  Notes are not checked for banned words.

### Example layout specs (worked example)

**Worked example:** `/workspace/pcct-centargo-proposal/build/PCCT_Centargo_P3T_研究Proposals_v4.pptx`.

**Anti-example:** v3, which had these problems:
- red-line boxes on S7/S8/S14/S21
- dense S16–S18
- 29 boxes on S22

The page numbers below are as of v4. Re-check them if the deck is rebuilt.

**A. Proposal slide** (cf. the v4 rebuilds of v3 S7/S8):
- Assertion title (hypothesis as a claim to test).
- Left ~55%: design schematic (AntV flow: cohort → P3T®/PAT arm vs. standard → endpoints).
- Right: literature figure with a source + license caption.
- Bottom strip: 2–3 endpoint chips + one "value to the department" line.
- No more than 6 text boxes. Compliance notes go in the speaker notes only.

**B. Platform / roadmap slide** (cf. the v4 rebuilds of v3 S16–S18 / S22):
- Hero product image (Centargo) on the left.
- Right: 3 capability cards. Each card has an outline Dark Blue icon, a short label, and a one-line "what this lets you study".
- The roadmap is a single horizontal timeline in Bayer Blue → Green.
- The collaboration ask goes in one emphasized box.
- No more than 8 substantive boxes, and under 220 CJK chars.

## Quick palette

| Role | HEX |
|------|-----|
| Primary / body | `#10384F` |
| Bayer Blue | `#0091DF` |
| Bright Blue | `#00BCFF` |
| Mid Blue | `#00617F` |
| Bright Green | `#89D329` |
| Green | `#66B512` |
| Mid Green | `#2B6636` |
| Dark Green | `#004422` |
| Fuchsia | `#FF3162` |
| Raspberry | `#D30F4B` |
| Mid Purple | `#624963` |
| Dark Purple | `#443247` |
| White | `#FFFFFF` |

## Tone

Professional consulting / life-science corporate. Use a clear title, Level 1/2 density, and an Overview for complex diagrams. For Chinese decks, write bilingual copy without claiming it came from brand files. In academic-promotion mode, the tone is peer-to-peer scientific: confident, evidence-led and inviting.

## Do not

- Invent non-Bayer colors or rainbow defaults
- Build Radiology/Centargo decks without the Icon Library POTX master chrome
- Flatten structure to bitmaps when SVG/native shapes work
- Mix icon weights or default to 3D character stock
- Skip brand files on company decks
- Put compliance words on the slide face (红线 / 合规 / 规避 / red line / compliance). Keep them in speaker notes
- Use invented product names (e.g. "Smart Protocol"). Use registered names only (P3T®, PAT, Centargo)
- Insert a cover image that is tiled, stretched, letterboxed or not sized to the cover placeholder
- Present cited numbers/figures with only a redrawn infographic and no source crop
- Default every slide to the same card grid
