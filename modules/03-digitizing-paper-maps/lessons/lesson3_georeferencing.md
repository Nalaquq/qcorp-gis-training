# Lesson 3: Georeferencing in ArcGIS Pro

**Duration:** 90 minutes
**Difficulty:** Intermediate
**Prerequisites:** Photographed map, ArcGIS Pro installed

---

## Overview

Georeferencing is the process of aligning a scanned or photographed map to real-world coordinates. This critical skill allows you to overlay historical maps on current basemaps, integrate old surveys into modern GIS, and preserve spatial information from paper records.

---

## Learning Objectives

By the end of this lesson, you will:

1. ✅ Understand what georeferencing is and why it matters
2. ✅ Identify good control points using local knowledge
3. ✅ Add control points in ArcGIS Pro
4. ✅ Understand transformation types
5. ✅ Assess georeferencing accuracy
6. ✅ Save georeferenced maps for use in GIS
7. ✅ Upload georeferenced maps to ArcGIS Online

---

## Part 1: What is Georeferencing? (15 minutes)

### The Problem

You have a paper map from 1982. It shows important land information, but:
- It's just a picture/scan (no coordinate information)
- You can't overlay it on current maps
- You can't measure distances on it
- It won't align with GPS data
- It's not usable in GIS

### The Solution: Georeferencing

Georeferencing assigns real-world coordinates to your image by:
1. Identifying features visible in both the old map and current basemap
2. Marking these matching points (called "control points")
3. Calculating the transformation needed to align the maps
4. Applying that transformation to the entire image

**Analogy:** Like pinning a paper map to a wall at specific spots so it lines up with a map painted on the wall behind it.

### Why This Matters for Quinhagak

**Real Example:** The ANCSA 14(c) survey map from 1982
- Shows land conveyances to the village
- Critical for land management decisions
- No digital version existed
- **After georeferencing:** Can overlay on current imagery, measure areas, analyze changes

**Other Applications:**
- Historical infrastructure maps
- Traditional use area documentation
- Comparing landscape changes over time
- Supporting land claims and surveys
- Preserving elder knowledge of place names

---

## Part 2: Control Points - The Key to Success (20 minutes)

### What Are Control Points?

Control points are features you can identify in BOTH:
- Your historical map (the image you're georeferencing)
- The current basemap (imagery, streets, etc.)

You tell ArcGIS Pro: "This point on the old map is the same as this point on the current basemap."

ArcGIS Pro uses these matched points to figure out how to align the whole map.

### Good Control Points vs Poor Control Points

**✅ GOOD Control Points (Permanent Features):**

1. **Lagoons and Water Bodies**
   - Example: Quinhagak village lagoon
   - Usually stable over decades
   - Clearly visible on imagery
   - Easy to identify exact location

2. **Permanent Buildings**
   - Schools (especially older ones)
   - Churches
   - Government buildings
   - Buildings that existed when map was made AND still exist

3. **Road Intersections**
   - Where roads cross
   - T-intersections
   - Road curves (if distinctive)

4. **River Confluences**
   - Where two rivers meet
   - Usually stable features
   - Clearly visible

5. **Survey Monuments**
   - Section corners
   - Benchmarks
   - If you know where they are

6. **Distinctive Shoreline Features**
   - Points, coves
   - Only if not eroding
   - Verify with elders if uncertain

**❌ POOR Control Points (Temporary or Changing):**

1. **Vegetation**
   - Trees, brush lines
   - Changes over time
   - May be cut or grow

2. **Temporary Structures**
   - Sheds, mobile buildings
   - May have been moved or removed

3. **Eroding Shorelines**
   - Riverbanks that change
   - Coastal erosion areas

4. **Recent Development**
   - New roads, buildings
   - Didn't exist when old map was made!

5. **Ambiguous Features**
   - "A building" (which one?)
   - Uncertain identification

### Using Your Local Knowledge

**This is where YOU have the advantage!**

You know Quinhagak. You can:
- Identify which buildings are old vs new
- Remember or ask about what used to be where
- Recognize distinctive features
- Ask elders about historical features
- Verify if something existed in 1982 (or whenever map was made)

**Student Success Story:**
When georeferencing the 1982 ANCSA map, students used their knowledge to select:
- The village lagoon (they knew it hadn't moved)
- The school (they knew which building was the old school)
- Churches (knew when they were built)
- Road intersections (knew which roads were old)

This local knowledge made georeferencing accurate and successful!

---

## Part 3: Georeferencing Workflow in ArcGIS Pro (45 minutes)

### Step 1: Set Up Your Project

**1. Create New Project**
- Open ArcGIS Pro
- Create new Map project
- Name: "Georeferencing_[MapName]"
- Location: Documents/ArcGIS/

**2. Add Basemap**
- Map tab → Basemap
- Choose appropriate basemap:
  - Imagery (good for older maps)
  - Topographic (good for maps with terrain)
  - Streets (good for infrastructure maps)

**3. Zoom to Quinhagak**
- Navigate to project area
- Zoom to level where you can see details
- Bookmark this view (helpful to return to)

### Step 2: Add Your Map Image

**1. Add Raster**
- Map tab → Add Data → Add Data
- Browse to your photographed map (.jpg or .tiff)
- Add to map

**2. First Look**
- Map will likely appear in wrong place (that's normal!)
- May appear off coast of Africa (coordinate confusion)
- May not appear at all initially

**3. Zoom to Raster**
- Right-click raster in Contents
- Zoom to Layer
- Now you can see your map

### Step 3: Open Georeference Tab

**1. Select Raster**
- Click on raster layer in Contents
- Ensure it's selected (highlighted)

**2. Open Georeference Tab**
- Imagery tab → Georeference
- Georeference ribbon appears

**3. Familiarize with Tools**
- Fit to Display
- Add Control Points
- Control Point Table
- Transformation
- Save/Cancel

### Step 4: Add Control Points

**This is the core of georeferencing!**

**Workflow for Each Control Point:**

1. **Find feature on your raster (old map)**
   - Click "Add Control Points" tool (or F9)
   - Click on a feature you can identify
   - Example: Center of lagoon on old map

2. **Find same feature on basemap**
   - Right-click → "Add X/Y" OR
   - Pan to find same feature on basemap
   - Click on exact same spot on basemap
   - Example: Center of lagoon on current imagery

3. **Point is added**
   - Link line connects the two points
   - Map begins to align (after 3+ points)

**Repeat for multiple control points**

**How Many Points?**
- Minimum: 3 points
- Recommended: 6-10 points
- More points can improve accuracy
- But bad points hurt accuracy!
- Quality over quantity

**Distribution Matters:**
- Spread points across entire map
- Don't cluster in one area
- Cover all four corners if possible
- Better coverage = better accuracy

### Step 5: Review and Refine

**1. Check Alignment**
- Toggle raster on/off
- Does it line up with basemap?
- Check multiple areas of map

**2. Review RMS Error**
- Open Control Point Table
- Check RMS Error column
- Lower is better
- Generally want < 5 pixels
- High error? Remove or adjust that point

**3. Identify Problem Points**
- Points with high residual error
- May be wrong identification
- May be bad control point choice
- Right-click → Delete to remove

**4. Add More Points if Needed**
- If alignment poor in certain area
- Add more points in that area
- Refine existing points

### Step 6: Choose Transformation

**Transformation Type:**
- Polynomial 1 (Affine) - **Use this for most maps**
  - Allows rotation, scale, skew
  - Requires 3+ control points
  - Good for maps without major distortion

- Polynomial 2 - For larger areas with curvature
  - Requires 6+ control points

- Polynomial 3 - For complex distortion
  - Requires 10+ control points

- Spline - Exact fit to control points
  - Use for very warped maps
  - Requires many points

**For most Quinhagak historical maps: Use Polynomial 1**

### Step 7: Save Georeferenced Map

**1. Verify Everything Looks Good**
- Check alignment throughout map
- Verify RMS error acceptable
- Test a few features

**2. Save**
- Georeference tab → Save
- Choose save location
- Creates new georeferenced raster
- Original image unchanged

**3. Close Georeference Tab**
- Click Close Georeference

**4. Test Result**
- Remove original un-georeferenced raster
- Add basemap
- Georeferenced map should align perfectly!

---

## Part 4: Special Case - Using PLSS Grid (10 minutes)

### When Your Map Has a Grid

Many survey maps include PLSS (Public Land Survey System) section grids.

**Advantage:** Grid lines are legally surveyed and precisely located!

### Workflow:

**1. Add PLSS Layer**
- Search ArcGIS Online for "Alaska PLSS"
- Add PLSS Sections layer
- Turn on labels (show section numbers)

**2. Identify Grid on Your Map**
- Find section lines on historical map
- Note section numbers
- Identify township and range

**3. Use Grid Intersections as Control Points**
- Where two section lines cross = section corner
- These are surveyed points
- Match corner on old map to same corner on PLSS layer
- Very accurate control points!

**4. Verify Section Numbers Match**
- Section 1 on old map = Section 1 on PLSS layer
- Sections numbered 1-36 in each township
- If numbers don't match, check township/range

**Student Success:**
After georeferencing the ANCSA map using village features, students added the PLSS grid layer and verified that section boundaries aligned correctly - confirming their georeferencing was accurate!

---

## Part 5: Uploading to ArcGIS Online (10 minutes)

### Export from ArcGIS Pro

**1. Right-click georeferenced raster**
- Data → Export Raster
- Or: Share tab → Package

**2. Settings**
- Format: TIFF (preferred) or JPEG
- Include georeferencing information
- Choose quality/compression

**3. Export**
- Save to known location
- Note file name

### Upload to ArcGIS Online

**1. Sign in to ArcGIS Online**
- Go to arcgis.com
- Sign in with organization account

**2. Add Item**
- My Content → Add Item
- From Computer
- Browse to exported raster

**3. Add Information**
- Title: Descriptive name
  - Example: "Quinhagak ANCSA 14(c) Survey Map 1982"
- Tags: quinhagak, historical, ANCSA, 1982, survey
- Summary: Brief description
- Credits: Who created, photographed, georeferenced

**4. Share**
- Share to appropriate Group
- Example: Quinhagak Georeferenced Maps
- Set sharing permissions (Group, Organization, or Public)

**5. Test**
- Create new web map
- Add your georeferenced map
- Verify it aligns with basemap
- Share success with community!

**Real Example:** https://arcg.is/0H8S1y1

---

## Practice Exercise

### Exercise: Georeference a Sample Map

**You will need:**
- Photographed map
- ArcGIS Pro
- 30-45 minutes

**Steps:**

1. **Examine Your Map First**
   - What year is it from?
   - What features can you identify?
   - Which features still exist?
   - Plan your control points

2. **Set Up Project**
   - Create new project
   - Add appropriate basemap
   - Add your map image

3. **Add 6-8 Control Points**
   - Use features you identified
   - Spread across map
   - Use your local knowledge!

4. **Check and Refine**
   - Review RMS error
   - Adjust problem points
   - Add more if needed

5. **Save and Test**
   - Save georeferenced map
   - Test alignment
   - Create simple web map

6. **Document**
   - What control points did you use?
   - What was your RMS error?
   - What challenges did you face?
   - How did you solve them?

---

## Common Issues and Solutions

### Issue: Can't Find Matching Features

**Problem:** Map is too old, area has changed completely

**Solutions:**
- Look for PLSS grid or other survey markers
- Research historical photos
- Ask elders about features
- Look for water features (more stable)
- Try different basemap (historical imagery if available)

### Issue: High RMS Error

**Problem:** Some control points have high residual error

**Solutions:**
- Open Control Point Table
- Sort by residual error
- Delete or adjust worst points
- Verify feature identification
- Add better-distributed points

### Issue: Map Stretches Oddly

**Problem:** Wrong transformation type or bad control points

**Solutions:**
- Try Polynomial 1 transformation
- Check for outlier control points
- Verify features correctly identified
- Ensure points distributed across map

### Issue: Can't See Control Points Clearly

**Problem:** Zoom level or image quality

**Solutions:**
- Zoom in closer when adding points
- Enhance raster contrast (Appearance tab)
- Try different basemap
- Use magnifier window

---

## Assessment

### Knowledge Check

1. What is georeferencing?
2. Why do we need at least 3 control points?
3. Name 3 good control points for a 1980s Quinhagak map
4. Name 3 poor control points and why
5. What is RMS error and what's a good target?
6. When would you use Polynomial 1 vs Spline transformation?
7. How did local knowledge help in the ANCSA map success?

### Practical Demonstration

Successfully georeference a map with:
- ✅ At least 6 control points
- ✅ Points distributed across map
- ✅ RMS error < 5 pixels
- ✅ Visual alignment verified
- ✅ Saved properly
- ✅ Uploaded to ArcGIS Online

---

## Key Takeaways

1. **Georeferencing makes historical maps usable in modern GIS**
2. **Control points are the key to success**
3. **Local knowledge is your advantage** - you know what features existed when!
4. **Quality over quantity** - 6 good points better than 20 bad points
5. **PLSS grids are excellent control points** if visible on map
6. **Always verify your results** - does alignment make sense?
7. **Share your work** - make georeferenced maps accessible to community

---

## Next Steps

- [Lesson 4: Working with Grid Overlays →](./lesson4_grid_overlays.md)
- Practice georeferencing more maps from land manager's office
- Help build the community's digital map collection
- Share knowledge with others!

---

## Resources

- [Esri Georeferencing Tutorial](https://learn.arcgis.com/en/projects/georeference-a-historical-map/)
- [ArcGIS Pro Georeferencing Documentation](https://pro.arcgis.com/en/pro-app/latest/help/data/imagery/overview-of-georeferencing.htm)
- [Quinhagak Georeferenced Maps Group](https://arcg.is/0H8S1y1)

---

**Lesson Version:** 1.0
**Last Updated:** November 2025
**Based on:** Successful georeferencing of 40 maps in one day!
