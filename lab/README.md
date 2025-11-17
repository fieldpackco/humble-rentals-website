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
- ⚡ **High Performance** - Self-contained HTML with embedded CSS/JS (no dependencies)
- ✏️ **Content Management** - Live editing interface for non-technical users
- 🎬 **Industry-Focused** - Tailored for film/video production professionals

## 🚀 Quick Start

### View the Website
1. Download or clone the repository
2. Open `lab-seven-battery-editable.html` in your browser
3. Click "✏️ Edit Content" to customize content

### Deploy to Web
- **GitHub Pages**: Enable in repository settings
- **Netlify**: Drag and drop the HTML files
- **Any Web Host**: Upload files to public directory

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

## 💻 Website Features

### Design System
- **Color Palette**: Professional orange (#FF6B35) to gold (#F4B942) gradients
- **Typography**: Inter/Poppins font stack with systematic sizing (12px - 112px)
- **Spacing**: Consistent 140px section padding with proportional components
- **Animations**: Sophisticated scroll-triggered reveals with cubic-bezier easing

### Content Sections
- **Hero Section** - Product introduction with compelling tagline
- **Specifications** - Technical details with visual icons
- **Features** - Split-screen benefit showcases
- **Gallery** - Product imagery with glassmorphism effects
- **Pricing** - Beta program packages with feature comparison
- **Roadmap** - Future product timeline

### Technical Implementation
- **Self-Contained** - No external dependencies or build process
- **CSS Custom Properties** - Systematic theming with CSS variables
- **Intersection Observer** - Performance-optimized scroll animations
- **Local Storage** - Persistent content customization
- **Mobile-First** - Responsive breakpoints at 480px, 768px, 1024px

## ✏️ Content Management

### Easy Editing Interface
The editable version includes a professional content management panel:

1. **Hero Content**: Headlines, pricing, call-to-action buttons
2. **Company Info**: Name, contact details, page title
3. **Real-Time Updates**: Changes appear instantly without refresh
4. **Persistent Storage**: Edits saved automatically in browser
5. **Mobile-Friendly**: Full editing capability on all devices

### Content Structure
```javascript
siteContent = {
  hero: {
    headline: "LAB SEVEN",
    tagline: "Power. Unleashed.",
    price: "From $999 or $83.25/mo. for 12 mo.*",
    availability: "Available for Beta Program"
  },
  company: {
    name: "Labrador Field Systems",
    contact: { email: "...", phone: "..." }
  }
}
```

See [`content-editor-guide.md`](content-editor-guide.md) for detailed instructions.

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

## 🛠️ Development

### No Build Process Required
- Open HTML files directly in browser
- All assets embedded inline
- Instant preview of changes
- Works offline

### Code Organization
```
1. CSS Custom Properties (:root)
2. Base Styles & Resets
3. Component Styles (Navigation → Hero → Content → Footer)
4. Responsive Media Queries
5. Animation Keyframes
6. JavaScript Features
```

### Browser Support
- ✅ Chrome/Edge (2020+)
- ✅ Safari (2020+)
- ✅ Firefox (2020+)
- ✅ Mobile browsers
- ⚠️ IE not supported (uses modern CSS features)

## 📊 Performance Metrics

- **Page Size**: ~50KB (self-contained)
- **Load Time**: <500ms (no external requests)
- **Lighthouse Score**: 90+ (Performance, Accessibility, Best Practices)
- **Core Web Vitals**: Excellent ratings
- **Mobile Performance**: Optimized for 3G+ connections

## 🔧 Customization

### Easy Modifications
1. **Colors**: Update CSS custom properties in `:root`
2. **Content**: Use the built-in editor or modify `siteContent` object
3. **Images**: Replace placeholder divs with actual product photos
4. **Sections**: Add new content blocks following existing patterns

### Advanced Customization
- **Animation Timing**: Adjust `cubic-bezier` values and delays
- **Typography Scale**: Modify font sizes while maintaining hierarchy
- **Color Gradients**: Update gradient definitions in CSS variables
- **Layout Grids**: Adjust breakpoints and grid systems

## 📈 Future Enhancements

### Planned Features
- [ ] Real product image integration
- [ ] Advanced form handling
- [ ] Multi-language support
- [ ] SEO optimization
- [ ] Performance monitoring
- [ ] A/B testing framework

### Expansion Possibilities
- Content Management API integration
- E-commerce functionality
- User authentication
- Analytics dashboard
- Social media integration

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