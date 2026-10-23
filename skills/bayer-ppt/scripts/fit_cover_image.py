#!/usr/bin/env python3
"""Center-crop an image to the cover picture placeholder's aspect and insert it exactly at its bounds.
Usage: fit_cover_image.py deck.pptx image.png [--slide 1] [--out out.pptx] [--full-bleed] [--behind/--front]
- Target = first PICTURE placeholder on the slide (type 18), else largest picture shape named COVER_IMG,
  else full slide (16:9). --full-bleed forces the full slide.
- Image is cropped with Pillow (no python-pptx auto-crop/stretch), saved next to the deck, inserted at
  exact (left, top, width, height), named COVER_IMG, and moved to z-order back (behind title text) by default.
- Existing COVER_IMG shapes on that slide are replaced (never tiled)."""
import argparse, os, sys
from PIL import Image
from pptx import Presentation

def target_box(prs, slide, full):
    if not full:
        for sh in slide.placeholders:
            if sh.placeholder_format.type == 18:  # PICTURE
                return sh, (sh.left, sh.top, sh.width, sh.height)
        for sh in slide.slide_layout.placeholders:
            if sh.placeholder_format.type == 18:
                return None, (sh.left, sh.top, sh.width, sh.height)
    return None, (0, 0, prs.slide_width, prs.slide_height)

def crop_to(img, aspect):
    w, h = img.size
    if w / h > aspect:
        nw = round(h * aspect); x = (w - nw) // 2; return img.crop((x, 0, x + nw, h))
    nh = round(w / aspect); y = (h - nh) // 2; return img.crop((0, y, w, y + nh))

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("pptx"); ap.add_argument("image")
    ap.add_argument("--slide", type=int, default=1); ap.add_argument("--out")
    ap.add_argument("--full-bleed", action="store_true"); ap.add_argument("--front", action="store_true")
    a = ap.parse_args()
    prs = Presentation(a.pptx); s = prs.slides[a.slide - 1]
    ph, (l, t, w, h) = target_box(prs, s, a.full_bleed)
    for sh in list(s.shapes):
        if sh.name.startswith("COVER_IMG"): sh._element.getparent().remove(sh._element)
    img = Image.open(a.image).convert("RGB"); src = img.size
    out_img = crop_to(img, w / h)
    base = os.path.splitext(a.out or a.pptx)[0]; crop_path = base + "_cover_crop.png"; out_img.save(crop_path)
    if ph is not None:
        ph._element.getparent().remove(ph._element)  # empty placeholder would show "Click to add picture"
    pic = s.shapes.add_picture(crop_path, l, t, w, h); pic.name = "COVER_IMG"
    if not a.front:
        tree = s.shapes._spTree; tree.remove(pic._element); tree.insert(2, pic._element)
    prs.save(a.out or a.pptx)
    err = abs(out_img.size[0] / out_img.size[1] - w / h) / (w / h)
    print(f"slide={a.slide} target={'placeholder' if ph is not None else 'layout/full'} box_emu=({l},{t},{w},{h}) "
          f"aspect={w/h:.4f} src={src} crop={out_img.size} aspect_err={err:.4%} -> {a.out or a.pptx}")
    sys.exit(0 if err < 0.005 else 2)
if __name__ == "__main__": main()
