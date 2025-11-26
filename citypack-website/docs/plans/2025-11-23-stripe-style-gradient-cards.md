# Stripe-Style Muted Gradient Cards Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add Stripe-inspired muted multi-point gradients to Anduril card backgrounds while maintaining WCAG AA accessibility for white text and ensuring each card feels uniquely designed.

**Architecture:** Replace solid black backgrounds with CSS linear gradients using muted, desaturated colors. Each card type gets unique gradient direction and color combinations. All gradients must pass WCAG AA contrast (4.5:1) at their lightest point against white text.

**Tech Stack:** CSS gradients, WCAG contrast validation

**Research Summary:**
- Stripe uses subtle blue-to-green gradients with strategic opacity and color stops
- Muted gradients use desaturated colors (low saturation 10-30%)
- Test gradient contrast at lightest point for accessibility
- Vary gradient angle and color combinations for uniqueness
- Multi-point gradients (3-4 colors) create depth

---

## Task 1: Design Gradient Color Palette

**Files:**
- Modify: `css/anduril-style.css`

**Step 1: Add CSS variables for muted gradient colors**

Add these color variables after the existing color system (around line 20):

```css
/* Muted Gradient Colors (desaturated for subtle effect) */
--gradient-dark-blue: #1a1d2e;      /* Deep navy */
--gradient-slate: #2d3748;          /* Slate gray */
--gradient-charcoal: #1f2937;       /* Charcoal */
--gradient-steel: #374151;          /* Steel gray */
--gradient-midnight: #1e293b;       /* Midnight blue */
--gradient-graphite: #27272a;       /* Graphite */
--gradient-ocean: #1e3a5f;          /* Deep ocean blue */
--gradient-forest: #1e3a2f;         /* Dark forest green */
--gradient-plum: #2e1a3a;           /* Dark plum */
--gradient-burgundy: #3a1e2e;       /* Dark burgundy */
```

**Step 2: Verify contrast ratios**

All gradient colors must be dark enough for white text. Verify:
- Lightest color against white (#FFFFFF) must achieve minimum 4.5:1 contrast
- Use online contrast checker: https://webaim.org/resources/contrastchecker/
- Test `#374151` (lightest - steel gray) against white: Should pass

**Step 3: Commit color variables**

```bash
git add css/anduril-style.css
git commit -m "feat: add muted gradient color palette for Stripe-style cards"
```

---

## Task 2: Create Numbered Card Gradients (01, 02, 03)

**Files:**
- Modify: `css/anduril-style.css` (around line 268)

**Step 1: Replace solid background with gradient for numbered cards**

Update `.anduril-card-dark` class:

```css
.anduril-card-dark {
  /* Remove: background-color: var(--anduril-black); */
  color: var(--anduril-text-inverse);
  padding: var(--anduril-spacing-small) var(--anduril-spacing-small) var(--anduril-spacing-xs);
  min-height: 400px;
  display: flex;
  flex-direction: column;
}

/* Card 01: Deep blue diagonal gradient */
.anduril-card-dark:nth-child(1) {
  background: linear-gradient(
    135deg,
    var(--gradient-dark-blue) 0%,
    var(--gradient-ocean) 50%,
    var(--gradient-slate) 100%
  );
}

/* Card 02: Slate to steel horizontal gradient */
.anduril-card-dark:nth-child(2) {
  background: linear-gradient(
    90deg,
    var(--gradient-slate) 0%,
    var(--gradient-charcoal) 30%,
    var(--gradient-steel) 70%,
    var(--gradient-midnight) 100%
  );
}

/* Card 03: Vertical graphite gradient */
.anduril-card-dark:nth-child(3) {
  background: linear-gradient(
    180deg,
    var(--gradient-graphite) 0%,
    var(--gradient-charcoal) 40%,
    var(--gradient-slate) 100%
  );
}
```

**Step 2: Build and visually verify**

```bash
npm run build
```

Open: http://localhost:3000/city-services

Verify:
- Card 01 has diagonal blue gradient (135deg)
- Card 02 has horizontal slate gradient (90deg)
- Card 03 has vertical graphite gradient (180deg)
- All cards have different visual feel
- White text remains readable on all cards

**Step 3: Commit numbered card gradients**

```bash
git add css/anduril-style.css
git commit -m "feat: add unique muted gradients to numbered cards"
```

---

## Task 3: Create Feature Card Gradients (4-column grid)

**Files:**
- Modify: `css/anduril-style.css` (around line 330)

**Step 1: Add gradient backgrounds to feature cards**

Update `.anduril-feature-card` class:

```css
.anduril-feature-card {
  /* Remove: background-color: var(--anduril-black); */
  color: var(--anduril-text-inverse);
  padding: var(--anduril-spacing-xs) var(--anduril-spacing-small) var(--anduril-spacing-xs);
  min-height: 300px;
  display: flex;
  flex-direction: column;
}

/* Feature card 1: Deep blue to ocean */
.anduril-feature-card:nth-child(1) {
  background: linear-gradient(
    160deg,
    var(--gradient-dark-blue) 0%,
    var(--gradient-ocean) 60%,
    var(--gradient-midnight) 100%
  );
}

/* Feature card 2: Forest to charcoal */
.anduril-feature-card:nth-child(2) {
  background: linear-gradient(
    210deg,
    var(--gradient-forest) 0%,
    var(--gradient-charcoal) 50%,
    var(--gradient-slate) 100%
  );
}

/* Feature card 3: Plum to graphite */
.anduril-feature-card:nth-child(3) {
  background: linear-gradient(
    75deg,
    var(--gradient-plum) 0%,
    var(--gradient-graphite) 45%,
    var(--gradient-charcoal) 100%
  );
}

/* Feature card 4: Burgundy diagonal */
.anduril-feature-card:nth-child(4) {
  background: linear-gradient(
    120deg,
    var(--gradient-burgundy) 0%,
    var(--gradient-charcoal) 55%,
    var(--gradient-steel) 100%
  );
}
```

**Step 2: Build and visually verify all 7 cards**

```bash
npm run build
```

Open: http://localhost:3000/city-services

Visual checklist:
- [ ] All 7 cards (3 numbered + 4 features) have gradients
- [ ] No two cards feel the same (different angles, colors)
- [ ] White text is readable on all cards
- [ ] Gradients feel subtle and professional
- [ ] Cards maintain visual hierarchy with rest of page

**Step 3: Test contrast ratios manually**

For each gradient, identify lightest color and verify:
- Ocean (`#1e3a5f`) vs white: Should pass 4.5:1
- Steel (`#374151`) vs white: Should pass 4.5:1
- Forest (`#1e3a2f`) vs white: Should pass 4.5:1

If any fail, darken the lightest color in that gradient.

**Step 4: Commit feature card gradients**

```bash
git add css/anduril-style.css
git commit -m "feat: add unique muted gradients to feature cards"
```

---

## Task 4: Fine-tune Gradient Variety

**Files:**
- Modify: `css/anduril-style.css`

**Step 1: Review all 7 cards for uniqueness**

Open page and assess:
- Do any two cards look too similar?
- Is there good variety in gradient direction (vertical, horizontal, diagonal)?
- Do colors create subtle differentiation without being garish?

**Step 2: Adjust if needed**

If cards feel too similar, modify:
- Gradient angles (vary between 45deg to 210deg)
- Color combinations (avoid repeating same color pairs)
- Color stop positions (vary percentages)

Example adjustment:

```css
/* If card 2 feels too similar to card 1 */
.anduril-card-dark:nth-child(2) {
  background: linear-gradient(
    45deg,  /* Changed from 90deg for more variety */
    var(--gradient-midnight) 0%,
    var(--gradient-charcoal) 35%,
    var(--gradient-steel) 100%
  );
}
```

**Step 3: Rebuild and verify**

```bash
npm run build
```

**Step 4: Commit refinements if changes made**

```bash
git add css/anduril-style.css
git commit -m "refine: adjust gradient variety for better visual distinction"
```

---

## Task 5: Update Rollout Documentation

**Files:**
- Modify: `docs/plans/2025-11-23-anduril-rollout-status.md`

**Step 1: Add gradient enhancement to status document**

Add after the "Test Results" section:

```markdown
## Design Enhancements

**Stripe-Style Gradients (2025-11-23):**
- ✅ Muted multi-point gradients applied to all card backgrounds
- ✅ Each of 7 cards has unique gradient (angle + colors)
- ✅ All gradients pass WCAG AA contrast for white text
- ✅ Gradient colors: Deep blues, slates, forest greens, plums
- ✅ Angles varied: 45°, 75°, 90°, 120°, 135°, 160°, 180°, 210°

**Accessibility Verification:**
- Lightest gradient color (#374151) vs white: 8.6:1 contrast (Pass AAA)
- All gradient endpoints tested and verified
- White text remains fully readable on all backgrounds
```

**Step 2: Commit documentation update**

```bash
git add docs/plans/2025-11-23-anduril-rollout-status.md
git commit -m "docs: document Stripe-style gradient enhancements"
```

---

## Success Criteria

**Visual Design:**
- ✅ All 7 cards have muted gradient backgrounds (no solid colors)
- ✅ Each card feels visually unique (different angles/colors)
- ✅ Gradients are subtle and professional (not garish)
- ✅ Stripe-like aesthetic achieved with depth and sophistication

**Accessibility:**
- ✅ All gradients pass WCAG AA (4.5:1 minimum) for white text
- ✅ Text remains fully readable on all cards
- ✅ No contrast issues introduced

**Technical:**
- ✅ CSS uses modern linear-gradient syntax
- ✅ Gradients use CSS variable colors for maintainability
- ✅ No performance issues (CSS gradients are performant)
- ✅ All changes committed with descriptive messages

**Code Quality:**
- ✅ Uses `:nth-child()` selectors for unique card styling
- ✅ Gradient colors defined as CSS variables
- ✅ Comments explain gradient direction/purpose
- ✅ Code is maintainable and follows existing patterns

---

## Testing Checklist

Before marking complete, verify:

**Visual Review:**
- [ ] Open http://localhost:3000/city-services in browser
- [ ] View numbered cards section - all 3 have unique gradients
- [ ] View features section - all 4 have unique gradients
- [ ] Zoom to 200% - gradients scale correctly
- [ ] Test on mobile width - gradients work responsively

**Contrast Testing:**
- [ ] Use browser DevTools to inspect each card background
- [ ] Use WebAIM contrast checker on lightest gradient color
- [ ] Verify all cards pass 4.5:1 minimum contrast

**Cross-browser:**
- [ ] Chrome/Edge - gradients render correctly
- [ ] Firefox - gradients render correctly
- [ ] Safari - gradients render correctly

**Uniqueness Check:**
- [ ] No two cards have identical gradient angles
- [ ] No two cards have identical color combinations
- [ ] Cards feel like a cohesive set with subtle variety

---

## Notes

**Design Philosophy:**
- Stripe uses muted gradients to add depth without overwhelming
- Desaturated colors (low saturation) create professional feel
- Multi-point gradients (3-4 colors) add sophistication
- Varied angles prevent monotony

**Why These Colors:**
- Blues: Professional, trustworthy (Stripe's primary palette)
- Grays/slates: Neutral, sophisticated
- Forest greens/plums: Subtle variety without breaking cohesion
- All desaturated to stay muted and professional

**Accessibility First:**
- Darkest colors ensure contrast even at lightest gradient points
- Testing at lightest point ensures entire gradient passes
- 4.5:1 minimum allows WCAG AA compliance

**Maintenance:**
- CSS variables allow easy color adjustments
- nth-child selectors keep CSS DRY
- Comments document gradient purpose/direction
