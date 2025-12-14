# Activity 8: NOAA LiDAR DEM Analysis

**Duration:** 90 minutes
**Difficulty:** Intermediate
**Prerequisites:** Lesson 8 (Raster Data)

---

## Overview

In this activity, you'll work with real NOAA LiDAR data collected in Quinhagak to create professional elevation visualizations. You'll download multi-tile LiDAR datasets, combine them using the Mosaic to New Raster tool, and create compelling cartographic products using multiple symbology techniques.

This activity introduces you to high-resolution elevation data and teaches essential raster processing workflows used in professional GIS projects.

**Example Final Output:**

![Quinhagak LiDAR Elevation Map](../../../assets/images/Layout.jpg)

*Professional elevation map you'll create using NOAA 2024 LiDAR data - showing mosaicked DEM with shaded relief symbology and professional cartographic elements*

---

## Learning Objectives

By the end of this activity, you will:

1. ✅ Access and download NOAA LiDAR data from online viewers
2. ✅ Understand LiDAR data structure and file organization
3. ✅ Combine multiple raster tiles using Mosaic to New Raster
4. ✅ Apply shaded relief symbology to DEMs
5. ✅ Create classified elevation visualizations
6. ✅ Work with color ramps for effective elevation display
7. ✅ Prepare elevation data for cartographic layouts

---

## Background: NOAA LiDAR Data for Quinhagak

### What is LiDAR?

**LiDAR** (Light Detection and Ranging) is a remote sensing technology that uses laser pulses to measure distances and create highly accurate elevation models.

**How it Works:**
- Aircraft or drone emits laser pulses
- Laser reflects off ground, vegetation, buildings
- Return time calculates distance
- GPS and orientation sensors determine exact position
- Millions of points create detailed 3D surface

**LiDAR Advantages:**
- Extremely high accuracy (vertical: ±5-15cm)
- Penetrates vegetation to ground surface
- Captures fine terrain details
- Works day or night
- Dense point coverage

### NOAA's 2024 Quinhagak LiDAR Collection

**Dataset Information:**
- **Collection Date:** 2024
- **Agency:** NOAA (National Oceanic and Atmospheric Administration)
- **Coverage Area:** Quinhagak and surrounding region
- **Purpose:** Coastal mapping and flood risk assessment
- **Resolution:** High-resolution elevation data
- **Format:** GeoTIFF tiles (not normalized to ground level)

**Why This Data Matters for Quinhagak:**
- Critical for erosion monitoring
- Supports relocation planning
- Enables flood risk modeling
- Documents current terrain conditions
- Provides baseline for future change detection

**Data Access:**
- **Metadata:** https://www.fisheries.noaa.gov/inport/item/77599
- **Download Viewer:** https://coast.noaa.gov/dataviewer/#/lidar/search/where:ID=10427/details/10427

---

## Part 1: Understanding and Downloading NOAA LiDAR Data (20 minutes)

### Step 1: Review Dataset Metadata

**Watch this video introduction to the NOAA LiDAR data and mosaic workflow:**

[![NOAA LiDAR Mosaic Raster Tutorial](https://img.youtube.com/vi/RV8uzf44KpM/maxresdefault.jpg)](https://www.youtube.com/watch?v=RV8uzf44KpM&t=70s)

*Click the image above to watch the tutorial on YouTube*

**Access Metadata:**
1. Open browser to: https://www.fisheries.noaa.gov/inport/item/77599
2. Review the following information:
   - Collection date and extent
   - Vertical and horizontal accuracy
   - Coordinate system
   - Processing methods
   - Data limitations

**Document:**
- [ ] Collection date: _________________
- [ ] Coordinate system: _________________
- [ ] Vertical accuracy: _________________
- [ ] File format: _________________

### Step 2: Access NOAA Data Viewer

**Navigate to Download Interface:**
1. Open: https://coast.noaa.gov/dataviewer/#/lidar/search/where:ID=10427/details/10427
2. The viewer shows LiDAR coverage areas
3. Zoom to Quinhagak area

**Interface Overview:**
- Map shows data coverage (blue areas)
- Search tools on left
- Download options on right
- Layer controls for visualization

### Step 3: Select and Download Quinhagak Tiles

**Select Area:**
1. Use pan/zoom to focus on Quinhagak
2. Click "Data" tab
3. Select download format: **GeoTIFF**
4. Choose tiles covering Quinhagak village area

**For Quinhagak, you will typically need:**
- 4 tiles covering the village and surrounding area
- File format: `.tif` or `.tiff`
- Size: Each tile approximately 50-200 MB

**Download Process:**
1. Click on tiles to select (they highlight)
2. Add to cart
3. Review selection
4. Download files
5. Save to organized folder

**Create Project Folder:**
```
C:/GIS_Projects/Quinhagak_LiDAR/
  ├── Original_Tiles/
  │   ├── tile_01.tif
  │   ├── tile_02.tif
  │   ├── tile_03.tif
  │   └── tile_04.tif
  └── Processed/
```

**Extract Downloaded Files:**
- [ ] Unzip downloaded data
- [ ] Place `.tif` files in `Original_Tiles` folder
- [ ] Verify all tiles downloaded completely
- [ ] Record number of tiles: _______

---

## Part 2: Examining Individual Tiles in ArcGIS Pro (15 minutes)

### Step 4: Create New ArcGIS Pro Project

**New Project:**
1. Open ArcGIS Pro
2. Create new project: "Quinhagak_LiDAR_Analysis"
3. Location: `C:/GIS_Projects/Quinhagak_LiDAR/`
4. Create geodatabase: `Quinhagak_LiDAR.gdb`

### Step 5: Add Individual LiDAR Tiles

**Add Tiles:**
1. Map tab → Add Data
2. Navigate to `Original_Tiles` folder
3. Add all LiDAR `.tif` files
4. All tiles appear in Contents pane

**Examine Individual Tiles:**

**Visual Inspection:**
- Notice tiles have different extent
- Overlapping edges
- Similar gray-scale appearance (raw elevation values)
- Visible tile boundaries

**Check Tile Properties:**
1. Right-click first tile → Properties
2. Source tab → examine:
   - **Extent:** Geographic coverage
   - **Cell Size X/Y:** Resolution
   - **Coordinate System:** Should be consistent
   - **Pixel Type:** Data type (usually 32-bit float)

**Document Tile Information:**
- [ ] Cell size (resolution): _______________ meters
- [ ] Coordinate system: _______________
- [ ] Pixel type: _______________
- [ ] Number of bands: _______________

**Verify Alignment:**
- Zoom to overlap area between two tiles
- Turn layers on/off to check alignment
- Values should be similar where tiles overlap

**Why Multiple Tiles?**
- Large areas split for manageable file sizes
- Processing efficiency
- Download flexibility
- Standard practice for LiDAR distribution

---

## Part 3: Mosaicking Tiles into Single DEM (25 minutes)

### Step 6: Run Mosaic to New Raster Tool

**Why Mosaic?**
- Create seamless elevation surface
- Easier to work with single file
- Better for analysis and visualization
- Professional workflow standard

**Access Tool:**
1. Analysis tab → Tools
2. Search: "Mosaic to New Raster"
3. Open Mosaic to New Raster tool

**Tool Parameters:**

**Input Rasters:**
- Click folder icon
- Navigate to `Original_Tiles` folder
- Select all 4 (or more) `.tif` files
- All tiles appear in list

**Output Location:**
- Select: `Quinhagak_LiDAR.gdb`

**Raster Dataset Name:**
- Name: `Quinhagak_DEM_2024`

**Spatial Reference (optional):**
- Leave blank (inherits from inputs)
- Or select: NAD 1983 Alaska Albers

**Pixel Type:**
- Select: **32-bit float**
- Preserves elevation precision

**Number of Bands:**
- Enter: **1**
- (Elevation is single-band data)

**Mosaic Operator:**
- Select: **MEAN**
- Averages values in overlap areas
- Creates smooth transitions
- Best for elevation data

**Mosaic Colormap Mode:**
- Select: **FIRST**
- Not critical for elevation data

**Background Value (optional):**
- Leave blank or 0

**NoData Value (optional):**
- Leave blank

**Run Tool:**
- [ ] Click Run
- [ ] Processing time: 2-5 minutes (depending on tile size)
- [ ] New mosaic appears in Contents: `Quinhagak_DEM_2024`

**After Processing:**
1. Turn off original tile layers (uncheck)
2. View mosaicked DEM
3. Zoom across former tile boundaries
4. Verify smooth transitions (no obvious seams)

**Document:**
- [ ] Mosaic created successfully: Yes / No
- [ ] Visible tile boundaries: Yes / No
- [ ] File size of mosaic: _______________ MB

---

## Part 4: Applying Shaded Relief Symbology (20 minutes)

### Step 7: Create Shaded Relief Visualization

**Purpose:**
Shaded relief (hillshade) makes elevation data look 3-dimensional by simulating sunlight and shadows on terrain.

**Apply Shaded Relief:**
1. Select `Quinhagak_DEM_2024` in Contents
2. Appearance tab → Symbology
3. Primary Symbology dropdown → Select: **Shaded Relief**

**Shaded Relief Parameters:**

**Altitude:**
- Default: 45 degrees
- Sun angle above horizon
- Lower values = longer shadows
- Recommended: 45°

**Azimuth:**
- Default: 315 degrees (northwest)
- Direction of sunlight
- Standard cartographic convention
- Try different values to see effect

**Z Factor:**
- Default: 1
- Vertical exaggeration
- For flat terrain: try 2-5
- For mountainous: keep at 1
- Quinhagak (relatively flat): try 2-3

**Apply Settings:**
- [ ] Altitude: 45°
- [ ] Azimuth: 315°
- [ ] Z Factor: _______ (experiment!)

**Result:**
- DEM now shows 3D appearance
- Terrain features visible
- Rivers, ridges, slopes apparent

### Step 8: Apply Color Ramp to Shaded Relief

**Add Color for Visual Appeal:**

**Access Color Ramp:**
1. Still in Symbology pane
2. Under Shaded Relief settings
3. Find "Color Scheme" or "Color Ramp"
4. Click color ramp dropdown

**Select Bathymetric Color Ramp:**
- Scroll through available ramps
- Look for: **Bathymetric** color scheme
- Blues for low elevation → greens → yellows → reds for high
- Very appealing for coastal terrain

**Alternative Color Ramps:**
- Elevation #1 (brown to white)
- Terrain (green to brown)
- DEM Screen (subtle earth tones)
- Experiment with different options

**Apply:**
- [ ] Color ramp selected: _______________
- [ ] Visual appeal: Good / Excellent

**Adjust Transparency (optional):**
- Appearance tab → Effects
- Transparency slider: try 0-30%
- Useful for overlaying on imagery

---

## Part 5: Creating Classified Elevation Layer (20 minutes)

### Step 9: Duplicate DEM Layer

**Why Duplicate?**
- Keep shaded relief version for reference
- Create classified version for layout
- Different symbologies serve different purposes

**Duplicate Layer:**
1. Right-click `Quinhagak_DEM_2024` in Contents
2. Select: **Copy**
3. Right-click Map name → **Paste**
4. Rename copied layer: `Quinhagak_DEM_Classified`

**Result:**
- Two copies of same raster
- Can apply different symbology to each
- Useful for comparison

### Step 10: Apply Classify Symbology

**Change to Classify:**
1. Select `Quinhagak_DEM_Classified`
2. Appearance tab → Symbology
3. Primary Symbology dropdown → Select: **Classify**

**Classify Settings:**

**Method:**
- Dropdown shows classification methods
- Select: **Natural Breaks (Jenks)**
- Optimizes class breaks to minimize within-class variance
- Best for showing elevation zones

**Classes:**
- Default: 5 classes
- Try: 5-7 classes for elevation
- More classes = more detail
- Fewer classes = simpler interpretation

**Color Scheme:**
- Select same as shaded relief: **Bathymetric**
- Or choose complementary scheme
- Maintain color consistency

**Class Labels:**
- Automatic labels show elevation ranges
- Example: "0 - 2.5 m", "2.5 - 5.0 m", etc.
- Can customize labels if needed

**Apply Settings:**
- [ ] Method: Natural Breaks (Jenks)
- [ ] Number of classes: _______
- [ ] Color scheme: _______________

**Result:**
- DEM shows distinct elevation zones
- Clear color breaks
- Easier to reference in legend
- Professional cartographic appearance

### Step 11: Compare Symbologies

**Toggle Between Versions:**
1. Turn shaded relief layer on/off
2. Turn classified layer on/off
3. Compare visual effectiveness

**Shaded Relief:**
- Shows terrain texture
- 3D appearance
- Subtle elevation changes
- Visually appealing
- Harder to reference exact elevations

**Classified:**
- Clear elevation zones
- Easy to create legend
- Quantifiable ranges
- Better for layout reference
- Less detailed texture

**Best Practice:**
- Use shaded relief for visual maps
- Use classified for analytical layouts
- Often combine both (transparency)

---

## Part 6: Creating Map Layout (30 minutes)

### Step 12: Create Professional Layout

**Purpose:**
Create a professional map showing Quinhagak elevation data with both symbology approaches.

**Target Output - Reference This Example:**

![Quinhagak LiDAR Elevation Map Example](../../../assets/images/Layout.jpg)

*Use this professional example as a reference for your layout design - note the placement of title, legend, scale bar, and text elements*

**Create Layout:**
1. Insert tab → New Layout
2. Select: **Letter Landscape** (11" × 8.5")
3. Layout view opens

**Insert Map Frame:**
1. Insert tab → Map Frame
2. Select your map
3. Draw rectangle on layout (leave room for title, legend, text)
4. Activate map frame (double-click inside)
5. Zoom to Quinhagak area
6. Deactivate (click outside frame)

**Map Frame Settings:**
1. Right-click map frame → Properties
2. Display tab:
   - Show only `Quinhagak_DEM_Classified` layer
   - (Or shaded relief, depending on preference)
3. Border: Add 1-2 pt border

### Step 13: Add Map Elements

**Title:**
1. Insert tab → Text
2. Click on layout to place
3. Text: "Quinhagak Elevation - NOAA LiDAR 2024"
4. Font: 18-24 pt, Bold
5. Center at top

**Legend:**
1. Insert tab → Legend
2. Click to place on right side
3. Legend automatically shows DEM classes
4. Right-click legend → Properties:
   - Remove layer name if desired
   - Adjust patch sizes
   - Format text

**Scale Bar:**
1. Insert tab → Scale Bar
2. Select style
3. Place at bottom of map
4. Properties:
   - Units: Meters or Feet
   - Adjust size

**North Arrow:**
1. Insert tab → North Arrow
2. Select simple style
3. Place in corner

**Text Boxes:**
Create text boxes for:

**Data Source:**
```
Data Source: NOAA 2024 LiDAR Collection
Dataset ID: 10427
Downloaded: [today's date]
```

**Map Information:**
```
Projection: NAD 1983 Alaska Albers
Symbology: Natural Breaks Classification (Jenks)
Color Ramp: Bathymetric
```

**Your Information:**
```
Created by: [Your Name]
Date: [Today's Date]
Module 04 Activity 8
```

### Step 14: Export Map

**Export as PDF:**
1. Share tab → Export
2. Format: **PDF**
3. Output:
   - Resolution: 300 dpi
   - Quality: Best
   - Embed fonts: Yes
4. Save as: `Quinhagak_LiDAR_Elevation_Map.pdf`
5. Location: `C:/GIS_Projects/Quinhagak_LiDAR/Processed/`

**Export as PNG (optional):**
1. Share tab → Export
2. Format: **PNG**
3. Resolution: 300 dpi
4. Save as: `Quinhagak_LiDAR_Elevation_Map.png`

**Deliverables:**
- [ ] PDF map exported
- [ ] PNG map exported (optional)
- [ ] Files saved to Processed folder

---

## Part 7: Analysis and Reflection (15 minutes)

### Step 15: Measure and Analyze

**Using Classified DEM:**
1. Return to map view
2. Map tab → Measure tool
3. Measure distances and record elevations

**Record Measurements:**

**Village Core:**
- Elevation range: _______ to _______ meters
- Dominant elevation class: _______

**Highest Point in View:**
- Location: _______
- Elevation: _______ meters

**Lowest Point:**
- Location: _______
- Elevation: _______ meters

**Kuskokwim River Bank:**
- Typical elevation: _______ meters

**Observations:**
- Elevation variation across village: _______ meters
- Terrain type (flat, rolling, steep): _______
- Notable features visible in DEM: _______________________

### Step 16: Reflection Questions

**Answer the following:**

1. **Data Quality:**
   - How does LiDAR resolution compare to satellite-derived DEMs you may have seen?
   - What level of detail is visible in this dataset?

   _____________________________________________

2. **Mosaic Process:**
   - Why is the "Mean" mosaic operator appropriate for LiDAR DEMs?
   - What might happen if you used "Maximum" instead?

   _____________________________________________

3. **Symbology Comparison:**
   - Which symbology (shaded relief vs. classified) is more useful for:
     - Understanding terrain shape? _____________
     - Identifying flood risk zones? _____________
     - Creating legends? _____________

4. **Community Applications:**
   - How could this elevation data support Quinhagak's relocation planning?
   - What other community projects might benefit from LiDAR data?

   _____________________________________________

5. **LiDAR Advantages:**
   - What are three advantages of LiDAR over traditional survey methods?

   1. _____________________________________________
   2. _____________________________________________
   3. _____________________________________________

---

## Submission Requirements

### Required Deliverables

Submit the following to your instructor:

**1. Map Products:**
- [ ] PDF map with classified elevation symbology
- [ ] Proper title, legend, scale bar, north arrow
- [ ] Data source and map information text

**2. ArcGIS Pro Project:**
- [ ] Saved project with both symbology versions
- [ ] Organized layer names
- [ ] Layout complete

**3. Reflection Responses:**
- [ ] All questions in Step 16 answered
- [ ] Measurements from Step 15 recorded
- [ ] Thoughtful analysis of results

**4. Process Documentation:**
- [ ] Screenshots of:
   - Individual tiles loaded
   - Mosaic to New Raster tool parameters
   - Shaded relief symbology settings
   - Classified symbology settings

**Optional Enhancements:**
- [ ] Create second map comparing shaded relief vs. classified
- [ ] Add Quinhagak infrastructure layers (buildings, roads)
- [ ] Create elevation profile along specific transect
- [ ] Calculate area by elevation class

---

## Assessment Rubric

### Technical Skills (60 points)

| Criteria | Points | Requirements |
|----------|--------|--------------|
| **Data Download** | 10 | All LiDAR tiles downloaded correctly |
| **Mosaic Process** | 15 | Proper parameters, successful mosaic, no tile boundaries visible |
| **Shaded Relief** | 10 | Appropriate settings, effective color ramp |
| **Classification** | 15 | Jenks method, appropriate classes, matching colors |
| **Layout** | 10 | Professional appearance, all required elements |

### Map Quality (25 points)

| Criteria | Points | Requirements |
|----------|--------|--------------|
| **Cartography** | 10 | Clear, balanced design, proper element placement |
| **Legend** | 5 | Accurate, well-formatted, easy to read |
| **Labels/Text** | 10 | Complete data source, map info, creator info |

### Analysis (15 points)

| Criteria | Points | Requirements |
|----------|--------|--------------|
| **Measurements** | 5 | Accurate measurements recorded |
| **Reflection** | 10 | Thoughtful, complete answers demonstrating understanding |

**Total: 100 points**

---

## Tips for Success

**Before You Start:**
- Ensure stable internet for downloads
- Create organized folder structure
- Verify adequate disk space (2-3 GB)

**During Download:**
- Select tiles carefully (only what you need)
- Verify complete downloads before extracting
- Keep original zipped files as backup

**Mosaicking:**
- Verify all inputs have same projection
- Use MEAN operator for smooth blending
- Inspect result for tile boundaries

**Symbology:**
- Experiment with different Z factors
- Try multiple color ramps
- Keep shaded relief and classified versions

**Layout Design:**
- Leave white space - don't crowd
- Align elements for professional appearance
- Use consistent fonts and sizes
- Proofread all text

**Common Issues:**
- Tiles won't mosaic: Check projections match
- Mosaic looks blocky: Verify MEAN operator used
- Colors look wrong: Ensure bathymetric ramp applied correctly
- Legend too large: Adjust patch sizes, remove layer name

---

## Extension Activities

### Advanced Challenges

**1. Slope Analysis:**
- Create slope map from DEM
- Identify steep erosion-prone areas
- Overlay with village infrastructure

**2. Elevation Profiles:**
- Create cross-section profiles
- Show elevation change along transects
- Useful for flood modeling

**3. Viewshed Analysis:**
- Calculate viewshed from observation points
- Determine visible areas from specific locations
- Support planning for observation towers

**4. Change Detection (if historical data available):**
- Compare 2024 LiDAR with previous datasets
- Quantify erosion or deposition
- Document terrain changes

**5. 3D Visualization:**
- Convert DEM to 3D scene
- Drape imagery over elevation
- Create flythrough animations

---

## Additional Resources

### NOAA LiDAR Data

**Dataset Metadata:**
- https://www.fisheries.noaa.gov/inport/item/77599

**Download Viewer:**
- https://coast.noaa.gov/dataviewer/#/lidar/search/where:ID=10427/details/10427

**Tutorial Video:**
- https://www.youtube.com/watch?v=RV8uzf44KpM&t=70s

### Learning Resources

**Mosaic to New Raster Tool:**
- ESRI Documentation: Search "Mosaic to New Raster"
- Understanding mosaic operators
- Best practices for large datasets

**DEM Visualization:**
- Hillshade techniques
- Color ramp selection for elevation
- Multi-directional hillshade

**LiDAR Fundamentals:**
- NOAA Digital Coast: https://coast.noaa.gov/digitalcoast/
- Understanding LiDAR returns
- Point cloud processing

---

## Summary

### What You Learned

**Technical Skills:**
- Downloading LiDAR data from NOAA viewers
- Understanding multi-tile raster datasets
- Using Mosaic to New Raster tool effectively
- Applying multiple symbology approaches
- Creating professional cartographic layouts

**Raster Concepts:**
- LiDAR data structure and organization
- Mosaic operators and their effects
- Shaded relief visualization
- Classification methods for elevation
- Color ramp selection for DEMs

**Community Applications:**
- High-resolution elevation data uses
- Supporting relocation planning
- Flood risk assessment
- Erosion monitoring
- Infrastructure planning

### Key Takeaways

1. **LiDAR provides unprecedented elevation accuracy** for community planning
2. **Mosaic tool combines tiles seamlessly** using appropriate operators
3. **Multiple symbology approaches** serve different cartographic purposes
4. **Professional layouts communicate** technical data effectively
5. **NOAA provides free, high-quality data** for Alaska communities

---

**Congratulations!** You've completed a professional LiDAR data processing workflow from download through final cartographic product. These skills are directly applicable to real community planning, grant applications, and environmental monitoring projects.

---

**Activity Version:** 1.0
**Last Updated:** December 2025
**Module:** 4 - Spatial Analysis in ArcGIS Pro
