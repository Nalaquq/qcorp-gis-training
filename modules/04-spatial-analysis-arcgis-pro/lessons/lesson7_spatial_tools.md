# Lesson 7: Advanced Spatial Analysis Tools

**Duration:** 90 minutes
**Difficulty:** Intermediate-Advanced
**Prerequisites:** Lesson 6 (Buffers), understanding of attribute tables

---

## Overview

This lesson covers essential geoprocessing tools for spatial analysis: Merge, Spatial Join, Dissolve, Clip, Erase, and Intersect. You'll learn when to use each tool and how to apply them to answer real-world questions about your community data.

---

## Learning Objectives

By the end of this lesson, you will be able to:

1. ✅ Merge multiple feature classes into one
2. ✅ Use Spatial Join to transfer attributes based on location
3. ✅ Dissolve features by attribute values
4. ✅ Clip data to a study area
5. ✅ Erase areas from analysis
6. ✅ Use Intersect to find overlapping areas
7. ✅ Choose the appropriate tool for each analysis question

---

## Part 1: Merge Tool

### What is Merge?

**Purpose:** Combine multiple feature classes of same geometry type into one

**Example:**
- Merge Road_Segments_North + Road_Segments_South = All_Roads
- Combine data from different sources
- Consolidate separate datasets

**Note:** Different from "Merge" in Edit tab (Lesson 12)
- Geoprocessing Merge: Combines entire feature classes
- Edit Merge: Combines selected features within layer

### Task 1.1: Merge Feature Classes

**Access:**
- Analysis tab → Tools
- Search: "Merge"

**Parameters:**

**Input Datasets:**
- Add multiple feature classes
- Must be same geometry type (all points, all lines, or all polygons)
- Example: Roads_East, Roads_West, Roads_Central

**Output Dataset:**
- Name and location
- Example: `All_Quinhagak_Roads`

**Field Map (optional):**
- How to handle different field names
- Match similar fields
- Drop unused fields

**Run:**
- All features combined into single output

---

## Part 2: Spatial Join

### What is Spatial Join?

**Purpose:** Transfer attributes from one layer to another based on spatial relationship

**Example:**
- Parcels layer + Community_Facilities layer
- Result: Parcels with attributes showing nearest facility

**Spatial Relationships:**
- Intersect: Features overlap
- Within: Feature completely inside
- Contains: Feature completely contains
- Closest: Nearest feature

### Task 2.1: Spatial Join

**Access:**
- Analysis tab → Tools
- Search: "Spatial Join"

**Parameters:**

**Target Features:**
- Layer receiving new attributes
- Example: Parcels

**Join Features:**
- Layer providing attributes
- Example: Facilities

**Output:**
- New feature class with combined attributes

**Join Operation:**
- One to one: Each target keeps one record
- One to many: Multiple records if multiple matches

**Match Option:**
- Intersect (default)
- Within distance
- Closest
- Etc.

**Run:**
- Output has geometry from target
- Attributes from both target and join features

**Use Case:**
- Which parcels are within 100m of river?
- Assign each building to nearest service area
- Tag features by zone they fall in

---

## Part 3: Dissolve Tool

### What is Dissolve?

**Purpose:** Combine adjacent features with same attribute value

**Example:**
- Parcels by owner: Merge all parcels belonging to same owner
- Land use: Combine adjacent parcels of same use type
- Administrative: Merge features by district/region

### Task 3.1: Dissolve by Attribute

**Access:**
- Analysis tab → Tools
- Search: "Dissolve"

**Parameters:**

**Input Features:**
- Layer to dissolve
- Example: Land_Parcels

**Output:**
- Dissolved feature class

**Dissolve Fields:**
- Attribute(s) to group by
- Example: Owner_Name, Land_Use
- Features with same value merge

**Statistics Fields (optional):**
- Calculate stats during dissolve
- SUM: Total area or count
- MEAN: Average value
- etc.

**Multi-part features:**
- Allow if non-adjacent features have same attribute
- Creates single feature with multiple parts

**Run:**
- Adjacent features with matching attributes merge

---

## Part 4: Clip Tool

### What is Clip?

**Purpose:** Extract data to study area boundary (like cookie cutter)

**Example:**
- Clip statewide roads to Quinhagak boundary
- Extract parcels within planning area
- Cut data to watershed or region

### Task 4.1: Clip to Study Area

**Access:**
- Analysis tab → Tools
- Search: "Clip"

**Parameters:**

**Input Features:**
- Layer to be clipped
- Example: Alaska_Rivers

**Clip Features:**
- Boundary polygon
- Example: Quinhagak_Boundary

**Output:**
- Clipped result
- Example: Quinhagak_Rivers

**Run:**
- Only features within clip boundary remain
- Features split at boundary
- Reduces dataset to area of interest

**Use Case:**
- Focus analysis on specific area
- Reduce data size
- Prepare data for sharing (only relevant area)

---

## Part 5: Erase Tool

### What is Erase?

**Purpose:** Remove areas from analysis (opposite of clip)

**Example:**
- Remove water bodies from land use analysis
- Exclude protected areas from development planning
- Remove already-developed parcels from available land

### Task 5.1: Erase Features

**Access:**
- Analysis tab → Tools
- Search: "Erase"

**Parameters:**

**Input Features:**
- Layer to erase from
- Example: All_Land_Parcels

**Erase Features:**
- Areas to remove
- Example: Water_Bodies

**Output:**
- Result with erased areas removed

**Run:**
- Areas matching erase features are removed
- Leaves "holes" where erase features were

**Use Case:**
- Remove restricted areas from planning
- Exclude water from terrestrial analysis
- Remove completed parcels from available inventory

---

## Part 6: Intersect Tool

### What is Intersect?

**Purpose:** Find where multiple layers overlap, keep only overlapping parts

**Example:**
- Parcels + Flood_Zone = Parcels_In_Flood_Zone
- Habitat + Protected_Areas = Protected_Habitat
- Combines attributes from all inputs

### Task 6.1: Intersect Multiple Layers

**Access:**
- Analysis tab → Tools
- Search: "Pairwise Intersect" (recommended) or "Intersect"

**Parameters:**

**Input Features:**
- Add 2+ feature classes
- Example: Parcels, Flood_Zones, Soil_Types

**Output:**
- Intersected result
- Only areas where ALL inputs overlap

**Run:**
- Output has geometry where all layers overlap
- Attributes from all input layers

**Pairwise Intersect vs Intersect:**
- Pairwise: Better performance, processes in pairs
- Standard Intersect: Processes all at once
- Use Pairwise for better speed

**Use Case:**
- Find parcels in both flood zone AND wetland
- Identify areas meeting multiple criteria
- Complex site selection

---

## Part 7: Decision Guide - Which Tool to Use?

### Quick Reference

| Goal | Tool | Example |
|------|------|---------|
| Combine separate datasets | **Merge** | Merge road segments from different areas |
| Transfer attributes by location | **Spatial Join** | Add zone name to each parcel |
| Combine features with same attribute | **Dissolve** | Merge parcels by owner |
| Extract data to area | **Clip** | Get roads within village boundary |
| Remove areas from data | **Erase** | Remove water bodies from land analysis |
| Find overlapping areas | **Intersect** | Parcels in both flood zone and wetland |
| Create buffer zones | **Buffer** (Lesson 6) | 100m around facilities |

---

## Part 8: Practical Exercise

### Exercise: Comprehensive Spatial Analysis

**Scenario:** Analyze parcels for potential community garden site

**Requirements:**
- Within village boundary
- Not in flood zone
- Within 500m of residential area
- Not on existing developed parcels
- Soil type suitable for gardening

**Workflow:**

1. **Clip Parcels:**
   - Clip all parcels to village boundary
   - Tool: Clip
   - Focus on relevant area

2. **Buffer Residential:**
   - Create 500m buffer around residential zones
   - Tool: Buffer
   - Shows service area

3. **Erase Developed:**
   - Remove already-developed parcels
   - Tool: Erase
   - Leaves undeveloped land

4. **Intersect Suitable Areas:**
   - Intersect: Buffered area + Good soil + Available parcels
   - Tool: Pairwise Intersect
   - Result: Parcels meeting all criteria

5. **Erase Flood Zones:**
   - Remove flood-prone areas
   - Tool: Erase
   - Final safe, suitable parcels

6. **Spatial Join Site Info:**
   - Join nearby facility info to candidates
   - Tool: Spatial Join
   - Adds context for decision-making

**Deliverable:**
- Final layer of suitable parcels
- Attribute table showing all criteria
- Map showing results
- Count of candidate sites

---

## Summary

### Tools Covered

1. **Merge:** Combine feature classes
2. **Spatial Join:** Transfer attributes by location
3. **Dissolve:** Combine by attribute
4. **Clip:** Extract to study area
5. **Erase:** Remove areas
6. **Intersect:** Find overlaps

### Key Concepts

- Each tool serves specific purpose
- Can chain tools together for complex analysis
- Order matters in workflow
- Understand your question to choose right tool

### Workflow Tips

1. Plan analysis steps before starting
2. Work on copies, keep originals
3. Name outputs clearly
4. Check intermediate results
5. Document your process

---

**Lesson Version:** 1.0  
**Last Updated:** November 2025  
**Module:** 4 - Spatial Analysis in ArcGIS Pro
