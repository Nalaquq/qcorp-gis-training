# Activity 10: SAR Trail Marking Grant Application

**Duration:** 180 minutes
**Difficulty:** Intermediate-Advanced
**Prerequisites:** Lessons 11-13, Activity 9 (Placename and Trail Mapping), basic cartography skills

---

## Overview

In this activity, you'll prepare a complete GIS dataset and application map for the Alaska Department of Transportation Community Trail Marking Grant. This real-world project demonstrates how GIS supports community funding applications by providing accurate, professional spatial data and visualizations.

You'll work with GPS trail data, clean and prepare it for analysis, calculate trail lengths in miles, and create a professional map suitable for grant submission.

**Example Output:** See the completed grant map below for reference on the expected quality and content.

![ADOT Trail Marking Grant Map](../../../assets/images/ADOT%20trail%20marking%20map_page-0001.jpg)
*Example grant application map showing the Eek to Goodnews Bay winter trail. Map prepared by Patrick Jones and Byron Phillips from Garmin GPX data collected from SAR volunteers, November 20, 2025.*

> **Note:** View the original PDF version at [`assets/ADOT trail marking map.pdf`](../../../assets/ADOT%20trail%20marking%20map.pdf)

---

## Learning Objectives

By the end of this activity, you will be able to:

1. ✅ Prepare GPS trail data for grant applications
2. ✅ Use edit tools (merge, split, extend) to clean trail data
3. ✅ Create and populate attribute fields for grant requirements
4. ✅ Calculate trail lengths in US Survey Miles
5. ✅ Create professional maps for grant applications
6. ✅ Organize project data for collaborative editing
7. ✅ Understand grant application data requirements

---

## Background: Alaska DOT Community Trail Marking Grant

### Grant Program Overview

**Purpose:** The Alaska Department of Transportation Northern Region offers grants to Alaska communities for marking winter trails to improve travel safety.

**Grant Information:**
- Website: https://dot.alaska.gov/nreg/wintertrails/
- Application includes guidelines, forms, and requirements
- Funding supports trail markers, signs, and safety improvements

**Typical Award Range:** $5,000 - $25,000 per community

**Application Requirements:**
1. Completed application form
2. **Map showing all trail routes**
3. **Length of each trail in miles**
4. Identification of dangerous crossings
5. Community support documentation
6. Cost estimates for proposed markers

### Why GIS is Essential

**What Grant Reviewers Need:**
- Accurate trail locations
- Precise measurements for cost estimation
- Professional presentation
- Verifiable data
- Clear identification of safety concerns

**GIS Provides:**
- ✅ Accurate GPS-based trail routes
- ✅ Calculated lengths in required units (miles)
- ✅ Professional maps with proper cartography
- ✅ Spatial data showing dangerous crossings
- ✅ Defensible, reproducible measurements

---

## Part 1: Project Setup and Data Organization (20 minutes)

### Task 1.1: Review Grant Materials

**Download Application Materials:**
1. Visit: https://dot.alaska.gov/nreg/wintertrails/
2. Download:
   - Grant application form (PDF)
   - Grant guidelines document
   - Any sample applications or maps if available

**Review Requirements:**
1. Read application guidelines carefully
2. Note specific data requirements:
   - Trail lengths must be in **miles**
   - Map scale and quality requirements
   - Required map elements
   - Deadline and submission format

**Document Requirements:**
Create notes on:
- What fields/attributes are needed in trail data
- What map elements must be included
- Units required for measurements
- Any special considerations

### Task 1.2: Set Up Collaborative Workspace

**OneDrive Setup** (for team collaboration):

1. Create shared folder in OneDrive:
   - Name: `SAR_Trail_Marking_Grant_2025`
   - Share with all team members
   - Set permissions: Edit access

2. Upload grant materials:
   - Application form
   - Guidelines
   - Any reference documents

3. Create subfolders:
   ```
   SAR_Trail_Marking_Grant_2025/
   ├── Application_Documents/
   ├── Maps/
   ├── GPS_Data/
   ├── Photos/
   └── Team_Notes/
   ```

**Benefit:** All team members can access and edit application materials collaboratively.

### Task 1.3: Create ArcGIS Pro Project

**Project Setup:**
1. Launch ArcGIS Pro
2. Create new project:
   - Name: `SAR_Trail_Marking_Grant`
   - Location: Documents/ArcGIS/
   - Template: Map

**Set Coordinate System:**
1. Right-click Map in Contents → Properties
2. Coordinate Systems tab
3. Search: "26937" (Alaska State Plane Zone 7)
4. Select: NAD 1983 StatePlane Alaska 7 FIPS 5007
5. OK

**Why State Plane?**
- Accurate measurements in feet/miles for Alaska
- Matches Alaska DOT standards
- Appropriate for local-scale mapping

**Add Basemap:**
1. Map tab → Basemap → Imagery
2. Provides reference for trail verification

---

## Part 2: Import and Review GPS Trail Data (30 minutes)

### Task 2.1: Import GPX Data from Garmin

**If continuing from Activity 9:**
- Use trail data already imported
- Skip to Task 2.2

**If starting fresh:**

1. **Connect Garmin Device:**
   - Connect GPS unit via USB
   - Open Garmin Basecamp

2. **Export GPX Files:**
   - Select all trail tracks
   - File → Export → Export Selection
   - Format: GPX
   - Save to: Project folder/GPS_Data/
   - Filename: `SAR_Trails_Raw.gpx`

3. **Convert to ArcGIS Layer:**
   - Analysis tab → Tools
   - Search: "GPX to Features"
   - Input GPX File: SAR_Trails_Raw.gpx
   - Output Feature Class: SAR_Trails (in project geodatabase)
   - Output Type: Tracks (for lines)
   - Run tool

4. **Add Result to Map:**
   - Tool completes
   - Add SAR_Trails layer to map
   - Zoom to layer extent

### Task 2.2: Initial Data Assessment

**Visual Review:**
1. Zoom to each trail
2. Compare to satellite imagery
3. Identify issues:
   - ✏️ Multiple segments for same trail?
   - ✏️ Gaps in GPS tracks?
   - ✏️ Trails extending too far?
   - ✏️ Trails deviating from actual route?

**Document Findings:**
Create list of issues to fix:
```
Trail Issues to Address:
□ Quinhagak to Goodnews: 3 segments, need to merge
□ Fish Camp Trail: Small gap from signal loss
□ Village Loop: Extends beyond actual endpoint
□ River Crossing Trail: Multiple overlapping tracks
```

**Open Attribute Table:**
1. Right-click SAR_Trails → Attribute Table
2. Review existing fields from GPS:
   - Track name (if named in GPS)
   - Date recorded
   - Any other GPS metadata

**Count Features:**
- Note total number of trail segments
- Prepare to clean and organize

---

## Part 3: Clean Trail Data Using Edit Tools (45 minutes)

### Task 3.1: Extend Segments to Close Small Gaps

**Reference:** Lesson 12 - Edit Tools

**For each gap < 50 meters:**

1. **Select First Segment:**
   - Edit tab → Select tool
   - Click segment on one side of gap

2. **Use Extend Tool:**
   - Edit tab → Modify Features
   - Search: "Extend"
   - Click "Extend or Trim" tool

3. **Configure Extend:**
   - Extension distance: 100 meters
   - Select by feature: Click next segment
   - Tool extends to connect

4. **Verify Connection:**
   - Zoom in close
   - Verify segments now connect cleanly
   - Check alignment makes sense

5. **Repeat for All Gaps**

**Save Edits:**
- Edit tab → Save
- Important: Save frequently!

### Task 3.2: Merge Trail Segments

**Reference:** Lesson 12 - Edit Tools

**For each complete trail route:**

**Example: Quinhagak to Goodnews Trail**

1. **Select All Segments:**
   - Edit tab → Select tool
   - Click first segment
   - Hold SHIFT
   - Click additional segments
   - All segments of same trail should be selected

2. **Verify Selection:**
   - Open attribute table
   - Click "Show selected records"
   - Confirm correct segments selected

3. **Merge Tool:**
   - Edit tab → Modify Features
   - Search: "Merge"
   - Merge dialog opens

4. **Choose Target Attributes:**
   - Review attribute values from each segment
   - Click row with best/most complete attributes
   - This feature will survive the merge

5. **Complete Merge:**
   - Click Merge button
   - Segments combine into single line
   - Verify on map

6. **Repeat for Each Trail:**
   - Process each named trail route
   - Merge all segments into single features

**Save Edits:**
- Edit tab → Save

### Task 3.3: Split at Logical Divisions (Optional)

**If your grant application requires trail segments:**

**Reference:** Lesson 12 - Edit Tools

**Example reasons to split:**
- Different trail names for connected routes
- Split at dangerous crossings for separate analysis
- Break long trail into manageable segments

**To Split:**
1. Select trail to split
2. Edit tab → Modify Features → Split
3. Draw split line across trail
4. Trail divides into separate features
5. Update attributes for each segment

---

## Part 4: Create and Populate Attribute Fields (30 minutes)

### Task 4.1: Plan Required Fields

**Based on grant requirements, create:**

| Field Name | Type | Length | Purpose |
|------------|------|--------|---------|
| Trail_Name | Text | 100 | Official trail name |
| From_Location | Text | 100 | Starting point |
| To_Location | Text | 100 | Destination |
| Trail_Type | Text | 50 | Winter, Summer, Year-round |
| Length_Miles | Double | - | Length in US Survey Miles (calculated) |
| Condition | Text | 20 | Good, Fair, Poor |
| Safety_Concerns | Text | 255 | Description of hazards |
| Grant_Priority | Short Integer | - | 1-5 (5=highest priority) |
| Markers_Needed | Long Integer | - | Estimated markers required |
| Cost_Estimate | Double | - | Estimated marking cost |
| Source | Text | 100 | GPS data source |
| Date_Collected | Date | - | When GPS data collected |
| Notes | Text | 255 | Additional information |

### Task 4.2: Add Fields to Layer

**Reference:** Lesson 13 - Attribute Fields and Calculating Geometry

**Steps:**

1. **Open Fields View:**
   - Right-click SAR_Trails layer
   - Design → Fields
   - OR: Open attribute table → Fields button

2. **Add Each Field:**
   - Scroll to bottom
   - Click "Click here to add a new field"
   - Configure each field from table above:
     - Field Name (no spaces!)
     - Data Type
     - Length (for text fields)
     - Alias (display name)
     - Allow Nulls: Yes
   - Repeat for all fields

3. **Save Fields:**
   - Click Save in Fields toolbar
   - Close Fields view

**Verify:**
- Open attribute table
- All new fields should appear
- Currently empty, will populate next

### Task 4.3: Populate Attribute Data

**Manual Data Entry:**

For each trail:

1. **Open Attribute Table**
2. **Click in field to edit**
3. **Enter information:**

**Example - Quinhagak to Goodnews Trail:**
- Trail_Name: "Quinhagak to Goodnews Bay Trail"
- From_Location: "Quinhagak"
- To_Location: "Goodnews Bay"
- Trail_Type: "Winter"
- Condition: "Good"
- Safety_Concerns: "River crossings with variable ice, exposed tundra section"
- Grant_Priority: 5
- Markers_Needed: (estimate: ~1 per mile = 47)
- Source: "Garmin GPS - SAR Volunteers"
- Date_Collected: 11/20/2025
- Notes: "Primary route for winter travel, SAR priority route"

4. **Repeat for All Trails**

**Save Edits:**
- Edit tab → Save
- All attributes preserved

---

## Part 5: Calculate Trail Lengths in Miles (15 minutes)

### Task 5.1: Calculate Geometry

**Reference:** Lesson 13 - Attribute Fields and Calculating Geometry

**Critical for Grant:** Alaska DOT requires lengths in **US Survey Miles**

**Steps:**

1. **Open Attribute Table**
2. **Right-click `Length_Miles` field header**
3. **Select "Calculate Geometry"**

4. **Configure Calculate Geometry:**
   - Property: Length_Miles
   - Geometry Attribute: **Length**
   - Units: **Miles (US Survey)** or **Miles US**
     - Scroll through length units carefully
     - Select US Survey version
   - Coordinate System: Use data source (default)

5. **Click OK**
   - Tool runs
   - `Length_Miles` field populates

6. **Verify Results**

**Expected Results:**

| Trail_Name | Length_Miles (approx) |
|------------|----------------------|
| Quinhagak to Goodnews Bay | 40-50 |
| Quinhagak to Fish Camp | 5-10 |
| Village Loop Trail | 2-5 |
| River Crossing Trail | 3-8 |

**Quality Check:**
- Do values make sense for trail distances?
- Compare to Google Earth measurements
- Verify total miles is reasonable

### Task 5.2: Calculate Total System Miles

**For Grant Application Summary:**

1. **In Attribute Table:**
   - Right-click `Length_Miles` column header
   - Statistics
   - View Sum

2. **OR: Bottom of Attribute Table:**
   - Look for statistics panel
   - Shows Sum, Mean, Min, Max

3. **Document Total:**
   - Total Trail Miles: ______
   - Record for grant application

**Example:**
```
Total Trail System: 59.2 miles
- Quinhagak to Goodnews Bay: 47.3 miles
- Quinhagak to Fish Camp: 8.7 miles
- Village Loop Trail: 3.2 miles
```

---

## Part 6: Create Professional Grant Application Map (40 minutes)

### Task 6.1: Prepare Map Content

**Reference:** Module 5 - Cartography, Lesson 9 - Graphics and Annotation

**Example Map:** Review the completed example at `assets/ADOT trail marking map.pdf` to see the expected layout, elements, and professional quality for your grant application map.

**Add Supporting Layers:**

1. **Community Buildings/Facilities:**
   - Add from AGOL if available
   - Shows context for trail system

2. **Dangerous Crossings:**
   - If created in Activity 9
   - Shows safety concerns

3. **Quinhagak Boundary:**
   - Community boundary or planning area
   - Defines project extent

**Style Trails:**

1. **Symbolize by Priority:**
   - Right-click SAR_Trails → Symbology
   - Unique Values
   - Field: Grant_Priority
   - Apply

2. **Or Single Symbol:**
   - Single symbol
   - Color: High contrast (Red or Bright Blue)
   - Width: 3-4 points
   - Make trails very visible

3. **Add Labels:**
   - Right-click layer → Labeling Properties
   - Field: Trail_Name
   - Font: 10-12 pt, bold
   - Halo: White
   - Enable labels

### Task 6.2: Create Map Layout

**Insert Layout:**
1. Insert tab → New Layout
2. Page size: Letter (8.5 x 11)
3. Orientation: Landscape

**Add Map Frame:**
1. Layout already contains map frame
2. Resize and position to show all trails
3. Zoom to appropriate scale

**Add Map Elements:**

**1. Title:**
- Insert → Text
- Text: "Quinhagak Community Trail System"
- Subtitle: "Alaska DOT Community Trail Marking Grant Application"
- Font: Large, bold (18-24 pt)
- Position: Top center

**2. Legend:**
- Insert → Legend
- Remove unnecessary layers
- Show:
  - Trails (with priority or single symbol)
  - Dangerous crossings
  - Community features
- Clean, readable formatting

**3. Scale Bar:**
- Insert → Scale Bar
- Units: Miles
- Style: Professional, clear
- Position: Lower left or right

**4. North Arrow:**
- Insert → North Arrow
- Simple, professional style
- Position: Upper right or with scale bar

**5. Data Sources and Credits:**
- Insert → Text
- Small text (8-10 pt)
- Content example (see `assets/ADOT trail marking map.pdf`):
  ```
  Map prepared by [Your Name] from Garmin GPX data
  collected from search and rescue volunteers on [Date]

  Data Sources:
  Trail GPS Data: Quinhagak SAR, November 2025
  Basemap: Esri World Imagery
  Projection: NAD 1983 StatePlane Alaska 7 FIPS 5007
  ```
- Position: Lower left corner

**6. Trail Table (Optional but Impressive):**
- Insert → Dynamic Text → Table
- OR create text box with trail summary:
  ```
  Trail Summary:

  Trail Name                    Length (Miles)  Priority
  Quinhagak to Goodnews Bay    47.3            High
  Quinhagak to Fish Camp       8.7             Medium
  Village Loop Trail           3.2             High

  Total System:                59.2 miles
  ```

### Task 6.3: Refine Cartography

**Review Cartographic Principles:**

1. **Visual Hierarchy:**
   - Trails most prominent
   - Supporting features secondary
   - Basemap subtle

2. **Color Choices:**
   - High contrast for trails
   - Accessible colors (avoid red-green for colorblind readers)
   - Professional palette

3. **Text Readability:**
   - Sufficient size for printing
   - Good contrast with background
   - Halos on labels if needed

4. **Layout Balance:**
   - Elements well-spaced
   - Not too crowded
   - Professional appearance

**Get Feedback:**
- Share layout with team
- Show to SAR volunteers
- Verify accuracy
- Make adjustments

### Task 6.4: Export Final Map

**Export as PDF:**
1. Share tab → Export Layout
2. Format: PDF
3. Resolution: 300 DPI (high quality)
4. Color Mode: RGB
5. Filename: `SAR_Trail_Marking_Grant_Map_2025.pdf`
6. Save to: OneDrive shared folder/Maps/

**Verify Export:**
1. Open PDF
2. Check:
   - All elements visible
   - Text readable
   - Colors accurate
   - High quality for printing

**Copy to Assets Directory:**
- Save copy to: `assets/ADOT trail marking map.pdf`
- This matches the example file created for this activity

**Example Output:**
- See completed example: `assets/ADOT trail marking map.pdf`
- This professional map demonstrates the expected quality and content for grant applications

---

## Part 7: Complete Grant Application (20 minutes)

### Task 7.1: Fill Application Form

**Open Application Form:**
1. From OneDrive: Application_Documents/
2. Open in PDF editor or print for hand-writing

**Use GIS Data to Complete:**

**Trail Information Section:**
- Trail names: From attribute table
- Trail lengths: From `Length_Miles` field
- Total system miles: Calculated sum

**Cost Estimation:**
- Markers needed: From attribute table
- Cost per marker: Research/estimate ($150-200 typical)
- Total cost: Calculate based on trail data

**Map Attachment:**
- Attach exported PDF map
- Reference: "See attached trail system map"

### Task 7.2: Supporting Documentation

**Prepare Additional Materials:**

1. **Trail Data Summary:**
   - Export attribute table to Excel
   - Clean formatting
   - Include in application packet

2. **Photos:**
   - Trail conditions
   - Existing markers or lack thereof
   - Dangerous crossings
   - Save to: OneDrive/Photos/

3. **Community Support Letters:**
   - SAR endorsement
   - Tribal council support
   - Community letters

### Task 7.3: Review and Package Application

**Final Review Checklist:**

- [ ] Application form complete
- [ ] All required signatures
- [ ] Professional map attached
- [ ] Trail data summary included
- [ ] Cost estimates accurate
- [ ] Supporting documentation organized
- [ ] Community support letters included
- [ ] Deadline met

**Package for Submission:**
1. All materials in one PDF if submitting electronically
2. OR: Printed, organized in folder if mailing
3. Keep copy for records

---

## Deliverables

### Required Submissions

1. **✅ Clean Trail Dataset**
   - SAR_Trails layer with all segments merged/cleaned
   - Complete attribute information
   - Accurate length calculations

2. **✅ Professional Grant Map (PDF)**
   - All required map elements
   - High-quality export (300 DPI)
   - Professional cartography
   - File: `ADOT trail marking map.pdf`
   - Example: See `assets/ADOT trail marking map.pdf`

3. **✅ Trail Data Summary**
   - Table showing all trails
   - Lengths in miles
   - Priority rankings
   - Cost estimates

4. **✅ Completed Grant Application**
   - All sections filled using GIS data
   - Map attached
   - Ready for submission

5. **✅ Organized Project Files**
   - OneDrive folder with all materials
   - Team can access and edit
   - Ready for collaborative review

---

## Assessment Criteria

| Criteria | Excellent (4) | Good (3) | Satisfactory (2) | Needs Work (1) |
|----------|---------------|----------|------------------|----------------|
| **Data Cleaning** | All segments merged correctly, no gaps or overlaps | Minor issues remaining | Some cleanup done | Raw data, not cleaned |
| **Attribute Completeness** | All fields populated accurately | Most fields complete | Some fields missing | Minimal attribution |
| **Length Calculation** | Accurate US Survey Miles, verified | Correct units, reasonable values | Calculated but wrong units | Not calculated or errors |
| **Map Quality** | Professional, all elements, grant-ready | Good map, minor improvements needed | Basic map, missing elements | Incomplete or poor quality |
| **Grant Application** | Complete, accurate, professional | Mostly complete | Partial completion | Not completed |
| **Team Collaboration** | Excellent organization, shared access | Good collaboration | Some collaboration | Individual work only |

---

## Discussion Questions

### GIS and Grant Applications

1. How does GIS strengthen a grant application compared to hand-drawn maps or estimates?
2. What data accuracy is necessary for cost estimates in grant applications?
3. How can you verify that your calculated measurements are correct?

### Trail Data Management

4. What challenges did you encounter cleaning GPS data?
5. How do you decide when to merge segments vs keep them separate?
6. What information should be documented about trail conditions?

### Community Application

7. How does this trail marking grant benefit the community?
8. What other grants or applications could benefit from GIS data?
9. How can this dataset be maintained and updated over time?

### Professional Skills

10. What makes a map "professional" and "grant-ready"?
11. How do you balance data accuracy with project timelines?
12. What role does collaborative organization (OneDrive) play in successful applications?

---

## Real-World Outcome

### Quinhagak SAR Grant Application

**Context:**
This activity is based on an actual grant application process where GIS data was essential for success.

**Process:**
1. **Community Need Identified:**
   - SAR volunteers recognized need for trail markers
   - Winter travel safety concern
   - Grant opportunity identified

2. **GIS Data Collected:**
   - GPS tracks from SAR volunteers
   - Traditional knowledge about trails
   - Dangerous crossing locations

3. **Data Prepared:**
   - Cleaned GPS data using edit tools
   - Calculated accurate lengths
   - Created professional map

4. **Application Submitted:**
   - Complete grant application
   - Professional supporting materials
   - Accurate cost estimates

**Impact:**
- Strong, competitive application
- Quantitative, verifiable data
- Professional presentation
- Community safety improvement opportunity

**Files Created:**
- Trail dataset with accurate measurements
- Professional map: `assets/ADOT trail marking map.pdf` (prepared by Patrick Jones and Byron Phillips)
- Complete application documentation

**Map Features (see example PDF):**
- Trail route from Eek through Quinhagak to Goodnews Bay
- Satellite basemap showing terrain
- Inset location map
- Professional legend and map elements
- Proper data attribution

**Lesson Learned:**
GIS transforms community needs into fundable, professional grant applications that make a real difference in community safety and well-being. The example map demonstrates how GPS data from SAR volunteers becomes a professional grant application document.

---

## Extension Activities

### Advanced Analysis

1. **Buffer Analysis:**
   - Create 1-mile buffers around trails
   - Identify households within easy trail access
   - Support community benefit analysis

2. **Cost-Benefit Calculation:**
   - Add fields for detailed cost breakdown
   - Calculate costs per mile, per marker
   - Compare different marking strategies

3. **Multi-year Planning:**
   - Phase marking over multiple years
   - Priority-based implementation plan
   - Track grant-funded vs future sections

### Additional Maps

1. **Winter Travel Network:**
   - Combine trails with ice roads
   - Show complete winter transportation system

2. **Safety Hazard Map:**
   - Focus on dangerous crossings
   - Detailed safety information
   - For SAR emergency reference

3. **Before/After Map:**
   - Show current trail system
   - Overlay proposed markers
   - Visualize grant impact

---

## Resources

### Grant Information
- [Alaska DOT Winter Trails Program](https://dot.alaska.gov/nreg/wintertrails/)
- Application deadlines and requirements
- Sample successful applications (if available)

### Technical Resources
- Lesson 11: Creating Layers
- Lesson 12: Edit Tools (Merge, Split, Extend)
- Lesson 13: Attribute Fields and Calculating Geometry
- Module 5 Lesson 9: Graphics and Cartography

### Tools Used
- GPX to Features tool
- Extend or Trim tool
- Merge tool
- Calculate Geometry tool
- Layout and cartography tools

---

## Instructor Notes

### Preparation

**Before Activity:**
- Review current Alaska DOT grant requirements
- Update any changed requirements in activity
- Prepare sample GPS data if students don't have their own
- Set up OneDrive shared folder or similar

**Time Management:**
- Data cleaning takes longer than expected - allow extra time
- Map creation can be done partially as homework
- Consider 2-session activity if time limited

### Teaching Tips

**Emphasize Real-World Application:**
- This is an actual grant application process
- Data quality matters for funding decisions
- Professional presentation = competitive application

**Collaborative Learning:**
- Have students work in pairs/small teams
- Simulate real grant application teams
- Share data cleaning strategies

**Troubleshooting:**
- Common issue: Wrong units in Calculate Geometry
- Watch for: Missed segments during merge
- Verify: Coordinate system set correctly

### Community Context

**Cultural Sensitivity:**
- Trail names may have cultural significance
- Respect traditional knowledge about routes
- Involve community members in verification

**Real Impact:**
- This grant funds actual community safety improvements
- GIS skills directly support community well-being
- Emphasize connection between technical skills and community benefit

---

## Acknowledgments

This activity was developed based on real grant application work supporting Quinhagak Search and Rescue's Alaska DOT Community Trail Marking Grant application. Thanks to SAR volunteers for sharing trail knowledge and GPS data, and to the community for supporting winter travel safety improvements.

The map created in this activity (`assets/ADOT trail marking map.pdf`) represents professional GIS work supporting actual community funding applications.

---

**Activity Version:** 1.0
**Last Updated:** November 2025
**Module:** 4 - Spatial Analysis in ArcGIS Pro
**Location:** Quinhagak, Alaska
**Real-World Application:** Alaska DOT Grant Support
