# River Extraction and Temporal Analysis Tools

Automated tools for extracting river channel polygons (including braids) from binary water/land rasters and analyzing changes over time.

## Overview

This toolkit provides a complete workflow for river monitoring:

1. **Google Earth Engine** → Export binary water/land classifications
2. **Python Extraction** → Convert rasters to river polygons
3. **Temporal Analysis** → Compare multiple dates to detect changes
4. **Export** → GeoPackage/GeoJSON for ArcGIS Pro, QGIS, or web apps

## Components

### 1. `river_extraction.py`

Core module for extracting river polygons from binary rasters.

**Features:**
- Automatic water value detection
- Noise removal (isolated pixels)
- Multiple extraction methods:
  - `largest`: Extract largest water body (default)
  - `seed_point`: Extract water body containing a specific point
- Preserves all braided channels
- Morphological cleaning (optional)
- Polygon simplification
- Batch processing support

**Usage:**

```python
from river_extraction import RiverExtractor

# Single raster
extractor = RiverExtractor("WaterLand_Classification.tif")
river_gdf = extractor.extract_river(
    method='largest',
    min_size_pixels=50,
    morphology_iterations=1,
    simplify_tolerance=1.0
)
extractor.save_vector(river_gdf, "river_2024-05-01.gpkg")
```

**Command Line:**

```bash
python river_extraction.py input.tif output.gpkg
```

### 2. `river_temporal_analysis.py`

Module for comparing river geometries across multiple dates.

**Features:**
- Area change calculations
- Gain/loss detection (new water, abandoned channels)
- Channel migration distance measurements
- New channel detection (avulsion, braiding)
- Abandoned channel identification
- Comprehensive report generation

**Usage:**

```python
from river_temporal_analysis import RiverTemporalAnalyzer

# Load river polygons from multiple dates
gdfs = [gpd.read_file(f"river_{date}.gpkg") for date in dates]

# Analyze
analyzer = RiverTemporalAnalyzer(gdfs, dates)
report = analyzer.generate_report("analysis_output")
```

**Command Line:**

```bash
python river_temporal_analysis.py output_dir river1.gpkg 2024-05-01 river2.gpkg 2024-10-30
```

### 3. `river_extraction_workflow.ipynb`

Interactive Jupyter notebook demonstrating the complete workflow with visualizations.

**Includes:**
- Step-by-step extraction tutorial
- Batch processing examples
- Temporal analysis with charts
- Change detection visualization
- Export options for ArcGIS Pro / web apps

**To Use:**

```bash
jupyter notebook river_extraction_workflow.ipynb
```

## Installation

### Requirements

```bash
pip install -r requirements.txt
```

**Core dependencies:**
- rasterio (raster I/O)
- geopandas (vector processing)
- scipy (morphological operations)
- numpy, pandas (data processing)
- matplotlib (visualization)

**Optional:**
- jupyter (for notebooks)
- earthengine-api, geemap (GEE integration)
- flask (for future web app)

### ArcGIS Pro Integration

If using in ArcGIS Pro's Python environment:

1. Open **ArcGIS Pro** → **Project** → **Python** → **Python Command Prompt**
2. Install dependencies:
   ```bash
   python -m pip install rasterio geopandas scipy
   ```
3. Run scripts directly from ArcGIS Pro's Python environment

## Workflow

### Complete End-to-End Process

#### Step 1: Export from Google Earth Engine

Use `sentinel2_water_land_classification.js`:

1. Draw polygon around river
2. Select date range
3. Adjust NIR threshold
4. Click "Run Analysis"
5. Export to Google Drive
6. Download GeoTIFF files

**Recommended:** Export multiple dates (e.g., monthly) for temporal analysis.

#### Step 2: Extract River Polygons

**Option A: Single date (interactive)**

```python
from river_extraction import RiverExtractor

extractor = RiverExtractor("WaterLand_2024-05-01.tif")
river_gdf = extractor.extract_river(method='largest')
extractor.save_vector(river_gdf, "river_2024-05-01.gpkg")
```

**Option B: Batch processing (multiple dates)**

```python
from river_extraction import batch_extract_rivers

rasters = [
    "WaterLand_2024-05.tif",
    "WaterLand_2024-06.tif",
    "WaterLand_2024-07.tif",
    "WaterLand_2024-08.tif"
]

gdfs = batch_extract_rivers(rasters, "extracted_rivers")
```

#### Step 3: Temporal Analysis

```python
from river_temporal_analysis import RiverTemporalAnalyzer
import geopandas as gpd

# Load extracted rivers
gdfs = [gpd.read_file(f"extracted_rivers/{f}.gpkg") for f in files]
dates = ["2024-05-01", "2024-06-01", "2024-07-01", "2024-08-01"]

# Analyze
analyzer = RiverTemporalAnalyzer(gdfs, dates)
report = analyzer.generate_report("temporal_analysis")
```

#### Step 4: Review Results

The analysis generates:

1. **area_changes.csv**: River area over time
2. **migration_distances.csv**: Channel migration measurements
3. **change_map_*.gpkg**: Spatial change maps (gains/losses)
4. **new_channels_*.gpkg**: New channel polygons
5. **abandoned_channels_*.gpkg**: Abandoned channel polygons

Open these in **ArcGIS Pro**, **QGIS**, or visualize in Python.

## Parameter Tuning

### Extraction Parameters

| Parameter | Description | Recommended Values |
|-----------|-------------|-------------------|
| `min_size_pixels` | Remove features smaller than this | 10-100 (depends on noise level) |
| `morphology_iterations` | Fill small gaps | 0-2 (0=none, 1=light, 2=moderate) |
| `simplify_tolerance` | Simplify polygons (meters) | 0.5-2.0 (0=no simplification) |

**Tips:**
- Start with defaults (`min_size_pixels=50`, `morphology_iterations=1`, `simplify_tolerance=1.0`)
- If results include too much noise, increase `min_size_pixels`
- If small braids are missing, decrease `min_size_pixels` or `morphology_iterations`
- Use `simplify_tolerance` to reduce file size (especially for web apps)

### Temporal Analysis Parameters

| Parameter | Description | Recommended Values |
|-----------|-------------|-------------------|
| `min_area_m2` | Minimum area for new/abandoned channels | 1000-5000 m² |
| `num_samples` | Points for migration distance calculation | 100-500 |

## Use Cases

### 1. **River Avulsion Monitoring (Qanirtuuq River)**

Detect sudden channel changes that could threaten infrastructure:

```python
# Process multiple years
analyzer = RiverTemporalAnalyzer(yearly_gdfs, yearly_dates)

# Detect new channels (potential avulsion)
new_channels = analyzer.detect_new_channels(0, -1, min_area_m2=5000)

# Calculate migration toward village
migration = analyzer.calculate_migration_distance(0, -1)
print(f"Maximum migration: {migration['max_migration_m']} meters")
```

### 2. **Seasonal Water Level Changes**

Compare wet vs dry season:

```python
# May (spring breakup) vs August (low water)
changes = analyzer.detect_gains_and_losses(
    date_idx1=0,  # May
    date_idx2=2   # August
)

# Visualize seasonal inundation
change_map = analyzer.create_change_map(0, 2, "seasonal_changes.gpkg")
```

### 3. **Storm Impact Assessment**

Before/after typhoon or flood event:

```python
# Pre-storm vs post-storm
pre_storm_gdf = extractor.extract_river("pre_storm.tif")
post_storm_gdf = extractor.extract_river("post_storm.tif")

analyzer = RiverTemporalAnalyzer([pre_storm_gdf, post_storm_gdf],
                                 ["2025-09-30", "2025-10-15"])
report = analyzer.generate_report("typhoon_impact")
```

### 4. **Salmon Spawning Habitat**

Map accessible water bodies for salmon:

```python
# Extract all connected water in the river system
river_gdf = extractor.extract_river(method='largest')

# Calculate total habitat area
habitat_area_ha = river_gdf['area_m2'].sum() / 10000

# Identify side channels (braids)
side_channels = river_gdf[river_gdf['area_m2'] < threshold]
```

## Future: Flask Web Application

This toolkit is designed for easy integration into a web application.

### Planned Flask App Features:

1. **Upload Interface**: Drag-and-drop GeoTIFFs from GEE
2. **Extraction API**: Background processing of rasters
3. **Temporal Dashboard**: Interactive charts and maps
4. **Change Detection**: Visual diff between dates
5. **Export Options**: Download results as Shapefile/GeoJSON
6. **Email Alerts**: Notify when significant changes detected

### Flask App Structure (Planned):

```
flask_app/
├── app.py                 # Main Flask application
├── routes/
│   ├── upload.py          # File upload endpoints
│   ├── extraction.py      # River extraction API
│   └── analysis.py        # Temporal analysis API
├── static/
│   ├── css/
│   └── js/                # Leaflet map, charts
├── templates/
│   ├── index.html         # Upload interface
│   ├── results.html       # Extraction results
│   └── temporal.html      # Temporal analysis dashboard
└── utils/
    ├── river_extraction.py     # Import from scripts/
    └── river_temporal_analysis.py
```

**Status:** Design phase. Contributions welcome!

## Troubleshooting

### Common Issues

**1. "No water features found"**
- Check that raster has water pixels (value should be 0 or 1)
- Verify water value auto-detection: `extractor.identify_water_value()`
- Try manually specifying: `water_value=0`

**2. "Extracted polygon is wrong water body"**
- Use `seed_point` method instead of `largest`
- Click on the river in GEE Code Editor to get coordinates
- Pass coordinates: `extract_river(method='seed_point', seed_point=(lon, lat))`

**3. "Too many small noise polygons"**
- Increase `min_size_pixels` (try 100-200)
- Increase `morphology_iterations` (try 2)

**4. "Missing small braids"**
- Decrease `min_size_pixels` (try 10-20)
- Set `morphology_iterations=0` (no cleaning)

**5. "Module not found" errors**
- Ensure you're in the correct directory: `cd scripts/`
- Or add to Python path: `sys.path.append('path/to/scripts')`

## Performance Notes

- **Single raster extraction**: ~5-30 seconds (depends on size)
- **Batch processing (10 rasters)**: ~1-5 minutes
- **Temporal analysis (10 dates)**: ~30-60 seconds

**Large rasters:**
- Consider tiling or using smaller AOIs
- Increase simplify_tolerance to reduce output size
- Use GeoPackage (GPKG) instead of Shapefile (no 2GB limit)

## Contributing

This is an active project! Contributions welcome:

1. Parameter optimization for different river types
2. Additional analysis metrics
3. Visualization improvements
4. Flask web app development
5. ArcGIS Pro toolbox wrapper

## License

MIT License - Free to use, modify, and distribute

## Citation

If you use these tools in research or publications:

```
Nalaquq LLC / QCORP GIS Training. (2025). River Extraction and Temporal Analysis Tools.
Qanirtuuq River Monitoring Project, NSF CIVIC Award #2527256.
```

## Support

- GitHub Issues: [qcorp-gis-training/issues](https://github.com/Nalaquq/qcorp-gis-training/issues)
- Contact: Nalaquq LLC Training Team

---

**Last Updated:** November 2025
**Version:** 1.0.0
