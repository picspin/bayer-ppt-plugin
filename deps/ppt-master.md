# Peer dependency: ppt-master

Bayer-ppt does **not** vendor [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) (large repo with binaries, docs, and tooling).

## Install

```bash
npx skills add hugohe3/ppt-master
```

Upstream: https://github.com/hugohe3/ppt-master

## Python environment

ppt-master expects a Python venv with its `requirements.txt` (includes `python-pptx` and related tooling).

Example (adjust to your install path):

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r <ppt-master-repo>/requirements.txt
```

**Local Grok Bot install example:** `/home/box/tools/ppt-master/` with `.venv` under that tree.

## When to use

| Need | Skill |
|------|--------|
| Bayer brand rules, Centargo master chrome, palette | `bayer-ppt` (this package) |
| Infographics / AntV DSL | `infographic-creator` (vendored here) |
| Native PPTX generate / edit / beautify / template routes | **ppt-master** (peer) via `ppt-master-bridge` |

## Agent note

After install, set `SKILL_DIR` to the absolute directory of the installed ppt-master skill and follow its `SKILL.md` load order (attribution guard → routing → selected profile). Bayer constraints from `brand-kit/` always override invented colors/layouts.
