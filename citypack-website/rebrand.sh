#!/bin/bash

# Citypack Rebranding Script
# Complete rebrand from Labrador/LAB SEVEN to Citypack/SEVEN PACK

cd /Users/amitrunchal/apps/fieldpack_apps/_citypack/citypack-website

echo "========================================="
echo "CITYPACK REBRANDING SCRIPT"
echo "========================================="
echo ""

# Step 1: Create backup branch
echo "Step 1: Creating backup branch..."
git checkout -b pre-rebrand-backup-$(date +%Y%m%d)
git checkout main
echo "✓ Backup branch created"
echo ""

# Step 2: Rebrand all content files - Labrador → Citypack
echo "Step 2: Rebranding 'Labrador' → 'Citypack' in content files..."
find content/ -name "*.json" -type f -exec sed -i '' 's/Labrador Field Systems/Citypack/g' {} +
find content/ -name "*.json" -type f -exec sed -i '' 's/Labrador/Citypack/g' {} +
find content/ -name "*.json" -type f -exec sed -i '' 's/LABRADOR/CITYPACK/g' {} +
echo "✓ Content files rebranded"
echo ""

# Step 3: Rebrand product name - LAB SEVEN → SEVEN PACK
echo "Step 3: Rebranding 'LAB SEVEN' → 'SEVEN PACK'..."
find content/ -name "*.json" -type f -exec sed -i '' 's/LAB SEVEN BATTERY/SEVEN PACK/g' {} +
find content/ -name "*.json" -type f -exec sed -i '' 's/LAB SEVEN/SEVEN PACK/g' {} +
find content/ -name "*.json" -type f -exec sed -i '' 's/Lab Seven/Seven Pack/g' {} +
echo "✓ Product name rebranded"
echo ""

# Step 4: Check for remaining instances
echo "Step 4: Checking for remaining instances..."
echo "Labrador/LABRADOR instances:"
grep -ri "labrador" content/ templates/ --exclude-dir=node_modules 2>/dev/null | wc -l | xargs echo
echo "LAB SEVEN/Lab Seven instances:"
grep -ri "lab seven" content/ templates/ --exclude-dir=node_modules 2>/dev/null | wc -l | xargs echo
echo ""

# Step 5: Build
echo "Step 5: Building site..."
npm run build
echo ""

# Step 6: Show changes summary
echo "Step 6: Changes summary..."
git status --short | head -20
echo ""
if [ $(git status --short | wc -l) -gt 20 ]; then
    echo "... and $(( $(git status --short | wc -l) - 20 )) more files"
    echo ""
fi

echo "========================================="
echo "REBRANDING COMPLETE!"
echo "========================================="
echo ""
echo "Templates and package.json already updated manually."
echo ""
echo "Next steps:"
echo "1. Review changes: git diff content/pages/home.json"
echo "2. Test locally: npm run dev"
echo "3. Commit: git add -A && git commit -m 'rebrand: Labrador → Citypack | LAB SEVEN → SEVEN PACK'"
echo "4. Update GitHub repo name to 'citypack-website'"
echo "5. Update git remote: git remote set-url origin https://github.com/fieldpackco/citypack-website.git"
echo "6. Push: git push origin main"
echo ""
