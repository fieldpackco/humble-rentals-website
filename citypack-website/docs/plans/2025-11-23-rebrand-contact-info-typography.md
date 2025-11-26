# Rebrand and Typography Improvements Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Remove all "Anytime Rentals" references, update contact info to amit@fieldpack.co / 310-776-0154, change "Solutions" to "Customers" in navigation, remove Roadmap feature, fix unstyled HTML sections, and improve typography.

**Architecture:** Systematic search and replace across all content JSON files, navigation updates, template inspection for unstyled sections, and CSS typography enhancements.

**Tech Stack:** JSON content files, Handlebars templates, CSS design system

---

## Task 1: Remove "Anytime Rentals" References from All Content Files

**Files:**
- Modify: `content/pages/pricing.json`
- Modify: `content/pages/features.json`
- Modify: `content/pages/contact.json`
- Modify: `content/pages/roadmap.json`
- Modify: `content/pages/how-it-works.json`
- Modify: `content/pages/gallery.json`
- Modify: `content/pages/location-managers.json`
- Modify: `content/pages/production-managers.json`
- Modify: `content/pages/gaffers.json`
- Modify: `content/pages/city-services.json`
- Modify: `content/pages/public-venues.json`
- Modify: `content/pages/street-festivals.json`
- Modify: `content/pages/experience-agencies.json`

**Step 1: Search for all "Anytime" references**

Run: `grep -r "Anytime" content/pages/ --include="*.json"`
Expected: List of files with "Anytime Rentals" or "Anytime Production Equipment Rentals"

**Step 2: Update each file to replace "Anytime Rentals" with "Labrador Field Systems"**

For each file found:
- Replace "Anytime Production Equipment Rentals" → "Labrador Field Systems"
- Replace "Anytime Rentals" → "Labrador Field Systems"
- Replace "rentals@anytimerentals.com" → "amit@fieldpack.co"
- Replace any phone numbers → "310-776-0154"

**Step 3: Verify all references removed**

Run: `grep -r "Anytime" content/pages/ --include="*.json"`
Expected: No results (or only in historical docs)

**Step 4: Commit**

```bash
git add content/pages/*.json
git commit -m "feat: rebrand from Anytime Rentals to Labrador Field Systems

- Replace all Anytime Rentals references with Labrador Field Systems
- Update contact email to amit@fieldpack.co
- Update phone to 310-776-0154"
```

---

## Task 2: Update Contact Page with New Contact Information

**Files:**
- Modify: `content/pages/contact.json`

**Step 1: Read current contact.json structure**

Run: `cat content/pages/contact.json`
Expected: See current contact structure

**Step 2: Update contact information**

Update the contact.json to include:
```json
{
  "meta": {
    "title": "Contact Labrador Field Systems",
    "description": "Get in touch with Labrador Field Systems for professional battery power solutions"
  },
  "hero": {
    "title": "Contact Labrador",
    "tagline": "Ready to power your next project?"
  },
  "contactInfo": {
    "email": "amit@fieldpack.co",
    "phone": "310-776-0154",
    "company": "Labrador Field Systems"
  }
}
```

**Step 3: Verify contact page renders correctly**

Run: `npm run build && curl -s http://localhost:3000/contact | grep "amit@fieldpack.co"`
Expected: Contact email appears in output

**Step 4: Commit**

```bash
git add content/pages/contact.json
git commit -m "feat: update contact information

- Email: amit@fieldpack.co
- Phone: 310-776-0154
- Company: Labrador Field Systems"
```

---

## Task 3: Change "Solutions" to "Customers" in Navigation

**Files:**
- Modify: `content/global/navigation.json`

**Step 1: Update navigation label**

Change line 5 in `content/global/navigation.json`:
```json
"label": "Customers",
```

**Step 2: Rebuild and verify**

Run: `npm run build && curl -s http://localhost:3000/ | grep "Customers"`
Expected: "Customers" appears in navigation

**Step 3: Commit**

```bash
git add content/global/navigation.json
git commit -m "feat: rename Solutions to Customers in navigation"
```

---

## Task 4: Remove Roadmap Feature from Navigation

**Files:**
- Modify: `content/global/navigation.json`

**Step 1: Remove roadmap menu item**

In `content/global/navigation.json`, delete the entire roadmap menu item object (lines 34-37):
```json
{
  "label": "Roadmap",
  "href": "/roadmap"
},
```

Note: Remove the trailing comma from the "Rental" menu item above it.

**Step 2: Rebuild and verify**

Run: `npm run build && curl -s http://localhost:3000/ | grep -i "roadmap"`
Expected: No "Roadmap" link in navigation

**Step 3: Commit**

```bash
git add content/global/navigation.json
git commit -m "feat: remove Roadmap from navigation"
```

---

## Task 5: Identify and Fix Unstyled HTML Sections

**Files:**
- Check: All built HTML files (`*.html`)
- Modify: Templates as needed

**Step 1: Scan for unstyled sections**

Run browser inspection or:
```bash
npm run build
curl -s http://localhost:3000/experience-agencies > /tmp/page.html
grep -E "class=\"[^\"]*\"" /tmp/page.html | grep -v "class=\"section\|class=\"card\|class=\"grid\|class=\"hero\|class=\"btn"
```

Look for sections still using old custom classes that don't exist in CSS.

**Step 2: Check remaining templates for custom classes**

Run: `grep -r "class=\"" templates/components/ | grep -v "section\|card\|grid\|hero\|btn\|nav"`
Expected: List any templates still using unmapped CSS classes

**Step 3: Fix any identified templates**

For each template with unmapped classes:
- Replace with actual CSS utility classes from `css/layouts.css` and `css/components.css`
- Follow the pattern: `.section`, `.section-title`, `.grid grid-N`, `.card`, etc.

**Step 4: Rebuild and visually verify**

Run: `npm run build`
Navigate to: http://localhost:3000 and check all pages for styling

**Step 5: Commit**

```bash
git add templates/components/*.hbs
git commit -m "fix: update remaining templates to use design system classes"
```

---

## Task 6: Improve Typography System

**Files:**
- Modify: `css/design-system.css`

**Step 1: Review current typography scale**

Run: `grep "font-size" css/design-system.css | head -20`
Expected: See current size scale

**Step 2: Enhance typography variables**

Add improved typography in `css/design-system.css` after existing font sizes:

```css
/* Typography Improvements */
--font-size-hero: clamp(48px, 8vw, 96px);
--font-size-section-title: clamp(32px, 5vw, 56px);
--font-size-card-title: clamp(18px, 2.5vw, 24px);

/* Improved line heights for readability */
--line-height-hero: 1.05;
--line-height-heading: 1.2;
--line-height-body: 1.6;

/* Enhanced letter spacing */
--letter-spacing-hero: -0.03em;
--letter-spacing-heading: -0.02em;
--letter-spacing-body: -0.01em;
```

**Step 3: Apply improved typography to existing classes**

In `css/layouts.css`, update:

```css
.hero-title {
    font-size: var(--font-size-hero);
    line-height: var(--line-height-hero);
    letter-spacing: var(--letter-spacing-hero);
}

.section-title {
    font-size: var(--font-size-section-title);
    line-height: var(--line-height-heading);
    letter-spacing: var(--letter-spacing-heading);
}

.card-title {
    font-size: var(--font-size-card-title);
    line-height: var(--line-height-heading);
    letter-spacing: var(--letter-spacing-heading);
}

body, p, .card-description {
    line-height: var(--line-height-body);
    letter-spacing: var(--letter-spacing-body);
}
```

**Step 4: Test responsive typography**

Run: `npm run build`
Test at: http://localhost:3000 at various screen sizes (mobile, tablet, desktop)
Expected: Typography scales smoothly, remains readable at all sizes

**Step 5: Commit**

```bash
git add css/design-system.css css/layouts.css
git commit -m "feat: improve typography with responsive scaling and enhanced readability

- Add clamp() for responsive font sizes
- Improve line-height for better readability
- Enhance letter-spacing for premium feel"
```

---

## Task 7: Final Verification and Build

**Files:**
- All modified files

**Step 1: Run complete build**

Run: `npm run build`
Expected: All 15 pages build successfully

**Step 2: Verify key changes on homepage**

Navigate to: http://localhost:3000
Verify:
- [ ] No "Anytime Rentals" text visible
- [ ] Navigation shows "Customers" not "Solutions"
- [ ] No "Roadmap" link in navigation
- [ ] All sections have proper styling
- [ ] Typography looks improved and responsive
- [ ] Contact info shows amit@fieldpack.co and 310-776-0154

**Step 3: Verify contact page**

Navigate to: http://localhost:3000/contact
Verify:
- [ ] Email: amit@fieldpack.co
- [ ] Phone: 310-776-0154
- [ ] Company: Labrador Field Systems

**Step 4: Scan all pages for "Anytime"**

Run: `grep -r "Anytime" *.html`
Expected: No results in built HTML files

**Step 5: Final commit**

```bash
git add -A
git commit -m "chore: final verification of rebranding and typography improvements

All Anytime Rentals references removed
Contact info updated
Navigation updated
Typography improved"
```

---

## Completion Checklist

- [ ] All "Anytime Rentals" references removed from content
- [ ] Contact email updated to amit@fieldpack.co
- [ ] Contact phone updated to 310-776-0154
- [ ] Navigation changed from "Solutions" to "Customers"
- [ ] Roadmap removed from navigation
- [ ] All HTML sections properly styled
- [ ] Typography improved with responsive scaling
- [ ] All pages build without errors
- [ ] Visual verification complete

