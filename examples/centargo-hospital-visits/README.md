# Example: Centargo hospital-visit update (fictionalized)

**Status:** scrubbed sample brief for agent testing — **not** a real operational report.  
Do not commit real hospital visit PPTX files with confidential volumes, colleague performance notes, or internal CRM detail.

## Goal

Produce a short **4-slide** internal Centargo update using:

- Slide master: Radiology Icon Library POTX → working `bayer-radiology-master.pptx`
- Title layout: `MEDRAD Centargo Title Slide 3`
- Content layouts: `MEDRAD Centargo Text Slide with logo`
- Palette: Dark Blue `#10384F`, Bayer Blue `#0091DF`, Bright Blue `#00BCFF`, sparingly MEDRAD `#E46C0A`
- Outline icons from `brand-kit/icons/examples/` (or full library after drop-in)

## Fictional brief (safe for publish)

**Audience:** Bayer Radiology internal team  
**Product:** MEDRAD Centargo  
**Story:** Quarterly touchpoint summary across three fictional sites in “Coastal Metro”

| Slide | Intent (fictional) |
|-------|--------------------|
| 1 Title | Centargo Q-update · three-site snapshot (volume band · status · focus) |
| 2 Site A — “Harbor General” | High CT volume; protocol complexity → research-support entry narrative |
| 3 Site B — “Metro First Imaging” | Pain → opportunity → action (training / Smart Protocol / dual-flow) |
| 4 Site C + next steps | Pending visit + 2×2 follow-up matrix + numbered overall next actions |

Use **placeholder hospital names** as above (or other clearly fictional names). Keep metrics qualitative (“high volume”, “protocol friction”) unless the operator supplies sanctioned numbers in a private workspace.

## Rebuild pattern (no sensitive PPTX in repo)

1. Drop proprietary `icon-language.potx` into `brand-assets/source/`.
2. Build a python-pptx–compatible working master under `exports/` (gitignored).
3. Run a project-local builder script (not shipped here), e.g.:

```bash
# pattern only — implement in your private workspace
source .venv/bin/activate
python build_deck_on_master.py \
  --master exports/bayer-radiology-master.pptx \
  --out exports/centargo-hospital-visits-fictional.pptx
```

4. Prefer **native shapes + outline SVGs** over flattened bitmaps; preserve layout logo chrome.

## Agent checklist

- [ ] `bayer-ppt` skill loaded; `THEME.json` read
- [ ] Centargo layouts used (not blank slides)
- [ ] ppt-master installed if native generate/edit routes are used
- [ ] No real PII / colleague performance narratives in committed examples
