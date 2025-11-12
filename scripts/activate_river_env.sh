#!/bin/bash
# Quick activation script for river analysis virtual environment
# Usage: source activate_river_env.sh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

if [ -d "river_env" ]; then
    source river_env/bin/activate
    echo "✓ River analysis environment activated!"
    echo ""
    echo "Available tools:"
    echo "  python river_extraction.py <raster.tif> <output.gpkg>"
    echo "  python river_temporal_analysis.py <output_dir> <river1.gpkg> <date1> ..."
    echo "  jupyter notebook river_extraction_workflow.ipynb"
    echo ""
else
    echo "ERROR: river_env not found!"
    echo "Run: python3 -m venv river_env && source river_env/bin/activate && pip install -r requirements.txt"
fi
