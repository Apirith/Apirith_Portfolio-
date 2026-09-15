---
title: Fallout-Inspired Smartwatch
slug: fallout-smartwatch
category: CAD
tool: SolidWorks
date: 2026-09
hero: assets/cad/fallout-smartwatch/body.png
drawing_pdf: assets/cad/fallout-smartwatch/drawing.pdf
status: draft
---

# Fallout-Inspired Smartwatch

A wrist-mounted smartwatch concept modeled in SolidWorks: a chunky, retro-industrial housing with a physical volume knob, a power button and screen, and a strap band that adjusts through a row of pin holes. The design language comes from Pip-Boy-style wearables — controls you can find by feel, and an enclosure that looks like it was machined rather than molded.

Five sheets, A-size (8.5 × 11 in) format, drawn at 2:1.

<!-- TODO (Apirith): two or three sentences in your own voice. What were you practicing — fillets,
     multi-body parts, tolerancing? What would you change on the next revision? This is the part a
     mechanical engineer reads first, and it's the only part I can't write for you. -->

## Parts

| Sheet | Component | From the drawing |
|---|---|---|
| 1 | Combined components | Assembly overview |
| 2 | Smartwatch body | 25.00 × 19.00 × 15.00 housing, R1.00 fillets throughout, 1.00 × 9.00 side slot, 14.00 slot on the underside, bore for the knob shaft |
| 3 | Strap band | 50.00 long, 19.00 wide at the head tapering to 8.00, a row of Ø1.10 adjustment holes, 20.00 clasp with a Ø3.00 pin, R0.45 end radius |
| 4 | Volume knob | Knurled grip, Ø0.40 teeth with R0.10 roots, 6.00 knob body on a Ø2.00 × 4.00 shaft, R1.00 edge |
| 5 | Power button + screen | Button and display components |

Dimensions are as drawn. **Confirm mm vs. inches before publishing** — the page currently states mm.

## Sheets

Three are live on the site: body, strap band, volume knob. Two are pending export.

| Sheet | State | Note |
|---|---|---|
| Body | Live | 640×480 — needs a 300 DPI re-export |
| Strap band | Live | 640×480 — needs a 300 DPI re-export |
| Volume knob | Live | 640×480 — needs a 300 DPI re-export |
| Combined components | Pending | Thumbnail in the source file is blank; open the sheet, let the views rebuild, then save |
| Power button + screen | Pending | Same |

The three live images came out of the preview thumbnails embedded in the `.SLDDRW` file, which is why they're small. Re-export each from SolidWorks at 300 DPI over the same filenames and the page picks them up with no code change.

## Also outstanding

- `drawing.pdf` is a placeholder. Export all five sheets as one PDF so the CAD page's main button works.
- `model.glb` is a rough stand-in. A real export of the assembly would make the 3D viewer show the actual design.
- For the scroll-linked exploded view: one transparent PNG per part from a single camera angle, or the assembly as `.glb`. The flat drawing sheets can't drive it.

See `CAD-GUIDE.md` for the export steps and the markup to paste in.
