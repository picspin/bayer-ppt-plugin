# brand-assets

Local drop-in and install-time configuration for **proprietary** Bayer binaries.

This package does **not** ship POTX/PPTX/PDF brand files. Agents resolve them via
`brand-kit/assets.manifest.json` and `scripts/resolve_assets.py`.

## Local vs knowledge base

| Source | Env | Typical use |
|--------|-----|-------------|
| **Local disk** | `BAYER_ASSETS_ROOT` or files under `brand-assets/source/` | Laptop / CI cache with renamed drop-ins |
| **Knowledge base** | `BAYER_KB_ROOT` | Synced drive, SharePoint mount, Notion export — recursive basename/alias match |
| **Per-asset override** | `BAYER_ASSET_<ID>` | Exact path for one file (highest priority) |

Search order (first hit wins): env override → `BAYER_ASSETS_ROOT` → `BAYER_KB_ROOT` → `${REPO_ROOT}/<rel>` → `BAYER_ASSET_PATH`.

## Files

| Path | Role |
|------|------|
| `source/` | Conventional drop-in directory (gitignored binaries) |
| `source/README.md` | Expected filenames |
| `config.json` | Written by `scripts/install.sh` (gitignored) — `assetsRoot`, `kbRoot`, `pptMasterRoot`, `venvPython` |

## Commands

```bash
python3 scripts/resolve_assets.py --check
python3 scripts/resolve_assets.py --get icon-library-potx
python3 scripts/resolve_assets.py --prepare-master   # → exports/bayer-radiology-master.pptx
```

When proprietary sources are missing, use `brand-kit/` markdown + `THEME.json` only and state that binaries were not resolved.
