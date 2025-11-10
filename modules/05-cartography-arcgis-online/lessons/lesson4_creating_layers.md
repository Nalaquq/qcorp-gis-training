# Lesson 4: Creating Custom Vector Layers

**Duration:** 90 minutes
**Prerequisites:** Lesson 2 - Understanding Vector Data
**Training Date Reference:** November 8, 2025

---

## Lesson Overview

This lesson teaches you how to create custom vector layers in ArcGIS Online. You'll learn to create point, line, and polygon layers, define attributes, digitize features, and follow best practices for accurate data collection.

---

## Learning Objectives

By the end of this lesson, you will be able to:

1. Create new point layers in ArcGIS Online
2. Create new line layers in ArcGIS Online
3. Create new polygon layers in ArcGIS Online
4. Define custom attribute fields
5. Digitize features accurately
6. Edit existing features
7. Use snapping and editing tools
8. Apply best practices for data quality

---

## Creating New Layers in ArcGIS Online

### Accessing the Create Layer Tool

**In Map Viewer:**
1. Open your map or create new map
2. Click **"Add"** button (top left)
3. Select **"Create feature layer"** or **"New sketch layer"**

**Two Options:**

**Feature Layer (Hosted):**
- Stored in your ArcGIS Online content
- Permanent layer
- Can be shared and reused
- **Use for:** Important data you'll keep and update

**Sketch Layer:**
- Temporary layer
- Exists only in current map
- Not saved to content
- **Use for:** Quick notes, temporary annotations

**For your work:** Use Feature Layers (permanent and shareable)

---

## Creating Point Layers

### Step-by-Step: Create Point Layer

**1. Initiate Creation:**
- Click "Add" → "Create feature layer"
- Select **"Point"** as feature type
- Click "Next"

**2. Define Layer Properties:**
- **Layer name:** Descriptive and clear
  - Good: "Typhoon_Merbok_Damaged_Fish_Racks"
  - Bad: "Points1", "Layer"
- **Description:** What the layer contains
- **Tags:** Keywords for searching (typhoon, damage, infrastructure)
- Click "Next"

**3. Define Attribute Fields:**

**Default Fields (always included):**
- ObjectID - Unique identifier (automatic)
- Creation/Edit dates (automatic)
- Creator/Editor (automatic)

**Add Custom Fields:**

Click "Add Field" for each attribute needed:

**Example: Damaged Fish Racks Layer**

| Field Name | Type | Description | Required? |
|------------|------|-------------|-----------|
| Rack_Name | Text (50) | Name/location of rack | Yes |
| Damage_Type | Text (50) | Type of damage | Yes |
| Severity | Text (20) | Low/Medium/High/Critical | Yes |
| Date_Assessed | Date | When damage documented | Yes |
| Est_Repair_Cost | Integer | Estimated cost in dollars | No |
| Repairable | Text (10) | Yes/No | Yes |
| Notes | Text (255) | Additional information | No |
| Photo_URL | Text (255) | Link to photo | No |

**Field Types to Choose:**
- **Text (String):** Names, descriptions, categories
- **Integer:** Whole numbers (counts, years)
- **Double:** Decimal numbers (measurements, costs)
- **Date:** Dates
- **Yes/No:** True/false values

**4. Field Settings:**

For each field, configure:
- **Display name:** How it appears to users
- **Alias:** User-friendly name
- **Length:** (for text) Max characters (50, 100, 255)
- **Allow nulls:** Can field be empty?
- **Default value:** Pre-filled value for new features

**5. Create Layer:**
- Review settings
- Click "Create"
- Layer added to map and your Content

### Digitizing Points

**Adding Point Features:**

**Method 1: Click to Place**
1. Select your point layer
2. Click "Edit" button
3. Choose "Add feature"
4. Click on map where point should be
5. Enter attribute information in form
6. Click "Save" or "Add another"

**Method 2: Search Location**
1. Use search box to find address or place
2. Add point at that location
3. Enter attributes

**Best Practices:**
- Zoom in for accuracy
- Use satellite/aerial imagery basemap
- Verify location before saving
- Complete all required attributes
- Take photos for Photo_URL if possible

**Example: Adding Damaged Fish Rack**
1. Zoom to fish rack location
2. Switch to satellite basemap
3. Click "Add feature"
4. Click exact location
5. Fill attributes:
   - Rack_Name: "North Beach Rack"
   - Damage_Type: "Structural failure"
   - Severity: "High"
   - Date_Assessed: 11/8/2025
   - Est_Repair_Cost: 5000
   - Repairable: "Yes"
   - Notes: "Main support beam damaged"

---

## Creating Line Layers

### Step-by-Step: Create Line Layer

**1. Initiate Creation:**
- Click "Add" → "Create feature layer"
- Select **"Line"** as feature type
- Click "Next"

**2. Define Layer Properties:**
- **Layer name:** "Proposed_Sewer_Lines"
- **Description:** "Proposed sewer infrastructure for village relocation site"
- **Tags:** relocation, sewer, proposed, infrastructure
- Click "Next"

**3. Define Attribute Fields:**

**Example: Proposed Sewer Lines**

| Field Name | Type | Description |
|------------|------|-------------|
| Line_ID | Text (20) | Unique identifier (S-001, S-002) |
| Line_Type | Text (50) | "Main", "Lateral", "Service" |
| Diameter_Inches | Integer | Pipe diameter |
| Material | Text (50) | "PVC", "HDPE", etc. |
| Status | Text (50) | "Proposed", "Designed", "Approved" |
| Phase | Text (20) | "Phase 1", "Phase 2", etc. |
| Length_Feet | Double | Length in feet (calculated) |
| Est_Cost | Integer | Estimated installation cost |
| Priority | Integer | 1-5 (1=highest) |
| Notes | Text (255) | Additional information |

**4. Create Layer**

### Digitizing Lines

**Adding Line Features:**

1. Select line layer
2. Click "Edit" → "Add feature"
3. Click to place first vertex (start point)
4. Click to add more vertices along the line
5. Double-click to end line
6. Enter attribute information
7. Save

**Drawing Techniques:**

**Straight Lines:**
- Click start point
- Click end point
- Double-click to finish

**Curved/Complex Lines:**
- Click frequently to follow curves
- Zoom in for detailed sections
- Use more vertices for accuracy

**Connected Networks:**
- End line exactly where another starts
- Use snapping (automatically connects nearby points)
- Verify no gaps in network

**Best Practices:**
- Follow actual/proposed alignment
- Use consistent vertex density
- Snap to existing features
- Start/end at logical connection points
- Measure and record length

**Example: Adding Proposed Sewer Line**
1. Zoom to relocation site
2. Use orthomosaic or site plan as reference
3. Click "Add feature"
4. Click at sewer main connection point
5. Click along proposed route
6. Click at each turn or junction
7. Double-click at end point
8. Fill attributes:
   - Line_ID: "S-001"
   - Line_Type: "Main"
   - Diameter_Inches: 8
   - Material: "HDPE"
   - Status: "Proposed"
   - Phase: "Phase 1"
   - Priority: 1
   - Notes: "Main sewer line to treatment facility"

---

## Creating Polygon Layers

### Step-by-Step: Create Polygon Layer

**1. Initiate Creation:**
- Click "Add" → "Create feature layer"
- Select **"Polygon"** as feature type
- Click "Next"

**2. Define Layer Properties:**
- **Layer name:** "Coastal_Erosion_Areas_Typhoon_Merbok"
- **Description:** "Areas of coastal erosion caused by Typhoon Merbok"
- **Tags:** erosion, typhoon, coastal, damage
- Click "Next"

**3. Define Attribute Fields:**

**Example: Erosion Areas**

| Field Name | Type | Description |
|------------|------|-------------|
| Area_ID | Text (20) | Unique identifier (E-001, E-002) |
| Location_Name | Text (100) | Descriptive location |
| Erosion_Severity | Text (50) | "Minor", "Moderate", "Severe", "Critical" |
| Date_Assessed | Date | When documented |
| Area_SqFeet | Double | Area in square feet (calculated) |
| Est_Volume_Loss | Integer | Cubic yards eroded |
| Infrastructure_Risk | Text (10) | "Yes"/"No" |
| Mitigation_Needed | Text (255) | What mitigation is needed |
| Priority | Integer | 1-5 for action priority |
| Notes | Text (255) | Additional information |

**4. Create Layer**

**Example: UAS Flight Areas**

For village relocation planning:

| Field Name | Type | Description |
|------------|------|-------------|
| Flight_Area_ID | Text (20) | FA-001, FA-002, etc. |
| Area_Name | Text (100) | Descriptive name |
| Priority | Integer | 1-5 (1=highest) |
| Flight_Altitude | Integer | Recommended altitude (feet) |
| Status | Text (50) | "Pending", "Scheduled", "Completed" |
| Date_Flown | Date | When surveyed |
| Area_Acres | Double | Area in acres (calculated) |
| Est_Images | Integer | Estimated image count |
| Purpose | Text (255) | Why this area needs mapping |
| Notes | Text (255) | Additional information |

### Digitizing Polygons

**Adding Polygon Features:**

1. Select polygon layer
2. Click "Edit" → "Add feature"
3. Click to place vertices around perimeter
4. Return to start point (close the polygon)
5. Double-click to finish
6. Enter attribute information
7. Save

**Drawing Techniques:**

**Simple Shapes:**
- Click at each corner
- Return to start point
- Double-click to close

**Complex Shapes:**
- Use more vertices for irregular boundaries
- Zoom in for detailed edges
- Follow natural features (coastline, etc.)

**Tracing from Imagery:**
- Use high-resolution basemap
- Zoom in close
- Click along visible boundary
- Adjust vertices as needed

**Best Practices:**
- Close polygons completely (no gaps)
- Don't overlap unless intentional
- Use adequate vertices for accuracy (but not excessive)
- Follow actual boundaries
- Snap to adjacent polygons if needed

**Example: Adding Erosion Area**
1. Zoom to eroded coastline
2. Use before/after imagery if available
3. Click "Add feature"
4. Click along eroded cliff edge
5. Click around perimeter of eroded area
6. Return to start point and double-click
7. Fill attributes:
   - Area_ID: "E-001"
   - Location_Name: "North Beach Bluff"
   - Erosion_Severity: "Severe"
   - Date_Assessed: 11/8/2025
   - Infrastructure_Risk: "Yes"
   - Mitigation_Needed: "Revetment or relocation"
   - Priority: 1
   - Notes: "Active erosion threatening buildings"

**Example: Adding UAS Flight Area**
1. Zoom to relocation site
2. Click "Add feature"
3. Click corners of area needing mapping
4. Close polygon
5. Fill attributes:
   - Flight_Area_ID: "FA-001"
   - Area_Name: "Proposed Infrastructure Zone"
   - Priority: 1
   - Flight_Altitude: 200
   - Status: "Pending"
   - Purpose: "High-resolution base map for engineering"
   - Notes: "Priority for Phase 1 planning"

---

## Editing Existing Features

### Editing Geometry (Shape/Location)

**Move Feature:**
1. Select feature
2. Click and drag to new location
3. Save

**Reshape Line or Polygon:**
1. Select feature
2. Click "Edit vertices"
3. Drag vertices to new positions
4. Add vertices: Click on line segment
5. Delete vertices: Select and press Delete
6. Save

**Split Features:**
- Divide one feature into two
- Useful for roads, parcels, areas

**Merge Features:**
- Combine multiple features into one
- Useful for adjacent areas

### Editing Attributes

**Edit Single Feature:**
1. Click on feature
2. Pop-up appears
3. Click "Edit"
4. Change attribute values
5. Save

**Edit Multiple Features:**
1. Open attribute table
2. Find feature rows
3. Click in cells to edit
4. Save changes

**Batch Edit:**
- Select multiple features
- Update common attribute
- All selected features updated at once

---

## Advanced Editing Tools

### Snapping

**What is Snapping?**
- Automatic connection to nearby features
- Ensures features connect exactly
- Prevents gaps and overlaps

**When to Use:**
- Connecting roads or utilities
- Adjacent polygons sharing boundaries
- Network connections (sewer lines)

**Enable Snapping:**
- Usually automatic in ArcGIS Online
- Can configure snapping tolerance
- Snap to vertices, edges, or endpoints

**Example:**
When drawing proposed sewer lines:
- Start line snaps to end of existing line
- Ensures continuous network
- No gaps at junctions

### Calculate Geometry

**Automatic Calculations:**
- Length (for lines)
- Area (for polygons)
- Perimeter (for polygons)

**How to Calculate:**
1. Open attribute table
2. Select field (e.g., Length_Feet)
3. Choose "Calculate"
4. Select geometry calculation
5. Values automatically filled

**Useful For:**
- Recording actual dimensions
- Cost estimation (based on length/area)
- Progress tracking (area completed)

---

## Data Quality Best Practices

### Accuracy

**Location Accuracy:**
- Zoom in when digitizing
- Use high-resolution basemaps
- Verify with GPS if available
- Cross-reference multiple sources

**Attribute Accuracy:**
- Complete all required fields
- Double-check values
- Use consistent terminology
- Verify dates and numbers

### Consistency

**Feature Consistency:**
- Similar features same type (all buildings as polygons, not mixed)
- Same level of detail across features
- Consistent scale of digitizing

**Attribute Consistency:**
- Use pick lists/domains for categories
- Consistent capitalization ("High" not "high" or "HIGH")
- Consistent units (all feet or all meters)
- Consistent date formats

**Example Pick List Values:**
- Severity: "Low", "Medium", "High", "Critical" (not "low", "med", "severe", etc.)
- Status: "Proposed", "Designed", "Approved", "Under Construction", "Complete"

### Completeness

**Complete Features:**
- All planned features digitized
- No missing sections
- Coverage complete

**Complete Attributes:**
- All required fields filled
- Optional fields filled when information available
- No blank critical fields

**Complete Documentation:**
- Layer description
- Attribute field definitions
- Data source noted
- Collection date recorded

---

## Common Mistakes and Solutions

### Points

**❌ Mistake:** Point in wrong location
**✅ Solution:** Select and drag to correct location, or delete and recreate

**❌ Mistake:** Missing required attributes
**✅ Solution:** Open attribute table, find feature, complete fields

### Lines

**❌ Mistake:** Lines don't connect at junctions
**✅ Solution:** Use snapping, or edit vertices to connect exactly

**❌ Mistake:** Too few vertices (looks blocky)
**✅ Solution:** Edit vertices, add more along curves

**❌ Mistake:** Too many vertices (file size large, unnecessary detail)
**✅ Solution:** Remove excess vertices on straight sections

### Polygons

**❌ Mistake:** Polygon not closed
**✅ Solution:** Edit vertices, connect last point to first point

**❌ Mistake:** Gaps between adjacent polygons
**✅ Solution:** Enable snapping, align shared boundaries

**❌ Mistake:** Unwanted overlaps
**✅ Solution:** Edit boundaries to eliminate overlap

**❌ Mistake:** Self-intersecting polygon (lines cross)
**✅ Solution:** Redraw or edit vertices to eliminate crossing

---

## Workflow Example: Creating Relocation Map Layers

### Step 1: Plan Your Layers

**Layers Needed:**
1. Proposed_Sewer_Lines (lines)
2. Proposed_Roads (lines)
3. UAS_Flight_Areas (polygons)
4. Proposed_Infrastructure (polygons)

### Step 2: Create Each Layer

**For each layer:**
1. Define what it will contain
2. Plan attribute fields
3. Create layer with appropriate geometry type
4. Define all attribute fields

### Step 3: Digitize Features

**Systematic Approach:**
1. Start with reference layers (basemap, orthomosaic)
2. Digitize one layer at a time
3. Complete all features in layer
4. Review and check quality
5. Move to next layer

### Step 4: Quality Check

**Review:**
- All features digitized?
- All attributes complete?
- Features in correct locations?
- No topology errors?
- Layer visible and styled?

### Step 5: Document

**Add Metadata:**
- Layer description
- Data source
- Collection date
- Contact person
- Use restrictions

---

## Review Questions

1. What are the steps to create a new point layer in ArcGIS Online?
2. What's the difference between a feature layer and a sketch layer?
3. What attribute fields would you create for a proposed roads layer?
4. How do you digitize a line feature?
5. How do you ensure polygon boundaries close properly?
6. What is snapping and when is it useful?
7. How can you calculate the length of a line feature?
8. What are three best practices for data quality?

---

## Practical Exercise

**Create Practice Layers:**

**Exercise 1: Point Layer**
Create a layer for community facilities:
- Layer name: "Community_Facilities"
- Add fields: Facility_Name, Type, Status, Contact
- Digitize 5 facilities in Quinhagak

**Exercise 2: Line Layer**
Create a layer for boardwalks:
- Layer name: "Boardwalk_Sections"
- Add fields: Section_ID, Condition, Width_Feet, Needs_Repair
- Digitize 3 boardwalk sections

**Exercise 3: Polygon Layer**
Create a layer for traditional use areas:
- Layer name: "Traditional_Use_Areas"
- Add fields: Area_Name, Use_Type, Season, Access
- Digitize 2 traditional use areas

---

## Key Takeaways

- **ArcGIS Online makes it easy** to create custom layers
- **Plan attribute fields carefully** before creating layer
- **Choose appropriate geometry type** (point, line, or polygon)
- **Zoom in for accuracy** when digitizing
- **Use snapping** to connect features properly
- **Complete attributes immediately** - don't leave blank
- **Be consistent** in feature detail and attribute values
- **Quality matters** - check your work as you go
- **Document your data** with descriptions and metadata

---

## Next Lesson

[Lesson 5: Cartographic Design Principles](./lesson5_cartography_principles.md)

You'll learn principles of effective map design to make your data communicate clearly.
