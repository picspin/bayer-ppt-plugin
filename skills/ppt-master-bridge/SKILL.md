---
name: ppt-master-bridge
description: >-
  Bridge between Bayer-ppt brand rules and the peer ppt-master skill. Use when
  Bayer / Radiology / Centargo decks need native editable PPTX generation or
  edit routes via ppt-master.
---
# ppt-master bridge (Bayer)

When Bayer decks need **native PPTX** (generate / edit / beautify / template-fill via ppt-master):

1. **Ensure ppt-master is installed**
   ```bash
   npx skills add hugohe3/ppt-master
   ```
   Details: [`deps/ppt-master.md`](../../deps/ppt-master.md).

2. **Follow upstream SKILL.md at the installed location**
   - Retain host `SKILL_DIR` for the installed ppt-master skill.
   - Do **not** use this bridge file as a substitute for ppt-master routing, attribution guard, or profile docs.

3. **Apply Bayer brand constraints on top**
   - Load [`skills/bayer-ppt/SKILL.md`](../bayer-ppt/SKILL.md).
   - Brand kit: `${REPO_ROOT}/brand-kit/` (THEME, DIGEST, patterns).
   - Proprietary masters: `${REPO_ROOT}/brand-assets/source/icon-language.potx` (Radiology/Centargo chrome).
   - Prefer **MEDRAD Centargo** layouts for Centargo decks (title / text-with-logo) — do not invent blank chrome.

4. **Runtime**
   - python-pptx / ppt-master usually expect a project `.venv` with dependencies from ppt-master `requirements.txt`.
   - Working master conversion note: POTX → patched PPTX working copy under `exports/` or project dir (gitignored).

If ppt-master is missing, stop native PPTX routes and tell the operator to install the peer skill; you may still draft outlines, brand-compliant structure, and AntV infographics via `infographic-creator`.
