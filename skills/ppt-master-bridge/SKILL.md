---
name: ppt-master-bridge
description: >-
  Bridge between Bayer-ppt brand rules and the peer ppt-master skill. Use when
  Bayer / Radiology / Centargo decks need native editable PPTX generation or
  edit routes via ppt-master.
---
# ppt-master bridge (Bayer)

When Bayer decks need **native PPTX** (generate / edit / beautify / template-fill via ppt-master):

1. **Ensure ppt-master + venv are installed**
   Prefer the one-shot installer (creates `.venv`, optional vendor clone, AntV runtime, `.bayer-ppt.env`):
   ```bash
   ./scripts/install.sh
   # or skip peers you already have:
   ./scripts/install.sh --skip-antv-runtime
   ```
   Manual peer install:
   ```bash
   npx skills add hugohe3/ppt-master
   ```
   Details: [`deps/ppt-master.md`](../../deps/ppt-master.md).

   After `install.sh`, ppt-master may live at:
   - npx/skills path under `~/.agents` / `~/.claude` / `~/.cursor`, or
   - `${REPO_ROOT}/vendor/ppt-master` (git clone fallback),
   - recorded in `brand-assets/config.json` → `pptMasterRoot` and `.bayer-ppt.env`.

2. **Follow upstream SKILL.md at the installed location**
   - Retain host `SKILL_DIR` for the installed ppt-master skill.
   - Do **not** use this bridge file as a substitute for ppt-master routing, attribution guard, or profile docs.

3. **Apply Bayer brand constraints on top**
   - Load [`skills/bayer-ppt/SKILL.md`](../bayer-ppt/SKILL.md).
   - Brand kit: `${REPO_ROOT}/brand-kit/` (THEME, DIGEST, patterns, `assets.manifest.json`).
   - Resolve proprietary masters via `scripts/resolve_assets.py` (prefer `BAYER_KB_ROOT` / `BAYER_ASSETS_ROOT` when set) — id `icon-library-potx` for Radiology/Centargo chrome.
   - Prefer **MEDRAD Centargo** layouts for Centargo decks (title / text-with-logo) — do not invent blank chrome.

4. **Runtime**
   - Use the venv from `install.sh` (`brand-assets/config.json` → `venvPython`, or `${REPO_ROOT}/.venv`).
   - Working master: `python3 scripts/resolve_assets.py --prepare-master` → `exports/bayer-radiology-master.pptx` (gitignored).

If ppt-master is missing, stop native PPTX routes and tell the operator to run `./scripts/install.sh` or install the peer skill; you may still draft outlines, brand-compliant structure, and AntV infographics via `infographic-creator`.
