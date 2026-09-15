# Site Structure

## The shape

Five pages, flat. No page is more than one click from any other, because the same five links sit in the header and footer everywhere.

| Page | File | Job |
|---|---|---|
| Home | `index.html` | Say who he is, show the one thing worth seeing, point at the three lanes |
| About | `about.html` | The longer story and the through-line between the lanes |
| CAD | `cad.html` | SolidWorks work, growing over time |
| AI | `ai.html` | Shipped AI and product work |
| Music | `music.html` | Tracks, remixes, and the YouTube channel |

Flat beats nested here. There isn't enough work yet for a category page to need sub-pages, and a person landing from a résumé link should be able to see everything without learning a hierarchy first.

### Why pages instead of one long scroll

The earlier plan was a single narrative scroll. Category pages won because CAD is meant to accumulate: a scroll has room for one flagship project, while a page has room for a gallery that grows without restructuring anything. The narrative survives on the home page in condensed form — three teasers, one per lane, each linking onward.

## Navigation

`Apirith Sothea · Home · About · CAD · AI · Music`

- Identical markup in every page's header and footer. If you change one, change all five.
- The current page is marked with `aria-current="page"`, which drives the color, weight and underline bar. There is no `.active` class.
- The header is sticky, so in-page anchors need `scroll-margin-top` — already set globally on `[id]`.
- Each link is a 44px-tall pill. On phones the header stacks to brand over nav, still one row of five.

## Files

```
Portfolio/
├── index.html · about.html · cad.html · ai.html · music.html
├── styles.css            Tokens in :root, then sections in page order
├── script.js             Year, scroll reveal, Reduce Motion
├── netlify.toml          publish = "files"
├── assets/
│   └── cad/
│       └── fallout-smartwatch/
│           ├── body.png · wrist-band.png · volume-knob.png
│           ├── drawing.pdf
│           └── model.glb
├── projects/
│   └── cad/
│       └── fallout-smartwatch.md
└── scripts/              Python helpers, not part of the site
```

Asset paths are `assets/<category>/<project-slug>/<file>`. Writeups are `projects/<category>/<slug>.md`. Slugs and filenames are lowercase with hyphens — Netlify serves case-sensitively, so `Body.PNG` works on Windows and 404s in production.

Files referenced by a page must be relative with no leading slash (`assets/cad/...`, not `/assets/cad/...`).

## Anatomy of a page

Every page is the same five parts in the same order:

1. `<head>` — title as `Section | Apirith Sothea`, meta description, font links, `styles.css`, favicon, `<noscript>` block
2. Skip link, then the header and nav
3. `<main id="main">` — an intro section (`.eyebrow`, `h1`, `.lede`), then content sections alternating `.section` and `.section.muted-section`
4. Footer — year and the five links
5. `script.js`

## Adding a page

1. Copy `about.html`, the plainest page, and change the title, meta description and `aria-current`.
2. Add the link to the header **and** footer of all five existing pages, plus the new one.
3. Use existing classes from `DESIGN-SYSTEM.md`. Add CSS only when nothing fits, and put the new rule in the section of `styles.css` where it belongs rather than at the bottom.
4. Run the checklist at the end of `DESIGN-SYSTEM.md`.

Six top-level items is about the ceiling for a nav this shape. Past that, group before adding.
