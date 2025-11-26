# Content Editing Guide

## Overview

All website content lives in JSON files in the `content/` directory. Edit these files to update the website - no HTML knowledge required.

This guide will walk you through safely editing content, validating your changes, and deploying updates to the live website.

## Content Structure

```
content/
├── pages/              # Individual page content (15 total pages)
│   ├── home.json                # Homepage (builds to index.html)
│   ├── experience-agencies.json # Solutions menu
│   ├── production-managers.json # Solutions menu
│   ├── gaffers.json             # Solutions menu
│   ├── location-managers.json   # Solutions menu
│   ├── city-services.json       # Solutions menu
│   ├── public-venues.json       # Solutions menu
│   ├── street-festivals.json    # Solutions menu
│   ├── specifications.json      # Product menu
│   ├── features.json            # Product menu
│   ├── gallery.json             # Product menu
│   ├── pricing.json             # Rental menu
│   ├── how-it-works.json        # Rental menu
│   ├── roadmap.json             # Top-level page
│   └── contact.json             # Top-level page
├── global/            # Shared across all pages
│   ├── navigation.json          # Dropdown navigation structure
│   └── footer.json
└── schemas/           # Content validation rules (DO NOT EDIT)
    ├── page.schema.json         # Standard page schema
    ├── home.schema.json         # Homepage-specific schema
    ├── hero.schema.json
    └── benefits.schema.json
```

## Quick Start Workflow

1. **Edit** a JSON file in `content/pages/` or `content/global/`
2. **Validate** your changes: `npm run validate`
3. **Preview** locally: `npm run dev`
4. **Commit** and push to deploy

## Editing Page Content

### 1. Find Your Page

Open the appropriate JSON file in `content/pages/`:

**Homepage:**
- Homepage: `home.json` (builds to `index.html`)

**Solutions Menu (Persona Pages):**
- Experience Agencies: `experience-agencies.json`
- Production Managers: `production-managers.json`
- Gaffers & Lighting: `gaffers.json`
- Location Managers: `location-managers.json`
- City Services & Permits: `city-services.json`
- Public Venues & Events: `public-venues.json`
- Street Festivals: `street-festivals.json`

**Product Menu:**
- Specifications: `specifications.json`
- Features: `features.json`
- Gallery: `gallery.json`

**Rental Menu:**
- Pricing: `pricing.json`
- How It Works: `how-it-works.json`

**Other Pages:**
- Roadmap: `roadmap.json`
- Contact: `contact.json`

### 2. Understanding Section Types

Each page is composed of sections. Here are the most common types:

#### Meta (SEO)

Controls how the page appears in search engines and browser tabs.

```json
"meta": {
  "title": "LAB SEVEN for Experience Agencies | Labrador Field Systems",
  "description": "Silent battery power for brand activations and experiential events. Get approved for impossible locations without generator drama."
}
```

**Rules:**
- **title**: 10-70 characters (appears in browser tab and Google results)
- **description**: 50-160 characters (appears in Google search results)

**Example:**
```json
"meta": {
  "title": "Your New Page Title | Labrador Field Systems",
  "description": "A compelling description that explains what visitors will find on this page and includes relevant keywords."
}
```

#### Hero Section

The top section of the page - the first thing visitors see.

```json
"hero": {
  "title": "Power immersive experiences anywhere",
  "tagline": "No refueling. No noise. More power than a 7000 watt generator. 60A silent power for brand activations, pop-ups, and installations.",
  "cta": {
    "primary": {
      "text": "Contact Labrador",
      "href": "#contact"
    },
    "secondary": {
      "text": "Book a Demo",
      "href": "#contact"
    }
  }
}
```

**Rules:**
- **title**: 10-100 characters, clear and compelling
- **tagline**: 20-300 characters, explains the value proposition
- **cta.primary/secondary**: Call-to-action buttons
  - **text**: Button label (2-30 characters)
  - **href**: Where the button links (use `#section-name` for same-page links, or full URLs)

**Example:**
```json
"hero": {
  "title": "Transform your production workflow",
  "tagline": "Professional-grade battery power that replaces noisy generators. Silent, powerful, and approved for indoor use.",
  "cta": {
    "primary": {
      "text": "Get Started",
      "href": "#contact"
    },
    "secondary": {
      "text": "Learn More",
      "href": "#benefits"
    }
  }
}
```

#### Benefits

Highlights the advantages of LAB SEVEN for your audience.

```json
"benefits": {
  "title": "Built for experiential marketing",
  "items": [
    {
      "icon": "✓",
      "title": "Get approved for impossible locations",
      "description": "Hotels, rooftops, retail spaces, historic buildings. Silent operation means yes from venues that always say no to generators."
    },
    {
      "icon": "🎯",
      "title": "Protect the brand experience",
      "description": "Your activation isn't competing with generator noise. Guests hear the music, the message, the moment—not a diesel engine."
    }
  ]
}
```

**Rules:**
- **title**: Section heading (5-80 characters)
- **items**: Array of 2-6 benefit items
  - **icon**: Single emoji or symbol (✓, ⚡, 🎯, 🔇, 💪, etc.)
  - **title**: Benefit headline (5-80 characters)
  - **description**: Detailed explanation (20-300 characters)

**Adding a new benefit:**
```json
{
  "icon": "🚀",
  "title": "Deploy faster than ever",
  "description": "Setup takes under 5 minutes. No permits, no fuel logistics, no waiting for fire marshal approval."
}
```

#### Problem

Describes the challenges your audience faces (builds empathy).

```json
"problem": {
  "title": "What experience agencies deal with today",
  "intro": "Generator drama kills brand moments and limits creative possibilities",
  "items": [
    {
      "title": "Venues say no",
      "description": "Noise, exhaust, insurance, fire code. Premium locations reject generators, limiting your creative options."
    }
  ]
}
```

#### Solution

Shows how LAB SEVEN solves those problems.

```json
"solution": {
  "title": "How LAB SEVEN solves it",
  "items": [
    {
      "title": "Silent approval",
      "description": "Zero emissions, zero noise. Indoor-approved power opens previously impossible venues."
    }
  ]
}
```

#### Specs

Technical specifications displayed as key metrics.

```json
"specs": {
  "title": "Power for full activations",
  "items": [
    {
      "value": "10kW",
      "label": "Continuous output"
    },
    {
      "value": "8+ hrs",
      "label": "Typical runtime"
    }
  ]
}
```

#### Journey

Before/after comparison showing the difference LAB SEVEN makes.

```json
"journey": {
  "title": "A day on activation",
  "comparison": {
    "without": {
      "title": "Without LAB SEVEN",
      "description": "Day starts with 2-hour generator setup and fire marshal inspection..."
    },
    "with": {
      "title": "With LAB SEVEN",
      "description": "Battery delivered and placed before crew call. Silent all day..."
    }
  }
}
```

#### Case Study

Real-world example of LAB SEVEN in action.

```json
"caseStudy": {
  "title": "Real activation, real results",
  "content": [
    "Luxury automotive brand launch in downtown hotel ballroom.",
    "LAB SEVEN powered full LED wall, theatrical lighting package.",
    "Results: Zero venue complaints. Zero delays."
  ],
  "quote": "First time we've powered a hotel ballroom event without generator restrictions."
}
```

#### FAQ

Common questions and answers.

```json
"faq": {
  "title": "Frequently asked questions",
  "items": [
    {
      "question": "Can it power LED walls and video playback?",
      "answer": "Yes. 10kW continuous output handles full LED walls, video playback systems, theatrical lighting, and audio simultaneously."
    }
  ]
}
```

#### Final CTA

Call-to-action at the bottom of the page.

```json
"finalCta": {
  "title": "Ready to power your next activation?",
  "description": "Contact Labrador Field Systems or book a demo to see LAB SEVEN in action",
  "cta": {
    "primary": {
      "text": "Contact Labrador",
      "href": "mailto:contact@labradorfieldystems.com"
    },
    "secondary": {
      "text": "Book a Site Visit",
      "href": "#"
    }
  },
  "contactInfo": {
    "company": "Available through Anytime Production Equipment Rentals",
    "phone": "818.394.9675",
    "email": "rentals@anytimerentals.com"
  }
}
```

### 3. Validate Your Changes

Before previewing or deploying, always validate your content:

```bash
npm run validate
```

**Success looks like:**
```
Loaded 3 schemas
✅ experience-agencies.json is valid
✅ street-festivals.json is valid
✅ All content validated successfully
```

**If validation fails:**
```
❌ experience-agencies.json is invalid
Error: data/meta/title must be at least 10 characters
```

Read the error message carefully. It tells you:
- Which file has the error
- Which field is invalid (e.g., `data/meta/title`)
- What's wrong (e.g., "must be at least 10 characters")

### 4. Preview Your Changes Locally

Start the development server to see your changes in real-time:

```bash
npm run dev
```

This will:
1. Build the site from your JSON content
2. Start a local server at `http://localhost:3000`
3. Open the site in your browser
4. **Auto-reload** whenever you save changes to JSON files

**Workflow:**
1. Run `npm run dev` once
2. Edit JSON files in your editor
3. Save the file
4. Browser automatically refreshes with your changes
5. Repeat until satisfied

Press `Ctrl+C` in the terminal to stop the dev server.

### 5. Deploy Your Changes

Once you're happy with your changes:

```bash
git add content/pages/your-file.json
git commit -m "Update content for experience agencies page"
git push origin main
```

Netlify will automatically build and deploy your changes in ~2 minutes.

## Editing Global Content

Global content appears on every page (navigation and footer).

### Navigation with Dropdown Menus

Edit `content/global/navigation.json`:

```json
{
  "logo": "LABRADOR",
  "menuItems": [
    {
      "label": "Solutions",
      "dropdown": true,
      "items": [
        { "text": "Experience Agencies", "href": "/experience-agencies" },
        { "text": "Production Managers", "href": "/production-managers" }
      ]
    },
    {
      "label": "Roadmap",
      "href": "/roadmap"
    }
  ]
}
```

**Navigation Structure:**

There are two types of menu items:

1. **Dropdown Menu** (like Solutions, Product, Rental):
```json
{
  "label": "Solutions",
  "dropdown": true,
  "items": [
    { "text": "Item Name", "href": "/page-url" }
  ]
}
```

2. **Simple Link** (like Roadmap, Contact):
```json
{
  "label": "Roadmap",
  "href": "/roadmap"
}
```

**To add a new dropdown menu:**
```json
{
  "label": "New Menu",
  "dropdown": true,
  "items": [
    { "text": "First Option", "href": "/first-option" },
    { "text": "Second Option", "href": "/second-option" }
  ]
}
```

**To add an item to an existing dropdown:**
Find the dropdown menu (e.g., "Solutions") and add a new item to its `items` array:
```json
{
  "text": "New Page",
  "href": "/new-page"
}
```

**Link types:**
- Use clean URLs: `/specifications` (not `/specifications.html`)
- Same-page section: `#section-id` (e.g., `#contact`)
- External site: Full URL (e.g., `https://labradorfieldystems.com`)

### Footer

Edit `content/global/footer.json`:

```json
{
  "copyright": "© 2025 Labrador Field Systems. All rights reserved.",
  "homeLink": {
    "text": "Return to main site",
    "href": "index.html"
  }
}
```

## JSON Editing Tips

### Valid JSON Format

JSON is strict about formatting. Follow these rules:

**✅ Good:**
```json
{
  "title": "My Title",
  "description": "My description here"
}
```

**❌ Bad:**
```json
{
  "title": "My Title",
  "description": "My description here",  ← Extra comma
}
```

**❌ Bad:**
```json
{
  title: "My Title",  ← Missing quotes around key
  "description": 'My description'  ← Must use double quotes
}
```

### Common JSON Mistakes

1. **Trailing commas:** Don't add a comma after the last item
   ```json
   {
     "item1": "value",
     "item2": "value"  ← No comma here
   }
   ```

2. **Use double quotes:** Single quotes don't work in JSON
   ```json
   "text": "Use double quotes"  ← Correct
   "text": 'Not single quotes'  ← Wrong
   ```

3. **Escape special characters:** If your text includes quotes
   ```json
   "quote": "He said \"hello\" to me"
   ```

4. **Arrays need brackets:** Multiple items use `[]`
   ```json
   "items": [
     { "title": "Item 1" },
     { "title": "Item 2" }
   ]
   ```

### Using a JSON Validator

Most code editors highlight JSON errors:
- **VS Code:** Install "JSON Tools" extension
- **Sublime Text:** Built-in JSON syntax checking
- **Online:** Use https://jsonlint.com/ to check your JSON

### Multi-line Text

Keep long text readable by breaking it into multiple lines in your editor, but remember it's still one string in JSON:

```json
"description": "This is a long description that explains the benefit in detail. You can write it on multiple lines in your editor, but it will appear as one continuous paragraph on the website."
```

## Common Content Editing Tasks

### Task: Update Page Title and Description

1. Open `content/pages/experience-agencies.json`
2. Edit the `meta` section:
   ```json
   "meta": {
     "title": "New Title | Labrador Field Systems",
     "description": "New description that appears in search results and social media shares."
   }
   ```
3. Validate: `npm run validate`
4. Preview: `npm run dev`
5. Commit and push

### Task: Add a New Benefit

1. Open your page JSON file
2. Find the `benefits.items` array
3. Add a new item:
   ```json
   "benefits": {
     "title": "Built for experiential marketing",
     "items": [
       {
         "icon": "✓",
         "title": "Existing benefit",
         "description": "Existing description"
       },
       {
         "icon": "🚀",
         "title": "New benefit title",
         "description": "New benefit description explaining the advantage."
       }
     ]
   }
   ```
4. Validate and preview

### Task: Change Call-to-Action Buttons

1. Find the section with CTA buttons (usually `hero` or `finalCta`)
2. Edit the text and/or href:
   ```json
   "cta": {
     "primary": {
       "text": "New Button Text",
       "href": "mailto:new-email@example.com"
     },
     "secondary": {
       "text": "Learn More",
       "href": "#benefits"
     }
   }
   ```
3. Validate and preview

### Task: Update Contact Information

1. Open the page JSON file
2. Find `finalCta.contactInfo`:
   ```json
   "contactInfo": {
     "company": "Available through Anytime Production Equipment Rentals",
     "phone": "818.394.9675",
     "email": "rentals@anytimerentals.com"
   }
   ```
3. Update as needed
4. Validate and preview

### Task: Add a New FAQ

1. Find the `faq.items` array
2. Add a new question/answer pair:
   ```json
   "faq": {
     "title": "Frequently asked questions",
     "items": [
       {
         "question": "Existing question?",
         "answer": "Existing answer."
       },
       {
         "question": "New question here?",
         "answer": "Answer to the new question with helpful details."
       }
     ]
   }
   ```
3. Validate and preview

### Task: Add a Page to a Dropdown Menu

1. Open `content/global/navigation.json`
2. Find the dropdown menu you want to edit (e.g., "Solutions")
3. Add a new item to the `items` array:
   ```json
   {
     "label": "Solutions",
     "dropdown": true,
     "items": [
       { "text": "Experience Agencies", "href": "/experience-agencies" },
       { "text": "New Solution Page", "href": "/new-solution" }
     ]
   }
   ```
4. Validate and preview
5. **Note:** Navigation changes affect ALL pages

### Task: Create a New Dropdown Menu

1. Open `content/global/navigation.json`
2. Add a new menu item to the `menuItems` array:
   ```json
   {
     "label": "Resources",
     "dropdown": true,
     "items": [
       { "text": "Case Studies", "href": "/case-studies" },
       { "text": "Downloads", "href": "/downloads" }
     ]
   }
   ```
3. Validate and preview
4. **Note:** You'll also need to create the corresponding page JSON files

## Content Best Practices

### Writing Effective Headlines

- **Be specific:** "Silent power for rooftop events" vs. "Better power"
- **Lead with benefits:** What the reader gets, not what the product is
- **Use action words:** "Get approved," "Deploy faster," "Save time"
- **Match your audience:** Use language they use in their work

### Writing Descriptions

- **Start with the benefit:** Don't bury the lead
- **Be concrete:** "Setup in 5 minutes" vs. "Quick setup"
- **Show, don't tell:** Use real scenarios and examples
- **Keep it scannable:** Break long text into multiple benefits

### Choosing Icons

Use icons that reinforce your message:
- ✓ (checkmark) - Approval, success, benefits
- ⚡ (lightning) - Speed, power, energy
- 🎯 (target) - Precision, focus, goals
- 🔇 (mute) - Silence, quiet operation
- 💪 (muscle) - Strength, capability
- 🚀 (rocket) - Innovation, advancement
- 💰 (money) - Cost savings, value
- ⏱️ (timer) - Time savings, efficiency

## Safety Guidelines

### SAFE to Edit

These files are designed for content editing:
- ✅ Any file in `content/pages/`
- ✅ Files in `content/global/` (navigation.json, footer.json)

### DO NOT Edit

These files control the build system and will break the site:
- ❌ Files in `content/schemas/` (validation rules)
- ❌ Files in `templates/` (HTML templates)
- ❌ Files in `src/` (build scripts)
- ❌ Files in `css/` (stylesheets)
- ❌ `package.json` (dependencies and scripts)

### Dangerous Operations

- ❌ Don't delete required fields (like `meta`, `hero`)
- ❌ Don't change field names (e.g., `"title"` → `"heading"`)
- ❌ Don't change data types (e.g., string to number)
- ❌ Don't delete sections other pages might reference
- ⚠️ Always validate before committing

## Troubleshooting

### "npm: command not found"

**Problem:** Node.js is not installed.

**Solution:**
1. Install Node.js from https://nodejs.org/
2. Restart your terminal
3. Try `npm run validate` again

### Validation Error: "must be at least X characters"

**Problem:** Text is too short.

**Solution:** Add more content until it meets the minimum length.

Example:
```json
// ❌ Too short (8 characters)
"title": "Benefits"

// ✅ Good (23 characters)
"title": "Benefits for Your Team"
```

### Validation Error: "must be at most X characters"

**Problem:** Text is too long.

**Solution:** Shorten the text or break it into multiple sections.

### Validation Error: "should have required property"

**Problem:** A required field is missing.

**Solution:** Add the missing field. Check the error message for which field is required.

Example:
```json
// ❌ Missing "description"
{
  "title": "My Benefit"
}

// ✅ Complete
{
  "title": "My Benefit",
  "description": "Description of the benefit"
}
```

### Dev Server Won't Start

**Problem:** Port 3000 is already in use.

**Solution:**
1. Find what's using port 3000: `lsof -ti:3000`
2. Kill it: `kill -9 <process-id>`
3. Or edit `src/dev-server.js` to use a different port

### Changes Not Showing in Browser

**Problem:** Browser cache or dev server not watching files.

**Solutions:**
1. Hard refresh: `Cmd+Shift+R` (Mac) or `Ctrl+Shift+R` (Windows)
2. Restart dev server: Stop (`Ctrl+C`) and run `npm run dev` again
3. Clear browser cache

### "Unexpected token" Error

**Problem:** Invalid JSON syntax.

**Solutions:**
1. Check for missing commas between items
2. Check for extra commas after last item
3. Ensure all strings use double quotes `"`
4. Ensure all brackets/braces are balanced
5. Use a JSON validator: https://jsonlint.com/

### My Changes Deployed but Don't Appear Live

**Problem:** Browser is showing cached version or Netlify build failed.

**Solutions:**
1. Check Netlify build status in your Netlify dashboard
2. Hard refresh the live site: `Cmd+Shift+R` (Mac) or `Ctrl+Shift+R` (Windows)
3. Check the build logs for errors
4. Verify your changes are in the `main` branch on GitHub

## Getting Help

If you run into issues:

1. **Read the error message carefully** - It usually tells you exactly what's wrong
2. **Check this guide** - See "Troubleshooting" section above
3. **Validate your JSON** - Run `npm run validate` to catch errors
4. **Check the schemas** - See `content/schemas/page.schema.json` for rules
5. **Review a working example** - Compare your JSON to `experience-agencies.json`
6. **Ask for help** - Contact the development team with:
   - The exact error message
   - Which file you were editing
   - What you were trying to do

## Advanced Topics

### Understanding the Dual Schema System

The website uses two different JSON schemas for validation:

1. **page.schema.json** - Used by most pages (persona pages, specs, features, etc.)
   - Enforces standard landing page structure
   - Includes: meta, hero, benefits, problem, solution, specs, journey, caseStudy, faq, finalCta

2. **home.schema.json** - Used only by `home.json`
   - Enforces hub-style homepage structure
   - Includes: meta, hero, overview, specsPreview, featuresPreview, solutionsPreview
   - Different because homepage is a preview/hub page, not a deep-dive landing page

**Why two schemas?**
The homepage (`home.json` → `index.html`) serves a different purpose than other pages. It's a hub with preview sections that link to deeper content. Persona pages and section pages are full landing pages with complete information. The different schemas enforce the correct structure for each purpose.

### Creating a New Page

To create a completely new page:

**Step 1: Create content file**
```bash
# Copy an existing page as a template
cp content/pages/experience-agencies.json content/pages/new-page.json
```

**Step 2: Edit the content**
Open `content/pages/new-page.json` and update all sections:
- Update `meta.title` and `meta.description` for SEO
- Change `hero` content to match your new page's purpose
- Update all sections (benefits, problem, solution, etc.)
- Ensure all text is unique to the new page

**Step 3: Validate your content**
```bash
npm run validate
```
This ensures your JSON structure is correct.

**Step 4: Add to navigation**

If your page should appear in a dropdown menu, edit `content/global/navigation.json`:

```json
{
  "label": "Solutions",
  "dropdown": true,
  "items": [
    { "text": "Experience Agencies", "href": "/experience-agencies" },
    { "text": "Your New Page", "href": "/new-page" }
  ]
}
```

If it's a standalone top-level page:
```json
{
  "label": "New Page",
  "href": "/new-page"
}
```

**Step 5: Add Netlify redirect (optional)**

If you want clean URLs (recommended), add a redirect to `netlify.toml`:

```toml
[[redirects]]
  from = "/new-page"
  to = "/new-page.html"
  status = 200
```

**Step 6: Build and test**
```bash
npm run build    # Build the site
npm run dev      # Preview locally
```

**Step 7: Deploy**
```bash
git add content/pages/new-page.json content/global/navigation.json netlify.toml
git commit -m "feat: add new-page"
git push origin main
```

### Adding New Pages to Dropdown Menus

**To add to existing dropdown (e.g., Solutions menu):**

1. Create your page content JSON file (see "Creating a New Page" above)
2. Open `content/global/navigation.json`
3. Find the appropriate dropdown menu
4. Add your page to the `items` array:

```json
{
  "label": "Solutions",
  "dropdown": true,
  "items": [
    { "text": "Experience Agencies", "href": "/experience-agencies" },
    { "text": "Production Managers", "href": "/production-managers" },
    { "text": "Your New Solution", "href": "/your-new-solution" }
  ]
}
```

5. Validate, build, and test
6. Commit and push

**To create a new dropdown menu:**

1. Open `content/global/navigation.json`
2. Add a new menu item with `"dropdown": true`:

```json
{
  "label": "Resources",
  "dropdown": true,
  "items": [
    { "text": "Case Studies", "href": "/case-studies" },
    { "text": "Downloads", "href": "/downloads" },
    { "text": "FAQ", "href": "/faq" }
  ]
}
```

3. Create the corresponding page JSON files
4. Validate, build, and test

### Special Page: Homepage (home.json → index.html)

The homepage is handled specially by the build system:

- **Content file:** `content/pages/home.json`
- **Schema:** `content/schemas/home.schema.json` (different from other pages)
- **Output file:** `index.html` (not `home.html`)

**Why is it different?**
- Uses `home.schema.json` instead of `page.schema.json`
- Has preview sections (specsPreview, featuresPreview, solutionsPreview) instead of full content
- Acts as a hub linking to deeper pages
- Build system automatically outputs it as `index.html`

**When editing homepage:**
- Edit `content/pages/home.json`
- Use preview sections to tease content from other pages
- Link to full pages using `/page-name` format
- Remember it has different schema requirements than other pages

### Reusing Content Across Pages

If multiple pages share the same benefit or section, consider:

1. Create the content once in the most relevant page
2. Copy it to other pages where it applies
3. Customize the wording for each audience

**Future:** We may add shared content sections in `content/global/` to avoid duplication.

### Understanding the Build System

When you run `npm run build`, here's what happens:

1. **Validation:** Checks all JSON against schemas
2. **Template Compilation:** Handlebars templates + JSON content → HTML
3. **CSS Processing:** PostCSS optimization and minification
4. **Output:** Clean HTML files in `dist/` directory

The dev server (`npm run dev`) does the same thing but also:
- Watches files for changes
- Rebuilds automatically
- Refreshes your browser
- Serves files locally

## Content Guidelines Summary

### Character Limits (enforced by validation)

| Field | Minimum | Maximum | Purpose |
|-------|---------|---------|---------|
| Meta title | 10 | 70 | SEO, browser tab |
| Meta description | 50 | 160 | Search results |
| Hero title | 10 | 100 | Page headline |
| Hero tagline | 20 | 300 | Value proposition |
| Benefit title | 5 | 80 | Benefit headline |
| Benefit description | 20 | 300 | Benefit details |
| CTA button text | 2 | 30 | Button label |

### Quality Checklist

Before committing content changes:

- [ ] All text is clear and free of typos
- [ ] Headlines are compelling and specific
- [ ] Benefits focus on audience needs
- [ ] Links are correct and working
- [ ] Contact information is up to date
- [ ] Validation passes: `npm run validate`
- [ ] Preview looks good: `npm run dev`
- [ ] Content matches brand voice
- [ ] Icons enhance the message
- [ ] Text length is appropriate (not too long/short)

---

**Ready to start editing?** Open a JSON file in `content/pages/` and make your first change. Remember: validate, preview, then commit!
