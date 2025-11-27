# Implementation Plan: Anduril-Inspired Grid Layout for Citypack

**Date:** November 27, 2025
**Author:** Claude Code
**Status:** Ready for Implementation

## Executive Summary

This plan outlines the implementation of a grid-based layout system inspired by Anduril's homepage design. The layout will maintain Citypack's orange-gold color scheme while adopting Anduril's sophisticated grid structure, asymmetric compositions, and content presentation patterns.

## Design Analysis: Anduril Homepage

### Visual Analysis from Screenshots

**Above the Fold:**
- Full-width hero video/image background
- Minimal navigation (clean, top-aligned)
- Dark theme with high contrast
- Centered or minimal text overlay

**Below the Fold - Product Grid:**
- **Bento-box style grid layout** (varying cell sizes)
- 3-column base grid with merged cells
- Product cards with:
  - Large background images
  - Product name overlaid
  - Hover interactions
- Asymmetric layout (different sized cells create visual interest)

**Content Sections:**
- Full-width feature sections
- Large imagery with minimal text
- "News & Insights" section with article cards
- Split layouts (50/50 text/image)

**Footer:**
- Dark background
- Multi-column layout
- Clean typography

### Grid Structure Analysis

**Product Grid Pattern (Below the Fold 1):**
```
Row 1: [1 cell] [1 cell] [1 cell]
Row 2: [1 cell] [2 cells merged - wider]
Row 3: [1 cell] [1 cell] [1 cell]
```

**Characteristics:**
- Base 3-column grid
- Strategic cell merging for emphasis
- Equal-height rows
- Minimal gap between cells (tight grid)
- Hover effects reveal product names
- Dark overlays on images for text legibility

## Citypack Adaptation Strategy

### Design Principles

**Keep from Anduril:**
- ✅ Bento-box grid layout system
- ✅ Asymmetric compositions
- ✅ Large imagery focus
- ✅ Minimal text overlays
- ✅ Clean navigation
- ✅ Full-width sections
- ✅ Tight grid gaps

**Adapt for Citypack:**
- 🔄 Use Citypack orange-gold color scheme
- 🔄 Battery/power imagery instead of defense products
- 🔄 Warmer color overlays (vs Anduril's cool blues)
- 🔄 Industry-specific content (production, events, etc.)

**Color Scheme:**
```css
/* Citypack Colors (from existing design system) */
--primary-orange: #FF6B35
--accent-gold: #F4B942
--gradient-primary: linear-gradient(135deg, #FF6B35 0%, #F4B942 100%)
--neutral-charcoal: #2C3E50
--text-primary: #0d1117

/* Dark Theme Overlays */
--overlay-dark: rgba(44, 62, 80, 0.85)
--overlay-gradient: linear-gradient(to bottom, rgba(255, 107, 53, 0.2), rgba(44, 62, 80, 0.9))
```

## Implementation Plan

### Phase 1: Create Grid System CSS (30 minutes)

#### Task 1.1: New CSS file for grid system
**File:** `css/grid-system.css`

**Create modular grid system:**

```css
/* ============================================
   CITYPACK GRID SYSTEM
   Anduril-inspired bento-box grid layout
   ============================================ */

/* Grid Container */
.grid-container {
    display: grid;
    grid-template-columns: repeat(12, 1fr);
    gap: 8px;
    padding: 0;
    width: 100%;
    max-width: 100vw;
}

/* Tight grid for bento-box style */
.grid-container.tight {
    gap: 4px;
}

.grid-container.standard {
    gap: 16px;
}

.grid-container.loose {
    gap: 24px;
}

/* Grid Items - Flexible Column Spans */
.grid-item {
    position: relative;
    overflow: hidden;
    background: var(--neutral-charcoal);
    border-radius: 0; /* Anduril uses sharp corners */
}

/* Column spans (12-column system) */
.span-1 { grid-column: span 1; }
.span-2 { grid-column: span 2; }
.span-3 { grid-column: span 3; }
.span-4 { grid-column: span 4; }
.span-5 { grid-column: span 5; }
.span-6 { grid-column: span 6; }
.span-7 { grid-column: span 7; }
.span-8 { grid-column: span 8; }
.span-9 { grid-column: span 9; }
.span-10 { grid-column: span 10; }
.span-11 { grid-column: span 11; }
.span-12 { grid-column: span 12; }

/* Row spans */
.row-span-1 { grid-row: span 1; }
.row-span-2 { grid-row: span 2; }
.row-span-3 { grid-row: span 3; }

/* Aspect Ratios */
.aspect-square { aspect-ratio: 1 / 1; }
.aspect-portrait { aspect-ratio: 3 / 4; }
.aspect-landscape { aspect-ratio: 4 / 3; }
.aspect-wide { aspect-ratio: 16 / 9; }
.aspect-ultra-wide { aspect-ratio: 21 / 9; }

/* Grid Card Components */
.grid-card {
    position: relative;
    overflow: hidden;
    cursor: pointer;
    transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.grid-card:hover {
    transform: scale(1.02);
    z-index: 10;
}

.grid-card-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

.grid-card:hover .grid-card-image {
    transform: scale(1.05);
}

.grid-card-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(
        to bottom,
        rgba(255, 107, 53, 0.1) 0%,
        rgba(44, 62, 80, 0.85) 100%
    );
    opacity: 0.9;
    transition: opacity 0.3s ease;
}

.grid-card:hover .grid-card-overlay {
    opacity: 1;
}

.grid-card-content {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    padding: 32px;
    color: white;
    z-index: 2;
}

.grid-card-title {
    font-size: 32px;
    font-weight: 700;
    margin: 0 0 8px 0;
    color: white;
}

.grid-card-subtitle {
    font-size: 14px;
    font-weight: 400;
    margin: 0;
    color: rgba(255, 255, 255, 0.8);
}

.grid-card-cta {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    margin-top: 16px;
    font-size: 14px;
    font-weight: 600;
    color: var(--accent-gold);
    text-decoration: none;
    opacity: 0;
    transform: translateY(10px);
    transition: all 0.3s ease;
}

.grid-card:hover .grid-card-cta {
    opacity: 1;
    transform: translateY(0);
}

.grid-card-cta::after {
    content: '→';
    font-size: 18px;
}

/* Responsive Grid */
@media (max-width: 1024px) {
    .grid-container {
        grid-template-columns: repeat(6, 1fr);
    }

    /* Adjust spans for tablet */
    .span-4, .span-5, .span-6, .span-7, .span-8 {
        grid-column: span 6;
    }
}

@media (max-width: 768px) {
    .grid-container {
        grid-template-columns: repeat(2, 1fr);
        gap: 8px;
    }

    /* Stack on mobile */
    .span-1, .span-2, .span-3, .span-4, .span-5, .span-6,
    .span-7, .span-8, .span-9, .span-10, .span-11, .span-12 {
        grid-column: span 2;
    }

    .grid-card-content {
        padding: 20px;
    }

    .grid-card-title {
        font-size: 24px;
    }
}
```

---

### Phase 2: Create Homepage Grid Layout (60 minutes)

#### Task 2.1: Update home page template
**File:** `templates/pages/home-page.hbs`

**New structure:**

```handlebars
<!-- Hero Section - Full Width -->
<section class="hero-full">
    <div class="hero-video-container">
        <div class="hero-overlay"></div>
        <div class="hero-content">
            <h1 class="hero-title">{{hero.title}}</h1>
            <p class="hero-subtitle">{{hero.tagline}}</p>
        </div>
    </div>
</section>

<!-- Product/Solution Grid - Bento Box Style -->
<section class="products-grid-section">
    <div class="grid-container tight">

        <!-- Row 1: 3 equal columns -->
        <a href="/solutions/compact" class="grid-card span-4 aspect-square">
            <img src="images/compact-systems.jpg" alt="Compact Systems" class="grid-card-image">
            <div class="grid-card-overlay"></div>
            <div class="grid-card-content">
                <h3 class="grid-card-title">Compact Systems</h3>
                <p class="grid-card-subtitle">2-5kW Power</p>
                <span class="grid-card-cta">Explore</span>
            </div>
        </a>

        <a href="/solutions/mid-range" class="grid-card span-4 aspect-square">
            <img src="images/mid-range-systems.jpg" alt="Mid-Range" class="grid-card-image">
            <div class="grid-card-overlay"></div>
            <div class="grid-card-content">
                <h3 class="grid-card-title">Mid-Range Systems</h3>
                <p class="grid-card-subtitle">5-10kW Power</p>
                <span class="grid-card-cta">Explore</span>
            </div>
        </a>

        <a href="/solutions/high-capacity" class="grid-card span-4 aspect-square">
            <img src="images/high-capacity.jpg" alt="High Capacity" class="grid-card-image">
            <div class="grid-card-overlay"></div>
            <div class="grid-card-content">
                <h3 class="grid-card-title">High-Capacity Systems</h3>
                <p class="grid-card-subtitle">10kW+ Power</p>
                <span class="grid-card-cta">Explore</span>
            </div>
        </a>

        <!-- Row 2: 1 narrow + 1 wide -->
        <a href="/customers/production" class="grid-card span-4 aspect-portrait">
            <img src="images/film-production.jpg" alt="Film Production" class="grid-card-image">
            <div class="grid-card-overlay"></div>
            <div class="grid-card-content">
                <h3 class="grid-card-title">Film Production</h3>
                <p class="grid-card-subtitle">Silent power for any set</p>
                <span class="grid-card-cta">Learn More</span>
            </div>
        </a>

        <a href="/customers/events" class="grid-card span-8 aspect-landscape">
            <img src="images/events.jpg" alt="Events" class="grid-card-image">
            <div class="grid-card-overlay"></div>
            <div class="grid-card-content">
                <h3 class="grid-card-title">Events & Activations</h3>
                <p class="grid-card-subtitle">Power experiences anywhere</p>
                <span class="grid-card-cta">Learn More</span>
            </div>
        </a>

        <!-- Row 3: 3 equal columns -->
        <a href="/features" class="grid-card span-4 aspect-square">
            <img src="images/monitoring.jpg" alt="Monitoring" class="grid-card-image">
            <div class="grid-card-overlay"></div>
            <div class="grid-card-content">
                <h3 class="grid-card-title">Smart Monitoring</h3>
                <p class="grid-card-subtitle">Real-time power tracking</p>
                <span class="grid-card-cta">View Features</span>
            </div>
        </a>

        <a href="/specifications" class="grid-card span-4 aspect-square">
            <img src="images/charging.jpg" alt="Fast Charging" class="grid-card-image">
            <div class="grid-card-overlay"></div>
            <div class="grid-card-content">
                <h3 class="grid-card-title">Fast Charging</h3>
                <p class="grid-card-subtitle">Rapid turnaround</p>
                <span class="grid-card-cta">View Specs</span>
            </div>
        </a>

        <a href="/contact" class="grid-card span-4 aspect-square">
            <img src="images/service.jpg" alt="Service" class="grid-card-image">
            <div class="grid-card-overlay"></div>
            <div class="grid-card-content">
                <h3 class="grid-card-title">White-Glove Service</h3>
                <p class="grid-card-subtitle">Full support included</p>
                <span class="grid-card-cta">Get Started</span>
            </div>
        </a>

    </div>
</section>

<!-- Feature Section - Full Width -->
<section class="feature-full">
    <div class="feature-split">
        <div class="feature-image">
            <img src="images/facility.jpg" alt="Citypack Facility">
        </div>
        <div class="feature-content">
            <h2>Built for Reliability</h2>
            <p>Our battery systems are engineered for professional applications where failure is not an option.</p>
            <a href="/about" class="btn-secondary">Learn More →</a>
        </div>
    </div>
</section>

<!-- News/Blog Grid -->
{{#if news}}
<section class="news-section">
    <div class="section-header">
        <h2>News & Insights</h2>
        <a href="/blog" class="view-all">All Articles →</a>
    </div>

    <div class="grid-container standard">
        {{#each news}}
        <article class="grid-card span-4 aspect-landscape">
            <img src="{{image}}" alt="{{title}}" class="grid-card-image">
            <div class="grid-card-overlay"></div>
            <div class="grid-card-content">
                <p class="article-date">{{date}}</p>
                <h3 class="grid-card-title">{{title}}</h3>
                <span class="grid-card-cta">Read More</span>
            </div>
        </article>
        {{/each}}
    </div>
</section>
{{/if}}
```

---

#### Task 2.2: Hero section styling
**Add to:** `css/components.css`

```css
/* ============================================
   HERO - FULL WIDTH ANDURIL STYLE
   ============================================ */

.hero-full {
    width: 100vw;
    height: 90vh;
    min-height: 600px;
    position: relative;
    overflow: hidden;
}

.hero-video-container {
    width: 100%;
    height: 100%;
    position: relative;
}

.hero-video-container::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(
        to bottom,
        rgba(13, 17, 23, 0.3) 0%,
        rgba(13, 17, 23, 0.7) 100%
    );
    z-index: 1;
}

.hero-video-container video,
.hero-video-container img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.hero-overlay {
    position: absolute;
    inset: 0;
    background: radial-gradient(
        circle at center,
        transparent 0%,
        rgba(13, 17, 23, 0.4) 100%
    );
    z-index: 1;
}

.hero-content {
    position: absolute;
    bottom: 80px;
    left: 40px;
    right: 40px;
    z-index: 2;
    color: white;
    max-width: 800px;
}

.hero-title {
    font-size: 72px;
    font-weight: 800;
    line-height: 1.1;
    margin: 0 0 16px 0;
    color: white;
    text-shadow: 0 2px 20px rgba(0, 0, 0, 0.3);
}

.hero-subtitle {
    font-size: 24px;
    font-weight: 400;
    line-height: 1.4;
    margin: 0;
    color: rgba(255, 255, 255, 0.9);
}

@media (max-width: 768px) {
    .hero-full {
        height: 70vh;
        min-height: 500px;
    }

    .hero-content {
        bottom: 40px;
        left: 20px;
        right: 20px;
    }

    .hero-title {
        font-size: 48px;
    }

    .hero-subtitle {
        font-size: 18px;
    }
}
```

---

#### Task 2.3: Feature section styling
**Add to:** `css/layouts.css`

```css
/* ============================================
   FULL WIDTH FEATURE SECTIONS
   ============================================ */

.feature-full {
    width: 100vw;
    margin: 80px 0;
}

.feature-split {
    display: grid;
    grid-template-columns: 1fr 1fr;
    min-height: 600px;
}

.feature-image {
    position: relative;
    overflow: hidden;
}

.feature-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.feature-content {
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 80px;
    background: var(--neutral-light);
}

.feature-content h2 {
    font-size: 48px;
    font-weight: 700;
    margin: 0 0 24px 0;
}

.feature-content p {
    font-size: 20px;
    line-height: 1.6;
    margin: 0 0 32px 0;
    color: var(--text-secondary);
}

@media (max-width: 1024px) {
    .feature-split {
        grid-template-columns: 1fr;
    }

    .feature-content {
        padding: 60px 40px;
    }
}

@media (max-width: 768px) {
    .feature-content {
        padding: 40px 24px;
    }

    .feature-content h2 {
        font-size: 36px;
    }

    .feature-content p {
        font-size: 18px;
    }
}
```

---

#### Task 2.4: News section styling
**Add to:** `css/components.css`

```css
/* ============================================
   NEWS & INSIGHTS SECTION
   ============================================ */

.news-section {
    padding: 120px 40px;
    background: white;
}

.section-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 48px;
}

.section-header h2 {
    font-size: 48px;
    font-weight: 700;
    margin: 0;
}

.view-all {
    font-size: 16px;
    font-weight: 600;
    color: var(--primary-orange);
    text-decoration: none;
    transition: color 0.3s ease;
}

.view-all:hover {
    color: var(--accent-gold);
}

.article-date {
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: var(--accent-gold);
    margin: 0 0 12px 0;
}

@media (max-width: 768px) {
    .news-section {
        padding: 80px 24px;
    }

    .section-header {
        flex-direction: column;
        align-items: flex-start;
        gap: 16px;
    }

    .section-header h2 {
        font-size: 36px;
    }
}
```

---

### Phase 3: Update Homepage Content Structure (30 minutes)

#### Task 3.1: Update home.json
**File:** `content/pages/home.json`

**Add grid content structure:**

```json
{
  "layout": "home-page",
  "meta": {
    "title": "Citypack | Professional Battery Solutions",
    "description": "Power solutions tailored to your needs. From compact systems to high-capacity power, Citypack delivers the right battery for your application."
  },
  "hero": {
    "title": "Power Solutions for Every Application",
    "tagline": "Professional battery systems sized for your needs. Silent, reliable, ready when you are.",
    "videoUrl": "/videos/hero-background.mp4",
    "videoFallback": "/images/hero-fallback.jpg"
  },
  "productGrid": [
    {
      "title": "Compact Systems",
      "subtitle": "2-5kW Power",
      "image": "/images/compact-systems.jpg",
      "link": "/specifications#compact",
      "color": "orange"
    },
    {
      "title": "Mid-Range Systems",
      "subtitle": "5-10kW Power",
      "image": "/images/mid-range-systems.jpg",
      "link": "/specifications#mid-range",
      "color": "gold"
    },
    {
      "title": "High-Capacity Systems",
      "subtitle": "10kW+ Power",
      "image": "/images/high-capacity-systems.jpg",
      "link": "/specifications#high-capacity",
      "color": "charcoal"
    }
  ],
  "customerGrid": [
    {
      "title": "Film Production",
      "subtitle": "Silent power for any set",
      "image": "/images/film-production.jpg",
      "link": "/production-managers",
      "size": "normal"
    },
    {
      "title": "Events & Activations",
      "subtitle": "Power experiences anywhere",
      "image": "/images/events-activations.jpg",
      "link": "/experience-agencies",
      "size": "wide"
    }
  ],
  "featureGrid": [
    {
      "title": "Smart Monitoring",
      "subtitle": "Real-time power tracking",
      "image": "/images/monitoring.jpg",
      "link": "/features#monitoring"
    },
    {
      "title": "Fast Charging",
      "subtitle": "Rapid turnaround",
      "image": "/images/fast-charging.jpg",
      "link": "/features#charging"
    },
    {
      "title": "White-Glove Service",
      "subtitle": "Full support included",
      "image": "/images/service.jpg",
      "link": "/contact"
    }
  ],
  "feature": {
    "title": "Built for Reliability",
    "description": "Our battery systems are engineered for professional applications where failure is not an option. Every system undergoes rigorous testing before deployment.",
    "image": "/images/facility.jpg",
    "cta": {
      "text": "Learn More",
      "link": "/about"
    }
  },
  "news": [
    {
      "date": "11/24/2025",
      "title": "Powering Major Productions Across the Industry",
      "image": "/images/news-1.jpg",
      "link": "/blog/powering-productions"
    },
    {
      "date": "11/15/2025",
      "title": "New High-Capacity Systems Now Available",
      "image": "/images/news-2.jpg",
      "link": "/blog/high-capacity-launch"
    },
    {
      "date": "11/08/2025",
      "title": "Why Silent Power Matters for Events",
      "image": "/images/news-3.jpg",
      "link": "/blog/silent-power"
    }
  ]
}
```

---

### Phase 4: Create Reusable Grid Components (45 minutes)

#### Task 4.1: Grid card component template
**File:** `templates/components/grid-card.hbs`

```handlebars
<a href="{{link}}" class="grid-card {{spanClass}} {{aspectClass}}">
    <img src="{{image}}" alt="{{title}}" class="grid-card-image">
    <div class="grid-card-overlay"></div>
    <div class="grid-card-content">
        {{#if date}}
        <p class="article-date">{{date}}</p>
        {{/if}}
        <h3 class="grid-card-title">{{title}}</h3>
        {{#if subtitle}}
        <p class="grid-card-subtitle">{{subtitle}}</p>
        {{/if}}
        <span class="grid-card-cta">{{ctaText}}</span>
    </div>
</a>
```

---

#### Task 4.2: Grid container component template
**File:** `templates/components/grid-container.hbs`

```handlebars
<div class="grid-container {{spacing}}">
    {{#each items}}
        {{> grid-card}}
    {{/each}}
</div>
```

---

### Phase 5: Implement on Additional Pages (60 minutes)

#### Task 5.1: Customer landing pages with grid
**Apply to:** All customer landing pages

**Pattern:**
```handlebars
<!-- Hero -->
<section class="hero-full">...</section>

<!-- Benefits Grid -->
<section class="benefits-section">
    <div class="grid-container standard">
        {{#each benefits}}
        <div class="grid-card span-4 aspect-square">
            <div class="benefit-icon">{{icon}}</div>
            <h3>{{title}}</h3>
            <p>{{description}}</p>
        </div>
        {{/each}}
    </div>
</section>

<!-- Feature Showcase Grid -->
<section class="features-grid-section">
    <div class="grid-container tight">
        <!-- Asymmetric grid like homepage -->
    </div>
</section>
```

---

#### Task 5.2: Solutions page with product grid
**File:** `templates/pages/solutions-page.hbs`

**Grid for showcasing different battery solutions:**
```handlebars
<section class="solutions-grid">
    <div class="grid-container tight">
        <!-- 3-column grid of solutions -->
        <!-- Each solution card spans 4 columns -->
        <!-- Hover reveals specs and CTA -->
    </div>
</section>
```

---

### Phase 6: Image Placeholders & Assets (30 minutes)

#### Task 6.1: Create placeholder images
**Directory:** `images/`

**Required images:**
- Hero backgrounds (1920x1080)
- Product/solution images (800x800, 1200x800, 800x1200)
- Customer/industry images (1200x800)
- Feature images (1200x800)
- News/blog images (800x600)

**Temporary approach:**
```css
/* Placeholder backgrounds with gradients */
.grid-card[data-placeholder="1"] {
    background: linear-gradient(135deg, #FF6B35 0%, #F4B942 100%);
}

.grid-card[data-placeholder="2"] {
    background: linear-gradient(135deg, #F4B942 0%, #FF6B35 100%);
}

.grid-card[data-placeholder="3"] {
    background: linear-gradient(135deg, #2C3E50 0%, #FF6B35 100%);
}
```

---

### Phase 7: Testing & Refinement (45 minutes)

#### Task 7.1: Responsive testing
**Test at breakpoints:**
- 1920px (desktop)
- 1440px (laptop)
- 1024px (tablet landscape)
- 768px (tablet portrait)
- 375px (mobile)

**Verify:**
- Grid reflows correctly
- Images maintain aspect ratios
- Text remains legible
- Touch targets adequate (minimum 44x44px)
- Hover states work on desktop
- Tap interactions work on mobile

---

#### Task 7.2: Performance optimization
**Checks:**
```bash
# Image optimization
- Compress all images to WebP
- Implement lazy loading
- Use srcset for responsive images

# CSS optimization
- Combine grid-system.css into build
- Minify for production
- Remove unused styles

# Animation performance
- Use transform/opacity only (GPU-accelerated)
- Reduce motion for accessibility
- Test on lower-end devices
```

---

#### Task 7.3: Accessibility audit
**Requirements:**
- All images have alt text
- Links have descriptive text (not just "Learn More")
- Color contrast meets WCAG AA (4.5:1)
- Keyboard navigation works
- Focus indicators visible
- Screen reader friendly

---

### Phase 8: Build & Deploy (15 minutes)

#### Task 8.1: Update build system
**Add to:** `package.json`

```json
{
  "scripts": {
    "build": "node src/build.js",
    "build:css": "postcss css/*.css --dir dist/css",
    "build:images": "node src/optimize-images.js",
    "build:all": "npm run build:css && npm run build:images && npm run build"
  }
}
```

---

#### Task 8.2: Deploy to staging
**Commands:**
```bash
npm run build
npm run validate
# Review build output
# Deploy to staging environment
```

---

## Grid Layout Patterns Library

### Pattern 1: Equal 3-Column Grid
```html
<div class="grid-container tight">
    <div class="grid-card span-4 aspect-square">...</div>
    <div class="grid-card span-4 aspect-square">...</div>
    <div class="grid-card span-4 aspect-square">...</div>
</div>
```

**Use for:** Product categories, feature highlights, service offerings

---

### Pattern 2: Asymmetric Bento Box (1+2 columns)
```html
<div class="grid-container tight">
    <div class="grid-card span-4 aspect-portrait">...</div>
    <div class="grid-card span-8 aspect-landscape">...</div>
</div>
```

**Use for:** Featured content, case studies, hero modules

---

### Pattern 3: Mixed Height Grid
```html
<div class="grid-container tight">
    <div class="grid-card span-4 aspect-square">...</div>
    <div class="grid-card span-4 row-span-2 aspect-portrait">...</div>
    <div class="grid-card span-4 aspect-square">...</div>
    <div class="grid-card span-4 aspect-square">...</div>
    <div class="grid-card span-4 aspect-square">...</div>
</div>
```

**Use for:** Image galleries, portfolio showcases

---

### Pattern 4: Full-Width Feature
```html
<div class="grid-container standard">
    <div class="grid-card span-12 aspect-ultra-wide">...</div>
</div>
```

**Use for:** Hero images, major announcements, video embeds

---

### Pattern 5: 4-Column Grid
```html
<div class="grid-container standard">
    <div class="grid-card span-3 aspect-square">...</div>
    <div class="grid-card span-3 aspect-square">...</div>
    <div class="grid-card span-3 aspect-square">...</div>
    <div class="grid-card span-3 aspect-square">...</div>
</div>
```

**Use for:** Benefits, features, statistics, team members

---

## Color Scheme Application

### Grid Overlays
```css
/* Warm overlay (Citypack brand) */
.grid-card-overlay.warm {
    background: linear-gradient(
        to bottom,
        rgba(255, 107, 53, 0.2) 0%,
        rgba(244, 185, 66, 0.3) 50%,
        rgba(44, 62, 80, 0.9) 100%
    );
}

/* Dark overlay (premium feel) */
.grid-card-overlay.dark {
    background: linear-gradient(
        to bottom,
        rgba(13, 17, 23, 0.3) 0%,
        rgba(13, 17, 23, 0.9) 100%
    );
}

/* Accent overlay (highlight items) */
.grid-card-overlay.accent {
    background: linear-gradient(
        135deg,
        rgba(255, 107, 53, 0.8) 0%,
        rgba(244, 185, 66, 0.8) 100%
    );
}
```

---

## File Structure

```
citypack-website/
├── css/
│   ├── grid-system.css          # NEW: Grid layout system
│   ├── design-system.css         # Existing: Colors, typography
│   ├── components.css            # Updated: Hero, cards, news
│   └── layouts.css               # Updated: Feature sections
├── templates/
│   ├── pages/
│   │   └── home-page.hbs         # Updated: Grid layout
│   └── components/
│       ├── grid-card.hbs         # NEW: Reusable grid card
│       └── grid-container.hbs    # NEW: Grid wrapper
├── content/
│   └── pages/
│       └── home.json             # Updated: Grid content structure
└── images/                        # NEW: Grid images
    ├── hero/
    ├── products/
    ├── customers/
    └── features/
```

---

## Success Criteria

✅ **Complete when:**
1. Grid system CSS implemented and responsive
2. Homepage uses bento-box grid layout
3. Grid components are reusable across pages
4. Color scheme uses Citypack orange-gold palette
5. All images have proper aspect ratios
6. Hover interactions work smoothly
7. Mobile experience is excellent
8. Build system includes new grid CSS
9. Content validates and builds successfully
10. Performance metrics are acceptable (Lighthouse >90)

---

## Timeline

**Total Estimated Time:** ~6 hours

- Phase 1 (Grid CSS): 30 min
- Phase 2 (Homepage Layout): 60 min
- Phase 3 (Content Structure): 30 min
- Phase 4 (Reusable Components): 45 min
- Phase 5 (Additional Pages): 60 min
- Phase 6 (Image Assets): 30 min
- Phase 7 (Testing): 45 min
- Phase 8 (Build & Deploy): 15 min

---

## Next Steps After Implementation

**Immediate:**
1. Gather real product/solution images
2. Create video content for hero section
3. Write compelling copy for grid cards

**Short-term:**
4. Implement grid on all customer pages
5. Create grid variations for different page types
6. A/B test grid layouts for engagement

**Long-term:**
7. Build CMS integration for grid content
8. Create animation library for grid interactions
9. Develop grid-based blog/news system

---

**End of Implementation Plan**
