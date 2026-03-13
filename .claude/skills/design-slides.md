# /design-slides - Premium Client Slide Generator

Generate high-quality, design-focused HTML slide decks for client presentations.

## Usage

```
/design-slides [topic or brief description]
```

## Skill Instructions

When this skill is invoked, generate a complete, self-contained HTML slide deck by following these rules precisely.

### Step 1: Understand the Brief

Ask the user if they haven't provided enough context:
- **Topic / proposal theme** (e.g., "DX transformation proposal for retail client")
- **Audience** (e.g., CTO, board members, marketing team)
- **Tone** (e.g., bold & visionary, calm & professional, data-driven)
- **Approximate slide count** (default: 12-18 slides)
- **Theme preference** (midnight-indigo / arctic-frost / obsidian-ember)

If the user gives a one-line brief, infer reasonable defaults and proceed.

### Step 2: Choose Theme & Reference Template

Read the base template and chosen theme:
- `templates/slide-base.html` - the HTML skeleton and CSS design system
- `templates/themes/{theme}.css` - the color/style theme

The generated deck MUST be a **single self-contained HTML file** that inlines ALL CSS (both the base design system and the theme) so the file works standalone when opened in a browser. Do NOT use external CSS `<link>` references — inline everything inside `<style>` tags.

### Step 3: Slide Architecture

Every deck MUST follow this structure:

```
1. COVER SLIDE        — Title + subtitle + company/date. Full visual impact.
2. AGENDA / OVERVIEW  — 3-5 key topics as a visual roadmap.
3-N. CONTENT SLIDES   — The substance (see slide type catalog below).
N+1. SUMMARY          — Key takeaways in 3-5 bullets.
N+2. NEXT STEPS       — Timeline or action items.
N+3. CLOSING          — Thank you / contact / CTA.
```

### Step 4: Slide Type Catalog

Use a VARIETY of these slide types across the deck. **Never use the same layout for consecutive slides.**

| Slide Type | CSS Class | When to Use |
|---|---|---|
| Cover | `slide-cover` | Opening slide with hero typography |
| Section Divider | `slide-section` | Full-accent-gradient separator between topics |
| Two Column | `grid-2` | Comparing, before/after, text + visual |
| Three Cards | `grid-3` | Features, pillars, options |
| Four Cards | `grid-4` | Metrics dashboard, multi-KPI |
| 2:1 Split | `grid-2-1` | Main content + sidebar |
| 1:2 Split | `grid-1-2` | Sidebar + main content |
| Big Number / KPI | Use `.metric` components | Impact metrics, ROI |
| Timeline | Use `.timeline` component | Roadmap, phasing |
| Numbered List | Use `.numbered-list` | Process, steps |
| Quote / Callout | Centered large text | Powerful statement |
| Closing | `slide-closing` | End slide with CTA |

### Step 5: Design Principles (CRITICAL)

Follow these rules to ensure slides look premium, NOT generic:

#### Typography
- Use `heading-hero` (120px) ONLY on the cover slide
- Use `heading-1` or `heading-2` for slide titles
- Titles should be SHORT and impactful (max 6-8 words)
- Body text should be `body-lg` or `body-base` — never smaller than `body-sm`
- Use `.text-gradient` sparingly for hero numbers or key phrases
- Use `.caption` class for labels, categories, and metadata

#### Visual Hierarchy
- Every slide must have ONE clear focal point
- Use whitespace aggressively — never fill more than 60% of the slide area
- Card content should be concise: 2-3 lines max per card
- Use `.divider-gradient` to separate heading from content

#### Color & Contrast
- Use accent colors for emphasis, not everywhere
- Text should have clear contrast against backgrounds
- Use `.text-muted` for secondary information
- Use `.text-subtle` for tertiary/metadata

#### Decorative Elements
- Add `<div class="bg-grid"></div>` to 30-40% of slides for texture
- Add `<div class="bg-noise"></div>` to all slides for depth
- Use `.bg-blob` elements (2 per slide max) on key slides (cover, section, closing)
- Never overdo decorations — they should be felt, not seen

#### Data & Metrics
- Always use `.metric` component for numbers — never plain text
- Use `.progress-bar` for percentages
- Use `.badge` or `.chip` for status/category labels
- Large numbers are more impactful than paragraphs of text

#### Card Design
- Alternate between `.card`, `.card-glass`, `.card-elevated`, `.card-outline`
- Add `.icon-circle` with emoji icons to card headers for visual anchoring
- Keep card content to heading + 1-2 lines of description

### Step 6: Content Quality

- **Headlines**: Write like a designer, not a report author. "Transform How You Ship" > "Digital Transformation Proposal"
- **Bullet points**: Max 4 per slide. Each under 12 words.
- **Numbers**: Always contextualize ("3.2x faster" not just "3.2x")
- **Language**: Match the client's industry jargon where appropriate
- **Flow**: Each slide should logically lead to the next

### Step 7: Page Numbers

Add to every slide except cover:
```html
<span class="page-number">02</span>
```

### Step 8: Output

Write the complete HTML file to:
```
examples/{descriptive-name}.html
```

The file must:
- Be a single self-contained HTML file (all CSS inlined)
- Open correctly in any modern browser
- Support keyboard navigation (arrow keys, space)
- Support click/tap navigation
- Support touch swipe on mobile
- Show a progress bar at the top
- Display a page counter (bottom-right, appears on hover)

### Step 9: Summary

After generating, tell the user:
- File path
- Number of slides
- Theme used
- Suggested improvements or variations

---

## Example Slide HTML Patterns

### Cover Slide
```html
<section class="slide slide-cover">
  <div class="bg-blob" style="width:600px;height:600px;background:var(--accent-primary);top:-200px;right:-100px;"></div>
  <div class="bg-blob" style="width:500px;height:500px;background:#ec4899;bottom:-150px;left:-100px;"></div>
  <div class="bg-noise"></div>
  <div class="slide-inner text-center">
    <div class="badge" style="margin-bottom:var(--space-md);">PROPOSAL 2026</div>
    <h1 class="heading-hero text-gradient" style="margin-bottom:var(--space-md);">Reimagine Your<br>Digital Experience</h1>
    <p class="body-lg text-muted" style="max-width:680px;margin:0 auto;">A strategic roadmap to transform customer engagement<br>and accelerate growth through technology.</p>
    <div style="margin-top:var(--space-xl);">
      <p class="caption text-subtle">CLIENT NAME | MARCH 2026</p>
    </div>
  </div>
</section>
```

### KPI / Metrics Slide
```html
<section class="slide">
  <div class="bg-noise"></div>
  <div class="slide-inner">
    <div class="caption text-accent" style="margin-bottom:var(--space-sm);">IMPACT METRICS</div>
    <h2 class="heading-2" style="margin-bottom:var(--space-lg);">Measurable Results<br>That Drive Growth</h2>
    <div class="divider-gradient" style="margin-bottom:var(--space-xl);"></div>
    <div class="grid-4">
      <div class="card-glass" style="text-align:center;">
        <div class="metric">
          <span class="metric-value">3.2x</span>
          <span class="metric-label">Faster Deployment</span>
          <span class="metric-delta positive">+220%</span>
        </div>
      </div>
      <!-- repeat for other metrics -->
    </div>
  </div>
  <span class="page-number">05</span>
</section>
```

### Three-Card Feature Slide
```html
<section class="slide">
  <div class="bg-grid"></div>
  <div class="bg-noise"></div>
  <div class="slide-inner">
    <div class="caption text-accent" style="margin-bottom:var(--space-sm);">OUR APPROACH</div>
    <h2 class="heading-2" style="margin-bottom:var(--space-xl);">Three Pillars of<br>Transformation</h2>
    <div class="grid-3">
      <div class="card">
        <div class="icon-circle" style="margin-bottom:var(--space-md);">&#9889;</div>
        <h3 class="heading-4" style="margin-bottom:var(--space-sm);">Speed</h3>
        <p class="body-base text-muted">Reduce time-to-market by automating key delivery pipelines.</p>
      </div>
      <!-- repeat -->
    </div>
  </div>
  <span class="page-number">06</span>
</section>
```

### Timeline Slide
```html
<section class="slide">
  <div class="bg-noise"></div>
  <div class="slide-inner">
    <div class="caption text-accent" style="margin-bottom:var(--space-sm);">ROADMAP</div>
    <h2 class="heading-2" style="margin-bottom:var(--space-xl);">Implementation<br>Timeline</h2>
    <div class="grid-2">
      <div class="timeline">
        <div class="timeline-item">
          <div class="caption text-accent">PHASE 01 — Q2 2026</div>
          <h3 class="heading-4" style="margin-top:var(--space-xs);">Discovery & Assessment</h3>
          <p class="body-sm text-muted" style="margin-top:var(--space-xs);">Current state analysis and opportunity mapping.</p>
        </div>
        <!-- repeat -->
      </div>
      <div class="card-glass" style="padding:var(--space-lg);">
        <!-- Summary or visual -->
      </div>
    </div>
  </div>
  <span class="page-number">10</span>
</section>
```

### Section Divider
```html
<section class="slide slide-section">
  <div class="bg-noise"></div>
  <div class="slide-inner text-center">
    <div class="badge" style="background:rgba(255,255,255,0.15);color:#fff;margin-bottom:var(--space-md);">SECTION 02</div>
    <h2 class="heading-1">Our Solution</h2>
    <p class="text-muted body-lg" style="margin-top:var(--space-md);max-width:600px;margin-left:auto;margin-right:auto;">How we will transform your operations end-to-end.</p>
  </div>
</section>
```
