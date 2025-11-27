# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 📋 Session Management

**IMPORTANT**: Before starting any work, review these files:
- `TODO.md` - Current task list and priorities
- `history.md` - Complete session history and context

These files track project progress and provide essential context for maintaining continuity across sessions.

## Project Overview

This repository contains premium marketing website prototypes, specifically focused on creating Apple-style product showcase websites. The primary project is the Citypack battery solutions website, built as a sophisticated multi-page application with integrated content management system.

### Latest Development (November 27, 2025)
Complete rebrand from LAB SEVEN/Labrador to Citypack. The project now focuses on delivering diverse battery solutions tailored to customer needs, rather than a specific product. The content-driven architecture with JSON management and Handlebars templating provides flexible content updates.

## Architecture

### Design System
The codebase implements a premium design system with:

- **CSS Custom Properties**: Centralized color palette using CSS variables in `:root`
  - Primary brand colors: `--primary-orange` (#FF6B35) to `--accent-gold` (#F4B942)
  - Semantic color tokens for text, backgrounds, and borders
  - Gradient definitions: `--gradient-primary` and `--gradient-secondary`

- **Typography Scale**: Systematic font sizing from 12px to 112px with precise letter-spacing
  - Font stack: Inter/Poppins with system fallbacks
  - Weight scale: 400, 500, 600, 700, 800

- **Spacing System**: Consistent 140px section padding with proportional margins
  - Card padding: 40-60px
  - Icon sizing: 96px, 120px, 140px scale

### Component Architecture

**Navigation**: Fixed glassmorphism header with:
- Backdrop blur effects
- Scroll-triggered background changes
- Hover animations with gradient underlining

**Hero Section**: Large-scale typography with:
- 96px headlines with gradient text treatments
- Staggered animation system
- Parallax product imagery

**Feature Blocks**: Split-screen layout pattern:
- Content/visual pairs with reversible direction
- Large statistic displays (112px font-weight 800)
- Glassmorphism visual containers

**Interactive Elements**:
- Custom button system with shimmer animations
- Hover effects using `transform: translateY()` and box-shadows
- Card lift interactions with gradient border highlights

### Animation System

- **Intersection Observer**: Scroll-triggered animations with staggered delays
- **Cubic Bezier Easing**: `cubic-bezier(0.4, 0, 0.2, 1)` for premium feel
- **Hover States**: Multi-property transitions (transform, box-shadow, background)
- **Loading Animations**: Progressive revelation with 150ms delays

## Development Workflow

### Testing
Development server with live reload:
```bash
# Start development server
npm run dev

# Build for production
npm run build

# Validate content
npm run validate
```

### Content Management
The site uses a content-driven architecture:
- Edit JSON files in `content/pages/` for page content
- Edit JSON files in `content/global/` for shared content
- Changes validate against JSON schemas
- Build system compiles templates with content
- Safe editing with validation before deployment

### Structure
- Single-file applications with embedded CSS and JavaScript
- Self-contained with no external dependencies
- Responsive design with mobile-first breakpoints at 768px, 1024px

### Code Organization
CSS follows this order:
1. CSS Custom Properties (`:root`)
2. Base styles and resets  
3. Component styles (navigation → hero → content sections → footer)
4. Responsive media queries
5. Animation keyframes

JavaScript features:
- Intersection Observer for scroll animations
- Smooth scroll polyfill
- Enhanced hover effects
- Parallax scrolling implementation
- **Content Management System**: Real-time content editing with localStorage persistence
- **Template Engine**: Dynamic HTML updates via `siteContent` configuration object

## Key Files

- `README.md`: Complete project overview, features, and usage guide
- `content/`: JSON content files (pages and global shared content)
- `templates/`: Handlebars templates (components and page layouts)
- `css/`: Modular stylesheets with design system
- `docs/CONTENT_EDITING.md`: Content editing guide
- `TODO.md`: Project task tracking and priority management
- `history.md`: Complete session documentation and request/response log
- `CLAUDE.md`: This technical documentation file
- `legacy/`: Archived files from previous iterations

## Design Principles

The codebase follows premium web design patterns:
- High contrast typography (800 font-weight headlines)
- Generous whitespace with 140px section padding
- Sophisticated color gradients avoiding flat colors
- Micro-interactions on all interactive elements
- Glassmorphism effects with backdrop-filter
- Professional animation timing (0.3-0.4s transitions)

Content structure maintains Apple-style information hierarchy while establishing unique brand identity through color, typography, and interaction design.