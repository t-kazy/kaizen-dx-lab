# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Project Overview

kaizen-dx-lab is a toolkit for generating premium, design-focused client presentation slides using Claude Code skills. It produces self-contained HTML slide decks with sophisticated CSS design systems, multiple themes, and interactive navigation.

## Repository Structure

```
.
├── CLAUDE.md
├── README.md
├── .claude/
│   └── skills/
│       ├── design-slides.md      # /design-slides - Generate premium slide decks
│       └── refine-slides.md      # /refine-slides - Review & improve existing decks
├── templates/
│   ├── slide-base.html           # Base HTML template with CSS design system
│   └── themes/
│       ├── midnight-indigo.css   # Dark theme (tech, SaaS, DX)
│       ├── arctic-frost.css      # Light theme (corporate, consulting)
│       └── obsidian-ember.css    # Dark warm theme (creative, startup)
└── examples/
    └── dx-transformation-proposal.html  # Sample slide deck
```

## Skills

### /design-slides
Generates a complete, self-contained HTML slide deck from a brief description. Outputs a single HTML file with all CSS inlined, keyboard/touch navigation, and a progress bar.

### /refine-slides
Reviews an existing slide deck against a design quality checklist and optionally applies fixes. Scores the deck out of 100 and provides actionable improvement suggestions.

## Design System

The slide system uses a custom CSS design system with:
- **Typography scale**: 14px to 120px with Inter + Noto Sans JP fonts
- **Spacing scale**: 8px to 128px
- **Component library**: Cards (4 variants), badges, chips, metrics/KPI, timelines, progress bars, icon circles, numbered lists
- **Decorative elements**: Gradient blobs, grid overlays, noise textures
- **Layouts**: 2-col, 3-col, 4-col grids, 2:1 and 1:2 splits
- **Themes**: 3 built-in themes with full CSS custom property system

## Key Rules for Slide Generation

- Generated slides MUST be single self-contained HTML files (all CSS inlined)
- Never use the same layout for consecutive slides
- Use whitespace aggressively — max 60% of slide area
- Titles should be 6-8 words max
- Max 4 bullet points per slide, each under 12 words
- Always use `.metric` component for numbers
- Follow the slide structure: Cover → Agenda → Content → Summary → Next Steps → Closing

## Development

No build tooling required. Slides are pure HTML/CSS/JS and open directly in any modern browser.
