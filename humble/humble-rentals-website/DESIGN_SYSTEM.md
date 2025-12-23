# Citypack Design System

A scalable, modular CSS architecture for the Citypack website, designed to support growth similar to Apple or Stripe with many subpages and categories.

## Architecture

The design system is split into three CSS files for maintainability and scalability:

### 1. `css/design-system.css` (329 lines)
**Core design tokens and base styles**
- CSS custom properties (color palette, typography scale, spacing, shadows)
- Typography system (display, heading, body text classes)
- Base animations (fadeIn, slideIn, pulse)
- Responsive breakpoints

### 2. `css/components.css` (452 lines)
**Reusable UI components**
- Navigation (fixed header with glassmorphism)
- Buttons (primary, secondary, sizes)
- Cards (standard, glass, feature cards)
- Lists, stats, badges, links
- Forms
- Quotes and testimonials

### 3. `css/layouts.css` (486 lines)
**Page layout patterns**
- Containers (content, wide, reading)
- Sections (standard, compact, hero)
- Grid systems (2, 3, 4 columns, auto-fit)
- Feature blocks (split-screen layouts)
- Comparison sections
- Footer

## Creating a New Page

### Basic Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Title | Citypack</title>
    <meta name="description" content="Your page description">

    <!-- Shared Design System -->
    <link rel="stylesheet" href="css/design-system.css">
    <link rel="stylesheet" href="css/components.css">
    <link rel="stylesheet" href="css/layouts.css">
</head>
<body>
    <!-- Navigation -->
    <nav>
        <div class="nav-wrapper">
            <div class="logo">CITYPACK</div>
            <ul class="nav-items">
                <li><a href="index.html">Home</a></li>
                <li><a href="#benefits">Benefits</a></li>
                <li><a href="#solution">Solution</a></li>
            </ul>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero">
        <h1 class="animate-in">Your headline here</h1>
        <p class="tagline animate-in">Your tagline here</p>
        <div class="cta-buttons animate-in">
            <a href="#contact" class="btn btn-primary">Primary CTA</a>
            <a href="#contact" class="btn btn-secondary">Secondary CTA</a>
        </div>
    </section>

    <!-- Your content sections here -->

    <!-- Footer -->
    <footer>
        <p>&copy; 2025 Citypack. All rights reserved.</p>
        <p><a href="index.html">Return to main site</a></p>
    </footer>

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
            nav.classList.toggle('scrolled', window.scrollY > 10);
        });

        // Animate on scroll
        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.animation = 'fadeIn 0.8s cubic-bezier(0.4, 0, 0.2, 1) forwards';
                }
            });
        }, { threshold: 0.15, rootMargin: '0px 0px -80px 0px' });

        document.querySelectorAll('.animate-in').forEach(el => observer.observe(el));
    </script>
</body>
</html>
```

## Common Patterns

### Benefits Grid
```html
<section class="benefits" id="benefits">
    <h2>Built for experiential marketing</h2>
    <div class="benefits-grid">
        <div class="benefit-card animate-in">
            <div class="benefit-icon">✓</div>
            <h3>Benefit headline</h3>
            <p>Benefit description</p>
        </div>
        <!-- More benefit cards -->
    </div>
</section>
```

### Problem/Solution Section
```html
<section class="problem" id="problem">
    <h2>What [audience] deal with today</h2>
    <p class="intro">Problem summary</p>
    <div class="problem-grid">
        <div class="problem-item">
            <h3>Problem headline</h3>
            <p>Problem description</p>
        </div>
        <!-- More problem items -->
    </div>
</section>
```

### Feature Specs
```html
<div class="quick-specs">
    <h3>Power for full activations</h3>
    <div class="specs-list">
        <div class="spec-item">
            <span class="spec-value">10kW</span>
            <span class="spec-label">Continuous output</span>
        </div>
        <!-- More spec items -->
    </div>
</div>
```

### Journey Comparison
```html
<section class="journey" id="journey">
    <h2>A day on activation</h2>
    <div class="journey-comparison">
        <div class="journey-column without">
            <h3>Without Citypack</h3>
            <p>Negative scenario description</p>
        </div>
        <div class="journey-column with">
            <h3>With Citypack</h3>
            <p>Positive scenario description</p>
        </div>
    </div>
</section>
```

## Design Tokens Reference

### Colors
- **Primary**: `--primary-orange` (#FF6B35), `--accent-gold` (#F4B942)
- **Neutral**: `--neutral-charcoal` (#2C3E50), `--neutral-light` (#F8F9FA)
- **Text**: `--text-primary` (#0d1117), `--text-secondary` (#656d76)

### Typography Scale
- Display: `--font-size-96`, `--font-size-56`, `--font-size-48`
- Headings: `--font-size-32`, `--font-size-28`, `--font-size-24`, `--font-size-20`
- Body: `--font-size-18`, `--font-size-16`, `--font-size-14`

### Spacing Scale (8px base)
- `--space-8`, `--space-16`, `--space-20`, `--space-24`, `--space-32`
- `--space-40`, `--space-48`, `--space-60`, `--space-80`
- `--space-100`, `--space-120`, `--space-140`

### Border Radius
- `--radius-sm` (8px), `--radius-md` (12px), `--radius-lg` (18px)
- `--radius-xl` (20px), `--radius-2xl` (24px)

## Customization

### Changing Brand Colors
Edit `css/design-system.css` and update the color variables in `:root`:
```css
:root {
    --primary-orange: #FF6B35;  /* Your new primary color */
    --accent-gold: #F4B942;     /* Your new accent color */
}
```
All components will automatically use the new colors.

### Adding New Components
Add new component styles to `css/components.css`:
```css
/* ============================================
   YOUR NEW COMPONENT
   ============================================ */

.your-component {
    padding: var(--space-40);
    background: var(--white);
    border-radius: var(--radius-lg);
}
```

### Responsive Breakpoints
The system uses three breakpoints:
- **1024px**: Tablet landscape (grids reduce columns)
- **768px**: Tablet portrait (grids collapse to single column)
- **480px**: Mobile (reduced spacing and font sizes)

## Best Practices

1. **Use design tokens**: Always use CSS variables instead of hardcoded values
   ```css
   /* Good */
   padding: var(--space-40);
   color: var(--primary-orange);

   /* Bad */
   padding: 40px;
   color: #FF6B35;
   ```

2. **Add `animate-in` class**: Add to elements you want to fade in on scroll
   ```html
   <div class="benefit-card animate-in">
   ```

3. **Use semantic class names**: Choose classes that describe purpose, not appearance
   ```html
   <!-- Good -->
   <div class="benefit-card">

   <!-- Bad -->
   <div class="orange-box-with-shadow">
   ```

4. **Follow section structure**: Use consistent section patterns across pages
   ```html
   <section class="section-name" id="section-id">
       <h2>Section title</h2>
       <div class="content-grid">
           <!-- Content -->
       </div>
   </section>
   ```

5. **Test responsively**: Always check your page at 768px and 480px widths

## Migration Summary

All 8 pages have been migrated to the shared design system:

| Page | Before | After | Savings |
|------|--------|-------|---------|
| index.html | 1,609 lines | 461 lines | 1,148 lines |
| experience-agencies.html | 862 lines | 247 lines | 615 lines |
| public-venues.html | 862 lines | 247 lines | 615 lines |
| location-managers.html | 862 lines | 247 lines | 615 lines |
| production-managers.html | 862 lines | 247 lines | 615 lines |
| gaffers.html | 862 lines | 247 lines | 615 lines |
| city-services.html | 862 lines | 247 lines | 615 lines |
| street-festivals.html | 256 lines | 186 lines | 70 lines |

**Total reduction**: ~4,900 lines of CSS eliminated by using the shared design system.

## Adding Clean URLs

To add a clean URL for your new page, update `netlify.toml`:

```toml
[[redirects]]
  from = "/your-page-name"
  to = "/your-page-name.html"
  status = 200
```

This allows users to access `labradorfieldystems.com/your-page-name` instead of requiring the `.html` extension.
