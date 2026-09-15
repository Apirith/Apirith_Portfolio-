# Working instructions

Personal portfolio for Apirith Sothea. Static site, deployed to Netlify from this folder.

Read `DESIGN-SYSTEM.md` before changing anything visual, and `SITE-STRUCTURE.md` before adding a page. `README.md` covers the stack. This file is the short version plus the rules that must not regress.

## Stack

Hand-written HTML, CSS and vanilla JS across five pages sharing `styles.css` and `script.js`. No build step, no framework, no bundler, no TypeScript, no CMS, no package.json. The only external dependencies are Google Fonts and `model-viewer`, loaded from a CDN in each page's `<head>`. Don't add libraries. If a change seems to need one, say so and ask before installing anything.

## Rules that must hold

An accessibility pass fixed all of these. Don't undo them.

1. **Blue text uses `--accent-text` (`#0a5bb8`), never `--accent` (`#0071e3`).** The bright blue measures 4.31:1 on `--surface` — under the 4.5:1 floor. Compute any new pairing; don't eyeball it.
2. **Every interactive element is at least 44px tall.** Nav links, footer links and `.button` already are.
3. **The global `:focus-visible` ring stays.** Never write `outline: none`.
4. **No state is signalled by color alone.** The current nav item carries `aria-current="page"`, a weight change and an underline bar.
5. **Technical images use `object-fit: contain`.** Never `cover` — it crops the drawing.
6. **Reduce Motion is respected.** `script.js` strips `auto-rotate` from `model-viewer`; the media query kills transitions and hover transforms. New animation gets the same treatment.
7. **`model-viewer` keeps `touch-action="pan-y"`**, or phones can't scroll past it.
8. **No `href="#"`.** Use a `.status-chip` ("Coming soon") until a real URL exists.
9. **Every page keeps** the skip link, `id="main"` on `<main>`, the favicon, and the `<noscript>` block that un-hides `.reveal`.
10. **No `localStorage`, `sessionStorage` or IndexedDB** anywhere.
11. **Colors come from `:root` tokens.** No hex values in rules.
12. **Header and footer nav are identical across all five pages.** Change one, change all five.

## How to work here

Prefer an existing class to a new one; prefer a token to a value. When new CSS is genuinely needed, put it in the section of `styles.css` where it belongs rather than appending to the bottom.

Copy is first person and plain. Button labels are verbs that say what happens — "See the CAD work", not "Explore". A link that opens a new tab says so in its label. Sentence case for headings.

Never describe unfinished work as finished. A missing export gets a pending state and plain words, not a placeholder graphic dressed up to look like the real thing. This matters most on the CAD page, where the subject is real drawings.

Before pushing, run the checklist at the end of `DESIGN-SYSTEM.md`: check 390px and 1280px, tab through for focus, confirm no horizontal scroll.

## Current state

Working: all five pages, shared nav and footer, the 3D smartwatch viewer on Home and CAD, three real drawing sheets on the CAD page, the accessibility floor described above, and dark mode (`prefers-color-scheme`, no in-app toggle — see `DESIGN-SYSTEM.md § 2`).

Gaps, in priority order — `NEXT-STEPS.md` has the full list:

1. **No contact details anywhere.** No email, LinkedIn, GitHub or resume link. The biggest gap for a portfolio aimed at hiring. Needs Apirith's decision on what to list, then a footer block on all five pages.
2. **`assets/cad/fallout-smartwatch/drawing.pdf` is a 637-byte placeholder**, so the CAD page's main button leads nowhere.
3. **Two sheets were never exported** — "Combined components" and "Power button + screen" show a pending state.
4. **The three sheet PNGs are 640×480**, pulled from thumbnails inside the `.SLDDRW`. They need 300 DPI re-exports over the same filenames.
5. **Smartwatch units unconfirmed** — the CAD page says mm.
6. **Music page has no tracks.**
7. **About page has a photo placeholder** and doesn't yet tell the Dana story that was meant to anchor it.
8. **`model.glb` is a rough stand-in** for the real assembly.

The scroll-linked exploded-view interaction from the original brief isn't built. It needs per-part exports from the assembly, or a placeholder-shape prototype first.

## Asking before assuming

Some of these gaps need information only Apirith has: what contact details to publish, which units the drawings use, which tracks to feature. Don't invent those. Ask, or leave a pending state and say what's needed.
