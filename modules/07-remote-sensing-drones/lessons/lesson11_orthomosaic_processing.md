# Lesson 11: Orthomosaic Processing and ArcGIS Online Integration

**Duration:** 90 minutes
**Prerequisites:** Lesson 10 - Data Upload Workflows
**Training Date Reference:** November 7, 2025

---

## Lesson Overview

This lesson covers how uploaded drone imagery is processed into orthomosaic maps, and how to integrate these products into ArcGIS Online for analysis, sharing, and content management. You'll learn about the photogrammetry process, quality assessment, and GIS integration workflows.

---

## Learning Objectives

By the end of this lesson, you will be able to:

1. Understand the photogrammetry processing workflow
2. Configure processing settings in ESRI Site Scan
3. Monitor processing progress and review quality reports
4. Publish orthomosaics to ArcGIS Online
5. Manage drone-derived content in ArcGIS Online
6. Share orthomosaics with stakeholders
7. Integrate orthomosaics with other GIS layers
8. Understand processing times and resource requirements

---

## Understanding Photogrammetry

### What is Photogrammetry?

**Definition:**
The science of making measurements from photographs, used to create accurate 3D models and maps from 2D images.

**Structure from Motion (SfM):**
- Computer vision technique
- Analyzes multiple overlapping images
- Identifies common features between images
- Calculates 3D positions of features
- Creates 3D point cloud
- Generates orthomosaic and elevation models

**Why Overlap Matters:**
- 80/80 overlap ensures each ground point visible in multiple images
- More overlap = more accurate 3D reconstruction
- Minimum 60% needed; 70-80% optimal
- Our grocery store mission (80/80) is excellent

### From Images to Orthomosaic

**Processing Steps:**

1. **Image Loading and Analysis**
   - Import ~1000 images
   - Extract GPS coordinates from each image
   - Read camera parameters
   - Verify image quality

2. **Keypoint Detection**
   - Identify distinctive features in each image
   - Find same features across multiple images
   - Create "tie points" linking images

3. **Camera Alignment**
   - Calculate exact camera position for each image
   - Refine GPS positions
   - Create accurate 3D camera network

4. **Dense Point Cloud Generation**
   - Calculate 3D position of millions of points
   - Create detailed 3D model of surveyed area
   - Point density depends on resolution and overlap

5. **Mesh Generation**
   - Convert point cloud to continuous surface
   - Create 3D triangulated mesh
   - Texture mapping

6. **Orthomosaic Creation**
   - Project images onto 3D surface
   - Remove perspective distortion
   - Blend images seamlessly
   - Create georeferenced map

7. **Digital Surface Model (DSM)**
   - Extract elevation data
   - Create raster elevation model
   - Represents surface heights (trees, buildings, ground)

---

## Processing in ESRI Site Scan

### Initiating Processing

**After Upload Complete:**

1. **In Site Scan interface:**
   - Navigate to your project (Quinhagak Grocery Store)
   - Select flight (Grocery Store 200ft)
   - Review image coverage map

2. **Check Image Quality:**
   - Site Scan shows image locations as green dots
   - Coverage area should be complete
   - No gaps in coverage
   - All images processed successfully

3. **Configure Processing:**
   - Click "Process" or "Start Processing"
   - Select output types needed:
     - ✅ Orthomosaic (always needed)
     - ✅ Digital Surface Model (DSM)
     - ✅ 3D Mesh (optional, for visualization)
     - ⬜ Point Cloud (optional, large files)

4. **Set Processing Options:**
   - **Quality:** High (recommended for first processing)
   - **Resolution:** Auto (based on flight altitude)
   - **Coordinate System:** Choose appropriate (WGS84 or local)
   - **Output format:** GeoTIFF for orthomosaic

5. **Start Processing:**
   - Click "Process"
   - Confirm settings
   - Processing begins automatically in cloud

### Processing Time

**Factors Affecting Processing Time:**
- Number of images (~1000 = substantial)
- Resolution/quality settings
- Processing queue (other users)
- Selected outputs

**Typical Times:**
- **~1000 images at high quality:**
  - Orthomosaic: 2-4 hours
  - DSM: 1-2 hours additional
  - 3D Mesh: 1-3 hours additional
- **Total for all products:** 4-8 hours

**November 7 Grocery Store Mission:**
- 1000 images
- Estimated processing time: 4-6 hours
- Processed overnight (common practice)

### Monitoring Processing

**Site Scan Progress Indicators:**
1. Processing status: "In Progress"
2. Progress percentage
3. Current processing stage
4. Estimated time remaining

**Email Notifications:**
- Site Scan sends email when processing complete
- Includes link to results
- Notifications for errors

**What to Check:**
- Processing doesn't stall
- No error messages
- Status updates periodically

---

## Reviewing Processing Results

### Quality Assessment

**When Processing Complete:**

1. **Access Results:**
   - Return to Site Scan project
   - Flight status shows "Processed"
   - Click to view results

2. **Processing Report:**
   - Review quality report
   - Check coverage completeness
   - Note any warnings or issues
   - Review statistics

**Key Quality Metrics:**

- **Coverage:** 100% of target area covered?
- **Resolution (GSD):** Matches expectations? (~0.5-0.7" at 200ft)
- **Image count:** All 1000 images used?
- **Reprojection error:** Lower is better (< 1 pixel ideal)
- **Point density:** Higher = more detail

### Visual Inspection

**Check Orthomosaic Quality:**

1. **Zoom to different areas**
   - Grocery store building
   - Parking areas
   - Behind store
   - Edges of coverage

2. **Look for Issues:**
   - ❌ Blurry areas (motion blur)
   - ❌ Stitching artifacts (visible seams)
   - ❌ Missing coverage (gaps)
   - ❌ Incorrect alignment
   - ❌ Color inconsistencies

3. **Verify Details:**
   - ✅ Buildings sharp and clear
   - ✅ Ground features visible
   - ✅ Text readable (if present)
   - ✅ No distortion
   - ✅ Consistent color

**Grocery Store Orthomosaic:**
- Building details clear
- Roof features visible
- Area behind store well-covered
- Ground resolution excellent at 200ft
- Suitable for infrastructure analysis

---

## Publishing to ArcGIS Online

### Export from Site Scan

**Prepare for Export:**

1. **In Site Scan:**
   - Select processed orthomosaic
   - Click "Export" or "Publish"
   - Choose "ArcGIS Online" destination

2. **Configure Export:**
   - **Item name:** "Quinhagak Grocery Store Orthomosaic 2025-11-07"
   - **Description:** Add details (altitude, date, coverage)
   - **Tags:** "drone", "orthomosaic", "Quinhagak", "grocery store"
   - **Summary:** Brief description for others

3. **Publishing Options:**
   - **Publish as:** Imagery Layer (recommended)
   - **Sharing:** Start as private, share later
   - **Coordinate system:** Verify correct
   - **Format:** Cloud Optimized GeoTIFF (COG)

4. **Initiate Publication:**
   - Click "Publish to ArcGIS Online"
   - Processing may take additional time
   - Monitor progress in Site Scan

### Direct Publication

**Alternative Method:**

Site Scan can publish directly to ArcGIS Online during processing:
- Configure during processing setup
- Automatic publication when complete
- No manual export needed
- Appears in ArcGIS Online content

---

## Managing Content in ArcGIS Online

### Accessing Your Orthomosaic

**In ArcGIS Online:**

1. **Sign in** to ArcGIS Online account
2. Navigate to **"Content"** tab
3. Find orthomosaic layer:
   - "Quinhagak Grocery Store Orthomosaic 2025-11-07"
   - Type: Imagery Layer
   - From Site Scan

### Content Management

**Item Details Page:**

**Overview Tab:**
- View thumbnail
- Read/edit description
- See metadata
- Check file size
- View extent

**Settings Tab:**
- Configure caching
- Set visibility range (scale-dependent rendering)
- Optimize performance
- Delete protection

**Sharing Tab:**
- **Everyone (public)** - Anyone can access
- **Organization** - Only your ESRI org
- **Groups** - Specific groups
- **Private** - Only you

**Best Practice for Grocery Store Orthomosaic:**
- Start as **Private** during review
- Share with **specific group** for team review
- Make **Organization** level if appropriate
- Consider **Public** for community sharing

### Organizing Content

**Create Folders:**
1. In Content page, create folder structure:
   ```
   Drone Missions/
   ├── 2025-11/
   │   ├── 2025-11-07 Grocery Store
   │   └── [future missions]
   └── Archive/
   ```

2. Move orthomosaic to appropriate folder
3. Keep organized by date and location

**Use Groups:**
1. Create group: "Quinhagak Drone Mapping"
2. Add relevant team members
3. Share drone content with group
4. Collaborate and review together

---

## Working with Orthomosaics in ArcGIS Online

### Adding to Web Maps

**Create New Map:**

1. **In ArcGIS Online:**
   - Click "Map" to open Map Viewer
   - Click "Add" → "Browse Living Atlas Layers"
   - Or "Add" → "My Content"

2. **Add Orthomosaic:**
   - Search for "Grocery Store Orthomosaic"
   - Click "Add to Map"
   - Layer appears in map

3. **Configure Display:**
   - Adjust transparency (if overlaying)
   - Set visible scale range
   - Configure pop-ups
   - Reorder layers

### Comparing with Other Data

**Overlay Additional Layers:**

1. **Add Basemap:**
   - World Imagery (for before/after comparison)
   - Streets map
   - Topographic

2. **Add Vector Layers:**
   - Building footprints
   - Infrastructure points
   - Property boundaries
   - Other community data

3. **Comparison Tools:**
   - **Swipe tool:** Compare drone imagery with basemap
   - **Transparency slider:** Blend layers
   - **Time slider:** If multiple dates available

### Measurements and Analysis

**Measure Tools:**
- Distance
- Area
- Coordinates
- Elevation (if DSM available)

**Example Uses:**
- Measure building dimensions
- Calculate parking lot area
- Assess distances between features
- Verify clearances

---

## Sharing Orthomosaics

### Creating Shareable Products

**Option 1: Web Map**
1. Create web map with orthomosaic
2. Add context (title, description)
3. Configure bookmarks for key areas
4. Save and share map

**Option 2: Web App**
1. Use orthomosaic in web app
2. Add measurement tools
3. Include comparison features
4. Publish for community use

**Option 3: Story Map**
1. Embed orthomosaic in Story Map
2. Tell story of mapping mission
3. Show before/after comparisons
4. Explain findings

**Option 4: Direct Layer Sharing**
1. Share imagery layer directly
2. Recipients add to their maps
3. Suitable for technical users
4. Full access to imagery

### Sharing with Community Partners

**Considerations for Quinhagak:**
- **Tribal Council:** Share via group
- **Community members:** Create simple web app
- **Planning Department:** Share layer for analysis
- **Public:** Consider Story Map with context

**Best Practices:**
- Provide instructions for access
- Include metadata (date, resolution, coverage)
- Explain appropriate uses
- Maintain data quality

---

## Advanced Integration

### Using with ArcGIS Pro

**Download and Use Locally:**

1. In ArcGIS Pro, add orthomosaic from ArcGIS Online
2. Perform advanced analysis
3. Extract features
4. Create derivatives
5. Publish results back to Online

**Advanced Analysis:**
- Change detection
- Feature extraction
- Volume calculations
- 3D analysis

### Integration with Other ESRI Products

**ArcGIS Drone2Map:**
- Desktop processing alternative
- More control over processing
- Local processing (no cloud required)
- Outputs directly compatible

**ArcGIS Survey123:**
- Reference orthomosaic during field surveys
- Offline basemap support
- Verify features against imagery

---

## Lessons Learned from Grocery Store Mission

### Workflow Success

**What Worked Well:**
- 80/80 overlap produced excellent results
- 200ft altitude appropriate for building-scale mapping
- ~1000 images sufficient for complete coverage
- Site Scan processing straightforward
- ArcGIS Online integration seamless

**Processing Outcomes:**
- High-quality orthomosaic created
- Sufficient detail for infrastructure analysis
- Good coverage of entire target area
- No major processing issues

### Best Practices Identified

1. **Start processing immediately** after upload (don't delay)
2. **Review results carefully** before sharing
3. **Organize content** in logical folder structure
4. **Tag thoroughly** for future discovery
5. **Share incrementally** (team first, then broader)
6. **Document metadata** (date, conditions, parameters)

---

## Review Questions

1. What is photogrammetry and how does it work?
2. Why is 80/80 overlap beneficial for orthomosaic creation?
3. How long does processing typically take for 1000 images?
4. What is a Cloud Optimized GeoTIFF (COG)?
5. What are the main sharing options in ArcGIS Online?
6. How can you compare a drone orthomosaic with historical imagery?
7. What folder structure is recommended for organizing drone content?
8. What products can be created from drone imagery in Site Scan?

---

## Practical Exercise

**Orthomosaic Integration Workflow:**

**Objective:** Practice the full workflow from processing to sharing

**Scenario:** You've processed the Grocery Store orthomosaic

**Tasks:**
1. **Review Processing Results** (15 min)
   - Check quality report
   - Visually inspect orthomosaic
   - Note any issues

2. **Publish to ArcGIS Online** (10 min)
   - Configure metadata
   - Set appropriate tags
   - Publish as imagery layer

3. **Content Management** (15 min)
   - Create folder structure
   - Move orthomosaic to folder
   - Create group for sharing

4. **Create Web Map** (20 min)
   - Add orthomosaic
   - Add basemap for comparison
   - Configure swipe tool
   - Add bookmarks
   - Save map

5. **Share Appropriately** (10 min)
   - Share with test group
   - Create share link
   - Document sharing settings

**Deliverable:** Web map ready for team review

---

## Key Takeaways

- **Photogrammetry converts overlapping images** into accurate orthomosaics
- **80/80 overlap provides excellent results** for 3D reconstruction
- **Processing takes several hours** - plan accordingly
- **Site Scan integrates seamlessly** with ArcGIS Online
- **Content management is critical** - organize early and consistently
- **Multiple sharing options** available based on audience
- **Orthomosaics are powerful basemaps** for community analysis
- **Metadata and tagging** enable future discovery and use

---

## Next Lesson

[Lesson 12: Understanding Raster Data - DSM, DTM, and Orthomosaics](./lesson12_raster_data_types.md)

You'll learn about different types of raster data products created from drone imagery and their specific applications.
