# Proprietary brand sources (gitignored)

Place Bayer-internal binaries here. They are **not** published with this package.

| Expected file | Description |
|---------------|-------------|
| `icon-language.potx` | Bayer in Radiology Icon Library — **primary slide master** for Radiology/Centargo |
| `official-template.pptx` | Bayer 16:9 Chart Pool (Updated) |
| `structured-graphics.pptx` | BC Chart Library |
| `color-system.pdf` | Bayer Color Guide |

## Drop-in steps

1. Obtain the files from your internal brand / Veeva / content factory channel.
2. Copy them into this directory with the names above.
3. For python-pptx, create a **working master** PPTX from `icon-language.potx` (content-type patch as needed) under `exports/` or your project folder — keep exports gitignored.
4. Confirm `brand-kit/` markdown specs match the dropped-in versions; update digests if your legal copies differ.

Do **not** commit PPTX/POTX/PDF binaries to a public fork.
