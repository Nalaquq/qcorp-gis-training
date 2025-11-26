# Module 4: Spatial Analysis in ArcGIS Pro

## Working with Projections, Spatial Tools, and Advanced Analysis

**Duration:** 2-3 days
**Prerequisites:** Module 1 (ArcGIS Online Basics), Module 2 (Field Data Collection)
**Software Required:** ArcGIS Pro
**Setting:** Red Building training room
**Training Date:** October 2025

---

## Overview

This module introduces you to ArcGIS Pro and fundamental spatial analysis concepts. You'll learn how map projections work, how to manage GIS data properly, and how to use powerful spatial analysis tools to answer real-world questions about your community.

By the end of this module, you'll be able to create new features, analyze spatial relationships, apply buffers, and conduct meaningful analysis using the parcels data and other layers from Quinhagak.

---

## Real-World Scenario

**The Task:** Working with Quinhagak parcel maps and other local assets to conduct spatial analysis that supports community decision-making. You'll trace historical features from georeferenced maps, analyze distances and buffers around important sites, and investigate environmental concerns like the "rusting rivers" phenomenon affecting streams in Alaska.

**What You'll Learn:**
- Understand how projections affect your maps and measurements
- Work with AGOL assets in ArcGIS Pro
- Create new features by tracing from georeferenced maps
- Perform spatial analysis (buffers, intersect, dissolve, clip, etc.)
- Manage your data properly using geodatabases
- Investigate environmental phenomena using GIS

**Community Context:** This module builds on the assets you created in earlier modules (web maps, georeferenced maps) and brings them into ArcGIS Pro for more advanced analysis that can support land management, environmental monitoring, and community planning decisions.

---

## Learning Objectives

By the end of this module, you will be able to:

1. ✅ Understand map projections and coordinate systems
   - Explain why projections introduce distortion
   - Change coordinate systems in ArcGIS Pro
   - Understand when to use WGS84 vs State Plane
   - Consider projection impacts on handheld data collection

2. ✅ Add and manage content in ArcGIS Pro
   - Add content from ArcGIS Online (personal and organizational)
   - Download and work with raster, polygon, and line layers
   - Understand public/private sharing for hosted data
   - Measure distances and check imagery resolution

3. ✅ Organize data properly
   - Maintain consistent directory structure
   - Understand geodatabase (.gdb) structure
   - Create feature classes inside geodatabases
   - Follow data management best practices

4. ✅ Work with symbology
   - Adjust layer symbology for better visualization
   - Choose appropriate color palettes
   - Modify transparency to see multiple layers
   - Style parcels and other community data

5. ✅ Create new features
   - Create point, line, and polygon feature classes
   - Trace features from georeferenced maps
   - Digitize historical features (old buildings, infrastructure)
   - Edit attribute tables

6. ✅ Perform spatial analysis
   - Create buffers around features
   - Dissolve overlapping buffers
   - Use intersect tools (pairwise intersect)
   - Apply clip, erase, merge, and spatial join operations
   - Understand when to use each tool

7. ✅ Create and manage layers
   - Create new feature classes in geodatabases
   - Choose appropriate geometry types
   - Configure attribute fields
   - Understand feature classes vs shapefiles

8. ✅ Use edit tools effectively
   - Merge multiple features into one
   - Split features into separate parts
   - Extend lines to connect features
   - Clean GPS data for analysis

9. ✅ Work with attribute fields and geometry
   - Add new fields to existing layers
   - Calculate geometry (length, area) in specific units
   - Prepare accurate measurements for applications
   - Understand coordinate system impacts

10. ✅ Work with raster data
    - Adjust HSV (Hue, Saturation, Value) and contrast
    - Clip rasters to specific extents
    - Understand raster resolution through measurement

11. ✅ Export and share results
    - Export layers, shapefiles, and packages
    - Upload results to ArcGIS Online
    - Understand different export formats

---

## Module Contents

### 📖 Lessons

1. [**Projections and Coordinate Systems**](./lessons/lesson1_projections.md) (90 min)
   - The balloon activity: understanding projection distortion
   - Changing coordinate systems in Map Properties
   - Visualizing projection changes on basemaps
   - Alaska State Plane zones and EPSG codes
   - WGS84 and handheld devices

2. [**Adding Content from ArcGIS Online**](./lessons/lesson2_adding_content.md) (60 min)
   - Searching personal vs organizational content
   - Public/private sharing challenges
   - Downloading Quinhagak layers (raster, polygon, line)
   - Measuring distances and checking resolution
   - Understanding hosted data limitations

3. [**Directory Structure and Data Management**](./lessons/lesson3_data_management.md) (45 min)
   - Setting up proper folder structure
   - Understanding geodatabase (.gdb) architecture
   - Creating feature classes in geodatabases
   - Best practices for file organization
   - Why geodatabases are preferred

4. [**Symbology and Visualization**](./lessons/lesson4_symbology.md) (45 min)
   - Adjusting layer symbology
   - Working with Quinhagak Parcels color schemes
   - Using transparency effectively
   - Creating readable, professional maps
   - Color palette resources

5. [**Creating Features: Points, Lines, and Polygons**](./lessons/lesson5_creating_features.md) (90 min)
   - Creating new feature classes
   - Tracing from georeferenced maps
   - Digitizing the old FAA building
   - Mapping the old sewer lagoon
   - Outlining housing plots
   - Editing attribute tables

6. [**Buffer Analysis**](./lessons/lesson6_buffers.md) (60 min)
   - Creating buffers around features
   - Understanding buffer distances
   - Dissolving overlapping buffers
   - Pairwise intersect between buffers
   - Practical applications for community planning

7. [**Advanced Spatial Analysis Tools**](./lessons/lesson7_spatial_tools.md) (90 min)
   - Merge: combining multiple features
   - Spatial Join: transferring attributes based on location
   - Dissolve: combining features by attribute
   - Clip: extracting data to study area
   - Erase: removing areas from analysis
   - Intersect: finding overlapping areas

8. [**Working with Raster Data**](./lessons/lesson8_raster_data.md) (60 min)
   - Adjusting HSV and contrast
   - Clipping rasters to extents
   - Understanding resolution
   - Raster vs vector considerations

9. [**Graphics and Annotation**](./lessons/lesson9_graphics.md) (30 min)
   - Adding text to maps
   - Creating graphics layers
   - Annotating georeferenced maps

10. [**Exporting and Sharing**](./lessons/lesson10_exporting.md) (45 min)
    - Export as layer vs shapefile vs package
    - Uploading to ArcGIS Online
    - File type conversion (interoperability tools)
    - Time-saving export workflows

11. [**Creating Layers in ArcGIS Pro**](./lessons/lesson11_creating_layers.md) (45 min)
    - Creating new feature classes in geodatabases
    - Choosing geometry types (point, line, polygon)
    - Setting coordinate systems
    - Adding and configuring attribute fields
    - Feature classes vs shapefiles
    - Best practices for layer creation

12. [**Using Edit Tools - Merge, Split, and Extend**](./lessons/lesson12_edit_tools.md) (60 min)
    - Merging multiple features into one
    - Splitting features into separate parts
    - Extending lines to connect features
    - Cleaning GPS trail data
    - Edit tools workflow for grant applications
    - Quality assurance and troubleshooting

13. [**Creating Attribute Fields and Calculating Geometry**](./lessons/lesson13_attribute_fields_geometry.md) (60 min)
    - Adding new fields to existing layers
    - Choosing appropriate field types
    - Using Calculate Geometry for line lengths
    - Calculating lengths in miles, kilometers, meters
    - Calculating polygon areas
    - Coordinate system impacts on measurements
    - Preparing measurements for grant applications

---

## 🛠️ Hands-On Activities

### Activity 1: Understanding Projections with the Balloon Activity
**Time:** 90 minutes

**Physical Activity:**
1. Map Alaska points on an inflated balloon
2. Pop the balloon and observe distortion when flattened
3. Discuss why all 2D maps have distortion

**Digital Practice:**
1. Open ArcGIS Pro and add Alaska basemap
2. Change coordinate systems in Map Properties
3. Observe how basemap changes with different projections
4. Compare WGS84 vs Alaska State Plane zones
5. Review EPSG:26937 (Alaska State Plane Zone 7)

**Resources:**
- https://epsg.io/26937
- https://gisgeography.com/state-plane-coordinate-system-spcs/

[📋 Activity Instructions](./activities/activity-01-projections.md) | [✅ Checklist](./activities/activity-01-checklist.md)

---

### Activity 2: Adding Quinhagak Assets to ArcGIS Pro
**Time:** 60 minutes

**The Task:** Bring your AGOL web map layers into ArcGIS Pro for analysis

Steps:
1. Search personal content in ArcGIS Pro
2. Add layers from your Quinhagak web map
3. Download at least one of each:
   - Raster layer (imagery)
   - Polygon layer (parcels)
   - Line layer (roads/rivers)
4. Measure distances on the map
5. Check imagery resolution by measuring known features
6. Organize layers in table of contents

**Deliverable:** ArcGIS Pro project with Quinhagak layers properly organized

[📋 Activity Instructions](./activities/activity-02-adding-content.md)

---

### Activity 3: Setting Up Your Geodatabase
**Time:** 45 minutes

**The Task:** Create a proper directory structure and geodatabase

Steps:
1. Navigate to Documents/ArcGIS folder
2. Create project folder structure
3. Create new file geodatabase
4. Learn geodatabase advantages over shapefiles
5. Create first feature class inside geodatabase

**Deliverable:** Organized project with geodatabase structure

[📋 Activity Instructions](./activities/activity-03-geodatabase.md)

---

### Activity 4: Styling the Quinhagak Parcels Map
**Time:** 45 minutes

**The Task:** Apply professional symbology to parcels data

Steps:
1. Add Quinhagak Parcels layer
2. Choose appropriate color palette from:
   https://cdn.arcgis.com/home/item.html?id=4b2af229785e46baa31c40fadd91fcc3
3. Adjust transparency to see basemap
4. Create readable, professional-looking map
5. Save layer file for future use

**Deliverable:** Styled parcels map with appropriate transparency

[📋 Activity Instructions](./activities/activity-04-symbology.md)

---

### Activity 5: Tracing Historical Features
**Time:** 90 minutes

**The Task:** Digitize historical features from georeferenced map

Steps:
1. Create three new feature classes in geodatabase:
   - Historical_Buildings (polygon)
   - Old_Infrastructure (polygon)
   - Housing_Plots (polygon)
2. Add georeferenced Quinhagak map as basemap
3. Trace the following features:
   - Old FAA building outline
   - Old sewer lagoon
   - Several housing plots
4. Add attributes to each feature (name, year if known, notes)
5. Save edits

**Deliverable:** Geodatabase with traced historical features

[📋 Activity Instructions](./activities/activity-05-tracing.md) | [📊 Sample Output](./activities/sample-output/)

---

### Activity 6: Buffer Analysis Around Infrastructure
**Time:** 60 minutes

**The Task:** Create and analyze buffers around community features

Steps:
1. Select polygon features from Activity 5
2. Create 100m buffers around each feature
3. Create 200m buffers around each feature
4. Dissolve overlapping buffers
5. Use pairwise intersect to find overlapping buffer zones
6. Analyze results: what features are within buffer zones?

**Deliverable:** Buffer analysis showing zones of influence around historical sites

[📋 Activity Instructions](./activities/activity-06-buffers.md)

---

### Activity 7: Rusting Rivers Environmental Analysis
**Time:** 120 minutes

**Real Environmental Issue:** Alaska is experiencing a "rusting rivers" phenomenon where streams are turning orange/rust color due to permafrost thaw releasing heavy metals (particularly concerning for fish due to Cadmium).

**The Task:** Map and analyze rust-colored rivers near Quinhagak

Steps:
1. Review background information:
   - https://www.scientificamerican.com/article/why-are-alaskas-rivers-turning-orange/
   - https://www.nationalgeographic.com/environment/article/alaska-orange-rivers-rusting
2. Create feature classes:
   - Rusting_Rivers_Points (point)
   - Rusting_Rivers_Polygons (polygon)
3. Use satellite imagery to identify orange/rust-colored streams
4. Note: Near Quinhagak, this occurs in floodplain sites rather than mainstem river
5. Digitize affected stream segments
6. Add attributes:
   - Color intensity (1-5 scale)
   - Date observed
   - Location description
   - Proximity to permafrost areas
7. Create buffer zones around affected areas
8. Analyze potential impacts on subsistence fishing areas

**Deliverable:** Map showing rusting river locations with analysis of potential impacts

**Discussion Points:**
- Connection to permafrost thaw and climate change
- Heavy metal impacts on aquatic ecosystems
- Traditional knowledge about water quality changes
- Implications for subsistence fishing

[📋 Activity Instructions](./activities/activity-07-rusting-rivers.md) | [📊 Sample Analysis](./activities/sample-output/rusting-rivers/)

---

### Activity 8: Comprehensive Spatial Analysis
**Time:** 90 minutes

**The Task:** Apply multiple spatial analysis tools to answer a community question

Choose one scenario:
1. **Scenario A:** Where should a new community building be located?
   - Use clip to extract parcels in suitable area
   - Buffer existing infrastructure
   - Use intersect to find parcels meeting all criteria
   - Use erase to remove unsuitable areas (wetlands, etc.)

2. **Scenario B:** What parcels are affected by potential flooding?
   - Create flood buffer zones from rivers/streams
   - Use spatial join to identify affected parcels
   - Calculate total area at risk
   - Dissolve by land use type

3. **Scenario C:** Community infrastructure planning
   - Merge road segments
   - Buffer roads to show right-of-way
   - Clip parcels to planning area
   - Analyze accessibility

**Deliverable:** Complete analysis with map and written findings

[📋 Activity Instructions](./activities/activity-08-comprehensive-analysis.md)

---

### Activity 9: Community Placename and Trail Mapping with Search and Rescue
**Time:** 180 minutes
**Training Date:** November 20, 2025

**Real Community Session:** Work with Quinhagak Search and Rescue volunteers to document traditional Yup'ik placenames and trails using traditional knowledge and GPS data.

**The Task:** Collaborate with community knowledge holders to add placenames, import trail data from GPS devices, and identify dangerous crossings for a grant application.

Steps:
1. Review and add placenames to existing feature layer:
   - https://services6.arcgis.com/HDgSl3KvKJMed1UY/arcgis/rest/services/Quinhagak_Yuuyaraq_Place_Names/FeatureServer
2. Extract GPX trail data from Garmin devices using Basecamp
3. Convert GPX to ArcGIS layers using GPX to Features tool
4. Create dangerous crossings layer for trail safety
5. Reference ELOKA Yup'ik Atlas for additional placenames:
   - https://eloka.nsidc.org/yupik/atlas/index.html
6. Support Alaska DOT Community Trail Marking Grant application:
   - https://dot.alaska.gov/nreg/wintertrails/
7. Add placename to help NSF team mark primary channel at Uyak River

**Skills Practiced:**
- Editing hosted feature layers
- GPX to layer conversion
- Creating points, lines, and polygon features
- Integrating traditional knowledge with GIS
- Grant application support mapping

**Deliverables:**
- Updated placename layer with new traditional knowledge
- Trail layer from converted GPS data
- Dangerous crossings layer
- Grant application map for Alaska DOT

**Community Outcome:**
Following this session, SAR volunteers committed to monitoring Uyak River flow direction in spring 2026, and the data will support both the trail marking grant application and NSF research.

[📋 Activity Instructions](./activities/activity-09-placename-trail-mapping.md)

---

### Activity 10: SAR Trail Marking Grant Application
**Time:** 180 minutes

**Real-World Grant Application:** Prepare a complete GIS dataset and professional map for Alaska Department of Transportation Community Trail Marking Grant application.

![ADOT Trail Marking Grant Map](../../assets/images/ADOT%20trail%20marking%20map_page-0001.jpg)
*Example output: Professional grant map showing Eek to Goodnews Bay winter trail*

**The Task:** Use GPS trail data to create accurate trail measurements and professional grant application materials.

**Process:**
1. Review Alaska DOT grant requirements and guidelines:
   - https://dot.alaska.gov/nreg/wintertrails/
2. Set up collaborative workspace in OneDrive for team editing
3. Import and clean GPS trail data from Garmin devices
4. Use edit tools to fix GPS inaccuracies:
   - Split tool to divide trails with errors
   - Merge tool to combine corrected segments (e.g., Quinhagak to Goodnews trail)
   - Extend tool to close gaps from signal loss
5. Create new fields in attribute table for grant requirements
6. Calculate trail lengths using Calculate Geometry tool in US Survey Miles
7. Create professional grant application map following cartography principles
8. Export map as PDF for grant submission

**Skills Practiced:**
- Creating layers in ArcGIS Pro (Lesson 11)
- Using edit tools: merge, split, extend (Lesson 12)
- Adding attribute fields
- Calculating geometry in specific units (Lesson 13)
- Professional cartography and map layout
- Grant application data preparation

**Deliverables:**
- Clean trail dataset with accurate attributes
- Trail lengths calculated in US Survey Miles
- Professional grant application map (PDF)
- Complete grant application materials
- Example output: See [`assets/ADOT trail marking map.pdf`](../../assets/ADOT%20trail%20marking%20map.pdf)

**Real-World Impact:**
This activity demonstrates how GIS supports community funding applications by providing accurate, professional spatial data. The techniques learned directly support successful grant applications for community safety improvements. The example map in the assets directory shows the professional quality expected for grant submissions.

**Lessons Referenced:**
- Lesson 11: Creating Layers
- Lesson 12: Edit Tools (Merge, Split, Extend)
- Lesson 13: Attribute Fields and Calculating Geometry
- Module 5, Lesson 9: Graphics and Cartography

[📋 Activity Instructions](./activities/activity-10-sar-trail-marking-grant.md)

---

## 📚 Resources

### Official Documentation
- [ArcGIS Pro Help](https://pro.arcgis.com/en/pro-app/latest/help/main/welcome-to-the-arcgis-pro-app-help.htm)
- [Understanding Coordinate Systems](https://pro.arcgis.com/en/pro-app/latest/help/mapping/properties/coordinate-systems-and-projections.htm)
- [Geodatabase Concepts](https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/overview/what-is-a-geodatabase-.htm)
- [Geoprocessing Tools Reference](https://pro.arcgis.com/en/pro-app/latest/tool-reference/main/arcgis-pro-tool-reference.htm)

### Projections and Coordinate Systems
- [🗺️ EPSG.io - Coordinate System Database](https://epsg.io/)
- [Alaska State Plane Zone 7 (EPSG:26937)](https://epsg.io/26937)
- [State Plane Coordinate System Guide](https://gisgeography.com/state-plane-coordinate-system-spcs/)
- [Understanding Map Projections](https://www.esri.com/arcgis-blog/products/arcgis-pro/mapping/gcs_vs_pcs/)

### Spatial Analysis Tools
- [Analysis Toolbox Overview](https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/an-overview-of-the-analysis-toolbox.htm)
- [Buffer Tool](https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/buffer.htm)
- [Intersect Tool](https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/intersect.htm)
- [Dissolve Tool](https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/dissolve.htm)
- [Clip Tool](https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/clip.htm)
- [Spatial Join](https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/spatial-join.htm)

### Environmental Context
- [Alaska's Rusting Rivers - Scientific American](https://www.scientificamerican.com/article/why-are-alaskas-rivers-turning-orange/)
- [Alaska Orange Rivers - National Geographic](https://www.nationalgeographic.com/environment/article/alaska-orange-rivers-rusting)
- [Permafrost Thaw and Water Quality](https://www.usgs.gov/programs/climate-research-and-development-program/science/permafrost-and-climate-change)

### Symbology Resources
- [ArcGIS Color Palettes](https://cdn.arcgis.com/home/item.html?id=4b2af229785e46baa31c40fadd91fcc3)
- [Cartography Guidelines](https://www.esri.com/arcgis-blog/products/arcgis-pro/mapping/making-meaningful-maps/)

### Data Management
- [File Geodatabase Best Practices](https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/manage-file-gdb/file-geodatabase-size-and-name-limits.htm)
- [Organizing Data in ArcGIS Pro](https://pro.arcgis.com/en/pro-app/latest/help/projects/connect-to-a-folder.htm)

### Quick Reference
- [📄 ArcGIS Pro Keyboard Shortcuts](./resources/keyboard-shortcuts.pdf)
- [📄 Geoprocessing Tools Quick Reference](./resources/geoprocessing-quick-ref.pdf)
- [📄 Projection Decision Tree](./resources/projection-decision-tree.pdf)
- [📄 When to Use Which Spatial Tool](./resources/spatial-tools-guide.pdf)

---

## 📝 Assessment

To complete this module, you must:

1. ✅ Demonstrate understanding of map projections (Activity 1)
2. ✅ Successfully add AGOL content to ArcGIS Pro (Activity 2)
3. ✅ Create and organize a geodatabase properly (Activity 3)
4. ✅ Apply appropriate symbology to maps (Activity 4)
5. ✅ Trace and create new features from georeferenced maps (Activity 5)
6. ✅ Perform buffer analysis (Activity 6)
7. ✅ Complete rusting rivers environmental analysis (Activity 7)
8. ✅ Conduct comprehensive spatial analysis (Activity 8)
9. ✅ Complete community placename and trail mapping (Activity 9)
10. ✅ Complete SAR Trail Marking Grant application (Activity 10)
11. ✅ Submit final project and reflection document (2-3 pages)

### Final Project Options

Choose one:

**Option A: Historical Change Analysis**
- Trace historical features from georeferenced map
- Create buffers showing zones of influence
- Analyze how land use has changed over time
- Present findings to class

**Option B: Environmental Monitoring**
- Map rusting rivers or other environmental concerns
- Perform spatial analysis of affected areas
- Calculate potential impacts on subsistence resources
- Create professional map for community presentation

**Option C: Community Planning**
- Use spatial analysis tools to answer a planning question
- Apply at least 4 different geoprocessing tools
- Create decision-support maps
- Write brief report with recommendations

### Reflection Questions

1. How do different map projections affect measurements and analysis? Why does this matter for community planning?
2. What are the advantages of using a geodatabase instead of shapefiles?
3. Explain a situation where you would use each of these tools: Buffer, Intersect, Clip, Spatial Join
4. How can GIS help monitor environmental changes like the rusting rivers phenomenon?
5. What did you learn about data organization and why is it important?
6. How might traditional knowledge complement the spatial analysis you performed?
7. What spatial analysis questions would be valuable to answer for Quinhagak?

[📄 Assessment Rubric](./assessment/rubric.md) | [📤 Submission Guidelines](./assessment/submit.md)

---

## 💡 Tips for Success

### Working with Projections
- **Start with the right projection** - Choose before starting analysis
- **Match your data** - Ensure all layers use same coordinate system
- **State Plane for local accuracy** - Use Alaska State Plane for Quinhagak area analysis
- **WGS84 for field data** - Remember handheld GPS units typically use WGS84
- **Check your coordinates** - Verify you're in the right location (Alaska, not Africa!)

### Data Management
- **Save early, save often** - ArcGIS Pro can be memory intensive
- **Use geodatabases** - Faster, more features than shapefiles
- **Consistent naming** - Use clear, descriptive names without spaces
- **Organize projects** - Keep everything in project folder
- **Document your work** - Add metadata to feature classes

### Creating Features
- **Zoom in close** - Get accurate traces
- **Use proper tools** - Right-click for vertex options
- **Save edits frequently** - Don't lose work
- **Check topology** - Ensure polygons close properly
- **Add attributes** - Document what you've created

### Spatial Analysis
- **Understand the question** - What are you trying to find out?
- **Choose right tool** - Review tool descriptions carefully
- **Test on small area first** - Some operations take time
- **Check results** - Do they make sense?
- **Document process** - Keep track of parameters used

### Raster Data
- **Be patient** - Raster operations can be slow
- **Check resolution** - Measure to verify
- **Clip to study area** - Work with smaller files when possible
- **Backup originals** - Keep original data unchanged

---

## 🔧 Troubleshooting

### Common Issues

**Coordinate system problems**
- Layers not aligning properly
- Features appearing in wrong location
- Measurements seem incorrect
- [See detailed guide →](./troubleshooting/coordinate-systems.md)

**Geoprocessing tools failing**
- Invalid topology errors
- Licensing issues
- Insufficient memory
- [See detailed guide →](./troubleshooting/geoprocessing-errors.md)

**Can't edit features**
- Edit session not started
- Layer not editable
- Geodatabase locked
- [See detailed guide →](./troubleshooting/editing-issues.md)

**Performance issues**
- ArcGIS Pro running slowly
- Large raster files
- Complex operations
- [See detailed guide →](./troubleshooting/performance.md)

**Can't add AGOL content**
- Sign-in problems
- Sharing permissions
- Layer not compatible
- [See detailed guide →](./troubleshooting/agol-connectivity.md)

[📋 Full Troubleshooting Guide](./troubleshooting/README.md)

---

## 🌟 Real-World Applications

The skills from this module support:

- **Land Management** - Analyze parcel data, buffer zones, land use planning
- **Environmental Monitoring** - Track changes like rusting rivers, erosion, permafrost thaw
- **Infrastructure Planning** - Site selection, impact assessment, accessibility analysis
- **Subsistence Resources** - Analyze traditional use areas, buffer zones around sensitive sites
- **Climate Change Impacts** - Monitor and map environmental changes over time
- **Cultural Preservation** - Document and analyze traditional sites and their surroundings
- **Emergency Response** - Evacuation planning, flood zone analysis, facility accessibility
- **Community Development** - Housing planning, facility siting, service area analysis
- **Water Quality** - Monitor changes in river systems, analyze contamination potential
- **Historical Documentation** - Preserve locations of historical features through digitization

---

## Case Studies

### Case Study 1: The Balloon Activity - Understanding Projections

**Challenge:** Students struggled to understand why different coordinate systems exist and why map projections matter for their work.

**Solution:** Physical balloon activity
1. Drew Alaska outline on inflated balloon
2. Marked several Yup'ik villages as points
3. Popped balloon and laid flat
4. Observed inevitable distortion when going from 3D to 2D

**Ah-ha Moment:** When students saw they couldn't flatten the balloon without tearing or stretching it, they immediately understood why all 2D maps involve compromise and distortion.

**Technical Follow-up:**
- Demonstrated changing projections in ArcGIS Pro
- Showed how basemap shape changes with different coordinate systems
- Explained Alaska DOT uses State Plane zones (EPSG:26937) for accuracy
- Discussed WGS84 for GPS and phone applications

**Lesson Learned:** Hands-on physical activities make abstract GIS concepts concrete and memorable.

[📄 Full Case Study](./case-studies/balloon-projections.md)

---

### Case Study 2: Rusting Rivers Investigation

**Background:** Students noticed orange/rust-colored streams near Quinhagak in recent imagery and wanted to investigate.

**Environmental Context:**
- Alaska experiencing "rusting rivers" phenomenon
- Caused by permafrost thaw releasing heavy metals
- Cadmium particularly concerning for fish mortality
- Most documented cases on North Slope
- Quinhagak instances appear in floodplain rather than mainstem river

**GIS Analysis:**
1. Created point and polygon feature classes for affected streams
2. Used satellite imagery to identify rust-colored water
3. Digitized affected stream segments
4. Attributed by color intensity and location
5. Created buffers around affected areas
6. Analyzed proximity to subsistence fishing areas

**Findings:**
- Multiple instances in floodplain upstream of Quinhagak
- Different pattern than North Slope (floodplain vs mainstem)
- Potential impacts on fish habitat
- Need for water quality monitoring

**Community Impact:** Analysis helped identify areas for water quality testing and raised awareness of climate change impacts on local water systems.

**Resources Used:**
- Scientific American article
- National Geographic article
- Sentinel-2 imagery
- Traditional knowledge about water quality changes

[📄 Full Case Study](./case-studies/rusting-rivers.md)

---

### Case Study 3: Tracing Historical Features

**Challenge:** Need to preserve knowledge of old community infrastructure locations before knowledge is lost.

**Solution:** Digitize from georeferenced historical maps

**Features Traced:**
- Old FAA building (no longer standing)
- Old sewer lagoon (relocated)
- Historical housing plots

**Process:**
1. Loaded georeferenced 1970s map as basemap
2. Created polygon feature classes in geodatabase
3. Carefully traced building outlines
4. Added attributes: name, approximate year, notes from elders
5. Created buffers to show impact zones
6. Performed intersect to find current parcels affected

**Value:**
- Preserves historical knowledge
- Supports land use planning
- Helps understand site contamination potential
- Documents community development over time

[📄 Full Case Study](./case-studies/historical-features.md)

---

## 📂 Module Files

```
04-spatial-analysis-arcgis-pro/
├── README.md (this file)
├── lessons/
│   ├── lesson1_projections.md
│   ├── lesson11_creating_layers.md
│   ├── lesson12_edit_tools.md
│   └── lesson13_attribute_fields_geometry.md
│   (lessons 2-10 in development)
├── activities/
│   ├── activity-07-rusting-rivers.md
│   ├── activity-09-placename-trail-mapping.md
│   └── activity-10-sar-trail-marking-grant.md
│   (activities 1-6, 8 in development)
├── resources/
│   ├── spatial-tools-guide.md
│   └── epsg-codes-alaska.md
└── instructor-notes.md

../../assets/
├── ADOT trail marking map.pdf
└── images/
    └── ADOT trail marking map_page-0001.jpg
```

**Note:** Many lesson and activity files are placeholders in the README describing planned content. Files marked "in development" will be created as the training program progresses. Lessons 11-13 and Activity 10 support real-world grant application workflows for community trail marking projects.

---

## Additional Topics Covered

This module also touched on several additional important topics:

### Advanced Geoprocessing
- **Merge** - Combining multiple feature classes into one
- **Spatial Join** - Transferring attributes based on location
- **Dissolve** - Aggregating features by attribute
- **Clip** - Extracting data to study area boundary
- **Erase** - Removing areas from analysis

### Attribute Table Management
- Editing attribute tables
- Adding new fields
- Calculating field values
- Joining tables

### Feature Editing
- Tracing existing features
- Vertex editing
- Split and merge features
- Topology rules

### Interoperability
- Converting between file formats
- Shapefile vs geodatabase vs CAD
- Time-saving conversion workflows

### Raster Processing
- HSV adjustments for imagery
- Contrast enhancement
- Clipping to extent
- Understanding raster resolution

### Integration with Other Tools
- Google Earth Engine basics
- Exporting for web (AGOL uploads)
- Package creation for sharing

---

## Next Steps

After completing this module:

- ✨ **Continue to:** [Module 5: Cartography](../05-cartography/)
- 📚 **Practice:** Perform spatial analysis on other community features
- 🎯 **Apply:** Use these tools for real community planning questions
- 💬 **Share:** Present your rusting rivers or historical analysis to community partners
- 🔬 **Explore:** Investigate other environmental monitoring questions using GIS

---

## Instructor Notes

[📖 View instructor-specific notes and teaching tips](./instructor-notes.md)

**Key Teaching Points:**
- Physical balloon activity is critical for understanding projections
- Emphasize data organization from the start - builds good habits
- Rusting rivers activity connects GIS to real environmental concerns
- Allow time for troubleshooting - spatial tools have learning curve
- Connect analysis to community decision-making throughout
- Validate traditional knowledge alongside technical analysis

---

**Module Version:** 1.0
**Last Updated:** November 2025
**Training Date:** October 2025
**Instructor:** Sean Gleason
**Maintainer:** Nalaquq Training Team
**Location:** Quinhagak, Alaska
