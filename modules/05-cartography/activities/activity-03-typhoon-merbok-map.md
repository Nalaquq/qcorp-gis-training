# Activity 3: Typhoon Merbok Damage Assessment Map

**Training Date:** November 8, 2025
**Duration:** 120 minutes
**Prerequisites:** Lessons 1-4, 7-8 completed

---

## Activity Overview

Create a professional damage assessment map documenting impacts from Typhoon Merbok on Quinhagak infrastructure. This map will be used for recovery planning, funding applications, and community communication.

---

## Learning Objectives

By completing this activity, you will be able to:

1. Create point layers for discrete damage locations
2. Create polygon layers for area-based damage
3. Design a map for emergency management purposes
4. Apply appropriate symbology for damage assessment
5. Include all required map elements
6. Export a professional PDF suitable for official use

---

## Background

### Typhoon Merbok Impact

**Event:** September 2022 (formerly known as Typhoon Merbok)
**Impact on Quinhagak:**
- Coastal storm surge and flooding
- High winds
- Coastal erosion
- Infrastructure damage
- Fish rack damage
- Sewer system impacts

**Documentation Needs:**
- Record damage locations and extent
- Support recovery funding requests
- Plan infrastructure repairs
- Communicate impacts to agencies
- Establish historical record

---

## Part 1: Project Setup (15 minutes)

### Task 1.1: Create New Map

1. **Sign in to ArcGIS Online**
   - Navigate to https://arcgis.com
   - Sign in with your credentials

2. **Create New Map**
   - Click "Map" button
   - New blank map opens

3. **Save Map**
   - Click "Save" → "Save As"
   - Title: "Typhoon Merbok Damage Assessment - Quinhagak"
   - Tags: "typhoon", "merbok", "damage", "quinhagak", "infrastructure"
   - Summary: "Map documenting damage from Typhoon Merbok in September 2022"
   - Save

### Task 1.2: Select Basemap

**Choose Appropriate Basemap:**
- Try "Imagery" - shows satellite view
- Or "Imagery with Labels" - satellite with place names
- Consider "Topographic" for broader context

**Why Imagery?**
- Shows ground conditions
- Helps identify damage locations
- Visual reference for extent
- Context for erosion areas

**Set Basemap:**
1. Click "Basemap" button
2. Select "Imagery with Labels"
3. Zoom to Quinhagak area
4. Position map showing community and coastline

---

## Part 2: Create Damage Point Layers (30 minutes)

### Task 2.1: Create Damaged Fish Racks Layer

**Create Layer:**
1. Click "Add" → "Create feature layer"
2. Select **"Point"**
3. Click "Next"

**Layer Properties:**
- Name: "Typhoon_Merbok_Damaged_Fish_Racks"
- Description: "Locations of fish racks damaged by Typhoon Merbok"
- Tags: damage, fish racks, typhoon, infrastructure
- Click "Next"

**Define Attributes:**

Add the following fields:

| Field Name | Type | Length/Settings | Description |
|------------|------|-----------------|-------------|
| Rack_ID | Text | 20 | Unique ID (FR-001, FR-002) |
| Rack_Name | Text | 100 | Name or description of location |
| Damage_Type | Text | 100 | Type of damage observed |
| Severity | Text | 20 | Low/Medium/High/Critical |
| Date_Assessed | Date | - | Date damage documented |
| Est_Repair_Cost | Integer | - | Estimated repair cost ($) |
| Repairable | Text | 10 | Yes/No/Unknown |
| Priority | Integer | - | Repair priority (1-5, 1=highest) |
| Notes | Text | 255 | Additional information |
| Assessor | Text | 50 | Person who documented damage |

**Create Layer**

### Task 2.2: Digitize Damaged Fish Racks

**Add Features:**
1. Click "Edit" button
2. Select "Typhoon_Merbok_Damaged_Fish_Racks" layer
3. Click "Add feature"

**For Each Damaged Rack:**
1. Zoom to location (use local knowledge or photos)
2. Click to place point at rack location
3. Fill in attributes:

**Example Fish Rack 1:**
- Rack_ID: FR-001
- Rack_Name: "North Beach Rack"
- Damage_Type: "Structural failure - main support damaged"
- Severity: "High"
- Date_Assessed: 11/8/2025 (or actual assessment date)
- Est_Repair_Cost: 5000
- Repairable: "Yes"
- Priority: 1
- Notes: "Main support beam broken, wire sections torn"
- Assessor: [Your name]

**Example Fish Rack 2:**
- Rack_ID: FR-002
- Rack_Name: "River Mouth Rack"
- Damage_Type: "Wire damage, partial washout"
- Severity: "Medium"
- Date_Assessed: 11/8/2025
- Est_Repair_Cost: 2500
- Repairable: "Yes"
- Priority: 2
- Notes: "Wire netting torn in three places"
- Assessor: [Your name]

**Add 3-5 damaged fish rack locations**

4. Click "Save" after each feature

### Task 2.3: Create Sewer Damage Points Layer

**Create Layer:**
1. Click "Add" → "Create feature layer"
2. Select **"Point"**

**Layer Properties:**
- Name: "Typhoon_Merbok_Sewer_Damage"
- Description: "Sewer infrastructure damage locations from Typhoon Merbok"
- Tags: sewer, damage, typhoon, infrastructure

**Define Attributes:**

| Field Name | Type | Description |
|------------|------|-------------|
| Damage_ID | Text (20) | Unique ID (SD-001, SD-002) |
| Location_Desc | Text (100) | Location description |
| Damage_Type | Text (100) | Type of sewer damage |
| Severity | Text (20) | Low/Medium/High/Critical |
| Date_Assessed | Date | Assessment date |
| Functional | Text (10) | Yes/No - still functioning? |
| Health_Risk | Text (10) | Yes/No - public health risk? |
| Repair_Priority | Integer | 1-5 (1=highest) |
| Est_Cost | Integer | Repair cost estimate |
| Notes | Text (255) | Additional information |

**Digitize Sewer Damage Locations:**
- Add 2-4 sewer damage points
- Complete all attributes for each
- Save features

---

## Part 3: Create Erosion Polygon Layer (30 minutes)

### Task 3.1: Create Coastal Erosion Layer

**Create Layer:**
1. Click "Add" → "Create feature layer"
2. Select **"Polygon"**

**Layer Properties:**
- Name: "Typhoon_Merbok_Coastal_Erosion"
- Description: "Areas of coastal erosion caused by Typhoon Merbok"
- Tags: erosion, coastal, typhoon, damage

**Define Attributes:**

| Field Name | Type | Description |
|------------|------|-------------|
| Erosion_ID | Text (20) | Unique ID (E-001, E-002) |
| Location_Name | Text (100) | Descriptive location name |
| Erosion_Type | Text (50) | "Cliff erosion", "Beach erosion", "Bluff failure" |
| Severity | Text (20) | Minor/Moderate/Severe/Critical |
| Date_Assessed | Date | Assessment date |
| Area_SqFeet | Double | Area in square feet (auto-calculate) |
| Est_Volume_Loss_CuYd | Integer | Estimated cubic yards lost |
| Infrastructure_Risk | Text (10) | Yes/No - threatens infrastructure? |
| At_Risk_Features | Text (255) | What infrastructure is at risk |
| Mitigation_Needed | Text (255) | What mitigation is needed |
| Priority | Integer | Action priority 1-5 |
| Notes | Text (255) | Additional information |

### Task 3.2: Digitize Erosion Areas

**For Each Erosion Area:**

1. **Locate erosion area on map**
   - Zoom to coastal areas affected
   - Use satellite imagery as reference
   - If available, compare with pre-storm imagery

2. **Digitize polygon:**
   - Click "Edit" → "Add feature"
   - Click around perimeter of eroded area
   - Return to start point
   - Double-click to close polygon

3. **Fill Attributes:**

**Example Erosion Area 1:**
- Erosion_ID: E-001
- Location_Name: "North Beach Bluff"
- Erosion_Type: "Bluff failure"
- Severity: "Severe"
- Date_Assessed: 11/8/2025
- Infrastructure_Risk: "Yes"
- At_Risk_Features: "Water tank access road, transmission lines within 50 feet"
- Mitigation_Needed: "Revetment or road relocation"
- Priority: 1
- Notes: "Active erosion, bluff height ~25 feet, threatens critical infrastructure"

**Example Erosion Area 2:**
- Erosion_ID: E-002
- Location_Name: "South Shoreline"
- Erosion_Type: "Beach erosion"
- Severity: "Moderate"
- Date_Assessed: 11/8/2025
- Infrastructure_Risk: "No"
- At_Risk_Features: "None immediately"
- Mitigation_Needed: "Monitor, potential beach nourishment"
- Priority: 3
- Notes: "Beach narrowed by approximately 15 feet"

**Add 2-3 erosion areas**

4. **Calculate Area:**
   - Open attribute table
   - Select Area_SqFeet field
   - Calculate geometry
   - Values automatically filled

---

## Part 4: Style and Symbolize Layers (20 minutes)

### Task 4.1: Style Fish Racks Layer

**Configure Symbology:**
1. Click on "Typhoon_Merbok_Damaged_Fish_Racks" layer
2. Click "Styles" button
3. Choose "Types (Unique symbols)"
4. Field: Severity

**Symbol Settings:**
- **Low:** Small yellow circle
- **Medium:** Medium orange circle
- **High:** Large red circle
- **Critical:** Large red circle with outline

**Or use single symbol:**
- Red X or red cross symbol
- Size: Medium
- Label: "Damaged Fish Rack"

### Task 4.2: Style Sewer Damage Layer

**Symbology:**
1. Select layer → Styles
2. Choose symbol appropriate for sewer damage
3. Options:
   - Red square
   - Hazard symbol
   - Infrastructure symbol
4. Size by Severity if desired

### Task 4.3: Style Erosion Layer

**Symbology:**
1. Select erosion layer → Styles
2. **Fill:**
   - Semi-transparent red or orange
   - 30-50% transparency
3. **Outline:**
   - Solid red line
   - Width: 2-3 pixels

**Or style by Severity:**
- Minor: Yellow fill
- Moderate: Orange fill
- Severe: Red fill
- Critical: Dark red fill
- All with 40% transparency

### Task 4.4: Configure Labels

**Label Important Features:**
1. Fish Racks: Label with Rack_Name
2. Erosion Areas: Label with Location_Name
3. Adjust label size and placement
4. Ensure labels don't overlap

### Task 4.5: Configure Pop-ups

**For Each Layer:**
1. Click layer → Configure pop-up
2. Choose fields to display
3. Order fields logically:
   - ID and Name first
   - Damage info
   - Cost and priority
   - Notes last
4. Format nicely with field aliases
5. Save

---

## Part 5: Add Context and Reference Layers (10 minutes)

### Task 5.1: Add Reference Features

**Optional Context Layers:**
- Community infrastructure (if available)
- Roads and trails
- Buildings
- Property boundaries
- Previous coastline (if available for comparison)

**From Living Atlas:**
1. Click "Add" → "Browse Living Atlas Layers"
2. Search for relevant layers
3. Add useful context (don't overcrowd map)

### Task 5.2: Layer Organization

**Organize Layer Order:**
1. Drag layers to appropriate order:
   - Damage points (top)
   - Erosion polygons
   - Context layers
   - Basemap (bottom)

2. Group related layers:
   - Create group "Typhoon Merbok Damage"
   - Move damage layers into group

---

## Part 6: Add Map Elements (10 minutes)

### Task 6.1: Add Title

**In Map Properties:**
- Title: "Typhoon Merbok Damage Assessment"
- Subtitle: "Quinhagak, Alaska - November 2025"

### Task 6.2: Configure Legend

**Legend Settings:**
1. Click layers to include in legend
2. Rename layers for legend:
   - "Damaged Fish Racks"
   - "Sewer Infrastructure Damage"
   - "Coastal Erosion Areas"
3. Remove unnecessary layers from legend (basemap, etc.)

### Task 6.3: Prepare for Export

**Final Map Adjustments:**
1. Zoom to extent showing all damage
2. Include small buffer around area
3. Verify all features visible
4. Check labels readable
5. Ensure legend clear

---

## Part 7: Export to PDF (15 minutes)

### Task 7.1: Configure Export Settings

**Export Setup:**
1. Click "Print" button
2. Configure settings:

**Layout:**
- Page size: **Letter** (8.5" x 11") or **Tabloid** (11" x 17")
- Orientation: Choose based on map shape (likely Portrait)
- Format: **PDF**

**Map Properties:**
- Title: "Typhoon Merbok Damage Assessment - Quinhagak, Alaska"
- Date: November 8, 2025
- Scale: Use appropriate fixed scale or current extent

**Map Elements:**
- ☑ Include legend (position: right side)
- ☑ Include scale bar (position: bottom left, units: feet and miles)
- ☑ Include north arrow (position: upper right)
- Add attribution: "Data Source: Qanirtuuq Inc., Assessment Date: 11/8/2025"

**Quality:**
- DPI: **300** (for print quality)
- Quality: High

### Task 7.2: Export

1. Click "Export" or "Print"
2. Wait for processing (30-60 seconds)
3. Download PDF when ready
4. File name: "Quinhagak_Typhoon_Merbok_Damage_2025-11-08.pdf"

### Task 7.3: Review PDF

**Quality Check:**
- Open PDF in reader
- Check all elements present:
  - ✓ Title clear
  - ✓ Legend complete and readable
  - ✓ Scale bar present
  - ✓ North arrow present
  - ✓ Date shown
  - ✓ All damage locations visible
  - ✓ Text readable (not too small)
  - ✓ Colors print clearly
- Zoom to 100% and verify quality
- If issues, adjust map and re-export

---

## Part 8: Create Simplified Community Version (Optional, 15 minutes)

### Task 8.1: Create Community-Friendly Version

**Purpose:** Map for community meetings with simplified language

**Simplifications:**
1. **Layer names:**
   - "Fish Rack Locations Needing Repair"
   - "Sewer Damage Locations"
   - "Coastal Erosion Areas"

2. **Simpler symbols:**
   - Larger, clearer symbols
   - Fewer categories
   - Just "Needs Repair" vs "Critical"

3. **Larger text:**
   - Increase label sizes
   - Fewer technical terms

4. **Export:**
   - Letter size
   - 150 DPI (screen viewing)
   - File name: "Quinhagak_Merbok_Damage_Community_2025-11-08.pdf"

---

## Deliverables

### Required Submissions:

1. **✓ ArcGIS Online Web Map**
   - Saved with proper title
   - All layers created and symbolized
   - Map elements configured

2. **✓ PDF Export (Technical)**
   - Professional quality (300 DPI)
   - All map elements included
   - Appropriate for official use
   - File name: Quinhagak_Typhoon_Merbok_Damage_2025-11-08.pdf

3. **✓ Layer Attribute Tables**
   - All features digitized
   - All attributes completed
   - Data quality checked

4. **Optional: Community Version PDF**
   - Simplified for general audience
   - File name: Quinhagak_Merbok_Damage_Community_2025-11-08.pdf

---

## Assessment Criteria

### Map Content (40 points)

**Damage Point Layers (15 points):**
- ✓ Fish racks layer created with 3-5 features
- ✓ Sewer damage layer created with 2-4 features
- ✓ All required attributes completed
- ✓ Locations accurate

**Erosion Polygon Layer (15 points):**
- ✓ Layer created with 2-3 features
- ✓ Polygons properly digitized (closed, accurate)
- ✓ All attributes completed
- ✓ Areas calculated

**Context and References (10 points):**
- ✓ Appropriate basemap selected
- ✓ Additional context layers if needed
- ✓ Layers organized logically

### Cartographic Design (30 points)

**Symbolization (15 points):**
- ✓ Appropriate symbols chosen
- ✓ Clear visual hierarchy
- ✓ Colors meaningful
- ✓ Labels readable

**Map Elements (15 points):**
- ✓ Title descriptive and clear
- ✓ Legend complete and readable
- ✓ Scale bar present and appropriate
- ✓ North arrow included
- ✓ Date and source shown

### Technical Quality (20 points)

**Data Quality (10 points):**
- ✓ Features accurately located
- ✓ Attributes complete and consistent
- ✓ No topology errors
- ✓ Proper field types used

**Export Quality (10 points):**
- ✓ PDF format
- ✓ 300 DPI resolution
- ✓ All elements included
- ✓ Professional appearance
- ✓ Readable when printed

### Documentation (10 points)

- ✓ Descriptive file name
- ✓ Map saved with metadata
- ✓ Layers have descriptions
- ✓ Attribution complete

**Total: 100 points**

---

## Real-World Application

### How This Map Would Be Used:

**Recovery Planning:**
- Prioritize repairs based on severity
- Estimate total recovery costs
- Plan repair sequencing

**Funding Applications:**
- Visual documentation for FEMA
- Support for state/federal grants
- Demonstrate impact to agencies

**Community Communication:**
- Show community what was damaged
- Explain repair priorities
- Update on recovery progress

**Historical Record:**
- Document storm impacts
- Compare with future events
- Track community resilience

---

## Key Takeaways

- **Damage assessment maps document impacts** for recovery and funding
- **Point layers work well** for discrete damage locations
- **Polygon layers show extent** of area-based damage like erosion
- **Complete attributes are critical** - support cost estimates and priorities
- **Professional maps support funding** - quality matters
- **Multiple versions serve different audiences** - technical vs. community
- **Maps communicate visually** - more effective than text alone
- **Documentation creates historical record** - valuable for future planning

---

## Next Activity

[Activity 4: Village Relocation Site Planning Map](./activity-04-relocation-site-map.md)

Apply these skills to create a forward-looking planning map for proposed village relocation.

---

**Congratulations!** You've created a professional damage assessment map documenting real-world impacts and supporting community recovery efforts.
