# Anduril-Style Redesign Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Transform city-services page to Anduril-style design with monochromatic palette, oversized typography, and asymmetric layouts as test case for site-wide rollout.

**Architecture:** Create new Anduril-specific template and CSS file, leaving existing templates untouched. Use hybrid approach with new `landing-page-anduril.hbs` template and `anduril-style.css` stylesheet. Test on city-services page before rolling out to other pages.

**Tech Stack:** Handlebars templating, CSS Grid, CSS Custom Properties, responsive typography with clamp()

**Design Reference:** `docs/plans/2025-11-23-anduril-style-redesign.md`

---

## Task 1: Create Anduril CSS Variables and Base Styles

**Files:**
- Create: `css/anduril-style.css`

**Step 1: Create CSS file with color system and typography variables**

Create `css/anduril-style.css`:

```css
/* ============================================
   ANDURIL-STYLE DESIGN SYSTEM
   Monochromatic palette with orange accent
   ============================================ */

:root {
  /* Monochromatic Base Colors */
  --anduril-gray-light: #E8E8E8;      /* Primary background */
  --anduril-gray-medium: #CCCCCC;     /* Borders, dividers */
  --anduril-white: #FFFFFF;           /* Alternate sections, cards */
  --anduril-black: #000000;           /* Dark cards, footer, primary text */

  /* Text Colors */
  --anduril-text-primary: #000000;    /* Headlines, body */
  --anduril-text-secondary: #666666;  /* Supporting text */
  --anduril-text-inverse: #FFFFFF;    /* Text on dark backgrounds */

  /* Brand Accent (LIMITED USE) */
  --anduril-orange: #FF6B35;          /* Logo, primary CTA only */

  /* Typography Scale */
  --anduril-font-hero: clamp(80px, 12vw, 140px);
  --anduril-font-section-title: clamp(48px, 8vw, 96px);
  --anduril-font-card-title: clamp(24px, 3vw, 36px);
  --anduril-font-body: 18px;
  --anduril-font-small: 14px;

  /* Font Weights */
  --anduril-weight-normal: 400;
  --anduril-weight-bold: 700;
  --anduril-weight-black: 900;

  /* Letter Spacing */
  --anduril-spacing-hero: -0.04em;      /* Very tight */
  --anduril-spacing-heading: -0.02em;   /* Tight */
  --anduril-spacing-body: 0;            /* Normal */

  /* Line Heights */
  --anduril-line-hero: 0.95;      /* Super tight */
  --anduril-line-heading: 1.1;    /* Tight */
  --anduril-line-body: 1.6;       /* Comfortable */

  /* Font Family */
  --anduril-font-family: 'Inter', 'Helvetica Neue', system-ui, -apple-system, sans-serif;

  /* Spacing */
  --anduril-spacing-section: 200px;
  --anduril-spacing-large: 100px;
  --anduril-spacing-medium: 60px;
  --anduril-spacing-small: 40px;
  --anduril-spacing-xs: 24px;

  /* Layout */
  --anduril-max-width: 1400px;
  --anduril-gap: 24px;
  --anduril-gap-large: 60px;
}

/* ============================================
   BASE STYLES
   ============================================ */

body {
  font-family: var(--anduril-font-family);
  color: var(--anduril-text-primary);
  background-color: var(--anduril-white);
  font-size: var(--anduril-font-body);
  line-height: var(--anduril-line-body);
  letter-spacing: var(--anduril-spacing-body);
}

/* Container */
.anduril-container {
  max-width: var(--anduril-max-width);
  margin: 0 auto;
  padding: 0 var(--anduril-spacing-small);
}

/* Background Colors */
.anduril-bg-light {
  background-color: var(--anduril-gray-light);
}

.anduril-bg-white {
  background-color: var(--anduril-white);
}

.anduril-bg-black {
  background-color: var(--anduril-black);
  color: var(--anduril-text-inverse);
}
```

**Step 2: Commit base styles**

```bash
git add css/anduril-style.css
git commit -m "feat: add Anduril-style CSS variables and base styles"
```

---

## Task 2: Create Anduril Navigation Component

**Files:**
- Create: `templates/components/nav-anduril.hbs`

**Step 1: Create simplified horizontal navigation template**

Create `templates/components/nav-anduril.hbs`:

```handlebars
<nav class="anduril-nav">
    <div class="anduril-container">
        <div class="anduril-nav-content">
            <a href="/" class="anduril-logo">LABRADOR</a>
            <div class="anduril-nav-links">
                <a href="/" class="anduril-nav-link">Home</a>
                <a href="/customers" class="anduril-nav-link">Customers</a>
                <a href="/specifications" class="anduril-nav-link">Product</a>
                <a href="/rental" class="anduril-nav-link">Rental</a>
                <a href="/contact" class="anduril-nav-link">Contact</a>
            </div>
        </div>
    </div>
</nav>
```

**Step 2: Add navigation styles to CSS**

Add to `css/anduril-style.css`:

```css
/* ============================================
   NAVIGATION
   ============================================ */

.anduril-nav {
  background-color: var(--anduril-gray-light);
  border-bottom: 1px solid var(--anduril-gray-medium);
  padding: var(--anduril-spacing-xs) 0;
  position: sticky;
  top: 0;
  z-index: 1000;
}

.anduril-nav-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.anduril-logo {
  font-size: 20px;
  font-weight: var(--anduril-weight-bold);
  color: var(--anduril-orange);
  text-decoration: none;
  letter-spacing: 0.05em;
}

.anduril-nav-links {
  display: flex;
  gap: var(--anduril-spacing-small);
}

.anduril-nav-link {
  font-size: 16px;
  color: var(--anduril-text-primary);
  text-decoration: none;
  transition: color 0.3s ease;
}

.anduril-nav-link:hover {
  color: var(--anduril-orange);
}

/* Responsive Navigation */
@media (max-width: 767px) {
  .anduril-nav-links {
    gap: 20px;
    font-size: 14px;
  }
}
```

**Step 3: Commit navigation component**

```bash
git add templates/components/nav-anduril.hbs css/anduril-style.css
git commit -m "feat: add Anduril-style simplified navigation"
```

---

## Task 3: Create Anduril Hero Component Styles

**Files:**
- Modify: `css/anduril-style.css`

**Step 1: Add hero section styles**

Add to `css/anduril-style.css`:

```css
/* ============================================
   HERO SECTION
   ============================================ */

.anduril-hero {
  background-color: var(--anduril-gray-light);
  padding: var(--anduril-spacing-section) 0;
  min-height: 80vh;
  display: flex;
  align-items: center;
}

.anduril-hero-content {
  max-width: 1000px;
}

.anduril-hero-label {
  font-size: var(--anduril-font-small);
  font-weight: var(--anduril-weight-bold);
  color: var(--anduril-text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin-bottom: var(--anduril-spacing-xs);
}

.anduril-hero-title {
  font-size: var(--anduril-font-hero);
  font-weight: var(--anduril-weight-black);
  line-height: var(--anduril-line-hero);
  letter-spacing: var(--anduril-spacing-hero);
  margin-bottom: var(--anduril-spacing-small);
  color: var(--anduril-text-primary);
}

.anduril-hero-description {
  font-size: var(--anduril-font-body);
  line-height: var(--anduril-line-body);
  color: var(--anduril-text-secondary);
  max-width: 600px;
  margin-bottom: var(--anduril-spacing-medium);
}

.anduril-cta-buttons {
  display: flex;
  gap: var(--anduril-spacing-xs);
  flex-wrap: wrap;
}

/* CTA Buttons */
.btn-anduril-primary {
  background-color: var(--anduril-orange);
  color: var(--anduril-white);
  padding: 16px 32px;
  font-size: 16px;
  font-weight: var(--anduril-weight-bold);
  text-decoration: none;
  border-radius: 4px;
  transition: background-color 0.3s ease, transform 0.2s ease;
  display: inline-block;
}

.btn-anduril-primary:hover {
  background-color: #E55A2B;
  transform: translateY(-2px);
}

.btn-anduril-secondary {
  background-color: transparent;
  color: var(--anduril-text-primary);
  padding: 16px 32px;
  font-size: 16px;
  font-weight: var(--anduril-weight-bold);
  text-decoration: none;
  border: 2px solid var(--anduril-text-primary);
  border-radius: 4px;
  transition: background-color 0.3s ease, color 0.3s ease;
  display: inline-block;
}

.btn-anduril-secondary:hover {
  background-color: var(--anduril-text-primary);
  color: var(--anduril-white);
}

/* Responsive Hero */
@media (max-width: 767px) {
  .anduril-hero {
    padding: 80px 0;
    min-height: 60vh;
  }

  .anduril-cta-buttons {
    flex-direction: column;
  }

  .btn-anduril-primary,
  .btn-anduril-secondary {
    text-align: center;
  }
}
```

**Step 2: Commit hero styles**

```bash
git add css/anduril-style.css
git commit -m "feat: add Anduril-style hero section styles"
```

---

## Task 4: Create Numbered Cards Component Styles

**Files:**
- Modify: `css/anduril-style.css`

**Step 1: Add numbered cards grid and card styles**

Add to `css/anduril-style.css`:

```css
/* ============================================
   NUMBERED CARDS (3-column grid)
   ============================================ */

.anduril-section {
  padding: var(--anduril-spacing-section) 0;
}

.anduril-section-title {
  font-size: var(--anduril-font-section-title);
  font-weight: var(--anduril-weight-black);
  line-height: var(--anduril-line-heading);
  letter-spacing: var(--anduril-spacing-heading);
  margin-bottom: var(--anduril-spacing-medium);
  text-align: left;
}

.anduril-cards-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--anduril-gap);
}

.anduril-card-dark {
  background-color: var(--anduril-black);
  color: var(--anduril-text-inverse);
  padding: var(--anduril-spacing-medium) var(--anduril-spacing-small);
  min-height: 400px;
  display: flex;
  flex-direction: column;
}

.anduril-card-number {
  font-size: 72px;
  font-weight: var(--anduril-weight-bold);
  line-height: 1;
  margin-bottom: var(--anduril-spacing-small);
  color: var(--anduril-text-inverse);
}

.anduril-card-title {
  font-size: var(--anduril-font-card-title);
  font-weight: var(--anduril-weight-bold);
  line-height: var(--anduril-line-heading);
  letter-spacing: var(--anduril-spacing-heading);
  margin-bottom: 20px;
  color: var(--anduril-text-inverse);
}

.anduril-card-description {
  font-size: 16px;
  line-height: var(--anduril-line-body);
  color: var(--anduril-text-inverse);
  opacity: 0.9;
}

/* Responsive Cards Grid */
@media (max-width: 1023px) {
  .anduril-cards-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 767px) {
  .anduril-cards-grid {
    grid-template-columns: 1fr;
  }

  .anduril-card-dark {
    min-height: 300px;
  }
}
```

**Step 2: Commit numbered cards styles**

```bash
git add css/anduril-style.css
git commit -m "feat: add Anduril-style numbered cards component"
```

---

## Task 5: Create Features Grid Component Styles

**Files:**
- Modify: `css/anduril-style.css`

**Step 1: Add 4-column features grid styles**

Add to `css/anduril-style.css`:

```css
/* ============================================
   FEATURES GRID (4-column)
   ============================================ */

.anduril-features-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: var(--anduril-gap);
}

.anduril-feature-card {
  background-color: var(--anduril-black);
  color: var(--anduril-text-inverse);
  padding: var(--anduril-spacing-small);
}

.anduril-feature-card-title {
  font-size: 24px;
  font-weight: var(--anduril-weight-bold);
  line-height: var(--anduril-line-heading);
  letter-spacing: var(--anduril-spacing-heading);
  margin-bottom: 16px;
  color: var(--anduril-text-inverse);
}

.anduril-feature-card-description {
  font-size: 16px;
  line-height: var(--anduril-line-body);
  color: var(--anduril-text-inverse);
  opacity: 0.9;
}

/* Responsive Features Grid */
@media (max-width: 1023px) {
  .anduril-features-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 767px) {
  .anduril-features-grid {
    grid-template-columns: 1fr;
  }
}
```

**Step 2: Commit features grid styles**

```bash
git add css/anduril-style.css
git commit -m "feat: add Anduril-style 4-column features grid"
```

---

## Task 6: Create Footer Component Styles

**Files:**
- Modify: `css/anduril-style.css`

**Step 1: Add footer styles**

Add to `css/anduril-style.css`:

```css
/* ============================================
   FOOTER
   ============================================ */

.anduril-footer {
  background-color: var(--anduril-black);
  color: var(--anduril-text-inverse);
  padding: var(--anduril-spacing-large) var(--anduril-spacing-small) var(--anduril-spacing-medium);
}

.anduril-footer-content {
  display: grid;
  grid-template-columns: 2fr 3fr;
  gap: var(--anduril-gap-large);
  margin-bottom: var(--anduril-spacing-medium);
}

.anduril-footer-brand {
  display: flex;
  flex-direction: column;
}

.anduril-footer-logo {
  font-size: 24px;
  font-weight: var(--anduril-weight-bold);
  color: var(--anduril-orange);
  letter-spacing: 0.05em;
  margin-bottom: 20px;
}

.anduril-footer-links {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: var(--anduril-spacing-small);
}

.anduril-footer-column h4 {
  font-size: 14px;
  font-weight: var(--anduril-weight-bold);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin-bottom: 20px;
  color: var(--anduril-text-inverse);
}

.anduril-footer-column ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.anduril-footer-column li {
  margin-bottom: 12px;
}

.anduril-footer-column a {
  color: var(--anduril-text-inverse);
  text-decoration: none;
  font-size: 16px;
  transition: color 0.3s ease;
}

.anduril-footer-column a:hover {
  color: var(--anduril-orange);
}

.anduril-footer-bottom {
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  padding-top: var(--anduril-spacing-small);
  font-size: var(--anduril-font-small);
  color: rgba(255, 255, 255, 0.6);
}

/* Responsive Footer */
@media (max-width: 767px) {
  .anduril-footer-content {
    grid-template-columns: 1fr;
    gap: var(--anduril-spacing-small);
  }

  .anduril-footer-links {
    grid-template-columns: 1fr;
  }
}
```

**Step 2: Commit footer styles**

```bash
git add css/anduril-style.css
git commit -m "feat: add Anduril-style footer component"
```

---

## Task 7: Create Anduril Page Template

**Files:**
- Create: `templates/pages/landing-page-anduril.hbs`

**Step 1: Create Anduril page template**

Create `templates/pages/landing-page-anduril.hbs`:

```handlebars
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{meta.title}}</title>
    <meta name="description" content="{{meta.description}}">

    <!-- Anduril-style CSS -->
    <link rel="stylesheet" href="/css/anduril-style.css">
</head>
<body>

    {{> nav-anduril}}

    <!-- Hero Section -->
    <section class="anduril-hero">
        <div class="anduril-container">
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
        </div>
    </section>

    <!-- Benefits Section (Numbered Cards) -->
    {{#if benefits}}
    <section class="anduril-section anduril-bg-white">
        <div class="anduril-container">
            <h2 class="anduril-section-title">{{benefits.title}}</h2>
            <div class="anduril-cards-grid">
                {{#each benefits.items}}
                <div class="anduril-card-dark">
                    <div class="anduril-card-number">0{{add @index 1}}</div>
                    <h3 class="anduril-card-title">{{title}}</h3>
                    <p class="anduril-card-description">{{description}}</p>
                </div>
                {{/each}}
            </div>
        </div>
    </section>
    {{/if}}

    <!-- Features Section (4-column Grid) -->
    {{#if features}}
    <section class="anduril-section anduril-bg-light">
        <div class="anduril-container">
            <h2 class="anduril-section-title">{{features.title}}</h2>
            <div class="anduril-features-grid">
                {{#each features.items}}
                <div class="anduril-feature-card">
                    <h3 class="anduril-feature-card-title">{{title}}</h3>
                    <p class="anduril-feature-card-description">{{description}}</p>
                </div>
                {{/each}}
            </div>
        </div>
    </section>
    {{/if}}

    <!-- Footer -->
    <footer class="anduril-footer">
        <div class="anduril-container">
            <div class="anduril-footer-content">
                <div class="anduril-footer-brand">
                    <div class="anduril-footer-logo">LABRADOR</div>
                </div>
                <div class="anduril-footer-links">
                    <div class="anduril-footer-column">
                        <h4>Company</h4>
                        <ul>
                            <li><a href="/about">About</a></li>
                            <li><a href="/contact">Contact</a></li>
                        </ul>
                    </div>
                    <div class="anduril-footer-column">
                        <h4>Product</h4>
                        <ul>
                            <li><a href="/specifications">Specifications</a></li>
                            <li><a href="/rental">Rental</a></li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="anduril-footer-bottom">
                <p>COPYRIGHT © 2025 LABRADOR FIELD SYSTEMS</p>
            </div>
        </div>
    </footer>

</body>
</html>
```

**Step 2: Commit Anduril page template**

```bash
git add templates/pages/landing-page-anduril.hbs
git commit -m "feat: add Anduril-style landing page template"
```

---

## Task 8: Update city-services.json Content

**Files:**
- Modify: `content/pages/city-services.json`

**Step 1: Read current city-services.json**

Run: `cat content/pages/city-services.json`

**Step 2: Update to use Anduril template and new content structure**

Replace entire contents of `content/pages/city-services.json`:

```json
{
  "layout": "landing-page-anduril",
  "meta": {
    "title": "Citypack for City Services | Citypack",
    "description": "Silent battery power for municipal operations and permitted events"
  },
  "hero": {
    "category": "CITY SERVICES",
    "title": "Power Public Events Anywhere",
    "description": "Zero emissions, zero noise, zero permits. Citypack provides silent battery power for city services, public events, and municipal operations without generator drama.",
    "cta": {
      "primary": {
        "text": "Contact Citypack",
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
    "title": "Why Cities Choose Citypack",
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
        "description": "Citypack handles delivery, placement, and pickup. White-glove service ensures your events run smoothly."
      }
    ]
  }
}
```

**Step 3: Commit content update**

```bash
git add content/pages/city-services.json
git commit -m "feat: update city-services to use Anduril template and content"
```

---

## Task 9: Build and Test city-services Page

**Files:**
- N/A (testing only)

**Step 1: Build the site**

Run: `npm run build`

Expected output: Should see "Built 15 HTML pages" including city-services.html

**Step 2: Verify dev server is running**

Check if dev server is already running on http://localhost:3000

If not running:
```bash
npm run dev
```

**Step 3: Open city-services page in browser**

Navigate to: http://localhost:3000/city-services

**Step 4: Visual verification checklist**

Verify the following:
- [ ] Hero section has light gray background (#E8E8E8)
- [ ] Hero title is massive (80-140px range)
- [ ] "CITY SERVICES" label appears above title
- [ ] Two CTA buttons: orange primary + outline secondary
- [ ] Benefits section has 3 black cards with white text
- [ ] Each card shows number (01, 02, 03)
- [ ] Features section has 4-column grid of black cards
- [ ] Footer is black with white text, orange logo
- [ ] Navigation is minimal horizontal links
- [ ] Page is responsive (test at mobile width)

**Step 5: Document any issues**

If issues found, create checklist in TODO.md for fixes needed.

---

## Task 10: Final Verification and Documentation

**Files:**
- Create: `docs/plans/2025-11-23-anduril-rollout-status.md`

**Step 1: Create rollout status document**

Create `docs/plans/2025-11-23-anduril-rollout-status.md`:

```markdown
# Anduril-Style Redesign Rollout Status

**Test Page:** city-services.html
**Status:** Testing Phase
**Date:** 2025-11-23

## Implementation Complete

✅ Task 1: CSS variables and base styles
✅ Task 2: Navigation component
✅ Task 3: Hero section styles
✅ Task 4: Numbered cards component
✅ Task 5: Features grid component
✅ Task 6: Footer component
✅ Task 7: Page template
✅ Task 8: city-services content update
✅ Task 9: Build and test

## Test Results

**Visual Checklist:**
- [ ] Hero section styling
- [ ] Typography scale
- [ ] Numbered cards layout
- [ ] Features grid layout
- [ ] Footer styling
- [ ] Navigation simplicity
- [ ] Mobile responsiveness
- [ ] Color palette (monochromatic + orange)

**Issues Found:**
(Document any issues here)

## Next Steps

**After Approval:**
1. Roll out to customer pages
2. Roll out to product pages
3. Roll out to other pages
4. Update homepage last
5. Archive old templates
6. Remove unused CSS

**Pages to Migrate:**
- experience-agencies.html
- production-managers.html
- gaffers.html
- location-managers.html
- public-venues.html
- street-festivals.html
- specifications.html
- features.html
- gallery.html
- pricing.html
- how-it-works.html
- contact.html
- index.html (homepage - last)
```

**Step 2: Commit rollout status document**

```bash
git add docs/plans/2025-11-23-anduril-rollout-status.md
git commit -m "docs: add Anduril redesign rollout status tracker"
```

**Step 3: Verify all files are committed**

Run: `git status`

Expected: Working tree clean (all changes committed)

---

## Success Criteria

**Implementation complete when:**
- ✅ All CSS styles created in `css/anduril-style.css`
- ✅ Navigation component created and styled
- ✅ Page template created with all sections
- ✅ city-services.json updated with new content structure
- ✅ Site builds successfully without errors
- ✅ city-services page loads at http://localhost:3000/city-services
- ✅ Visual design matches Anduril reference (monochromatic, oversized type, asymmetric layouts)
- ✅ Page is fully responsive (mobile, tablet, desktop)
- ✅ All commits made with descriptive messages

**Ready for stakeholder review when:**
- ✅ Visual checklist in Task 9 is complete
- ✅ No console errors in browser
- ✅ Page loads in under 2 seconds
- ✅ Orange accent appears ONLY in logo and primary CTA
- ✅ Typography feels bold and premium

---

## Notes

- This implementation creates NEW files, leaving existing templates untouched
- Existing pages continue to work with old design
- city-services becomes isolated test case
- After approval, other pages migrate one by one
- Incremental approach reduces risk
- Can easily revert city-services if needed

---

## Reference Files

- Design spec: `docs/plans/2025-11-23-anduril-style-redesign.md`
- Rollout tracker: `docs/plans/2025-11-23-anduril-rollout-status.md`
- Test page: http://localhost:3000/city-services
