# Site Navigation & Information Architecture Restructure

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Restructure the LAB SEVEN website with proper navigation hierarchy that integrates 7 new persona-focused landing pages into a cohesive site architecture with dropdown menus and dedicated section pages.

**Architecture:** Transform the current single-page site into a multi-page architecture with:
- Homepage hub with overview content
- "Solutions" dropdown menu for 7 persona landing pages
- Dedicated pages for Specs, Features, Gallery, Pricing, Roadmap sections
- Updated global navigation that works across all pages
- Consistent design system and component usage

**Tech Stack:** Handlebars templates, JSON content, existing CSS design system, Node.js build system

---

## Current State Analysis

**Current Homepage (`index.html`):**
- Navigation: Specs | Features | Gallery | Pricing | Roadmap | Contact (all anchor links to same page)
- Footer: Shows "Solutions" menu with Film & TV, Commercial, Events, Enterprise (placeholder links)
- All content on one scrolling page

**New Persona Pages (7 pages):**
- experience-agencies.html
- city-services.html
- gaffers.html
- production-managers.html
- location-managers.html
- public-venues.html
- street-festivals.html

**Problem:** Navigation links go to anchor sections (#specs, #features) but those sections should be separate pages. Persona pages have no home in current nav structure.

---

## Proposed Information Architecture

```
LAB SEVEN Site Structure
│
├── Home (/)
│   ├── Hero + Overview
│   ├── Quick Specs Summary
│   ├── Key Features Highlights
│   └── CTA to Solutions & Rental
│
├── Solutions (dropdown menu)
│   ├── Experience Agencies
│   ├── Production Managers
│   ├── Gaffers & Lighting
│   ├── Location Managers
│   ├── City Services & Permits
│   ├── Public Venues & Events
│   └── Street Festivals
│
├── Product
│   ├── Specifications (full specs page)
│   ├── Features (detailed features page)
│   └── Gallery (image gallery page)
│
├── Rental
│   ├── Pricing (rates & options)
│   └── How It Works
│
├── Roadmap (future products)
│
└── Contact
```

**Navigation Bar Structure:**
```
[LABRADOR LOGO]  Solutions ▾  |  Product ▾  |  Rental ▾  |  Roadmap  |  Contact
```

---

## Task 1: Create Global Navigation Component with Dropdowns

**Goal:** Replace hardcoded nav with template-driven navigation supporting dropdown menus

**Files:**
- Modify: `content/global/navigation.json`
- Create: `templates/components/nav-with-dropdowns.hbs`
- Modify: `templates/components/nav.hbs` (update to use new structure)

**Step 1: Update navigation JSON schema to support dropdowns**

Create `content/global/navigation.json`:
```json
{
  "logo": "LABRADOR",
  "menuItems": [
    {
      "label": "Solutions",
      "dropdown": true,
      "items": [
        { "text": "Experience Agencies", "href": "/experience-agencies" },
        { "text": "Production Managers", "href": "/production-managers" },
        { "text": "Gaffers & Lighting", "href": "/gaffers" },
        { "text": "Location Managers", "href": "/location-managers" },
        { "text": "City Services & Permits", "href": "/city-services" },
        { "text": "Public Venues & Events", "href": "/public-venues" },
        { "text": "Street Festivals", "href": "/street-festivals" }
      ]
    },
    {
      "label": "Product",
      "dropdown": true,
      "items": [
        { "text": "Specifications", "href": "/specifications" },
        { "text": "Features", "href": "/features" },
        { "text": "Gallery", "href": "/gallery" }
      ]
    },
    {
      "label": "Rental",
      "dropdown": true,
      "items": [
        { "text": "Pricing", "href": "/pricing" },
        { "text": "How It Works", "href": "/how-it-works" }
      ]
    },
    {
      "label": "Roadmap",
      "href": "/roadmap"
    },
    {
      "label": "Contact",
      "href": "/contact"
    }
  ]
}
```

**Step 2: Create dropdown navigation template**

Create `templates/components/nav-with-dropdowns.hbs`:
```handlebars
<nav>
    <div class="nav-wrapper">
        <a href="/" class="logo">{{logo}}</a>
        <ul class="nav-items">
            {{#each menuItems}}
            {{#if dropdown}}
            <li class="nav-dropdown">
                <button class="nav-dropdown-toggle">
                    {{label}} <span class="dropdown-arrow">▾</span>
                </button>
                <ul class="nav-dropdown-menu">
                    {{#each items}}
                    <li><a href="{{href}}">{{text}}</a></li>
                    {{/each}}
                </ul>
            </li>
            {{else}}
            <li><a href="{{href}}">{{label}}</a></li>
            {{/if}}
            {{/each}}
        </ul>
    </div>
</nav>
```

**Step 3: Add dropdown CSS styles**

Add to `css/components.css`:
```css
/* Navigation Dropdown Styles */
.nav-dropdown {
    position: relative;
}

.nav-dropdown-toggle {
    background: none;
    border: none;
    color: var(--text-primary);
    font-size: var(--font-size-16);
    font-weight: var(--font-weight-medium);
    cursor: pointer;
    padding: var(--space-8) var(--space-16);
    display: flex;
    align-items: center;
    gap: var(--space-4);
    transition: color var(--transition-fast);
}

.nav-dropdown-toggle:hover {
    color: var(--primary-orange);
}

.dropdown-arrow {
    font-size: var(--font-size-12);
    transition: transform var(--transition-fast);
}

.nav-dropdown:hover .dropdown-arrow {
    transform: rotate(180deg);
}

.nav-dropdown-menu {
    position: absolute;
    top: 100%;
    left: 0;
    background: var(--white);
    border: 1px solid var(--border-light);
    border-radius: var(--radius-md);
    box-shadow: 0 4px 12px var(--shadow-medium);
    min-width: 240px;
    padding: var(--space-8) 0;
    opacity: 0;
    visibility: hidden;
    transform: translateY(-10px);
    transition: all var(--transition-fast) var(--easing-standard);
    z-index: 1000;
}

.nav-dropdown:hover .nav-dropdown-menu {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
}

.nav-dropdown-menu li {
    list-style: none;
}

.nav-dropdown-menu a {
    display: block;
    padding: var(--space-12) var(--space-20);
    color: var(--text-primary);
    text-decoration: none;
    font-size: var(--font-size-14);
    transition: all var(--transition-fast);
}

.nav-dropdown-menu a:hover {
    background: var(--neutral-light);
    color: var(--primary-orange);
    padding-left: var(--space-24);
}
```

**Step 4: Update build system to use new nav component**

Modify `templates/layouts/base.hbs` to use `nav-with-dropdowns` instead of `nav`:
```handlebars
<body>
    {{> nav-with-dropdowns navigation}}
    {{{body}}}
    {{> footer footer}}
    <!-- scripts -->
</body>
```

**Step 5: Test navigation rendering**

```bash
npm run build
```

Expected: All pages rebuild with new dropdown navigation

**Step 6: Commit**

```bash
git add content/global/navigation.json templates/components/nav-with-dropdowns.hbs css/components.css templates/layouts/base.hbs
git commit -m "feat: add dropdown navigation with Solutions and Product menus"
```

---

## Task 2: Extract Homepage Content to JSON

**Goal:** Convert index.html from static HTML to JSON-based content

**Files:**
- Create: `content/pages/home.json`
- Create: `content/schemas/home.schema.json`
- Update: `templates/pages/landing-page.hbs` or create `templates/pages/home-page.hbs`

**Step 1: Create home page content schema**

Create `content/schemas/home.schema.json`:
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["meta", "hero", "overview", "specsPreview", "featuresPreview"],
  "properties": {
    "meta": {
      "type": "object",
      "required": ["title", "description"],
      "properties": {
        "title": { "type": "string" },
        "description": { "type": "string" }
      }
    },
    "hero": {
      "type": "object",
      "required": ["title", "tagline", "availability", "cta"],
      "properties": {
        "title": { "type": "string" },
        "tagline": { "type": "string" },
        "priceText": { "type": "string" },
        "availability": { "type": "string" },
        "cta": {
          "type": "object",
          "properties": {
            "primary": {
              "type": "object",
              "properties": {
                "text": { "type": "string" },
                "href": { "type": "string" }
              }
            },
            "secondary": {
              "type": "object",
              "properties": {
                "text": { "type": "string" },
                "href": { "type": "string" }
              }
            }
          }
        }
      }
    },
    "overview": {
      "type": "object",
      "required": ["title", "subtitle"],
      "properties": {
        "title": { "type": "string" },
        "subtitle": { "type": "string" }
      }
    },
    "specsPreview": {
      "type": "object",
      "required": ["title", "items"],
      "properties": {
        "title": { "type": "string" },
        "linkText": { "type": "string" },
        "linkHref": { "type": "string" },
        "items": {
          "type": "array",
          "maxItems": 4,
          "items": {
            "type": "object",
            "properties": {
              "icon": { "type": "string" },
              "title": { "type": "string" },
              "value": { "type": "string" },
              "unit": { "type": "string" },
              "description": { "type": "string" }
            }
          }
        }
      }
    },
    "featuresPreview": {
      "type": "object",
      "required": ["title", "items"],
      "properties": {
        "title": { "type": "string" },
        "linkText": { "type": "string" },
        "linkHref": { "type": "string" },
        "items": {
          "type": "array",
          "maxItems": 3,
          "items": {
            "type": "object",
            "properties": {
              "title": { "type": "string" },
              "description": { "type": "string" }
            }
          }
        }
      }
    },
    "solutionsPreview": {
      "type": "object",
      "required": ["title", "subtitle", "items"],
      "properties": {
        "title": { "type": "string" },
        "subtitle": { "type": "string" },
        "items": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "title": { "type": "string" },
              "description": { "type": "string" },
              "href": { "type": "string" }
            }
          }
        }
      }
    }
  }
}
```

**Step 2: Extract content from index.html to JSON**

Create `content/pages/home.json`:
```json
{
  "meta": {
    "title": "LAB SEVEN - Labrador Field Systems",
    "description": "No refueling. No noise. More power than a 7000 watt generator. Professional battery power for production."
  },
  "hero": {
    "title": "LAB SEVEN",
    "tagline": "No refueling. No noise. More power than a 7000 watt generator.",
    "priceText": "Available through Anytime Production Equipment Rentals",
    "availability": "ONE FREE RENTAL DAY WITH PROMO CODE \"241\"",
    "cta": {
      "primary": {
        "text": "Contact Anytime Rentals",
        "href": "mailto:rentals@anytimerentals.com"
      },
      "secondary": {
        "text": "View Specs",
        "href": "/specifications"
      }
    },
    "links": [
      {
        "text": "See what makes it different",
        "href": "/features"
      },
      {
        "text": "Rental options",
        "href": "/pricing"
      }
    ]
  },
  "overview": {
    "title": "Turn any outlet into 60A distro",
    "subtitle": "Quiet, house-power charging with battery buffering. Plug into a standard 15/20A receptacle, cap the draw, and let the pack cover peaks. Less friction with owners, fewer noise complaints, and a calmer set."
  },
  "specsPreview": {
    "title": "The battery built for production",
    "linkText": "Full Specifications",
    "linkHref": "/specifications",
    "items": [
      {
        "icon": "⚡",
        "title": "True 60A Power",
        "value": "60A",
        "unit": "OUT",
        "description": "Three 20A Edison on their own circuits, and 1 60A Bates. The only battery with 60A Bates out, no adapters needed."
      },
      {
        "icon": "🔋",
        "title": "Fastest Charging",
        "value": "1",
        "unit": "hour",
        "description": "Charge one battery in 1 hour using 60A Bates or 4-5 hours using standard 110v"
      },
      {
        "icon": "💪",
        "title": "7.5kWh Storage",
        "value": "7.5",
        "unit": "kWh",
        "description": "1 or 2 batteries solve any problem for HMU, crafty, production, and more"
      },
      {
        "icon": "🔌",
        "title": "Use Existing Distro",
        "value": "BATES",
        "unit": "",
        "description": "Nobody needs to change their workflows - use the same distro boxes you always have"
      }
    ]
  },
  "featuresPreview": {
    "title": "Why production teams choose LAB SEVEN",
    "linkText": "All Features",
    "linkHref": "/features",
    "items": [
      {
        "title": "Saves money over generators",
        "description": "When you add fuel runs, fire watch, noise complaints, and slow wrap, generators cost more than the day rate suggests."
      },
      {
        "title": "Works everywhere generators can't",
        "description": "Indoor venues, noise-restricted zones, residential areas, and historic locations that prohibit generators."
      },
      {
        "title": "Professional grade reliability",
        "description": "LFP chemistry, BMS protection, real-time monitoring. Built for the demands of professional production."
      }
    ]
  },
  "solutionsPreview": {
    "title": "Solutions for every production type",
    "subtitle": "See how LAB SEVEN solves specific challenges for your role",
    "items": [
      {
        "title": "Experience Agencies",
        "description": "Silent power for brand activations and experiential events",
        "href": "/experience-agencies"
      },
      {
        "title": "Production Managers",
        "description": "Efficient, reliable power for streamlined productions",
        "href": "/production-managers"
      },
      {
        "title": "Gaffers & Lighting",
        "description": "Power your lighting setups anywhere without generator noise",
        "href": "/gaffers"
      },
      {
        "title": "Location Managers",
        "description": "Get venue approval with silent, zero-emission power",
        "href": "/location-managers"
      }
    ]
  }
}
```

**Step 3: Create home page template**

Create `templates/pages/home-page.hbs`:
```handlebars
<!-- Hero Section -->
<section class="hero">
    <h1 class="animate-in">{{hero.title}}</h1>
    <p class="tagline animate-in">{{hero.tagline}}</p>
    <p class="price animate-in">{{hero.priceText}}</p>
    <p class="availability animate-in">{{hero.availability}}</p>
    <div class="cta-buttons animate-in">
        <a href="{{hero.cta.primary.href}}" class="btn btn-primary">{{hero.cta.primary.text}}</a>
        <a href="{{hero.cta.secondary.href}}" class="btn btn-secondary">{{hero.cta.secondary.text}}</a>
    </div>
    {{#if hero.links}}
    <div class="links animate-in">
        {{#each hero.links}}
        <a href="{{href}}">{{text}}</a>
        {{/each}}
    </div>
    {{/if}}
    <div class="hero-image animate-in">
        <div class="product-image">
            <div class="product-label">LAB SEVEN</div>
        </div>
    </div>
</section>

<!-- Overview Section -->
{{#if overview}}
<section class="typography-section">
    <h2>{{overview.title}}</h2>
    <p class="subtitle">{{overview.subtitle}}</p>
</section>
{{/if}}

<!-- Specs Preview -->
{{#if specsPreview}}
<section class="specs">
    <h2>{{specsPreview.title}}</h2>
    {{#if specsPreview.linkText}}
    <a href="{{specsPreview.linkHref}}" class="section-link">{{specsPreview.linkText}} →</a>
    {{/if}}
    <div class="specs-grid">
        {{#each specsPreview.items}}
        <div class="spec-card animate-in">
            <div class="spec-icon">{{icon}}</div>
            <h3>{{title}}</h3>
            <div class="spec-value">{{value}}{{#if unit}}<span class="spec-unit">{{unit}}</span>{{/if}}</div>
            <p>{{description}}</p>
        </div>
        {{/each}}
    </div>
</section>
{{/if}}

<!-- Features Preview -->
{{#if featuresPreview}}
<section class="features-preview">
    <h2>{{featuresPreview.title}}</h2>
    {{#if featuresPreview.linkText}}
    <a href="{{featuresPreview.linkHref}}" class="section-link">{{featuresPreview.linkText}} →</a>
    {{/if}}
    <div class="features-preview-grid">
        {{#each featuresPreview.items}}
        <div class="feature-preview-card">
            <h3>{{title}}</h3>
            <p>{{description}}</p>
        </div>
        {{/each}}
    </div>
</section>
{{/if}}

<!-- Solutions Preview -->
{{#if solutionsPreview}}
<section class="solutions-preview">
    <h2>{{solutionsPreview.title}}</h2>
    <p class="subtitle">{{solutionsPreview.subtitle}}</p>
    <div class="solutions-grid">
        {{#each solutionsPreview.items}}
        <a href="{{href}}" class="solution-card">
            <h3>{{title}}</h3>
            <p>{{description}}</p>
            <span class="card-arrow">→</span>
        </a>
        {{/each}}
    </div>
</section>
{{/if}}
```

**Step 4: Update build system to handle home page differently**

Modify `src/build.js` to detect `home.json` and use different template:
```javascript
pageFiles.forEach(file => {
  const pageName = file.replace('.json', '');
  const pagePath = path.join(pagesDir, file);
  const pageData = JSON.parse(fs.readFileSync(pagePath, 'utf8'));

  const templateData = {
    ...pageData,
    navigation,
    footer
  };

  // Use different template for home page
  const pageTemplate = (pageName === 'home') ? homePageTemplate : landingPageTemplate;
  const bodyHTML = pageTemplate(templateData);

  const finalHTML = baseLayout({
    ...templateData,
    body: bodyHTML
  });

  // Output home page as index.html
  const outputName = (pageName === 'home') ? 'index.html' : `${pageName}.html`;
  const outputPath = path.join(BUILD_DIR, outputName);
  fs.writeFileSync(outputPath, finalHTML, 'utf8');

  console.log(`✅ Built ${outputName}`);
});
```

**Step 5: Validate and build**

```bash
npm run validate
npm run build
```

Expected: `index.html` generates from `home.json`, all persona pages still work

**Step 6: Commit**

```bash
git add content/pages/home.json content/schemas/home.schema.json templates/pages/home-page.hbs src/build.js
git commit -m "feat: convert homepage to JSON-based content system"
```

---

## Task 3: Create Specifications Page

**Goal:** Extract specs section from index.html into dedicated full page

**Files:**
- Create: `content/pages/specifications.json`
- Create: `templates/pages/specs-page.hbs`

**Step 1: Create specifications content**

Create `content/pages/specifications.json`:
```json
{
  "meta": {
    "title": "LAB SEVEN Specifications | Labrador Field Systems",
    "description": "Complete technical specifications for LAB SEVEN battery system. 60A output, 7.5kWh capacity, 1-hour fast charging."
  },
  "hero": {
    "title": "Technical Specifications",
    "subtitle": "Professional-grade power in a portable package"
  },
  "powerOutput": {
    "title": "Power Output",
    "specs": [
      {
        "label": "60A Bates Connector",
        "value": "1x 60A output (Stage Pin)",
        "description": "True 60A output on professional Bates connector. No adapters, no workarounds."
      },
      {
        "label": "20A Edison Outlets",
        "value": "3x 20A outputs (NEMA 5-20R)",
        "description": "Each on its own circuit, no shared neutral. Run three 1800W devices simultaneously."
      },
      {
        "label": "Continuous Power",
        "value": "10kW continuous",
        "description": "Sustained 10kW output for hours. No derating, no thermal limits on set."
      },
      {
        "label": "Peak Power",
        "value": "12kW peak (30 seconds)",
        "description": "Handles startup surges from HMIs, motors, and compressors without tripping."
      }
    ]
  },
  "batterySystem": {
    "title": "Battery System",
    "specs": [
      {
        "label": "Capacity",
        "value": "7.5kWh",
        "description": "LiFePO4 (LFP) chemistry. Safer, longer-lasting, more stable than NMC."
      },
      {
        "label": "Cell Configuration",
        "value": "16S48P (51.2V nominal)",
        "description": "Professional battery architecture. 3000+ cycle lifespan at 80% DOD."
      },
      {
        "label": "Battery Management",
        "value": "JBD BMS with balancing",
        "description": "Real-time monitoring, cell balancing, over-current protection, thermal management."
      },
      {
        "label": "Runtime",
        "value": "45 minutes to 8+ hours",
        "description": "Depends on load. 8hrs at 1kW average, 45min at full 10kW continuous draw."
      }
    ]
  },
  "charging": {
    "title": "Charging",
    "specs": [
      {
        "label": "Fast Charging (60A Input)",
        "value": "1 hour (0-100%)",
        "description": "Use 60A Bates input to charge in 1 hour. Perfect for rotating batteries on multi-day shoots."
      },
      {
        "label": "Standard Charging (110V)",
        "value": "4-5 hours (0-100%)",
        "description": "Plug into any 15/20A outlet. Charge overnight between shoot days."
      },
      {
        "label": "Input Power",
        "value": "Up to 7.2kW max",
        "description": "Accepts 110V (15/20A) or 240V (30A) input. Automatically adjusts charging rate."
      }
    ]
  },
  "physical": {
    "title": "Physical Specifications",
    "specs": [
      {
        "label": "Dimensions",
        "value": "24\" W × 18\" D × 36\" H",
        "description": "Fits through standard doorways. Similar footprint to a road case."
      },
      {
        "label": "Weight",
        "value": "~180 lbs (82 kg)",
        "description": "Heavy but manageable. Roll it, don't lift it. Load levelers on all four corners."
      },
      {
        "label": "Construction",
        "value": "Welded steel frame, powder-coated",
        "description": "Built for the road. Impact-resistant corners, weather-sealed electronics bay."
      },
      {
        "label": "Wheels",
        "value": "4x industrial casters (2 locking)",
        "description": "8-inch pneumatic tires. Smooth rolling on concrete, asphalt, or uneven ground."
      }
    ]
  },
  "safety": {
    "title": "Safety & Certifications",
    "specs": [
      {
        "label": "Chemistry",
        "value": "LiFePO4 (LFP)",
        "description": "Most stable lithium chemistry. No thermal runaway risk. Safer than NMC/NCA batteries."
      },
      {
        "label": "Circuit Protection",
        "value": "Per-circuit breakers",
        "description": "Individual breakers on all outputs. BMS protects battery, breakers protect your gear."
      },
      {
        "label": "Certifications",
        "value": "UL testing in progress",
        "description": "Meeting UL 2743 (portable power stations) and UL 2271 (battery packs) requirements."
      },
      {
        "label": "Insurance",
        "value": "Production-friendly",
        "description": "LFP chemistry accepted by most production insurance. Check with your provider."
      }
    ]
  },
  "monitoring": {
    "title": "Monitoring & Controls",
    "specs": [
      {
        "label": "Display",
        "value": "4.3\" color touchscreen",
        "description": "Real-time voltage, current, power, SOC%, temperature, runtime estimate."
      },
      {
        "label": "Remote Monitoring",
        "value": "Bluetooth + WiFi",
        "description": "Monitor from your phone. Track multiple units. Get alerts for low battery or faults."
      },
      {
        "label": "Data Logging",
        "value": "30-day history",
        "description": "Review past usage. Export logs for reports. Prove runtime to clients."
      }
    ]
  },
  "environmental": {
    "title": "Environmental",
    "specs": [
      {
        "label": "Operating Temperature",
        "value": "-10°C to 50°C (14°F to 122°F)",
        "description": "Works in cold and heat. BMS adjusts charging rate based on temperature."
      },
      {
        "label": "Storage Temperature",
        "value": "-20°C to 60°C (-4°F to 140°F)",
        "description": "Leave it in the truck. Store it in the warehouse. It's fine."
      },
      {
        "label": "Humidity",
        "value": "5-95% RH (non-condensing)",
        "description": "Electronics bay is weather-sealed. Can handle rain and humidity."
      },
      {
        "label": "Altitude",
        "value": "Up to 10,000 ft",
        "description": "No derating at altitude. Works the same in Denver as in Los Angeles."
      }
    ]
  }
}
```

**Step 2: Build and validate**

```bash
npm run validate
npm run build
```

Expected: `/specifications.html` generates successfully

**Step 3: Commit**

```bash
git add content/pages/specifications.json
git commit -m "feat: create dedicated specifications page"
```

---

## Task 4: Create Features Page

**Goal:** Create comprehensive features page with detailed explanations

**Files:**
- Create: `content/pages/features.json`

(Similar structure to specifications but focused on benefits and use cases)

---

## Task 5: Create Gallery, Pricing, Roadmap, Contact Pages

**Goal:** Create remaining top-level pages

**Files:**
- Create: `content/pages/gallery.json`
- Create: `content/pages/pricing.json`
- Create: `content/pages/roadmap.json`
- Create: `content/pages/contact.json`

(Follow same pattern as previous pages)

---

## Task 6: Update .gitignore and Clean Script

**Goal:** Don't track generated HTML files in git

**Files:**
- Modify: `.gitignore`
- Modify: `package.json` clean script

**Step 1: Update .gitignore to exclude generated HTML**

Add to `.gitignore`:
```
# Generated HTML files (built from content/)
index.html
experience-agencies.html
city-services.html
gaffers.html
production-managers.html
location-managers.html
public-venues.html
street-festivals.html
specifications.html
features.html
gallery.html
pricing.html
roadmap.html
contact.html

# Keep legacy files for reference
!legacy/*.html
```

**Step 2: Update clean script**

Modify `package.json`:
```json
{
  "scripts": {
    "clean": "rm -f index.html *-agencies.html *-services.html *-managers.html gaffers.html public-venues.html street-festivals.html specifications.html features.html gallery.html pricing.html roadmap.html contact.html"
  }
}
```

**Step 3: Test clean and rebuild**

```bash
npm run clean
npm run build
```

Expected: All generated HTML deleted, then rebuilt from JSON

**Step 4: Commit**

```bash
git add .gitignore package.json
git commit -m "chore: exclude generated HTML from git tracking"
```

---

## Task 7: Update Netlify Configuration

**Goal:** Ensure Netlify builds site correctly with new structure

**Files:**
- Modify: `netlify.toml`

**Step 1: Update Netlify publish directory**

Netlify should build the site, so generated HTML files should be in the publish directory.

Actually, we changed the build to output to the root directory (`lab/`), so Netlify config is already correct. Just verify:

```toml
[build]
  base = "lab"
  publish = "."  # Site root, where HTML files are generated
  command = "npm ci && npm run build"
```

**Step 2: Add new redirect rules for clean URLs**

Add to `netlify.toml`:
```toml
# New page redirects (extensionless URLs)
[[redirects]]
  from = "/specifications"
  to = "/specifications.html"
  status = 200

[[redirects]]
  from = "/features"
  to = "/features.html"
  status = 200

[[redirects]]
  from = "/gallery"
  to = "/gallery.html"
  status = 200

[[redirects]]
  from = "/pricing"
  to = "/pricing.html"
  status = 200

[[redirects]]
  from = "/roadmap"
  to = "/roadmap.html"
  status = 200

[[redirects]]
  from = "/contact"
  to = "/contact.html"
  status = 200
```

**Step 3: Commit**

```bash
git add netlify.toml
git commit -m "chore: add Netlify redirects for new pages"
```

---

## Task 8: Update Documentation

**Goal:** Document the new site structure and navigation

**Files:**
- Update: `README.md`
- Update: `docs/CONTENT_EDITING.md`

**Step 1: Update README with new site map**

Add site structure section to README showing all pages and navigation hierarchy.

**Step 2: Update CONTENT_EDITING guide**

Update the guide to explain:
- Home page special handling
- Navigation dropdown structure
- How to add new pages
- How to add new menu items

**Step 3: Commit**

```bash
git add README.md docs/CONTENT_EDITING.md
git commit -m "docs: update documentation for new site structure"
```

---

## Testing Checklist

**Navigation:**
- [ ] All dropdown menus work correctly
- [ ] Hover states show/hide menus smoothly
- [ ] Mobile menu collapses properly (if implemented)
- [ ] All links go to correct pages

**Pages:**
- [ ] Home page renders with correct content
- [ ] All 7 persona pages render correctly
- [ ] Specifications page shows all specs
- [ ] Features page shows all features
- [ ] Gallery, Pricing, Roadmap, Contact pages render

**Build System:**
- [ ] `npm run validate` passes for all pages
- [ ] `npm run build` generates all HTML files
- [ ] `npm run dev` serves all pages with live reload
- [ ] `npm run clean` removes all generated files

**Deployment:**
- [ ] Netlify build succeeds
- [ ] All pages accessible on deployed site
- [ ] Redirects work for extensionless URLs
- [ ] No 404 errors

---

## Success Criteria

✅ Site has clear information architecture with logical navigation
✅ 7 persona landing pages are accessible from Solutions dropdown
✅ Dedicated pages exist for Specs, Features, Gallery, Pricing, Roadmap
✅ Home page acts as hub with previews and links to deeper pages
✅ All pages use consistent navigation and design system
✅ Build system generates all pages from JSON content
✅ Documentation updated to reflect new structure
✅ Site deploys successfully to Netlify

---

## Future Enhancements

**Phase 2:**
- Mobile navigation menu (hamburger)
- Search functionality
- Breadcrumb navigation
- Related pages/cross-linking
- Analytics tracking
- SEO optimization (structured data, sitemaps)

**Phase 3:**
- Blog/news section
- Case studies library
- Video gallery
- Downloadable resources (spec sheets, CAD files)
- Customer testimonials
- Dealer/rental location finder
