# Lesson 12: Using Edit Tools - Merge, Split, and Extend

**Duration:** 60 minutes
**Difficulty:** Intermediate
**Prerequisites:** Lesson 11 (Creating Layers), Lesson 5 (Creating Features), basic editing experience

---

## Overview

When working with GPS trail data or digitizing features, you'll often need to modify, combine, or divide features to create accurate representations. GPS tracks may have gaps or overlaps, trails may need to be split into segments, or separate features may need to be combined into one.

This lesson focuses on three essential editing tools in ArcGIS Pro:
- **Merge:** Combine multiple features into one
- **Split:** Divide a feature into separate parts
- **Extend:** Extend a line to meet another line

These tools are critical for cleaning GPS data, managing trail networks, and preparing data for analysis.

---

## Learning Objectives

By the end of this lesson, you will be able to:

1. ✅ Use the Merge tool to combine multiple features into one
2. ✅ Split features into separate parts
3. ✅ Extend line features to connect with other features
4. ✅ Clean GPS trail data for accurate analysis
5. ✅ Understand when to use each editing tool
6. ✅ Apply edit tools to prepare data for grant applications

---

## Part 1: Understanding the Edit Tab

### Accessing Edit Tools

**Location:** Edit tab on the ribbon

**Key Sections:**

1. **Features Group:**
   - Create: Add new features
   - Modify: Change existing feature shapes

2. **Selection Group:**
   - Select: Choose features to edit
   - Clear: Deselect all

3. **Manage Edits Group:**
   - Save: Save your changes
   - Discard: Cancel unsaved changes

4. **Tools Group:**
   - Contains Merge, Split, and other editing tools

### Starting an Edit Session

**Before You Can Edit:**
1. Layer must be added to the map
2. Layer must be editable (not from a service unless configured)
3. You must start an edit session

**To Start Editing:**
1. Click Edit tab
2. Tools and features become available
3. Edit tab stays active until you save or discard

**Important:** Always save your work frequently!

---

## Part 2: The Merge Tool

### What is Merge?

**Purpose:** Combine two or more features into a single feature

**When to Use:**
- Combining GPS track segments into one continuous trail
- Merging separate trail sections that are actually one route
- Consolidating overlapping features
- Cleaning data with unnecessary subdivisions

### How Merge Works

**Result:** Multiple selected features become one feature

**What Happens:**
- Geometries are combined
- One attribute record remains
- You choose which attributes to keep

### Using the Merge Tool

**Step-by-Step:**

1. **Select Features to Merge**
   - Edit tab → Select tool (or press 'C' key)
   - Click first feature
   - Hold SHIFT and click additional features
   - OR drag box around all features to merge
   - Selected features highlight in cyan

2. **Open Merge Tool**
   - Edit tab → Modify Features button
   - Search for "Merge" in Modify Features pane
   - Click Merge tool

3. **Choose Target Feature**
   - Merge dialog shows all selected features
   - Choose which feature's attributes to preserve
   - Click the feature that has the correct attributes
   - This feature will be the "survivor"

4. **Complete Merge**
   - Click Merge button
   - Selected features combine into one
   - Check result on map

5. **Save Edits**
   - Edit tab → Save button
   - Changes are permanent

### Merge Attributes Dialog

**Understanding the Dialog:**

When you merge, you'll see a table showing:
- All selected features (one per row)
- All attribute fields (columns)
- Values from each feature

**Choosing Attributes:**
- Features in red will be deleted
- Feature in green will survive
- Click row to make it the target
- You can edit any values before merging

**Best Practice:** Choose the feature with the most complete or accurate attributes as your target.

### Real-World Example: Merging GPS Trails

**Scenario:** You collected a trail using Garmin GPS, but the track has gaps due to signal loss.

**Problem:**
- GPS created 3 separate line features
- Need one continuous trail for measuring length
- Need single feature for grant application

**Solution:**
1. Select all 3 trail segments
2. Merge tool
3. Choose segment with best attributes
4. Merge
5. Result: One continuous trail

---

## Part 3: The Split Tool

### What is Split?

**Purpose:** Divide a single feature into two or more separate features

**When to Use:**
- Breaking a long trail into named segments
- Dividing a trail at dangerous crossings for analysis
- Separating different trail types on same route
- Creating segments between markers for grant application

### How Split Works

**Result:** One feature becomes multiple features

**Methods:**
1. **Split at specific points** - divide where you click
2. **Split by distance** - create evenly-spaced segments
3. **Split by percentage** - divide into proportional parts

### Using the Split Tool

**Method 1: Interactive Split (Most Common)**

**Step-by-Step:**

1. **Select Feature to Split**
   - Edit tab → Select tool
   - Click the line feature you want to split
   - Feature highlights in cyan

2. **Open Split Tool**
   - Edit tab → Modify Features
   - Search "Split"
   - Click Split tool

3. **Create Split Line**
   - Your cursor changes to crosshairs
   - Click to draw a line across the feature
   - Click where you want to cut
   - Double-click to finish split line
   - Feature splits where line crosses it

4. **Result**
   - Original feature is now 2+ separate features
   - Each has copy of original attributes
   - Each gets unique OBJECTID

5. **Save Edits**
   - Edit tab → Save

**Method 2: Split at Vertices**

If your feature has vertices (points along the line), you can split exactly at a vertex:

1. Select feature
2. Right-click directly on a vertex
3. Select "Split" from context menu
4. Feature splits at that point

**Method 3: Split by Distance**

For creating evenly-spaced segments:

1. Select feature
2. Modify Features → Split
3. In Split pane, click "Options"
4. Choose "Distance" or "Percentage"
5. Enter value
6. Click Split
7. Feature divides into equal segments

### Split Attributes

**What Happens to Attributes:**
- Each new feature gets a copy of all attributes
- Text fields: same value in all pieces
- Numeric fields: same value in all pieces
- **Shape_Length:** Automatically recalculates for each piece

**After Splitting:**
You'll need to update attributes to reflect the new features:
- Update names (e.g., "Main Trail - Segment 1", "Main Trail - Segment 2")
- Update segment-specific attributes
- Verify calculated fields

### Real-World Example: Splitting Trail Segments

**Scenario:** You have a 15-mile trail from Quinhagak to Goodnews Bay. For the grant application, you need to split it into segments between proposed marker locations.

**Problem:**
- One continuous trail
- Need segments between markers for cost estimation
- Each segment needs individual attributes

**Solution:**
1. Add proposed marker points to map
2. Select trail line
3. Use Split tool
4. Split at each marker location
5. Update attributes for each segment:
   - Segment name
   - Markers at each end
   - Individual length
   - Priority for marking

---

## Part 4: The Extend Tool

### What is Extend?

**Purpose:** Extend a line feature to meet another line feature

**When to Use:**
- Connecting GPS trails that have small gaps
- Extending trails to meet road networks
- Fixing GPS tracks that stopped short of destination
- Connecting trail segments for network analysis

### How Extend Works

**Result:** Selected line extends until it intersects the target line

**Requirements:**
- Both features must be line features
- Target line must be within reasonable distance
- Extension follows straight line from endpoint

### Using the Extend Tool

**Step-by-Step:**

1. **Identify Features**
   - Line to extend: The short feature
   - Target line: The feature to extend to

2. **Open Extend Tool**
   - Edit tab → Modify Features
   - Search "Extend or Trim"
   - Click Extend or Trim tool

3. **Set Extension Distance**
   - In Extend or Trim pane
   - Set "Extension distance" (how far to search)
   - Usually 10-100 meters depending on gap size

4. **Select Target Line**
   - Click "Select by feature" in pane
   - Click the line you want to extend TO
   - This is your target/reference

5. **Select Line to Extend**
   - Click the line you want to extend FROM
   - Tool extends line to target

6. **Review Result**
   - Line extends to meet target
   - Creates clean connection

7. **Save Edits**
   - Edit tab → Save

### Extend vs Trim

**Extend:** Makes line longer to reach another line

**Trim:** Makes line shorter by cutting at another line

Both use same tool with different results depending on geometry.

### Real-World Example: Connecting GPS Gaps

**Scenario:** GPS track data from Garmin has small gaps where signal was lost.

**Problem:**
- Trail segments are close but don't connect
- Gaps prevent measuring total trail length
- Network analysis won't work on disconnected trails

**Solution:**
1. Use Extend tool on each segment
2. Extend to connect with next segment
3. Verify alignment makes sense
4. Then use Merge to create single feature

---

## Part 5: Combining Tools - Trail Data Workflow

### Real-World Workflow: Cleaning GPS Trail Data

**Scenario:** You imported GPX files from multiple Garmin devices for SAR trail mapping. The data has issues common to GPS collection:
- Multiple track segments for same trail
- Small gaps from signal loss
- Trails extend beyond intended endpoints
- Need clean data for grant application

### Step-by-Step Workflow

**Step 1: Import and Review Data**
1. Import GPX to features (covered in Activity 9)
2. Add to map
3. Zoom to each trail
4. Identify problems:
   - Where are gaps?
   - Where are overlaps?
   - What needs to be combined?

**Step 2: Extend Features to Close Small Gaps**
1. Identify trail segments with small gaps (< 50m)
2. For each gap:
   - Select one segment
   - Extend tool
   - Target: adjacent segment
   - Extend to connect
3. Verify connection is correct path

**Step 3: Merge Connected Segments**
1. Select all segments of same trail
2. Merge tool
3. Choose feature with best attributes
4. Complete merge
5. Result: One continuous trail

**Step 4: Split at Logical Divisions**
1. If trail needs to be segmented:
   - Split at dangerous crossings
   - Split at marker locations
   - Split where trail type changes
2. Split tool at each division point

**Step 5: Update Attributes**
1. Open attribute table
2. For each trail/segment:
   - Update name
   - Add description
   - Verify attributes
3. Save edits

**Step 6: Calculate Geometry**
1. Add field: Length_Miles
2. Calculate geometry (covered in Lesson 13)
3. Verify lengths are correct

**Step 7: Final QA/QC**
1. Review each trail visually
2. Check attribute table completeness
3. Verify lengths make sense
4. Create map to review with SAR volunteers
5. Make final corrections

---

## Part 6: Edit Tools Best Practices

### Before You Edit

**1. Save Your Work First**
- Make backup copy of data
- Save project
- Work on copy, not original

**2. Plan Your Edits**
- What needs to be merged?
- Where should splits occur?
- What are you trying to achieve?

**3. Check Your Selection**
- Verify you selected correct features
- Wrong selection = wrong result
- Use attribute table to confirm selection

### During Editing

**1. Work Methodically**
- Complete one trail before moving to next
- Save after each major edit
- Use consistent approach

**2. Zoom In**
- Don't edit at small scale
- Zoom close to see detail
- Verify vertex alignment

**3. Use Attribute Table**
- Keep table open
- Track which features are edited
- Update attributes immediately

### After Editing

**1. Visual QA/QC**
- Pan through entire dataset
- Look for:
  - Gaps where shouldn't be
  - Overlaps
  - Odd angles or shapes

**2. Attribute QA/QC**
- Sort by each field
- Look for:
  - Blank required fields
  - Duplicate names
  - Inconsistent values

**3. Calculate Geometry**
- Update length or area fields
- Verify calculations are reasonable
- Check totals match expectations

---

## Part 7: Troubleshooting

### Merge Tool Issues

**Problem:** Merge option is grayed out
**Solution:**
- Must have 2+ features selected
- Features must be same geometry type (all lines or all polygons)
- Must be in edit session
- Layer must be editable

**Problem:** Wrong attributes after merge
**Solution:**
- Choose different target feature before merging
- Or manually edit attributes after merge

**Problem:** Merged feature looks wrong
**Solution:**
- Ctrl+Z to undo
- Verify you selected correct features
- Check features are actually connected/overlapping

### Split Tool Issues

**Problem:** Can't split feature
**Solution:**
- Only one feature can be selected
- Must be line or polygon (can't split points)
- Must be in edit session

**Problem:** Split line doesn't split feature
**Solution:**
- Split line must cross completely through feature
- Zoom in and try again
- Ensure split line intersects feature

**Problem:** Split created too many pieces
**Solution:**
- Undo (Ctrl+Z)
- Redraw split line to cross only where intended

### Extend Tool Issues

**Problem:** Extend doesn't work
**Solution:**
- Increase extension distance
- Verify target line is selected
- Check if gap is too large (may need to manually connect)

**Problem:** Extends to wrong feature
**Solution:**
- More specific target selection
- Temporarily hide other layers
- Manually edit vertex instead

---

## Part 8: Practice Exercises

### Exercise 1: Merge Trail Segments

**Setup:**
Create 3 separate line features that should be one trail:
1. Create new line layer: `Practice_Trails`
2. Draw 3 connected line segments
3. Give each different attributes

**Task:**
1. Select all 3 segments
2. Merge into one trail
3. Choose which attributes to keep
4. Verify result is single feature

**Verification:**
- Open attribute table - should show 1 feature
- Calculate geometry - should show total length

---

### Exercise 2: Split Trail by Segments

**Setup:**
Use the merged trail from Exercise 1

**Task:**
1. Split trail into 3 equal segments using distance method
2. Update attributes for each segment:
   - Segment 1, 2, 3
   - Different conditions
   - Different priority levels

**Verification:**
- Should have 3 features
- Each approximately same length
- Each with unique attributes

---

### Exercise 3: Extend to Close Gaps

**Setup:**
Create 2 line features with small gap between them

**Task:**
1. Use Extend tool to close gap
2. Connect one line to the other
3. Verify clean connection
4. Merge into single feature

**Verification:**
- Lines meet at endpoints
- No overlap
- Single continuous feature after merge

---

## Real-World Case Study: Quinhagak to Goodnews Trail

### Background

**Project:** SAR Trail Marking Grant Application

**Challenge:**
- GPS data from Garmin had inaccuracies
- Trail showed as multiple disconnected segments
- Some segments extended beyond actual trail
- Needed accurate length for grant application

### Process

**Step 1: Assessment**
- Imported GPX data
- Identified 7 separate track segments
- Noted 3 small gaps from signal loss
- Found 2 segments extended too far

**Step 2: Trim Excess**
- Used Edit vertices to shorten overextended segments
- Trimmed to match satellite imagery

**Step 3: Close Gaps**
- Extended segments to close 3 small gaps
- Verified alignment with imagery

**Step 4: Merge Trail**
- Selected all 7 segments
- Merged into single "Quinhagak to Goodnews Trail" feature
- Kept attributes from most complete segment

**Step 5: Calculate Length**
- Used Calculate Geometry tool (Lesson 13)
- Field: Length_Miles
- Result: Accurate measurement for grant application

### Result

**Before:**
- 7 disconnected segments
- Unable to measure total length
- Looked unprofessional

**After:**
- 1 continuous trail
- Accurate length in miles
- Professional data for grant
- Ready for application map

**Outcome:** Data used in successful grant application to Alaska DOT for trail marking funding.

---

## Summary

### Key Concepts

1. **Merge** combines multiple features into one
   - Use for GPS segments of same trail
   - Choose target feature for attributes
   - Creates single continuous feature

2. **Split** divides one feature into multiple
   - Use for creating segments
   - All pieces get copy of attributes
   - Update attributes after splitting

3. **Extend** lengthens lines to meet other lines
   - Use for closing small gaps
   - Connects near-miss features
   - Set appropriate extension distance

### Workflow Integration

These tools work together:
1. **Extend** to close gaps
2. **Merge** to combine into one
3. **Split** to divide into logical segments
4. **Calculate Geometry** to measure results

### Best Practices Review

- ✅ Always work on backup copies
- ✅ Save frequently
- ✅ Verify selection before editing
- ✅ Zoom in for accuracy
- ✅ Update attributes after edits
- ✅ QA/QC your results
- ✅ Document your process

---

## Additional Resources

### ArcGIS Pro Documentation
- [Merge Features](https://pro.arcgis.com/en/pro-app/latest/help/editing/merge-features.htm)
- [Split Features](https://pro.arcgis.com/en/pro-app/latest/help/editing/split-a-feature.htm)
- [Extend or Trim Features](https://pro.arcgis.com/en/pro-app/latest/help/editing/extend-or-trim-features.htm)
- [Edit Tab Overview](https://pro.arcgis.com/en/pro-app/latest/help/editing/the-edit-tab.htm)

### Related Lessons
- Lesson 5: Creating Features (digitizing basics)
- Lesson 11: Creating Layers (layer setup)
- Lesson 13: Attribute Fields and Calculating Geometry (measuring results)

### Video Tutorials
- [ArcGIS Pro Editing Workflows](https://www.esri.com/training/)
- Search: "ArcGIS Pro editing tools"

---

## Next Steps

After mastering these edit tools:
1. Practice on real GPS data
2. Clean trail datasets
3. Prepare data for analysis
4. Calculate accurate measurements (Lesson 13)
5. Create professional maps for grant applications

---

**Lesson Version:** 1.0
**Last Updated:** November 2025
**Module:** 4 - Spatial Analysis in ArcGIS Pro
**Location:** Quinhagak, Alaska
