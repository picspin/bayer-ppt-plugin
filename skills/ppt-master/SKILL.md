---
name: ppt-master
description: >-
  Thin pointer to the upstream ppt-master skill (hugohe3/ppt-master). This package
  does NOT vendor the full ~900MB ppt-master tree. Install the peer skill, then
  follow its SKILL.md at the installed location.
---
# ppt-master (peer wrapper)

This directory is a **thin wrapper**, not a full copy of [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master).

## Install (required for native PPTX routes)

```bash
npx skills add hugohe3/ppt-master
```

Or treat ppt-master as a **peer dependency** of Bayer-ppt workflows. See [`deps/ppt-master.md`](../../deps/ppt-master.md).

## After install

1. Locate the installed skill directory (host-provided `SKILL_DIR` containing `skills/ppt-master/SKILL.md` or the marketplace install path).
2. Read and follow **that** upstream `SKILL.md` — routing, attribution guard, and profiles live there.
3. For Bayer-branded decks, also load `skills/bayer-ppt` and `skills/ppt-master-bridge` in this repo so brand kit + MEDRAD Centargo master rules apply.

Do not search the web or invent ppt-master procedures here; the upstream skill is authoritative once installed.
