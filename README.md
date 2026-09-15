# apirithportfolio

Personal portfolio for Apirith Sothea — mechanical design, AI products, and music. Live at [apirithportfolio.netlify.app](https://apirithportfolio.netlify.app).

## Running it

There's no build step. Open `index.html` in a browser, or serve the folder so the 3D model and fonts load over HTTP:

```
python -m http.server 8000
```

Then visit `http://localhost:8000`.

## Deploying

Netlify watches this folder (`netlify.toml`). Commit and push, and the site rebuilds itself. There's nothing to run first.

## What's here

```
index.html          Home — intro, 3D smartwatch, three project cards
about.html          About
cad.html            SolidWorks work
ai.html             AI projects
music.html          Music and YouTube
styles.css          All styling. Tokens live at the top in :root
script.js           Footer year, scroll reveals, Reduce Motion handling
assets/             Images, models, PDFs, by category and project slug
projects/           Markdown writeups — the source copy for each project
scripts/            One-off Python helpers for generating placeholder assets
```

## The documents

| File | What it's for |
|---|---|
| `DESIGN-SYSTEM.md` | Color, type, spacing, components, motion, and the accessibility floor |
| `SITE-STRUCTURE.md` | Pages, navigation, file layout, and how to add a page |
| `CAD-GUIDE.md` | Getting SolidWorks work onto the site |
| `NEXT-STEPS.md` | What's done, what's blocked, what's next |
| `CLAUDE.md` | Working instructions for Claude Code sessions in this folder |

## Stack, and why

Hand-written HTML, CSS and vanilla JavaScript. No framework, no bundler, no CMS, no TypeScript.

The site is five pages of mostly static content with one custom interaction. A build step would add a thing to maintain and break, and would buy nothing. The only external dependencies are Google Fonts and `model-viewer` for the 3D model, both loaded from a CDN in each page's `<head>`.

If a change seems to need a package, it probably doesn't.
