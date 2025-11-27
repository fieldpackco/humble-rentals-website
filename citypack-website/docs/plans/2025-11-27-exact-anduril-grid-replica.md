# Exact Anduril Grid Layout Replica - Implementation Plan

**Date:** November 27, 2025
**Objective:** Create an EXACT pixel-perfect replica of Anduril's below-the-fold grid layout with Citypack placeholder text and gradient backgrounds

## Current State Analysis

### What We Have Now:
- Grid cards with minimum heights (400px/600px)
- Gradient backgrounds showing
- Basic bento-box structure
- Cards are visible but layout doesn't match Anduril

### Problems Identified:
1. **Grid gaps are wrong** - Current: 8px, Anduril: 0-4px (tight/minimal gaps)
2. **Card proportions incorrect** - Not matching Anduril's exact grid cell layout
3. **Grid structure wrong** - Using 12-column when Anduril uses a tighter 3-column base
4. **No rounded corners** - Anduril uses subtle border-radius (~8px)
5. **Wrong section spacing** - Too much white space between sections
6. **Text positioning wrong** - Text should be bottom-left, not centered in cards
7. **Card heights inconsistent** - Need exact aspect ratios from Anduril
8. **Missing tight grid composition** - Anduril's grid is edge-to-edge with minimal gaps

## Anduril Grid Analysis (Below the Fold 1)

### Exact Grid Structure:
```
Row 1: [3 equal squares across]
  - Ghost (1x1)
  - Barracuda (1x1)
  - Lattice (1x1)

Row 2: [1 tall + 1 wide + stack of 2]
  - Roadrunner (1x2 tall, left)
  - Fury (2x1 wide, center)
  - Menace (1x1, right top)
  - Dive-XL (1x1, right bottom)
```

### Key Visual Details:
- **Gap:** 4px between cards (very tight)
- **Border radius:** ~8px on all cards
- **Grid base:** 3 columns of equal width
- **Text position:** Bottom-left corner with 24px padding
- **Text style:**
  - Product name: white, ~24px, bold
  - Subtitle (if any): white, ~14px, light weight
- **Image treatment:** Full bleed, dark overlay for text readability
- **Hover state:** Subtle scale (1.02) + slight glow

## Implementation Strategy

### Phase 1: Rebuild Grid System CSS
**File:** `css/grid-system.css`

Replace current 12-column system with exact 3-column Anduril grid:

```css
/* ANDURIL EXACT REPLICA GRID */
.products-grid-section {
    padding: 0;
    margin: 0;
    width: 100vw;
    margin-left: calc(-50vw + 50%);
    margin-right: calc(-50vw + 50%);
}

.grid-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 4px; /* Anduril's tight gap */
    padding: 0;
    width: 100%;
    max-width: 100vw;
}

/* Card base styles */
.grid-card {
    position: relative;
    overflow: hidden;
    border-radius: 8px; /* Anduril's subtle rounding */
    cursor: pointer;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    min-height: 400px;
}

.grid-card:hover {
    transform: scale(1.02);
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3);
    z-index: 10;
}

/* Exact Anduril cell sizes */
.grid-1x1 {
    grid-column: span 1;
    grid-row: span 1;
    aspect-ratio: 1 / 1;
}

.grid-1x2 {
    grid-column: span 1;
    grid-row: span 2;
    aspect-ratio: 1 / 2;
}

.grid-2x1 {
    grid-column: span 2;
    grid-row: span 1;
    aspect-ratio: 2 / 1;
}

/* Card content positioning - Anduril style */
.grid-card-content {
    position: absolute;
    bottom: 24px;
    left: 24px;
    right: 24px;
    z-index: 2;
    color: white;
}

.grid-card-title {
    font-size: 24px;
    font-weight: 700;
    margin: 0 0 4px 0;
    color: white;
    line-height: 1.2;
}

.grid-card-subtitle {
    font-size: 14px;
    font-weight: 400;
    margin: 0;
    color: rgba(255, 255, 255, 0.85);
    line-height: 1.4;
}

/* Image fills entire card */
.grid-card-image {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    background-size: cover;
    background-position: center;
    transition: transform 0.5s ease;
}

.grid-card:hover .grid-card-image {
    transform: scale(1.05);
}

/* Dark overlay for text readability */
.grid-card-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(
        to bottom,
        rgba(0, 0, 0, 0.2) 0%,
        rgba(0, 0, 0, 0.6) 100%
    );
    z-index: 1;
}

/* Remove CTA arrows for now - cleaner look like Anduril */
.grid-card-cta {
    display: none;
}
```

### Phase 2: Update HTML Template Structure
**File:** `templates/pages/landing-page-anduril.hbs`

Replace benefits grid section with exact Anduril structure:

```handlebars
<!-- Products Grid - Exact Anduril Layout -->
{{#if benefits}}
<section class="products-grid-section">
    <div class="grid-container">
        <!-- Row 1: Three equal squares -->
        {{#each benefits.items}}
        {{#if @first}}
        <div class="grid-card grid-1x1" data-placeholder="1">
            <div class="grid-card-image"></div>
            <div class="grid-card-overlay"></div>
            <div class="grid-card-content">
                <h3 class="grid-card-title">{{title}}</h3>
            </div>
        </div>
        {{else if @index 1}}
        <div class="grid-card grid-1x1" data-placeholder="2">
            <div class="grid-card-image"></div>
            <div class="grid-card-overlay"></div>
            <div class="grid-card-content">
                <h3 class="grid-card-title">{{title}}</h3>
            </div>
        </div>
        {{else if @index 2}}
        <div class="grid-card grid-1x1" data-placeholder="3">
            <div class="grid-card-image"></div>
            <div class="grid-card-overlay"></div>
            <div class="grid-card-content">
                <h3 class="grid-card-title">{{title}}</h3>
            </div>
        </div>
        {{/if}}
        {{/each}}

        <!-- Row 2: Roadrunner (tall left) -->
        <div class="grid-card grid-1x2" data-placeholder="4">
            <div class="grid-card-image"></div>
            <div class="grid-card-overlay"></div>
            <div class="grid-card-content">
                <h3 class="grid-card-title">City Fleet Management</h3>
                <p class="grid-card-subtitle">End-to-end battery deployment</p>
            </div>
        </div>

        <!-- Row 2: Fury (wide center) -->
        <div class="grid-card grid-2x1" data-placeholder="5">
            <div class="grid-card-image"></div>
            <div class="grid-card-overlay"></div>
            <div class="grid-card-content">
                <h3 class="grid-card-title">Power Analytics</h3>
                <p class="grid-card-subtitle">Real-time usage tracking</p>
            </div>
        </div>

        <!-- Row 3: Menace (right top) -->
        <div class="grid-card grid-1x1" data-placeholder="6">
            <div class="grid-card-image"></div>
            <div class="grid-card-overlay"></div>
            <div class="grid-card-content">
                <h3 class="grid-card-title">Event Support</h3>
            </div>
        </div>

        <!-- Row 3: Dive-XL (right bottom) -->
        <div class="grid-card grid-1x1" data-placeholder="1">
            <div class="grid-card-image"></div>
            <div class="grid-card-overlay"></div>
            <div class="grid-card-content">
                <h3 class="grid-card-title">Emergency Backup</h3>
            </div>
        </div>
    </div>
</section>
{{/if}}
```

### Phase 3: Enhanced Gradient Placeholders
**Update in:** `css/grid-system.css`

Create better gradient placeholders that match Anduril's color palette but use Citypack colors:

```css
/* Citypack-branded gradient placeholders */
.grid-card[data-placeholder="1"] .grid-card-image {
    background: linear-gradient(135deg, #FF6B35 0%, #F4B942 100%);
}

.grid-card[data-placeholder="2"] .grid-card-image {
    background: linear-gradient(135deg, #2C3E50 0%, #FF6B35 50%, #F4B942 100%);
}

.grid-card[data-placeholder="3"] .grid-card-image {
    background: linear-gradient(135deg, #1a1a1a 0%, #2C3E50 100%);
}

.grid-card[data-placeholder="4"] .grid-card-image {
    background: linear-gradient(180deg, #F4B942 0%, #FF6B35 100%);
}

.grid-card[data-placeholder="5"] .grid-card-image {
    background: linear-gradient(90deg, #2C3E50 0%, #1a1a1a 50%, #2C3E50 100%);
}

.grid-card[data-placeholder="6"] .grid-card-image {
    background: linear-gradient(135deg, #FF6B35 0%, #2C3E50 100%);
}
```

### Phase 4: Remove/Hide Features Section Temporarily
**File:** `templates/pages/landing-page-anduril.hbs`

Comment out the "From Pilot to Generator Policy" section for now to match Anduril's clean product grid:

```handlebars
<!-- TEMPORARILY HIDDEN - Focus on product grid first
{{#if features}}
<section class="news-section">
...
</section>
{{/if}}
-->
```

### Phase 5: Responsive Breakpoints (Anduril-style)
**File:** `css/grid-system.css`

```css
/* Tablet: 2 columns */
@media (max-width: 1024px) {
    .grid-container {
        grid-template-columns: repeat(2, 1fr);
    }

    .grid-1x2 {
        grid-row: span 1;
        aspect-ratio: 1 / 1;
    }

    .grid-2x1 {
        grid-column: span 2;
    }
}

/* Mobile: 1 column */
@media (max-width: 768px) {
    .grid-container {
        grid-template-columns: 1fr;
        gap: 8px;
    }

    .grid-1x1,
    .grid-1x2,
    .grid-2x1 {
        grid-column: span 1;
        grid-row: span 1;
        aspect-ratio: 16 / 9; /* Wider on mobile */
        min-height: 300px;
    }

    .grid-card-content {
        bottom: 16px;
        left: 16px;
        right: 16px;
    }

    .grid-card-title {
        font-size: 20px;
    }
}
```

### Phase 6: Content Structure Update
**File:** `content/pages/home.json`

Simplify benefits to match the grid structure:

```json
{
  "benefits": {
    "title": "Our Solutions",
    "items": [
      {
        "title": "Public Works Crews",
        "description": null
      },
      {
        "title": "Farmers Markets",
        "description": null
      },
      {
        "title": "City Events",
        "description": null
      }
    ]
  }
}
```

## Execution Plan

### Step 1: Backup Current CSS
Create backup of `css/grid-system.css` before making changes

### Step 2: Rewrite Grid System CSS
Replace entire grid system with Anduril-exact structure:
- 3-column base grid
- 4px gaps
- 8px border radius
- Exact cell sizing classes (grid-1x1, grid-1x2, grid-2x1)
- Bottom-left text positioning
- Enhanced gradient placeholders

### Step 3: Update Template HTML
Rewrite `landing-page-anduril.hbs` products section:
- 7 cards total in exact Anduril layout
- Row 1: 3 equal squares
- Row 2: 1 tall + 1 wide + 2 stack
- Proper class assignments
- Remove CTA links

### Step 4: Update home-page.hbs (if needed)
Mirror changes to home-page.hbs template

### Step 5: Hide Features Section
Comment out features grid temporarily to focus on product grid

### Step 6: Test Responsive Breakpoints
Verify layout on:
- Desktop (1920px+)
- Tablet (768-1024px)
- Mobile (320-768px)

### Step 7: Build and Verify
```bash
npm run build
```

### Step 8: Visual Comparison
Compare rendered HTML side-by-side with Anduril screenshots:
- Card spacing
- Text positioning
- Gradient backgrounds
- Hover effects
- Overall proportions

### Step 9: Iterate and Refine
Make pixel-perfect adjustments:
- Adjust gap from 4px if needed
- Fine-tune border-radius
- Adjust text sizes
- Perfect gradient colors

### Step 10: Commit Changes
Commit with detailed message explaining exact Anduril replica implementation

## Success Criteria

- [ ] Grid uses 3-column base (not 12-column)
- [ ] Gap is 4px (tight, like Anduril)
- [ ] Cards have 8px border radius
- [ ] 7 cards in exact Anduril layout pattern
- [ ] Text positioned bottom-left with 24px padding
- [ ] Gradient placeholders using Citypack colors
- [ ] Hover effect matches Anduril (scale 1.02 + shadow)
- [ ] Responsive breakpoints work on tablet/mobile
- [ ] No white space issues between sections
- [ ] Layout is edge-to-edge full width

## Key Differences from Previous Attempt

1. **Gap size:** 8px → 4px (much tighter)
2. **Column system:** 12-column → 3-column (matches Anduril exactly)
3. **Cell classes:** span-X → grid-1x1, grid-1x2, grid-2x1 (explicit sizing)
4. **Border radius:** 0 → 8px (subtle rounding)
5. **Card count:** 3 benefits → 7 product cards (proper Anduril structure)
6. **Text position:** Centered → Bottom-left (Anduril style)
7. **CTA buttons:** Visible → Hidden (cleaner look)
8. **Aspect ratios:** Variable → Fixed (1:1, 1:2, 2:1 only)

## Files to Modify

1. `css/grid-system.css` - Complete rewrite of grid system
2. `templates/pages/landing-page-anduril.hbs` - Product grid structure
3. `templates/pages/home-page.hbs` - Mirror changes
4. `content/pages/home.json` - Simplified benefit items (optional)

## Estimated Effort

- CSS Rewrite: 30 minutes
- Template Update: 20 minutes
- Testing/Refinement: 20 minutes
- **Total: ~70 minutes**

## Notes

- This is a COMPLETE rewrite, not incremental changes
- Previous 12-column system was fundamentally wrong for Anduril replica
- Focus on exact visual match, not semantic HTML perfection
- Gradients are temporary - will be replaced with real images later
- Keep it simple - match the reference images exactly
