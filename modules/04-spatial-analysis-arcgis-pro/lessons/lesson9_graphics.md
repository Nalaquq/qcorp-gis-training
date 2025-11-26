# Lesson 9: Graphics and Annotation

**Duration:** 30 minutes
**Difficulty:** Beginner
**Prerequisites:** Basic ArcGIS Pro navigation

---

## Overview

Graphics and text annotations help communicate information on your maps. This lesson teaches you to add text, shapes, and annotations directly to maps and layouts, particularly useful for labeling georeferenced maps and adding context to projects.

---

## Learning Objectives

By the end of this lesson, you will be able to:

1. ✅ Add text to maps
2. ✅ Create graphics layers
3. ✅ Annotate georeferenced maps
4. ✅ Add arrows, shapes, and other graphics
5. ✅ Format and style text elements

---

## Part 1: Understanding Graphics

### Graphics vs Features

**Graphics:**
- Drawing elements on map
- Not stored in geodatabase
- Part of map or layout
- Quick annotations

**Features:**
- Actual GIS data
- Stored in feature class
- Has attributes
- Can be analyzed

**When to Use Graphics:**
- Temporary labels
- Map annotations
- Callouts and arrows
- Quick markup

---

## Part 2: Adding Text to Maps

### Task 2.1: Insert Text

**Access:**
1. Insert tab on ribbon
2. Graphics group
3. Click "Text" button

**Add Text:**
1. Click "Text"
2. Click on map where you want text
3. Type your text
4. Press Enter

**Format Text:**
1. Select text graphic
2. Format tab appears
3. Options:
   - Font, size, color
   - Bold, italic, underline
   - Alignment
   - Halo (outline for readability)
   - Background

### Common Uses

**On Georeferenced Maps:**
- Label features visible in historical map
- Mark points of interest
- Add explanatory notes
- Document observations

**On Analysis Maps:**
- Add title or subtitle
- Note date or data source
- Explain methodology
- Highlight key findings

---

## Part 3: Creating Graphics Layer

### What is a Graphics Layer?

**Purpose:**
- Organizes graphics
- Each map can have one or more graphics layers
- Appears in Contents pane
- Can turn on/off visibility

### Task 3.1: Work with Graphics Layer

**Default Graphics Layer:**
- Automatically created when you add graphics
- Named "New Graphics Layer"

**Rename:**
1. Right-click graphics layer in Contents
2. Properties
3. General tab
4. Name: "Annotations" or descriptive name

**Multiple Graphics Layers:**
- Organize different types of graphics
- Insert tab → New Graphics Layer
- Example: "Labels", "Arrows", "Boundaries"

**Control Visibility:**
- Check/uncheck in Contents
- Show/hide groups of graphics

---

## Part 4: Adding Shapes

### Available Shapes

**Access:** Insert tab → Graphics group

**Options:**
- Rectangle
- Circle / Ellipse
- Polygon (freeform)
- Line
- Arrow
- Cloud callout

### Task 4.1: Add Shapes

**Example: Add Arrow**

1. **Insert tab → Arrow**
2. **Click start point**
3. **Click end point**
4. **Arrow appears**

**Format Arrow:**
- Select arrow
- Format tab
- Line color, width
- Arrow head style
- Fill (if applicable)

**Use Cases:**
- Point to features
- Show direction
- Connect related items
- Highlight areas

---

## Part 5: Annotating Georeferenced Maps

### Common Workflow

**Scenario:** Historical Quinhagak map needs labels

**Steps:**

1. **Add Georeferenced Map:**
   - Load historical map as raster

2. **Create Graphics Layer:**
   - Insert → New Graphics Layer
   - Name: "Historical Labels"

3. **Add Text Labels:**
   - Insert → Text
   - Click location of feature
   - Type label: "Old FAA Building"
   - Format text for readability

4. **Add Arrows if Needed:**
   - Insert → Arrow
   - Point to specific features

5. **Add Legend or Key:**
   - Text box explaining symbols
   - Context for readers

**Tips:**
- Use halo on text for readability
- Consistent font/size
- Don't overcrowd
- Place text near features

---

## Part 6: Converting Graphics to Features

### When to Convert

**If graphics need to be:**
- Permanent data
- Shared across projects
- Analyzed spatially
- Stored in geodatabase

### Task 6.1: Convert Graphics to Features

**Access:**
- Right-click graphics layer
- Data → Convert Graphics to Features

**Parameters:**
- Output feature class
- Choose geometry type

**Result:**
- Graphics become real features
- Stored in geodatabase
- Can be edited and analyzed

---

## Part 7: Best Practices

### Effective Annotation

**Do:**
- Use clear, readable fonts
- Add halos for text on busy backgrounds
- Be concise
- Organize with graphics layers
- Consistent styling

**Don't:**
- Overcrowd map with too many labels
- Use tiny font sizes
- Place text over important features
- Mix too many font styles

### Organization

**Create Separate Layers for:**
- Labels
- Arrows/callouts
- Boundaries or highlights
- Draft notes (temporary)

**Benefits:**
- Easy to show/hide
- Better organization
- Control what goes in final map

---

## Part 8: Graphics in Layouts

### Graphics on Map vs Layout

**Map View Graphics:**
- Tied to geography
- Move when you pan/zoom
- Part of map

**Layout Graphics:**
- Fixed position on page
- Titles, legends, scale bars
- Don't move with map

**Using Both:**
- Map graphics: Annotate geographic features
- Layout graphics: Title, credits, notes

---

## Part 9: Practice Exercise

### Exercise: Annotate Historical Map

**Goal:** Add helpful annotations to georeferenced Quinhagak map

**Tasks:**

1. **Add Historical Map:**
   - Load georeferenced historical map

2. **Create Graphics Layer:**
   - Name: "Historical_Annotations"

3. **Add Text Labels:**
   - Label at least 5 features visible in map
   - Examples: Buildings, roads, landmarks
   - Use readable font and halo

4. **Add Arrows:**
   - Point to at least 2 small features
   - Help viewers find them

5. **Add Legend/Key:**
   - Text box explaining what map shows
   - Date of map
   - Source information

6. **Format Consistently:**
   - Same font/size for similar labels
   - Consistent arrow style
   - Professional appearance

**Deliverable:**
- Annotated historical map
- Clear, readable labels
- Organized graphics layer
- Professional presentation

---

## Summary

### Key Concepts

1. **Graphics:** Drawing elements, not features
2. **Text:** Add labels and annotations
3. **Shapes:** Arrows, rectangles, circles, etc.
4. **Graphics Layers:** Organize graphics
5. **Formatting:** Font, color, halo, style

### Common Tasks

- Add text: Insert tab → Text
- Add arrow: Insert tab → Arrow
- Format: Select graphic → Format tab
- Organize: Create/rename graphics layers

### Workflow

1. Decide what to annotate
2. Create graphics layer
3. Add text and shapes
4. Format for readability
5. Organize and review

---

**Lesson Version:** 1.0  
**Last Updated:** November 2025  
**Module:** 4 - Spatial Analysis in ArcGIS Pro
