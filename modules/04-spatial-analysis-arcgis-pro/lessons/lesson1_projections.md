# Lesson 1: Projections and Coordinate Systems

**Duration:** 90 minutes
**Difficulty:** Intermediate
**Prerequisites:** Basic understanding of maps

---

## Overview

Understanding map projections is fundamental to working with GIS. This lesson uses a hands-on balloon activity to demonstrate why all 2D maps involve distortion, then teaches you how to work with different coordinate systems in ArcGIS Pro.

---

## Learning Objectives

By the end of this lesson, you will:

1. ✅ Understand why map projections introduce distortion
2. ✅ Explain the difference between 3D earth and 2D maps
3. ✅ Change coordinate systems in ArcGIS Pro Map Properties
4. ✅ Visualize how different projections change basemaps
5. ✅ Understand Alaska State Plane zones
6. ✅ Know when to use WGS84 vs State Plane projections
7. ✅ Consider projection implications for handheld data collection

---

## Part 1: The Balloon Activity (30 minutes)

### Materials Needed
- One inflated balloon per group (2-3 students)
- Permanent markers
- Paper and pencil
- Scissors (for popping)

### Activity Steps

**Step 1: Map Alaska on the Balloon**
1. Imagine the balloon is the Earth
2. Using a marker, draw the outline of Alaska on the balloon
3. Mark several Yup'ik villages as points:
   - Quinhagak
   - Bethel
   - Nome
   - Kotzebue
   - Barrow

**Step 2: Observe the 3D Representation**
- Notice how the points relate to each other on the curved surface
- Measure approximate distances between villages (with string along surface)
- Note: Everything sits on a curved surface, no distortion yet

**Step 3: Pop the Balloon**
- Carefully pop the balloon with scissors
- Try to lay it completely flat on the table

**Step 4: Observe What Happens**
- Can you lay it perfectly flat? (Answer: No!)
- What happens when you try to flatten it?
  - Material tears, OR
  - Material stretches, OR
  - You have to crumple/fold it
- Notice how distances between points are now different
- Some areas are stretched, others compressed

### Key Insight

**This is the fundamental challenge of cartography:** You cannot convert a 3D sphere to a 2D plane without introducing distortion.

Every map projection is a different compromise:
- Some preserve **area** (equal-area projections)
- Some preserve **shape** (conformal projections)
- Some preserve **distance** (equidistant projections)
- Some preserve **direction** (azimuthal projections)
- **None can preserve everything!**

### Discussion Questions

1. What happened to Alaska's shape when you flattened the balloon?
2. Did the distances between villages stay the same?
3. If you were creating a map, what would you want to preserve? (area, shape, distance, direction)
4. Why might different users need different map projections?

---

## Part 2: Coordinate Systems Basics (20 minutes)

### Key Concepts

#### Geographic Coordinate System (GCS)
- Uses latitude and longitude (degrees)
- Describes locations on 3D earth surface
- Examples: WGS84, NAD83
- **WGS84** - World Geodetic System 1984
  - Used by GPS satellites
  - Used by most smartphones and handheld devices
  - Global standard for location

#### Projected Coordinate System (PCS)
- Uses X,Y coordinates (meters or feet)
- Describes locations on 2D flat map
- Must be based on a GCS
- Examples: Alaska State Plane, UTM, Web Mercator

### Why This Matters for Quinhagak

**Scenario 1: Collecting Data with GPS**
- Your handheld GPS records locations in WGS84
- Data appears in latitude/longitude
- Works anywhere in the world
- Good for: field data collection, general navigation

**Scenario 2: Measuring Distances in Quinhagak**
- Need accurate measurements for land management
- Alaska State Plane Zone 7 (EPSG:26937) designed for accuracy in this region
- Uses feet or meters instead of degrees
- Good for: parcels, infrastructure, local planning

**The Challenge:**
- Field data comes in WGS84
- Local maps use State Plane
- You need to work with both!

### Alaska State Plane Zones

Alaska is too large for one projection to be accurate everywhere, so it's divided into **10 State Plane zones**.

**Quinhagak is in Zone 7**
- EPSG Code: **26937** (NAD83 Alaska State Plane Zone 7)
- Units: feet
- Optimized for accuracy in this region
- Used by Alaska Department of Transportation

**Why zones exist:**
- Smaller areas = less distortion
- Each zone optimized for local accuracy
- Distortion increases as you move away from zone center

### Resource: Exploring EPSG Codes

Visit: https://epsg.io/26937

This site shows:
- Projection parameters
- Area of use
- Coordinate system details
- Export formats

**Explore:**
1. Search for EPSG:26937 (Alaska State Plane Zone 7)
2. Look at the "Area of use" map - see Quinhagak's location
3. Note the units (feet)
4. Compare with EPSG:4326 (WGS84)

### Additional Resource

State Plane Coordinate System guide:
https://gisgeography.com/state-plane-coordinate-system-spcs/

---

## Part 3: Changing Coordinate Systems in ArcGIS Pro (40 minutes)

### Exercise 1: Starting a New Project

**Step 1: Create Project**
1. Open ArcGIS Pro
2. Click "Map" template
3. Name: "Projections_Practice"
4. Location: Documents/ArcGIS/
5. Click OK

**Step 2: Add Alaska Basemap**
1. In Map tab, click "Basemap"
2. Choose "Imagery" or "Topographic"
3. Zoom to Alaska
4. Zoom closer to Quinhagak area
   - Longitude: ~-161.9
   - Latitude: ~59.76

### Exercise 2: Check Current Coordinate System

**Step 1: Open Map Properties**
1. Right-click on "Map" in Contents pane
2. Select "Properties"
3. Click "Coordinate Systems" tab

**Step 2: Identify Current System**
- Look at "Current XY"
- Default is usually Web Mercator (EPSG:3857)
- Note: Web Mercator designed for web maps, not accurate measurements!

### Exercise 3: Change to WGS84

**Step 1: Search for WGS84**
1. In Coordinate Systems search box, type: "WGS84"
2. Expand "Geographic Coordinate Systems"
3. Expand "World"
4. Select "WGS 1984" (EPSG:4326)
5. Click OK

**Step 2: Observe Changes**
- Watch how the basemap transforms
- Notice the shape of Alaska changes
- Zoom level may change
- Coordinates at bottom now show lat/lon in degrees

**Discussion:**
- How did Alaska's shape change?
- What happened to Greenland? (Web Mercator makes it huge!)

### Exercise 4: Change to Alaska State Plane Zone 7

**Step 1: Search for State Plane**
1. Open Map Properties → Coordinate Systems again
2. Search: "Alaska State Plane Zone 7"
3. Look for NAD 1983 StatePlane Alaska 7 FIPS 5007
4. Select it
5. Click OK

**Step 2: Observe Changes**
- Basemap transforms again
- Now optimized for accuracy in Quinhagak region
- Coordinates at bottom show feet or meters
- Alaska appears different shape than WGS84

**Step 3: Add Coordinate Display**
1. Look at bottom right of map
2. See X,Y coordinates as you move mouse
3. Note units (feet)

### Exercise 5: Compare Multiple Projections

Create a table comparing how the same location appears:

| Projection | Quinhagak X | Quinhagak Y | Units | Use Case |
|------------|-------------|-------------|-------|----------|
| WGS84 | -161.9° | 59.76° | Degrees | GPS, global |
| Alaska State Plane Zone 7 | ~1,847,000 | ~460,000 | Feet | Local planning |
| Web Mercator | ~-18,020,000 | ~8,393,000 | Meters | Web maps |

**Try This:**
1. Switch between coordinate systems
2. Position mouse over same landmark each time
3. Record coordinates
4. Notice how dramatically they differ!

---

## Part 4: Working with Multiple Coordinate Systems (20 minutes)

### The ArcGIS Pro Solution: "On-the-Fly" Projection

**Good News:** ArcGIS Pro automatically handles layers in different coordinate systems!

**How it works:**
1. Your map has a coordinate system (set in Map Properties)
2. You add a layer with different coordinate system
3. ArcGIS Pro automatically transforms the layer to match your map
4. Layers from different sources display together seamlessly

**Example:**
- Map coordinate system: Alaska State Plane Zone 7
- GPS data collected in: WGS84
- AGOL basemap in: Web Mercator
- **Result:** Everything displays together correctly!

### Best Practices

**For Data Collection:**
- ✅ Handheld GPS devices use WGS84 - that's fine!
- ✅ ArcGIS Pro will transform to your map projection
- ✅ Know what coordinate system your data is in

**For Analysis:**
- ✅ Set map to appropriate projection BEFORE starting analysis
- ✅ Use Alaska State Plane Zone 7 for Quinhagak area work
- ✅ Use WGS84 for regional/global work
- ⚠️ Don't use Web Mercator for measurement/analysis!

**For Measurement:**
- ✅ Use projected coordinate system (State Plane, UTM)
- ✅ Choose appropriate units (feet or meters)
- ⚠️ Don't measure distances in lat/lon (degrees)!

**For Sharing:**
- ✅ WGS84 most universally compatible
- ✅ Web Mercator for web maps
- ✅ Document coordinate system in metadata

---

## Part 5: Real-World Application for Quinhagak (10 minutes)

### Scenario: Planning a Community Survey

**The Situation:**
You need to survey land parcels using a handheld GPS device.

**Questions to Consider:**

1. **What coordinate system will your GPS use?**
   - Answer: WGS84 (that's what GPS satellites broadcast)

2. **What coordinate system should your ArcGIS Pro map use?**
   - Answer: Alaska State Plane Zone 7 (for accurate local measurements)

3. **Will there be a problem?**
   - Answer: No! ArcGIS Pro handles the transformation automatically

4. **What do you need to do?**
   - Set up map in Alaska State Plane Zone 7
   - Collect GPS data (in WGS84)
   - Import GPS data to ArcGIS Pro
   - ArcGIS Pro transforms it to match map
   - Verify data appears in correct location

### Common Issues and Solutions

**Problem:** GPS data appears in wrong location (e.g., off coast of Africa)

**Likely Cause:** Coordinate system confusion
- Data in WGS84 being interpreted as State Plane
- Or vice versa

**Solution:**
1. Check data's actual coordinate system
2. Define coordinate system correctly (don't project it)
3. Let ArcGIS Pro transform to map coordinate system

**Problem:** Measurements don't match field measurements

**Likely Cause:** Wrong coordinate system for measurement

**Solution:**
1. Ensure map uses projected coordinate system (State Plane)
2. Don't measure in WGS84 (geographic coordinates)
3. Check units (feet vs meters)

---

## Summary

### Key Takeaways

1. **3D to 2D = Distortion**
   - Cannot avoid it
   - Choose projection based on what you need to preserve

2. **Two Main Types**
   - Geographic (lat/lon, degrees) - WGS84
   - Projected (X,Y, feet/meters) - State Plane

3. **For Quinhagak Work**
   - Use Alaska State Plane Zone 7 (EPSG:26937)
   - GPS data in WGS84 is fine, ArcGIS Pro will transform

4. **Best Practices**
   - Set appropriate projection at project start
   - Use projected coordinates for measurement
   - Know what coordinate system your data uses
   - Let ArcGIS Pro handle transformations

### Vocabulary

- **Projection** - Mathematical transformation from 3D earth to 2D map
- **Coordinate System** - Framework for defining locations
- **GCS** - Geographic Coordinate System (lat/lon)
- **PCS** - Projected Coordinate System (X,Y)
- **WGS84** - World Geodetic System 1984, GPS standard
- **EPSG Code** - Standardized identifier for coordinate systems
- **State Plane** - Projection system designed for US states
- **Distortion** - Unavoidable changes when flattening sphere

---

## Practice Exercises

### Exercise 1: Projection Explorer
1. Open ArcGIS Pro
2. Add Alaska basemap
3. Try at least 5 different projections
4. Screenshot Alaska in each projection
5. Note which preserves shape, which preserves area

### Exercise 2: Find Your EPSG Code
1. Go to https://epsg.io/
2. Search for your home village or region
3. Find appropriate State Plane zone
4. Note EPSG code
5. Try using it in ArcGIS Pro

### Exercise 3: Coordinate Comparison
1. Pick a landmark in Quinhagak
2. Record its coordinates in:
   - WGS84 (lat/lon)
   - Alaska State Plane Zone 7 (X,Y feet)
   - UTM Zone 3N (X,Y meters)
3. Understand these are all the same location!

---

## Additional Resources

### Online Tools
- [EPSG.io - Coordinate System Database](https://epsg.io/)
- [Projection Wizard - Choose Right Projection](https://projectionwizard.org/)

### Reading
- [Understanding Coordinate Systems and Projections](https://pro.arcgis.com/en/pro-app/latest/help/mapping/properties/coordinate-systems-and-projections.htm)
- [State Plane Coordinate System Explained](https://gisgeography.com/state-plane-coordinate-system-spcs/)
- [Alaska State Plane Zones Map](https://www.commerce.alaska.gov/web/portals/4/pub/StatePlane.pdf)

### Videos
- [Coordinate Systems Explained (Esri)](https://www.esri.com/arcgis-blog/products/arcgis-pro/mapping/coordinate-systems-101/)

---

## Assessment Questions

1. Why can't we make a perfectly accurate flat map of the earth?
2. What is the difference between a geographic and projected coordinate system?
3. Why does Alaska use 10 different State Plane zones instead of just one?
4. Your GPS device collects data in WGS84, but your map is in Alaska State Plane Zone 7. Is this a problem? Why or why not?
5. When should you use WGS84 vs Alaska State Plane Zone 7?
6. What is an EPSG code and why is it useful?
7. Explain the balloon activity to someone who wasn't here. What did it demonstrate?

---

## Next Lesson

[Lesson 2: Adding Content from ArcGIS Online →](./lesson2_adding_content.md)

Learn how to bring your AGOL web map layers into ArcGIS Pro for advanced analysis!

---

**Lesson Version:** 1.0
**Last Updated:** November 2025
