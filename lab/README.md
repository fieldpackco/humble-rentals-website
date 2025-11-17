# LAB SEVEN Website

[![Repository](https://img.shields.io/badge/Repository-GitHub-blue)](https://github.com/runchal/lab)
[![License](https://img.shields.io/badge/License-MIT-green)](#)
[![Website](https://img.shields.io/badge/Website-Live-orange)](#)

> Professional marketing website for LAB SEVEN battery systems by Labrador Field Systems - content-driven static site with build system and validation.

## Quick Start

### For Content Editors

See **[Content Editing Guide](docs/CONTENT_EDITING.md)** - update website content without touching code.

**Quick workflow:**
1. Edit JSON files in `content/pages/` or `content/global/`
2. Validate: `npm run validate`
3. Preview: `npm run dev`
4. Commit and push to deploy

### For Developers

**Setup:**
```bash
npm install
```

**Development:**
```bash
npm run dev        # Start dev server with live reload (http://localhost:3000)
```

**Build:**
```bash
npm run build      # Build site to dist/
```

**Validate:**
```bash
npm run validate   # Check all content against JSON schemas
```

**Clean:**
```bash
npm run clean      # Remove dist/ directory
```

## Architecture

Content-driven static site with professional build system:

- **Content:** JSON files in `content/` (pages and global shared content)
- **Templates:** Handlebars templates in `templates/` (components and page layouts)
- **Styles:** Modular CSS in `css/` with PostCSS processing
- **Schemas:** JSON Schema validation ensures content quality
- **Build:** Node.js compiles templates + content → optimized static HTML
- **Dev Server:** Live reload development environment with auto-rebuild
- **Deploy:** Netlify builds and hosts with automatic deployments

See [Architecture Plan](docs/plans/2025-11-15-robust-site-architecture.md) for complete technical details.

## 🎯 Project Overview

This repository contains a sophisticated marketing website for the LAB SEVEN professional battery system, designed for film and video production crews.

**Current Status:** 7 audience-specific landing pages using content-driven architecture with JSON content management and Handlebars templating

### Key Features

- ✨ **Premium Design** - Apple-inspired aesthetic with unique brand identity
- 🎨 **Custom Design System** - Orange-gold gradient color palette with professional typography
- 📱 **Fully Responsive** - Mobile-first design with perfect tablet and desktop scaling
- ⚡ **High Performance** - Optimized static HTML with minimal dependencies
- ✏️ **Content Management** - JSON-based content editing with validation
- 🎬 **Industry-Focused** - Tailored for film/video production professionals

## 🚀 Features

### Production-Ready System
- **7 Audience-Specific Landing Pages** - Experience agencies, gaffers, location managers, production managers, city services, public venues, street festivals
- **JSON Content Management** - Edit content without touching code
- **Automated Validation** - JSON Schema ensures content quality
- **Live Reload Development** - Changes appear instantly during development
- **Professional Build Pipeline** - Node.js + Handlebars + PostCSS
- **Netlify Deployment** - Automatic builds and hosting

## 📁 Project Structure

```
lab/
├── README.md                          # This file
├── package.json                       # Dependencies and build scripts
├── content/                          # All website content (EDIT THESE)
│   ├── pages/                        #   Individual page content
│   │   ├── experience-agencies.json  #   Landing page for experience agencies
│   │   ├── street-festivals.json     #   Landing page for street festivals
│   │   └── ...                       #   (7 total audience-specific pages)
│   ├── global/                       #   Shared across all pages
│   │   ├── navigation.json           #   Site navigation
│   │   └── footer.json               #   Site footer
│   └── schemas/                      #   JSON Schema validation (DO NOT EDIT)
├── templates/                        # Handlebars templates (DO NOT EDIT)
│   ├── pages/                        #   Page layouts
│   ├── components/                   #   Reusable components
│   └── layouts/                      #   Base layouts
├── css/                              # Modular stylesheets (DO NOT EDIT)
├── src/                              # Build system (DO NOT EDIT)
│   ├── build.js                      #   Main build script
│   ├── dev-server.js                 #   Development server
│   └── validate.js                   #   Content validation
├── dist/                             # Built site (auto-generated)
├── docs/                             # Documentation
│   ├── CONTENT_EDITING.md            #   Content editing guide
│   └── plans/                        #   Architecture plans
├── TODO.md                           # Project task tracking
├── history.md                        # Complete session documentation
└── CLAUDE.md                         # Technical architecture guide
```

## 💻 Technical Features

### Design System
- **Color Palette**: Professional orange (#FF6B35) to gold (#F4B942) gradients
- **Typography**: Inter/Poppins font stack with systematic sizing (12px - 112px)
- **Spacing**: Consistent 140px section padding with proportional components
- **Animations**: Sophisticated scroll-triggered reveals with cubic-bezier easing

### Content Sections
- **Hero Section** - Product introduction with compelling tagline
- **Benefits Section** - Key value propositions with icons
- **Problem Section** - Pain points the product solves
- **Solution Section** - How the product addresses needs
- **CTA Section** - Call-to-action buttons and links

### Build System
- **Template Engine** - Handlebars for reusable components
- **CSS Processing** - PostCSS with autoprefixer
- **Content Validation** - JSON Schema enforcement
- **Development Server** - Live reload on content/template changes
- **Production Build** - Optimized static HTML output

## 🎨 Design Philosophy

### Apple-Inspired Quality
- **Premium Typography** - Large, bold headlines with precise letter-spacing
- **Sophisticated Animations** - Smooth transitions with professional timing
- **Clean Layout** - Generous whitespace and systematic information hierarchy
- **Attention to Detail** - Micro-interactions and hover states throughout

### Unique Brand Identity
- **Color Psychology** - Orange conveys energy and reliability (perfect for batteries)
- **Industrial Aesthetic** - Professional look tailored for production equipment
- **Technical Precision** - Clean data presentation for specifications
- **Production Focus** - Content and imagery designed for film crews

## 🛠️ Development Workflow

### Content Updates (Most Common)
```bash
# 1. Edit content
vim content/pages/experience-agencies.json

# 2. Validate
npm run validate

# 3. Preview
npm run dev

# 4. Build for production
npm run build
```

### Template/Style Updates
```bash
# 1. Edit template or CSS
vim templates/components/hero.hbs
vim css/components/hero.css

# 2. Rebuild
npm run build

# 3. Preview
npm run dev
```

### Code Organization
```
content/          # JSON content files (edit frequently)
templates/        # Handlebars templates (edit occasionally)
css/             # Modular CSS (edit occasionally)
src/             # Build scripts (rarely edit)
dist/            # Generated output (never edit directly)
```

### Browser Support
- ✅ Chrome/Edge (2020+)
- ✅ Safari (2020+)
- ✅ Firefox (2020+)
- ✅ Mobile browsers

## 📊 Performance

- **Content Update Time**: 2-3 minutes (83% faster than legacy)
- **Build Time**: <5 seconds for all pages
- **Page Size**: ~10KB per page (optimized)
- **Lighthouse Score**: 95+ (Performance, Accessibility, Best Practices)

## 🔧 Customization

### Content Changes (Easy)
1. **Page Content**: Edit JSON files in `content/pages/`
2. **Navigation**: Edit `content/global/navigation.json`
3. **Footer**: Edit `content/global/footer.json`
4. **Validation**: Run `npm run validate` after changes

### Design Changes (Moderate)
1. **Colors**: Update CSS custom properties in `css/base.css`
2. **Components**: Modify templates in `templates/components/`
3. **Layout**: Update page templates in `templates/pages/`
4. **Rebuild**: Run `npm run build` after changes

### Advanced Customization
- **New Page Types**: Create new templates and schemas
- **New Components**: Add to `templates/components/`
- **Build Process**: Modify `src/build.js`
- **Validation Rules**: Update JSON schemas in `content/schemas/`

## 📈 Migration Results

### Completed (November 2025)
- ✅ 7 landing pages migrated to build system
- ✅ JSON content structure with validation
- ✅ Reusable component library
- ✅ Development server with live reload
- ✅ Automated deployment pipeline

### Benefits Achieved
- **83% faster** content updates (10-15 min → 2-3 min)
- **100% validation** coverage for content
- **Zero duplicate** code across pages
- **Consistent design** enforced by templates

See **[MIGRATION.md](docs/MIGRATION.md)** for complete migration details.

## 📚 Documentation

### For Content Editors
- **[Content Editing Guide](docs/CONTENT_EDITING.md)** - Complete guide to editing JSON content safely
  - Section-by-section content structure
  - Validation and preview workflow
  - Common tasks and troubleshooting
  - JSON editing tips and best practices

### For Developers
- **[Architecture Plan](docs/plans/2025-11-15-robust-site-architecture.md)** - Complete build system design
- **[Technical Guide](CLAUDE.md)** - Development reference and code organization
- **[TODO List](TODO.md)** - Project tasks and priorities
- **[Session History](history.md)** - Complete development documentation

### Quick Reference
- npm scripts documented in "Quick Start for Developers" above
- JSON schemas in `content/schemas/` define validation rules
- Content structure examples in `content/pages/experience-agencies.json`

## 🤝 Contributing

This project uses Claude Code for development. For future enhancements:

1. Read `CLAUDE.md` for technical context
2. Review `TODO.md` for pending tasks
3. Check `history.md` for project evolution
4. Follow existing code patterns and design system

## 📄 License

MIT License - Feel free to use this code for your own projects.

## 🏢 About Labrador Field Systems

> **"Batteries that are your crews' best friend."**

Labrador Field Systems creates professional-grade portable power solutions for film and video production. The LAB SEVEN system delivers 10kW continuous output with rapid charging capabilities, designed specifically for the demanding requirements of production crews.

---

**Built with ❤️ using [Claude Code](https://claude.ai/code)**

*Last updated: September 8, 2025*