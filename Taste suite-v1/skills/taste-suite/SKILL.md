---
name: taste-suite
description: Anti-generic frontend design taste for landing pages, portfolios, redesigns, and UI styles (minimalist, soft/premium, brutalist), plus design-image generation, brand kits, Stitch DESIGN.md files, and full-output enforcement. Use for any frontend design or redesign task.
---

# Taste Suite

This skill bundles 13 frontend design "taste" skills in one place (from leonxlnx/taste-skill, MIT licensed). This file only routes the request. The real instructions are in `references/`.

## How to use

1. Read the request and choose the **one primary reference** that fits, using the table below.
2. Read that reference file in full before designing or writing code, and follow it.
3. Add a second reference only when the task clearly needs it, for example a style reference plus `redesign-skill.md` when restyling an existing site.
4. If two references contradict each other, the primary reference wins.

## Routing table

| Task | Read |
|---|---|
| **Default**: new landing page, portfolio, or marketing site with no style named | `references/taste-skill.md` |
| Upgrade or restyle an **existing** site or app (audit first) | `references/redesign-skill.md` |
| Clean editorial look: warm monochrome, flat bento grids, muted pastels | `references/minimalist-skill.md` |
| Premium, "expensive" agency look: soft shadows, refined spacing, motion | `references/soft-skill.md` |
| Raw industrial/brutalist look: Swiss type, terminal aesthetic, dashboards | `references/brutalist-skill.md` |
| Heavy scroll motion with GSAP (pinning, stacking, scrubbing), AIDA structure | `references/gpt-tasteskill.md` |
| Generate design images first, then code the site to match them | `references/image-to-code-skill.md` |
| Generate website design reference images (one image per section) | `references/imagegen-frontend-web.md` |
| Generate mobile app screen concepts (iOS/Android) | `references/imagegen-frontend-mobile.md` |
| Brand kit boards: logo system, identity deck, brand guidelines images | `references/brandkit.md` |
| Write a `DESIGN.md` for Google Stitch | `references/stitch-skill.md` (example output: `references/stitch-example-DESIGN.md`) |
| User needs a complete, untruncated output with no placeholders | `references/output-skill.md` (it can be layered on top of any other reference) |
| User asks specifically for the original v1 behavior | `references/taste-skill-v1.md` |

## Notes

- The image-generation references (`image-to-code`, `imagegen-*`, `brandkit`) assume an image-generation tool is available. If none is available, use their art direction as a written brief and build the design directly in code.
- Do not mix several visual styles (for example minimalist and brutalist) in one design unless the user asks for it.
