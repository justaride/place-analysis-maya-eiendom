#!/bin/bash

# Script to update all place-analysis projects with template changes
# Created: 2025-11-19

TEMPLATE_DIR="/Users/gabrielboen/place-analysis-template"

# List of projects to update
PROJECTS=(
  "/Users/gabrielboen/natural-state-place-analysis-grunerlokka-2025"
  "/Users/gabrielboen/place-analysis-aspelin-ramm"
  "/Users/gabrielboen/place-analysis-brodreneevensen"
  "/Users/gabrielboen/place-analysis-eiendomsspar"
  "/Users/gabrielboen/place-analysis-lokka"
  "/Users/gabrielboen/place-analysis-maya-eiendom"
  "/Users/gabrielboen/place-analysis-roger-vodal"
  "/Users/gabrielboen/place-analysis-sio"
)

# Files to copy
FILES=(
  "src/components/layout/Navigation.tsx"
  "src/components/ui/NaturalStateCard.tsx"
  "src/app/page.tsx"
  "src/app/om-prosjektet/page.tsx"
  "src/types/eiendom.ts"
  "src/components/eiendom/AnalyseSelector.tsx"
  "src/app/eiendommer/[id]/page.tsx"
)

echo "========================================="
echo "Place Analysis Template Update Script"
echo "========================================="
echo ""

for PROJECT in "${PROJECTS[@]}"; do
  PROJECT_NAME=$(basename "$PROJECT")
  echo "Updating: $PROJECT_NAME"

  for FILE in "${FILES[@]}"; do
    SOURCE="$TEMPLATE_DIR/$FILE"
    DEST="$PROJECT/$FILE"

    if [ -f "$SOURCE" ]; then
      # Create directory if it doesn't exist
      mkdir -p "$(dirname "$DEST")"

      # Copy file
      cp "$SOURCE" "$DEST"
      echo "  ✓ Copied: $FILE"
    else
      echo "  ✗ Source not found: $FILE"
    fi
  done

  echo "  ✓ $PROJECT_NAME updated"
  echo ""
done

echo "========================================="
echo "Update complete!"
echo "========================================="
