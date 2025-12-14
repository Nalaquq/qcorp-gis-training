# Lesson 8b: Understanding DEM, DSM, and DTM

**Duration:** 45 minutes
**Difficulty:** Intermediate
**Prerequisites:** Lesson 8 (Raster Data)

---

## Overview

Elevation data comes in different forms, each representing terrain differently. This lesson explains the distinctions between Digital Elevation Models (DEM), Digital Surface Models (DSM), and Digital Terrain Models (DTM), helping you choose the right elevation data for your specific GIS application.

Understanding these differences is critical for accurate analysis in flood modeling, viewshed analysis, infrastructure planning, and environmental monitoring.

---

## Learning Objectives

By the end of this lesson, you will be able to:

1. ✅ Define DEM, DSM, and DTM
2. ✅ Explain the differences between these elevation data types
3. ✅ Identify which elevation model is appropriate for specific tasks
4. ✅ Understand how LiDAR and photogrammetry create different products
5. ✅ Recognize the implications of surface vs. terrain models for analysis

---

## Part 1: Elevation Model Definitions

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

## Part 2: Key Differences Illustrated

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

## Part 3: How LiDAR Creates Different Models

### LiDAR Point Cloud Returns

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

### Point Cloud Classification

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

## Part 4: Choosing the Right Elevation Model

### Use DSM When You Need:

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

### Use DTM When You Need:

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

### Use General DEM When:

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

## Part 5: Real-World Quinhagak Examples

### Example 1: Village Relocation Planning

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

### Example 2: Communication Tower Visibility

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

### Example 3: Storm Surge Flood Modeling

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

### Example 4: Drone Flight Planning

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

## Part 6: Working with NOAA LiDAR Data

### NOAA Quinhagak 2024 Dataset

**What NOAA Provides:**
- Raw LiDAR point cloud
- Classified point cloud
- Derived products (DEM/DTM)
- Metadata documentation

**Example Professional Map from NOAA LiDAR Data:**

![Quinhagak LiDAR Elevation Map](../../../assets/images/Layout.jpg)

*Professional elevation map created from mosaicked NOAA 2024 LiDAR tiles for Quinhagak - demonstrates effective use of shaded relief symbology and professional cartography*

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

## Part 7: Practical Considerations

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

## Part 8: Knowledge Check

### Questions

**1. Definition Check:**
- What does DSM stand for? _______________________
- What does DTM stand for? _______________________
- What does DEM stand for? _______________________

**2. True or False:**
- [ ] DSM includes building heights
- [ ] DTM shows tree canopy
- [ ] LiDAR can create both DSM and DTM
- [ ] Drone photogrammetry creates DTM
- [ ] DSM is better for flood modeling
- [ ] DTM is better for viewshed analysis

**3. Scenario Analysis:**

For each scenario, indicate DSM or DTM:

a) Planning new road alignment: _______
b) Calculating solar panel shading: _______
c) Identifying low-lying flood areas: _______
d) Planning cell tower placement for coverage: _______
e) Calculating earthwork volume for foundation: _______
f) Mapping line-of-sight for radio communication: _______

**4. LiDAR Understanding:**
- Which LiDAR return creates DSM? _______
- Which LiDAR return creates DTM? _______
- Can photogrammetry create DTM? _______

**5. Application:**

You're planning Quinhagak's relocation and need to:
- Model storm surge flooding
- Plan building foundations
- Assess drainage patterns
- Calculate cut/fill volumes

Which elevation model do you need? _______

Why? _______________________________________

---

## Summary

### Key Concepts

**DEM (Digital Elevation Model):**
- Generic term for any elevation data
- Commonly used to mean DTM
- Always verify which type you have

**DSM (Digital Surface Model):**
- Top surface of everything
- Includes buildings, trees, all features
- Use for viewshed, obstacle clearance, 3D visualization

**DTM (Digital Terrain Model):**
- Bare earth only
- Buildings and vegetation removed
- Use for hydrology, drainage, earthwork, terrain analysis

**LiDAR Advantage:**
- Creates both DSM and DTM
- Ground classification separates them
- Multiple returns enable separation

**Photogrammetry Limitation:**
- Creates DSM only
- Cannot see through vegetation
- Ground surface not accessible

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

### Best Practices

1. **Always verify** what type of elevation model you have
2. **Name files clearly** to indicate DSM or DTM
3. **Document metadata** for future reference
4. **Choose the right model** for your specific analysis
5. **Understand data source** (LiDAR vs photogrammetry)
6. **Visual inspection** helps confirm model type
7. **When in doubt, ask** the data provider

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

### Related Lessons

**Module 04:**
- Lesson 8: Working with Raster Data
- Activity 8: NOAA LiDAR DEM Analysis

**Module 07:**
- Lesson 12: Understanding Raster Data - DSM, DTM, and Orthomosaics
- (Drone-specific perspective on these concepts)

---

## Answers to Knowledge Check

**1. Definitions:**
- DSM: Digital Surface Model
- DTM: Digital Terrain Model
- DEM: Digital Elevation Model

**2. True/False:**
- ✅ DSM includes building heights
- ❌ DTM shows tree canopy (removed)
- ✅ LiDAR can create both DSM and DTM
- ❌ Drone photogrammetry creates DTM (creates DSM)
- ❌ DSM is better for flood modeling (DTM is correct)
- ❌ DTM is better for viewshed (DSM is correct)

**3. Scenarios:**
- a) Road alignment: DTM
- b) Solar shading: DSM
- c) Flood areas: DTM
- d) Cell tower coverage: DSM
- e) Foundation earthwork: DTM
- f) Radio line-of-sight: DSM

**4. LiDAR:**
- DSM: First return
- DTM: Ground-classified / last return
- Photogrammetry DTM: No

**5. Application:**
- Need: **DTM**
- Why: All listed tasks (flood modeling, foundations, drainage, cut/fill) require bare earth surface. Buildings and vegetation are irrelevant or misleading for these analyses.

---

**Lesson Version:** 1.0
**Last Updated:** December 2025
**Module:** 4 - Spatial Analysis in ArcGIS Pro
