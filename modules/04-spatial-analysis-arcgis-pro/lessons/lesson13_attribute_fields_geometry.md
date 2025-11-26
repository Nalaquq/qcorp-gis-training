# Lesson 13: Creating Attribute Fields and Calculating Geometry

**Duration:** 60 minutes
**Difficulty:** Intermediate
**Prerequisites:** Lesson 11 (Creating Layers), Lesson 12 (Edit Tools), basic understanding of attribute tables

---

## Overview

For grant applications, analysis, and data management, you often need to add information to your attribute tables and calculate values based on feature geometry. Whether you're calculating trail lengths in miles for a grant application, measuring erosion area in square meters, or creating unique identifiers, understanding how to work with attribute fields and geometry calculations is essential.

This lesson covers how to add new fields to existing layers and use Calculate Geometry to automatically measure line lengths and polygon areas in your desired units.

---

## Learning Objectives

By the end of this lesson, you will be able to:

1. ✅ Add new fields to existing feature class attribute tables
2. ✅ Choose appropriate field types and properties
3. ✅ Use the Calculate Geometry tool to measure line lengths
4. ✅ Calculate line lengths in miles, kilometers, and meters
5. ✅ Calculate polygon areas in various units
6. ✅ Understand coordinate system impacts on measurements
7. ✅ Prepare accurate measurements for grant applications and analysis

---

## Part 1: Understanding Attribute Tables

### What Are Attribute Tables?

**Definition:** A database table attached to each feature layer storing information about each feature

**Structure:**
- Each row = one feature (point, line, or polygon)
- Each column = one field (attribute)
- Cells = values for that feature's attribute

### Default Fields

**Every feature class includes:**

| Field | Purpose | Editable |
|-------|---------|----------|
| OBJECTID | Unique identifier | No (auto-generated) |
| Shape | Geometry storage | No (edit feature, not field) |
| Shape_Length | For lines: length in coordinate system units | No (auto-calculated) |
| Shape_Area | For polygons: area in coordinate system units | No (auto-calculated) |

### Why Add Custom Fields?

**Default fields aren't always useful:**
- `Shape_Length` in State Plane = length in feet
- Grant application needs miles
- Analysis might need kilometers

**Custom fields let you:**
- Store calculations in specific units
- Add descriptive information
- Create derived values
- Support analysis requirements

---

## Part 2: Adding New Fields

### When to Add Fields

**During Layer Creation:**
- Best practice: plan fields when creating layer
- See Lesson 11 for creating layers with fields

**To Existing Layers:**
- Data was created by someone else
- Requirements changed
- Need additional calculations
- Import data lacking needed fields

### Method 1: Using Fields View (Recommended)

**Step-by-Step:**

1. **Open Attribute Table**
   - Right-click layer in Contents
   - Select "Attribute Table"
   - Table opens at bottom of screen

2. **Open Fields View**
   - In attribute table toolbar
   - Click "Fields" button
   - OR: Right-click layer → Design → Fields

3. **Add New Field**
   - Fields view opens showing all fields
   - Scroll to bottom (first empty row)
   - Click "Click here to add a new field"

4. **Configure Field Properties**

| Property | Description | Example |
|----------|-------------|---------|
| Field Name | No spaces, descriptive | Length_Miles |
| Data Type | Type of data to store | Double |
| Alias | Display name (can have spaces) | Length (Miles) |
| Allow Nulls | Can field be empty? | Yes |
| Default Value | Pre-populate new features | 0 |
| Domain | Limit to specific values | Optional |

5. **Choose Data Type**

**Common Data Types:**

- **Text:** Names, descriptions, categories
  - Length: 50-255 characters typical

- **Short Integer:** Small whole numbers (-32,768 to 32,767)
  - Use for: counts, rankings, small IDs

- **Long Integer:** Large whole numbers
  - Use for: large IDs, population counts

- **Float:** Numbers with decimals (single precision)
  - Use for: most measurements
  - Less precision than Double

- **Double:** Numbers with decimals (double precision)
  - Use for: precise measurements, coordinates
  - **Recommended for geometry calculations**

- **Date:** Date and time values
  - Use for: collection dates, verification dates

6. **Save Changes**
   - Click "Save" in Fields view toolbar
   - New field appears in attribute table
   - Will be empty until populated

### Method 2: Using Add Field Tool (Geoprocessing)

**When to Use:** Scripting or automating field creation

**Steps:**
1. Analysis tab → Tools
2. Search "Add Field"
3. Input: Your layer
4. Field Name: New field name
5. Field Type: Choose from dropdown
6. Run tool

### Field Naming Best Practices

**Do:**
- Use descriptive names: `Length_Miles`, `Area_SqMeters`
- Use underscores instead of spaces
- Be consistent across layers
- Use full words when possible

**Don't:**
- Use spaces: `Length Miles` ❌
- Use special characters: `Length(Miles)` ❌
- Start with numbers: `2024_Length` ❌
- Use reserved words: `Table`, `Field`, `Shape` ❌

---

## Part 3: Calculate Geometry for Line Features

### Overview: Calculating Trail Length

**Common Need:** Measure trail length in miles for grant applications

**Challenge:**
- Default `Shape_Length` in State Plane = feet
- Default in WGS84 = decimal degrees (not useful!)
- Need measurement in miles or kilometers

**Solution:** Add custom field and use Calculate Geometry

### Step-by-Step: Calculate Length in Miles

**Scenario:** You have SAR trail data and need to calculate length in US Survey Miles for Alaska DOT grant application

**Step 1: Add Length Field**

1. Open attribute table for trail layer
2. Click Fields button
3. Add new field:
   - Field Name: `Length_Miles`
   - Data Type: **Double**
   - Alias: "Length (US Survey Miles)"
   - Allow Nulls: Yes
4. Save

**Step 2: Calculate Geometry**

1. **Back to Attribute Table**
   - Close Fields view
   - Return to attribute table
   - Right-click the `Length_Miles` field header
   - Select "Calculate Geometry"

2. **Calculate Geometry Dialog Opens**

**Property** = `Length_Miles` (your field)

**Geometry Attribute** = "Length"
- For polygons, would be "Area"

**Units:**
This is critical! Choose carefully:

For **US Survey Miles** (Alaska standard):
- Scroll to "Length Units"
- Find "Miles (US Survey)" or "Miles US"
- Select it

**Coordinate System:**
- Default: Use data source (layer's coordinate system)
- Usually correct - leave as is
- For most accurate measurements in Alaska: NAD 1983 StatePlane Alaska Zone 7

3. **Click OK**
   - Tool runs
   - `Length_Miles` field populates with calculated values
   - Each trail shows length in miles

**Step 3: Verify Results**

1. Review calculated values
2. Do they make sense?
   - Local trail: 2-15 miles typical
   - Regional route: 15-100 miles
   - If values seem wrong, check:
     - Correct units selected?
     - Coordinate system correct?

### Calculate Geometry Options

**Length Units Available:**

| Unit | When to Use |
|------|-------------|
| **Miles (US Survey)** | Alaska DOT grants, US applications |
| Kilometers | International standards, metric preference |
| Meters | Detailed analysis, scientific work |
| Feet | Engineering, US technical work |
| Feet (US Survey) | Surveying, Alaska State Plane default |

**Best Practice for Alaska Grants:**
- Alaska DOT typically wants **US Survey Miles**
- Matches State Plane coordinate system
- Matches road signs and common usage

### Calculating Length in Multiple Units

**Sometimes You Need Both:**
- Grant needs miles
- Analysis needs meters
- Want both for flexibility

**Solution:** Add multiple fields

**Example:**
1. Add field: `Length_Miles` (Double)
2. Calculate Geometry → Miles US
3. Add field: `Length_Kilometers` (Double)
4. Calculate Geometry → Kilometers
5. Add field: `Length_Meters` (Double)
6. Calculate Geometry → Meters

Now you have all units available!

---

## Part 4: Calculate Geometry for Polygon Features

### Calculating Area

**Common Uses:**
- Erosion area in square meters
- Parcel size in acres
- Water body area in hectares
- Planning zones in square miles

### Step-by-Step: Calculate Area

**Scenario:** Calculate erosion site areas in square meters

**Step 1: Add Area Field**

1. Open attribute table
2. Fields view
3. Add new field:
   - Field Name: `Area_SqMeters`
   - Data Type: **Double**
   - Alias: "Area (Square Meters)"
4. Save

**Step 2: Calculate Geometry**

1. Attribute table
2. Right-click `Area_SqMeters` field header
3. Calculate Geometry

**Settings:**
- Property: `Area_SqMeters`
- Geometry Attribute: **Area**
- Units: Select "Square Meters" or "Meters, Square"

4. Click OK
5. Field populates with area values

### Area Units Available

| Unit | When to Use | Conversion |
|------|-------------|------------|
| Square Meters | Scientific, metric standard | - |
| Hectares | Large areas (100m x 100m) | 10,000 sq meters = 1 hectare |
| Square Kilometers | Very large areas | 1,000,000 sq meters = 1 sq km |
| Acres | US land measurement | ~4,047 sq meters = 1 acre |
| Square Miles | Large US areas | 2.59 sq km = 1 sq mile |
| Square Feet | Small US areas | 0.093 sq meters = 1 sq foot |

**Alaska Common Uses:**
- Parcels: Acres or Square Feet
- Environmental monitoring: Square Meters or Hectares
- Regional planning: Square Miles or Square Kilometers

---

## Part 5: Understanding Coordinate System Impact

### Why Coordinate System Matters

**Key Concept:** Measurements depend on map projection

**Example:**

Same trail measured in different coordinate systems:

| Coordinate System | Shape_Length | Actual Length |
|-------------------|--------------|---------------|
| WGS84 (Geographic) | 0.0234 degrees | Meaningless! |
| State Plane (Projected) | 24,567 feet | Real measurement |
| Web Mercator | Variable | Distorted |

### Projected vs Geographic Coordinate Systems

**Geographic (WGS84, NAD83):**
- Units: Decimal degrees
- Shape_Length and Shape_Area NOT useful for measurements
- Must use Calculate Geometry to get real-world units

**Projected (State Plane, UTM):**
- Units: Feet or Meters
- Shape_Length gives usable measurement
- Still better to use Calculate Geometry for specific units

### Best Practices for Accurate Measurements

1. **Use Projected Coordinate System**
   - For Alaska: NAD 1983 StatePlane Alaska Zone 7
   - EPSG: 26937

2. **Match Coordinate System to Area**
   - State Plane optimized for specific zones
   - Quinhagak = Zone 7
   - Using wrong zone = measurement distortion

3. **Use Calculate Geometry Tool**
   - Even in projected systems
   - Lets you choose exact units needed
   - More accurate than manual conversion

4. **Verify Results**
   - Do measurements match expectations?
   - Compare to known distances
   - Check with imagery

---

## Part 6: Real-World Application - Grant Application Example

### SAR Trail Marking Grant Scenario

**Requirements:**
Alaska DOT Community Trail Marking Grant requires:
- Map of each trail
- **Length of each trail in miles**
- Total trail miles in application
- Dangerous crossing locations

### Complete Workflow

**Step 1: Import and Clean Data**
1. Import GPX from Garmin (covered in Activity 9)
2. Use Edit tools to merge segments (Lesson 12)
3. Split trail at logical segments (Lesson 12)

**Step 2: Set Up Attribute Table**

Add fields to trail layer:

| Field Name | Type | Purpose |
|------------|------|---------|
| Trail_Name | Text (100) | Official trail name |
| From_Location | Text (100) | Start point |
| To_Location | Text (100) | End point |
| Length_Miles | Double | Length in US Survey Miles |
| Grant_Priority | Short Integer | 1-5 ranking |
| Markers_Needed | Long Integer | Estimated markers |

**Step 3: Calculate Trail Length**

1. Right-click `Length_Miles` field
2. Calculate Geometry
3. Length → Miles (US Survey)
4. OK

Results:
```
Trail_Name                    Length_Miles
Quinhagak to Goodnews Bay    47.3
Quinhagak to Fish Camp       8.7
Village Loop Trail           3.2
```

**Step 4: Calculate Total Miles**

Bottom of attribute table:
- Look for statistics (sum, mean, etc.)
- OR use Statistics tool
- Total = 59.2 miles

Enter in grant application!

**Step 5: Create Application Map**

1. Map showing all trails
2. Label with trail names
3. Show Length_Miles in popup or label
4. Export map as PDF
5. Include with grant application

### Result

**Professional grant application includes:**
- Accurate trail lengths in required units (US Survey Miles)
- Individual trail measurements
- Total system mileage
- Professional map
- Data that can be verified

**Outcome:** Much stronger application with quantitative data!

---

## Part 7: Advanced Field Calculations

### Calculate Statistics

**Beyond Geometry:** Calculate values based on other fields

**Example:** Calculate cost estimates

1. Add fields:
   - `Length_Miles` (calculated)
   - `Cost_Per_Mile` (Double, default value: 500)
   - `Total_Cost` (Double)

2. Calculate `Total_Cost`:
   - Right-click `Total_Cost` header
   - Calculate Field (not Calculate Geometry)
   - Expression: `!Length_Miles! * !Cost_Per_Mile!`
   - OK

Result: Automatic cost calculation per trail!

### Field Calculator Basics

**When to Use:**
- Calculate values from other fields
- Text concatenation
- Conditional logic
- Math operations

**Access:**
- Right-click field → Calculate Field
- Write Python or Arcade expression
- More powerful than Calculate Geometry

**Example - Create Full Name:**
```python
!Trail_Name! + " (" + str(!Length_Miles!) + " miles)"
```

Result: "Quinhagak to Goodnews Bay (47.3 miles)"

---

## Part 8: Quality Assurance and Verification

### Verify Calculated Values

**Visual Check:**
1. Sort by calculated field
2. Look for:
   - Null values (missing calculations)
   - Zero values (calculation error)
   - Negative values (shouldn't happen)
   - Unreasonably large values

**Logical Check:**
1. Compare to expectations:
   - Trail to next village: 10-50 miles typical
   - Walking trail: 0.5-5 miles typical
   - Regional route: 50-200 miles

**Reference Check:**
1. Compare to known distances
2. Measure same feature in Google Earth
3. Check against historical records

### Common Calculation Errors

**Problem:** All values are 0
**Cause:** Wrong geometry attribute selected
**Solution:** Recalculate with correct attribute (Length vs Area)

**Problem:** Values extremely small or large
**Cause:** Wrong units selected
**Solution:** Recalculate with correct units

**Problem:** Values are null
**Cause:** Features have no geometry
**Solution:** Check feature geometry is valid

**Problem:** Values don't match expectations
**Cause:** Wrong coordinate system
**Solution:**
- Check layer coordinate system
- Reproject if needed
- Recalculate geometry

---

## Part 9: Practice Exercises

### Exercise 1: Calculate Trail Lengths

**Setup:**
1. Create line layer: `Practice_Trails`
2. Draw 3 trail lines of different lengths
3. Name each trail in attributes

**Tasks:**
1. Add field: `Length_Miles` (Double)
2. Calculate Geometry in US Survey Miles
3. Add field: `Length_Kilometers` (Double)
4. Calculate Geometry in Kilometers
5. Verify values make sense (1 mile ≈ 1.6 km)

**Deliverable:**
- Attribute table showing both mile and kilometer values
- Screenshot showing calculated values

---

### Exercise 2: Calculate Erosion Areas

**Setup:**
1. Create polygon layer: `Erosion_Sites`
2. Draw 3 polygons representing erosion areas
3. Make different sizes

**Tasks:**
1. Add field: `Area_SqMeters` (Double)
2. Calculate Geometry in Square Meters
3. Add field: `Area_Hectares` (Double)
4. Calculate Geometry in Hectares
5. Verify: Large polygon > Small polygon in both units

**Deliverable:**
- Table showing areas in both units
- Verification that conversions are correct (10,000 sq m = 1 hectare)

---

### Exercise 3: Grant Application Summary

**Setup:**
Use trails from Exercise 1

**Tasks:**
1. Add field: `Markers_Per_Mile` (Double, default = 4)
2. Add field: `Total_Markers` (Double)
3. Use Calculate Field to calculate:
   - `Total_Markers` = `Length_Miles` * `Markers_Per_Mile`
4. Add field: `Marker_Cost` (Double, default = 150)
5. Calculate field: `Total_Cost` = `Total_Markers` * `Marker_Cost`

**Deliverable:**
- Complete cost estimate per trail
- Total markers needed
- Total cost estimate
- Professional summary for grant application

---

## Part 10: Troubleshooting Guide

### Field Issues

**Can't add field**
- Layer is locked or read-only
- Check you have edit permissions
- Close other applications using the geodatabase

**Field won't calculate**
- Check field is correct data type (use Double for geometry)
- Verify layer has geometry
- Check coordinate system is defined

**Wrong values after calculation**
- Verify correct units selected
- Check coordinate system
- Ensure geometry is valid

### Calculation Issues

**Calculate Geometry option grayed out**
- Field must be numeric type (not text)
- Must be editable layer
- Check field isn't system field (OBJECTID, Shape)

**Values don't match other sources**
- Different units?
- Different coordinate systems?
- Different measurement methods?

**Null values after calculation**
- Features may lack geometry
- Check for empty features
- Verify features are actually drawn

---

## Summary

### Key Concepts

1. **Adding Fields**
   - Use Fields view for control
   - Choose appropriate data type
   - Double for precise measurements

2. **Calculate Geometry**
   - Right-click field header
   - Choose Length or Area
   - Select appropriate units
   - Verify results

3. **Units Matter**
   - Alaska grants: US Survey Miles
   - Scientific: Meters/Kilometers
   - Choose units for your audience

4. **Coordinate Systems**
   - Use projected systems for measurements
   - State Plane for local accuracy
   - Verify before calculating

### Complete Workflow

1. Create or prepare layer
2. Add necessary fields (Double type)
3. Calculate Geometry
4. Choose correct attribute (Length/Area)
5. Select appropriate units
6. Verify results
7. Use in analysis or applications

### Best Practices

- ✅ Plan fields before creating layers
- ✅ Use Double type for measurements
- ✅ Calculate Geometry in needed units
- ✅ Verify calculations make sense
- ✅ Keep multiple unit fields if needed
- ✅ Document units in field aliases
- ✅ Use projected coordinate systems

---

## Real-World Impact

### Grant Application Success

**Before this lesson:**
- Manual measurement (inaccurate)
- Guessing trail lengths
- Weak grant applications

**After this lesson:**
- Precise, verifiable measurements
- Professional data presentation
- Confident grant applications
- Defensible numbers

### Example Success: Quinhagak SAR Grant

**Application required:**
- Exact trail lengths in miles
- Total system mileage
- Cost estimates per mile

**What we provided:**
- Calculated length for each trail
- Total: 59.2 miles
- Professional map with measurements
- Cost estimate based on accurate lengths

**Result:** Strong, data-driven application using tools from this lesson.

---

## Additional Resources

### Documentation
- [Calculate Geometry (ArcGIS Pro)](https://pro.arcgis.com/en/pro-app/latest/help/data/tables/calculate-geometry.htm)
- [Add Field (ArcGIS Pro)](https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/add-field.htm)
- [Field Data Types](https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/overview/arcgis-field-data-types.htm)
- [Calculate Field](https://pro.arcgis.com/en/pro-app/latest/help/data/tables/calculate-field.htm)

### Unit Conversions
- 1 Mile (US Survey) = 1.609344 kilometers
- 1 Kilometer = 0.621371 miles
- 1 Acre = 43,560 square feet = 4,047 square meters
- 1 Hectare = 10,000 square meters = 2.471 acres
- 1 Square Mile = 640 acres = 2.59 square kilometers

### Related Lessons
- Lesson 11: Creating Layers (adding fields during creation)
- Lesson 12: Edit Tools (preparing features for calculation)
- Lesson 1: Projections (coordinate system impacts on measurement)

---

## Next Steps

Now that you can calculate geometry:
1. Apply to real trail data
2. Prepare grant applications
3. Create professional analysis
4. Support community decision-making with accurate data

---

**Lesson Version:** 1.0
**Last Updated:** November 2025
**Module:** 4 - Spatial Analysis in ArcGIS Pro
**Location:** Quinhagak, Alaska
