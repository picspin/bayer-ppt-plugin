---
name: bayer-ppt
description: >-
  Use when building Bayer / company decks that must follow Color Guide, Chart
  Pool layouts, BC Chart Library frameworks, and Bayer icon language — with
  ppt-master + AntV Infographic. For Radiology/Centargo, use Icon Library POTX
  as slide master.
---
# Bayer-ppt

Use this for **any Bayer / company presentation** that must follow Bayer brand templates — corporate Chart Pool layouts, consulting frameworks, pharma/radiology, Crop Science, or general pitches.

Brand layer on top of **ppt-master** (peer skill — see `ppt-master-bridge`) and **infographic-creator** (bundled in this repo). Load those after this skill and the brand assets.

## Path resolution (portable)

Resolve paths relative to the **plugin/repo root**, never hard-code a single machine path.

| Variable | Meaning |
|----------|---------|
| `${BAYER_PPT_ROOT}` | Directory containing this skill’s parent repo (the publishable package). Default: detect as the repo root that contains `brand-kit/` (walk up from this `SKILL.md` → `skills/bayer-ppt/` → repo root). Override with env `BAYER_PPT_ROOT` if needed. |
| `${REPO_ROOT}` | Same as `${BAYER_PPT_ROOT}` for this package. |
| Brand kit | `${REPO_ROOT}/brand-kit/` |
| Proprietary sources | `${REPO_ROOT}/brand-assets/source/` |
| Outline icon examples | `${REPO_ROOT}/brand-kit/icons/examples/` |

**Local Grok Bot install example** (not the publishable layout): `/home/box/tools/bayer-ppt/` may hold the same brand-kit + `source/` binaries on an internal box. Prefer `${REPO_ROOT}` when this plugin is installed via `npx skills add`.

### Brand asset map

| Path under `${REPO_ROOT}` | Use |
|---------------------------|-----|
| `brand-kit/THEME.json` | Palette, fonts, slide size, AntV palette, layout hints |
| `brand-kit/BRAND.md` | Color rules, typography, tone |
| `brand-kit/DIGEST.md` | Four-asset model + **precedence** |
| `brand-kit/OFFICIAL_TEMPLATE.md` | Bayer 16:9 Chart Pool (Aug 2019) — layouts, diagrams, icons, elements |
| `brand-kit/STRUCTURE_PATTERNS.md` | BC Chart Library + Official Template (2019) section → AntV maps |
| `brand-kit/ICON_LANGUAGE.md` | Radiology SVG outline language + Chart Pool element language |
| `brand-kit/icons/examples/` | Generic outline SVG exemplars (style only) |
| `brand-assets/source/color-system.pdf` | Bayer Color Guide *(proprietary — drop-in)* |
| `brand-assets/source/structured-graphics.pptx` | BC Chart Library *(proprietary — drop-in)* |
| `brand-assets/source/official-template.pptx` | Chart Pool Updated *(proprietary — drop-in)* |
| `brand-assets/source/icon-language.potx` | **Radiology Icon Library POTX** — primary slide-master backbone for Radiology/Centargo (`ALL.AA.Illustrative_Elements.Icon_Library_Overview`) |

### Working master for python-pptx

POTX / PPTX masters often need a **content-type patched** working copy before `python-pptx` can open them reliably (e.g. rename/copy `icon-language.potx` → a `.pptx` working master and patch `[Content_Types].xml` / relationships as required by your tooling).

Suggested location (gitignored exports): `${REPO_ROOT}/exports/bayer-radiology-master.pptx` or a project-local path such as `./bayer-radiology-master.pptx`. Do not commit the binary master.

**Before designing:** read `THEME.json`, `DIGEST.md` precedence, then the pattern docs that match the ask. Never invent HEX.

## Peer skills

1. **infographic-creator** — vendored at `skills/infographic-creator/` in this repo. Use AntV Infographic DSL with `THEME.json` → `antv_theme.palette` (Dark Blue first).
2. **ppt-master** — **not vendored** (~900MB). Install peer: `npx skills add hugohe3/ppt-master`. See `deps/ppt-master.md` and `skills/ppt-master-bridge/SKILL.md`. When Bayer decks need native editable PPTX generation/edit routes, ensure ppt-master is installed and follow **its** `SKILL.md` at the installed location (`SKILL_DIR`).

## Slide master backbone (Radiology / Centargo)

For Bayer Radiology and especially **Centargo** decks, do **not** build blank custom slides as the chrome. Start from `brand-assets/source/icon-language.potx` and use product layouts so Bayer logo + frame styles stay on the master:

| Role | Layout name (examples) |
|------|------------------------|
| Title | `MEDRAD Centargo Title Slide 3` (or MEDRAD Title Slide 1/2) |
| Content | `MEDRAD Centargo Text Slide with logo` |
| Agenda | `MEDRAD Agenda` |
| Color BG content | `MEDRAD Centargo Text Color Background Logo` |

Other product families (Gadovist, Ultravist, Primovist, Radimetrics, Equipment Service, …) have parallel layouts on the same master — pick the matching product set when the deck is product-specific.

Fill title/subtitle/footer/date/slide-number placeholders; add structure cards in the content area **without removing** layout logo graphics.

## Precedence (critical)

1. **Brand hues (12 + white):** Color Guide wins. Mid Green = `#2B6636` (ignore BC `#2B6640` drift).
2. **Radiology/Centargo slide chrome (logo/frame):** Icon Library POTX masters/layouts.
3. **Corporate layouts / photo+text / butterflies / circular toolkits / spheres / 3D people / classification:** Official Chart Pool (`OFFICIAL_TEMPLATE.md`).
4. **Consulting frameworks** (BCG, Porter, ADKAR, RACI, Ansoff, swimlane, stakeholder, SCS…): BC Chart Library.
5. **Outline SVG icons + radiology product accents:** Radiology POTX + `brand-kit/icons/examples/`. Chart Pool icons are grouped shapes — approximate with outline Dark Blue unless user wants Pool art.
6. **Traffic lights / trend icons:** status only, not decoration.
7. **Fonts:** Arial / Arial Unicode MS until official Bayer fonts are provided.

## Hard constraints

1. Palette only from Color Guide 12 + white (+ black as theme `dk1`). Body text: `#10384F` on `#FFFFFF`.
2. Do not map palette colors to divisions/departments. Crop Science in Chart Pool is an **icon chapter**, not a division palette.
3. Slide size 16:9 — `12190413 × 6858000` EMU.
4. Icons: outline, ~SW 8 on 256, `#10384F`; max one accent; support titles — never replace them; do not recolor Dark Blue strokes; **do not default to Chart Pool 3D JPEGs**.
5. Radiology / product accents (e.g. MEDRAD `#E46C0A`) only when asked for Radiology/product decks.
6. Classification ribbon (Identity Net): remind for internal decks when appropriate — do not invent marks.
7. Chart Pool copy may be an **Updated subset** — prefer file indices in `OFFICIAL_TEMPLATE.md` over agenda numbers.

## Default pipeline

1. Clarify deliverable if needed (outline / full draft / tighten).
2. Open Icon Library POTX (or Chart Pool for non-Radiology corporate) as the presentation backbone.
3. Pick structure patterns from Chart Pool / BC Chart Library as needed.
4. Dense structure → **infographic-creator** with `THEME.json` → `antv_theme.palette` (Dark Blue first). Requires AntV Infographic CDN/runtime when rendering.
5. AI art → flat corporate graphics in Bayer palette. Prefer outline/flat over 3D people unless user asks.
6. Compose on master layouts via `python-pptx` (project venv) and/or full **ppt-master** when generating from documents — set `SKILL_DIR` to the installed ppt-master skill directory.

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

Professional consulting / life-science corporate. Clear title; Level 1/2 density; Overview for complex diagrams. For Chinese decks, write bilingual copy without claiming it came from brand files.

## Do not

- Invent non-Bayer colors or rainbow defaults
- Build Radiology/Centargo decks without the Icon Library POTX master chrome
- Flatten structure to bitmaps when SVG/native shapes work
- Mix icon weights; default to 3D character stock
- Skip brand files on company decks
- Vendor or commit proprietary POTX/PPTX/PDF binaries into the public skill repo
