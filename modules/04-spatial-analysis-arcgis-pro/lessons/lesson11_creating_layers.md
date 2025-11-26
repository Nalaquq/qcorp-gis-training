# Lesson 11: Creating Layers in ArcGIS Pro

**Duration:** 45 minutes
**Difficulty:** Beginner-Intermediate
**Prerequisites:** Basic ArcGIS Pro navigation, understanding of feature types (point, line, polygon)

---

## Overview

Creating new feature layers is a fundamental skill in ArcGIS Pro. Whether you're digitizing trails from GPS data, tracing features from imagery, or setting up a data structure for field collection, understanding how to create and configure layers is essential.

In this lesson, you'll learn how to create new feature classes within geodatabases, configure their properties, and set up attribute fields that support your data collection and analysis needs.

---

## Learning Objectives

By the end of this lesson, you will be able to:

1. ✅ Create new feature classes in a geodatabase
2. ✅ Choose appropriate geometry types (point, line, polygon)
3. ✅ Set coordinate systems for new layers
4. ✅ Add and configure attribute fields
5. ✅ Understand field types and their appropriate uses
6. ✅ Create layers for various real-world applications

---

## Why Create New Layers?

### Common Use Cases

**Trail Mapping:**
- Digitize snowmachine trails from GPS tracks
- Create route layers for search and rescue operations
- Document traditional travel routes

**Community Infrastructure:**
- Map community buildings and facilities
- Track infrastructure maintenance needs
- Plan new development locations

**Environmental Monitoring:**
- Document erosion areas
- Track wildlife observations
- Map permafrost changes

**Cultural Resources:**
- Preserve traditional placenames
- Document historical sites
- Map subsistence use areas

---

## Part 1: Understanding Feature Classes vs Shapefiles

### Feature Classes (Recommended)

**Advantages:**
- Stored in geodatabases for better organization
- Support longer field names (up to 255 characters)
- Better performance with large datasets
- Can store multiple feature types in one geodatabase
- Support advanced data types
- More efficient storage

**File Location:**
- Stored inside .gdb folder
- Example: `MyProject.gdb/Trails`

### Shapefiles (Legacy Format)

**Limitations:**
- Separate files for each layer (.shp, .dbf, .shx, .prj)
- Field names limited to 10 characters
- Less efficient for large datasets
- Can clutter file system

**When to Use:**
- Sharing data with users without ArcGIS
- Compatibility with older software
- Simple, small datasets

**Best Practice:** Always create feature classes in geodatabases unless you have a specific reason to use shapefiles.

---

## Part 2: Creating a Feature Class

### Method 1: Using the Catalog Pane (Recommended)

**Step 1: Open the Catalog Pane**
1. Click View tab → Catalog Pane
2. Navigate to your project geodatabase
   - Usually under Databases folder
   - Named after your project (e.g., `MyProject.gdb`)

**Step 2: Create New Feature Class**
1. Right-click on the geodatabase
2. Select New → Feature Class
3. The Create Feature Class wizard opens

**Step 3: Configure Basic Properties**

**Feature Class Name:**
- Use descriptive names
- No spaces (use underscores)
- Examples: `SAR_Trails`, `Community_Buildings`, `Erosion_Sites`

**Alias (Optional):**
- Display name that can include spaces
- Example: "SAR Winter Trails"

**Geometry Type:**
Choose based on what you're mapping:
- **Point:** Individual locations (buildings, signs, observations)
- **Line:** Linear features (trails, roads, rivers)
- **Polygon:** Areas (parcels, zones, water bodies)
- **Multipoint:** Clusters of related points
- **Multipatch:** 3D features (buildings with height)

**Step 4: Set Coordinate System**

**Important:** Always set the coordinate system when creating a layer!

**Options:**

1. **Import from existing layer** (recommended)
   - Click folder icon
   - Select a layer from your map
   - Ensures compatibility

2. **Select from favorites:**
   - For Quinhagak area: NAD 1983 StatePlane Alaska 7 FIPS 5007
   - EPSG: 26937

3. **Search by EPSG code:**
   - Search box → enter "26937"
   - Select from results

**Step 5: Configure Storage Settings** (Usually leave defaults)
- Configuration keyword: DEFAULT
- Check "Has Z" if storing elevation values
- Check "Has M" if storing measure values (for linear referencing)

**Step 6: Add Fields (Attributes)**

This is where you define what information to store about each feature.

**Default Fields (automatically included):**
- `OBJECTID`: Unique identifier for each feature
- `Shape`: Geometry storage
- `Shape_Length` or `Shape_Area`: Calculated automatically for lines/polygons

**Add Custom Fields:**

Click "Add New Field" and configure:

| Field Setting | Description | Example |
|---------------|-------------|---------|
| Field Name | No spaces, descriptive | Trail_Name |
| Data Type | Type of data stored | Text, Number, Date |
| Length | For text fields, max characters | 100 |
| Allow Nulls | Can field be empty? | Usually Yes |
| Default Value | Pre-populate with value | "Unknown" |

**Common Field Types:**

- **Text:** Names, descriptions, categories
  - Set appropriate length (50-255 common)

- **Long Integer:** Whole numbers (IDs, counts)
  - Example: Number of markers needed

- **Double:** Numbers with decimals (measurements)
  - Example: Trail length in miles

- **Date:** Dates and times
  - Example: Date surveyed

- **Short Integer:** Small whole numbers (-32,768 to 32,767)
  - Example: Priority ranking (1-5)

**Step 7: Complete Creation**
1. Review all settings
2. Click Finish
3. New feature class appears in geodatabase
4. Right-click → Add to Current Map to begin editing

---

## Part 3: Example - Creating a Snowmachine Trails Layer

### Real-World Scenario: SAR Trail Mapping

You need to create a layer to store snowmachine trail data for a trail marking grant application.

**Requirements:**
- Track trail names and routes
- Record trail length
- Note difficulty and condition
- Document when last verified
- Assign priority for grant funding

### Step-by-Step Creation

**Step 1: Create Feature Class**
1. Catalog Pane → Right-click geodatabase → New → Feature Class
2. Name: `SAR_Snowmachine_Trails`
3. Alias: "SAR Snowmachine Trails"
4. Type: **Polyline** (lines)
5. Coordinate System: NAD 1983 StatePlane Alaska 7 FIPS 5007

**Step 2: Add Attribute Fields**

| Field Name | Type | Length | Description |
|------------|------|--------|-------------|
| Trail_Name | Text | 100 | Name of trail |
| Trail_Type | Text | 50 | Winter, Summer, Year-round |
| From_Location | Text | 100 | Starting point |
| To_Location | Text | 100 | Ending point |
| Difficulty | Text | 20 | Easy, Moderate, Difficult |
| Condition | Text | 20 | Good, Fair, Poor, Unknown |
| Date_Verified | Date | - | Last verification date |
| Verified_By | Text | 100 | Who verified |
| Safety_Notes | Text | 255 | Important safety information |
| Grant_Priority | Short Integer | - | Priority 1-5 (5=highest) |
| Markers_Needed | Long Integer | - | Est. number of markers |
| Length_Miles | Double | - | Trail length (calculated) |
| Source | Text | 100 | Data source (GPS, digitized, etc.) |
| Notes | Text | 255 | Additional information |

**Step 3: Finish and Add to Map**
1. Click Finish
2. Right-click layer → Add to Current Map
3. Layer appears in Contents pane
4. Ready for editing!

---

## Part 4: Creating Multiple Related Layers

### Grant Application Example

For a comprehensive trail marking grant, you might need several related layers:

**1. Trails Layer** (Line)
- Main trail routes
- Created above

**2. Dangerous Crossings Layer** (Point)
- Hazard locations
- River crossings with thin ice
- Overflow areas

**3. Trail Markers Layer** (Point)
- Proposed marker locations
- Marker types and specifications

**4. Trail Segments Layer** (Line)
- Break trails into segments between markers
- For detailed cost estimation

### Organizing Related Layers

**Naming Convention:**
Use consistent prefixes to keep related layers together:
- `SAR_Trails`
- `SAR_Crossings`
- `SAR_Markers`
- `SAR_Segments`

**Feature Dataset Option:**
For tightly integrated layers, create a Feature Dataset:
1. Right-click geodatabase → New → Feature Dataset
2. Name: `SAR_Trail_System`
3. Set coordinate system once
4. Create all layers inside dataset
5. All layers automatically share coordinate system

---

## Part 5: Importing Structure from Existing Layer

### When to Use

If you already have a layer with the structure you need:
- Don't recreate fields manually
- Import the schema (structure) from existing layer
- Saves time and ensures consistency

### How to Import Structure

**Method 1: Export/Import**
1. Right-click existing layer → Data → Export Features
2. Output: New feature class name
3. Structure and fields copied automatically
4. Delete all features if you want empty layer

**Method 2: Feature Class to Feature Class Tool**
1. Analysis tab → Tools → Search "Feature Class to Feature Class"
2. Input: Existing layer
3. Output: New layer location and name
4. Field Map: Configure which fields to keep
5. Where Clause: Leave empty for structure only

---

## Part 6: Best Practices

### Naming Conventions

**Do:**
- Use descriptive names: `Winter_Trails` not `Layer1`
- Use underscores instead of spaces: `Trail_Markers` not `Trail Markers`
- Be consistent: `SAR_Trails`, `SAR_Markers` (same prefix)
- Use appropriate case: `Trail_Name` or `TRAIL_NAME` (pick one style)

**Don't:**
- Use special characters: `Trails#2024` ❌
- Start with numbers: `2024_Trails` ❌
- Use reserved words: `Table`, `Field` ❌
- Make names too long: `Snowmachine_Trail_Routes_Winter_2024_SAR_Grant_Application` ❌

### Field Configuration

**Text Field Lengths:**
- Names: 50-100 characters
- Short codes: 10-20 characters
- Descriptions/Notes: 255 characters (max)
- Don't make fields unnecessarily long (wastes storage)

**Field Names:**
- Be descriptive but concise
- Use full words when possible: `Length_Miles` not `Len_Mi`
- Consistent terminology across layers
- Consider how names sort alphabetically

**Required vs Optional Fields:**
- Think about which fields MUST have values
- Set "Allow Nulls" = No for required fields
- Set default values where appropriate
- Example: Default `Status` = "Needs_Verification"

### Coordinate Systems

**Always Set Coordinate System:**
- Never create a layer without defining projection
- Match coordinate system of other layers you'll use
- For Alaska local analysis: State Plane
- For web sharing: Web Mercator
- For GPS compatibility: WGS84

**Check Your Work:**
- After creating layer, check properties
- Verify coordinate system is correct
- Test by adding to map with other layers
- Ensure alignment is correct

---

## Part 7: Common Issues and Troubleshooting

### Layer Won't Add to Map

**Problem:** Created layer doesn't appear in Contents
**Solution:**
- Check Catalog Pane → Refresh
- Right-click layer → Add to Current Map
- Verify layer actually saved (check geodatabase)

### Can't Create Feature Class

**Problem:** "Create Feature Class" option grayed out
**Solution:**
- Ensure you're right-clicking on geodatabase, not a folder
- Check you have write permissions
- Close and reopen Catalog Pane
- Verify geodatabase isn't locked by another process

### Layer in Wrong Location

**Problem:** Features appear in ocean or wrong continent
**Solution:**
- Wrong coordinate system selected
- Delete and recreate with correct coordinate system
- Or use Project tool to convert

### Fields Won't Accept Data

**Problem:** Can't enter data in certain fields
**Solution:**
- Check field type matches data (text vs number)
- For numbers, verify not exceeding field precision
- For text, check not exceeding length
- Verify in edit session

---

## Practice Exercise

### Exercise 1: Create a Community Buildings Layer

**Task:** Create a point layer to inventory community buildings

**Requirements:**
1. Create feature class named: `Community_Buildings`
2. Type: Point
3. Coordinate System: Alaska State Plane Zone 7

**Fields to Add:**

| Field Name | Type | Length | Purpose |
|------------|------|--------|---------|
| Building_Name | Text | 100 | Building name |
| Building_Type | Text | 50 | School, Store, Office, etc. |
| Address | Text | 100 | Physical address |
| Year_Built | Long Integer | - | Construction year |
| Condition | Text | 20 | Good, Fair, Poor |
| Owner | Text | 100 | Tribal, Private, State, etc. |
| Use | Text | 100 | Current use |
| Notes | Text | 255 | Additional information |

**Steps:**
1. Open Catalog Pane
2. Navigate to geodatabase
3. Create new feature class
4. Configure all fields
5. Add to map
6. Verify you can start edit session

---

### Exercise 2: Create a River Erosion Monitoring Layer

**Task:** Create a polygon layer to track erosion areas

**Requirements:**
1. Feature class: `Erosion_Monitoring`
2. Type: Polygon
3. Include fields for:
   - Location description
   - Date observed
   - Severity (Low, Medium, High, Critical)
   - Area in square meters (calculated field)
   - Observer name
   - Photos taken (Yes/No)
   - Monitoring priority (1-5)

**Challenge:**
Configure the layer so it's ready for multi-year monitoring. Consider what fields would help track changes over time.

---

## Real-World Application

### SAR Trail Marking Grant Case Study

**Context:**
Quinhagak SAR needed to document trails for Alaska DOT grant application requiring:
- Map of all trails
- Trail lengths in miles
- Identification of dangerous crossings
- Priority ranking for marker placement

**Solution:**
Created structured layers to organize all required information:

1. **Trails Layer:** Routes with complete attributes
2. **Crossings Layer:** Hazard locations with safety notes
3. **Markers Layer:** Proposed marker locations

**Result:**
- Professional data structure
- Easy to calculate total miles
- Clear priority ranking
- Grant-ready documentation

**Files Created:**
- `SAR_Trails` (line layer)
- `SAR_Dangerous_Crossings` (point layer)
- `SAR_Proposed_Markers` (point layer)

Each layer had consistent fields and naming, making the dataset professional and easy to understand.

---

## Summary

Creating well-structured layers is foundational to effective GIS work. Key takeaways:

1. **Always use geodatabases** for feature class storage
2. **Plan your fields** before creating the layer
3. **Set coordinate systems** correctly from the start
4. **Use consistent naming** conventions
5. **Think ahead** about what data you need to collect
6. **Test your structure** by starting an edit session

Properly structured layers make data collection easier, analysis more reliable, and sharing more professional.

---

## Additional Resources

### Documentation
- [ArcGIS Pro: Create Feature Class](https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/overview/create-a-feature-class.htm)
- [Geodatabase Feature Classes](https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/overview/feature-class-basics.htm)
- [Field Data Types](https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/overview/arcgis-field-data-types.htm)

### Related Lessons
- Lesson 3: Data Management (geodatabase organization)
- Lesson 5: Creating Features (how to digitize into layers)
- Lesson 13: Attribute Fields and Calculating Geometry (working with fields)

---

## Next Steps

After creating layers, you'll need to:
1. **Add features** → See Lesson 5: Creating Features
2. **Edit features** → See Lesson 12: Edit Tools
3. **Calculate values** → See Lesson 13: Attribute Fields and Calculating Geometry

---

**Lesson Version:** 1.0
**Last Updated:** November 2025
**Module:** 4 - Spatial Analysis in ArcGIS Pro
**Location:** Quinhagak, Alaska
