# Cover and Density Rules

Applies to every deck built with the Bayer-ppt skill. Palette: Color Guide 12 hues, body text Dark Blue `#10384F`. Chart Pool numbers are 1-based.

## Cover procedure (global-understanding cover)

The cover is built last, after all slide titles exist. It must reflect the whole deck, not slide 2.

### 1. Build the deck thesis
1. List every slide's assertion title in order (number, title).
2. Summarise them into **one sentence**, the deck thesis. It must contain a claim, not a topic.
3. Extract **3 key visual motifs**: concrete, drawable nouns or shapes (e.g. "molecule network", "circular pathway", "radiology scan").
4. Do not use the cover to introduce content that appears nowhere in the deck.

### 2. Choose a route

**Route A: generated image**
- Use the `image-gen-router` skill.
- Primary: MGA, `mga_image.py -a 16:9 -q high`.
- Fallback order: Kie, then Gemini.
- Prompt template:
  ```
  Flat corporate illustration, Bayer color palette (Dark Blue #10384F + Color Guide hues),
  motifs: <motif1>, <motif2>, <motif3>. Clean vector look, soft geometry.
  No text, no logos, no people faces. Keep the <left/top> third as calm negative space
  where the title placeholder sits.
  ```
- Reject outputs with text artifacts, logos, faces, or off-palette colors; regenerate.

**Route B: global cover schema**
- Pick a schema from Chart Pool or Icon Library and render it as **one composition**:
  - circular shapes, CP 139-165
  - connected spheres, CP 27-40
  - Radiology outline icons (Icon Library)
- Recolor to the Bayer palette only. Do not mix more than one schema family.
- Group the composition and leave the title region free.

### 3. Fit into the deck
```
python scripts/fit_cover_image.py deck.pptx cover.png --slide 1
```
- The script center-crops the image to the picture placeholder aspect, or to full-slide 16:9 if there is no placeholder.
- It inserts the image exactly at the placeholder bounds, names the shape `COVER_IMG`, and sends it behind the text.
- **Never** tile, stretch, or rely on python-pptx auto-crop (it squashes the image).
- Route B compositions are exported to PNG first, then fitted the same way.

### 4. Verify render
Render slide 1 to an image and check all four:
- [ ] Title is legible (contrast against the image, no overlap with busy areas)
- [ ] Logo is visible
- [ ] No letterbox bars or stretched pixels
- [ ] `COVER_IMG` is behind all text shapes

### Record in speaker notes
```
COVER: thesis=<one sentence> | route=A/B | prompt=<prompt or schema ids>
```

## Density 70-80%

### Definition
- **Safe area** = slide minus 0.5 in left/right margins, minus the top title band (top 1.3 in), minus the bottom footer band (0.6 in). On 13.333 × 7.5 in this is 12.333 × 5.6 in.
- **Visible content shapes** are:
  - text boxes containing text
  - pictures
  - charts
  - tables
  - groups
  - autoshapes with fill
- **Density** = union area of visible content shapes, clipped to the safe area, divided by the safe area. Measure it on a **40 × 24 grid**: a cell counts as covered if its center lies inside any content shape.
- Overlaps count once (union).
- Empty placeholders, lines, and invisible shapes do not count.

### Excluded slides
Cover, section dividers, agenda, references, and closing slides are excluded. They are auto-detected by layout name or title keywords (e.g. Agenda, Contents, References, Thank you, Section). To exclude any other slide, add this to its notes:
```
DENSITY: skip
```

### Target: 0.70-0.80

| Result | Fix |
|---|---|
| **< 0.70** | Enlarge the hero visual. Add a source crop (`SRC_`). Add a KPI chip strip. **Do not** add more text. |
| **> 0.80** | Cut text. Move detail to speaker notes. Split the slide. Widen gutters. |

### Whitespace rule
Whitespace consists of **gutters (≥ 0.2 in) between blocks** and the margins. An empty quadrant or half-empty slide is a defect even if the overall density number passes. Check that no 2 × 2 block of grid quadrants is uncovered.

## Cited-content rule

Any slide that cites a source must show the cited material itself. Triggers include:
- arXiv, doi, PMID, "et al."
- bracket citations like [n]
- "Fig. N" or "Table N" of a paper
- 文献

### Requirements
1. At least **one screenshot or crop** of the cited figure, table, or page region.
2. Shape name prefix **`SRC_`**, e.g. `SRC_h2_fig1`.
3. A caption text box **directly below** the crop, in this format:
   ```
   Source: Author Year, Venue, Fig. N / Table N, license (CC BY 4.0)
   ```
4. Infographics or tables that we redraw are **supplementary, never a substitute** for the source crop.

### Image handling
```
pdftoppm -r 200 -f <page> -l <page> -png paper.pdf page
```
Then crop the figure region from `page-<n>.png`.
- Resolution must be ≥ 150 dpi at the placed size.
- Keep the original aspect ratio (no stretch).
- Do not recolor the figure.
- If the license does not allow reuse, state that in the caption and link to the original instead of embedding. Flag this to the user.

### Lint
The lint script checks, for each citing slide:
- a shape named `SRC_*` exists
- a caption box sits directly below it and starts with `Source:`
- effective dpi is ≥ 150

A slide that fails any check is a lint error and blocks delivery.