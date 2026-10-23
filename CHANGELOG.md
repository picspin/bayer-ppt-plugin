# Changelog

## 0.3.0 — 2026-10-23
- **Cover**: derive a global deck thesis → generate/select cover schema; `scripts/fit_cover_image.py` crops to exact placeholder size (`COVER_IMG`).
- **Density**: `lint_slide_face.py` reports per-slide `dens=`; target 0.70–0.80 of content area.
- **Chart intent**: `references/chart-intent-map.md` maps 17 intents (progression, hierarchy, classification, cycle, timeline, comparison…) to Chart Pool / BC Chart Library slides; notes record `INTENT | PATTERN`; one pattern ≤30% of deck; `scripts/chart_pool_index.py`.
- **Citations**: any slide with a reference must carry an `SRC_` source screenshot; infographics/tables are supplements only.
- **Academic-promotion mode**: `references/academic-promotion-mode.md` (claim titles, compliance in notes, image on every slide, banned-word lint).
- Added `.claude-plugin/plugin.json`, GitHub Actions `plugin-validate.yml`.
