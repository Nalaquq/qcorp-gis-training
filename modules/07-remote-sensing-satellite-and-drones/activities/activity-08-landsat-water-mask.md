# Lesson: Landsat Water Detection & Spectral Index Analysis with Google Earth Engine

**Duration:** 120–150 minutes
**Prerequisites:** Basic JavaScript familiarity, GEE account, understanding of raster data
**Difficulty:** Intermediate

---

## Overview

In this lesson, you will use the Google Earth Engine (GEE) Code Editor to generate monthly water masks and spectral vegetation/moisture indices from Landsat satellite imagery. The script supports Landsat 5, 7, 8, and 9, allowing you to analyze water body extent and vegetation health from 1984 to the present.

By the end, you will have exported monthly multiband composites, binary water/land classifications, and multi-band spectral index rasters as GeoTIFF files. These outputs support temporal analysis of waterway and lake growth/shrinkage alongside vegetation health changes — ready for use in ArcGIS Pro or further processing with `river_extraction_workflow.ipynb`.

This approach is particularly valuable for monitoring seasonal and long-term environmental changes in rivers, lakes, wetlands, and surrounding vegetation across Alaska Native communities.

---

## Learning Objectives

By the end of this lesson, you will be able to:

1. ✅ Understand the Landsat mission history and band differences across L5/L7/L8/L9
2. ✅ Use GEE to query, filter, and merge satellite imagery collections
3. ✅ Apply QA_PIXEL cloud masking and Collection 2 Level 2 surface reflectance scaling
4. ✅ Harmonize band names across different Landsat sensors
5. ✅ Create monthly median composites from cloud-masked imagery
6. ✅ Apply NIR thresholding to classify water vs. land
7. ✅ Explain what spectral indices are and why they are useful for environmental monitoring
8. ✅ Interpret NDVI, EVI, GNDVI, CIG, and other vegetation indices
9. ✅ Interpret NDWI, MNDWI, and other water/moisture indices
10. ✅ Export multiband rasters, binary masks, and index rasters as GeoTIFF to Google Drive

---

## Part 1: Background — The Landsat Program

The Landsat program is the longest-running satellite Earth observation program, providing continuous global coverage since 1972. For this script, we use Collection 2 Level 2 surface reflectance data from four sensors:

| Sensor | Mission | Years | GEE Collection | Key Bands |
|--------|---------|-------|----------------|-----------|
| TM | Landsat 5 | 1984–2012 | `LANDSAT/LT05/C02/T1_L2` | SR_B1–B5, SR_B7 |
| ETM+ | Landsat 7 | 1999–2024 | `LANDSAT/LE07/C02/T1_L2` | SR_B1–B5, SR_B7 |
| OLI | Landsat 8 | 2013–present | `LANDSAT/LC08/C02/T1_L2` | SR_B2–B7 |
| OLI-2 | Landsat 9 | 2021–present | `LANDSAT/LC09/C02/T1_L2` | SR_B2–B7 |

### Key Points

- **Resolution:** All sensors provide 30m spatial resolution for optical bands
- **Revisit:** Each satellite revisits the same location every 16 days; overlapping missions increase temporal coverage
- **Collection 2 Level 2:** Surface reflectance data with atmospheric correction applied by USGS. Raw pixel values must be scaled: `SR = pixel_value × 0.0000275 − 0.2`
- **Band numbering differs:** Landsat 5/7 use SR_B1–B5 + SR_B7 for the six optical bands, while Landsat 8/9 use SR_B2–B7. Our script harmonizes these to common names (Blue, Green, Red, NIR, SWIR1, SWIR2)
- **Landsat 7 SLC failure:** After May 2003, Landsat 7 images have scan-line corrector gaps. Monthly median compositing helps fill these gaps

---

## Part 2: Background — NIR Water Detection

### Why NIR?

Water strongly absorbs near-infrared (NIR) radiation, while vegetation and soil reflect it strongly. This makes the NIR band an effective single-band indicator for water detection:

- **Water:** Low NIR reflectance (typically < 0.1–0.2)
- **Vegetation:** High NIR reflectance (typically > 0.3)
- **Bare soil:** Moderate NIR reflectance (typically 0.2–0.4)

### How Thresholding Works

A threshold value is applied to the NIR band:
- If `NIR < threshold` → classified as **water (1)**
- If `NIR ≥ threshold` → classified as **land (0)**

### Limitations

- **Turbid water** (high sediment) can have elevated NIR values, causing under-detection
- **Cloud shadows** may be misclassified as water (our script masks these using QA_PIXEL)
- **Dark surfaces** (asphalt, lava, deep shadows) may be misclassified as water
- **Seasonal ice/snow** can affect results in winter months
- A single global threshold may not work perfectly for all conditions — always preview and adjust

---

## Part 3: Background — Spectral Indices

### What Is a Spectral Index?

A spectral index is a mathematical combination of two or more spectral bands that highlights a specific property of the Earth's surface. Rather than looking at raw reflectance values, indices amplify the signal of what you care about (vegetation health, water presence, soil exposure) and suppress everything else.

Most indices use a **normalized difference** formula:

```
Index = (Band_A - Band_B) / (Band_A + Band_B)
```

This produces values between **-1 and +1**, making it easy to compare across different dates, sensors, and lighting conditions. The normalization cancels out variations in brightness, so you are measuring the *relative* difference between bands rather than absolute reflectance.

### Why Use Indices Instead of Raw Bands?

- **Consistency:** Indices are less sensitive to atmospheric conditions, sun angle, and sensor calibration differences than raw band values
- **Interpretability:** A single NDVI value tells you more about vegetation health than six separate band values
- **Change detection:** Comparing index values across months or years reveals trends that are hard to see in raw imagery
- **Thresholding:** Indices make it straightforward to classify features (e.g., "NDVI > 0.4 = healthy vegetation")

### How to Interpret Index Values

Most normalized indices range from **-1 to +1**:
- Values near **+1** indicate strong presence of the feature the index measures
- Values near **0** indicate mixed or transitional conditions
- Values near **-1** indicate absence or the opposite condition

For example, NDVI values:
- **0.6–0.9** = Dense, healthy vegetation (forests, wetlands in summer)
- **0.2–0.5** = Moderate vegetation (grasslands, sparse shrubs)
- **0.0–0.2** = Bare soil, rock, or dormant vegetation
- **< 0.0** = Water, snow, or clouds

---

## Part 4: Available Indices — Reference

The script computes 13 spectral indices organized into four categories. All use the harmonized band names (Blue, Green, Red, NIR, SWIR1, SWIR2) so they work consistently across all Landsat sensors.

### Vegetation Health & Biomass (8 indices)

| Index | Full Name | Formula | What It Measures |
|-------|-----------|---------|-----------------|
| **NDVI** | Normalized Difference Vegetation Index | `(NIR - Red) / (NIR + Red)` | Overall vegetation greenness and biomass. The most widely used vegetation index. Higher values = more/healthier vegetation. |
| **EVI** | Enhanced Vegetation Index | `2.5 × (NIR - Red) / (NIR + 6×Red - 7.5×Blue + 1)` | Similar to NDVI but corrects for atmospheric aerosols and soil background. Better in dense canopy where NDVI saturates. |
| **GNDVI** | Green Normalized Difference Vegetation Index | `(NIR - Green) / (NIR + Green)` | Sensitive to chlorophyll concentration and nitrogen content. Useful for assessing crop/plant nutrition status. |
| **SAVI** | Soil-Adjusted Vegetation Index | `1.5 × (NIR - Red) / (NIR + Red + 0.5)` | Like NDVI but minimizes soil brightness influence. Best for areas with sparse vegetation and exposed soil. |
| **MSAVI** | Modified Soil-Adjusted Vegetation Index | `(2×NIR + 1 - √((2×NIR+1)² - 8×(NIR-Red))) / 2` | Automatically adjusts the soil correction factor. More accurate than SAVI for very sparse vegetation. |
| **CIG** | Chlorophyll Index Green | `(NIR / Green) - 1` | Estimates leaf chlorophyll content. Directly relates to plant photosynthetic capacity and health. |
| **VARI** | Visible Atmospherically Resistant Index | `(Green - Red) / (Green + Red - Blue)` | Estimates vegetation fraction using only visible bands. Works even without NIR data. |
| **ARVI** | Atmospherically Resistant Vegetation Index | `(NIR - (2×Red - Blue)) / (NIR + (2×Red - Blue))` | Self-corrects for atmospheric scattering. Best for smoky or hazy conditions (e.g., wildfire season). |

### Water (2 indices)

| Index | Full Name | Formula | What It Measures |
|-------|-----------|---------|-----------------|
| **NDWI** | Normalized Difference Water Index | `(Green - NIR) / (Green + NIR)` | Water body delineation and vegetation water stress. Positive values indicate open water. |
| **MNDWI** | Modified Normalized Difference Water Index | `(Green - SWIR1) / (Green + SWIR1)` | Better than NDWI at separating water from built-up areas and bare soil. Uses SWIR instead of NIR. |

### Burn & Disturbance (1 index)

| Index | Full Name | Formula | What It Measures |
|-------|-----------|---------|-----------------|
| **NBR** | Normalized Burn Ratio | `(NIR - SWIR2) / (NIR + SWIR2)` | Fire severity and vegetation disturbance. Low/negative values indicate burned areas. Also useful for detecting other types of landscape disturbance. |

### Soil & Moisture (2 indices)

| Index | Full Name | Formula | What It Measures |
|-------|-----------|---------|-----------------|
| **BSI** | Bare Soil Index | `((SWIR1 + Red) - (NIR + Blue)) / ((SWIR1 + Red) + (NIR + Blue))` | Identifies exposed soil and bare ground. Positive values indicate bare soil, negative values indicate vegetation or water cover. |
| **NDMI** | Normalized Difference Moisture Index | `(NIR - SWIR1) / (NIR + SWIR1)` | Canopy and soil moisture content. Higher values indicate more moisture. Useful for drought monitoring and wetland delineation. |

### Indices NOT Available on Landsat

The following indices from the Planet imagery workflow require **red edge bands** (~700–730nm) that Landsat sensors do not carry. Use **Sentinel-2** (which has three red edge bands) for these:

| Index | Why It Needs Red Edge |
|-------|----------------------|
| **RTVICore** (Red Edge Triangulated Vegetation Index) | Uses red edge reflectance to triangulate chlorophyll absorption |
| **PRI** (Photochemical Reflectance Index) | Requires narrow bands at 531nm and 570nm |
| **CRI** (Carotenoid Reflectance Index) | Requires narrow bands at 510nm and 550nm |
| **CIrededge** (Chlorophyll Index Red Edge) | Uses red edge band divided by NIR |

---

## Part 5: Choosing the Right Indices for Your Analysis

### For Water Body Monitoring (lake/river growth and shrinkage)

Use these together for the most complete picture:
- **NDWI** or **MNDWI** — Delineate water boundaries (MNDWI is better if your AOI includes buildings or roads)
- **NDMI** — Track moisture in surrounding wetlands and riparian zones
- **Water mask** (NIR threshold) — Simple binary classification for change detection

### For Vegetation Health Over Time

- **NDVI** — Start here as your baseline vegetation metric
- **EVI** — Use alongside NDVI in densely vegetated areas where NDVI saturates (forests, dense wetlands)
- **GNDVI** — Track nitrogen/chlorophyll changes (good for detecting vegetation stress before it's visible in NDVI)
- **CIG** — Most directly related to photosynthetic capacity

### For Sparse Vegetation / Tundra

- **SAVI** or **MSAVI** — Essential when there is significant bare soil or rock (common in Alaska tundra, gravel bars)
- **BSI** — Track bare ground exposure as permafrost thaw or erosion exposes soil

### For Disturbance Detection

- **NBR** — Detect wildfire burn scars, logging, or other sudden vegetation loss
- **ARVI** — Better than NDVI when smoke or haze is present (wildfire season)

### Recommended Default Selection

For a comprehensive temporal analysis of waterways and surrounding vegetation in Alaska, we recommend starting with:

- ✅ **NDVI** — vegetation baseline
- ✅ **EVI** — dense vegetation correction
- ✅ **GNDVI** — chlorophyll/nitrogen tracking
- ✅ **CIG** — photosynthetic health
- ✅ **NDWI** — water extent
- ☐ Add **SAVI/MSAVI** if your AOI has significant bare ground
- ☐ Add **NBR** if investigating fire history
- ☐ Add **NDMI** if tracking wetland moisture

---

## Part 6: Methodology Walkthrough

This section walks through each part of the `landsat_water_mask.js` script.

### 6.1 Sensor Configuration

The script defines a `LANDSAT_SENSORS` dictionary mapping each sensor to its GEE collection ID, date range, native band names, and common band names. This enables automatic collection selection based on the user's date range.

### 6.2 Cloud Masking

The `maskCloudsLandsat()` function uses the `QA_PIXEL` quality band included with every Landsat image:
- **Bit 3** = cloud detected
- **Bit 4** = cloud shadow detected

Pixels where either bit is set are masked (removed from analysis).

### 6.3 Surface Reflectance Scaling

The `applyScaleFactors()` function converts raw digital numbers to physical surface reflectance values using the Collection 2 Level 2 formula: `SR = DN × 0.0000275 − 0.2`. This ensures values are comparable across sensors and dates.

### 6.4 Band Harmonization

The `makeHarmonizer()` function renames sensor-specific bands to common names:
- Landsat 5/7: `SR_B1→Blue, SR_B2→Green, SR_B3→Red, SR_B4→NIR, SR_B5→SWIR1, SR_B7→SWIR2`
- Landsat 8/9: `SR_B2→Blue, SR_B3→Green, SR_B4→Red, SR_B5→NIR, SR_B6→SWIR1, SR_B7→SWIR2`

This allows images from different sensors to be merged into a single collection. It also means the spectral index formulas work identically regardless of which Landsat sensor captured the data.

### 6.5 Auto-Selection & Merging

The `getLandsatCollection()` function checks which sensors overlap the user's date range and merges their harmonized collections. For example, a date range of 1998–2002 would include both Landsat 5 and Landsat 7 imagery.

### 6.6 Query & Preview

When the user clicks **Query Imagery**, the script:
1. Extracts the drawn polygon geometry
2. Calls `getLandsatCollection()` to build the merged collection
3. Reports the image count and sensors used
4. Displays a median RGB composite on the map

### 6.7 NIR Threshold & Water Mask Preview

The user adjusts the NIR threshold slider (range 0.05–0.50, default 0.15) and clicks **Preview Water Mask** to see the binary classification overlaid on the map. Water area statistics (hectares and percent of AOI) are calculated and displayed.

### 6.8 Spectral Index Selection

The UI panel contains checkboxes for all 13 available indices, organized by category. NDVI, EVI, GNDVI, CIG, and NDWI are selected by default. The user can toggle individual indices or use the Select All / Clear All buttons.

### 6.9 Monthly Composite & Index Generation

When the user clicks **Generate Monthly Masks**, the script:
1. Iterates through each month in the date range
2. Filters the collection to that month
3. Computes a **median** composite (why median? — it is resistant to outliers from clouds, haze, and sensor artifacts)
4. Applies the NIR threshold to create a binary water mask
5. Computes selected spectral indices from the composite
6. Submits up to three export tasks per month to Google Drive:
   - `{prefix}_multiband_YYYY-MM.tif` — 6-band surface reflectance composite
   - `{prefix}_water_mask_YYYY-MM.tif` — binary water classification (1=water, 0=land)
   - `{prefix}_indices_YYYY-MM.tif` — multi-band raster with all selected spectral indices
7. Skips months with zero available images

### Why Compute Indices on Monthly Composites?

The indices are computed **after** the monthly median compositing step, not on individual images. This is important because:
- The median composite already has clouds, shadows, and outliers removed
- Index values from a clean composite are more representative than averaging noisy per-image indices
- It reduces the number of GEE computations and export tasks

---

## Part 7: Hands-On Exercise

Follow these steps to run the script with a test area:

### Exercise A: Water Mask Generation

- [ ] Open the [GEE Code Editor](https://code.earthengine.google.com/)
- [ ] Copy the contents of `landsat_water_mask.js` into a new script
- [ ] Draw a polygon around your area of interest (e.g., a river reach near Quinhagak)
- [ ] Set the start date to **1990-01-01** and end date to **1995-12-31**
- [ ] Enter a filename prefix (e.g., `quinhagak_river`)
- [ ] Click **Query Imagery** — verify Landsat 5 TM is the collection used
- [ ] Examine the RGB preview on the map
- [ ] Adjust the NIR threshold slider and click **Preview Water Mask**
- [ ] Try the Conservative (0.10), Moderate (0.15), and Aggressive (0.20) presets

### Exercise B: Spectral Index Selection

- [ ] In the Spectral Indices panel, ensure **NDVI**, **EVI**, **GNDVI**, **CIG**, and **NDWI** are checked
- [ ] If your AOI has significant bare ground (gravel bars, tundra), also check **SAVI** and **BSI**
- [ ] Click **Generate Monthly Masks**
- [ ] Open the **Tasks** tab and run the export tasks
- [ ] Download the exported GeoTIFFs from Google Drive
- [ ] Verify you have three files per month: `_multiband_`, `_water_mask_`, and `_indices_`

### Exercise C: Temporal Comparison

- [ ] Change the date range to **2020-01-01 to 2024-12-31** and verify that Landsat 8 and 9 are auto-selected
- [ ] Run the same analysis with the same indices selected
- [ ] In ArcGIS Pro, load the NDVI band from a 1990s summer month and a 2020s summer month
- [ ] Compare: Has vegetation coverage increased or decreased? Where are the biggest changes?
- [ ] Load the NDWI bands from the same months — has the river/lake extent changed?

### Exercise D: Index Interpretation

Open an exported `_indices_` GeoTIFF in ArcGIS Pro and examine each band:

- [ ] **NDVI band:** Apply a green color ramp. Where is vegetation healthiest? Where is it absent?
- [ ] **NDWI band:** Apply a blue color ramp. Do the positive-value areas match the water mask?
- [ ] **CIG band:** Compare with NDVI. Are there areas where CIG shows stress that NDVI doesn't?
- [ ] **GNDVI band:** Look for spatial patterns in nitrogen/chlorophyll — do they follow the river corridor?

---

## Part 8: Key Takeaways

- The Landsat archive provides 40+ years of continuous 30m imagery — the longest satellite record available
- Band harmonization is essential when combining data from different Landsat sensors
- QA_PIXEL cloud masking removes clouds and shadows before compositing
- Monthly median composites reduce noise and fill data gaps (especially Landsat 7 SLC gaps)
- NIR thresholding is a simple but effective method for water detection; the optimal threshold depends on local conditions
- **Spectral indices** are mathematical combinations of bands that highlight specific surface properties
- **Normalized difference indices** (NDVI, NDWI, etc.) produce values from -1 to +1, making them comparable across dates and sensors
- Different indices reveal different aspects of the landscape — use multiple indices together for a complete picture
- **Vegetation indices** (NDVI, EVI, GNDVI, CIG) track plant health, biomass, and chlorophyll over time
- **Water indices** (NDWI, MNDWI) complement the binary water mask with continuous moisture information
- **SAVI/MSAVI** are critical for Alaska tundra and gravel bar environments where bare soil is common
- Exporting monthly index rasters enables time-series analysis of environmental change
- Binary water masks can be used directly in `river_extraction_workflow.ipynb` for polygon extraction and temporal change analysis

---

## Part 9: Assessment Questions

1. Why do Landsat 5/7 and Landsat 8/9 have different band numbers for the same spectral region? What problem does band harmonization solve?

2. What is the Collection 2 Level 2 surface reflectance scaling formula, and why is it necessary?

3. Which bits in the `QA_PIXEL` band indicate clouds and cloud shadows? Why do we mask both?

4. Why do we use the **median** rather than the **mean** for monthly composites?

5. If you set the NIR threshold too low (e.g., 0.05), what would happen to the water mask? What about too high (e.g., 0.40)?

6. A date range of 2010–2015 would include imagery from which Landsat sensors? Why might combining multiple sensors be beneficial?

7. What are two limitations of NIR-based water detection that could affect your results in Alaska?

8. Explain in your own words what a **normalized difference** index does. Why does dividing by the sum of two bands make the index more consistent across different dates?

9. You are monitoring a river corridor in tundra with large gravel bars. Which vegetation index would you choose over NDVI, and why?

10. What is the difference between **NDWI** and **MNDWI**? In what situation would you prefer MNDWI?

11. Your NDVI time series shows values of 0.65 in July 1990 and 0.45 in July 2023 for the same location. What might this indicate? What additional indices would help you investigate?

12. Why can't we compute RTVICore, PRI, CRI, or CIrededge from Landsat imagery? Which satellite would you use instead?

13. You notice that NDVI shows a healthy value (0.5) but CIG is unusually low for an area. What might this suggest about the vegetation?

---

## Part 10: Additional Resources

### Spectral Index References
- [Index Database (IDB)](https://www.indexdatabase.de/) — Comprehensive catalog of 500+ spectral indices with formulas and references
- [Awesome Spectral Indices (GitHub)](https://github.com/awesome-spectral-indices/awesome-spectral-indices) — Standardized index list with GEE code examples
- [USGS Landsat Spectral Indices](https://www.usgs.gov/landsat-missions/landsat-surface-reflectance-derived-spectral-indices) — Official USGS documentation on commonly used Landsat indices

### Landsat & GEE
- [USGS Landsat Missions](https://www.usgs.gov/landsat-missions) — Official documentation for all Landsat sensors
- [GEE Landsat Collection 2 Guide](https://developers.google.com/earth-engine/datasets/catalog/landsat) — GEE dataset catalog with band information
- [GEE QA_PIXEL Bitmask Documentation](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C02_T1_L2#bands) — Bitmask definitions for cloud masking

### Related Scripts in This Repository
- [`sentinel2_water_land_classification.js`](../../scripts/sentinel2_water_land_classification.js) — Similar approach using Sentinel-2 (10m, 2017–present)
- [`sentinel2_date_slider.js`](../../scripts/sentinel2_date_slider.js) — Multi-band Sentinel-2 composite with date selection
- [`river_extraction_workflow.ipynb`](../../scripts/river_extraction_workflow.ipynb) — Extract river polygons from binary water masks for temporal analysis
- [`planet_imagery_diagnostics.ipynb`](../../usda/planet_imagery_diagnostics.ipynb) — Planet imagery analysis with additional red-edge indices (RTVICore, PRI, CRI, CIrededge)

---

## Metadata

| Field | Value |
|-------|-------|
| **Version** | 2.0 |
| **Date** | February 2026 |
| **Author** | Nalaquq LLC / QCORP GIS Training |
| **Script** | `scripts/landsat_water_mask.js` |
| **Module** | Remote Sensing & Water Detection |
