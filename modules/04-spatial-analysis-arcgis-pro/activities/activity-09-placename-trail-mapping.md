# Activity 9: Community Placename and Trail Mapping with Search and Rescue

**Training Date:** November 20, 2025
**Duration:** 180 minutes
**Difficulty:** Intermediate
**Prerequisites:** Lessons 1-5 completed, familiarity with editing feature layers

---

## Overview

In this activity, you'll work with community members to document traditional Yup'ik placenames and trails. This session brings together traditional knowledge holders from Quinhagak Search and Rescue with GIS technology to preserve cultural knowledge, support community navigation safety, and prepare grant applications for trail marking programs.

![Community Placename Mapping Session](../../../assets/images/Placename%20Mapping.JPG)
*SAR volunteers collaborate with GIS tech to map trails and placenames in ArcGIS Pro*

---

## Learning Objectives

By the end of this activity, you will:

1. ✅ Edit and add features to an existing hosted feature layer
2. ✅ Add point features (placenames) with complete attribute information
3. ✅ Convert GPX files from GPS devices to GIS layers
4. ✅ Create line features (trails) from GPS track data
5. ✅ Create point features for hazard locations (dangerous crossings)
6. ✅ Reference external cultural mapping resources
7. ✅ Integrate traditional knowledge with GIS data
8. ✅ Support grant applications with spatial documentation

---

## Background: Community Mapping and Traditional Knowledge

### Yup'ik Placenames

**Cultural Significance:**
Traditional Yup'ik placenames carry important information about:
- Geographic features and landmarks
- Historical events and traditional use
- Navigation and wayfinding
- Resource locations
- Safety information

**Preservation Needs:**
- Elder knowledge must be documented before it's lost
- Placenames support search and rescue operations
- Maps with local names improve community navigation
- Cultural preservation for future generations

### Quinhagak Search and Rescue

**Role in Community:**
- Volunteer organization supporting emergency response
- Expert knowledge of trails and travel routes
- Traditional navigation knowledge holders
- Critical community safety resource

**Mapping Needs:**
- Document winter and summer trails
- Mark dangerous crossings and hazards
- Create reference maps for search operations
- Support grant applications for trail marking

### Alaska DOT Community Trail Marking Grant

**Program Overview:**
The Alaska Department of Transportation offers grants for community trail marking to improve winter travel safety.

**Grant Information:**
https://dot.alaska.gov/nreg/wintertrails/

**Requirements for Application:**
- Map of proposed trail routes
- Identification of dangerous crossings
- Community support documentation
- GIS data showing trail locations

---

## Data Resources

### Existing Feature Layer

**Quinhagak Yuuyaraq Place Names:**
https://services6.arcgis.com/HDgSl3KvKJMed1UY/arcgis/rest/services/Quinhagak_Yuuyaraq_Place_Names/FeatureServer

This layer contains:
- Existing documented placenames
- Yup'ik spellings and meanings
- Location coordinates
- Source information

### Reference Resources

**ELOKA Yup'ik Atlas:**
https://eloka.nsidc.org/yupik/atlas/index.html

The Exchange for Local Observations and Knowledge of the Arctic (ELOKA) hosts a Yup'ik atlas with additional placenames that may be useful for comparison and verification.

---

## Part 1: Session Setup and Review (20 minutes)

### Task 1.1: Project Setup

**Create ArcGIS Pro Project:**
1. Launch ArcGIS Pro
2. Create new project: "Placename_Trail_Mapping_Nov2025"
3. Location: Documents/ArcGIS/
4. Template: Map

**Set Coordinate System:**
1. Right-click Map → Properties
2. Coordinate Systems tab
3. Select: NAD 1983 StatePlane Alaska 7 FIPS 5007
4. Click OK

### Task 1.2: Add Existing Placename Layer

**Add from ArcGIS Online:**
1. Insert tab → Add Data → Data From Path
2. Enter URL:
   ```
   https://services6.arcgis.com/HDgSl3KvKJMed1UY/arcgis/rest/services/Quinhagak_Yuuyaraq_Place_Names/FeatureServer
   ```
3. Add layer to map

**Review Existing Data:**
1. Open attribute table
2. Note existing fields:
   - Placename (Yup'ik)
   - English translation
   - Description
   - Source
   - Date added
3. Count existing features
4. Zoom to Quinhagak area

### Task 1.3: Set Up Display for Community Review

**Display Configuration:**
1. Connect to large screen/projector
2. Set basemap to satellite imagery
3. Label placenames on map
4. Configure pop-ups to show all attributes

**Prepare for Session:**
- Print list of existing placenames for volunteers to review
- Have blank forms ready for new placename documentation
- Ensure editing permissions are configured

---

## Part 2: Community Placename Review and Addition (45 minutes)

### Task 2.1: Review Existing Placenames with Volunteers

**Community Review Process:**
1. Display all existing placenames on large screen
2. SAR volunteers review for accuracy:
   - Correct spelling?
   - Location accurate?
   - Description complete?
3. Note corrections needed
4. Identify gaps - what places are missing?

**Documentation:**
- Take notes on volunteer feedback
- Record suggested corrections
- List new placenames to add
- Note any disputed or uncertain names

### Task 2.2: Add New Placenames

**Start Edit Session:**
1. Click Edit tab
2. Click Create button
3. Select Placename layer

**For Each New Placename:**
1. Volunteer describes location
2. Zoom to location on satellite imagery
3. Click to place point at correct location
4. Fill in attributes:

**Required Attributes:**

| Field | Description | Example |
|-------|-------------|---------|
| Placename | Yup'ik name | Uyak |
| English | Translation | "Neck" or channel |
| Description | What/where it is | Primary channel where Uyak meets Qanirtuuq |
| Type | Feature type | River, Lake, Hill, Camp, etc. |
| Source | Knowledge source | Quinhagak SAR, [Volunteer name] |
| Date_Added | Date documented | 11/20/2025 |
| Notes | Additional context | Location for NSF channel marking |

5. Save after each addition

**Quality Control:**
- Confirm placement with volunteer
- Verify spelling
- Check translation accuracy
- Document source clearly

### Task 2.3: Update Existing Placename Information

**Edit Existing Features:**
1. Select feature to edit
2. Open Attributes pane
3. Update information based on volunteer feedback
4. Add additional details from traditional knowledge
5. Save edits

**Common Updates:**
- Additional context or stories
- Alternative names
- Historical significance
- Associated features

---

## Part 3: GPS Trail Data Import (30 minutes)

### Task 3.1: Extract GPX Data from Garmin Devices

**Connect GPS Device:**
1. SAR volunteer provides Garmin GPS unit
2. Connect to laptop via USB cable
3. Device appears as removable drive

**Open Garmin Basecamp:**
1. Launch Garmin Basecamp software
2. Device appears in Devices panel
3. View stored tracks and waypoints

**Export GPX Files:**
1. Select desired tracks in Basecamp
2. File → Export → Export Selection
3. Format: GPX
4. Save to project folder: "GPX_Tracks"
5. Use descriptive filename: "SAR_Winter_Trails_2024.gpx"

**Multiple Files:**
- Export tracks from multiple devices if needed
- Name files clearly by volunteer or route
- Keep original data organized

### Task 3.2: Convert GPX to ArcGIS Layer

**Use GPX to Features Tool:**
1. Analysis tab → Tools → Search "GPX to Features"
2. Open GPX to Features tool

**Tool Parameters:**
- Input GPX File: Browse to saved .gpx file
- Output Feature Class: "SAR_Trails" (in project geodatabase)
- Output Type: Tracks (for line features)

3. Click Run
4. Add result to map

**Review Results:**
1. Examine converted line features
2. Check alignment with satellite imagery
3. Verify complete track conversion
4. Note any gaps or errors

### Task 3.3: Clean and Attribute Trail Data

**Add Trail Attributes:**

Create/populate these fields:
- Trail_Name: Name of trail/route
- Trail_Type: Winter, Summer, Year-round
- Difficulty: Easy, Moderate, Difficult
- Condition: Good, Fair, Poor, Unknown
- Last_Verified: Date last traveled
- Safety_Notes: Important information
- Grant_Priority: Priority for marking (1-5)
- Source: Who provided data

**Trail Review with Volunteers:**
1. Display trails on screen
2. Volunteers identify and name each route
3. Discuss condition and safety
4. Mark priority for grant application
5. Document traditional trail names if applicable

---

## Part 4: Identify Dangerous Crossings (25 minutes)

### Task 4.1: Create Dangerous Crossings Feature Class

**Create New Point Layer:**
1. Right-click geodatabase → New → Feature Class
2. Name: "Dangerous_Crossings"
3. Type: Point
4. Same coordinate system as project

**Define Attributes:**

| Field Name | Type | Description |
|------------|------|-------------|
| Crossing_ID | Text (20) | Unique identifier |
| Location_Name | Text (100) | Local/traditional name |
| Hazard_Type | Text (50) | Thin ice, Overflow, Open water, etc. |
| Severity | Text (20) | High, Medium, Low |
| Season | Text (50) | When hazard is present |
| Trail_Name | Text (100) | Associated trail |
| Description | Text (255) | Detailed hazard description |
| Recommended_Action | Text (255) | How to navigate safely |
| Date_Documented | Date | When identified |
| Source | Text (100) | Who reported |

### Task 4.2: Document Dangerous Crossings with Volunteers

**Identification Process:**
1. Review each trail segment with SAR volunteers
2. Ask about dangerous locations:
   - Where have accidents occurred?
   - Where is ice unreliable?
   - Where are overflow areas?
   - Where do people get lost?

**Add Crossing Points:**
1. Start edit session
2. Select Dangerous_Crossings layer
3. Click location on map
4. Fill complete attributes
5. Save edits

**Example Dangerous Crossing:**
- Crossing_ID: DC-001
- Location_Name: "Uyak River Main Channel"
- Hazard_Type: "Variable ice thickness"
- Severity: "High"
- Season: "Fall freeze-up, Spring breakup"
- Trail_Name: "Quinhagak to Fish Camp Trail"
- Description: "Primary channel has unpredictable ice due to tidal influence and current"
- Recommended_Action: "Check ice thickness, avoid during transition seasons"
- Date_Documented: 11/20/2025
- Source: "Quinhagak SAR"

**Priority for Grant:**
- Mark crossings that need trail markers
- Note recommended marker types
- Estimate number of markers needed

---

## Part 5: Reference External Resources (20 minutes)

### Task 5.1: Review ELOKA Yup'ik Atlas

**Access ELOKA Resource:**
1. Open web browser
2. Navigate to: https://eloka.nsidc.org/yupik/atlas/index.html

**Compare with Local Data:**
1. Search for Quinhagak area
2. Compare placenames with local layer
3. Identify any additional names to verify locally
4. Note different spellings or translations

**Discussion with Volunteers:**
- Do these names match local usage?
- Are there corrections needed?
- Should any be added to local layer?
- What's the authoritative local spelling?

### Task 5.2: Document Additional Placenames from Research

**Cross-Reference Process:**
1. Note potentially useful names from ELOKA
2. Verify with SAR volunteers
3. If confirmed, add to local placename layer
4. Document ELOKA as secondary source

**Important:** Always prioritize local traditional knowledge over external sources. External resources are for comparison and completeness, not authority.

---

## Part 6: Special Project - Uyak River Channel Marking (15 minutes)

### Task 6.1: NSF Research Support

**Context:**
A National Science Foundation research team needs to mark the primary channel where Uyak River meets Qanirtuuq River (Kanektok River). The SAR volunteers can provide critical traditional knowledge about this location.

**Add Placename for NSF Project:**
1. SAR volunteers identify the primary channel location
2. Add point at exact location
3. Fill detailed attributes:
   - Placename: [Yup'ik name]
   - English: Primary channel at Uyak-Qanirtuuq confluence
   - Description: Location for NSF channel marking project
   - Type: River/Channel
   - Source: Quinhagak SAR, [volunteer names]
   - Notes: "Added for NSF research team channel marking. SAR volunteers recommend monitoring flow direction in spring when travel resumes."

### Task 6.2: Document Monitoring Plan

**Community Follow-up:**
At the end of the session, SAR volunteers agreed to:
- Monitor Uyak flow and direction in spring
- Report any changes or unusual conditions
- Provide additional information to NSF team
- Update placename layer with observations

**Document in Notes:**
Add to feature notes: "Spring 2026 monitoring planned by SAR volunteers for flow direction and ice conditions."

---

## Part 7: Data Review and Export (15 minutes)

### Task 7.1: Review All Additions

**Quality Check:**
1. Review all new placenames - complete attributes?
2. Review trail data - properly attributed?
3. Review dangerous crossings - locations accurate?
4. Check spelling with volunteers one more time

**Statistics to Document:**
- Number of new placenames added: ___
- Number of placenames updated: ___
- Length of trails documented: ___
- Number of dangerous crossings identified: ___

### Task 7.2: Save and Sync

**Save Local Edits:**
1. Save all edits
2. Save project

**Sync to ArcGIS Online:**
If editing hosted layer:
1. Edits sync automatically
2. Verify by checking ArcGIS Online

**Export Backup:**
1. Export layers to local geodatabase
2. Create backup of today's work
3. Document what was added

---

## Part 8: Grant Application Preparation (15 minutes)

### Task 8.1: Create Trail Marking Application Map

**Map for Alaska DOT Grant:**
1. Insert → New Layout
2. Page size: Letter, Landscape

**Map Content:**
- All trails with priority for marking
- All dangerous crossings
- Placenames for reference
- Clear legend

**Map Elements:**
- Title: "Quinhagak Community Trails - Proposed Marking Locations"
- Subtitle: "Alaska DOT Community Trail Marking Grant Application"
- Legend showing:
  - Trails by priority
  - Dangerous crossings by severity
- Scale bar
- North arrow
- Data sources and date

### Task 8.2: Export Grant Materials

**Export Map:**
1. File → Export Layout
2. Format: PDF
3. Resolution: 300 DPI
4. Filename: "Quinhagak_Trail_Marking_Grant_Map_2025.pdf"

**Export Data Summary:**
Create document listing:
- Total trail miles
- Number of dangerous crossings
- Recommended markers needed
- Community support (SAR involvement)

---

## Deliverables

### Required Submissions

1. **✅ Updated Placename Layer**
   - New placenames added with complete attributes
   - Existing placenames updated as needed
   - All sources documented

2. **✅ Trail Layer**
   - GPX data converted to GIS layer
   - Trails attributed with names and conditions
   - Priority marked for grant application

3. **✅ Dangerous Crossings Layer**
   - All hazard locations documented
   - Complete attributes including recommended actions
   - Severity and season information

4. **✅ Grant Application Map**
   - Professional map showing trails and crossings
   - Clear legend and all required elements
   - PDF export for submission

5. **✅ Session Documentation**
   - List of volunteers who participated
   - Summary of additions and updates
   - Notes on follow-up actions (spring monitoring)

### Optional Deliverables

- **Web map** for SAR use
- **Mobile map** for field reference
- **Summary report** for tribal council
- **Thank you materials** for volunteers

---

## Assessment Criteria

| Criteria | Excellent (4) | Good (3) | Satisfactory (2) | Needs Work (1) |
|----------|---------------|----------|------------------|----------------|
| **Placename Documentation** | 5+ new names, complete attributes, verified | 3-4 new names, complete attributes | 1-2 names, basic attributes | Incomplete or inaccurate |
| **GPX Conversion** | Successful conversion, complete attribution | Successful conversion, basic attribution | Partial conversion | Unsuccessful |
| **Dangerous Crossings** | 3+ crossings, detailed information, actionable | 2 crossings, good detail | 1 crossing, basic info | Missing or incomplete |
| **Grant Map** | Professional, complete, grant-ready | Professional, mostly complete | Basic map, some elements | Incomplete |
| **Traditional Knowledge Integration** | Extensive, respectful, well-documented | Good integration, documented | Some integration | Minimal |
| **Community Engagement** | Excellent facilitation, full participation | Good facilitation | Adequate engagement | Poor engagement |

---

## Discussion Questions

### Traditional Knowledge and GIS

1. How does combining traditional knowledge with GIS benefit the community?
2. What are the ethical considerations when documenting traditional placenames?
3. How can GIS help preserve cultural knowledge for future generations?
4. What's the appropriate way to attribute knowledge to community sources?

### Search and Rescue Applications

5. How will this mapping data help SAR operations?
6. What additional data would be useful for search and rescue?
7. How should this data be maintained and updated?
8. Who should have access to sensitive location information?

### Trail Safety and Marking

9. What criteria should determine marking priority?
10. How can technology complement traditional navigation methods?
11. What are the limitations of GPS and mapping for winter travel?
12. How should trail conditions be monitored and updated?

### Community Collaboration

13. What worked well about this collaborative mapping session?
14. How could future sessions be improved?
15. What other community knowledge should be documented?
16. How can youth be involved in traditional knowledge mapping?

---

## Real-World Outcomes

### From This Session

**Immediate Results:**
- Placenames added to community layer
- Trails documented for grant application
- Dangerous crossings identified for marking
- NSF research support provided

**Grant Application:**
The trail and crossing data will support Quinhagak SAR's application to the Alaska DOT Community Trail Marking Grant program. The professional GIS documentation strengthens the application.

**Research Collaboration:**
The Uyak River channel placename will help NSF researchers locate and mark the primary channel, improving both research accuracy and community navigation safety.

**Spring Monitoring:**
SAR volunteers committed to monitoring Uyak River conditions in spring 2026, creating an ongoing community science collaboration.

### Long-term Benefits

**Cultural Preservation:**
- Traditional placenames documented and preserved
- Elder knowledge recorded before it's lost
- Youth can learn from mapped cultural information

**Community Safety:**
- SAR has better reference maps
- Dangerous crossings are documented
- Trail marking will improve winter travel safety

**Ongoing Updates:**
- Framework established for continued documentation
- Community members can contribute additional knowledge
- Data can be updated as conditions change

---

## Follow-up Actions

### Immediate

1. [ ] Send thank you to SAR volunteers
2. [ ] Share data summary with tribal council
3. [ ] Submit trail marking grant application
4. [ ] Provide Uyak location to NSF team

### Short-term

1. [ ] Create web map for SAR use
2. [ ] Train additional community members on editing
3. [ ] Schedule follow-up session for additional areas
4. [ ] Develop mobile map for field use

### Long-term

1. [ ] Spring 2026 Uyak monitoring
2. [ ] Annual review and update of placenames
3. [ ] Expand to other traditional knowledge areas
4. [ ] Youth education program using maps

---

## Resources

### Technical

- [ArcGIS Pro GPX to Features Tool](https://pro.arcgis.com/en/pro-app/latest/tool-reference/conversion/gpx-to-features.htm)
- [Editing Hosted Feature Layers](https://pro.arcgis.com/en/pro-app/latest/help/editing/edit-web-layers.htm)
- [Garmin Basecamp Software](https://www.garmin.com/en-US/software/basecamp/)

### Grant Information

- [Alaska DOT Winter Trails Program](https://dot.alaska.gov/nreg/wintertrails/)
- [Community Trail Marking Grant Application](https://dot.alaska.gov/nreg/wintertrails/)

### Cultural Mapping Resources

- [ELOKA Yup'ik Atlas](https://eloka.nsidc.org/yupik/atlas/index.html)
- [Alaska Native Language Center](https://www.uaf.edu/anlc/)
- [Traditional Knowledge and GIS Best Practices](https://www.fs.fed.us/pnw/pubs/pnw_gtr592.pdf)

### Community Resources

- Quinhagak Search and Rescue
- Native Village of Kwinhagak
- Qanirtuuq Incorporated

---

## Instructor Notes

### Session Facilitation

**Before Session:**
- Confirm SAR volunteer attendance
- Test ArcGIS Online connectivity
- Prepare large screen display
- Have forms ready for documentation
- Review existing placename data

**During Session:**
- Create welcoming environment for knowledge sharing
- Allow time for stories and context
- Be patient with technology
- Verify spellings carefully
- Respect cultural protocols

**After Session:**
- Thank volunteers sincerely
- Share results promptly
- Follow up on commitments made
- Document lessons learned

### Cultural Sensitivity

**Important Considerations:**
- Some placenames may have cultural restrictions
- Always ask before documenting sensitive locations
- Credit knowledge sources appropriately
- Respect if some information shouldn't be mapped
- Consider data access and sharing permissions

### Technical Tips

- Save frequently during editing sessions
- Have backup plan if connectivity fails
- Export GPX files before session if possible
- Use large font sizes for group viewing
- Test all connections before volunteers arrive

---

## Acknowledgments

This activity was developed in collaboration with Quinhagak Search and Rescue volunteers who generously shared their traditional knowledge and trail expertise. Their contributions preserve important cultural and safety information for current and future generations.

Special thanks to GIS Technician Patrick Jones for facilitating the November 20, 2025 mapping session and to the SAR volunteers who participated.

---

**Activity Version:** 1.0
**Last Updated:** November 2025
**Training Date:** November 20, 2025
**Location:** Quinhagak, Alaska
**GIS Tech:** Patrick Jones
**Partners:** Quinhagak Search and Rescue
