# Lesson 12: Understanding Raster Data - DSM, DTM, and Orthomosaics

**Duration:** 90 minutes
**Prerequisites:** Lesson 11 - Orthomosaic Processing and ArcGIS Online Integration
**Training Date Reference:** November 7, 2025

---

## Lesson Overview

This lesson explores the different types of raster data products created from drone imagery, with focus on orthomosaics, Digital Surface Models (DSM), and Digital Terrain Models (DTM). You'll learn what each product represents, how they're created, and their specific applications in GIS workflows.

---

## Learning Objectives

By the end of this lesson, you will be able to:

1. Understand what raster data is and how it differs from vector data
2. Explain what an orthomosaic is and its characteristics
3. Describe Digital Surface Models (DSM) and their applications
4. Understand Digital Terrain Models (DTM) and how they differ from DSM
5. Choose the appropriate raster product for specific tasks
6. Work with elevation data in ArcGIS Online
7. Perform basic raster analysis
8. Understand resolution, accuracy, and data limitations

---

## Introduction to Raster Data

### What is Raster Data?

**Definition:**
Raster data represents geographic information as a grid of cells (pixels), where each cell contains a value.

**Characteristics:**
- **Grid structure:** Rows and columns of cells
- **Cell size (resolution):** Physical size each pixel represents
- **Cell values:** Numbers representing something (elevation, color, temperature)
- **Extent:** Geographic area covered
- **Coordinate system:** How the grid is positioned on Earth

**Raster vs. Vector:**

| Raster | Vector |
|--------|--------|
| Grid of pixels | Points, lines, polygons |
| Good for continuous data | Good for discrete features |
| Fixed resolution | Scalable |
| File size based on extent | File size based on complexity |
| Examples: Imagery, elevation | Examples: Roads, boundaries |

**Drone-Derived Rasters:**
- Orthomosaic (RGB imagery)
- Digital Surface Model (DSM) - elevations
- Digital Terrain Model (DTM) - ground elevations
- Thermal imagery (temperature values)

---

## Orthomosaics

### What is an Orthomosaic?

**Definition:**
An orthomosaic (or orthophoto) is a geometrically corrected aerial photograph where perspective distortion has been removed, making it like a map.

**Key Characteristics:**

1. **Orthogonal (straight down view):**
   - No perspective effects
   - Buildings don't lean
   - Uniform scale across image

2. **Georeferenced:**
   - Tied to real-world coordinates
   - Can overlay with other GIS data
   - Accurate spatial positioning

3. **Mosaicked:**
   - Stitched from many individual images
   - Seamless appearance
   - Single continuous image

4. **Corrected:**
   - Lens distortion removed
   - Elevation effects compensated
   - True measurements possible

### Orthomosaic from Grocery Store Mission

**Specifications:**
- **Resolution (GSD):** ~0.5-0.7 inches per pixel at 200ft altitude
- **Coverage:** Grocery store and surrounding area
- **Size:** ~8-12 GB (depends on compression)
- **Format:** GeoTIFF (Cloud Optimized GeoTIFF ideal)
- **Created from:** ~1000 images with 80/80 overlap

**What It Shows:**
- ✅ Building roofs (color, condition, features)
- ✅ Ground features (parking, vehicles, vegetation)
- ✅ Infrastructure (paths, utilities visible)
- ✅ True colors (RGB imagery)
- ❌ Under overhangs or trees (shadows)
- ❌ Vertical surfaces (walls)

### Orthomosaic Applications

**Infrastructure Documentation:**
- Building condition assessment
- Roof inspections
- Asset inventory
- Facility planning

**Mapping and Measurement:**
- Base maps for GIS
- Distance and area measurements
- Feature digitizing
- Planning and design

**Change Detection:**
- Compare different time periods
- Track development
- Monitor erosion
- Document damage

**Communication:**
- Visual context for stakeholders
- Community engagement
- Grant applications
- Public information

**Quinhagak Applications:**
- Document community infrastructure
- Support land use planning
- Track coastal changes
- Cultural site documentation

---

## Digital Surface Models (DSM)

### What is a DSM?

**Definition:**
A Digital Surface Model represents the elevation of the Earth's surface including all objects on it (buildings, trees, vehicles).

**Characteristics:**

1. **Elevation Values:**
   - Each pixel contains height above reference (sea level or datum)
   - Values in feet or meters
   - Typically stored as 32-bit floating point

2. **Includes Everything:**
   - ✅ Buildings
   - ✅ Trees and vegetation
   - ✅ Vehicles
   - ✅ Ground
   - = Top surface of visible features

3. **Created from:**
   - Photogrammetry (our method)
   - LiDAR
   - Radar
   - Aerial photography

### DSM from Grocery Store Mission

**What It Contains:**
- Elevation of grocery store roof
- Height of trees behind store
- Ground elevation where visible
- Vehicles in parking lot
- All surfaces visible from above

**Uses:**
- **Building heights:** Calculate from ground to roof
- **Volume calculations:** Stockpiles, excavations
- **Viewshed analysis:** What's visible from where
- **3D visualization:** Drape imagery over surface
- **Flood modeling:** Water flow over surfaces
- **Solar analysis:** Roof orientation and shading

### Visualizing DSM Data

**Display Methods:**

1. **Hillshade:**
   - Simulated shadows
   - Makes elevation differences visible
   - Good for visualization

2. **Color Ramp:**
   - Colors represent elevation
   - Low = blue/green
   - High = yellow/red
   - Quantitative display

3. **Contour Lines:**
   - Lines of equal elevation
   - Traditional topographic display
   - Can be generated from DSM

**In ArcGIS Online:**
- Apply symbology to elevation layer
- Use stretch renderer
- Create hillshade effect
- Combine with orthomosaic for context

---

## Digital Terrain Models (DTM)

### What is a DTM?

**Definition:**
A Digital Terrain Model (also called DEM - Digital Elevation Model) represents the "bare earth" surface, with buildings, trees, and other objects removed.

**Key Difference from DSM:**
- **DSM:** Includes everything (trees, buildings)
- **DTM:** Just the ground surface

**Characteristics:**

1. **Bare Earth:**
   - Buildings removed
   - Trees/vegetation removed
   - Natural ground surface
   - Also called "bald earth"

2. **How It's Created:**
   - Classification of point cloud
   - Identify ground points
   - Filter out non-ground points
   - Interpolate ground surface

3. **More Processing:**
   - Requires point cloud classification
   - More complex than DSM
   - May need manual editing
   - Not always produced automatically

### DTM Applications

**Hydrology:**
- Water flow direction
- Watershed delineation
- Flood modeling
- Drainage analysis

**Engineering:**
- Cut and fill calculations
- Road design
- Site grading
- Excavation planning

**Environmental:**
- Erosion modeling
- Habitat analysis
- Slope stability
- Coastal processes

**Planning:**
- Buildable area identification
- Slope analysis
- Line-of-sight analysis
- Terrain characterization

### DTM vs DSM: Practical Example

**Scenario:** Grocery Store Area

**DSM Shows:**
- Grocery store roof at 25 feet
- Trees behind store at 30 feet
- Ground at parking lot at 5 feet
- Vehicle tops at 10 feet

**DTM Shows:**
- Ground under store at 5 feet
- Ground under trees at 8 feet
- Ground at parking lot at 5 feet
- Ground under vehicles at 5 feet

**Use Case Examples:**

**Need DSM:**
- Building height calculation
- Solar panel placement
- Line of sight analysis
- Vegetation height

**Need DTM:**
- Natural ground slope
- Water flow patterns
- Foundation depth
- Cut/fill volumes for construction

---

## Working with Raster Data in ArcGIS Online

### Loading Elevation Data

**Add DSM to Map:**

1. **From Content:**
   - Navigate to Content
   - Find DSM layer (if published separately)
   - Add to map

2. **From Site Scan:**
   - Access Site Scan project
   - Export DSM to ArcGIS Online
   - Similar process to orthomosaic

3. **Configure Display:**
   - Choose appropriate symbology
   - Set elevation color ramp
   - Adjust transparency
   - Add hillshade effect

### Basic Raster Analysis

**Measurement Tools:**

1. **Elevation Profile:**
   - Draw line across area
   - View elevation change along line
   - Identify high/low points
   - Calculate slopes

2. **Viewshed:**
   - Determine what's visible from point
   - Used for tower placement
   - Communication planning
   - Visual impact assessment

3. **Slope Analysis:**
   - Calculate slope steepness
   - Identify steep areas
   - Plan access routes
   - Erosion risk assessment

**Analysis Examples for Grocery Store:**

1. **Building Height:**
   - Sample DSM at roof
   - Sample ground near building
   - Calculate difference = height

2. **Drainage:**
   - Analyze DSM slope
   - Identify low points
   - Plan water management

3. **Access:**
   - Calculate slopes around building
   - Identify accessible routes
   - ADA compliance check

---

## Resolution and Accuracy

### Understanding Resolution (GSD)

**Ground Sample Distance (GSD):**
- Size of one pixel on the ground
- Lower number = higher resolution = more detail

**Flight Altitude Effect:**
- **100 ft:** ~0.25-0.35 inches/pixel (very high detail)
- **200 ft:** ~0.5-0.7 inches/pixel (high detail) ← Grocery Store
- **400 ft:** ~1.0-1.4 inches/pixel (moderate detail)

**Trade-offs:**
- **Lower altitude (higher resolution):**
  - ✅ More detail
  - ✅ Better for small features
  - ❌ Smaller coverage area
  - ❌ More images needed
  - ❌ Longer flight time

- **Higher altitude (lower resolution):**
  - ✅ Larger coverage area
  - ✅ Fewer images
  - ✅ Shorter flight time
  - ❌ Less detail
  - ❌ May miss small features

### Accuracy Considerations

**Horizontal Accuracy:**
- How precisely positioned features are
- Affected by GPS quality
- Ground Control Points improve accuracy
- Typical without GCPs: 3-10 feet
- With GCPs: Sub-inch possible

**Vertical Accuracy:**
- How precise elevation measurements are
- Important for DSM/DTM
- Affected by GPS, overlap, processing
- Typical: 2-5x GSD
- For 200ft flight: ~1-3 inches vertical

**Factors Affecting Accuracy:**
- GPS signal quality (drones have good GPS)
- Overlap percentage (80/80 is excellent)
- Image quality (sharpness, lighting)
- Processing settings
- Ground Control Points (most important for precision)

**Grocery Store Mission Accuracy:**
- No ground control points (GCPs) used
- Expected horizontal: ~5-10 feet
- Expected vertical: ~2-4 inches
- Sufficient for infrastructure assessment
- Would need GCPs for surveying-grade accuracy

---

## Choosing the Right Product

### Decision Matrix

**Need Visual Information?**
→ Use Orthomosaic
- Feature identification
- Visual documentation
- Base mapping
- Communication

**Need Height Information?**
→ Use DSM
- Building heights
- Vegetation heights
- Volume calculations
- 3D visualization

**Need Bare Ground?**
→ Use DTM
- Slope analysis
- Hydrology modeling
- Cut/fill calculations
- Foundation planning

**Need Both?**
→ Combine Products
- Drape orthomosaic over DSM (3D visualization)
- Overlay orthomosaic with elevation contours
- Analysis with visual reference

### Application-Specific Recommendations

**Infrastructure Inspection:**
- Primary: Orthomosaic (visual)
- Secondary: DSM (heights, drainage)

**Site Planning:**
- Primary: DTM (ground surface)
- Secondary: Orthomosaic (context)
- Tertiary: DSM (existing structures)

**Volume Calculations:**
- Primary: DSM (for above-ground)
- Primary: DTM (for excavations)

**Change Detection:**
- Orthomosaics for visual changes
- DSMs for elevation changes
- Both for comprehensive analysis

**Community Communication:**
- Primary: Orthomosaic (easy to understand)
- Secondary: 3D visualization (orthomosaic + DSM)

---

## Data Management Best Practices

### File Formats

**GeoTIFF:**
- Standard raster format
- Georeferenced
- Widely compatible
- Large file sizes

**Cloud Optimized GeoTIFF (COG):**
- Optimized for web delivery
- Faster display
- Recommended for ArcGIS Online
- Same quality as standard GeoTIFF

**JPEG 2000:**
- High compression
- Good quality
- Smaller files
- Some compatibility issues

### Storage Considerations

**File Sizes (Typical):**
- Orthomosaic: 8-20 GB (depending on area and resolution)
- DSM: 2-5 GB
- DTM: 2-5 GB
- 3D Mesh: 5-15 GB
- Point Cloud: 20-100+ GB (very large)

**Storage Strategy:**
- Publish compressed versions to ArcGIS Online
- Keep original high-resolution files archived
- Use COG format for web delivery
- Consider tiled imagery for very large areas

---

## Review Questions

1. What is the main difference between raster and vector data?
2. What does "ortho" mean in orthomosaic?
3. How does a DSM differ from a DTM?
4. What is Ground Sample Distance (GSD)?
5. How does flight altitude affect image resolution?
6. What applications require a DTM instead of a DSM?
7. What is the approximate GSD at 200 feet altitude?
8. How can you improve the accuracy of drone-derived elevation data?

---

## Practical Exercise

**Raster Data Exploration:**

**Objective:** Work with different raster products from the grocery store mission

**Part 1: Orthomosaic Analysis (20 minutes)**
1. Open grocery store orthomosaic in ArcGIS Online
2. Measure building dimensions
3. Measure distances
4. Calculate parking lot area
5. Identify features visible in imagery

**Part 2: DSM Visualization (20 minutes)**
1. Add DSM layer to map
2. Apply elevation color ramp
3. Create hillshade visualization
4. Estimate building height
5. Identify high and low points

**Part 3: Comparison (15 minutes)**
1. Compare orthomosaic with DSM
2. Identify where they provide different information
3. Discuss which product better for specific tasks
4. Document findings

**Deliverable:** Report comparing the three products with specific use case recommendations

---

## Key Takeaways

- **Raster data represents information as grid of pixels** with values
- **Orthomosaics are corrected aerial photographs** suitable for mapping
- **DSMs include all surface features** (buildings, trees, ground)
- **DTMs show bare earth** with objects removed
- **Resolution (GSD) determined by flight altitude** - lower altitude = higher resolution
- **Each product has specific applications** - choose based on need
- **Accuracy depends on many factors** - GCPs most important for precision
- **Combine products for comprehensive analysis** (e.g., drape orthomosaic on DSM)
- **Proper data management critical** - file sizes can be large

---

## Next Steps

After completing this lesson, you now understand:
- The different raster products from drone mapping
- How to work with orthomosaics in ArcGIS Online
- The difference between DSMs and DTMs
- How to choose the right product for your needs

**Continue with:**
- [Activity: Complete Orthomosaic Mapping Mission](../activities/activity-06-first-orthomosaic.md)
- Advanced raster analysis techniques
- Multi-temporal change detection
- 3D visualization workflows

---

## Additional Resources

### Further Reading
- [ESRI: What is Raster Data?](https://desktop.arcgis.com/en/arcmap/latest/manage-data/raster-and-images/what-is-raster-data.htm)
- [Understanding DSM, DTM, and DEMs](https://www.esri.com/about/newsroom/arcuser/understanding-dsms-dtms-and-dems/)
- [Site Scan Processing Documentation](https://doc.arcgis.com/en/site-scan/)

### Tutorials
- ArcGIS Online: Working with Imagery Layers
- Site Scan: Understanding Processing Outputs
- ArcGIS Pro: Raster Analysis

---

**Module 7: Remote Sensing — Satellite Imagery & Drone Operations**
**Lesson 12: Understanding Raster Data - DSM, DTM, and Orthomosaics**
**Updated:** November 2025
