# bayer-ppt-plugin

Cursor / Claude–compatible **skills marketplace** package for Bayer-branded PowerPoint workflows.

Bundles:

| Skill | Role |
|-------|------|
| `skills/bayer-ppt` | Brand rules, Centargo/Radiology master backbone, palette & precedence |
| `skills/infographic-creator` | Vendored AntV Infographic skill |
| `skills/ppt-master` | Thin wrapper → install peer `hugohe3/ppt-master` (not vendored) |
| `skills/ppt-master-bridge` | When native PPTX is needed, ensure ppt-master + follow its SKILL.md |

Derived specs live in `brand-kit/` (markdown + `THEME.json` + `assets.manifest.json`). Proprietary POTX/PPTX/PDF binaries are **not** shipped — resolve from local disk or a knowledge-base path.

---

## Quick start · 一键安装

```bash
./scripts/install.sh
# optional:
./scripts/install.sh --assets-dir /path/to/binaries --kb-dir /path/to/kb \
  --skip-ppt-master   # or omit to install peer
# Windows: .\scripts\install.ps1  (Git Bash / WSL) or see script help
```

Flags:

| Flag | Effect |
|------|--------|
| `--prefix DIR` | Venv / vendor prefix (default: `$REPO_ROOT/.venv`) |
| `--skip-ppt-master` | Do not `npx skills add` / clone ppt-master |
| `--skip-antv-runtime` | Skip `npm install @antv/infographic` (use CDN) |
| `--assets-dir DIR` | Sets `BAYER_ASSETS_ROOT` + `brand-assets/config.json` |
| `--kb-dir DIR` | Sets `BAYER_KB_ROOT` for recursive basename resolution |

Install creates a `.venv`, installs `python-pptx` / `lxml` / `Pillow`, optionally vendors ppt-master + AntV runtime, then runs:

```bash
python3 scripts/resolve_assets.py --check --write-env
```

### Asset / KB environment variables

```bash
export BAYER_PPT_ROOT=/path/to/bayer-ppt-plugin
export BAYER_ASSETS_ROOT=/path/to/local/binaries   # optional
export BAYER_KB_ROOT=/path/to/kb-or-sharepoint     # optional
# per-file override example:
export BAYER_ASSET_ICON_LIBRARY_POTX=/secure/icon-language.potx
# or:
source "$BAYER_PPT_ROOT/.bayer-ppt.env"
```

Verify:

```bash
python3 scripts/resolve_assets.py --check
python3 scripts/resolve_assets.py --json | head
python3 scripts/resolve_assets.py --get icon-library-potx
python3 scripts/resolve_assets.py --prepare-master
```

Manifest: [`brand-kit/assets.manifest.json`](brand-kit/assets.manifest.json). Details: [`brand-assets/README.md`](brand-assets/README.md).

### Marketplace / skills add

```bash
npx skills add YOUR_ORG/bayer-ppt-plugin
```

Claude Code / Cursor marketplace: `.claude-plugin/marketplace.json` registers plugin **`bayer-ppt`**.

### Peer dependencies · 对等依赖

1. **ppt-master** — installed by `install.sh` (or `npx skills add hugohe3/ppt-master`). See [`deps/ppt-master.md`](deps/ppt-master.md).
2. **Python venv** — created by `install.sh`.
3. **AntV Infographic** — optional local runtime under `runtime/antv-infographic`, or CDN: [infographic.antv.vision](https://infographic.antv.vision/).

---

## Private assets · 私有素材

```text
brand-assets/source/
  icon-language.potx          # Radiology Icon Library (slide master)
  official-template.pptx      # Chart Pool
  structured-graphics.pptx    # BC Chart Library
  color-system.pdf            # Color Guide
```

Or leave `source/` empty and resolve from `BAYER_KB_ROOT`. Instructions: [`brand-assets/source/README.md`](brand-assets/source/README.md).

**Working master (python-pptx):** `resolve_assets.py --prepare-master` → `exports/bayer-radiology-master.pptx` (gitignored).

---

## MEDRAD Centargo layout backbone · 母版规则

For Radiology / **Centargo** decks, start from the Icon Library POTX master — do **not** invent blank chrome:

| Role | Layout (examples) |
|------|-------------------|
| Title | `MEDRAD Centargo Title Slide 3` |
| Content | `MEDRAD Centargo Text Slide with logo` |
| Agenda | `MEDRAD Agenda` |

Keep Bayer logo + Centargo frame graphics from the layout; fill placeholders; add content cards in the body region only.

---

## Repo layout · 目录

```text
.claude-plugin/marketplace.json
skills/bayer-ppt/SKILL.md
skills/infographic-creator/SKILL.md
skills/ppt-master/SKILL.md
skills/ppt-master-bridge/SKILL.md
brand-kit/          # derived specs + assets.manifest.json + outline SVG examples
brand-assets/       # drop-in + config (binaries gitignored)
scripts/install.sh  # one-shot installer
scripts/resolve_assets.py
deps/ppt-master.md
examples/centargo-hospital-visits/
AGENTS.md
```

Path resolution uses `${REPO_ROOT}` / `${BAYER_PPT_ROOT}` (directory containing `brand-kit/`). Absolute `/home/box/tools/...` paths appear only as a **local Grok Bot install example**, not as the portable default.

---

## Example · 示例

See [`examples/centargo-hospital-visits/README.md`](examples/centargo-hospital-visits/README.md) for a **fictionalized** Centargo hospital-visit deck brief and rebuild pattern (no confidential operational PPTX).

---

## License note

Brand guide digests and outline exemplars are for authorized Bayer presentation work. Proprietary binaries remain Bayer confidential. Upstream `infographic-creator` follows AntV skill licensing; `ppt-master` remains MIT under hugohe3 — install separately.


## Publish to GitHub

Recommended: **private** repo (Bayer brand binaries stay in `brand-assets/source/` locally and are gitignored).

```bash
cd bayer-ppt-plugin
git add .
git commit -m "Bayer-ppt portable assets + install.sh"
gh repo create YOUR_ORG/bayer-ppt-plugin --private --source=. --remote=origin --push
```

Then on each host:

```bash
./scripts/install.sh --assets-dir ./brand-assets/source --kb-dir /path/to/kb
# or npx skills add YOUR_ORG/bayer-ppt-plugin
```


## Install in Claude Code (marketplace plugin)

```bash
claude plugin marketplace add picspin/bayer-ppt-plugin
claude plugin install bayer-ppt@bayer-ppt
```

`install.sh` and `npx skills add` remain supported (see above).

## v0.3.0 highlights
- Global-thesis cover with exact placeholder fit (`fit_cover_image.py`, `COVER_IMG`)
- Information-density lint, target 70–80%
- Chart-intent → Chart Pool / BC Chart Library mapping (17 intents, ≤30% same pattern)
- Mandatory `SRC_` source screenshots on cited slides
- Academic-promotion mode + slide-face lint

Proprietary Bayer templates (pptx/potx/pdf) are gitignored — drop them into `brand-assets/source/` locally. See CHANGELOG.md.
