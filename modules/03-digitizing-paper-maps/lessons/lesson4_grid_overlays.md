# Lesson 4: Working with Grid Overlays

**Duration:** 45 minutes
**Difficulty:** Intermediate
**Prerequisites:** Lesson 3 (Georeferencing basics)

---

## Overview

Many historical maps include grid systems like PLSS (Public Land Survey System). These grids are precisely surveyed and make excellent control points for georeferencing. This lesson teaches you how to leverage grid overlays for more accurate georeferencing.

---

## Learning Objectives

By the end of this lesson, you will:

1. ✅ Understand PLSS (Public Land Survey System)
2. ✅ Recognize grid systems on historical maps
3. ✅ Add PLSS layers in ArcGIS Pro
4. ✅ Use grid intersections as control points
5. ✅ Verify georeferencing accuracy using grids
6. ✅ Work with Township and Range notation

---

## Part 1: Understanding PLSS (15 minutes)

### What is PLSS?

**Public Land Survey System:**
- Surveying method used across much of the United States
- Divides land into Townships and Sections
- Creates a rectangular grid system
- Used extensively in Alaska

**Why It Exists:**
- Systematic way to describe land locations
- Legal land descriptions
- Property boundaries
- Survey reference system

### The PLSS Hierarchy

**Principal Meridian and Base Line:**
- Starting references for the grid
- In Alaska: Copper River Meridian, Fairbanks Meridian, etc.

**Townships:**
- 6 miles × 6 miles squares
- Numbered from baseline (North or South)
- Example: Township 12 North (T12N)

**Ranges:**
- 6 miles wide columns
- Numbered from principal meridian (East or West)
- Example: Range 73 West (R73W)

**Sections:**
- 1 mile × 1 mile squares (usually)
- 36 sections in each township
- Numbered 1-36 in specific pattern:
  ```
  6   5   4   3   2   1
  7   8   9   10  11  12
  18  17  16  15  14  13
  19  20  21  22  23  24
  30  29  28  27  26  25
  31  32  33  34  35  36
  ```

**Legal Description Example:**
"NE 1/4 of Section 12, T12N, R73W, Copper River Meridian"

Translates to:
- Northeast quarter
- Of Section 12
- In Township 12 North
- Range 73 West
- Referenced to Copper River Meridian

### PLSS in Alaska

**Coverage:**
- Not all of Alaska is surveyed under PLSS
- Primarily:
  - Homestead areas
  - Resource development areas
  - ANCSA conveyance areas
  - Areas around communities

**Quinhagak Area:**
- PLSS sections exist
- Used for ANCSA land conveyances
- Visible on many historical maps
- Excellent for georeferencing!

### Why PLSS Grids Are Excellent Control Points

**Advantages:**
1. **Legally Surveyed** - Precise, documented locations
2. **Permanent** - Section corners are monumented
3. **Easy to Identify** - Grid lines visible on many maps
4. **Verifiable** - Can cross-check section numbers
5. **Widely Available** - PLSS data available from BLM
6. **Distributed** - Grid provides evenly-spaced control points

**Perfect for Georeferencing:**
- Historical survey maps often show PLSS grid
- Modern GIS layers show same grid
- Match section corners exactly
- Multiple control points available

---

## Part 2: Identifying Grids on Historical Maps (10 minutes)

### Types of Grids You Might Encounter

**1. PLSS Section Grid**
- Township and section lines
- Section numbers (1-36)
- May show quarter-sections
- Most common on survey maps

**2. UTM Grid**
- Universal Transverse Mercator
- Metric grid (1km or 10km intervals)
- Numbers indicate coordinates
- Less common on local maps

**3. State Plane Grid**
- Alaska State Plane zones
- Usually in feet
- Tick marks on map edges
- Common on modern maps

**4. Lat/Long Grid**
- Latitude and longitude lines
- Degrees and minutes
- Often on older topographic maps
- Can be used but less precise

### What to Look For on Your Map

**Grid Lines:**
- Look for regular pattern of lines
- Usually lighter than other features
- May be dashed or dotted
- Cross entire map

**Labels:**
- Section numbers (1-36)
- Township/Range notation (T12N R73W)
- Coordinate values
- Grid intervals

**Legend/Title Block:**
- May specify grid system
- "PLSS shown"
- "Sections shown"
- Township and Range of map

**Corner Marks:**
- Survey monuments
- Section corners
- May show as symbols

### Example: ANCSA 14(c) Map

**The 1982 ANCSA map georeferenced by students showed:**
- ✅ PLSS section grid visible
- ✅ Section numbers labeled
- ✅ Township and Range noted in title block
- ✅ Section corners marked

**This grid was used to verify georeferencing accuracy after using village features as initial control points!**

---

## Part 3: Adding PLSS Layers in ArcGIS Pro (10 minutes)

### Finding PLSS Data

**Source 1: ArcGIS Online / Living Atlas**

1. In ArcGIS Pro, click "Portal" tab
2. Search: "Alaska PLSS"
3. Look for:
   - "BLM Alaska PLSS Sections"
   - "Alaska Cadastral Survey"
4. Add to map

**Source 2: Bureau of Land Management (BLM)**

1. Go to BLM website
2. Navigate to cadastral survey data
3. Download Alaska PLSS shapefile
4. Add to ArcGIS Pro

**Source 3: Alaska State GIS Data**

1. Alaska Geospatial Data Clearinghouse
2. Search for PLSS or cadastral
3. Download and add

### Layer Properties to Understand

Once PLSS layer is added:

**Attribute Table includes:**
- Township (TWNSHPNO)
- Range (RANGENO)
- Section (SECTION)
- Section Number (SECTNNO)
- Survey information

**Geometry:**
- Polygon features (section boundaries)
- Line features (section lines)
- Point features (section corners)

**Coverage:**
- May not cover all of Alaska
- Verify coverage in your area

### Symbolizing PLSS Layer

**For Use as Reference:**

1. **Section Polygons:**
   - No fill (transparent)
   - Outline only
   - Thin line (0.5 pt)
   - Contrasting color (red or blue)

2. **Labels:**
   - Turn on labels
   - Label with Section Number
   - Clear, readable font
   - Size: 10-12 pt

3. **Transparency:**
   - Set to 40-50%
   - Can see through to basemap
   - Can see through to your raster

**This allows you to overlay PLSS on your historical map!**

---

## Part 4: Using Grids for Georeferencing (15 minutes)

### Method 1: Section Corners as Control Points

**Best when:**
- Section corners visible/marked on historical map
- PLSS layer available
- Need highly accurate georeferencing

**Workflow:**

1. **Add PLSS layer to ArcGIS Pro**
   - Symbolize with section outlines
   - Turn on section number labels

2. **Identify section corners on historical map**
   - Where 4 sections meet
   - May be marked with symbol
   - Grid line intersections

3. **Add Control Points**
   - Georeference tab → Add Control Points
   - Click on section corner on historical map
   - Click on same section corner on PLSS layer
   - (Use vertex snapping to hit exact corner!)

4. **Verify Section Numbers**
   - Check that section numbers match
   - Historical map Section 12 = PLSS Section 12
   - If numbers don't match, wrong location!

5. **Use Multiple Corners**
   - Minimum 4 corners (one from each quadrant of map)
   - More corners = better accuracy
   - Distribute across entire map

**Advantages:**
- Very accurate (surveyed points)
- Easy to verify correctness
- Multiple points available
- High confidence

### Method 2: Grid Line Intersections

**Best when:**
- Grid lines visible but corners not marked
- Less detailed historical map
- Need quick georeferencing

**Workflow:**

1. **Identify grid on historical map**
   - Section grid lines
   - Note pattern and spacing

2. **Add PLSS layer**
   - Match section numbers
   - Verify you're in correct township/range

3. **Use line intersections as control points**
   - Where grid lines cross
   - Pick clear, unambiguous intersections
   - Use zoomed-in view for precision

4. **Add control points**
   - Click intersection on historical map
   - Click same intersection on PLSS layer
   - Multiple intersections across map

### Method 3: Hybrid Approach (Recommended!)

**Use BOTH local features AND grid:**

**Step 1: Initial Georeferencing with Local Features**
- Use village features (buildings, roads, lagoon)
- Get map approximately in right place
- 4-6 control points

**Step 2: Verification with PLSS Grid**
- Add PLSS layer
- Check if sections align
- If alignment good → georeferencing successful!
- If alignment poor → adjust control points

**Step 3: Refinement**
- Add section corners as additional control points
- Improves accuracy
- Provides verification

**This was the approach used successfully with the ANCSA 14(c) map!**

### Checking Your Work

**After Georeferencing:**

1. **Toggle PLSS layer on/off**
   - Does historical map grid align with PLSS?
   - Check multiple locations

2. **Check Section Numbers**
   - Do section numbers match?
   - Section 1 on map = Section 1 on PLSS?

3. **Check Grid Spacing**
   - Are sections approximately 1 mile × 1 mile?
   - Measure using ArcGIS Pro measure tool
   - Should be ~5,280 feet (1 mile)

4. **Visual Inspection**
   - Zoom to different areas
   - Check alignment throughout map
   - Look for systematic errors

**If Everything Aligns:**
✅ Excellent! Your georeferencing is accurate!

**If Grid is Off:**
❌ Review control points, may need adjustment

---

## Part 5: Special Considerations (10 minutes)

### Irregular Sections

**Not All Sections Are Perfect Squares:**

- **Correction Lines** - Adjust for earth curvature
- **Fractional Sections** - Along boundaries, water bodies
- **Lots** - Irregular pieces
- **Meandered Lines** - Follow water boundaries

**What This Means:**
- Section might not be exactly 1 mile × 1 mile
- Grid might have slight offsets
- Still useful for georeferencing
- Just be aware of irregularities

### Historical Survey Accuracy

**Older Surveys:**
- May have errors (surveying technology limited)
- Corners may be slightly off
- Grid lines may not be perfectly straight

**Modern PLSS GIS Layers:**
- Usually based on best available survey data
- May have been adjusted/corrected
- Generally very accurate

**Impact on Georeferencing:**
- Minor discrepancies possible
- Still much better than no grid reference
- Use RMS error to verify acceptable accuracy

### Maps Without Section Numbers

**Problem:** Grid lines visible but no section numbers labeled

**Solutions:**
1. Research map to determine Township/Range
2. Look for numbered sections to establish pattern
3. Count sections following standard numbering
4. Consult land records for area
5. Use other control points to get approximate location, then match to PLSS

### Coordinate System Considerations

**Historical maps may be in different coordinate systems:**
- Old datum (NAD27 vs modern NAD83)
- Different projection
- Different zone

**PLSS layer coordinate system:**
- Check layer properties
- Usually in modern coordinate system

**Your georeferencing:**
- Set map coordinate system to match PLSS layer
- Or ensure ArcGIS Pro reprojects on-the-fly
- Verify alignment

---

## Practice Exercise

### Exercise: Georeference Using PLSS Grid

**You will need:**
- Historical map with visible PLSS grid
- ArcGIS Pro
- PLSS layer
- 30 minutes

**Steps:**

1. **Examine Map**
   - Identify PLSS grid
   - Note section numbers visible
   - Note Township and Range (if shown)
   - Plan which corners to use

2. **Set Up ArcGIS Pro**
   - Add historical map
   - Add PLSS layer from ArcGIS Online
   - Symbolize PLSS (transparent fill, visible outlines)
   - Turn on section number labels

3. **Verify Coverage**
   - Is PLSS layer available for your map area?
   - Do section numbers seem to match?

4. **Add Control Points - Round 1 (PLSS Grid)**
   - Add 4-6 control points using section corners
   - Distribute across map
   - Use vertex snapping for precision

5. **Initial Assessment**
   - Check RMS error
   - Toggle raster on/off to check alignment
   - Verify section numbers match

6. **Add Control Points - Round 2 (Local Features)**
   - Add 2-4 local feature control points
   - Buildings, roads, water features
   - Refine alignment

7. **Final Verification**
   - Check grid alignment throughout map
   - Measure section to verify ~1 mile
   - Review RMS error
   - Document control points used

8. **Save and Document**
   - Save georeferenced raster
   - Export control point table
   - Note accuracy assessment

---

## Key Takeaways

1. **PLSS grids are surveyed and legally defined** - Excellent control points
2. **Section corners are most accurate** - Use when visible
3. **Verify section numbers match** - Critical check
4. **Hybrid approach works best** - Local features + grid verification
5. **Not all sections are perfect squares** - Expect minor irregularities
6. **PLSS data available from BLM and ArcGIS Online** - Free resources
7. **Grid overlay confirms accuracy** - Great verification tool

---

## Real-World Success: Quinhagak ANCSA Map

**The Challenge:**
- 1982 ANCSA 14(c) survey map
- Needed accurate georeferencing
- Critical for land management

**The Approach:**
1. Students used local knowledge (village lagoon, buildings)
2. Added 6 control points using familiar features
3. Georeferenced map
4. **Then added PLSS layer to verify!**

**The Result:**
- PLSS sections aligned perfectly with georeferenced map
- Confirmed accurate georeferencing
- Section numbers matched
- Grid spacing correct (~1 mile sections)

**The Lesson:**
Local knowledge + grid verification = Success!

---

## Assessment Questions

1. What does PLSS stand for and what is it?
2. How large is a standard section?
3. How are sections numbered within a township?
4. Why are section corners excellent control points?
5. Describe the hybrid georeferencing approach.
6. How can you verify georeferencing accuracy using PLSS?
7. What should you do if section numbers don't match after georeferencing?

---

## Next Steps

- [Lesson 5: Uploading to ArcGIS Online →](./lesson5_uploading.md)
- Practice identifying grids on historical maps
- Experiment with PLSS-based georeferencing
- Build confidence in verification techniques

---

## Resources

- [BLM Alaska Cadastral Survey](https://www.blm.gov/programs/national-cadastral-survey)
- [Understanding PLSS](https://nationalmap.gov/small_scale/a_plss.html)
- [Alaska Geospatial Data](https://agc.dnr.alaska.gov/)

---

**Lesson Version:** 1.0
**Last Updated:** November 2025
**Success Story:** ANCSA map verified with PLSS!
