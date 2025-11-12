# Google Earth Engine Scripts

This directory contains Google Earth Engine (GEE) scripts for satellite imagery analysis and processing.

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

## Installation & Setup

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

---

## Support

For questions or issues with these scripts, please open an issue in the main repository or contact the training team.

---

**Last Updated:** November 2025
