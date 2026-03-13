# /refine-slides - Slide Design Review & Refinement

Review and improve an existing slide deck for design quality, content impact, and visual consistency.

## Usage

```
/refine-slides [path-to-slide-file]
```

## Skill Instructions

### Step 1: Read the Slide File

Read the specified HTML slide file completely.

### Step 2: Design Audit

Evaluate each slide against this checklist and report findings:

#### Layout & Composition
- [ ] Every slide has ONE clear focal point
- [ ] No slide uses more than 60% of its area
- [ ] Consecutive slides use different layout types
- [ ] Grid layouts are properly aligned
- [ ] Whitespace is generous (padding >= `var(--space-xl)`)

#### Typography
- [ ] `heading-hero` used only on cover
- [ ] Titles are 6-8 words max
- [ ] Body text uses `body-lg` or `body-base` (never raw `<p>`)
- [ ] `.caption` used for labels/metadata
- [ ] `.text-gradient` used max 2-3 times in entire deck
- [ ] No orphaned single words on a line (check for `<br>` wrapping)

#### Visual Consistency
- [ ] Cards use consistent border-radius and padding
- [ ] Icon circles are present on card-heavy slides
- [ ] Decorative elements (`.bg-noise`, `.bg-grid`, `.bg-blob`) are applied correctly
- [ ] Color usage follows theme palette (no hardcoded colors outside theme)
- [ ] `.divider-gradient` separates heading from content where appropriate

#### Content Quality
- [ ] Headlines are action-oriented / impactful (not generic)
- [ ] Bullet points <= 4 per slide, each <= 12 words
- [ ] Metrics use `.metric` component (not plain text)
- [ ] Numbers are contextualized ("3.2x faster" not "3.2x")
- [ ] Logical flow from slide to slide

#### Structure
- [ ] Deck starts with cover slide
- [ ] Agenda/overview slide follows cover
- [ ] Section dividers separate major topics
- [ ] Summary slide near the end
- [ ] Next steps / timeline before closing
- [ ] Closing slide is last
- [ ] Page numbers on all slides except cover

#### Technical
- [ ] Single self-contained HTML file (no external CSS links)
- [ ] Google Fonts loaded correctly
- [ ] Keyboard navigation works
- [ ] Touch/click navigation included
- [ ] Progress bar present

### Step 3: Generate Report

Present findings as:

```
## Slide Deck Review: {filename}

### Score: {X}/100

### Strengths
- ...

### Issues Found
| # | Slide | Severity | Issue | Fix |
|---|-------|----------|-------|-----|
| 1 | 3     | High     | ...   | ... |

### Recommendations
1. ...
```

### Step 4: Apply Fixes

Ask the user: "Would you like me to apply the fixes automatically?"

If yes, edit the file to fix all issues found. Prioritize:
1. **High severity**: Broken layouts, missing structure, unreadable text
2. **Medium severity**: Inconsistent styling, missing decorative elements
3. **Low severity**: Content wording, minor spacing tweaks

### Step 5: Before/After

After applying fixes, summarize what changed:
- Number of slides modified
- Key improvements made
- Remaining suggestions that require user input (e.g., content changes)
