# Activity 7: Rusting Rivers Environmental Analysis

**Duration:** 120 minutes
**Difficulty:** Intermediate to Advanced
**Prerequisites:** Lessons 1-6, Activities 1-5 completed

---

## Overview

In this activity, you'll use GIS to investigate an emerging environmental phenomenon affecting Alaska: "rusting rivers." Streams are turning orange/rust color due to permafrost thaw releasing heavy metals. This is a real environmental concern with implications for fish populations and subsistence resources.

---

## Learning Objectives

By the end of this activity, you will:

1. ✅ Research and understand a real environmental issue
2. ✅ Create feature classes for environmental monitoring
3. ✅ Use satellite imagery to identify environmental changes
4. ✅ Digitize affected stream segments
5. ✅ Apply spatial analysis to assess potential impacts
6. ✅ Create professional maps for community presentation
7. ✅ Connect GIS analysis to traditional knowledge

---

## Background: Alaska's Rusting Rivers

### The Phenomenon

In recent years, scientists have documented streams in Alaska turning bright orange/rust color. This "rusting rivers" phenomenon is:

- **Caused by:** Permafrost thaw releasing previously frozen minerals
- **Primary concern:** Heavy metals (Iron, Zinc, Cadmium, Copper, Nickel)
- **Ecological impact:** Cadmium particularly harmful to fish mortality
- **Climate connection:** Linked to Arctic warming and permafrost degradation
- **Geographic pattern:** Initially documented on North Slope, now appearing elsewhere

### Scientific Context

**Research Findings:**
- pH levels in affected streams drop (more acidic)
- Heavy metal concentrations increase dramatically
- Aquatic invertebrates show population decline
- Fish populations potentially impacted
- Clear water turns orange/brown from iron oxidation

**Key Citation:**
O'Donnell, J.A., et al. (2024). "Rapid changes in stream chemistry and biology in Arctic rivers." Various academic journals and reports.

### Media Coverage

**Scientific American Article:**
https://www.scientificamerican.com/article/why-are-alaskas-rivers-turning-orange/

Key points from article:
- First noticed around 2018 in Brooks Range
- Dozens of streams now affected
- "Looks like rust soup" - local description
- Visible from space in satellite imagery
- Implication for drinking water and subsistence

**National Geographic Coverage:**
https://www.nationalgeographic.com/environment/article/alaska-orange-rivers-rusting

Additional context:
- Impact on salmon and other fish species
- Traditional knowledge about water quality changes
- Monitoring challenges in remote areas
- Future predictions with continued warming

### Quinhagak Context

**Important Difference:**
Near Quinhagak, the rusting phenomenon appears to occur primarily in **floodplain channels** rather than mainstem rivers (unlike North Slope examples).

**Why This Matters:**
- Different ecosystem impact pattern
- May affect fish habitat differently
- Requires different monitoring approach
- Local traditional knowledge essential

---

## Part 1: Research and Planning (20 minutes)

### Step 1: Read Background Materials

Review the following resources:

1. **Scientific American Article** (20 min)
   - https://www.scientificamerican.com/article/why-are-alaskas-rivers-turning-orange/
   - Note key findings about heavy metals
   - Understand ecological impacts

2. **National Geographic Article** (20 min)
   - https://www.nationalgeographic.com/environment/article/alaska-orange-rivers-rusting
   - Focus on fish impacts
   - Note visual signatures in imagery

### Step 2: Consult Traditional Knowledge

**Discussion Questions for Elders/Community Members:**

1. Have you noticed changes in river/stream color in recent years?
2. Are there specific streams that look different now than before?
3. Have you noticed changes in fish populations or health?
4. What do you know about water quality in different areas?
5. Are there places where people used to fish but don't anymore?

**Documentation:**
- Take notes during discussions
- Mark mentioned locations on map
- Record specific observations
- Note time periods mentioned

### Step 3: Review Satellite Imagery

Before starting GIS work:
1. Look at recent Sentinel-2 or Landsat imagery of Quinhagak area
2. Scan for orange/rust colored streams
3. Note that floodplain channels are where this appears locally
4. Screenshot potential locations for reference

---

## Part 2: Setting Up Your GIS Project (15 minutes)

### Create New Project

**Step 1: Start ArcGIS Pro**
1. Create new project
2. Name: "Rusting_Rivers_Quinhagak"
3. Location: Documents/ArcGIS/
4. Template: Map

**Step 2: Set Coordinate System**
1. Right-click Map → Properties
2. Coordinate Systems tab
3. Select: NAD 1983 StatePlane Alaska 7 FIPS 5007
4. Click OK

**Step 3: Add Basemap and Quinhagak Layers**
1. Add Imagery basemap
2. Add from ArcGIS Online:
   - Quinhagak Parcels
   - Quinhagak Rivers/Streams (if available)
   - Other relevant local layers
3. Zoom to Quinhagak area
4. Save project

### Create Geodatabase

**Step 4: Create Project Geodatabase**
1. In Catalog pane, right-click project folder
2. New → File Geodatabase
3. Name: "Rusting_Rivers.gdb"
4. This will store all your analysis data

---

## Part 3: Creating Feature Classes (20 minutes)

### Create Point Feature Class

**Step 1: Create Rusting_Rivers_Points**
1. Right-click Rusting_Rivers.gdb
2. New → Feature Class
3. Name: "Rusting_Rivers_Points"
4. Type: Point
5. Coordinate System: NAD 1983 StatePlane Alaska 7
6. Click Next

**Step 2: Add Fields**

Add the following fields:

| Field Name | Data Type | Length | Description |
|------------|-----------|--------|-------------|
| Stream_Name | Text | 100 | Name of stream/location |
| Observation_Date | Date | - | When observed/mapped |
| Color_Intensity | Short Integer | - | Scale 1-5 (1=slight, 5=severe) |
| Color_Description | Text | 50 | Orange, rust, brown, etc. |
| Source | Text | 50 | Satellite, field, elder knowledge |
| Flow_Type | Text | 50 | Floodplain, mainstem, tributary |
| Subsistence_Impact | Text | 10 | High, Medium, Low, Unknown |
| Notes | Text | 255 | Additional observations |
| Observer | Text | 100 | Who documented this |

**Step 3: Create Fields**
- Add each field with appropriate settings
- Click Finish

### Create Polygon Feature Class

**Step 4: Create Rusting_Rivers_Polygons**
1. Right-click Rusting_Rivers.gdb
2. New → Feature Class
3. Name: "Rusting_Rivers_Polygons"
4. Type: Polygon
5. Same coordinate system
6. Add same fields as point layer
7. Additional field:
   - Area_sqkm (Double) - calculated area of affected zone

**Step 5: Add to Map**
- Add both new feature classes to map
- Set different symbols (points as circles, polygons as semi-transparent fill)

---

## Part 4: Identifying Affected Streams (30 minutes)

### Using Satellite Imagery

**Step 1: Load Current Imagery**
1. In ArcGIS Pro, add Living Atlas imagery:
   - Search "Sentinel-2" in Living Atlas
   - Or add Landsat imagery
   - Filter to most recent clear-sky imagery
   - Focus on summer months (less snow)

**Step 2: Scan for Orange/Rust Colored Water**

**Visual Indicators:**
- Bright orange color in stream channels
- Rust/brown coloration
- Contrast with normal blue/clear water
- Often more visible in shallow areas

**Where to Look (Quinhagak Context):**
- ⚠️ Focus on **floodplain channels**
- Check smaller tributaries
- Look in areas with exposed soil/banks
- Areas with permafrost presence

**Step 3: Compare with Historical Imagery**
1. Add Esri Wayback Imagery
2. Compare same locations from 3-5 years ago
3. Note any changes in water color
4. Screenshot comparisons

### Digitizing Points

**Step 4: Mark Affected Locations**

For each affected stream you identify:

1. **Start Edit Session**
   - Click Edit tab
   - Click Create
   - Select Rusting_Rivers_Points

2. **Add Point**
   - Click on affected stream location
   - Add point

3. **Fill Attributes**
   - Stream_Name: e.g., "Tributary A upstream of village"
   - Observation_Date: Today's date (or image date)
   - Color_Intensity: Rate 1-5 based on imagery
   - Color_Description: "bright orange", "rust brown", etc.
   - Source: "Sentinel-2 imagery, [date]"
   - Flow_Type: "Floodplain channel" (likely for Quinhagak)
   - Subsistence_Impact: Your assessment
   - Notes: Any additional context
   - Observer: Your name

4. **Save Edits**
   - Click Save in Edit tab
   - Continue for all identified locations

**Target:** Identify and document at least 5-10 affected locations

### Digitizing Polygons

**Step 5: Outline Affected Stream Segments**

For larger affected areas:

1. **Switch to Polygon Tool**
   - In Create Features, select Rusting_Rivers_Polygons
   - Use Polygon tool

2. **Trace Affected Area**
   - Outline the rust-colored stream segment
   - Include entire visible affected zone
   - Be as accurate as possible

3. **Fill Attributes**
   - Same attribute fields as points
   - Area_sqkm will auto-calculate

4. **Save Edits**

**Target:** Create polygons for 3-5 major affected stream segments

---

## Part 5: Spatial Analysis (25 minutes)

### Buffer Analysis

**Objective:** Determine what areas might be impacted by contaminated water

**Step 1: Create Buffers Around Affected Streams**

1. **Open Buffer Tool**
   - Analysis tab → Tools
   - Search "Buffer"
   - Open Buffer tool

2. **Set Parameters**
   - Input Features: Rusting_Rivers_Points (or Polygons)
   - Output: Rusting_Rivers_Buffer_100m
   - Distance: 100 meters
   - Dissolve Type: None (keep individual buffers)
   - Click Run

3. **Create Additional Buffer**
   - Repeat with 500m buffer
   - Name: Rusting_Rivers_Buffer_500m
   - This represents wider potential impact zone

### Intersect with Subsistence Areas

**Step 2: Identify Affected Subsistence Resources**

If you have subsistence use area data:

1. **Spatial Join or Intersect**
   - Analysis → Tools
   - Search "Intersect" or "Spatial Join"
   - Input: Fishing areas and buffer zones
   - Output: Affected_Subsistence_Areas

2. **Analyze Results**
   - How many fishing sites within 100m of affected streams?
   - How many within 500m?
   - What species are potentially impacted?

### Distance Analysis

**Step 3: Calculate Distance to Village**

1. **Near Tool**
   - Analysis → Tools → Near
   - Input Features: Rusting_Rivers_Points
   - Near Features: Village center point
   - This adds distance field to your points

2. **Review Results**
   - Open attribute table
   - Sort by distance
   - Identify closest affected streams to village
   - Note: Closer streams = higher concern

### Watershed Analysis (Advanced)

**Step 4: Determine Drainage Patterns**

If time allows:
1. Use hydrology tools to determine flow direction
2. Identify which streams drain to subsistence fishing areas
3. Create watershed polygons for affected streams
4. Analyze downstream impacts

---

## Part 6: Creating Analysis Maps (1 hour)

### Map 1: Affected Streams Overview

**Layout:**
1. Insert → New Layout → Letter size landscape
2. Add map frame showing entire study area
3. Show:
   - All affected stream points (color by intensity)
   - All affected stream polygons
   - Buffer zones (transparent)
   - Basemap showing context

**Map Elements:**
- Title: "Rusting Rivers Near Quinhagak - [Year]"
- Legend
- Scale bar
- North arrow
- Data sources
- Your name and date

### Map 2: Close-up of Most Affected Area

**Layout:**
1. Insert → New Layout → Letter size portrait
2. Zoom to most severely affected area
3. Show:
   - Detailed imagery
   - Stream polygons
   - Color intensity labels
   - Buffer zones

**Annotation:**
- Add text labels for stream names
- Note color intensity
- Add callout boxes for key observations

### Map 3: Subsistence Impact Assessment

**Layout:**
1. Insert → New Layout → Letter size landscape
2. Show:
   - Affected streams
   - Fishing areas (if available)
   - Buffer zones intersecting fishing areas
   - Village location
   - Distance rings from village

**Analysis Notes:**
- Add text box with findings:
  - Number of affected streams identified
  - Total area of affected waterways
  - Number of subsistence areas within buffer zones
  - Recommended monitoring locations

---

## Part 7: Documentation and Reporting (30 minutes)

### Create Summary Report

**Required Sections:**

**1. Introduction**
- Brief background on rusting rivers phenomenon
- Why this matters for Quinhagak
- Study objectives

**2. Methods**
- Imagery sources and dates
- GIS methods used
- Field verification (if any)
- Traditional knowledge incorporated

**3. Findings**
- Number of affected streams identified
- Locations and severity
- Pattern observations (floodplain vs mainstem)
- Proximity to subsistence areas
- Maps showing results

**4. Discussion**
- Comparison to North Slope patterns
- Unique Quinhagak characteristics
- Potential fish and ecosystem impacts
- Climate change connection
- Traditional knowledge insights

**5. Recommendations**
- Priority areas for water quality testing
- Monitoring protocol suggestions
- Subsistence resource considerations
- Future analysis needs
- Community communication approach

**6. References**
- Scientific articles
- Imagery sources
- Community knowledge sources
- GIS data sources

### Export Final Products

**Export Maps:**
1. File → Export Layout
2. Format: PDF (high quality)
3. Save with descriptive names

**Export Data:**
1. Right-click Rusting_Rivers.gdb
2. Export → Create File Geodatabase Package
3. Include all feature classes
4. Add documentation

**Share to ArcGIS Online:**
1. Right-click feature class
2. Sharing → Share As Web Layer
3. Set appropriate permissions
4. Add to Quinhagak group (if exists)

---

## Deliverables

### Required Submissions

1. **✅ Rusting_Rivers.gdb**
   - With populated point and polygon feature classes
   - Minimum 5 documented locations
   - Complete attribute information

2. **✅ Three Professional Maps**
   - Overview map
   - Detailed close-up map
   - Subsistence impact map

3. **✅ Written Report**
   - 3-5 pages
   - All required sections
   - Maps included
   - References cited

4. **✅ Presentation File**
   - PowerPoint or PDF
   - For sharing with community
   - 5-10 slides
   - Non-technical language

### Optional Advanced Work

- **Water quality data integration** (if available)
- **Time series analysis** (compare multiple years)
- **Statistical analysis** of pattern distribution
- **3D visualization** using terrain data
- **Story Map** for public outreach
- **Mobile app** for community reporting

---

## Discussion Questions

### Analyzing Your Results

1. How many affected streams did you identify near Quinhagak?
2. Do they follow the floodplain pattern mentioned in the background?
3. How does this compare to North Slope rusting rivers?
4. What subsistence resources might be affected?

### Traditional Knowledge Integration

5. How does your GIS analysis compare to community observations?
6. What did elders know about water quality changes?
7. Are there areas of concern not visible in satellite imagery?
8. How can GIS support traditional environmental knowledge?

### Climate Change Connection

9. How might continued permafrost thaw affect this phenomenon?
10. What other environmental changes might GIS help monitor?
11. How can this analysis inform climate adaptation planning?

### Action and Advocacy

12. Who needs to see this information? (EPA, Tribal Council, etc.)
13. What additional data collection is needed?
14. How can this support environmental protection efforts?
15. What role can community members play in ongoing monitoring?

---

## Real-World Application

### Next Steps for Community Use

**Immediate Actions:**
1. Share maps with Tribal Environmental Office
2. Present findings to Council
3. Request water quality testing for identified streams
4. Create community awareness materials

**Ongoing Monitoring:**
1. Train community members to use this GIS method
2. Create protocol for annual imagery review
3. Develop reporting system for new observations
4. Build time-series database

**Research Partnerships:**
1. Share data with university researchers
2. Connect with Alaska permafrost monitoring networks
3. Contribute to regional rusting rivers database
4. Participate in statewide monitoring efforts

**Advocacy:**
1. Use maps in grant applications for water quality monitoring
2. Submit to regulatory agencies (EPA, ADEC)
3. Include in climate change impact assessments
4. Support environmental protection policies

---

## Additional Resources

### Scientific Background
- [USGS Permafrost Research](https://www.usgs.gov/programs/climate-research-and-development-program/science/permafrost-and-climate-change)
- [Alaska Permafrost and Climate Change](https://agcrops.osu.edu/newsletter/corn-newsletter/2024-10/alaskas-turning-orange-its-not-all-rust)
- [Arctic River Chemistry Changes](https://www.nature.com/articles/s43247-024-01587-z)

### GIS Methods
- [Hydrology Toolset in ArcGIS Pro](https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-analyst/an-overview-of-the-hydrology-tools.htm)
- [Remote Sensing of Water Quality](https://www.usgs.gov/mission-areas/water-resources/science/remote-sensing-water-quality)

### Community Resources
- [Tribal Environmental Programs](https://www.epa.gov/tribal)
- [Alaska Native Science Commission](http://www.nativescience.org/)
- [Traditional Ecological Knowledge Resources](https://www.itk.ca/)

---

## Assessment Rubric

| Criteria | Excellent (4) | Good (3) | Satisfactory (2) | Needs Work (1) |
|----------|---------------|----------|------------------|----------------|
| **Feature Class Creation** | Complete attributes, 10+ locations, detailed notes | Complete attributes, 5-9 locations | Minimal attributes, 3-4 locations | Incomplete data |
| **Spatial Analysis** | Multiple analysis methods, thoughtful interpretation | Buffer and one other analysis | Buffer analysis only | Analysis incomplete |
| **Maps** | Professional, clear, all elements, excellent design | Professional, clear, all elements | Basic maps, missing some elements | Unclear or incomplete |
| **Report** | Comprehensive, well-written, integrated knowledge | Complete, clear, good integration | Basic report, minimal integration | Incomplete or unclear |
| **Traditional Knowledge** | Extensively integrated, cited, valued | Some integration | Minimal integration | Not included |
| **Community Relevance** | Highly applicable, actionable recommendations | Applicable recommendations | General recommendations | Limited relevance |

---

## Instructor Notes

**Key Teaching Points:**
- This is a real, emerging environmental issue
- Connects GIS to climate change and subsistence
- Emphasizes value of combining technology and traditional knowledge
- Demonstrates how GIS can support environmental advocacy

**Discussion Facilitation:**
- Encourage sharing of community observations
- Validate traditional knowledge as equal to scientific data
- Connect to broader climate change impacts
- Discuss emotional aspects of environmental change

**Differentiation:**
- Beginners: Focus on point digitization and simple buffers
- Intermediate: Add polygon creation and intersect analysis
- Advanced: Include watershed analysis and statistical work

**Community Sensitivity:**
- This touches on subsistence resources - be respectful
- Some may find environmental changes distressing
- Emphasize community agency and action
- Frame as supporting traditional stewardship

---

**Activity Version:** 1.0
**Last Updated:** November 2025
**Training Location:** Quinhagak, Alaska
