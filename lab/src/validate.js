const fs = require('fs');
const path = require('path');
const Ajv = require('ajv');

const SCHEMAS_DIR = path.join(__dirname, '../content/schemas');
const PAGES_DIR = path.join(__dirname, '../content/pages');

const ajv = new Ajv({ allErrors: true, verbose: true });

// Load all schemas
const schemas = {};
const schemaFiles = fs.readdirSync(SCHEMAS_DIR);

// First pass: load all schemas with both filename and ID
schemaFiles.forEach(file => {
  const schemaPath = path.join(SCHEMAS_DIR, file);
  const schema = JSON.parse(fs.readFileSync(schemaPath, 'utf8'));
  const schemaId = file.replace('.schema.json', '');
  schemas[schemaId] = schema;
  // Add schema with both the short ID and the full filename as reference
  ajv.addSchema(schema, schemaId);
  ajv.addSchema(schema, file);
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
