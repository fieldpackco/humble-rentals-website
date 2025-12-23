# Rebrand: Citypack → Humble - Implementation Plan

**Date:** November 27, 2025
**Objective:** Rebrand entire website from "Citypack" to "Humble" (Humble Rentals, LLC)

## Branding Guidelines

### Company Names:
- **Primary:** "Humble"
- **Legal:** "Humble Rentals, LLC"
- **Usage:**
  - Logo/Navigation: "HUMBLE"
  - Footer copyright: "Humble Rentals, LLC" or "Humble"
  - Content: "Humble" (keep it simple and clean)

### What to Replace:
- "Citypack" → "Humble"
- "CITYPACK" → "HUMBLE"
- "citypack" → "humble"

## Files to Update

### 1. Global Content (Navigation & Footer)
- `content/global/navigation.json` - Logo text
- `content/global/footer.json` - Copyright, company name

### 2. Page Content (20+ files)
All JSON files in `content/pages/`:
- home.json
- solutions.json
- features.json
- specifications.json
- pricing.json
- customers.json
- company.json
- contact.json
- resources.json
- technology.json
- impact.json
- roadmap.json
- how-it-works.json
- cities.json
- city-services.json
- street-festivals.json
- public-venues.json
- gaffers.json
- location-managers.json
- production-managers.json
- experience-agencies.json
- gallery.json

### 3. Documentation Files
- `CLAUDE.md` - Project description
- `README.md` - Project title and description
- `DESIGN_SYSTEM.md` - Company references
- `TODO.md` - Any company references
- `package.json` - Name, description, repository

### 4. Configuration Files
- `_redirects` - Any hardcoded URLs

### 5. CSS Files (Headers/Comments)
- `css/grid-system.css` - Header comments
- `css/anduril-style.css` - Header comments (if any)

### 6. Template Files
- Check all `.hbs` files for hardcoded "Citypack" references
- `templates/pages/landing-page-anduril.hbs`
- `templates/components/footer.hbs`
- `templates/components/nav-anduril.hbs`

### 7. Plan Documentation
- `docs/plans/2025-11-27-anduril-grid-layout-implementation.md`
- `docs/plans/2025-11-27-exact-anduril-grid-replica.md`

## Implementation Steps

### Phase 1: Global Navigation & Footer
Update global content files:
- `content/global/navigation.json`: "CITYPACK" → "HUMBLE"
- `content/global/footer.json`: Update copyright to "Humble Rentals, LLC"

### Phase 2: Update All Page Content
Bulk update all content JSON files:
```bash
find content/pages -name "*.json" -type f -exec sed -i '' 's/Citypack/Humble/g' {} +
find content/pages -name "*.json" -type f -exec sed -i '' 's/CITYPACK/HUMBLE/g' {} +
find content/pages -name "*.json" -type f -exec sed -i '' 's/citypack/humble/g' {} +
```

### Phase 3: Update Documentation
Update:
- `CLAUDE.md` - Project overview
- `README.md` - Title and description
- `DESIGN_SYSTEM.md` - Company references
- `package.json` - Update to version 3.0.0 with new name

### Phase 4: Update CSS Comments
- `css/grid-system.css` - Header comment

### Phase 5: Update Templates (if needed)
Check for hardcoded references in:
- `templates/pages/landing-page-anduril.hbs`
- `templates/components/footer.hbs`

### Phase 6: Validate Content
Run validation to ensure no JSON errors:
```bash
npm run validate
```

### Phase 7: Build and Test
```bash
npm run build
```

Check generated HTML files for any remaining "Citypack" references.

### Phase 8: Update Repository
Consider renaming repository (optional):
- Current: `citypack-website`
- New: `humble-website` or keep as-is

### Phase 9: Commit Changes
Commit with detailed message explaining rebrand.

## Verification Checklist

After implementation, verify:
- [ ] Logo in navigation shows "HUMBLE"
- [ ] Footer copyright shows "Humble Rentals, LLC" or "Humble"
- [ ] All page titles/content use "Humble"
- [ ] Meta descriptions updated
- [ ] No "Citypack" references in generated HTML
- [ ] All links and navigation work
- [ ] Build completes successfully
- [ ] Content validation passes

## Notes

- Keep URLs the same (no need to change file names)
- Repository name can stay as `citypack-website` or be updated later
- Focus on content and branding, not file structure
- This is purely a content rebrand, no design changes needed

## Color Scheme
Keep existing Citypack color scheme:
- Primary Orange: #FF6B35
- Accent Gold: #F4B942
- Neutral colors remain the same

These colors now represent Humble's brand identity.
