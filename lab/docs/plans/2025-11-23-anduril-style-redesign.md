# Anduril-Style Redesign - Design Document

**Date:** 2025-11-23
**Status:** Approved for Implementation
**Test Page:** city-services.html

---

## Overview

Transform LAB SEVEN website to adopt Anduril's minimal, monochromatic design aesthetic while maintaining existing content structure and orange brand accent. Use hybrid approach: create new Anduril-style template and CSS, test on one page, then roll out incrementally.

**Reference:** Anduril.com screenshots (Command & Control, Features pages)

---

## Design Principles

1. **Monochromatic palette**: Gray, white, black with orange accent only
2. **Oversized typography**: Massive headlines (120px+), tight letter-spacing
3. **Asymmetric layouts**: 60/40 and 70/30 column splits using CSS Grid
4. **High contrast**: Black cards with white text, light gray backgrounds
5. **Generous spacing**: 200px+ section padding, ample white space
6. **Minimal navigation**: Horizontal text links, simplified structure

---

## Color System

### New Variables
```css
/* Monochromatic Base */
--color-gray-light: #E8E8E8;      /* Primary background (Anduril-style) */
--color-gray-medium: #CCCCCC;     /* Borders, dividers */
--color-white: #FFFFFF;           /* Alternate sections, cards */
--color-black: #000000;           /* Dark cards, footer, primary text */

/* Text */
--color-text-primary: #000000;    /* Headlines, body */
--color-text-secondary: #666666;  /* Supporting text */
--color-text-inverse: #FFFFFF;    /* Text on dark backgrounds */

/* Brand Accent (LIMITED USE) */
--color-orange: #FF6B35;          /* Logo, primary CTA only */
```

### Usage Rules
- **Orange appears ONLY in:**
  - Logo text ("LABRADOR")
  - Primary CTA buttons ("Contact Labrador")
  - Navigation hover states

- **Background pattern:**
  - Hero: Light gray (#E8E8E8)
  - Sections: Alternate white → light gray → white
  - Feature cards: Black (#000000)
  - Footer: Black (#000000)

---

## Typography System

### Font Sizes
```css
--font-hero: clamp(80px, 12vw, 140px);        /* Hero headlines */
--font-section-title: clamp(48px, 8vw, 96px); /* Section titles */
--font-card-title: clamp(24px, 3vw, 36px);    /* Card headlines */
--font-body: 18px;                             /* Body text */
--font-small: 14px;                            /* Fine print, captions */
```

### Font Weights
```css
--font-weight-normal: 400;   /* Body text */
--font-weight-bold: 700;     /* Subheadings */
--font-weight-black: 900;    /* Hero headlines */
```

### Letter Spacing & Line Height
```css
/* Tight spacing for impact */
--letter-spacing-hero: -0.04em;      /* Very tight, Anduril-style */
--letter-spacing-heading: -0.02em;   /* Tight */
--letter-spacing-body: 0;            /* Normal */

/* Compressed line height for headlines */
--line-height-hero: 0.95;   /* Super tight */
--line-height-heading: 1.1; /* Tight */
--line-height-body: 1.6;    /* Comfortable */
```

### Font Stack
```css
--font-family: 'Inter', 'Helvetica Neue', system-ui, -apple-system, sans-serif;
```

---

## Layout Patterns

### 1. Hero Section
**Structure:** Full-width, left-aligned, oversized headline

```
┌─────────────────────────────────────────────┐
│ [CATEGORY LABEL]                            │
│                                              │
│ MASSIVE                                      │
│ HEADLINE                                     │
│ TEXT                                         │
│                                              │
│ Supporting description text in smaller       │
│ size, constrained width for readability     │
│                                              │
│ [Primary CTA] [Secondary CTA]               │
└─────────────────────────────────────────────┘
```

**CSS:**
- Background: Light gray
- Padding: 200px vertical, 40px horizontal
- Max-width: 1400px container
- Headline max-width: 1000px (for readability)
- Min-height: 80vh

---

### 2. Numbered Cards (like "Kill Chain" section)
**Structure:** 3-column grid, black cards with large numbers

```
┌────────────┬────────────┬────────────┐
│ 01         │ 02         │ 03         │
│            │            │            │
│ Title      │ Title      │ Title      │
│            │            │            │
│ Descriptio │ Descriptio │ Descriptio │
│ n text     │ n text     │ n text     │
└────────────┴────────────┴────────────┘
```

**CSS:**
- Grid: 3 columns, 24px gap
- Card background: Black
- Card text: White
- Card padding: 60px 40px
- Card min-height: 400px
- Number size: 72px, bold
- Number margin-bottom: 40px

**Responsive:**
- Desktop: 3 columns
- Tablet: 2 columns
- Mobile: 1 column stack

---

### 3. Split-Screen Features (like "Battle Management Platform")
**Structure:** Asymmetric 60/40 layout

```
┌────────────────────┬──────────────┐
│                    │              │
│                    │ 01 Title     │
│   VISUAL/IMAGE     │ Description  │
│   PLACEHOLDER      │              │
│                    │ 02 Title     │
│                    │ Description  │
│                    │              │
└────────────────────┴──────────────┘
```

**CSS:**
- Grid: 6fr 4fr (60/40 split)
- Gap: 60px
- Visual: Left column (image/placeholder)
- Content: Right column (numbered list)
- Feature numbers: 24px, bold
- Feature title: 36px
- Feature description: 18px

**Responsive:**
- Desktop: 60/40 split
- Tablet: 50/50 split
- Mobile: Stack (visual on top)

---

### 4. Features Grid (like "Features" 4-column)
**Structure:** 4-column grid, black cards

```
┌──────┬──────┬──────┬──────┐
│ Card │ Card │ Card │ Card │
│ Title│ Title│ Title│ Title│
│      │      │      │      │
│ Desc │ Desc │ Desc │ Desc │
└──────┴──────┴──────┴──────┘
```

**CSS:**
- Grid: 4 columns, 24px gap
- Card background: Black
- Card text: White
- Card padding: 40px
- Title: 24px, bold
- Description: 16px

**Responsive:**
- Desktop: 4 columns
- Tablet: 2 columns
- Mobile: 1 column

---

### 5. Footer
**Structure:** Black background, multi-column layout

```
┌─────────────────────────────────────┐
│ LABRADOR       COMPANY    SOCIAL    │
│                                      │
│                Mission    X          │
│                Newsroom   YouTube    │
│                Careers    Instagram  │
│                                      │
│ COPYRIGHT © 2025 LABRADOR            │
└─────────────────────────────────────┘
```

**CSS:**
- Background: Black
- Text: White
- Padding: 100px 40px 60px
- Grid: 2fr 3fr (brand vs links)
- Logo color: Orange (accent)
- Link hover: Orange

---

## Navigation Design

### Anduril-Style Navigation
**Structure:** Minimal horizontal links, no dropdowns on subpages

```
┌────────────────────────────────────────────┐
│ LABRADOR    Home  Customers  Product  Contact │
└────────────────────────────────────────────┘
```

**CSS:**
- Background: Light gray
- Border-bottom: 1px solid medium gray
- Padding: 24px 40px
- Logo: Orange, 20px, bold
- Links: 16px, black, 40px gap
- Hover: Orange color transition

**Decision:** Keep current dropdown system OR simplify to horizontal links?
- **Recommendation:** Flatten to horizontal links for Anduril aesthetic
- Primary nav: Home, Customers, Product, Rental, Contact
- Customers can link to customer listing page vs dropdown

---

## Component Specifications

### Anduril Hero Component
```handlebars
<section class="anduril-hero">
    <div class="anduril-hero-content">
        <div class="anduril-hero-label">{{hero.category}}</div>
        <h1 class="anduril-hero-title">{{hero.title}}</h1>
        <div class="anduril-hero-description">
            <p>{{hero.description}}</p>
        </div>
        <div class="anduril-cta-buttons">
            <a href="{{hero.cta.primary.href}}" class="btn-anduril-primary">
                {{hero.cta.primary.text}}
            </a>
            <a href="{{hero.cta.secondary.href}}" class="btn-anduril-secondary">
                {{hero.cta.secondary.text}}
            </a>
        </div>
    </div>
</section>
```

### Numbered Card Component
```handlebars
<div class="anduril-card-dark">
    <div class="anduril-card-number">0{{add @index 1}}</div>
    <h3 class="anduril-card-title">{{title}}</h3>
    <p class="anduril-card-description">{{description}}</p>
</div>
```

### Split-Screen Component
```handlebars
<div class="anduril-split-layout">
    <div class="anduril-split-visual">
        {{!-- Visual placeholder or image --}}
        <div class="visual-placeholder"></div>
    </div>
    <div class="anduril-split-content">
        {{#each items}}
        <div class="anduril-feature-item">
            <div class="anduril-feature-number">0{{add @index 1}}</div>
            <h3 class="anduril-feature-title">{{title}}</h3>
            <p class="anduril-feature-description">{{description}}</p>
        </div>
        {{/each}}
    </div>
</div>
```

---

## Implementation Strategy

### Phase 1: Create & Test (city-services page)
1. Create `templates/pages/landing-page-anduril.hbs`
2. Create `css/anduril-style.css` with all new styles
3. Create `templates/components/nav-anduril.hbs` (simplified nav)
4. Update `content/pages/city-services.json` to use new template
5. Build and review at http://localhost:3000/city-services

**Files to create:**
```
css/anduril-style.css                    (NEW)
templates/pages/landing-page-anduril.hbs (NEW)
templates/components/nav-anduril.hbs     (NEW)
```

**Files to modify:**
```
content/pages/city-services.json (test page)
```

### Phase 2: Iterate & Validate
1. Review test page with stakeholder
2. Adjust typography scale if needed
3. Refine spacing and layout proportions
4. Get approval to proceed

### Phase 3: Roll Out
**Gradual migration order:**
1. Customer pages: experience-agencies, production-managers, gaffers, location-managers, public-venues, street-festivals
2. Product pages: specifications, features, gallery
3. Other pages: pricing, how-it-works, contact
4. Homepage: index.html (last - most visible)

### Phase 4: Cleanup
1. Remove old CSS files after all pages migrated
2. Archive old templates
3. Update build system if needed

---

## Content Changes for city-services (Test Page)

Update `content/pages/city-services.json`:

```json
{
  "layout": "landing-page-anduril",
  "meta": {
    "title": "LAB SEVEN for City Services | Labrador Field Systems",
    "description": "Silent battery power for municipal operations and permitted events"
  },
  "hero": {
    "category": "CITY SERVICES",
    "title": "Power Public Events Anywhere",
    "description": "Zero emissions, zero noise, zero permits. LAB SEVEN provides silent battery power for city services, public events, and municipal operations without generator drama.",
    "cta": {
      "primary": {
        "text": "Contact Labrador",
        "href": "/contact"
      },
      "secondary": {
        "text": "View Specifications",
        "href": "/specifications"
      }
    }
  },
  "benefits": {
    "title": "Built for Municipal Operations",
    "items": [
      {
        "title": "Permit-Friendly Power",
        "description": "Zero emissions and silent operation eliminate permitting friction. Deploy in noise-restricted zones without special approvals."
      },
      {
        "title": "Residential Compliance",
        "description": "No noise complaints from neighbors. Perfect for street festivals, farmers markets, and community events in residential areas."
      },
      {
        "title": "Quick Deployment",
        "description": "Under 5 minutes to power on. No fuel logistics, no fire watch required. Your crew focuses on the event, not power management."
      }
    ]
  },
  "features": {
    "title": "Why Cities Choose LAB SEVEN",
    "items": [
      {
        "title": "Community Events Without Disruption",
        "description": "Power farmers markets, street fairs, and neighborhood gatherings without disturbing residents. Silent operation means happier communities."
      },
      {
        "title": "Simplified Permitting",
        "description": "Zero-emission classification streamlines permit approval. No special fire watch requirements or noise variance needed."
      },
      {
        "title": "Cost-Effective Operations",
        "description": "Eliminate fuel costs, fire watch requirements, and noise mitigation expenses. Transparent rental pricing includes delivery and backup."
      },
      {
        "title": "Professional Support",
        "description": "Labrador Field Systems handles delivery, placement, and pickup. White-glove service ensures your events run smoothly."
      }
    ]
  }
}
```

---

## Responsive Breakpoints

```css
/* Desktop */
@media (min-width: 1024px) {
  /* All asymmetric layouts active */
  /* 3-4 column grids */
}

/* Tablet */
@media (min-width: 768px) and (max-width: 1023px) {
  /* 2 column grids */
  /* 50/50 splits instead of 60/40 */
  /* Hero font: 80-100px */
}

/* Mobile */
@media (max-width: 767px) {
  /* Single column stacks */
  /* Hero font: 48-60px */
  /* Padding: 80px vertical */
}
```

---

## Success Criteria

**Visual match to Anduril:**
- ✅ Monochromatic color scheme (gray/black/white + orange accent)
- ✅ Oversized typography (120px+ heroes)
- ✅ Asymmetric layouts (60/40, 70/30 splits)
- ✅ Black numbered cards with white text
- ✅ Generous spacing (200px+ sections)
- ✅ Minimal navigation

**Technical requirements:**
- ✅ No animations changed
- ✅ No image changes needed
- ✅ Works with existing build system
- ✅ Responsive across all devices
- ✅ Fast page load (CSS only changes)

**Rollout criteria:**
- ✅ city-services test page approved
- ✅ Typography feels premium and bold
- ✅ Layouts work on mobile/tablet
- ✅ Orange accent used sparingly
- ✅ Ready to migrate other pages

---

## Next Steps

1. **Create implementation plan** (using writing-plans skill)
2. **Set up git worktree** for isolated development
3. **Build test page** (city-services)
4. **Review with stakeholder**
5. **Iterate and approve**
6. **Roll out to remaining pages**

---

## Notes

- Keep existing content structure - only visual redesign
- No animations changes (per requirement)
- Test thoroughly on city-services before rollout
- Orange accent maintains brand recognition
- Incremental approach reduces risk
