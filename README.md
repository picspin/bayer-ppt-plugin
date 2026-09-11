# bayer-ppt-plugin

Cursor / Claude–compatible **skills marketplace** package for Bayer-branded PowerPoint workflows.

Bundles:

| Skill | Role |
|-------|------|
| `skills/bayer-ppt` | Brand rules, Centargo/Radiology master backbone, palette & precedence |
| `skills/infographic-creator` | Vendored AntV Infographic skill |
| `skills/ppt-master` | Thin wrapper → install peer `hugohe3/ppt-master` (not vendored) |
| `skills/ppt-master-bridge` | When native PPTX is needed, ensure ppt-master + follow its SKILL.md |

Derived specs live in `brand-kit/` (markdown + `THEME.json`). Proprietary POTX/PPTX/PDF binaries are **not** shipped — drop them into `brand-assets/source/`.

---

## Install · 安装

```bash
npx skills add YOUR_ORG/bayer-ppt-plugin
# e.g. after publish: npx skills add <your-org>/bayer-ppt-plugin
```

Claude Code / Cursor marketplace: this repo’s `.claude-plugin/marketplace.json` registers plugin **`bayer-ppt`** with the skills listed above.

### Peer dependencies · 对等依赖

1. **ppt-master** (native PPTX routes) — **not** included (~900MB upstream):

   ```bash
   npx skills add hugohe3/ppt-master
   ```

   See [`deps/ppt-master.md`](deps/ppt-master.md).

2. **Python venv** — `python-pptx` and ppt-master `requirements.txt` for compose/edit.

3. **AntV Infographic CDN / runtime** — required when rendering `infographic-creator` output ([AntV Infographic](https://infographic.antv.vision/)).

---

## Private assets drop-in · 私有素材放置

```text
brand-assets/source/
  icon-language.potx          # Radiology Icon Library (slide master)
  official-template.pptx      # Chart Pool
  structured-graphics.pptx    # BC Chart Library
  color-system.pdf            # Color Guide
```

Instructions: [`brand-assets/source/README.md`](brand-assets/source/README.md). These paths are gitignored.

**Working master (python-pptx):** convert/patch `icon-language.potx` → a local `exports/bayer-radiology-master.pptx` (gitignored). Do not commit binaries.

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
brand-kit/          # derived specs + outline SVG examples
brand-assets/source/# proprietary drop-in (gitignored)
deps/ppt-master.md
examples/centargo-hospital-visits/  # fictionalized sample brief
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
git init
git add .
git commit -m "Initial Bayer-ppt plugin package"
gh repo create YOUR_ORG/bayer-ppt-plugin --private --source=. --remote=origin --push
```

Then install in any agent:

```bash
npx skills add YOUR_ORG/bayer-ppt-plugin
# peer
npx skills add hugohe3/ppt-master
pip install -r "$(dirname $(find ~/.agents -name svg_to_pptx.py 2>/dev/null | head -1))/../../requirements.txt"  # or follow deps/ppt-master.md
```

Copy proprietary POTX/PPTX/PDF into `brand-assets/source/` on each machine that authors decks.
