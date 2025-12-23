# Implementation Plan: Rebrand Citypack/Citypack to Citypack

**Date:** November 27, 2025
**Author:** Claude Code
**Status:** Ready for Implementation

## Executive Summary

This plan outlines the complete rebranding of the website from Citypack/Citypack to Citypack. The rebrand includes:

1. Removing all references to Citypack, PACK SEVEN, SEVEN PACK, and customizable battery concepts
2. Updating Citypack to Citypack throughout
3. Repositioning from a specific product (Citypack battery) to a company that delivers any and all types of batteries depending on customer needs

## Scope Analysis

### Files Requiring Updates

Based on codebase analysis, the following categories of files need updates:

**Documentation Files (7 files)**
- `CLAUDE.md` - Technical documentation
- `README.md` - Project overview
- `DESIGN_SYSTEM.md` - Design system documentation
- `TODO.md` - Task tracking
- `history.md` - Session history
- `content-editor-guide.md` - Content editing guide
- `docs/CONTENT_EDITING.md` - Content editing documentation

**Content JSON Files (20+ files)**
- `content/global/navigation.json` - Site navigation
- `content/global/footer.json` - Footer content
- `content/pages/*.json` - All page content files including:
  - experience-agencies.json
  - production-managers.json
  - gaffers.json
  - location-managers.json
  - city-services.json
  - public-venues.json
  - street-festivals.json
  - specifications.json
  - features.json
  - gallery.json
  - pricing.json
  - how-it-works.json
  - roadmap.json
  - contact.json
  - solutions.json
  - customers.json
  - impact.json
  - cities.json
  - company.json

**HTML Template Files (4+ files)**
- `templates/pages/home-page.hbs`
- `templates/pages/landing-page.hbs`
- Other template files in `templates/` directory

**CSS Files (3 files)**
- `css/design-system.css` - Design tokens and base styles
- `css/components.css` - Component styles
- `css/layouts.css` - Layout patterns

**Legacy HTML Files (5 files)**
- `lab-seven-battery.html` - Should be renamed/archived
- `lab-seven-battery-editable.html` - Should be renamed/archived
- `lab-seven-premium.html` - Should be renamed/archived
- `lab-seven-stripe-style.html` - Should be renamed/archived
- Other HTML files with Citypack references

**Configuration Files**
- `package.json` - Project metadata
- `netlify.toml` - Deployment configuration
- `_redirects` - URL redirects

**Plan Documents**
- `docs/plans/*.md` - Various planning documents

### Key Rebranding Changes

#### Brand Names
- "Citypack" → Remove entirely (product-specific name)
- "PACK SEVEN" → Remove entirely (product-specific name)
- "SEVEN PACK" → Remove entirely (product-specific name)
- "Citypack" → "Citypack"
- "Citypack" → "Citypack"

#### Business Positioning
**FROM:** Specific product focus (Citypack customizable battery system)
**TO:** Battery solutions provider (delivering any and all types of batteries depending on need)

#### Messaging Changes
- Remove all references to "customizable battery"
- Remove all references to "modular" battery system
- Update messaging to emphasize diverse battery solutions
- Change from product-centric to service-centric language

## Implementation Tasks

### Phase 1: Documentation & Configuration (30 minutes)

#### Task 1.1: Update CLAUDE.md
**File:** `/Users/amitrunchal/apps/fieldpack_apps/_citypack/citypack-website/CLAUDE.md`

**Changes:**
```markdown
# Before
This repository contains premium marketing website prototypes, specifically focused on creating Apple-style product showcase websites. The primary project is the Citypack battery system website for Citypack, built as a sophisticated single-page application with integrated content management system.

# After
This repository contains premium marketing website prototypes, specifically focused on creating Apple-style product showcase websites. The primary project is the Citypack battery solutions website, built as a sophisticated multi-page application with integrated content management system.
```

**Additional changes:**
- Update all references from "Citypack" to "Citypack battery solutions"
- Update "Citypack" to "Citypack"
- Remove references to specific Citypack file names
- Update development workflow sections to reference new file naming

**Verification:**
```bash
grep -i "lab.seven\|labrador\|pack.seven\|seven.pack" CLAUDE.md
# Should return no matches
```

---

#### Task 1.2: Update README.md
**File:** `/Users/amitrunchal/apps/fieldpack_apps/_citypack/citypack-website/README.md`

**Changes:**
```markdown
# Before
# Citypack Website

> Professional marketing website for Citypack battery systems by Citypack

## 🏢 About Citypack

> **"Batteries that are your crews' best friend."**

Citypack creates professional-grade portable power solutions for film and video production. The Citypack system delivers 10kW continuous output with rapid charging capabilities, designed specifically for the demanding requirements of production crews.

# After
# Citypack Website

> Professional marketing website for Citypack - delivering battery solutions tailored to your needs

## 🏢 About Citypack

> **"Power solutions for every application."**

Citypack delivers professional-grade portable power solutions across industries. From film production to events to emergency services, we provide the right battery system for your specific requirements.
```

**Additional changes:**
- Update title badges and links
- Update all section headers from "Citypack" to "Citypack"
- Update product positioning from specific battery to solutions provider
- Update feature descriptions to be solution-focused
- Update file structure references
- Update development workflow examples

**Verification:**
```bash
grep -i "lab.seven\|labrador\|pack.seven\|seven.pack" README.md
# Should return no matches
```

---

#### Task 1.3: Update DESIGN_SYSTEM.md
**File:** `/Users/amitrunchal/apps/fieldpack_apps/_citypack/citypack-website/DESIGN_SYSTEM.md`

**Changes:**
```markdown
# Before
# Citypack Design System

A scalable, modular CSS architecture for the Citypack website

# After
# Citypack Design System

A scalable, modular CSS architecture for the Citypack website
```

**Additional changes:**
- Update basic template example to use Citypack branding
- Update navigation logo from "LABRADOR" to "CITYPACK"
- Update title tag pattern: "Page Title | Citypack"
- Update footer copyright: "© 2025 Citypack. All rights reserved."
- Update all example content references

**Verification:**
```bash
grep -i "lab.seven\|labrador\|pack.seven\|seven.pack" DESIGN_SYSTEM.md
# Should return no matches
```

---

#### Task 1.4: Update TODO.md
**File:** `/Users/amitrunchal/apps/fieldpack_apps/_citypack/citypack-website/TODO.md`

**Changes:**
- Update title: "TODO List - Citypack Project"
- Update task descriptions to reference Citypack instead of Citypack
- Update file name references (lab-seven-*.html)
- Add new completed task: "✅ Complete rebrand from Citypack/Citypack to Citypack"

**Verification:**
```bash
grep -i "lab.seven\|labrador\|pack.seven\|seven.pack" TODO.md
# Should return no matches (except in completed rebranding task)
```

---

#### Task 1.5: Update package.json
**File:** `/Users/amitrunchal/apps/fieldpack_apps/_citypack/citypack-website/package.json`

**Changes:**
```json
{
  "name": "citypack-website",
  "version": "2.0.0",
  "description": "Professional marketing website for Citypack battery solutions",
  "repository": {
    "type": "git",
    "url": "https://github.com/runchal/citypack.git"
  },
  "keywords": [
    "citypack",
    "batteries",
    "power-solutions",
    "marketing-site"
  ]
}
```

**Verification:**
```bash
grep -i "lab.seven\|labrador\|pack.seven\|seven.pack" package.json
# Should return no matches
```

---

### Phase 2: Content Files - Global (15 minutes)

#### Task 2.1: Update navigation.json
**File:** `/Users/amitrunchal/apps/fieldpack_apps/_citypack/citypack-website/content/global/navigation.json`

**Changes:**
```json
{
  "logo": "CITYPACK",
  "menuItems": [
    // Keep existing menu structure, just update logo
  ]
}
```

**Verification:**
```bash
grep -i "labrador" content/global/navigation.json
# Should return no matches
```

---

#### Task 2.2: Update footer.json
**File:** `/Users/amitrunchal/apps/fieldpack_apps/_citypack/citypack-website/content/global/footer.json`

**Changes:**
```json
{
  "copyright": "© 2025 Citypack. All rights reserved.",
  "homeLink": {
    "text": "Return to main site",
    "href": "index.html"
  }
}
```

**Verification:**
```bash
grep -i "labrador" content/global/footer.json
# Should return no matches
```

---

### Phase 3: Content Files - Pages (60 minutes)

Each page content file needs to be updated to:
1. Remove all "Citypack" product references
2. Update "Citypack" to "Citypack"
3. Remove references to customizable/modular battery concepts
4. Update messaging to focus on diverse battery solutions

#### Task 3.1: Update experience-agencies.json
**File:** `/Users/amitrunchal/apps/fieldpack_apps/_citypack/citypack-website/content/pages/experience-agencies.json`

**Changes:**
```json
{
  "meta": {
    "title": "Battery Solutions for Experience Agencies | Citypack",
    "description": "Silent battery power for brand activations and experiential events. Professional power solutions tailored to your activation needs."
  },
  "hero": {
    "category": "EXPERIENCE AGENCIES",
    "title": "Power Immersive Experiences Anywhere",
    "description": "No refueling. No noise. Professional battery systems sized for your activation. Silent power for brand activations, pop-ups, and installations. No permits, no noise complaints, no limits.",
    "cta": {
      "primary": {
        "text": "Contact Citypack",
        "href": "/contact"
      }
    }
  },
  "benefits": {
    "title": "Built for Experiential Marketing",
    "items": [
      // Update items to remove specific Citypack references
    ]
  },
  "features": {
    "title": "Why Experience Agencies Choose Citypack",
    "items": [
      {
        "title": "Silent Approval",
        "description": "Zero emissions, zero noise. Indoor-approved power opens previously impossible venues. Say yes to rooftop activations, hotel ballrooms, historic buildings, and retail spaces that prohibit generators."
      },
      {
        "title": "True Cost Savings",
        "description": "Cost-competitive with generators once you factor in permits, fuel, fire watch, and crew time. Transparent rental pricing includes delivery, pickup, and backup generator."
      },
      {
        "title": "White-Glove Service",
        "description": "Citypack handles delivery, placement, and pickup. You don't touch it. Your crew focuses on creating experiences, not managing power logistics."
      },
      {
        "title": "Right-Sized Power",
        "description": "We provide the battery system that matches your activation needs. From small pop-ups to major installations, we deliver the right solution."
      }
    ]
  }
}
```

**Verification:**
```bash
grep -i "lab.seven\|labrador" content/pages/experience-agencies.json
# Should return no matches
```

---

#### Task 3.2: Update production-managers.json
**File:** `/Users/amitrunchal/apps/fieldpack_apps/_citypack/citypack-website/content/pages/production-managers.json`

**Similar changes to experience-agencies.json:**
- Update meta title to "Battery Solutions for Production Managers | Citypack"
- Update CTA text to "Contact Citypack"
- Update "Citypack" references to "Citypack"
- Remove Citypack product-specific references
- Update messaging to emphasize tailored solutions

**Verification:**
```bash
grep -i "lab.seven\|labrador" content/pages/production-managers.json
# Should return no matches
```

---

#### Task 3.3: Update gaffers.json
**File:** `/Users/amitrunchal/apps/fieldpack_apps/_citypack/citypack-website/content/pages/gaffers.json`

**Similar changes:**
- Update meta title to "Battery Solutions for Gaffers & Lighting | Citypack"
- Update company references
- Remove product-specific references
- Focus on solutions approach

**Verification:**
```bash
grep -i "lab.seven\|labrador" content/pages/gaffers.json
# Should return no matches
```

---

#### Task 3.4: Update location-managers.json
**File:** `/Users/amitrunchal/apps/fieldpack_apps/_citypack/citypack-website/content/pages/location-managers.json`

**Similar changes as above**

**Verification:**
```bash
grep -i "lab.seven\|labrador" content/pages/location-managers.json
# Should return no matches
```

---

#### Task 3.5: Update city-services.json
**File:** `/Users/amitrunchal/apps/fieldpack_apps/_citypack/citypack-website/content/pages/city-services.json`

**Similar changes as above**

**Verification:**
```bash
grep -i "lab.seven\|labrador" content/pages/city-services.json
# Should return no matches
```

---

#### Task 3.6: Update public-venues.json
**File:** `/Users/amitrunchal/apps/fieldpack_apps/_citypack/citypack-website/content/pages/public-venues.json`

**Similar changes as above**

**Verification:**
```bash
grep -i "lab.seven\|labrador" content/pages/public-venues.json
# Should return no matches
```

---

#### Task 3.7: Update street-festivals.json
**File:** `/Users/amitrunchal/apps/fieldpack_apps/_citypack/citypack-website/content/pages/street-festivals.json`

**Similar changes as above**

**Verification:**
```bash
grep -i "lab.seven\|labrador" content/pages/street-festivals.json
# Should return no matches
```

---

#### Task 3.8: Update specifications.json
**File:** `/Users/amitrunchal/apps/fieldpack_apps/_citypack/citypack-website/content/pages/specifications.json`

**Critical changes:**
- Remove all Citypack product specifications
- Update to showcase range of battery solutions available
- Remove modular/customizable language
- Focus on "we deliver the right specs for your needs"

**Example approach:**
```json
{
  "meta": {
    "title": "Battery Specifications | Citypack",
    "description": "Professional battery systems sized for your application. View our range of power solutions."
  },
  "hero": {
    "title": "Power Solutions Tailored to Your Needs",
    "description": "Citypack delivers battery systems across a range of capacities and configurations. Tell us your requirements, and we'll provide the right solution."
  },
  "categories": [
    {
      "name": "Small Events & Activations",
      "description": "Compact battery systems for pop-ups, small installations, and mobile applications",
      "powerRange": "2-5kW continuous"
    },
    {
      "name": "Mid-Size Productions",
      "description": "Versatile battery systems for film shoots, medium events, and temporary installations",
      "powerRange": "5-10kW continuous"
    },
    {
      "name": "Large-Scale Applications",
      "description": "High-capacity battery systems for major events, large productions, and demanding installations",
      "powerRange": "10kW+ continuous"
    }
  ]
}
```

**Verification:**
```bash
grep -i "lab.seven\|pack.seven\|seven.pack\|customizable\|modular" content/pages/specifications.json
# Should return no matches
```

---

#### Task 3.9: Update features.json
**File:** `/Users/amitrunchal/apps/fieldpack_apps/_citypack/citypack-website/content/pages/features.json`

**Changes:**
- Remove Citypack-specific features
- Update to describe general capabilities across battery range
- Remove modular/customizable messaging
- Focus on service capabilities (delivery, sizing, support)

**Verification:**
```bash
grep -i "lab.seven\|pack.seven\|seven.pack\|customizable\|modular" content/pages/features.json
# Should return no matches
```

---

#### Task 3.10: Update gallery.json
**File:** `/Users/amitrunchal/apps/fieldpack_apps/_citypack/citypack-website/content/pages/gallery.json`

**Changes:**
- Update title to "Citypack Solutions Gallery"
- Update descriptions to focus on applications not specific product
- Remove Citypack branding from image captions

**Verification:**
```bash
grep -i "lab.seven\|labrador" content/pages/gallery.json
# Should return no matches
```

---

#### Task 3.11: Update pricing.json
**File:** `/Users/amitrunchal/apps/fieldpack_apps/_citypack/citypack-website/content/pages/pricing.json`

**Changes:**
- Remove Citypack specific pricing
- Update to tiered pricing based on power requirements
- Update company name references
- Focus on "get a quote for your specific needs"

**Verification:**
```bash
grep -i "lab.seven\|labrador" content/pages/pricing.json
# Should return no matches
```

---

#### Task 3.12: Update how-it-works.json
**File:** `/Users/amitrunchal/apps/fieldpack_apps/_citypack/citypack-website/content/pages/how-it-works.json`

**Changes:**
- Update workflow descriptions
- Change "rent Citypack" to "rent battery solution"
- Update company references

**Verification:**
```bash
grep -i "lab.seven\|labrador" content/pages/how-it-works.json
# Should return no matches
```

---

#### Task 3.13: Update roadmap.json
**File:** `/Users/amitrunchal/apps/fieldpack_apps/_citypack/citypack-website/content/pages/roadmap.json`

**Critical changes:**
- Remove all references to future Citypack variants
- Remove PACK SEVEN, SEVEN PACK concepts
- Update to focus on expanding battery solutions portfolio
- Remove modular/customizable future product references

**Verification:**
```bash
grep -i "lab.seven\|pack.seven\|seven.pack\|labrador\|customizable\|modular" content/pages/roadmap.json
# Should return no matches
```

---

#### Task 3.14: Update contact.json
**File:** `/Users/amitrunchal/apps/fieldpack_apps/_citypack/citypack-website/content/pages/contact.json`

**Changes:**
- Update company name from "Citypack" to "Citypack"
- Update all contact form messaging
- Update email addresses (if they reference labrador)

**Verification:**
```bash
grep -i "labrador" content/pages/contact.json
# Should return no matches
```

---

#### Task 3.15: Update additional page files
**Files:**
- `content/pages/solutions.json`
- `content/pages/customers.json`
- `content/pages/impact.json`
- `content/pages/cities.json`
- `content/pages/company.json`

**Apply similar changes to all files:**
1. Update company references
2. Remove product-specific naming
3. Remove customizable/modular concepts
4. Update to solutions-focused messaging

**Verification:**
```bash
for file in content/pages/*.json; do
  echo "Checking $file"
  grep -i "lab.seven\|pack.seven\|seven.pack\|labrador" "$file"
done
# Should return no matches for any file
```

---

### Phase 4: Templates (45 minutes)

#### Task 4.1: Identify all template files
**Command:**
```bash
find templates -name "*.hbs" -type f
```

#### Task 4.2: Update home-page.hbs
**File:** `/Users/amitrunchal/apps/fieldpack_apps/_citypack/citypack-website/templates/pages/home-page.hbs`

**Changes:**
- Remove Citypack references in template text
- Update default placeholders
- Update meta tag defaults
- Update any hardcoded company references

**Verification:**
```bash
grep -i "lab.seven\|labrador\|pack.seven\|seven.pack" templates/pages/home-page.hbs
# Should return no matches
```

---

#### Task 4.3: Update landing-page.hbs
**File:** `/Users/amitrunchal/apps/fieldpack_apps/_citypack/citypack-website/templates/pages/landing-page.hbs`

**Similar changes as home-page.hbs**

**Verification:**
```bash
grep -i "lab.seven\|labrador\|pack.seven\|seven.pack" templates/pages/landing-page.hbs
# Should return no matches
```

---

#### Task 4.4: Update all component templates
**Files:** All .hbs files in `templates/components/`

**Changes:**
- Review each component template
- Remove any hardcoded Citypack/Citypack references
- Update default values and placeholders

**Verification:**
```bash
find templates/components -name "*.hbs" -exec grep -Hi "lab.seven\|labrador\|pack.seven\|seven.pack" {} \;
# Should return no matches
```

---

### Phase 5: CSS Files (30 minutes)

#### Task 5.1: Update design-system.css
**File:** `/Users/amitrunchal/apps/fieldpack_apps/_citypack/citypack-website/css/design-system.css`

**Changes:**
- Review CSS comments for Citypack references
- Update any example content in comments
- Update color variable naming if it references Citypack

**Verification:**
```bash
grep -i "lab.seven\|labrador" css/design-system.css
# Should return no matches
```

---

#### Task 5.2: Update components.css
**File:** `/Users/amitrunchal/apps/fieldpack_apps/_citypack/citypack-website/css/components.css`

**Changes:**
- Review component comments
- Update example usage in comments

**Verification:**
```bash
grep -i "lab.seven\|labrador" css/components.css
# Should return no matches
```

---

#### Task 5.3: Update layouts.css
**File:** `/Users/amitrunchal/apps/fieldpack_apps/_citypack/citypack-website/css/layouts.css`

**Changes:**
- Review layout comments
- Update example usage in comments

**Verification:**
```bash
grep -i "lab.seven\|labrador" css/layouts.css
# Should return no matches
```

---

### Phase 6: Legacy HTML Files (30 minutes)

#### Task 6.1: Archive legacy Citypack HTML files
**Files to archive:**
- `lab-seven-battery.html`
- `lab-seven-battery-editable.html`
- `lab-seven-premium.html`
- `lab-seven-stripe-style.html`

**Actions:**
1. Create `legacy/lab-seven/` directory
2. Move these files to legacy directory
3. Add README.md in legacy/lab-seven/ explaining these are archived Citypack files

**Commands:**
```bash
mkdir -p legacy/lab-seven
mv lab-seven-*.html legacy/lab-seven/
```

**Create legacy README:**
```bash
cat > legacy/lab-seven/README.md << 'EOF'
# Legacy Citypack Files

These files contain the original Citypack product-specific website designs.

**ARCHIVED:** November 27, 2025
**REASON:** Rebranding from Citypack product to Citypack solutions company

These files are kept for reference but should not be used in production.

## Files
- lab-seven-battery.html - Original static marketing website
- lab-seven-battery-editable.html - Version with content management
- lab-seven-premium.html - Premium design variant
- lab-seven-stripe-style.html - Stripe-inspired design variant
EOF
```

---

#### Task 6.2: Update active HTML files
**Files:** All remaining .html files in root directory

**For each HTML file:**
1. Read the file
2. Search for Citypack, Citypack, PACK SEVEN, SEVEN PACK references
3. Update to Citypack
4. Remove customizable/modular concepts

**Files to check:**
- index.html
- experience-agencies.html
- production-managers.html
- gaffers.html
- location-managers.html
- city-services.html
- public-venues.html
- street-festivals.html
- specifications.html
- features.html
- gallery.html
- pricing.html
- how-it-works.html
- roadmap.html
- contact.html
- customers.html
- solutions.html
- impact.html
- cities.html
- company.html

**Verification:**
```bash
for file in *.html; do
  echo "Checking $file"
  grep -i "lab.seven\|labrador\|pack.seven\|seven.pack" "$file" && echo "FOUND IN $file"
done
# Should show no matches after updates
```

---

### Phase 7: Documentation & Plans (45 minutes)

#### Task 7.1: Update docs/CONTENT_EDITING.md
**File:** `/Users/amitrunchal/apps/fieldpack_apps/_citypack/citypack-website/docs/CONTENT_EDITING.md`

**Changes:**
- Update all Citypack references to Citypack
- Update company name references
- Update example content

**Verification:**
```bash
grep -i "lab.seven\|labrador" docs/CONTENT_EDITING.md
# Should return no matches
```

---

#### Task 7.2: Update docs/MIGRATION.md (if exists)
**Changes:**
- Update historical references (keep as historical context)
- Add note about rebrand
- Update current state references

---

#### Task 7.3: Update all plan documents
**Files:** All .md files in `docs/plans/`

**Approach:**
For historical plan documents, add a header note:
```markdown
> **Historical Note:** This plan was created before the November 2025 rebrand from Citypack/Citypack to Citypack. References to Citypack and Citypack are preserved for historical context.
```

For current/active plans:
- Update all references to Citypack
- Remove product-specific naming

**Files to review:**
```bash
ls -1 docs/plans/*.md
```

**Verification:**
```bash
# Check which plan files have Citypack references
for file in docs/plans/*.md; do
  grep -l -i "lab.seven\|labrador" "$file"
done
```

---

#### Task 7.4: Update history.md
**File:** `/Users/amitrunchal/apps/fieldpack_apps/_citypack/citypack-website/history.md`

**Changes:**
- Add new entry documenting the rebrand
- Update most recent references to use Citypack
- Preserve historical entries as context

**Add to history.md:**
```markdown
## Session: November 27, 2025 - Complete Rebrand to Citypack

### Major Changes
- **Rebranded from Citypack/Citypack to Citypack**
  - Removed all references to Citypack, PACK SEVEN, SEVEN PACK products
  - Updated Citypack to Citypack throughout
  - Removed customizable/modular battery concepts
  - Repositioned from product company to solutions provider

### Files Updated
- All documentation files (CLAUDE.md, README.md, DESIGN_SYSTEM.md, etc.)
- All content JSON files (20+ files)
- All template files (.hbs)
- All CSS files
- All active HTML files
- Configuration files (package.json, netlify.toml)

### Files Archived
- Moved lab-seven-*.html files to legacy/lab-seven/
```

---

#### Task 7.5: Update content-editor-guide.md
**File:** `/Users/amitrunchal/apps/fieldpack_apps/_citypack/citypack-website/content-editor-guide.md`

**Changes:**
- Update company references
- Update example content
- Update file references

**Verification:**
```bash
grep -i "lab.seven\|labrador" content-editor-guide.md
# Should return no matches
```

---

### Phase 8: Configuration & Build Files (20 minutes)

#### Task 8.1: Update netlify.toml
**File:** `/Users/amitrunchal/apps/fieldpack_apps/_citypack/citypack-website/netlify.toml`

**Changes:**
- Review redirect rules
- Update any comments or descriptions
- Ensure no Citypack references

**Verification:**
```bash
grep -i "lab.seven\|labrador" netlify.toml
# Should return no matches
```

---

#### Task 8.2: Update _redirects (if exists)
**File:** `/Users/amitrunchal/apps/fieldpack_apps/_citypack/citypack-website/_redirects`

**Changes:**
- Review redirect rules
- Update comments

**Verification:**
```bash
grep -i "lab.seven\|labrador" _redirects
# Should return no matches
```

---

#### Task 8.3: Update build scripts
**Files:** All .js files in `src/`

**Changes:**
- Update comments and console messages
- Update any hardcoded references

**Verification:**
```bash
find src -name "*.js" -exec grep -Hi "lab.seven\|labrador" {} \;
# Should return no matches
```

---

### Phase 9: Rebuild & Verification (30 minutes)

#### Task 9.1: Validate all content files
**Command:**
```bash
npm run validate
```

**Expected:** All content files pass JSON schema validation

---

#### Task 9.2: Rebuild entire site
**Command:**
```bash
npm run clean
npm run build
```

**Expected:** Clean build with no errors

---

#### Task 9.3: Comprehensive grep verification
**Run comprehensive search across entire codebase:**

```bash
# Search all files (excluding node_modules and .git)
grep -r -i "lab.seven\|labrador\|pack.seven\|seven.pack" \
  --exclude-dir=node_modules \
  --exclude-dir=.git \
  --exclude-dir=legacy \
  --exclude="*.md" \
  .

# Search specifically for customizable/modular in content
grep -r -i "customizable\|modular" \
  content/ \
  --include="*.json"
```

**Expected:** No matches except in:
- `legacy/` directory (archived files)
- Plan documents with historical notes
- This implementation plan itself

---

#### Task 9.4: Visual verification
**Commands:**
```bash
npm run dev
# Visit http://localhost:3000
```

**Verify:**
1. Navigation shows "CITYPACK" logo
2. No Citypack references visible on any page
3. Footer shows "© 2025 Citypack. All rights reserved."
4. All links work correctly
5. Content reads naturally with new branding
6. No references to "customizable battery"
7. Messaging focuses on solutions approach

**Pages to check:**
- Home page (index.html)
- All 7 customer landing pages
- All product pages (specifications, features, gallery)
- All rental pages (pricing, how-it-works)
- Contact page
- Roadmap page

---

#### Task 9.5: Test build output
**Review generated HTML files in dist/ (if using build system):**

```bash
# Search built files for any missed references
grep -r -i "lab.seven\|labrador\|pack.seven\|seven.pack" dist/

# Search for customizable/modular
grep -r -i "customizable\|modular" dist/
```

**Expected:** No matches

---

### Phase 10: Git Operations (15 minutes)

#### Task 10.1: Stage all changes
```bash
git add .
git status
# Review changes carefully
```

---

#### Task 10.2: Commit rebrand
```bash
git commit -m "$(cat <<'EOF'
rebrand: Complete rebrand from Citypack/Citypack to Citypack

Major changes:
- Removed all references to Citypack, PACK SEVEN, SEVEN PACK
- Updated Citypack to Citypack throughout
- Removed customizable/modular battery concepts
- Repositioned from product company to solutions provider

Files updated:
- All documentation files (CLAUDE.md, README.md, DESIGN_SYSTEM.md)
- All content JSON files (20+ files in content/)
- All template files (templates/**/*.hbs)
- All CSS files (css/*.css)
- All active HTML files
- Configuration files (package.json, netlify.toml)

Files archived:
- Moved lab-seven-*.html to legacy/lab-seven/

Verification:
- All content validates against schemas
- Clean build with no errors
- No Citypack/Citypack references in active codebase
- Site displays Citypack branding throughout

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"
```

---

#### Task 10.3: Push to repository
```bash
git push origin main
```

---

## Risk Mitigation

### Backups
**Before starting:**
```bash
# Create backup branch
git checkout -b backup-before-citypack-rebrand
git push origin backup-before-citypack-rebrand
git checkout main
```

### Testing Checklist
- [ ] All content files validate
- [ ] Build completes without errors
- [ ] All pages load correctly
- [ ] Navigation works properly
- [ ] No broken links
- [ ] Forms work (if applicable)
- [ ] Mobile responsive
- [ ] No console errors

### Rollback Plan
If issues arise:
```bash
git checkout backup-before-citypack-rebrand
git checkout -b main-recovery
# Fix issues
git checkout main
git merge main-recovery
```

## Success Criteria

✅ **Complete when:**
1. Zero references to "Citypack", "PACK SEVEN", "SEVEN PACK" in active codebase
2. All "Citypack" references updated to "Citypack"
3. All references to customizable/modular battery concepts removed
4. All content validates successfully
5. Build completes without errors
6. Visual verification shows Citypack branding throughout
7. Messaging focuses on solutions provider approach
8. Legacy files properly archived
9. All changes committed and pushed
10. Site deploys successfully with new branding

## Estimated Time

**Total:** 4-5 hours

- Phase 1 (Documentation): 30 min
- Phase 2 (Global Content): 15 min
- Phase 3 (Page Content): 60 min
- Phase 4 (Templates): 45 min
- Phase 5 (CSS): 30 min
- Phase 6 (HTML Files): 30 min
- Phase 7 (Docs/Plans): 45 min
- Phase 8 (Config): 20 min
- Phase 9 (Verification): 30 min
- Phase 10 (Git): 15 min

## Notes for Engineer

### Critical Points

1. **Don't just find-and-replace** - Read the context and ensure natural language flow
2. **Preserve historical context** in plan documents - add notes rather than rewriting history
3. **Archive, don't delete** legacy Citypack files - they have value as reference
4. **Test thoroughly** - this is a complete rebrand affecting every customer-facing string
5. **Watch for customizable/modular** - these concepts must be completely removed

### Common Pitfalls

- Missing references in comments or meta tags
- Hardcoded strings in template files
- References in build script console.log statements
- Email addresses or contact info referencing old brand
- Image alt text and accessibility strings
- JSON schema descriptions
- Example content in documentation

### Quality Checks

After each phase, run:
```bash
npm run validate  # Content validation
npm run build     # Build verification
git diff          # Review changes
```

---

**End of Implementation Plan**
