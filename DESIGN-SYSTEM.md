# Design System

The rules that make every page of this site look like one site. Everything here is implemented in `styles.css` — this document is the reasoning, the file is the source of truth. If the two disagree, fix one of them.

Contrast ratios below are computed from the actual hex values against the actual background, not estimated. Apple's floor is 4.5:1 for text under 17pt and 3:1 for text at 18pt or larger or bold (`accessibility.md › Vision`); this system aims higher so there's room to move a color without falling through the floor.

## 1. Principles

Four decisions that everything else follows from.

**The work is the interface.** A drawing sheet, a 3D model, a track — those are what someone came for. Chrome stays quiet so they read as the loud thing. Apple's version: "branding defers to content" (`branding.md`).

**One accent, spent carefully.** Blue marks what's interactive and the current location. It never fills a large area and never decorates. `color.md › Best practices`: "Avoid using the same color to mean different things."

**Hierarchy comes from size, weight and space** — not from color blocks, borders or rules. `typography.md › Conveying hierarchy`: "Adjust font weight, size, and color as needed to emphasize important information."

**Nothing is conveyed by color alone.** Every state carries a second cue: weight, an underline, a shape, a word.

## 2. Color

Defined once in `:root` in `styles.css`. Never hard-code a hex value in a rule.

### Light (default)

| Token | Value | Role | Contrast |
|---|---|---|---|
| `--bg` | `#ffffff` | Page ground | — |
| `--surface` | `#f5f5f7` | Alternating sections, cards | — |
| `--surface-2` | `#fbfbfd` | Inset panels inside a card | — |
| `--border` | `#d2d2d7` | Dividers, card outlines | 1.5:1 — non-text only |
| `--text` | `#1d1d1f` | Headings, body | 16.8:1 on white |
| `--muted` | `#6e6e73` | Captions, metadata, secondary prose | 5.07:1 on white, 4.66:1 on `--surface` |
| `--accent` | `#0071e3` | Non-text marks only: bullets, rules, fills | 4.7:1 on white — below floor on tinted grounds |
| `--accent-text` | `#0a5bb8` | Every blue **word**: links, eyebrows, tags, active nav | 6.56:1 white · 6.02:1 surface · 5.72:1 accent-soft |
| `--accent-soft` | `#e8f0fe` | Tag pill grounds | — |
| `--header-bg` | `rgba(255, 255, 255, 0.8)` | Sticky header ground, blurred | — |
| `--header-border` | `rgba(0, 0, 0, 0.06)` | Header bottom hairline | non-text only |

The `--accent` / `--accent-text` split is the one non-obvious rule here, and it exists because `#0071e3` measures 4.31:1 on `--surface` and 4.10:1 on `--accent-soft` — both under the 4.5:1 minimum. Bright blue for marks, dark blue for words.

### Dark (built)

Apple asks for both appearances with no in-app toggle (`dark-mode.md › Best practices`: "Avoid offering an app-specific appearance setting"), and 7:1 for small text where possible. These values clear 7:1 everywhere text is required to. Implemented inside `@media (prefers-color-scheme: dark)` in `styles.css`, redefining `:root` tokens only — there's exactly one rule outside the token block that changes (the drawing-sheet dimming noted below), everything else in the stylesheet is unchanged and just inherits the new token values. There is no in-app toggle; the OS setting is the only control.

| Token | Value | Contrast |
|---|---|---|
| `--bg` | `#101114` | — |
| `--surface` | `#191b1f` | — |
| `--surface-2` | `#1c1f24` | Inset panels inside a card. `--muted` on it: 6.84:1 |
| `--border` | `#2c2f35` | non-text only |
| `--text` | `#f2f3f5` | 17.0:1 on bg · 15.5:1 on surface |
| `--muted` | `#a2a7b0` | 7.81:1 on bg · 7.14:1 on surface |
| `--accent` | `#4da3ff` | marks only |
| `--accent-text` | `#6fb6ff` | 8.82:1 on bg · 8.06:1 on surface · 7.28:1 on accent-soft |
| `--accent-soft` | `#16243a` | — |
| `--header-bg` | `rgba(16, 17, 20, 0.72)` | Sticky header ground, blurred |
| `--header-border` | `rgba(255, 255, 255, 0.08)` | Header bottom hairline |
| `--shadow` | `rgba(0, 0, 0, 0.5)` | Card hover shadows read against dark surfaces |

Two tokens are deliberately constant across both appearances, because they belong to elements that are already dark (or already light) regardless of OS setting, and re-tinting them would fight their own content:

- `--dark-bg`, `--dark-surface`, `--dark-text`, `--dark-muted` — the home hero (`.dark-section`) is dark in both appearances already, so it carries its own fixed palette rather than reading from `--bg`/`--text`.
- `--thumb-ink` (`#1d1d1f`) — the CAD/AI/Music thumbnail tiles on the home page are light material-swatch gradients in both appearances, so their label text stays the fixed dark ink rather than following `--text` (which would otherwise go near-white and vanish against the still-light tile).

The home hero was already dark in both appearances, so it needed no dark variant — but the drawing sheet PNGs are white-ground images and would glow at full brightness on a dark page. They're dimmed with `filter: brightness(.92)` inside the same dark-mode media query, per `dark-mode.md › Dark Mode colors`: "Soften the color of white backgrounds." The sheets keep their white paper ground rather than being recolored — a technical drawing that's been retinted is a falsified drawing.

## 3. Typography

Manrope carries everything. JetBrains Mono is reserved for CAD dimensions and sheet captions, where a technical-drawing voice is true to the content rather than decorative. Two faces is the limit — `typography.md › Conveying hierarchy`: "Minimize the number of typefaces you use."

| Role | Size | Weight | Notes |
|---|---|---|---|
| Hero title | `clamp(2.6rem, 7vw, 6rem)` | 600 | Home only, max 16ch, centered |
| `h1` | `clamp(2.8rem, 6vw, 5.2rem)` | 700 | One per page |
| `h2` | `clamp(2rem, 3.4vw, 3.2rem)` | 600 | Section heads |
| `h3` | `1.4rem` | 700 | Card and item titles |
| `.lede` | `clamp(1.05rem, 1.6vw, 1.3rem)` | 500 | `--muted`, max 62ch |
| Body | `1rem` / 1.5 | 400 | |
| `.eyebrow` | `0.82rem` | 700 | Uppercase, `0.12em` tracking, `--accent-text` |
| `.meta`, `.card-label` | `0.78rem` | 700 | Uppercase, `0.08em` tracking, `--muted` |
| Mono caption | `0.85rem` | 400 | JetBrains Mono, sheet captions only |

Nothing renders below `0.78rem` (12.5px). Apple's floor for custom desktop type is 10pt and 11pt on mobile (`accessibility.md › Vision`); uppercase tracked-out text needs more than the floor to stay readable, which is why the small labels sit at 12.5px rather than the 10.9px they started at. No weight below 400 at any size — "avoid Ultralight, Thin, and Light font weights" (`typography.md › Ensuring legibility`).

Only the weights actually used are requested from Google Fonts: Manrope 400/500/600/700/800, JetBrains Mono 400/500.

## 4. Space and shape

| Token | Value | Use |
|---|---|---|
| `--max-width` | `1240px` | Container ceiling |
| Container gutter | `1.5rem`, `1rem` under 420px | Never less |
| Section rhythm | `clamp(4rem, 9vw, 8rem)` | Vertical padding, top and bottom |
| `--radius-lg` | `28px` | Cards, panels |
| `--radius-md` | `18px` | Images inside cards, mini-cards |
| `--radius-sm` | `12px` | Thumbnails, chips |
| Pill | `999px` | Buttons, tags, nav items |

Grids use `repeat(auto-fit, minmax(290px, 1fr))` rather than fixed column counts, so a three-up row becomes two and then one without a breakpoint for each step.

## 5. Components

| Class | What it is | Rules |
|---|---|---|
| `.site-header` / `.site-nav` | Sticky header, same five links on every page | Links are 44px-tall pills; current page carries `aria-current="page"` plus weight, color and an underline bar |
| `.button.primary` | One per view, the main action | Solid `--text` on light grounds, white on dark |
| `.button.secondary` | Everything else | Outlined, `--border` |
| `.project-card` + `.card-link` | Work summary that links onward | `.card-link` pins to the card's bottom so uneven cards still align |
| `.sheet-grid` | Drawing sheets | `object-fit: contain` on a 4:3 frame — a cropped drawing is a broken drawing. Caption carries the sheet name plus an "Open full size" link |
| `.sheet-placeholder` | A sheet that isn't exported yet | Dashed outline, plain words. Never a fake drawing |
| `.status-chip` | "Coming soon" | Replaces a link that has no destination |
| `.spec-strip` | Real numbers from the drawing | Only real values, never rounded for looks |
| `.project-tags` | Component names | `--accent-text` on `--accent-soft` |
| `.music-note`, `.bullet-list`, `.split-layout`, `.mini-card` | Supporting blocks | — |
| `.reveal` | Fade-and-rise on scroll | Off under Reduce Motion; `<noscript>` un-hides it |
| `.skip-link` | First focusable element on every page | Jumps to `#main` |

Every interactive element is at least 44px tall. Apple's desktop minimum is 28×28pt and mobile is 44×44pt (`accessibility.md › Mobility`); this site uses one size for both so a link never needs a second measurement on a phone.

## 6. Motion

One idea: motion confirms, it never performs. `motion.md › Best practices`: "Add motion purposefully, supporting the experience without overshadowing it."

- Easing is `cubic-bezier(0.22, 1, 0.36, 1)` everywhere; 0.35s for hover, 0.9s for the scroll reveal.
- The one deliberate moment is the 3D smartwatch: it turns slowly on its own until touched, then follows the pointer. It earns the exception because rotating the object *is* the content.
- Hover lifts are 1–4px. Anything larger reads as a bounce.
- `prefers-reduced-motion: reduce` collapses transitions to nothing, stops the model's idle spin (handled in `script.js`), and cancels hover transforms. Motion is never the only carrier of meaning.

## 7. Accessibility floor

Non-negotiable. A change that breaks any line here doesn't ship.

1. Text under 17pt clears 4.5:1 against its real background. Blue text uses `--accent-text`.
2. Every link, button and control is at least 44px tall, with space between neighbors.
3. `:focus-visible` shows a 3px ring on everything focusable. `outline: none` appears nowhere.
4. Every page has a skip link and `id="main"` on `<main>`.
5. No state is signalled by color alone.
6. Images carry alt text that states what the drawing shows, including its real dimensions. Decorative images carry `alt=""`.
7. `model-viewer` keeps `touch-action="pan-y"` so a phone can still scroll past it.
8. Reduce Motion is respected; the page is fully usable with JavaScript off.
9. No `href="#"`. Ever.
10. One `h1` per page, headings in order, no level skipped.

## 8. Review checklist

Before pushing, at 390px and at 1280px:

- [ ] No horizontal scrollbar at either width
- [ ] Tab through the page: focus is visible at every stop, and the order matches the visual order
- [ ] Any new color pairing computed, not eyeballed
- [ ] New controls measure 44px
- [ ] Every new link has a real destination
- [ ] Text still readable at 200% browser zoom
- [ ] With Reduce Motion on, nothing moves on its own
- [ ] Toggle the OS to dark and back: no hard-coded `white`/hex crept into a new rule, nothing goes invisible
