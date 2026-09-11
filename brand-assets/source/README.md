# Proprietary brand sources (gitignored)

Place Bayer-internal binaries here. They are **not** published with this package.

| Expected file | Manifest id | Description |
|---------------|-------------|-------------|
| `icon-language.potx` | `icon-library-potx` | Bayer in Radiology Icon Library — **primary slide master** for Radiology/Centargo |
| `official-template.pptx` | `chart-pool` | Bayer 16:9 Chart Pool (Updated) |
| `structured-graphics.pptx` | `bc-chart-library` | BC Chart Library |
| `color-system.pdf` | `color-guide` | Bayer Color Guide |

Aliases (KB basename match) include e.g. `ALL.AA.Illustrative_Elements.Icon_Library_Overview.potx` → `icon-library-potx`. See `brand-kit/assets.manifest.json`.

## Drop-in steps

1. Obtain the files from your internal brand / Veeva / content factory channel **or** point `BAYER_KB_ROOT` at a synced knowledge-base tree.
2. Copy them into this directory with the names above, **or** set `--assets-dir` / `BAYER_ASSETS_ROOT` during `./scripts/install.sh`.
3. For python-pptx, run:
   ```bash
   python3 scripts/resolve_assets.py --prepare-master
   ```
   This copies the resolved POTX to `exports/bayer-radiology-master.pptx` and patches content-type template→presentation when needed.
4. Confirm `brand-kit/` markdown specs match the dropped-in versions; update digests if your legal copies differ.

Do **not** commit PPTX/POTX/PDF binaries to a public fork. Prefer KB resolution on shared hosts so binaries never need to live in the git clone.
