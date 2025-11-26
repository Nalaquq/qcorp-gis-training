# Lesson 6: Buffer Analysis

**Duration:** 60 minutes
**Difficulty:** Intermediate
**Prerequisites:** Lesson 5 (Creating Features)

---

## Overview

Buffers create zones around features at specified distances. This lesson teaches buffer creation, dissolving overlapping buffers, and using pairwise intersect to find where buffer zones overlap - essential for proximity analysis and planning.

---

## Learning Objectives

By the end of this lesson, you will be able to:

1. ✅ Create buffers around point, line, and polygon features
2. ✅ Understand buffer distance units
3. ✅ Dissolve overlapping buffers
4. ✅ Use pairwise intersect between buffer polygons
5. ✅ Apply buffers for community planning questions

---

## Part 1: Understanding Buffers

### What is a Buffer?

**Definition:** A polygon representing area within specified distance of a feature

**Examples:**
- 100m buffer around historical building (impact zone)
- 1km buffer around community (service area)
- 50m buffer around river (riparian zone)

### When to Use Buffers

**Common Applications:**
- Proximity analysis (what's near what?)
- Impact zones
- Service areas
- Safety zones
- Planning regulations

---

## Part 2: Creating Buffers

### Task 2.1: Buffer Tool

**Access:**
1. Analysis tab → Tools
2. Search: "Buffer"
3. Open "Buffer" tool (Analysis Tools)

**Parameters:**

**Input Features:**
- Layer to buffer
- Example: Historical_Buildings from Lesson 5

**Output Feature Class:**
- Name and location for buffer polygons
- Example: `Buildings_Buffer_100m`

**Distance:**
- Linear Unit: Enter distance
- Example: 100 Meters
- Options: Meters, Kilometers, Miles, Feet

**Side Type (optional):**
- Full (both sides) - default
- Left or Right (for lines)

**End Type (for lines):**
- Round (curved ends) - default
- Flat (straight across)

**Dissolve Type:**
- None: Keep separate buffers
- All: Merge all buffers into one
- List: Merge by attribute

**Run Tool:**
- Click Run
- Buffer layer added to map

---

## Part 3: Multiple Buffer Distances

### Task 3.1: Create Multiple Ring Buffers

**Tool:** Multiple Ring Buffer

1. **Search "Multiple Ring Buffer"**

2. **Input Features:**
   - Your point or polygon layer

3. **Output:**
   - Name buffer layer

4. **Distances:**
   - Enter multiple values
   - Example: 100 200 300 (meters)
   - Creates concentric buffers

5. **Result:**
   - Multiple rings at different distances
   - Useful for graduated zones

---

## Part 4: Dissolving Buffers

### Why Dissolve?

**Problem:** Individual buffers may overlap

**Solution:** Dissolve combines overlapping polygons into single feature

### Task 4.1: Buffer with Dissolve

**Method 1: During Buffer Creation**
- In Buffer tool
- Dissolve Type: "All"
- Creates single merged buffer

**Method 2: Separate Dissolve**

1. **Create buffers first** (without dissolve)

2. **Run Dissolve Tool:**
   - Analysis tab → Tools
   - Search: "Dissolve"
   - Input: Buffer layer
   - Output: Dissolved_Buffers
   - Dissolve Fields: (leave empty for all)
   - Run

3. **Result:**
   - Overlapping areas merged
   - Single or fewer polygons

---

## Part 5: Pairwise Intersect

### Understanding Intersect

**Purpose:** Find where two buffer zones overlap

**Example:**
- Buffer A: 100m around FAA building
- Buffer B: 100m around sewer lagoon
- Intersect: Where both buffers overlap

### Task 5.1: Pairwise Intersect Between Buffers

**Scenario:** Find overlap between two buffer zones

**Steps:**

1. **Create Two Buffer Layers:**
   - Buffer1: Historical_Buildings (100m)
   - Buffer2: Infrastructure_Sites (100m)

2. **Run Pairwise Intersect:**
   - Analysis tab → Tools
   - Search: "Pairwise Intersect"
   - Input Features: Buffer1, Buffer2
   - Output: `Buffer_Overlap`
   - Run

3. **Result:**
   - Polygons showing only overlap areas
   - Attributes from both inputs
   - Shows compound impact zones

**Applications:**
- Compound impact areas
- Joint service zones
- Overlapping influence areas

---

## Part 6: Practical Applications

### Example: Infrastructure Impact Analysis

**Question:** Which parcels are within 200m of historical contamination sites?

**Workflow:**

1. **Create Buffer:**
   - Input: Historical contamination polygons
   - Distance: 200 meters
   - Dissolve: All

2. **Spatial Join or Intersect:**
   - Find parcels within buffer
   - Tag affected parcels

3. **Analysis:**
   - Count affected parcels
   - Calculate affected area
   - Identify owners to notify

---

## Part 7: Practice Exercise

### Exercise: Historical Sites Impact Analysis

**Goal:** Analyze impact zones around historical features from Lesson 5

**Tasks:**

1. **Create 100m Buffers:**
   - Buffer Historical_Buildings
   - Output: `Buildings_Buffer_100m`

2. **Create 200m Buffers:**
   - Same buildings, 200m distance
   - Output: `Buildings_Buffer_200m`

3. **Dissolve Buffers:**
   - Dissolve 100m buffers
   - Result: Single merged zone

4. **Pairwise Intersect:**
   - If you have multiple buffer layers
   - Find overlap zones
   - Analyze compound impacts

5. **Analysis Questions:**
   - How much area in 100m buffer?
   - How many parcels affected?
   - Where do buffers overlap?

**Deliverable:**
- Buffer layers at multiple distances
- Dissolved buffer showing total impact zone
- Intersect layer showing overlaps (if applicable)
- Summary of findings

---

## Summary

### Key Concepts

1. **Buffers:** Zones at specified distance from features
2. **Distance Units:** Choose appropriate (meters, miles, etc.)
3. **Dissolve:** Merge overlapping buffers
4. **Pairwise Intersect:** Find overlap between buffer zones
5. **Applications:** Proximity, impact, service area analysis

### Tools Used

- **Buffer:** Create distance zones
- **Multiple Ring Buffer:** Concentric zones
- **Dissolve:** Merge overlaps
- **Pairwise Intersect:** Find overlaps

### Workflow

1. Identify features to buffer
2. Determine appropriate distance
3. Run Buffer tool
4. Dissolve if needed
5. Intersect with other buffers or features
6. Analyze results

---

**Lesson Version:** 1.0  
**Last Updated:** November 2025  
**Module:** 4 - Spatial Analysis in ArcGIS Pro
