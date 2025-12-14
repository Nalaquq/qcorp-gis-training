# Lesson 8: Working with Raster Data

**Duration:** 90 minutes
**Difficulty:** Intermediate
**Prerequisites:** Lesson 2 (Adding Content)

---

## Overview

Raster data (images and surfaces) requires different handling than vector data. This comprehensive lesson teaches you to adjust imagery appearance using HSV and contrast controls, clip rasters to your study area, understand raster resolution, and work with elevation models. You'll learn the critical differences between Digital Elevation Models (DEM), Digital Surface Models (DSM), and Digital Terrain Models (DTM), and how to choose the right elevation data for your specific GIS applications.

Understanding these concepts is essential for flood modeling, viewshed analysis, infrastructure planning, and environmental monitoring in Alaska Native communities.

---

## Learning Objectives

By the end of this lesson, you will be able to:

1. ✅ Understand raster data structure (pixels/cells)
2. ✅ Adjust HSV (Hue, Saturation, Value) for imagery
3. ✅ Modify contrast and brightness
4. ✅ Clip rasters to specific extents
5. ✅ Understand and verify raster resolution
6. ✅ Combine multiple raster tiles using Mosaic to New Raster
7. ✅ Define and distinguish between DEM, DSM, and DTM
8. ✅ Identify which elevation model is appropriate for specific tasks
9. ✅ Understand how LiDAR and photogrammetry create different products
10. ✅ Recognize the implications of surface vs. terrain models for analysis

---

## Part 1: Understanding Raster Data

### What is Raster Data?

**Structure:**
- Grid of cells (pixels)
- Each cell has a value
- Regular spacing (resolution)

**Types:**
- **Imagery:** Satellite or aerial photos
- **DEMs:** Digital Elevation Models
- **Land Cover:** Classification rasters
- **Analysis Outputs:** Density, distance, suitability maps

**Resolution:**
- Cell size (e.g., 30m, 1m, 0.3m)
- Smaller = more detail
- Larger file sizes for higher resolution

---

## Part 2: Adjusting HSV (Hue, Saturation, Value)

### What is HSV?

**Hue:** Color tone
**Saturation:** Color intensity
**Value:** Brightness

### Task 2.1: Adjust Imagery Appearance

**Access:**
1. Select raster layer in Contents
2. Appearance tab on ribbon
3. Look for imagery adjustment tools

**Hue:**
- Shift: Changes color tone
- Useful for color balancing
- -180 to +180 degrees

**Saturation:**
- Intensity of color
- 0% = grayscale
- 100% = full color
- >100% = more vivid

**Value (Brightness):**
- Overall lightness/darkness
- Adjust for visibility

**Gamma:**
- Midtone brightness
- <1 = darker midtones
- >1 = lighter midtones

**When to Adjust:**
- Imagery too dark or washed out
- Color balance off
- Want to emphasize features
- Preparing for printing

---

## Part 3: Contrast and Brightness

### Contrast Stretch

**Purpose:** Enhance visual range of pixel values

**Access:**
- Select raster layer
- Appearance tab → Symbology
- Stretch type dropdown

**Stretch Types:**

**None:**
- Raw pixel values
- Often too dark or bright

**Standard Deviation:**
- Based on statistical distribution
- Good default choice
- Adjustable (1, 2, or 3 std dev)

**Min-Max:**
- Full range from minimum to maximum values
- Maximum contrast
- May lose detail in extremes

**Percent Clip:**
- Clips extreme values
- Often gives balanced result
- Default: 0.5% each end

**Histogram Equalize:**
- Redistributes values evenly
- Good for varied terrain

**Try Different Stretches:**
- Visual preference
- Depends on data and purpose
- No single "correct" answer

---

## Part 4: Clipping Rasters to Extent

### Why Clip Rasters?

**Reasons:**
- Reduce file size
- Focus on study area
- Faster processing
- Easier to share

### Task 4.1: Clip Raster to Extent

**Method 1: Clip Raster Tool**

**Access:**
- Analysis tab → Tools
- Search: "Clip Raster"

**Parameters:**

**Input Raster:**
- Imagery or raster to clip

**Output Extent:**
- Options:
  - Draw rectangle
  - Use current display extent
  - Use feature layer extent
  - Enter coordinates

**Output Raster:**
- Name and location
- Example: `Quinhagak_Imagery_Clipped.tif`

**Clipping Geometry (optional):**
- Use polygon to clip to irregular shape
- Example: Village boundary

**NoData Value:**
- Value for areas outside extent
- Often 0 or -9999

**Run:**
- Clipped raster created
- Smaller file size
- Faster to display

**Method 2: Extract by Mask**

**For irregular shapes:**
- Search: "Extract by Mask"
- Input: Raster
- Mask: Polygon feature class
- Output shaped to polygon

---

## Part 5: Understanding Resolution

### Measuring Resolution

**From Lesson 2:** Measure known features to estimate resolution

**Check Metadata:**
1. Right-click raster layer
2. Properties
3. Source tab
4. Look for:
   - Cell Size X
   - Cell Size Y
   - Shows resolution in map units

**Common Resolutions:**

| Source | Typical Resolution |
|--------|-------------------|
| Landsat | 30m |
| Sentinel-2 | 10m |
| NAIP Aerial | 1m |
| Commercial Satellite | 0.3-0.5m |
| Drone | 0.05-0.15m |

**Is Resolution Adequate?**

**For parcel mapping:** Need ~1m or better
**For vegetation:** 10-30m often adequate
**For building details:** Need 0.3-1m
**For construction:** Need <0.15m

---

## Part 6: Combining Rasters with Mosaic to New Raster

### When to Use Mosaic Raster Tool

**Purpose:**
- Combine multiple raster datasets into one seamless raster
- Merge adjacent tiles of elevation data
- Create continuous coverage from separate files

**Common Scenarios:**
- LiDAR data downloaded as multiple tiles
- DEMs split by geographic extent
- Satellite imagery in adjacent scenes
- Combining orthomosaics from separate flights

### Understanding the Mosaic to New Raster Tool

**Watch this video explanation of the Mosaic Raster function:**

[![Mosaic Raster Function Tutorial](https://img.youtube.com/vi/RV8uzf44KpM/maxresdefault.jpg)](https://www.youtube.com/watch?v=RV8uzf44KpM&t=70s)

*Click the image above to watch the tutorial on YouTube*

**Example Output - Professional Elevation Map:**

![Quinhagak LiDAR Elevation Map](../../../assets/images/Layout.jpg)

*Example of final map created from mosaicked NOAA LiDAR tiles showing Quinhagak elevation with professional cartography*

### Task 6.1: Mosaic Multiple Raster Tiles

**Access:**
1. Analysis tab → Tools
2. Search: "Mosaic to New Raster"
3. Open the tool

**Parameters:**

**Input Rasters:**
- Add all raster tiles you want to combine
- Click folder icon and select multiple files
- Example: 4 LiDAR DEM tiles for Quinhagak

**Output Location:**
- Geodatabase or folder
- Example: `C:/GIS_Projects/Quinhagak/Quinhagak.gdb`

**Raster Dataset Name:**
- Name for output mosaic
- Example: `Quinhagak_DEM_Mosaic`

**Coordinate System (optional):**
- Usually inherits from input rasters
- Verify all inputs have same projection

**Pixel Type (optional):**
- Should match input data
- For elevation: typically 32-bit floating point

**Number of Bands:**
- DEMs: 1 band
- RGB imagery: 3 bands

**Mosaic Operator:**
- **FIRST:** Uses first raster's values in overlap areas
- **LAST:** Uses last raster's values in overlap areas
- **MEAN:** Averages overlapping values (recommended for DEMs)
- **MAXIMUM:** Takes highest value
- **MINIMUM:** Takes lowest value

**For LiDAR DEMs:** Use **MEAN** to blend seamlessly

**Mosaic Colormap Mode:**
- Usually "FIRST" or "MATCH"
- Less critical for elevation data

**Run:**
- Tool creates single continuous raster
- Check output for seamless blending
- Verify no obvious tile boundaries

### Best Practices

**Before Mosaicking:**
- Ensure all inputs have same projection
- Check that cell sizes match
- Verify data types are compatible

**After Mosaicking:**
- Inspect overlap areas for artifacts
- Check that values make sense
- Compare with original tiles

**File Management:**
- Keep original tiles as backup
- Name mosaic clearly
- Document source data

---

## Part 7: Understanding Elevation Models - DEM, DSM, and DTM

### Overview of Elevation Data Types

Elevation data comes in different forms, each representing terrain differently. Understanding these differences is critical for accurate analysis in flood modeling, viewshed analysis, infrastructure planning, and environmental monitoring.

---

### Digital Elevation Model (DEM)

**Definition:**
A **DEM** (Digital Elevation Model) is a general term for any digital representation of topographic elevation.

**Key Characteristics:**
- **Generic term** covering all elevation datasets
- Can represent either surface or terrain
- Most commonly used term in GIS
- Often used interchangeably (though technically incorrect)

**Important:**
In common usage, "DEM" often specifically refers to **bare earth** elevation (equivalent to DTM), but technically it's a broader category that includes both DSM and DTM.

**Common Sources:**
- USGS National Elevation Dataset (NED)
- NOAA LiDAR collections
- SRTM (Shuttle Radar Topography Mission)
- State and regional elevation datasets

**Typical Resolution:**
- USGS DEMs: 10m, 30m
- LiDAR DEMs: 1m, 0.5m, or finer
- SRTM: 30m globally

**Applications:**
- Slope calculation
- Viewshed analysis
- Drainage modeling
- 3D visualization

---

### Digital Surface Model (DSM)

**Definition:**
A **DSM** (Digital Surface Model) represents the elevation of the **top surface** of everything - ground, buildings, trees, power lines, and all other features.

**What It Includes:**
- Ground surface
- **Building rooftops**
- **Tree canopy tops**
- **Power lines**
- **Vehicles**
- Any object above ground

**Characteristics:**
- Represents "first return" in LiDAR
- Shows what you would see from aircraft
- Includes all vertical features
- More variable elevation values

**Creation Methods:**
- **LiDAR:** First return data
- **Photogrammetry:** Structure from Motion (SfM)
- **Drone imagery:** Processed orthomosaics
- **Satellite stereo imagery:** Digital correlation

**Visual Example:**
Imagine flying over a city - a DSM shows the height of rooftops, not the ground beneath buildings.

---

### Digital Terrain Model (DTM)

**Definition:**
A **DTM** (Digital Terrain Model) represents the **bare earth surface** with vegetation, buildings, and other surface features removed.

**What It Shows:**
- Ground surface only
- Natural terrain features (hills, valleys)
- **No buildings**
- **No vegetation**
- **No power lines**

**Characteristics:**
- Represents "last return" or "ground return" in LiDAR
- Shows actual terrain beneath features
- Smoother in developed areas
- Essential for hydrologic modeling

**Creation Methods:**
- **LiDAR:** Ground-classified point cloud
- **Manual editing:** Removing features from DSM
- **Automated classification:** Algorithms identify ground points

**Visual Example:**
Imagine removing all buildings and trees - a DTM shows the ground surface as if nothing was there.

---

### Side-by-Side Comparison

**Example: Village with Buildings and Trees**

**DSM (Digital Surface Model):**
```
Elevation profile across village:
     Building    Tree      Building
        ___       /\         ___
       |   |     /  \       |   |
_______|   |____|    |______|   |________
^      ^   ^    ^    ^      ^   ^        ^
Ground shown at top of features
```

**DTM (Digital Terrain Model):**
```
Elevation profile across village:
(Same location, buildings/trees removed)

________    _________    _____________
        \  /         \  /
         \/           \/
^                                       ^
Ground shown as continuous bare earth surface
```

### Critical Differences Table

| Feature | DEM (Generic) | DSM | DTM |
|---------|---------------|-----|-----|
| **Represents** | Elevation (general) | Top surface | Bare earth |
| **Includes buildings** | Varies | ✅ Yes | ❌ No |
| **Includes vegetation** | Varies | ✅ Yes | ❌ No |
| **Use for flood modeling** | Depends | ❌ No | ✅ Yes |
| **Use for viewshed** | Depends | ✅ Yes | ❌ No |
| **Shows canopy height** | Varies | ✅ Yes | ❌ No |
| **LiDAR source** | Either | First return | Ground return |
| **Smoother surface** | Varies | ❌ No | ✅ Yes |

---

### How LiDAR Creates Different Models

**LiDAR Basics:**
- Laser pulses sent from aircraft
- Multiple returns from single pulse possible
- Returns classified by algorithm

**Return Types:**

**First Return:**
- Hits top of tallest object
- Tree canopy, building roof, power line
- Creates DSM

**Intermediate Returns:**
- Hits objects between first and ground
- Branches, lower vegetation
- Used for vegetation structure

**Last Return / Ground Return:**
- Penetrates to ground surface
- Bare earth elevation
- Creates DTM

**Standard LiDAR Classifications:**
1. **Unclassified** (default)
2. **Ground** ← Used for DTM
3. **Low vegetation** (< 0.5m)
4. **Medium vegetation** (0.5-2m)
5. **High vegetation** (> 2m)
6. **Buildings** ← Excluded from DTM
7. **Water**
8. **Noise** (outliers)

**Processing Workflow:**
1. Raw LiDAR point cloud collected
2. Automated classification algorithms run
3. Manual quality control
4. **Ground points extracted → DTM**
5. **All first returns → DSM**

---

### Photogrammetry vs LiDAR

**Photogrammetry (Drone/Aircraft):**
- Creates DSM only (surface visible in photos)
- Cannot see through vegetation
- Cannot penetrate to ground
- **Output: DSM only**

**LiDAR:**
- Laser penetrates vegetation
- Multiple returns captured
- Ground classification possible
- **Output: Both DSM and DTM**

**Important Implication:**
NOAA's 2024 Quinhagak LiDAR data can produce both DSM and DTM, while drone orthomosaic missions produce only DSM.

---

### Choosing the Right Elevation Model

**Use DSM When You Need:**

**1. Viewshed Analysis**
- What can be seen from observation point?
- Buildings and trees block views
- Need surface heights as they exist

**2. Flight Path Planning**
- Aircraft/drone must avoid obstacles
- Need actual heights of features
- Safety critical

**3. Solar Analysis**
- Building shadows matter
- Tree shading affects solar panels
- Surface features are relevant

**4. Infrastructure Clearance**
- Power line height verification
- Bridge clearance calculations
- Actual heights needed

**5. 3D City Modeling**
- Building heights required
- Realistic visualization
- Urban planning

**Example:**
*"Will the proposed cell tower be visible from the school?"* → Use DSM (trees may block view)

---

**Use DTM When You Need:**

**1. Flood Modeling**
- Water flows on ground surface
- Buildings don't affect water flow path
- Need bare earth terrain

**2. Erosion Analysis**
- Natural terrain shape matters
- Vegetation is temporary
- Ground surface drives erosion

**3. Drainage Network Mapping**
- Water follows ground surface
- Building don't divert natural flow
- Watershed delineation

**4. Archaeological Site Modeling**
- Terrain features matter
- Modern buildings are noise
- Looking for ancient landforms

**5. Contour Line Generation**
- Traditional topographic maps
- Bare earth convention
- Infrastructure planning

**6. Cut/Fill Calculations**
- Earthmoving planning
- Natural ground needed
- Construction volume estimates

**Example:**
*"Where will storm water pond during flooding?"* → Use DTM (water flows on ground, not rooftops)

---

**Use General DEM When:**

**Casual Visualization:**
- Background hillshade
- General terrain context
- Not critical which type

**No Specific Analysis:**
- Map basemap
- Reference layer
- Illustrative purposes

**Source Unclear:**
- Downloaded data without documentation
- Older datasets
- Assume it's one or the other and verify

---

### Real-World Quinhagak Examples

**Example 1: Village Relocation Planning**

**Scenario:** Planning new residential area on high ground

**Need DTM Because:**
- Foundation levels on natural ground
- Grading and earthwork on bare terrain
- Current buildings won't exist in new area
- Drainage must follow natural terrain

**Wrong Choice (DSM):**
- Would show existing building heights
- Not useful for new construction
- Misleading elevation values

---

**Example 2: Communication Tower Visibility**

**Scenario:** Proposed radio tower - which houses can receive signal?

**Need DSM Because:**
- Trees may block radio signals
- Buildings may obstruct transmission
- Actual surface features matter
- Line-of-sight analysis

**Wrong Choice (DTM):**
- Would ignore tree obstruction
- Overestimate coverage area
- Poor planning result

---

**Example 3: Storm Surge Flood Modeling**

**Scenario:** Predicting which areas flood during storm surge

**Need DTM Because:**
- Water flows on ground surface
- Buildings don't redirect water flow significantly
- Temporary features (vehicles) irrelevant
- Ground elevation determines inundation

**Wrong Choice (DSM):**
- Building heights inflate elevations
- Underestimate flood extent
- Dangerous planning error

---

**Example 4: Drone Flight Planning**

**Scenario:** Planning autonomous drone survey mission

**Need DSM Because:**
- Must avoid tall trees
- Must clear building rooftops
- Safety requires actual heights
- Collision avoidance

**Wrong Choice (DTM):**
- Would ignore obstacles
- Drone could crash into trees/buildings
- Safety failure

---

### Working with NOAA LiDAR Data

**NOAA Quinhagak 2024 Dataset**

**What NOAA Provides:**
- Raw LiDAR point cloud
- Classified point cloud
- Derived products (DEM/DTM)
- Metadata documentation

**Available Products:**

**Bare Earth DEM (DTM):**
- Ground-classified points only
- Buildings/vegetation removed
- Suitable for hydrologic analysis
- **This is what you typically download as "DEM"**

**First Surface DSM:**
- All first returns
- Includes all features
- Less commonly distributed
- May need to request specifically

**Point Cloud (LAS/LAZ):**
- Raw classified points
- Most flexible
- Requires specialized software
- Can derive custom products

---

### Identifying What You Have

**Check Metadata:**
1. Read dataset description
2. Look for "bare earth" or "ground classified"
3. Check processing methods
4. Contact data provider if unclear

**Visual Inspection:**
1. Load in ArcGIS Pro
2. Zoom to known building location
3. **If building visible as elevation bump:** DSM
4. **If building area smooth/flat:** DTM
5. Compare with imagery

**Elevation Profile Test:**
1. Create elevation profile across village
2. Look for building-shaped elevation spikes
3. **Spikes present:** DSM
4. **Relatively smooth:** DTM

---

### Hillshade Visualization

**Makes elevation data easier to interpret:**

**Access:**
- Select DEM/DTM layer
- Appearance tab → Symbology
- Choose "Hillshade"

**Parameters:**
- Azimuth: Sun direction (default 315°)
- Altitude: Sun angle above horizon (default 45°)
- Z Factor: Vertical exaggeration

**Result:**
- 3D-looking terrain
- Easy to see landforms
- Better than raw elevation values

---

### File Naming Conventions

**Be Specific in Your Naming:**

**Good:**
- `Quinhagak_DTM_2024_NOAA.tif`
- `Quinhagak_DSM_Drone_Nov2025.tif`
- `Kuskokwim_BarEarth_DEM_1m.tif`

**Unclear:**
- `Elevation.tif`
- `DEM.tif`
- `Quinhagak.tif`

---

### Documentation Best Practices

**Always Record:**
- Source agency and date
- Product type (DSM, DTM, or uncertain)
- Resolution
- Vertical datum
- Processing methods if known
- Intended use

**Metadata Template:**
```
Dataset: Quinhagak Elevation
Type: DTM (Bare Earth)
Source: NOAA 2024 LiDAR Collection
Resolution: 1 meter
Vertical Datum: NAVD88
Horizontal: NAD83 Alaska Albers
Downloaded: 2025-12-13
Purpose: Flood modeling and relocation planning
```

---

### Common Mistakes to Avoid

**1. Using DSM for Flood Modeling**
- **Error:** Water appears to flow over buildings
- **Result:** Underestimate flood extent
- **Fix:** Use DTM

**2. Using DTM for Viewshed**
- **Error:** Ignoring tree/building obstruction
- **Result:** Overestimate visibility
- **Fix:** Use DSM

**3. Assuming DEM Means DTM**
- **Error:** "DEM" used generically
- **Result:** Wrong model for analysis
- **Fix:** Verify which type

**4. Mixing DSM and DTM**
- **Error:** Combining different models
- **Result:** Inconsistent analysis
- **Fix:** Use same model type throughout

---

## Part 8: Raster vs Vector

### When to Use Each

**Raster:**
- Continuous surfaces (elevation, temperature)
- Imagery and photos
- Analysis outputs (density, cost distance)
- Large regional datasets

**Vector:**
- Discrete features (buildings, roads, parcels)
- Precise boundaries
- Attribute-rich data
- Network analysis

**Often Use Together:**
- Vector features on raster basemap
- Extract raster values to vector points
- Clip raster by vector boundary

---

## Part 9: Practical Exercises

### Exercise 1: Imagery Enhancement and Clipping

**Goal:** Prepare Quinhagak imagery for analysis

**Tasks:**

1. **Add Imagery:**
   - Add Quinhagak satellite or aerial imagery

2. **Check Resolution:**
   - Properties → Source → Cell Size
   - Record resolution
   - Verify adequate for your purpose

3. **Adjust Appearance:**
   - Try different contrast stretches
   - Adjust brightness if needed
   - Modify saturation for better visibility
   - Find best visualization

4. **Clip to Village:**
   - Use Clip Raster tool
   - Extent: Quinhagak boundary polygon
   - Create clipped output

5. **Compare:**
   - Original vs clipped file size
   - Display performance
   - Appearance

**Deliverable:**
- Well-displayed imagery
- Clipped to study area
- Optimized for analysis
- Documented resolution

---

### Exercise 2: Identifying Elevation Model Type

**Goal:** Determine whether you have a DSM or DTM

**Tasks:**

1. **Load Elevation Data:**
   - Add NOAA Quinhagak LiDAR elevation data
   - Add corresponding imagery as reference

2. **Visual Inspection:**
   - Zoom to an area with known buildings
   - Apply hillshade symbology
   - Look for building-shaped elevation patterns

3. **Check Metadata:**
   - Open layer properties
   - Check source information
   - Look for "bare earth," "ground classified," or "surface" indicators

4. **Create Elevation Profile:**
   - Draw a line across buildings
   - Generate elevation profile
   - Analyze for elevation spikes at building locations

5. **Document Findings:**
   - Identify model type (DSM or DTM)
   - Record in metadata template
   - Note implications for analysis

**Deliverable:**
- Confirmed elevation model type
- Completed metadata documentation
- Understanding of appropriate uses

---

### Exercise 3: Knowledge Check Scenarios

**Goal:** Practice choosing the right elevation model

**Scenarios to Analyze:**

1. **Planning new water/sewer infrastructure routes**
   - Which model? _______
   - Why? _______________________

2. **Assessing visibility of new clinic from residential area**
   - Which model? _______
   - Why? _______________________

3. **Modeling coastal erosion patterns**
   - Which model? _______
   - Why? _______________________

4. **Planning helicopter landing approach paths**
   - Which model? _______
   - Why? _______________________

5. **Calculating excavation volumes for new foundation**
   - Which model? _______
   - Why? _______________________

**Answers:**
1. DTM - Infrastructure follows ground surface
2. DSM - Buildings and trees affect line of sight
3. DTM - Natural terrain drives erosion
4. DSM - Must avoid all obstacles
5. DTM - Need natural ground elevation

---

## Summary

### Key Concepts

**Raster Data Fundamentals:**
1. **Raster Data:** Grid of cells with values
2. **HSV:** Hue, Saturation, Value adjustments
3. **Contrast Stretch:** Enhance visual range
4. **Clipping:** Reduce to study area
5. **Resolution:** Cell size determines detail
6. **Mosaic to New Raster:** Combine multiple tiles
7. **Raster vs Vector:** Different purposes

**Elevation Models:**

**DEM (Digital Elevation Model):**
- Generic term for any elevation data
- Commonly used to mean DTM
- Always verify which type you have

**DSM (Digital Surface Model):**
- Top surface of everything
- Includes buildings, trees, all features
- Use for viewshed, obstacle clearance, 3D visualization
- Created from first returns (LiDAR) or photogrammetry

**DTM (Digital Terrain Model):**
- Bare earth only
- Buildings and vegetation removed
- Use for hydrology, drainage, earthwork, terrain analysis
- Created from ground-classified LiDAR points

**LiDAR vs Photogrammetry:**
- LiDAR creates both DSM and DTM
- Photogrammetry creates DSM only
- Ground classification separates them

### Critical Choice Matrix

| Analysis Type | Use DSM | Use DTM |
|--------------|---------|---------|
| **Flood modeling** | ❌ | ✅ |
| **Viewshed** | ✅ | ❌ |
| **Drainage** | ❌ | ✅ |
| **Solar analysis** | ✅ | ❌ |
| **Earthwork** | ❌ | ✅ |
| **Flight planning** | ✅ | ❌ |
| **Erosion** | ❌ | ✅ |
| **Line-of-sight** | ✅ | ❌ |

### Common Tasks

**Imagery:**
- Adjust appearance: Appearance tab → Image controls
- Clip raster: Clip Raster or Extract by Mask tool
- Check resolution: Layer Properties → Source

**Elevation Data:**
- Hillshade visualization: Symbology → Hillshade
- Combine tiles: Mosaic to New Raster tool
- Identify model type: Visual inspection + metadata check
- Choose appropriate model for analysis

### Best Practices

**General Raster Management:**
- Clip large rasters to study area
- Adjust display for visibility
- Understand resolution limitations
- Document raster sources and dates
- Save processed rasters with clear names

**Elevation Data Management:**
1. **Always verify** what type of elevation model you have
2. **Name files clearly** to indicate DSM or DTM
3. **Document metadata** for future reference
4. **Choose the right model** for your specific analysis
5. **Understand data source** (LiDAR vs photogrammetry)
6. **Visual inspection** helps confirm model type
7. **When in doubt, ask** the data provider

**Common Mistakes to Avoid:**
- Using DSM for flood modeling → Use DTM
- Using DTM for viewshed → Use DSM
- Assuming DEM always means DTM → Verify
- Mixing DSM and DTM in same analysis → Use consistent model type

---

**Lesson Version:** 2.0 (Combined with Lesson 8b - DEM/DSM/DTM)
**Last Updated:** December 2025
**Module:** 4 - Spatial Analysis in ArcGIS Pro

---

## Additional Resources

### NOAA LiDAR Resources

**Digital Coast:**
- https://coast.noaa.gov/digitalcoast/
- LiDAR data access
- Training materials
- Processing guidance

**Understanding LiDAR:**
- Point cloud fundamentals
- Classification schemes
- Product derivation

### Professional Standards

**ASPRS LiDAR Standards:**
- American Society for Photogrammetry and Remote Sensing
- Classification standards
- Accuracy specifications

**USGS 3DEP:**
- 3D Elevation Program
- National elevation standards
- Data access
