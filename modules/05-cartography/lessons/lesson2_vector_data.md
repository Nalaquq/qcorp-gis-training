# Lesson 2: Understanding Vector Data

**Duration:** 75 minutes
**Prerequisites:** Lesson 1 - Introduction to Web Maps
**Training Date Reference:** November 8, 2025

---

## Lesson Overview

This lesson introduces vector data - the fundamental data type for representing discrete features in GIS. You'll learn about the three types of vector features (points, lines, and polygons), when to use each, and how they differ from raster data.

---

## Learning Objectives

By the end of this lesson, you will be able to:

1. Explain what vector data is and how it represents geographic features
2. Identify the three types of vector features
3. Choose the appropriate feature type for different real-world objects
4. Understand feature attributes and attribute tables
5. Distinguish between vector and raster data
6. Apply vector data concepts to community mapping needs

---

## What is Vector Data?

### Definition

**Vector data** represents geographic features using discrete geometric shapes:
- **Points** - specific locations
- **Lines** - connections between locations
- **Polygons** - enclosed areas

Each feature is defined by coordinates and can have associated information (attributes).

### How Vector Data Works

**Coordinate-Based:**
- Features stored as coordinate pairs (X, Y or Latitude, Longitude)
- Points: Single coordinate
- Lines: Series of connected coordinates
- Polygons: Closed series of coordinates forming a boundary

**Example:**
```
Point: Single location
  Coordinates: (-161.8640, 59.7644)

Line: Connected locations
  Coordinates: (-161.8640, 59.7644) → (-161.8650, 59.7650) → (-161.8660, 59.7655)

Polygon: Enclosed area
  Coordinates: Form closed shape returning to start point
```

---

## The Three Types of Vector Features

### 1. Point Features

**What They Represent:**
- Specific locations
- Things at a location
- Events at a location

**Characteristics:**
- Single coordinate pair
- No length or area
- Size on map is symbolic (not to scale)

**Real-World Examples:**

From Quinhagak Mapping:
- ✅ Damaged fish racks (Typhoon Merbok map)
- ✅ Sewer damage locations (Typhoon Merbok map)
- ✅ Water treatment plant location (Relocation map)
- ✅ Individual buildings
- ✅ Community facilities

Other Examples:
- Wells or water sources
- Power poles
- GPS survey points
- Monitoring stations
- Cultural sites
- Emergency shelters

**When to Use Points:**
- Location is more important than shape/size
- Feature too small to show as polygon at map scale
- Representing events or occurrences
- Counting or inventorying discrete items

### 2. Line Features

**What They Represent:**
- Connections between locations
- Linear features
- Networks
- Paths or routes

**Characteristics:**
- Series of connected coordinate pairs
- Have length but no area
- Width on map is symbolic

**Real-World Examples:**

From Quinhagak Mapping:
- ✅ Proposed sewer lines (Relocation map)
- ✅ Proposed road network (Relocation map)
- ✅ Utility corridors

Other Examples:
- Rivers and streams
- Trails and paths
- Power lines
- Pipelines
- Property boundaries (lines)
- Contour lines (elevation)
- Flight paths

**When to Use Lines:**
- Representing linear infrastructure
- Showing connections or networks
- Depicting routes or paths
- Showing boundaries (can also use polygons)
- Flow or movement

### 3. Polygon Features

**What They Represent:**
- Areas
- Enclosed regions
- Zones or districts
- 2-dimensional features

**Characteristics:**
- Closed series of coordinates
- Have both perimeter (length) and area
- Can calculate area measurements

**Real-World Examples:**

From Quinhagak Mapping:
- ✅ Coastal erosion areas (Typhoon Merbok map)
- ✅ UAS orthomosaic collection zones (Relocation map)
- ✅ Proposed infrastructure sites (Relocation map)
- ✅ Flooding extent

Other Examples:
- Building footprints
- Land parcels
- Vegetation types
- Bodies of water (lakes, ponds)
- Zoning districts
- Tribal lands
- Hunting/fishing areas
- Exclusion or buffer zones

**When to Use Polygons:**
- Representing areas or regions
- When area measurement important
- Showing zones or boundaries
- Depicting coverage or extent
- Land use or land cover

---

## Choosing the Right Feature Type

### Decision Guide

**Ask Yourself:**

1. **Is it a specific location?**
   - YES → Use **Point**
   - Examples: Fish rack location, building point

2. **Is it a linear feature or connection?**
   - YES → Use **Line**
   - Examples: Road, sewer line, trail

3. **Is it an area or region?**
   - YES → Use **Polygon**
   - Examples: Erosion zone, building footprint, proposed site

4. **Does scale matter?**
   - Small map scale: Use simpler features (buildings as points)
   - Large map scale: Use detailed features (buildings as polygons)

### Scale Considerations

**Same Feature, Different Scales:**

**Buildings:**
- Regional map: Point (dot represents building)
- Community map: Polygon (show building footprint)
- Site plan: Detailed polygon (show rooms, doors)

**Roads:**
- Regional map: Line (center line)
- Detailed map: Polygon (show road width)

**Water Treatment Plant (from Relocation Map):**
- Planning map: Point or simple polygon (location/general size)
- Site design: Detailed polygon (exact footprint and facilities)

---

## Feature Attributes

### What are Attributes?

**Attributes** are information attached to each feature.

**Think of it as:**
- Feature = the shape/location (WHERE)
- Attributes = the information about it (WHAT)

### Attribute Tables

Each layer has an **attribute table** with:
- **Rows** = individual features
- **Columns** = attribute fields
- **Cells** = values for each feature/field

**Example: Damaged Fish Racks (Typhoon Merbok Map)**

| Feature ID | Rack_Name | Damage_Type | Severity | Repair_Cost | Photo_Link |
|------------|-----------|-------------|----------|-------------|------------|
| 1 | River Mouth Rack | Structural | High | $5,000 | link... |
| 2 | North Beach Rack | Wire Damage | Medium | $2,000 | link... |
| 3 | South Site Rack | Complete Loss | Critical | $8,000 | link... |

### Attribute Field Types

**Text (String):**
- Names, descriptions, categories
- Examples: "Damaged", "Proposed", "Main Street"

**Numbers (Integer or Float):**
- Counts, measurements, costs
- Examples: 5, 2500.50, -10

**Date:**
- When something occurred or was observed
- Examples: 11/8/2025, 2025-09-15

**Yes/No (Boolean):**
- True/false questions
- Examples: Is_Damaged (Yes/No), Needs_Repair (True/False)

### Designing Attributes

**Good Attribute Design (from your maps):**

**Typhoon Merbok Damage Map:**
- Damage_Type (text): "Erosion", "Structural", "Flooding"
- Severity (text): "Low", "Medium", "High", "Critical"
- Date_Assessed (date): When damage documented
- Est_Cost (number): Estimated repair cost
- Priority (number): 1-5 ranking

**Village Relocation Map:**
- Feature_Type (text): "Sewer", "Road", "Water", "Building"
- Status (text): "Proposed", "Planned", "Under Design"
- Phase (text): "Phase 1", "Phase 2", "Future"
- Length_ft (number): For lines - length in feet
- Area_sqft (number): For polygons - area in square feet

---

## Vector vs. Raster Data

### Key Differences

| Aspect | Vector | Raster |
|--------|---------|---------|
| **Structure** | Points, lines, polygons | Grid of pixels |
| **Features** | Discrete objects | Continuous surfaces |
| **Precision** | Exact coordinates | Limited by pixel size |
| **File Size** | Based on complexity | Based on extent |
| **Best For** | Discrete features | Imagery, elevation |
| **Examples** | Roads, buildings | Satellite images, DSM |

### When to Use Each

**Use Vector For:**
- Infrastructure (roads, utilities)
- Boundaries (parcels, zones)
- Points of interest (facilities, damage locations)
- Networks (sewer, roads)
- Planning (proposed features)

**Use Raster For:**
- Satellite or drone imagery
- Elevation data (DSM, DTM)
- Temperature data (thermal imagery)
- Continuous phenomena
- Background context (basemaps)

### Combining Vector and Raster

**Common Approach:**
- **Raster basemap** - provides visual context (satellite image, orthomosaic)
- **Vector features** - shows specific items (roads, damage locations, proposed infrastructure)

**Your Maps Use Both:**
- Typhoon Merbok Map: Satellite basemap + vector damage features
- Relocation Map: Orthomosaic basemap + vector proposed features

---

## Real-World Application: Your Maps

### Typhoon Merbok Damage Map

**Points:**
- Individual damaged fish racks
- Sewer damage locations
- Other infrastructure damage points

**Why points?** Each damage location is discrete, countable, and the specific location is most important.

**Polygons:**
- Erosion areas
- Flooding extent

**Why polygons?** These represent areas/zones, and the extent (area) of damage is important to show.

**Attributes Include:**
- Type of damage
- Severity level
- Estimated repair cost
- Assessment date

### Village Relocation Site Map

**Polygons:**
- UAS flight areas (where to collect orthomosaics)
- Proposed water treatment plant
- Other infrastructure footprints

**Why polygons?** These are areas with specific boundaries, and area/size is important for planning.

**Lines:**
- Proposed sewer lines
- Proposed road network

**Why lines?** These are linear infrastructure networks, connections between locations.

**Attributes Include:**
- Feature type (sewer, road, building)
- Phase (when to be built)
- Status (proposed, planned, designed)
- Dimensions (length, width, area)

---

## Working with Vector Data in ArcGIS Online

### Adding Vector Layers

**From Existing Sources:**
1. Search for public layers
2. Add from Living Atlas
3. Import from files (shapefile, GeoJSON, CSV)
4. Connect to organizational content

**Creating New:**
1. Click "Add" → "Create Layer"
2. Choose feature type (point, line, polygon)
3. Define attributes
4. Start digitizing

### Viewing Attributes

**In Map:**
- Click on feature → Pop-up shows attributes
- Configure which attributes display

**In Table:**
- Open attribute table
- View all features and all attributes
- Sort, filter, query data
- Edit values

### Editing Features

**Geometry (Shape/Location):**
- Move features
- Reshape lines/polygons
- Add/delete vertices
- Split or merge features

**Attributes (Information):**
- Edit field values
- Add new records
- Delete records
- Calculate values

---

## Best Practices

### Data Collection

**Be Consistent:**
- Use same feature type for similar objects
- Use consistent attribute values (not "High" and "high")
- Follow naming conventions
- Complete all required fields

**Be Accurate:**
- Zoom in when digitizing
- Use snapping to connect features
- Verify coordinates if GPS collected
- Double-check attribute values

**Be Organized:**
- Logical layer names
- Clear attribute field names
- Document data sources
- Include collection date

### Common Mistakes to Avoid

**❌ Wrong Feature Type:**
- Using points when polygons needed (or vice versa)
- Mixing feature types in one layer

**❌ Inconsistent Attributes:**
- Different spellings or capitalizations
- Missing required information
- Incorrect data types

**❌ Topology Errors:**
- Gaps between polygons that should connect
- Overlapping polygons that shouldn't overlap
- Lines that don't connect properly

**✅ Do:**
- Choose appropriate feature type for each object
- Define attributes before collecting data
- Use consistent values (create dropdown lists)
- Check work as you go
- Save frequently

---

## Review Questions

1. What are the three types of vector features?
2. When would you use a point feature vs. a polygon feature?
3. What are feature attributes?
4. How is vector data different from raster data?
5. Why did we use points for damaged fish racks but polygons for erosion areas?
6. Why did we use lines for proposed sewer infrastructure?
7. What attribute fields would be useful for a road network layer?
8. Give three examples each of features that should be points, lines, and polygons in Quinhagak.

---

## Practical Exercise

**Feature Type Practice:**

For each item below, identify whether it should be mapped as a point, line, or polygon:

1. __ Quinhagak airport terminal building (detailed site map)
2. __ Fire hydrant locations
3. __ A traditional fish camp area
4. __ The Kuskokwim River
5. __ Power transmission lines
6. __ Boardwalk sections in the village
7. __ A proposed new school building location (preliminary planning)
8. __ The extent of a berry picking area
9. __ Snow machine trail to fish camp
10. __ Individual grave locations in cemetery

**Design Attributes:**

For the "Proposed Roads" layer in the village relocation map, design an attribute table. List at least 5 useful attribute fields with their data types and example values.

---

## Key Takeaways

- **Vector data represents discrete geographic features** using points, lines, and polygons
- **Points** show specific locations (damaged fish racks, facilities)
- **Lines** show linear features and connections (roads, sewer lines, trails)
- **Polygons** show areas and regions (erosion zones, proposed sites)
- **Choose feature type based on** what you're representing and what information is important
- **Attributes store information about** each feature (damage type, status, cost, etc.)
- **Vector data is ideal for** infrastructure, boundaries, planning, and discrete features
- **Design attributes carefully** - they make your data useful for analysis and decision-making

---

## Next Lesson

[Lesson 3: Accessing Publicly Available Layers](./lesson3_public_layers.md)

You'll learn how to find and add existing data layers to your maps from ArcGIS Living Atlas and other sources.
