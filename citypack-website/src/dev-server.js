const chokidar = require('chokidar');
const browserSync = require('browser-sync').create();
const { execSync } = require('child_process');
const path = require('path');

// Ensure we're in the project root
const projectRoot = path.resolve(__dirname, '..');
process.chdir(projectRoot);

console.log('🚀 Starting development server...\n');

// Initial build
try {
  console.log('📦 Running initial build...');
  execSync('npm run build', { stdio: 'inherit', cwd: projectRoot });
} catch (error) {
  console.error('❌ Initial build failed');
  process.exit(1);
}

// Start BrowserSync
browserSync.init({
  server: {
    baseDir: '.',  // Serve from lab/ directory root
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
