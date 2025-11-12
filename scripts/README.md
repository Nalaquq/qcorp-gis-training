# Satellite Imagery Analysis and River Monitoring Tools

This directory contains tools for satellite imagery analysis and automated river monitoring:

- **Google Earth Engine Scripts**: JavaScript tools for exporting satellite data
- **Python Analysis Tools**: Automated river extraction and temporal change detection

## Quick Start

1. **Export Data from GEE** → Use JavaScript scripts below to export water/land classifications
2. **Extract Rivers** → Use Python tools to convert rasters to vector polygons
3. **Analyze Changes** → Compare multiple dates to detect channel migration

See [RIVER_ANALYSIS_README.md](./RIVER_ANALYSIS_README.md) for detailed Python tool documentation.

## Scripts

### sentinel2_date_slider.js

An interactive Google Earth Engine script for downloading Sentinel-2 satellite imagery with customizable date ranges and band selection.

**Features:**
- Interactive date range selection using dual date sliders
- Multi-band selection UI with 22 available Sentinel-2 bands organized by category:
  - **True Color Image**: TCI_R, TCI_G, TCI_B (10m resolution)
  - **Visible & NIR**: B2 (Blue), B3 (Green), B4 (Red), B8 (NIR) (10m resolution)
  - **Red Edge**: B5, B6, B7, B8A (20m resolution)
  - **SWIR**: B11, B12 (20m resolution)
  - **Atmospheric**: B1 (Aerosols), B9 (Water Vapor) (60m resolution)
  - **Level-2 Products**: AOT, WVP, SCL (10-20m resolution)
- Automatic cloud masking (filters to <5% cloud coverage)
- Smart visualization based on selected bands:
  - Single band: Displays as grayscale
  - Multiple bands: Displays first 3 as RGB composite
- Export to Google Drive as multi-band GeoTIFF
- Draw custom AOI (Area of Interest) with polygon tool

**How to Use:**

1. **Access the Script:**
   - Open [Google Earth Engine Code Editor](https://code.earthengine.google.com/)
   - Copy and paste the contents of `sentinel2_date_slider.js`

2. **Set Up Your Analysis:**
   - Draw a polygon on the map to define your area of interest
   - Use the start and end date sliders to select your time range
   - Select which bands you want to export (RGB selected by default)
     - Use "Select All" to export all 22 bands
     - Use "Clear All" to deselect everything and start fresh

3. **Run and Export:**
   - Click "Run Analysis" to process the imagery
   - The selected bands will be visualized on the map
   - Check the "Tasks" tab (top-right) to export to Google Drive
   - Click "Run" on the export task to download your GeoTIFF

**Use Cases:**
- Vegetation health analysis (using NIR and Red Edge bands)
- Water body mapping (using SWIR bands)
- True color imagery for visual interpretation
- Multi-spectral analysis combining multiple bands
- Time-series analysis of landscape change

**Data Source:**
[Copernicus Sentinel-2 SR Harmonized](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED)

**Resolution:** 10m-60m (varies by band)

**Cloud Coverage Filter:** <5%

---

### sentinel2_water_land_classification.js

An interactive Google Earth Engine script for water/land classification using NIR (Near-Infrared) imagery from Sentinel-2. Perfect for river monitoring, water body mapping, and detecting landscape changes.

**Features:**
- NIR-based binary classification (B8 band at 835nm)
- Adjustable threshold slider for water detection sensitivity
- Three preset modes:
  - **Conservative** (0.10): Detects more water, good for turbid/shallow water
  - **Moderate** (0.15): Balanced detection (default)
  - **Aggressive** (0.20): Detects less water, good for clear water bodies
- Real-time area statistics (hectares and percentages for water and land)
- Binary raster output (0 = Water, 1 = Land)
- Visual legend with color-coded display (Blue = Water, Green = Land)
- Automatic cloud masking (<5% cloud coverage)
- Date range selection with dual sliders
- Export as byte-encoded GeoTIFF for efficient storage

**How to Use:**

1. **Access the Script:**
   - Open [Google Earth Engine Code Editor](https://code.earthengine.google.com/)
   - Copy and paste the contents of `sentinel2_water_land_classification.js`

2. **Set Up Your Analysis:**
   - Draw a polygon on the map to define your study area
   - Use the start and end date sliders to select your time range
   - Adjust the NIR threshold slider to fine-tune water detection:
     - **Lower values** (0.05-0.10): Detect more water (includes turbid, vegetated, or shallow water)
     - **Higher values** (0.20-0.30): Detect less water (only clear, deep water bodies)
   - Use preset buttons for quick threshold selection

3. **Run and Export:**
   - Click "Run Analysis" to process the classification
   - View water/land statistics in the status panel
   - The binary classification will display on the map (Blue=Water, Green=Land)
   - Optional: Toggle on the "NIR (B8)" layer to see the raw NIR data
   - Check the "Tasks" tab (top-right) to export to Google Drive
   - Click "Run" on the export task to download your binary GeoTIFF

4. **Interpret Results:**
   - **Value 0 (Blue)**: Water - includes rivers, lakes, ponds, flooded areas
   - **Value 1 (Green)**: Land - includes vegetation, bare ground, buildings, ice/snow
   - Use area statistics to quantify water extent changes over time

**Use Cases:**
- **River monitoring**: Track river channel migration and avulsion
- **Flood mapping**: Assess inundation extent during high water events
- **Water body inventory**: Map lakes, ponds, and wetlands
- **Seasonal analysis**: Compare water extent across different seasons
- **Change detection**: Identify new water bodies or dried-up areas
- **Salmon habitat**: Map potential spawning areas and water access

**Method:**
The script uses a simple but effective NIR threshold method. Water absorbs NIR radiation (low reflectance), while land reflects it (high reflectance). By setting a threshold value, we separate water from land. The optimal threshold varies based on:
- Water turbidity (sediment content)
- Vegetation in/around water
- Water depth
- Atmospheric conditions
- Surrounding land cover

**Data Source:**
[Copernicus Sentinel-2 SR Harmonized](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED)

**Resolution:** 10m (B8 NIR band)

**Cloud Coverage Filter:** <5%

**Output Format:** Binary GeoTIFF (byte-encoded: 0=Water, 1=Land)

**Tips:**
- Run multiple analyses with different thresholds to find the best one for your area
- For river monitoring, use summer dates (June-August) when water is most visible
- For flood assessment, compare classifications before and after storm events
- Export multiple dates and compare in ArcGIS Pro to create change detection maps
- Consider ground-truthing results with field observations or high-resolution imagery

---

## Python River Analysis Tools

### Overview

Automated Python tools for extracting river channel polygons (including braids) from binary water/land rasters and performing temporal change analysis.

**Tools:**
- `river_extraction.py` - Extract river polygons from binary rasters
- `river_temporal_analysis.py` - Compare multiple dates, detect changes
- `river_extraction_workflow.ipynb` - Interactive Jupyter notebook tutorial
- `requirements.txt` - Python dependencies

**Complete documentation:** See [RIVER_ANALYSIS_README.md](./RIVER_ANALYSIS_README.md)

### Installation

```bash
pip install -r requirements.txt
```

**Required packages:** rasterio, geopandas, scipy, numpy, pandas, matplotlib

### Quick Usage

**Extract river from single raster:**

```bash
python river_extraction.py WaterLand_Classification.tif river_output.gpkg
```

**Or in Python:**

```python
from river_extraction import RiverExtractor

extractor = RiverExtractor("WaterLand_Classification.tif")
river_gdf = extractor.extract_river(method='largest')
extractor.save_vector(river_gdf, "river_output.gpkg")
```

**Temporal analysis:**

```bash
python river_temporal_analysis.py output_dir river1.gpkg 2024-05-01 river2.gpkg 2024-10-30
```

**Interactive workflow:**

```bash
jupyter notebook river_extraction_workflow.ipynb
```

### Key Features

**River Extraction:**
- Automatic water detection
- Preserves all braided channels (no size limit)
- Two extraction methods: largest water body or seed point
- Noise removal and polygon simplification
- Batch processing for multiple dates

**Temporal Analysis:**
- Area change calculations over time
- Gain/loss detection (new water, abandoned channels)
- Channel migration distance measurements
- New channel detection (avulsion, braiding events)
- Comprehensive reports with maps and statistics

### Use Cases

- **River Avulsion Monitoring**: Track sudden channel changes
- **Flood Assessment**: Quantify inundation extent
- **Seasonal Variability**: Compare wet vs dry seasons
- **Storm Impact**: Before/after event analysis
- **Salmon Habitat**: Map accessible spawning areas
- **Infrastructure Planning**: Identify areas at risk

### Outputs

All tools export to **GeoPackage (.gpkg)** format, compatible with:
- ArcGIS Pro
- QGIS
- Python (geopandas)
- Web applications (convertible to GeoJSON)

### Future Development

These tools are designed to be integrated into a **Flask web application** for automated river monitoring. The modular architecture allows easy deployment as a web service with:
- Upload interface for binary rasters
- Automated extraction and analysis
- Interactive change detection dashboard
- Email alerts for significant changes

---

## Installation & Setup (Google Earth Engine)

### Prerequisites

1. **Google Earth Engine Account:**
   - Sign up at [https://earthengine.google.com/](https://earthengine.google.com/)
   - Earth Engine is free for non-commercial use

2. **Google Drive:**
   - Ensure you have sufficient storage for exported imagery
   - Large AOIs may produce multi-gigabyte files

### No Installation Required

Google Earth Engine runs entirely in the cloud through your web browser. Simply copy the script into the Code Editor and run it.

---

## Additional Resources

- [Google Earth Engine Documentation](https://developers.google.com/earth-engine/)
- [Sentinel-2 Band Information](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED#bands)
- [Earth Engine Code Editor Guide](https://developers.google.com/earth-engine/guides/playground)
- [Water Detection Methods in Remote Sensing](https://developers.google.com/earth-engine/tutorials/community/sentinel-2-s2cloudless)
- [Image Classification Tutorial](https://developers.google.com/earth-engine/guides/classification)

---

## Support

For questions or issues with these scripts, please open an issue in the main repository or contact the training team.

---

**Last Updated:** November 2025
