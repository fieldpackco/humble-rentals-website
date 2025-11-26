# Robust Site Architecture for Rapid Iteration

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Transform static HTML site into a component-based architecture with content management, enabling rapid iteration without touching code.

**Architecture:** Template-driven system with JSON content storage, shared component library, build process for optimization, and local development server. Separates content (JSON), presentation (templates), styling (CSS), and behavior (JS).

**Tech Stack:** Node.js build system, Handlebars templates, JSON content files, PostCSS for CSS processing, live-reload dev server, Netlify deployment

---

## Current State Analysis

**Existing Structure:**
- 19 HTML files (8 using shared CSS, 11 legacy files with embedded CSS)
- 4 shared CSS files: `design-system.css`, `components.css`, `layouts.css`, `index-components.css`
- All content hardcoded in HTML
- No build process
- Static deployment to Netlify

**Problems:**
1. **Content locked in HTML** - Non-developers can't update copy
2. **Duplicate HTML** - Shared sections (nav, footer, hero) copied across files
3. **No validation** - Easy to break responsive design or accessibility
4. **Slow iteration** - Every content change requires HTML editing and deployment
5. **Legacy files** - Half the site still uses old embedded CSS approach

**Goals:**
1. **Content in JSON** - Editable by non-technical stakeholders
2. **Reusable components** - Nav, hero, benefits, etc. defined once
3. **Type safety** - Validate content structure before build
4. **Fast iteration** - Content changes = edit JSON, run build, deploy
5. **Developer experience** - Hot reload, linting, automated testing

---

## Architecture Overview

```
lab/
├── content/              # All page content (JSON)
│   ├── pages/
│   │   ├── index.json
│   │   ├── experience-agencies.json
│   │   └── ...
│   ├── global/
│   │   ├── navigation.json
│   │   ├── footer.json
│   │   └── brand.json
│   └── schemas/         # JSON schemas for validation
│       ├── page.schema.json
│       ├── hero.schema.json
│       └── ...
├── templates/           # Handlebars templates
│   ├── layouts/
│   │   ├── base.hbs
│   │   └── landing-page.hbs
│   ├── components/
│   │   ├── nav.hbs
│   │   ├── hero.hbs
│   │   ├── benefits.hbs
│   │   ├── problem.hbs
│   │   ├── solution.hbs
│   │   └── footer.hbs
│   └── pages/
│       ├── index.hbs
│       └── landing-page.hbs
├── css/                 # Existing CSS (unchanged)
│   ├── design-system.css
│   ├── components.css
│   ├── layouts.css
│   └── index-components.css
├── js/                  # Shared JavaScript
│   └── main.js
├── src/                 # Build system
│   ├── build.js         # Main build script
│   ├── validate.js      # JSON schema validation
│   └── dev-server.js    # Local dev server
├── dist/                # Built files (gitignored)
│   ├── index.html
│   ├── experience-agencies.html
│   ├── css/
│   └── ...
├── package.json
└── netlify.toml
```

---

## Task 1: Setup Build System Foundation

**Files:**
- Create: `package.json`
- Create: `.gitignore`
- Create: `src/build.js`

**Step 1: Initialize package.json**

```bash
cd /Users/amitrunchal/apps/labrador/lab/lab
npm init -y
```

Expected: `package.json` created

**Step 2: Install dependencies**

```bash
npm install --save-dev handlebars ajv chokidar browser-sync
npm install --save-dev postcss postcss-cli autoprefixer cssnano
```

Expected: `node_modules/` and `package-lock.json` created

**Step 3: Create .gitignore**

Create: `.gitignore`

```gitignore
node_modules/
dist/
.DS_Store
*.log
.env
```

**Step 4: Update package.json scripts**

Modify: `package.json`

```json
{
  "name": "lab-seven-website",
  "version": "1.0.0",
  "scripts": {
    "build": "node src/build.js",
    "dev": "node src/dev-server.js",
    "validate": "node src/validate.js",
    "clean": "rm -rf dist",
    "prebuild": "npm run clean && npm run validate"
  },
  "devDependencies": {
    "ajv": "^8.12.0",
    "autoprefixer": "^10.4.16",
    "browser-sync": "^2.29.3",
    "chokidar": "^3.5.3",
    "cssnano": "^6.0.1",
    "handlebars": "^4.7.8",
    "postcss": "^8.4.31",
    "postcss-cli": "^11.0.0"
  }
}
```

**Step 5: Create basic build script**

Create: `src/build.js`

```javascript
const fs = require('fs');
const path = require('path');
const Handlebars = require('handlebars');

const BUILD_DIR = path.join(__dirname, '../dist');
const TEMPLATES_DIR = path.join(__dirname, '../templates');
const CONTENT_DIR = path.join(__dirname, '../content');

// Ensure dist directory exists
if (!fs.existsSync(BUILD_DIR)) {
  fs.mkdirSync(BUILD_DIR, { recursive: true });
}

console.log('Build system initialized');
console.log(`Templates: ${TEMPLATES_DIR}`);
console.log(`Content: ${CONTENT_DIR}`);
console.log(`Output: ${BUILD_DIR}`);

// TODO: Implement template compilation
```

**Step 6: Test build script**

```bash
node src/build.js
```

Expected output:
```
Build system initialized
Templates: /Users/amitrunchal/apps/labrador/lab/lab/templates
Content: /Users/amitrunchal/apps/labrador/lab/lab/content
Output: /Users/amitrunchal/apps/labrador/lab/lab/dist
```

**Step 7: Commit foundation**

```bash
git add package.json package-lock.json .gitignore src/build.js
git commit -m "feat: add build system foundation

- Initialize npm project with Handlebars, AJV, PostCSS
- Create build script skeleton
- Setup gitignore for node_modules and dist"
```

---

## Task 2: Create Content Schema and Validation

**Files:**
- Create: `content/schemas/page.schema.json`
- Create: `content/schemas/hero.schema.json`
- Create: `content/schemas/benefits.schema.json`
- Create: `src/validate.js`

**Step 1: Create hero schema**

Create: `content/schemas/hero.schema.json`

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["title", "tagline", "cta"],
  "properties": {
    "title": {
      "type": "string",
      "minLength": 10,
      "maxLength": 100
    },
    "tagline": {
      "type": "string",
      "minLength": 20,
      "maxLength": 300
    },
    "cta": {
      "type": "object",
      "required": ["primary", "secondary"],
      "properties": {
        "primary": {
          "type": "object",
          "required": ["text", "href"],
          "properties": {
            "text": { "type": "string" },
            "href": { "type": "string" }
          }
        },
        "secondary": {
          "type": "object",
          "required": ["text", "href"],
          "properties": {
            "text": { "type": "string" },
            "href": { "type": "string" }
          }
        }
      }
    }
  }
}
```

**Step 2: Create benefits schema**

Create: `content/schemas/benefits.schema.json`

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["title", "items"],
  "properties": {
    "title": {
      "type": "string",
      "minLength": 5,
      "maxLength": 100
    },
    "items": {
      "type": "array",
      "minItems": 1,
      "maxItems": 6,
      "items": {
        "type": "object",
        "required": ["icon", "title", "description"],
        "properties": {
          "icon": { "type": "string" },
          "title": {
            "type": "string",
            "minLength": 5,
            "maxLength": 80
          },
          "description": {
            "type": "string",
            "minLength": 20,
            "maxLength": 300
          }
        }
      }
    }
  }
}
```

**Step 3: Create page schema**

Create: `content/schemas/page.schema.json`

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["meta", "hero"],
  "properties": {
    "meta": {
      "type": "object",
      "required": ["title", "description"],
      "properties": {
        "title": {
          "type": "string",
          "minLength": 10,
          "maxLength": 70
        },
        "description": {
          "type": "string",
          "minLength": 50,
          "maxLength": 160
        }
      }
    },
    "hero": {
      "$ref": "hero.schema.json"
    },
    "benefits": {
      "$ref": "benefits.schema.json"
    },
    "problem": {
      "type": "object",
      "properties": {
        "title": { "type": "string" },
        "intro": { "type": "string" },
        "items": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["title", "description"],
            "properties": {
              "title": { "type": "string" },
              "description": { "type": "string" }
            }
          }
        }
      }
    },
    "solution": {
      "type": "object",
      "properties": {
        "title": { "type": "string" },
        "items": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["title", "description"],
            "properties": {
              "title": { "type": "string" },
              "description": { "type": "string" }
            }
          }
        }
      }
    }
  }
}
```

**Step 4: Create validation script**

Create: `src/validate.js`

```javascript
const fs = require('fs');
const path = require('path');
const Ajv = require('ajv');

const SCHEMAS_DIR = path.join(__dirname, '../content/schemas');
const PAGES_DIR = path.join(__dirname, '../content/pages');

const ajv = new Ajv({ allErrors: true, verbose: true });

// Load all schemas
const schemas = {};
const schemaFiles = fs.readdirSync(SCHEMAS_DIR);

schemaFiles.forEach(file => {
  const schemaPath = path.join(SCHEMAS_DIR, file);
  const schema = JSON.parse(fs.readFileSync(schemaPath, 'utf8'));
  const schemaId = file.replace('.schema.json', '');
  schemas[schemaId] = schema;
  ajv.addSchema(schema, schemaId);
});

console.log(`Loaded ${Object.keys(schemas).length} schemas`);

// Validate all page content files
let hasErrors = false;

if (fs.existsSync(PAGES_DIR)) {
  const pageFiles = fs.readdirSync(PAGES_DIR).filter(f => f.endsWith('.json'));

  pageFiles.forEach(file => {
    const pagePath = path.join(PAGES_DIR, file);
    const pageData = JSON.parse(fs.readFileSync(pagePath, 'utf8'));

    const validate = ajv.getSchema('page');
    const valid = validate(pageData);

    if (!valid) {
      console.error(`\n❌ Validation failed for ${file}:`);
      console.error(JSON.stringify(validate.errors, null, 2));
      hasErrors = true;
    } else {
      console.log(`✅ ${file} is valid`);
    }
  });
}

if (hasErrors) {
  console.error('\n❌ Validation failed');
  process.exit(1);
} else {
  console.log('\n✅ All content validated successfully');
  process.exit(0);
}
```

**Step 5: Test validation with empty pages directory**

```bash
node src/validate.js
```

Expected output:
```
Loaded 3 schemas
✅ All content validated successfully
```

**Step 6: Commit schemas and validation**

```bash
git add content/schemas/ src/validate.js
git commit -m "feat: add content validation with JSON schemas

- Create hero, benefits, and page schemas
- Build validation script using AJV
- Enforce content structure and length constraints"
```

---

## Task 3: Extract Content from experience-agencies.html

**Files:**
- Create: `content/pages/experience-agencies.json`
- Create: `content/global/navigation.json`
- Create: `content/global/footer.json`

**Step 1: Create navigation content**

Create: `content/global/navigation.json`

```json
{
  "logo": "LABRADOR",
  "links": [
    { "text": "Home", "href": "index.html" },
    { "text": "Benefits", "href": "#benefits" },
    { "text": "Solution", "href": "#solution" },
    { "text": "Case Study", "href": "#case-study" },
    { "text": "FAQ", "href": "#faq" }
  ]
}
```

**Step 2: Create footer content**

Create: `content/global/footer.json`

```json
{
  "copyright": "© 2025 Labrador Field Systems. All rights reserved.",
  "homeLink": {
    "text": "Return to main site",
    "href": "index.html"
  }
}
```

**Step 3: Extract experience-agencies content**

Create: `content/pages/experience-agencies.json`

```json
{
  "meta": {
    "title": "LAB SEVEN for Experience Agencies | Labrador Field Systems",
    "description": "Silent battery power for brand activations and experiential events. Get approved for impossible locations without generator drama."
  },
  "hero": {
    "title": "Power immersive experiences anywhere",
    "tagline": "No refueling. No noise. More power than a 7000 watt generator. 60A silent power for brand activations, pop-ups, and installations. No permits, no noise complaints, no limits.",
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
  },
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
      },
      {
        "icon": "⚡",
        "title": "Deploy faster, wrap faster",
        "description": "Under 5 minutes to power on. No fuel logistics, no fire watch, no generator babysitting. Your crew focuses on the experience, not the power."
      }
    ]
  },
  "problem": {
    "title": "What experience agencies deal with today",
    "intro": "Generator drama kills brand moments and limits creative possibilities",
    "items": [
      {
        "title": "Venues say no",
        "description": "Noise, exhaust, insurance, fire code. Premium locations reject generators, limiting your creative options."
      },
      {
        "title": "Budget drain",
        "description": "Generator rentals ($500+/day) plus fuel, permits, and fire watch eat into activation budgets."
      },
      {
        "title": "Noise ruins moments",
        "description": "Generator noise competes with your activation, ruins video content, and damages the brand experience."
      },
      {
        "title": "Setup complexity",
        "description": "Generator logistics reduce time for actual experience design and execution."
      }
    ]
  },
  "solution": {
    "title": "How LAB SEVEN solves it",
    "items": [
      {
        "title": "Silent approval",
        "description": "Zero emissions, zero noise. Indoor-approved power opens previously impossible venues. Say yes to rooftop activations, hotel ballrooms, historic buildings, and retail spaces that prohibit generators."
      },
      {
        "title": "True cost savings",
        "description": "Cost-competitive with generators once you factor in permits, fuel, fire watch, and crew time. Transparent rental pricing includes delivery, pickup, and backup generator."
      },
      {
        "title": "White-glove service",
        "description": "Anytime Rentals handles delivery, placement, and pickup. You don't touch it. Your crew focuses on creating experiences, not managing power logistics."
      },
      {
        "title": "Real power",
        "description": "60A Bates out plus three 20A Edison circuits. Power full AV rigs, theatrical lighting, interactive elements, and charging stations simultaneously."
      }
    ]
  }
}
```

**Step 4: Validate experience-agencies content**

```bash
npm run validate
```

Expected output:
```
Loaded 3 schemas
✅ experience-agencies.json is valid
✅ All content validated successfully
```

**Step 5: Commit extracted content**

```bash
git add content/pages/experience-agencies.json content/global/
git commit -m "feat: extract experience-agencies content to JSON

- Create navigation and footer global content
- Extract all experience-agencies.html content to JSON
- Content validates against schemas"
```

---

## Task 4: Create Handlebars Component Templates

**Files:**
- Create: `templates/components/nav.hbs`
- Create: `templates/components/hero.hbs`
- Create: `templates/components/benefits.hbs`
- Create: `templates/components/problem.hbs`
- Create: `templates/components/solution.hbs`
- Create: `templates/components/footer.hbs`

**Step 1: Create navigation component**

Create: `templates/components/nav.hbs`

```handlebars
<nav>
    <div class="nav-wrapper">
        <div class="logo">{{logo}}</div>
        <ul class="nav-items">
            {{#each links}}
            <li><a href="{{href}}">{{text}}</a></li>
            {{/each}}
        </ul>
    </div>
</nav>
```

**Step 2: Create hero component**

Create: `templates/components/hero.hbs`

```handlebars
<section class="hero">
    <h1 class="animate-in">{{title}}</h1>
    <p class="tagline animate-in">{{tagline}}</p>
    <div class="cta-buttons animate-in">
        <a href="{{cta.primary.href}}" class="btn btn-primary">{{cta.primary.text}}</a>
        <a href="{{cta.secondary.href}}" class="btn btn-secondary">{{cta.secondary.text}}</a>
    </div>
</section>
```

**Step 3: Create benefits component**

Create: `templates/components/benefits.hbs`

```handlebars
<section class="benefits" id="benefits">
    <h2>{{title}}</h2>
    <div class="benefits-grid">
        {{#each items}}
        <div class="benefit-card animate-in">
            <div class="benefit-icon">{{icon}}</div>
            <h3>{{title}}</h3>
            <p>{{description}}</p>
        </div>
        {{/each}}
    </div>
</section>
```

**Step 4: Create problem component**

Create: `templates/components/problem.hbs`

```handlebars
<section class="problem" id="problem">
    <h2>{{title}}</h2>
    <p class="intro">{{intro}}</p>
    <div class="problem-grid">
        {{#each items}}
        <div class="problem-item">
            <h3>{{title}}</h3>
            <p>{{description}}</p>
        </div>
        {{/each}}
    </div>
</section>
```

**Step 5: Create solution component**

Create: `templates/components/solution.hbs`

```handlebars
<section class="solution" id="solution">
    <h2>{{title}}</h2>
    <div class="solution-grid">
        {{#each items}}
        <div class="solution-item">
            <h3>{{title}}</h3>
            <p>{{description}}</p>
        </div>
        {{/each}}
    </div>
</section>
```

**Step 6: Create footer component**

Create: `templates/components/footer.hbs`

```handlebars
<footer>
    <p>{{copyright}}</p>
    <p><a href="{{homeLink.href}}">{{homeLink.text}}</a></p>
</footer>
```

**Step 7: Commit component templates**

```bash
git add templates/components/
git commit -m "feat: create Handlebars component templates

- Add nav, hero, benefits, problem, solution, footer components
- Each component accepts data context for rendering
- Components mirror existing HTML structure"
```

---

## Task 5: Create Page Layout and Build System

**Files:**
- Create: `templates/layouts/base.hbs`
- Create: `templates/layouts/landing-page.hbs`
- Create: `templates/pages/landing-page.hbs`
- Modify: `src/build.js`

**Step 1: Create base layout**

Create: `templates/layouts/base.hbs`

```handlebars
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{meta.title}}</title>
    <meta name="description" content="{{meta.description}}">

    <!-- Shared Design System -->
    <link rel="stylesheet" href="css/design-system.css">
    <link rel="stylesheet" href="css/components.css">
    <link rel="stylesheet" href="css/layouts.css">
    {{#if additionalCSS}}
    {{#each additionalCSS}}
    <link rel="stylesheet" href="{{this}}">
    {{/each}}
    {{/if}}
</head>
<body>
    {{{body}}}

    <script>
        // Smooth scroll
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            });
        });

        // Sticky nav
        window.addEventListener('scroll', () => {
            const nav = document.querySelector('nav');
            if (window.scrollY > 10) {
                nav.classList.add('scrolled');
            } else {
                nav.classList.remove('scrolled');
            }
        });

        // Elements with .animate-in class automatically have gradient animation from CSS
    </script>
</body>
</html>
```

**Step 2: Create landing page template**

Create: `templates/pages/landing-page.hbs`

```handlebars
{{> nav navigation}}

{{> hero hero}}

{{#if benefits}}
{{> benefits benefits}}
{{/if}}

{{#if problem}}
{{> problem problem}}
{{/if}}

{{#if solution}}
{{> solution solution}}
{{/if}}

{{> footer footer}}
```

**Step 3: Update build.js to compile templates**

Modify: `src/build.js`

```javascript
const fs = require('fs');
const path = require('path');
const Handlebars = require('handlebars');

const BUILD_DIR = path.join(__dirname, '../dist');
const TEMPLATES_DIR = path.join(__dirname, '../templates');
const CONTENT_DIR = path.join(__dirname, '../content');
const CSS_DIR = path.join(__dirname, '../css');

// Ensure dist directory exists
if (!fs.existsSync(BUILD_DIR)) {
  fs.mkdirSync(BUILD_DIR, { recursive: true });
}

// Register partials (components)
const componentsDir = path.join(TEMPLATES_DIR, 'components');
const componentFiles = fs.readdirSync(componentsDir);

componentFiles.forEach(file => {
  const componentName = file.replace('.hbs', '');
  const componentPath = path.join(componentsDir, file);
  const componentTemplate = fs.readFileSync(componentPath, 'utf8');
  Handlebars.registerPartial(componentName, componentTemplate);
});

console.log(`Registered ${componentFiles.length} component partials`);

// Load base layout
const baseLayoutPath = path.join(TEMPLATES_DIR, 'layouts', 'base.hbs');
const baseLayoutTemplate = fs.readFileSync(baseLayoutPath, 'utf8');
const baseLayout = Handlebars.compile(baseLayoutTemplate);

// Load page template
const landingPagePath = path.join(TEMPLATES_DIR, 'pages', 'landing-page.hbs');
const landingPageTemplate = fs.readFileSync(landingPagePath, 'utf8');
const landingPage = Handlebars.compile(landingPageTemplate);

// Load global content
const navigationPath = path.join(CONTENT_DIR, 'global', 'navigation.json');
const footerPath = path.join(CONTENT_DIR, 'global', 'footer.json');
const navigation = JSON.parse(fs.readFileSync(navigationPath, 'utf8'));
const footer = JSON.parse(fs.readFileSync(footerPath, 'utf8'));

// Build pages
const pagesDir = path.join(CONTENT_DIR, 'pages');
const pageFiles = fs.readdirSync(pagesDir).filter(f => f.endsWith('.json'));

pageFiles.forEach(file => {
  const pageName = file.replace('.json', '');
  const pagePath = path.join(pagesDir, file);
  const pageData = JSON.parse(fs.readFileSync(pagePath, 'utf8'));

  // Combine page data with global content
  const templateData = {
    ...pageData,
    navigation,
    footer
  };

  // Render page body
  const bodyHTML = landingPage(templateData);

  // Render into base layout
  const finalHTML = baseLayout({
    ...templateData,
    body: bodyHTML
  });

  // Write to dist
  const outputPath = path.join(BUILD_DIR, `${pageName}.html`);
  fs.writeFileSync(outputPath, finalHTML, 'utf8');

  console.log(`✅ Built ${pageName}.html`);
});

// Copy CSS to dist
const distCssDir = path.join(BUILD_DIR, 'css');
if (!fs.existsSync(distCssDir)) {
  fs.mkdirSync(distCssDir, { recursive: true });
}

const cssFiles = fs.readdirSync(CSS_DIR);
cssFiles.forEach(file => {
  const srcPath = path.join(CSS_DIR, file);
  const destPath = path.join(distCssDir, file);
  fs.copyFileSync(srcPath, destPath);
});

console.log(`✅ Copied ${cssFiles.length} CSS files`);

console.log('\n✨ Build complete!');
```

**Step 4: Test build**

```bash
npm run build
```

Expected output:
```
Loaded 3 schemas
✅ experience-agencies.json is valid
✅ All content validated successfully
Registered 6 component partials
✅ Built experience-agencies.html
✅ Copied 4 CSS files
✨ Build complete!
```

**Step 5: Verify generated HTML**

```bash
head -40 dist/experience-agencies.html
```

Expected: Valid HTML with navigation, hero, benefits, etc.

**Step 6: Commit build system**

```bash
git add templates/ src/build.js
git commit -m "feat: implement template compilation and build system

- Create base layout and landing page templates
- Update build.js to compile Handlebars templates
- Register component partials
- Copy CSS files to dist
- Generate experience-agencies.html from JSON content"
```

---

## Task 6: Create Development Server with Live Reload

**Files:**
- Create: `src/dev-server.js`
- Modify: `package.json`

**Step 1: Create dev server**

Create: `src/dev-server.js`

```javascript
const chokidar = require('chokidar');
const browserSync = require('browser-sync').create();
const { execSync } = require('child_process');
const path = require('path');

console.log('🚀 Starting development server...\n');

// Initial build
try {
  console.log('📦 Running initial build...');
  execSync('npm run build', { stdio: 'inherit' });
} catch (error) {
  console.error('❌ Initial build failed');
  process.exit(1);
}

// Start BrowserSync
browserSync.init({
  server: {
    baseDir: 'dist',
    serveStaticOptions: {
      extensions: ['html']
    }
  },
  port: 3000,
  open: true,
  notify: false
});

console.log('\n✅ Development server running at http://localhost:3000\n');

// Watch for changes
const watcher = chokidar.watch([
  'content/**/*.json',
  'templates/**/*.hbs',
  'css/**/*.css',
  'src/build.js'
], {
  ignored: /(^|[\/\\])\../,
  persistent: true
});

watcher.on('change', (filePath) => {
  console.log(`\n📝 Changed: ${filePath}`);

  try {
    console.log('🔨 Rebuilding...');
    execSync('npm run build', { stdio: 'inherit' });
    console.log('♻️  Reloading browser...');
    browserSync.reload();
  } catch (error) {
    console.error('❌ Build failed - fix errors and save to retry');
  }
});

console.log('👀 Watching for changes...');
console.log('   - content/**/*.json');
console.log('   - templates/**/*.hbs');
console.log('   - css/**/*.css');
console.log('\nPress Ctrl+C to stop\n');
```

**Step 2: Test dev server**

```bash
npm run dev
```

Expected: Browser opens to http://localhost:3000/experience-agencies

**Step 3: Test live reload**

Edit: `content/pages/experience-agencies.json`

Change hero title to: "Power immersive experiences ANYWHERE"

Expected:
- Console shows "Changed: content/pages/experience-agencies.json"
- Console shows "Rebuilding..."
- Browser auto-reloads with updated title

**Step 4: Revert test change**

Restore original hero title in `content/pages/experience-agencies.json`

**Step 5: Stop dev server**

Press Ctrl+C

**Step 6: Commit dev server**

```bash
git add src/dev-server.js package.json
git commit -m "feat: add development server with live reload

- Create dev-server.js with chokidar and browser-sync
- Watch content, templates, and CSS for changes
- Auto-rebuild and reload browser on file changes
- Improve developer iteration speed dramatically"
```

---

## Task 7: Migrate Remaining Landing Pages

**Files:**
- Create: `content/pages/street-festivals.json`
- Create: `content/pages/public-venues.json`
- Create: `content/pages/location-managers.json`
- Create: `content/pages/production-managers.json`
- Create: `content/pages/gaffers.json`
- Create: `content/pages/city-services.json`

**Step 1: Extract street-festivals content**

Read current HTML: `street-festivals.html`

Create: `content/pages/street-festivals.json`

```json
{
  "meta": {
    "title": "LAB SEVEN for Street Festivals | Labrador Field Systems",
    "description": "Silent, scalable battery power for street festivals. No noise complaints, no fuel trucks, no permit battles."
  },
  "hero": {
    "title": "Silent power for street festivals",
    "tagline": "No generator noise complaints. No fuel trucks during the event. No permit battles. Scale from one battery to twenty. Keep the neighborhood happy and your event on track.",
    "cta": {
      "primary": {
        "text": "Contact Labrador",
        "href": "#contact"
      },
      "secondary": {
        "text": "See Pricing",
        "href": "#pricing"
      }
    }
  },
  "benefits": {
    "title": "Built for outdoor festivals",
    "items": [
      {
        "icon": "🔇",
        "title": "Zero noise complaints",
        "description": "Battery power means silent operation. Neighbors stay happy, city permits stay valid, and your festival runs without generator drama."
      },
      {
        "icon": "⚡",
        "title": "Scalable power",
        "description": "Start with one battery for a vendor booth. Scale to twenty for multiple stages. Add or remove units as your festival grows or changes."
      },
      {
        "icon": "🚫",
        "title": "No fuel logistics",
        "description": "No fuel trucks navigating through crowds. No refueling during peak attendance. No fuel spill cleanup. Charge overnight, run all day."
      }
    ]
  }
}
```

**Note:** For remaining pages, follow the same pattern:
1. Read existing HTML
2. Extract meta, hero, benefits, problem, solution sections
3. Create JSON file in `content/pages/`
4. Validate with `npm run validate`

**Step 2: Extract remaining pages (abbreviated for brevity)**

Create these files following the same JSON structure:
- `content/pages/public-venues.json`
- `content/pages/location-managers.json`
- `content/pages/production-managers.json`
- `content/pages/gaffers.json`
- `content/pages/city-services.json`

**Step 3: Validate all content**

```bash
npm run validate
```

Expected output:
```
Loaded 3 schemas
✅ experience-agencies.json is valid
✅ street-festivals.json is valid
✅ public-venues.json is valid
✅ location-managers.json is valid
✅ production-managers.json is valid
✅ gaffers.json is valid
✅ city-services.json is valid
✅ All content validated successfully
```

**Step 4: Build all pages**

```bash
npm run build
```

Expected: 7 HTML files in `dist/`

**Step 5: Commit migrated content**

```bash
git add content/pages/
git commit -m "feat: migrate all landing pages to JSON content

- Extract street-festivals, public-venues, location-managers content
- Extract production-managers, gaffers, city-services content
- All pages validate against schemas
- Build generates 7 landing pages from JSON"
```

---

## Task 8: Update Netlify Configuration

**Files:**
- Modify: `netlify.toml` (in repo root)
- Create: `.nvmrc`

**Step 1: Create .nvmrc for Node version**

Create: `.nvmrc`

```
18
```

**Step 2: Update netlify.toml**

Modify: `netlify.toml` (in repo root, not in lab/)

```toml
[build]
  base = "lab"
  publish = "dist"
  command = "npm ci && npm run build"

[build.environment]
  NODE_VERSION = "18"

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-Content-Type-Options = "nosniff"
    X-XSS-Protection = "1; mode=block"
    Referrer-Policy = "strict-origin-when-cross-origin"

[[headers]]
  for = "/*.html"
  [headers.values]
    Cache-Control = "public, max-age=3600"

[[headers]]
  for = "/css/*.css"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"

[[headers]]
  for = "/js/*.js"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"

[[redirects]]
  from = "/editable"
  to = "/lab-seven-battery-editable.html"
  status = 200

[[redirects]]
  from = "/static"
  to = "/lab-seven-battery.html"
  status = 200

[[redirects]]
  from = "/macbook"
  to = "/macbook-air-replica.html"
  status = 200

# User-type landing pages
[[redirects]]
  from = "/experience-agencies"
  to = "/experience-agencies.html"
  status = 200

[[redirects]]
  from = "/street-festivals"
  to = "/street-festivals.html"
  status = 200

[[redirects]]
  from = "/public-venues"
  to = "/public-venues.html"
  status = 200

[[redirects]]
  from = "/location-managers"
  to = "/location-managers.html"
  status = 200

[[redirects]]
  from = "/production-managers"
  to = "/production-managers.html"
  status = 200

[[redirects]]
  from = "/gaffers"
  to = "/gaffers.html"
  status = 200

[[redirects]]
  from = "/city-services"
  to = "/city-services.html"
  status = 200
```

**Step 3: Test build locally**

```bash
cd /Users/amitrunchal/apps/labrador/lab/lab
rm -rf node_modules package-lock.json
npm ci
npm run build
```

Expected: Clean build with all pages generated

**Step 4: Commit Netlify configuration**

```bash
git add netlify.toml .nvmrc
git commit -m "feat: update Netlify config for build system

- Change publish directory from . to dist
- Add build command: npm ci && npm run build
- Set Node version to 18
- Update CSS path in headers to /css/*.css"
```

---

## Task 9: Add Content Editing Documentation

**Files:**
- Create: `docs/CONTENT_EDITING.md`
- Modify: `README.md`

**Step 1: Create content editing guide**

Create: `docs/CONTENT_EDITING.md`

```markdown
# Content Editing Guide

## Overview

All website content lives in JSON files in the `content/` directory. Edit these files to update the website - no HTML knowledge required.

## Content Structure

```
content/
├── pages/              # Individual page content
│   ├── index.json
│   ├── experience-agencies.json
│   └── ...
├── global/            # Shared across all pages
│   ├── navigation.json
│   └── footer.json
└── schemas/           # Content validation rules
```

## Editing Page Content

### 1. Find Your Page

Open the appropriate JSON file in `content/pages/`:
- Homepage: `index.json`
- Experience Agencies: `experience-agencies.json`
- Street Festivals: `street-festivals.json`
- etc.

### 2. Edit Content

Each page has these sections:

**Meta (SEO):**
```json
"meta": {
  "title": "Page Title | Labrador Field Systems",
  "description": "Page description for search engines"
}
```

**Hero Section:**
```json
"hero": {
  "title": "Main headline",
  "tagline": "Supporting text that explains your value proposition",
  "cta": {
    "primary": { "text": "Primary Button", "href": "#section" },
    "secondary": { "text": "Secondary Button", "href": "#section" }
  }
}
```

**Benefits:**
```json
"benefits": {
  "title": "Section headline",
  "items": [
    {
      "icon": "✓",
      "title": "Benefit title",
      "description": "Benefit description"
    }
  ]
}
```

### 3. Validate Changes

Before deploying, validate your content:

```bash
npm run validate
```

If validation fails, the error message will tell you exactly what's wrong.

### 4. Preview Changes

Start the dev server to see your changes:

```bash
npm run dev
```

Browser opens to http://localhost:3000. Changes auto-reload.

### 5. Deploy

Commit and push to GitHub:

```bash
git add content/pages/your-file.json
git commit -m "Update content for X page"
git push origin main
```

Netlify auto-deploys in ~2 minutes.

## Content Rules

### Text Length Limits

- **Title:** 10-70 characters (for SEO)
- **Description:** 50-160 characters (for SEO)
- **Hero Title:** 10-100 characters
- **Hero Tagline:** 20-300 characters
- **Benefit Title:** 5-80 characters
- **Benefit Description:** 20-300 characters

### Icons

Use emoji or text icons:
- ✓ (checkmark)
- ⚡ (lightning)
- 🎯 (target)
- 🔇 (mute)
- Any emoji that supports your message

## Global Content

### Navigation

Edit `content/global/navigation.json`:

```json
{
  "logo": "LABRADOR",
  "links": [
    { "text": "Home", "href": "index.html" },
    { "text": "Benefits", "href": "#benefits" }
  ]
}
```

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

## Common Tasks

### Add a New Benefit

In your page JSON:

```json
"benefits": {
  "items": [
    // ... existing benefits
    {
      "icon": "🚀",
      "title": "Your new benefit",
      "description": "Description of the benefit"
    }
  ]
}
```

### Update Hero CTA

```json
"hero": {
  "cta": {
    "primary": {
      "text": "New Button Text",
      "href": "#new-section"
    }
  }
}
```

### Change Navigation Links

Edit `content/global/navigation.json` to add/remove/reorder nav items.

## Getting Help

If validation fails, read the error message carefully. It tells you:
- Which file has the error
- Which field is invalid
- What the expected format is

Common errors:
- Text too long/short
- Missing required field
- Invalid link format
```

**Step 2: Update README.md**

Modify: `README.md`

Add section at the top:

```markdown
# LAB SEVEN Website

## Quick Start

### For Content Editors

See [Content Editing Guide](docs/CONTENT_EDITING.md) - update website content without touching code.

### For Developers

**Setup:**
```bash
npm install
```

**Development:**
```bash
npm run dev  # Start dev server with live reload
```

**Build:**
```bash
npm run build  # Build site to dist/
```

**Validate:**
```bash
npm run validate  # Check content against schemas
```

## Architecture

Content-driven static site:
- **Content:** JSON files in `content/`
- **Templates:** Handlebars in `templates/`
- **Styles:** Modular CSS in `css/`
- **Build:** Node.js compiles templates + content → static HTML
- **Deploy:** Netlify builds and hosts

See [Architecture Plan](docs/plans/2025-11-15-robust-site-architecture.md) for details.

---

[Rest of existing README content...]
```

**Step 3: Commit documentation**

```bash
git add docs/CONTENT_EDITING.md README.md
git commit -m "docs: add content editing guide and update README

- Create comprehensive content editing guide for non-technical users
- Explain JSON structure, validation, and deployment workflow
- Update README with quick start for editors and developers
- Reference architecture plan"
```

---

## Task 10: Clean Up Legacy Files

**Files:**
- Delete: Old HTML files with embedded CSS
- Create: `docs/MIGRATION.md`

**Step 1: Identify legacy files**

```bash
ls -la *.html
```

Legacy files (not migrated to build system):
- `lab-seven-battery.html` (1603 lines, embedded CSS)
- `lab-seven-battery-editable.html` (777 lines, embedded CSS)
- `lab-seven-premium.html` (1108 lines, embedded CSS)
- `lab-seven-stripe-style.html` (1007 lines, embedded CSS)
- `macbook-air-replica.html` (788 lines, reference design)
- `color-lookbook.html` (882 lines, reference design)
- `test.html` (515 lines, test file)

**Step 2: Create migration tracking doc**

Create: `docs/MIGRATION.md`

```markdown
# Migration Status

## Completed (Build System)

✅ **Landing Pages** (7 total)
- experience-agencies.html
- street-festivals.html
- public-venues.html
- location-managers.html
- production-managers.html
- gaffers.html
- city-services.html

**Status:** Using JSON content + Handlebars templates

## Legacy Files (To Migrate)

### Priority 1: Core Product Pages

- [ ] `index.html` (412 lines) - Homepage, uses shared CSS
- [ ] `lab-seven-battery.html` (1603 lines) - Full product page
- [ ] `lab-seven-battery-editable.html` (777 lines) - Editable version

### Priority 2: Alternative Designs

- [ ] `lab-seven-premium.html` (1108 lines) - Premium variant
- [ ] `lab-seven-stripe-style.html` (1007 lines) - Stripe-style variant

### Reference/Archive

- `macbook-air-replica.html` (788 lines) - Design reference
- `color-lookbook.html` (882 lines) - Color reference
- `test.html` (515 lines) - Test file

## Migration Process

For each legacy file:

1. Extract content to `content/pages/<name>.json`
2. Create/update template in `templates/pages/<name>.hbs`
3. Add page-specific CSS if needed
4. Validate content: `npm run validate`
5. Build and test: `npm run build && npm run dev`
6. Update this doc
7. Archive original HTML to `archive/` folder

## Notes

- Keep original HTML files until migration complete and tested
- Update Netlify redirects if URLs change
- Test all pages on deployed site before deleting originals
```

**Step 3: Create archive folder**

```bash
mkdir -p archive
```

**Step 4: Move reference files to archive**

```bash
git mv macbook-air-replica.html archive/
git mv color-lookbook.html archive/
git mv test.html archive/
```

**Step 5: Update .gitignore**

Modify: `.gitignore`

```gitignore
node_modules/
dist/
.DS_Store
*.log
.env

# Keep archive tracked but mark as legacy
# archive/
```

**Step 6: Commit cleanup**

```bash
git add docs/MIGRATION.md archive/ .gitignore
git commit -m "chore: organize legacy files and create migration tracker

- Move reference designs to archive/
- Create migration status document
- Track which files use build system vs legacy approach
- Document migration process for remaining pages"
```

---

## Summary & Next Steps

### What We Built

✅ **Build System**
- Node.js build process with Handlebars templates
- JSON content validation with schemas
- Development server with live reload
- Netlify deployment configuration

✅ **Content Management**
- All landing pages (7) migrated to JSON
- Validation ensures content quality
- Non-developers can edit content safely

✅ **Developer Experience**
- `npm run dev` - instant feedback on changes
- `npm run validate` - catch errors before deploy
- `npm run build` - production build

✅ **Documentation**
- Content editing guide for non-technical users
- Architecture documentation
- Migration tracking

### Iteration Speed Improvements

**Before:**
1. Edit HTML directly (risk of breaking structure)
2. Test locally by opening HTML file
3. Commit and push
4. Wait for Netlify deploy
5. Hope nothing broke

**After:**
1. Edit JSON content (validated structure)
2. Save file → browser auto-reloads
3. Commit and push
4. Automated build and deploy
5. Schema validation prevents errors

**Time to make content change:**
- Before: 10-15 minutes
- After: 2-3 minutes

### Remaining Work

**Priority 1: Migrate Homepage**
- Extract `index.html` content to JSON
- Create homepage template (more complex than landing pages)
- Handle homepage-specific components

**Priority 2: Migrate Core Product Pages**
- `lab-seven-battery.html` - main product page
- `lab-seven-battery-editable.html` - editable version

**Priority 3: Optimization**
- CSS optimization with PostCSS
- Image optimization pipeline
- Performance testing

**Priority 4: Advanced Features**
- Multi-language support (i18n)
- A/B testing capability
- Analytics integration

### How to Use This Architecture

**Adding a new landing page:**

1. Create `content/pages/new-page.json`
2. Use existing JSON structure
3. Run `npm run validate`
4. Run `npm run build`
5. Add redirect to `netlify.toml`
6. Done - page is live

**Updating content:**

1. Edit JSON file in `content/pages/`
2. Save (dev server auto-reloads)
3. Review in browser
4. Commit and push
5. Netlify auto-deploys

**Adding a new component:**

1. Create `templates/components/new-component.hbs`
2. Add to page template
3. Update content schema if needed
4. Component reusable across all pages

This architecture supports rapid iteration while maintaining quality through validation, automation, and clear separation of concerns.
