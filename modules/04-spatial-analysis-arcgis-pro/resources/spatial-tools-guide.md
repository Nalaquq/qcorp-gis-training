# Spatial Analysis Tools Quick Reference Guide

## When to Use Which Tool: A Practical Guide

This guide helps you choose the right spatial analysis tool for your task in ArcGIS Pro.

---

## Buffer

**What it does:** Creates zones at specified distances around features

**Use when you need to:**
- Show areas within a certain distance of a feature
- Create setback zones
- Establish protection areas
- Analyze proximity

**Real Quinhagak Examples:**
- 50m buffer around streams (water quality protection)
- 100m buffer around historical sites (cultural resource protection)
- 500m buffer from school (walking distance analysis)
- 1000m buffer from contamination site (impact zone)

**Input:** Points, lines, or polygons
**Output:** Polygons

**Key Parameters:**
- Distance (choose carefully - check units!)
- Dissolve type (keep separate or merge overlaps)

**Tool Location:** Analysis Tools → Proximity → Buffer

---

## Clip

**What it does:** Cuts features to a boundary (like cookie cutter)

**Use when you need to:**
- Extract data for your study area only
- Remove features outside your area of interest
- Create subset of larger dataset
- Focus analysis on specific region

**Real Quinhagak Examples:**
- Clip statewide parcels layer to just Quinhagak area
- Clip satellite imagery to village boundary
- Extract rivers within Quinhagak watershed
- Cut road network to planning area

**Input:** Features to be clipped + clip boundary
**Output:** Only features inside clip boundary

**Analogy:** Using cookie cutter to cut shapes from dough

**Tool Location:** Analysis Tools → Extract → Clip

---

## Dissolve

**What it does:** Combines adjacent features into single feature

**Use when you need to:**
- Combine multiple polygons into one
- Aggregate data by category
- Simplify many features to fewer features
- Merge overlapping buffers

**Real Quinhagak Examples:**
- Dissolve all parcels by owner (combine all parcels owned by same person)
- Merge overlapping stream buffers into single protection zone
- Combine housing plots by neighborhood
- Aggregate land use types

**Input:** Polygons (usually)
**Output:** Fewer, larger polygons

**Key Parameters:**
- Dissolve field (which attribute to group by)
- Statistics (optional - sum areas, count features, etc.)

**Tool Location:** Data Management Tools → Generalization → Dissolve

---

## Erase

**What it does:** Removes areas from features (opposite of Clip)

**Use when you need to:**
- Remove wetlands from buildable area
- Exclude protected areas from development zone
- Cut out existing development from vacant land
- Remove overlap between features

**Real Quinhagak Examples:**
- Erase wetlands from potential building sites
- Remove existing infrastructure from vacant parcels
- Exclude flood zones from land use planning area
- Cut out protected cultural sites from development areas

**Input:** Features to be erased from + erase features
**Output:** Input features with holes where erase features were

**Analogy:** Eraser removing parts of a drawing

**Tool Location:** Analysis Tools → Overlay → Erase

---

## Intersect

**What it does:** Finds overlapping areas and keeps only the overlap

**Use when you need to:**
- Find areas that meet ALL criteria
- Identify where features overlap
- Combine attributes from multiple layers
- Find features in multiple buffer zones

**Real Quinhagak Examples:**
- Find parcels within both stream buffer AND wetland areas
- Identify areas affected by multiple contamination sources
- Locate housing plots in both floodplain and high-density zones
- Find areas suitable for development (meeting all criteria)

**Input:** Two or more feature layers
**Output:** Only overlapping areas, with attributes from all inputs

**Analogy:** Venn diagram overlap

**Tool Location:** Analysis Tools → Overlay → Intersect

**Note:** Pairwise Intersect is similar but handles more than two inputs differently

---

## Merge

**What it does:** Combines multiple datasets into one (stacks them)

**Use when you need to:**
- Combine data from different sources
- Join multiple tiles into seamless dataset
- Append new data to existing dataset
- Create unified dataset from pieces

**Real Quinhagak Examples:**
- Merge GPS tracks from multiple days
- Combine infrastructure data from different years
- Unite river segments into complete stream network
- Merge adjacent map tiles

**Input:** Two or more feature classes (must be same geometry type)
**Output:** Single feature class containing all features from all inputs

**Important:** Features don't have to overlap - just combining them!

**Tool Location:** Data Management Tools → General → Merge

---

## Spatial Join

**What it does:** Transfers attributes from one layer to another based on location

**Use when you need to:**
- Add attributes based on what feature is inside, nearest to, or intersects
- Count features within polygons
- Find which zone a point is in
- Transfer information based on location

**Real Quinhagak Examples:**
- Join parcel info to GPS points (what parcel is each point in?)
- Count rusting river points within each watershed
- Add land use type to infrastructure points
- Find nearest road to each building

**Input:** Target features + join features
**Output:** Target features with attributes from join features added

**Key Parameters:**
- Match option:
  - Intersect (default)
  - Closest
  - Within a distance

**Tool Location:** Analysis Tools → Overlay → Spatial Join

---

## Select by Location

**What it does:** Selects features based on spatial relationship to other features

**Use when you need to:**
- Identify features near something
- Find features inside a boundary
- Select features that intersect
- Create subsets based on location

**Real Quinhagak Examples:**
- Select parcels within 100m of contaminated site
- Find all rivers that cross into wetland areas
- Identify buildings within flood zone
- Select infrastructure points near planning area

**Input:** Features to select from + features to select based on
**Output:** Selection (not new feature class - just selected)

**Key Parameters:**
- Relationship type:
  - Intersect
  - Within a distance
  - Completely within
  - Contains
  - Etc.

**Tool Location:** Map → Select by Location

**Pro Tip:** Use this before running other tools to work only with selected features

---

## Near

**What it does:** Calculates distance from each feature to nearest feature in another layer

**Use when you need to:**
- Find distance to closest feature
- Identify nearest neighbor
- Calculate proximity values
- Rank by distance

**Real Quinhagak Examples:**
- Calculate distance from each rusting river to village
- Find distance from each parcel to nearest road
- Measure how far each building is from shoreline
- Identify which infrastructure is closest to airport

**Input:** From features + to features
**Output:** From features with added distance field (and optionally nearest feature ID)

**Tool Location:** Analysis Tools → Proximity → Near

**Note:** Doesn't create lines - just adds distance information to table

---

## Union

**What it does:** Combines features from multiple layers, keeping ALL areas from ALL inputs

**Use when you need to:**
- Preserve all features from all inputs
- Create composite map of multiple layers
- Calculate overlapping and non-overlapping areas
- Complex overlay analysis

**Real Quinhagak Examples:**
- Combine land ownership with land use (show all combinations)
- Union parcels with planning zones (preserve both boundaries)
- Overlay multiple environmental constraints
- Create comprehensive land suitability map

**Input:** Two or more polygon layers
**Output:** All areas from all inputs, subdivided where they overlap

**Analogy:** Layering transparent maps and tracing all boundaries

**Tool Location:** Analysis Tools → Overlay → Union

**Warning:** Can create very complex outputs with many small polygons!

---

## Summary Table: Choosing the Right Tool

| **Your Question** | **Use This Tool** | **What You Get** |
|-------------------|-------------------|------------------|
| What's within 100m of this feature? | Buffer | Zone showing area within distance |
| What's in my study area only? | Clip | Features trimmed to boundary |
| Combine these into one feature | Dissolve | Single merged feature |
| Remove these areas from that | Erase | Features with holes cut out |
| Where do these overlap? | Intersect | Only overlapping areas |
| Stack these datasets together | Merge | Combined dataset |
| What attributes match this location? | Spatial Join | Features with transferred attributes |
| Which features are near/in this? | Select by Location | Selection set |
| How far to nearest feature? | Near | Distance values in table |
| Show all areas from all layers | Union | Comprehensive overlay |

---

## Decision Tree

**START: What are you trying to do?**

```
Do you need to create distance zones?
└─ YES → BUFFER

Do you need to limit data to study area?
└─ YES → CLIP

Do you need to combine multiple features into one?
└─ YES → DISSOLVE

Do you need to remove certain areas?
└─ YES → ERASE

Do you need to find where things overlap?
└─ YES → INTERSECT

Do you need to stack multiple datasets?
└─ YES → MERGE

Do you need to transfer attributes by location?
└─ YES → SPATIAL JOIN

Do you just need to select features by location?
└─ YES → SELECT BY LOCATION

Do you need distance to nearest feature?
└─ YES → NEAR

Do you need comprehensive overlay of all areas?
└─ YES → UNION
```

---

## Common Workflows

### Workflow 1: Site Suitability Analysis

**Goal:** Find suitable parcels for new community building

**Steps:**
1. **Buffer** streams by 50m (setback requirement)
2. **Buffer** roads by 200m (accessibility requirement)
3. **Clip** parcels to planning area
4. **Erase** stream buffers from parcels (remove unbuildable areas)
5. **Intersect** result with road buffers (must be near road)
6. **Select by Location** parcels > 2000 sq meters (size requirement)
7. Review selected parcels - these meet all criteria!

### Workflow 2: Environmental Impact Assessment

**Goal:** Assess impact of contamination on subsistence areas

**Steps:**
1. **Buffer** contamination site by 100m, 500m, 1000m (impact zones)
2. **Intersect** buffers with fishing areas (find overlaps)
3. **Spatial Join** fishing areas to buffers (add distance category)
4. **Calculate** area of fishing grounds affected
5. **Near** tool to find distance to nearest villages
6. Create maps showing impact zones

### Workflow 3: Historical Documentation

**Goal:** Document historical features and their influence areas

**Steps:**
1. Digitize historical features from georeferenced map
2. **Buffer** each feature by 100m (zone of influence)
3. **Dissolve** buffers (create combined historical district)
4. **Clip** current parcels to historical district
5. **Spatial Join** parcel owners to historical features (who's affected)
6. **Near** to calculate distance from each historical feature to current infrastructure

### Workflow 4: Stream Protection Planning

**Goal:** Establish stream protection zones

**Steps:**
1. **Buffer** all streams by 50m (protection buffer)
2. **Dissolve** overlapping buffers (single protection zone)
3. **Intersect** with parcels (which parcels affected)
4. **Calculate** percentage of each parcel in buffer
5. **Spatial Join** to transfer stream names to affected parcels
6. **Select by Location** parcels completely within buffer (highest impact)

---

## Tips for Success

### Before Running Tools

**1. Check Coordinate System**
- Ensure all layers in same coordinate system
- Use projected coordinates (State Plane) not geographic (lat/lon)
- Buffer distances won't work correctly in wrong coordinate system

**2. Understand Your Data**
- Know geometry type (point, line, polygon)
- Check attribute table
- Verify data quality
- Look for gaps or overlaps

**3. Save Your Work**
- Save project before running complex operations
- Some tools take time to run
- Can't undo after tool completes

**4. Test First**
- Try tool on small subset before full dataset
- Verify parameters are correct
- Check results make sense

### During Tool Use

**1. Name Outputs Clearly**
- Include tool name: Parcels_Buffer_100m
- Include date if relevant: Streams_Clip_2024
- Put in geodatabase, not as shapefile

**2. Document Parameters**
- What distance for buffer?
- Which dissolve field?
- What relationship for spatial join?
- Keep notes for reproducibility

**3. Watch for Errors**
- Read error messages carefully
- Common issues: coordinate systems, topology, locked files
- Check tool help if confused

### After Running Tools

**1. Verify Results**
- Does output make sense?
- Check feature count (expected number?)
- Open attribute table
- Review attributes transferred
- Zoom to features and inspect

**2. Check Geometry**
- Any odd shapes?
- Gaps or overlaps where unexpected?
- Tiny slivers (often indicate problems)?

**3. Save and Organize**
- Keep outputs in geodatabase
- Delete failed attempts
- Organize in feature datasets if complex project
- Add metadata

---

## Common Mistakes to Avoid

**1. Wrong Coordinate System**
- Running buffer in geographic coordinates (degrees)
- Layers don't line up
- **Fix:** Project to State Plane first

**2. Forgetting to Select**
- Running tool on entire dataset when you only want subset
- **Fix:** Use Select by Location or Select by Attribute first

**3. Overwriting Important Data**
- Running tool and losing original
- **Fix:** Always create new output, never overwrite input

**4. Not Dissolving Buffers**
- Creating overlapping buffers when you want single zone
- **Fix:** Set dissolve parameter or run Dissolve after

**5. Wrong Tool Choice**
- Using Intersect when you need Union
- Using Merge when you need Dissolve
- **Fix:** Review tool descriptions carefully

**6. Ignoring Attribute Tables**
- Not checking what fields are created
- Missing important information in attributes
- **Fix:** Always open attribute table and review

**7. Unrealistic Distances**
- 100,000 meter buffer (way too big!)
- 0.5 foot buffer (way too small!)
- **Fix:** Think about real-world distances, check units

---

## Getting Help

**In ArcGIS Pro:**
- Hover over tool for description
- Click tool → Help (at bottom) → detailed documentation
- Error messages often contain solutions
- Tool help includes examples

**Online:**
- [ArcGIS Pro Tool Reference](https://pro.arcgis.com/en/pro-app/latest/tool-reference/main/arcgis-pro-tool-reference.htm)
- [Esri Community Forums](https://community.esri.com/)
- [GIS Stack Exchange](https://gis.stackexchange.com/)

**In This Training:**
- Ask instructor
- Consult classmates
- Review lesson materials
- Practice with sample data

---

## Practice Exercises

Try these to build confidence:

**Exercise 1: Basic Buffer**
- Create point for school
- Buffer 500m
- Style to show walking distance

**Exercise 2: Clip Practice**
- Download Alaska rivers layer
- Clip to Quinhagak area
- Count how many rivers in your area

**Exercise 3: Dissolve Parcels**
- Load parcels
- Dissolve by owner name
- See combined properties

**Exercise 4: Site Suitability**
- Find parcels that are:
  - Within 200m of road (Intersect)
  - Outside 50m stream buffer (Erase)
  - Larger than 5000 sq ft (Select by Attribute)

---

## Quick Reference: Tool Icons in ArcGIS Pro

When you see these icons, you know which toolset:

- **Proximity Tools** (Buffer, Near) - Usually show distance lines
- **Overlay Tools** (Intersect, Union, Erase) - Show overlapping shapes
- **Extract Tools** (Clip, Select) - Show extraction/selection

---

**Print this guide and keep it handy while working in ArcGIS Pro!**

**Remember:** Practice makes perfect. The more you use these tools, the more intuitive they become.

---

**Version:** 1.0
**Last Updated:** November 2025
**For:** Quinhagak GIS Training, Module 4
