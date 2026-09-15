# Putting CAD Work on the Site

A browser can't open `.SLDDRW`, `.SLDPRT` or `.SLDASM`. Every CAD project reaches the site as exported images, a PDF, and words. This is the whole workflow.

## 1. Export from SolidWorks

| What | How | Used for |
|---|---|---|
| **Sheet images** | Open the drawing → File → Save As → PNG. In *Options*, set 300 DPI. Save one sheet at a time if "All sheets" isn't offered | The gallery on the CAD page |
| **Full drawing set** | File → Save As → PDF, with "All sheets" checked | The "View full drawing" button |
| **Hero render** | Open the part or assembly → isometric view → File → Save As → PNG, white or transparent background | Card thumbnails |
| **Exploded steps** *(assemblies)* | ConfigurationManager → Exploded View → capture each step | The scroll-explode interaction, if it gets built |
| **3D model** *(optional)* | Save As `.stl` or `.step`, then Blender → Import, then File → Export → glTF 2.0 (`.glb`) | The interactive viewer |

Source `.SLD*` files stay out of the repo. They're large, and nobody visiting the site can open them.

A drawing exported as PNG keeps its border and title block. That's wanted — it's what makes it read as a drawing rather than a picture. For a card thumbnail, use a clean model render instead.

## 2. Put the files where they belong

```
assets/cad/<project-slug>/
├── hero.png              card thumbnail
├── <sheet-name>.png      one per drawing sheet, 300 DPI
├── drawing.pdf           the full set
└── model.glb             optional
```

Lowercase, hyphens, no spaces: `wrist-band.png`, never `Wrist Band.PNG`.

## 3. Write it up

Create `projects/cad/<slug>.md` — frontmatter, the story in a few sentences, a table of parts with real dimensions, then the sheet list. Use `fallout-smartwatch.md` as the model.

Write about decisions, not features. "The knurl started at 0.6mm and was too coarse to grip at this scale" is worth more than "features a knurled knob." If a dimension is on the drawing, name it; a number that came from somewhere real is the thing a mechanical engineer reading this page is looking for.

## 4. Put it on the page

A sheet with a real export:

```html
<figure class="reveal">
  <img
    src="assets/cad/<slug>/<sheet>.png"
    alt="Drawing sheet for the <part>: <what the views show, with real dimensions>."
    loading="lazy"
  />
  <figcaption>
    <span><Sheet name></span>
    <a href="assets/cad/<slug>/<sheet>.png" target="_blank" rel="noopener noreferrer">Open full size ↗</a>
  </figcaption>
</figure>
```

A sheet that isn't exported yet:

```html
<figure class="reveal">
  <div class="sheet-placeholder">Sheet export pending</div>
  <figcaption>
    <span><Sheet name></span>
    <span class="status-chip">Coming soon</span>
  </figcaption>
</figure>
```

Say what's missing. Don't fill the gap with a drawn-looking placeholder — a fake drawing on a page whose subject is real drawings costs more credibility than an empty slot.

The 3D viewer, when there's a `.glb`:

```html
<model-viewer
  src="assets/cad/<slug>/model.glb"
  alt="Interactive 3D model of the <thing>"
  camera-controls
  touch-action="pan-y"
  auto-rotate
  interaction-prompt="none"
  shadow-intensity="1"
  environment-image="neutral"
></model-viewer>
<p class="hero-viewer-hint">Drag to rotate · scroll the page as normal</p>
```

`touch-action="pan-y"` is not optional — without it the viewer swallows vertical drags and the page can't be scrolled past on a phone. The hint line is what tells people it's interactive at all, now that the built-in prompt is off.

## 5. Rules for this page type

- Drawing images use `object-fit: contain`. `cover` crops the title block off, which is the part that says whose drawing it is.
- Alt text describes the drawing, not the file: views shown and real dimensions. A screen reader user should get what a sighted visitor gets from a glance.
- The spec strip carries real values from the drawing only.
- Every "Open full size" link opens a real file.
- Long dimension strings use JetBrains Mono; nothing else on the page does.

## Checklist for a new project

1. Export sheets at 300 DPI, the PDF, and a hero render
2. Drop them in `assets/cad/<slug>/`
3. Write `projects/cad/<slug>.md`
4. Add the figures to `cad.html`, with a spec strip if there are numbers worth pulling out
5. Add or update the card on `index.html`
6. Run the checklist at the end of `DESIGN-SYSTEM.md`, then push
