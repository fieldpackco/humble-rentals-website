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

console.log('Build system initialized');
console.log(`Templates: ${TEMPLATES_DIR}`);
console.log(`Content: ${CONTENT_DIR}`);
console.log(`Output: ${BUILD_DIR}`);

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
