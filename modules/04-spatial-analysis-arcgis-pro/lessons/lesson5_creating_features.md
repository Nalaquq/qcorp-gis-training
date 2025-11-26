# Lesson 5: Creating Features - Points, Lines, and Polygons

**Duration:** 90 minutes
**Difficulty:** Intermediate
**Prerequisites:** Lesson 3 (Data Management), Lesson 11 (Creating Layers)

---

## Overview

This lesson teaches you to create and digitize geographic features from georeferenced maps and imagery. Using a historical Quinhagak map, you'll trace the old FAA building, old sewer lagoon, and housing plots to preserve knowledge of historical community infrastructure.

---

## Learning Objectives

By the end of this lesson, you will be able to:

1. ✅ Start an edit session
2. ✅ Create point, line, and polygon features
3. ✅ Trace features from georeferenced maps
4. ✅ Edit feature vertices and shapes
5. ✅ Add attribute information
6. ✅ Save and verify edits

---

## Part 1: Starting an Edit Session

### Understanding Editing in ArcGIS Pro

**Edit Session:**
- Must be started to create or modify features
- Changes can be saved or discarded
- Undo/redo available

### Task 1.1: Start Editing

1. **Edit Tab:**
   - Click "Edit" tab on ribbon
   - Tools become available

2. **Create Features:**
   - Click "Create" button
   - Create Features pane opens

3. **Select Layer:**
   - Choose feature class to edit
   - Select tool (Point, Line, Polygon)

4. **Start Drawing:**
   - Click on map to create features

### Saving Edits

**Save Frequently!**
- Edit tab → Save button
- Ctrl+S
- Saves all changes permanently

**Discard Edits:**
- Edit tab → Discard button
- Cancels all unsaved changes

---

## Part 2: Creating Polygon Features

### Task 2.1: Trace Old FAA Building

**Setup:**
1. Add georeferenced Quinhagak map as basemap
2. Create polygon feature class: `Historical_Buildings`
3. Zoom to old FAA building location

**Digitizing Steps:**

1. **Start Edit Session:**
   - Edit tab → Create

2. **Select Feature Class:**
   - Click `Historical_Buildings` in Create Features pane
   - Select "Polygon" tool

3. **Trace Building Outline:**
   - Click each corner of building
   - Follow outline carefully
   - Double-click to finish polygon

4. **Add Attributes:**
   - Attributes pane appears automatically
   - Fill in:
     - Building_Name: "Old FAA Building"
     - Year_Built: Approximate year
     - Status: "Demolished" or "Removed"
     - Notes: Any additional information

5. **Save Edits:**
   - Edit tab → Save

**Tips:**
- Zoom in close for accuracy
- Use F2 key to finish feature
- Right-click for vertex options

### Task 2.2: Map Old Sewer Lagoon

**Same Process:**
1. Create new polygon
2. Trace lagoon outline from historical map
3. Fill attributes:
   - Feature_Name: "Old Sewer Lagoon"
   - Feature_Type: "Wastewater Treatment"
   - Status: "Relocated"
   - Notes: Environmental considerations

### Task 2.3: Outline Housing Plots

**Multiple Features:**
1. Create multiple polygons
2. Each housing plot = one feature
3. Number or name each plot
4. Document historical use

---

## Part 3: Creating Line Features

### When to Use Lines

**Examples:**
- Roads and trails
- Rivers and streams
- Utility lines
- Fence lines
- Historical routes

### Task 3.1: Create Line Feature

1. **Create Line Feature Class:**
   - Example: `Historical_Roads`

2. **Select Polyline Tool:**
   - Create Features → Select layer
   - Choose "Line" tool

3. **Draw Line:**
   - Click to start
   - Click at each vertex
   - Follow feature path
   - Double-click to end

4. **Add Attributes:**
   - Road_Name
   - Road_Type
   - Condition
   - Notes

---

## Part 4: Creating Point Features

### When to Use Points

**Examples:**
- Building locations
- Observation points
- Sample sites
- Markers or signs
- Wells or infrastructure

### Task 4.1: Create Point Feature

1. **Create Point Feature Class:**
   - Example: `Historical_Sites`

2. **Select Point Tool:**
   - Create Features → Select layer
   - Choose "Point" tool

3. **Place Point:**
   - Click location on map
   - Point created

4. **Add Attributes:**
   - Site_Name
   - Site_Type
   - Description
   - Date_Documented

---

## Part 5: Editing Existing Features

### Modify Features Tool

**Access:**
- Edit tab → Modify Features button
- Shows editing tools

**Common Edit Operations:**

**Move:**
- Select feature
- Modify → Move tool
- Drag to new location

**Reshape:**
- Modify → Edit Vertices tool
- Add, delete, or move vertices

**Split:**
- See Lesson 12

**Merge:**
- See Lesson 12

---

## Part 6: Best Practices for Digitizing

### Accuracy Tips

1. **Zoom In:**
   - Get close to feature
   - Better accuracy
   - Easier to see detail

2. **Use Snapping:**
   - Edit tab → Snapping dropdown
   - Enable snapping to features
   - Vertices snap together

3. **Follow Imagery:**
   - Trace carefully
   - Use highest resolution imagery
   - Check alignment

4. **Check Topology:**
   - Polygons should close
   - No gaps or overlaps (usually)
   - Validate geometry

### Attribute Best Practices

1. **Complete Information:**
   - Fill all relevant fields
   - Don't leave important fields null

2. **Consistent Format:**
   - Same capitalization
   - Same date format
   - Standardized categories

3. **Source Documentation:**
   - Note where information came from
   - Date of digitizing
   - Who created it

---

## Part 7: Practical Exercise

### Exercise: Digitize Historical Features

**Goal:** Create complete historical feature dataset from georeferenced map

**Tasks:**

1. **Create Three Feature Classes:**
   - `Historical_Buildings` (polygon)
   - `Historical_Infrastructure` (polygon) 
   - `Historical_Sites` (point)

2. **Digitize Features:**
   - Trace at least 3 polygons
   - Create at least 2 points
   - Add complete attributes

3. **Quality Check:**
   - All polygons close properly
   - All attributes filled
   - Features in correct locations

4. **Save:**
   - Save edits
   - Save project

**Deliverable:**
- Geodatabase with historical features
- Complete attribute information
- Properly digitized geometries

---

## Summary

### Key Concepts

1. **Edit Session:** Must start to create/modify
2. **Create Tools:** Point, Line, Polygon
3. **Tracing:** Follow basemap/imagery carefully
4. **Attributes:** Complete information for each feature
5. **Save Often:** Don't lose work

### Workflow

1. Start edit session (Edit tab → Create)
2. Select feature class and tool
3. Digitize feature on map
4. Fill attributes
5. Save edits

---

**Lesson Version:** 1.0  
**Last Updated:** November 2025  
**Module:** 4 - Spatial Analysis in ArcGIS Pro
