# Homepage Design Options for LAB SEVEN

**Date:** 2025-11-23
**Current Status:** Proposing design directions
**Context:** All subpages successfully migrated to Anduril-style template

---

## Option 1: Anduril-Style Consistency (Recommended)

**Philosophy:** Keep the entire site cohesive with the same Anduril template used on subpages.

### Structure
- Same layout as subpages (hero → benefits → features)
- Same gradient backgrounds (gray → white → gray)
- Same numbered cards and feature grids
- Unified visual language across entire site

### Homepage Specifics
**Hero:**
- Category: "BATTERY POWER SYSTEMS"
- Title: "LAB SEVEN" (oversized, 140px)
- Description: Current tagline about silent battery power
- Primary CTA: "Contact Labrador"
- Secondary CTA: "View Specifications"

**Benefits (3 numbered cards):**
1. True 60A Power - The only battery with 60A Bates out
2. Fastest Charging - 1 hour charge with 60A, 4-5 hours with 110v
3. Professional Grade - LFP chemistry, BMS protection, real-time monitoring

**Features (4 cards):**
1. Saves money over generators
2. Works everywhere generators can't
3. Turn any outlet into 60A distro
4. Use existing distro boxes

**Solutions Section (4 cards pointing to customer pages):**
- City Services & Permits
- Street Festivals & Public Events
- Public Venues & Events
- Experience Agencies

### Pros
- ✅ Complete visual consistency across all pages
- ✅ Simplest implementation (reuse existing template)
- ✅ Strong brand cohesion
- ✅ Easy to maintain (one design system)

### Cons
- ❌ Homepage doesn't stand out as "special"
- ❌ Less room for product showcase/imagery
- ❌ Doesn't maximize homepage's marketing potential

---

## Option 2: Enhanced Anduril Homepage

**Philosophy:** Use Anduril aesthetic but create a unique homepage template with richer content sections.

### Structure
- **Hero:** Larger, more dramatic (full viewport height)
  - Oversized "LAB SEVEN" branding
  - Animated product image or video background
  - Same gradient treatment but more dramatic scale

- **Quick Specs Bar:** Horizontal strip with 4 key specs
  - 60A OUT | 1 HR CHARGE | 7.5 kWh | BATES DISTRO
  - Black background with orange accent numbers

- **Benefits:** Same 3 numbered cards as Option 1

- **Product Showcase:** Split-screen section
  - Left: Large product image/3D view
  - Right: Rotating feature highlights
  - Anduril's asymmetric 60/40 layout

- **Solutions Grid:** 4-column customer segments (same as Option 1)

- **Features:** 4 feature cards at bottom

### Pros
- ✅ Homepage feels premium and special
- ✅ Better product showcase opportunities
- ✅ Still maintains Anduril aesthetic
- ✅ More engaging for first-time visitors

### Cons
- ❌ Requires new template creation
- ❌ More complex than Option 1
- ❌ Slight inconsistency with subpages

---

## Option 3: Minimalist Landing Page

**Philosophy:** Ultra-minimal Anduril approach - less content, more impact.

### Structure
- **Hero:** Full viewport with just LAB SEVEN branding
  - Massive "LAB SEVEN" title (200px+)
  - One-line tagline
  - Single CTA: "Contact Labrador"
  - Scroll indicator at bottom

- **Key Stat Trio:** Three massive numbers
  - 60A | 1HR | 7.5kWh
  - Black cards with huge typography
  - Minimal description under each

- **Solutions:** Large typography list
  - City Services
  - Street Festivals
  - Public Venues
  - Experience Agencies
  - Each links to dedicated page

- **Single CTA Footer:** Black section
  - "Ready to power your next project?"
  - Contact button

### Pros
- ✅ Most dramatic visual impact
- ✅ Very Anduril-esque (bold minimalism)
- ✅ Fast load, easy to scan
- ✅ Forces clarity in messaging

### Cons
- ❌ May not provide enough information
- ❌ Requires visitors to click through to learn more
- ❌ Less SEO content on homepage

---

## Option 4: Two-Column Hero Split

**Philosophy:** Blend Anduril aesthetics with Apple-style product showcase.

### Structure
- **Hero:** Asymmetric split (40/60)
  - Left 40%: Text content
    - "LAB SEVEN" title
    - Tagline
    - 3 key bullet points
    - Two CTAs
  - Right 60%: Product image
    - Large LAB SEVEN unit photo
    - Gradient background behind product

- **Scrolling Spec Highlights:** Horizontal scroll cards
  - 6-8 cards with key specs
  - Swipe/scroll interaction
  - Black cards with white text

- **Benefits:** Same 3 numbered cards

- **Customer Segments:** 4 cards pointing to pages

- **Features:** 4 cards at bottom

### Pros
- ✅ Product-focused while maintaining Anduril style
- ✅ More engaging than pure text
- ✅ Good balance of info and visuals
- ✅ Modern, interactive feel

### Cons
- ❌ Requires product photography/renders
- ❌ More complex template needed
- ❌ Horizontal scroll may not work on all devices

---

## Recommendation Matrix

| Criterion | Option 1 | Option 2 | Option 3 | Option 4 |
|-----------|----------|----------|----------|----------|
| **Consistency** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Visual Impact** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Implementation Speed** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ |
| **Marketing Effectiveness** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ |
| **Maintenance** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |

---

## My Recommendation: **Option 1 (Anduril-Style Consistency)**

**Why:**
1. **Ship Fast:** Reuses existing template - can launch today
2. **Cohesive Brand:** Entire site feels like one unified product
3. **Proven Design:** Already working well on subpages
4. **Easy to Evolve:** Can enhance later if needed

**Implementation:**
- Update home.json to use "landing-page-anduril" layout
- Restructure content into hero, benefits, features, solutions
- Keep existing messaging, just adapt structure
- 15 minutes of work

**You can always enhance later** if you want more homepage pizzazz, but this gets you a solid, professional homepage immediately while maintaining perfect visual consistency.

---

## Quick Start: Option 1 Implementation

If you choose Option 1, here's the new home.json structure:

```json
{
  "layout": "landing-page-anduril",
  "meta": {
    "title": "LAB SEVEN - Labrador Field Systems",
    "description": "Silent battery power for city services, live events, and public venues. Zero emissions, zero noise."
  },
  "hero": {
    "category": "BATTERY POWER SYSTEMS",
    "title": "LAB SEVEN",
    "description": "Silent battery power for city services, live events, and public venues. True 60A output. Zero emissions, zero noise complaints, zero permits.",
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
    "title": "Built for Professional Power",
    "items": [
      {
        "title": "True 60A Power",
        "description": "The only battery with 60A Bates out. Three 20A Edison circuits and 1 60A Bates. No adapters needed."
      },
      {
        "title": "Fastest Charging",
        "description": "Charge one battery in 1 hour using 60A Bates input, or 4-5 hours using standard 110v outlet."
      },
      {
        "title": "Professional Reliability",
        "description": "LFP chemistry, BMS protection, real-time monitoring. 7.5kWh storage. Built for production demands."
      }
    ]
  },
  "features": {
    "title": "Why Teams Choose LAB SEVEN",
    "items": [
      {
        "title": "Saves Money Over Generators",
        "description": "When you add fuel runs, fire watch, noise complaints, and slow wrap, generators cost more than the day rate suggests."
      },
      {
        "title": "Works Where Generators Can't",
        "description": "Indoor venues, noise-restricted zones, residential areas, and historic locations that prohibit generators."
      },
      {
        "title": "Turn Any Outlet Into 60A Distro",
        "description": "Plug into standard 15/20A receptacle, cap the draw, let the pack cover peaks. Less friction, fewer noise complaints."
      },
      {
        "title": "Use Existing Distro",
        "description": "Nobody needs to change workflows. Use the same distro boxes you always have. Professional-grade compatibility."
      }
    ]
  }
}
```

---

## Next Steps

Let me know which option you prefer, and I can implement it immediately!

1. **Option 1:** Update home.json → Build → Done (15 min)
2. **Option 2:** Create enhanced template → Update home.json → Build (2-3 hours)
3. **Option 3:** Create minimal template → Update home.json → Build (1 hour)
4. **Option 4:** Create split template → Needs product images → Update home.json → Build (3-4 hours)
