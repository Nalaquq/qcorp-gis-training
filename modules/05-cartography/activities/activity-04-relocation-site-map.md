# Activity 4: Village Relocation Site Planning Map

**Training Date:** November 8, 2025
**Duration:** 150 minutes
**Prerequisites:** Lessons 1-4, 7-8 completed, Activity 3 completed

---

## Activity Overview

Create a comprehensive planning map for a proposed village relocation site near Quinhagak airport. This map will show proposed infrastructure, planned utility networks, and areas requiring drone survey data collection. The map will support community planning, engineering design, and funding applications.

---

## Learning Objectives

By completing this activity, you will be able to:

1. Create polygon layers for proposed infrastructure and survey areas
2. Create line layers for utility networks and roads
3. Design a forward-looking planning map
4. Apply cartographic principles for technical planning
5. Create multiple map versions for different audiences
6. Export professional planning documents

---

## Background

### Village Relocation Planning

**Context:**
Many Alaska Native villages face threats from:
- Coastal erosion
- Flooding
- Permafrost degradation
- Climate change impacts

**Quinhagak Considerations:**
- Evaluating potential relocation sites
- Site near airport being assessed
- Need comprehensive planning
- Infrastructure design required
- Community input essential

**Planning Needs:**
- Identify areas for detailed survey (UAS orthomosaics)
- Plan infrastructure locations
- Design utility networks
- Estimate costs and phasing
- Engage community in planning

---

## Part 1: Project Setup (15 minutes)

### Task 1.1: Create New Map

1. **Sign in to ArcGIS Online**
2. **Create New Map**
3. **Save Map:**
   - Title: "Proposed Village Relocation Site - Quinhagak"
   - Tags: "relocation", "planning", "quinhagak", "infrastructure", "proposed"
   - Summary: "Planning map for proposed village relocation site near airport"
   - Save in appropriate folder

### Task 1.2: Select Basemap and Location

**Basemap Selection:**
- Use "Imagery" or "Imagery with Labels"
- If you have drone orthomosaic of area, use that
- Otherwise, best available satellite imagery

**Locate Site:**
1. Zoom to Quinhagak area
2. Find airport location
3. Identify proposed relocation site
4. Position map to show site and surroundings

---

## Part 2: Create UAS Flight Area Polygons (30 minutes)

### Task 2.1: Create UAS Flight Areas Layer

**Purpose:** Define areas needing high-resolution drone orthomosaic collection for detailed planning

**Create Layer:**
1. Click "Add" → "Create feature layer"
2. Select **"Polygon"**
3. Click "Next"

**Layer Properties:**
- Name: "UAS_Orthomosaic_Flight_Areas"
- Description: "Areas requiring UAS orthomosaic collection for site planning"
- Tags: UAS, drone, orthomosaic, survey, planning
- Click "Next"

**Define Attributes:**

| Field Name | Type | Length | Description |
|------------|------|--------|-------------|
| Flight_Area_ID | Text | 20 | Unique ID (FA-001, FA-002) |
| Area_Name | Text | 100 | Descriptive name |
| Priority | Integer | - | 1-5 (1=highest priority) |
| Flight_Altitude | Integer | - | Recommended altitude (feet) |
| Overlap_Percent | Text | 20 | "80/80" (standard) |
| Status | Text | 50 | "Pending", "Scheduled", "Completed" |
| Planned_Date | Date | - | When flight scheduled |
| Date_Flown | Date | - | Actual flight date |
| Area_Acres | Double | - | Area in acres (calculate) |
| Est_Images | Integer | - | Estimated image count |
| Purpose | Text | 255 | Why this area needs mapping |
| Phase | Text | 20 | "Phase 1", "Phase 2", etc. |
| Notes | Text | 255 | Additional information |

**Create Layer**

### Task 2.2: Digitize Flight Areas

**Flight Area 1: Main Infrastructure Zone**
1. Click "Edit" → "Add feature"
2. Digitize polygon around proposed main development area
3. Fill attributes:
   - Flight_Area_ID: FA-001
   - Area_Name: "Main Infrastructure Development Zone"
   - Priority: 1
   - Flight_Altitude: 200
   - Overlap_Percent: "80/80"
   - Status: "Pending"
   - Purpose: "High-resolution base map for engineering design, infrastructure planning"
   - Phase: "Phase 1"
   - Notes: "Priority area containing proposed water treatment plant, roads, and utilities"

**Flight Area 2: Residential Zone**
1. Add new feature
2. Digitize polygon for proposed residential area
3. Fill attributes:
   - Flight_Area_ID: FA-002
   - Area_Name: "Proposed Residential Area"
   - Priority: 2
   - Flight_Altitude: 150
   - Overlap_Percent: "80/80"
   - Status: "Pending"
   - Purpose: "Detailed mapping for lot layout and residential planning"
   - Phase: "Phase 2"
   - Notes: "Lower altitude for higher resolution lot planning"

**Flight Area 3: Environmental Buffer Zone**
1. Add new feature
2. Digitize polygon for environmental/buffer areas
3. Fill attributes:
   - Flight_Area_ID: FA-003
   - Area_Name: "Environmental Assessment Area"
   - Priority: 3
   - Flight_Altitude: 250
   - Overlap_Percent: "75/75"
   - Status: "Pending"
   - Purpose: "Vegetation mapping and environmental assessment"
   - Phase: "Phase 1"
   - Notes: "Broader coverage for environmental planning"

**Add 2-3 total flight areas**

4. **Calculate Areas:**
   - Open attribute table
   - Calculate Area_Acres field
   - Save

---

## Part 3: Create Proposed Infrastructure Polygons (30 minutes)

### Task 3.1: Create Proposed Infrastructure Layer

**Purpose:** Show locations and footprints of proposed facilities

**Create Layer:**
1. Click "Add" → "Create feature layer"
2. Select **"Polygon"**

**Layer Properties:**
- Name: "Proposed_Infrastructure_Sites"
- Description: "Proposed infrastructure facility locations and footprints"
- Tags: infrastructure, proposed, planning, facilities

**Define Attributes:**

| Field Name | Type | Description |
|------------|------|-------------|
| Facility_ID | Text (20) | Unique ID (INF-001, INF-002) |
| Facility_Name | Text (100) | Name of facility |
| Facility_Type | Text (50) | "Water Treatment", "School", "Clinic", etc. |
| Status | Text | 50 | "Proposed", "Planned", "Designed", "Approved" |
| Phase | Text (20) | "Phase 1", "Phase 2", "Future" |
| Priority | Integer | 1-5 (1=highest) |
| Size_SqFeet | Double | Building/facility size |
| Est_Cost | Integer | Estimated construction cost |
| Funding_Status | Text (50) | "Unfunded", "Partially Funded", "Funded" |
| Design_Status | Text (50) | "Conceptual", "Preliminary", "Final" |
| Notes | Text (255) | Additional information |

### Task 3.2: Digitize Proposed Facilities

**Water Treatment Plant:**
1. Digitize polygon at proposed location
2. Attributes:
   - Facility_ID: INF-001
   - Facility_Name: "New Water Treatment Plant"
   - Facility_Type: "Water Treatment"
   - Status: "Proposed"
   - Phase: "Phase 1"
   - Priority: 1
   - Est_Cost: 5000000
   - Funding_Status: "Partially Funded"
   - Design_Status: "Preliminary"
   - Notes: "Critical infrastructure, size based on population projections"

**Additional Facilities:**
Create polygons for:
- Community center/tribal office
- School
- Health clinic
- Power generation facility
- Storage facilities
- Open space/park areas

**Add 3-5 proposed infrastructure sites**

---

## Part 4: Create Proposed Sewer Lines (25 minutes)

### Task 4.1: Create Proposed Sewer Lines Layer

**Create Layer:**
1. Click "Add" → "Create feature layer"
2. Select **"Line"**

**Layer Properties:**
- Name: "Proposed_Sewer_Lines"
- Description: "Proposed sewer infrastructure network for relocation site"
- Tags: sewer, utilities, proposed, infrastructure, planning

**Define Attributes:**

| Field Name | Type | Description |
|------------|------|-------------|
| Line_ID | Text (20) | Unique ID (S-001, S-002) |
| Line_Type | Text (50) | "Main", "Lateral", "Service", "Force Main" |
| Diameter_Inches | Integer | Pipe diameter |
| Material | Text (50) | "PVC", "HDPE", "Ductile Iron" |
| Status | Text (50) | "Proposed", "Designed", "Approved" |
| Phase | Text (20) | Construction phase |
| Length_Feet | Double | Line length (calculate) |
| Est_Cost_PerFoot | Integer | Cost per linear foot |
| Est_Total_Cost | Integer | Total line cost |
| Priority | Integer | 1-5 installation priority |
| Connects_To | Text (50) | What it connects to |
| Notes | Text (255) | Additional information |

### Task 4.2: Digitize Sewer Lines

**Main Sewer Line:**
1. Click "Edit" → "Add feature"
2. Draw line from treatment plant through site
3. Attributes:
   - Line_ID: S-001
   - Line_Type: "Main"
   - Diameter_Inches: 8
   - Material: "HDPE"
   - Status: "Proposed"
   - Phase: "Phase 1"
   - Priority: 1
   - Est_Cost_PerFoot: 150
   - Connects_To: "Water Treatment Plant"
   - Notes: "Primary sewer main, connects all zones"

**Lateral Lines:**
Create lines branching from main:
- Secondary mains to residential areas
- Service laterals to facilities
- Collection network

**Drawing Tips:**
- Start at treatment plant
- Follow logical routing (downslope if possible)
- Connect to all facilities and residential zones
- Use snapping to ensure connections
- Consider road alignments

**Add 5-8 sewer lines total**

4. **Calculate Lengths:**
   - Open attribute table
   - Calculate Length_Feet
   - Calculate Est_Total_Cost (Length * Cost_Per_Foot)

---

## Part 5: Create Proposed Road Network (25 minutes)

### Task 5.1: Create Proposed Roads Layer

**Create Layer:**
1. Click "Add" → "Create feature layer"
2. Select **"Line"**

**Layer Properties:**
- Name: "Proposed_Road_Network"
- Description: "Proposed road network for relocation site"
- Tags: roads, proposed, infrastructure, transportation

**Define Attributes:**

| Field Name | Type | Description |
|------------|------|-------------|
| Road_ID | Text (20) | Unique ID (R-001, R-002) |
| Road_Name | Text (100) | Street name (if designated) |
| Road_Type | Text (50) | "Primary", "Secondary", "Access" |
| Width_Feet | Integer | Road width |
| Surface_Type | Text (50) | "Gravel", "Paved", "Boardwalk" |
| Status | Text (50) | "Proposed", "Designed", "Approved" |
| Phase | Text (20) | Construction phase |
| Length_Feet | Double | Road length (calculate) |
| Est_Cost_PerFoot | Integer | Cost per linear foot |
| Est_Total_Cost | Integer | Total cost |
| Priority | Integer | 1-5 construction priority |
| Connects | Text (255) | What areas it connects |
| Notes | Text (255) | Additional information |

### Task 5.2: Digitize Road Network

**Main Access Road:**
1. Draw line from existing road/airport to site
2. Attributes:
   - Road_ID: R-001
   - Road_Name: "Main Access Road"
   - Road_Type: "Primary"
   - Width_Feet: 24
   - Surface_Type: "Gravel"
   - Status: "Proposed"
   - Phase: "Phase 1"
   - Priority: 1
   - Est_Cost_PerFoot: 200
   - Connects: "Airport access to village site"
   - Notes: "Primary access, requires permits"

**Internal Road Network:**
Create roads connecting:
- Main facilities
- Residential areas
- Treatment plant
- Community buildings

**Road Types:**
- Primary: 24' wide, main routes
- Secondary: 20' wide, residential streets
- Access: 16' wide, facility access

**Add 6-10 road segments**

4. **Calculate costs**

---

## Part 6: Style and Symbolize All Layers (20 minutes)

### Task 6.1: Style UAS Flight Areas

**Symbolization:**
1. Select layer → Styles
2. Style by Priority field
3. **Colors:**
   - Priority 1: Red outline, light red fill (30% transparent)
   - Priority 2: Orange outline, light orange fill
   - Priority 3: Yellow outline, light yellow fill
4. **Outline:** 2-3 pixel width
5. **Labels:** Show Area_Name

### Task 6.2: Style Proposed Infrastructure

**Symbolization:**
1. Style by Facility_Type
2. **Colors/Symbols:**
   - Water Treatment: Blue polygon
   - School: Purple polygon
   - Clinic: Red cross polygon
   - Community Center: Green polygon
   - Other: Gray polygon
3. **Fill:** 50% transparency
4. **Outline:** Solid, 2 pixels
5. **Labels:** Show Facility_Name

### Task 6.3: Style Sewer Lines

**Symbolization:**
1. Style by Line_Type
2. **Colors:**
   - Main: Dark brown, thick (4 pixels)
   - Lateral: Medium brown, medium (2 pixels)
   - Service: Light brown, thin (1 pixel)
3. **Line style:** Solid or dashed (to differentiate from roads)
4. **Labels:** Show Line_ID on main lines

### Task 6.4: Style Road Network

**Symbolization:**
1. Style by Road_Type
2. **Colors:**
   - Primary: Black, thick (5 pixels)
   - Secondary: Gray, medium (3 pixels)
   - Access: Light gray, thin (2 pixels)
3. **Line style:** Solid double line (if available)
4. **Labels:** Show Road_Name where designated

### Task 6.5: Configure Pop-ups

**For Each Layer:**
- Configure pop-ups with relevant fields
- Format nicely
- Include cost estimates
- Show status and phase
- Order fields logically

---

## Part 7: Add Context and Annotations (10 minutes)

### Task 7.1: Add Context Layers

**Reference Features:**
- Airport boundary
- Existing infrastructure
- Environmental constraints
- Elevation contours (if available)
- Water bodies
- Property boundaries

### Task 7.2: Layer Organization

**Organize Layers:**
1. Create group: "Proposed Infrastructure"
2. Move all proposed layers into group
3. Order logically:
   - Roads (top)
   - Sewer lines
   - Infrastructure polygons
   - Flight areas
   - Context layers
   - Basemap

---

## Part 8: Export Technical Version (15 minutes)

### Task 8.1: Prepare for Export

1. **Zoom to final extent**
   - Show entire site
   - Include airport for context
   - Small buffer around site

2. **Verify all elements:**
   - All layers visible
   - Labels clear
   - Legend organized
   - Symbology appropriate

### Task 8.2: Configure and Export

**Export Settings:**
- **Page size:** Tabloid (11" x 17")
- **Orientation:** Choose best (likely Landscape)
- **Format:** PDF

**Title:** "Proposed Village Relocation Site - Quinhagak, Alaska"
**Subtitle:** "Preliminary Site Plan - November 2025"

**Map Elements:**
- ☑ Legend (all layers, right side)
- ☑ Scale bar (feet and miles, bottom)
- ☑ North arrow (upper right)
- **Attribution:** "Prepared by: [Name/Organization], Date: 11/8/2025"
- **Note:** "Proposed locations subject to engineering review and design"

**Quality:**
- DPI: 300
- Resolution: High

**Export:**
- Click Export
- File name: "Quinhagak_Relocation_Site_Technical_2025-11-08.pdf"

**Review PDF carefully**

---

## Part 9: Create Community Presentation Version (20 minutes)

### Task 9.1: Simplify for Community Audience

**Purpose:** Map for community meetings, easier to understand

**Simplifications:**

1. **Layer Names (Rename for Legend):**
   - "Areas We'll Map with Drones"
   - "New Buildings and Facilities"
   - "New Sewer Lines"
   - "New Roads"

2. **Reduce Detail:**
   - Show only main roads (hide access roads)
   - Show only main sewer lines
   - Combine less important layers

3. **Simplify Labels:**
   - Use plain language
   - Larger text
   - Fewer technical details

4. **Color Scheme:**
   - Bright, easy-to-distinguish colors
   - High contrast
   - Clear differences

### Task 9.2: Export Community Version

**Export Settings:**
- Page size: Letter (8.5" x 11")
- Orientation: Landscape
- DPI: 150 (for screen/projector)

**Title:** "Proposed New Village Site"
**Subtitle:** "What It Could Look Like"

**Simplify Legend:**
- Clear, non-technical labels
- Fewer categories
- Larger symbols

**Export:**
- File name: "Quinhagak_Relocation_Community_2025-11-08.pdf"

---

## Deliverables

### Required Submissions:

1. **✓ ArcGIS Online Web Map**
   - All four layers created
   - Complete attributes
   - Professional styling

2. **✓ Technical PDF (Tabloid)**
   - High resolution (300 DPI)
   - All technical details
   - Professional appearance
   - File: Quinhagak_Relocation_Site_Technical_2025-11-08.pdf

3. **✓ Community PDF (Letter)**
   - Simplified for general audience
   - 150 DPI
   - Plain language
   - File: Quinhagak_Relocation_Community_2025-11-08.pdf

4. **✓ Layer Data**
   - UAS Flight Areas: 2-3 polygons, complete attributes
   - Proposed Infrastructure: 3-5 sites, complete attributes
   - Proposed Sewer Lines: 5-8 lines, complete attributes, calculated lengths
   - Proposed Road Network: 6-10 roads, complete attributes, calculated lengths

---

## Assessment Criteria

### Layer Creation (40 points)

**UAS Flight Areas (10 points):**
- ✓ Layer created with 2-3 features
- ✓ Attributes complete
- ✓ Areas calculated
- ✓ Logical coverage

**Proposed Infrastructure (10 points):**
- ✓ Layer created with 3-5 facilities
- ✓ Attributes complete including costs
- ✓ Appropriate locations
- ✓ Variety of facility types

**Sewer Lines (10 points):**
- ✓ Layer created with 5-8 lines
- ✓ Logical network design
- ✓ Lines properly connected
- ✓ Lengths and costs calculated

**Road Network (10 points):**
- ✓ Layer created with 6-10 roads
- ✓ Logical network design
- ✓ Different road types
- ✓ Lengths and costs calculated

### Cartographic Design (30 points)

**Symbolization (15 points):**
- ✓ Appropriate symbols for each layer
- ✓ Clear visual distinction between layers
- ✓ Color scheme logical and effective
- ✓ Labels readable and well-placed
- ✓ Legend clear

**Map Layout (15 points):**
- ✓ Title descriptive
- ✓ All required map elements
- ✓ Professional appearance
- ✓ Appropriate scale
- ✓ Context provided

### Technical Quality (20 points)

**Data Quality (10 points):**
- ✓ Features accurately placed
- ✓ Networks properly connected
- ✓ Attributes complete
- ✓ Calculations correct

**Exports (10 points):**
- ✓ Both PDFs created
- ✓ Appropriate resolution
- ✓ Elements included
- ✓ Professional quality

### Multiple Audiences (10 points)

- ✓ Technical version appropriate for engineers/planners
- ✓ Community version simplified and accessible
- ✓ Different levels of detail appropriate
- ✓ Both versions professionally produced

**Total: 100 points**

---

## Real-World Application

### How These Maps Would Be Used:

**Engineering Design:**
- Base for detailed engineering plans
- Cost estimation
- Phasing and sequencing
- Permit applications

**Community Engagement:**
- Visual communication of proposal
- Facilitate community input
- Show potential impacts
- Build understanding and support

**Funding Applications:**
- Support grant applications
- Show comprehensive planning
- Demonstrate need
- Provide cost estimates

**Environmental Assessment:**
- Identify survey needs (UAS areas)
- Show infrastructure footprint
- Plan mitigation measures
- Support permitting

**Decision Making:**
- Compare alternatives
- Evaluate feasibility
- Plan phasing
- Allocate resources

---

## Key Takeaways

- **Planning maps show proposed, not existing features**
- **Multiple layer types work together** (polygons for areas, lines for networks)
- **Line networks require careful digitizing** - connections matter
- **Cost estimation supported by GIS** - calculate lengths/areas automatically
- **Different audiences need different maps** - technical vs. community versions
- **Planning maps evolve** - expect revisions as design progresses
- **Visual communication is powerful** - maps help people understand complex plans
- **Professional appearance builds credibility** - quality matters for funding and support

---

## Congratulations!

You've created a comprehensive planning map showing:
- Proposed infrastructure locations
- Utility network design
- Survey data collection needs
- Cost estimates
- Phased implementation

These skills are directly applicable to real community planning projects and demonstrate professional GIS capabilities.

---

## Next Activity

[Activity 5: FAA Development Approval Map](./activity-05-faa-development-approval-map.md)

Apply these skills to create a regulatory approval map for FAA and NVK, incorporating external data sources and buffer analysis to ensure proposed developments respect Native Allotment boundaries.

---

**Your maps are building toward real-world community outcomes!**
