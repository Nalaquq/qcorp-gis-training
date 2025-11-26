#!/bin/bash
# Convert ADOT trail marking map PDF to PNG for markdown display

# Try different conversion methods
if command -v pdftoppm &> /dev/null; then
    echo "Using pdftoppm..."
    pdftoppm -png -singlefile -r 150 "assets/ADOT trail marking map.pdf" "assets/ADOT-trail-marking-map"
elif command -v convert &> /dev/null; then
    echo "Using ImageMagick convert..."
    convert -density 150 "assets/ADOT trail marking map.pdf" "assets/ADOT-trail-marking-map.png"
elif command -v magick &> /dev/null; then
    echo "Using ImageMagick magick..."
    magick -density 150 "assets/ADOT trail marking map.pdf" "assets/ADOT-trail-marking-map.png"
elif command -v gs &> /dev/null; then
    echo "Using ghostscript..."
    gs -dNOPAUSE -dBATCH -sDEVICE=png16m -r150 -sOutputFile="assets/ADOT-trail-marking-map.png" "assets/ADOT trail marking map.pdf"
else
    echo "No PDF conversion tool found. Please install one of:"
    echo "  - poppler-utils (for pdftoppm)"
    echo "  - imagemagick (for convert)"
    echo "  - ghostscript (for gs)"
    echo ""
    echo "Or convert manually and save as: assets/ADOT-trail-marking-map.png"
    exit 1
fi

echo "Conversion complete! Check assets/ADOT-trail-marking-map.png"
