const fs = require('fs');
const path = require('path');
const Handlebars = require('handlebars');

const BUILD_DIR = path.join(__dirname, '..'); // Output to lab/ directory (site root)
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

// Register Handlebars helpers
Handlebars.registerHelper('add', function(a, b) {
  return a + b;
});

// Load base layout
const baseLayoutPath = path.join(TEMPLATES_DIR, 'layouts', 'base.hbs');
const baseLayoutTemplate = fs.readFileSync(baseLayoutPath, 'utf8');
const baseLayout = Handlebars.compile(baseLayoutTemplate);

// Load page templates
const landingPagePath = path.join(TEMPLATES_DIR, 'pages', 'landing-page.hbs');
const landingPageTemplate = fs.readFileSync(landingPagePath, 'utf8');
const landingPage = Handlebars.compile(landingPageTemplate);

const homePagePath = path.join(TEMPLATES_DIR, 'pages', 'home-page.hbs');
const homePageTemplate = fs.readFileSync(homePagePath, 'utf8');
const homePage = Handlebars.compile(homePageTemplate);

const specsPagePath = path.join(TEMPLATES_DIR, 'pages', 'specs-page.hbs');
const specsPageTemplate = fs.readFileSync(specsPagePath, 'utf8');
const specsPage = Handlebars.compile(specsPageTemplate);

const landingPageAndurilPath = path.join(TEMPLATES_DIR, 'pages', 'landing-page-anduril.hbs');
const landingPageAndurilTemplate = fs.readFileSync(landingPageAndurilPath, 'utf8');
const landingPageAnduril = Handlebars.compile(landingPageAndurilTemplate);

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

  // Use different template based on page type
  let pageTemplate;
  if (pageData.layout === 'landing-page-anduril') {
    pageTemplate = landingPageAnduril;
  } else if (pageName === 'home') {
    pageTemplate = homePage;
  } else if (pageName === 'specifications') {
    pageTemplate = specsPage;
  } else {
    pageTemplate = landingPage;
  }
  const bodyHTML = pageTemplate(templateData);

  // Render into base layout (skip for standalone templates)
  let finalHTML;
  if (pageData.layout === 'landing-page-anduril') {
    // Anduril template is standalone - don't wrap in base layout
    finalHTML = bodyHTML;
  } else {
    // Other templates need base layout wrapper
    finalHTML = baseLayout({
      ...templateData,
      body: bodyHTML
    });
  }

  // Output home page as index.html
  const outputName = (pageName === 'home') ? 'index.html' : `${pageName}.html`;
  const outputPath = path.join(BUILD_DIR, outputName);
  fs.writeFileSync(outputPath, finalHTML, 'utf8');

  console.log(`✅ Built ${outputName}`);
});

// CSS files already exist in lab/css/ - no need to copy

console.log('\n✨ Build complete!');
