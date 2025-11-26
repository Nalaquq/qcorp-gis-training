# Lesson 4: Symbology and Visualization

**Duration:** 45 minutes
**Difficulty:** Beginner-Intermediate
**Prerequisites:** Lesson 2 (Adding Content), Lesson 3 (Data Management)

---

## Overview

Symbology is how you style your map layers to make them meaningful and visually appealing. This lesson teaches you how to adjust colors, symbols, and transparency to create readable, professional maps using Quinhagak Parcels data as an example.

---

## Learning Objectives

By the end of this lesson, you will be able to:

1. ✅ Adjust layer symbology in ArcGIS Pro
2. ✅ Choose appropriate color palettes for data visualization
3. ✅ Use transparency to see multiple layers
4. ✅ Create professional-looking, readable maps
5. ✅ Apply symbology based on attribute values

---

## Part 1: Accessing Symbology Controls

### Opening the Symbology Pane

**Method 1: Right-click Layer**
1. Right-click layer in Contents pane
2. Select "Symbology"
3. Symbology pane opens on right

**Method 2: Appearance Tab**
1. Select layer in Contents
2. Click "Appearance" tab on ribbon
3. Click "Symbology" button

**Symbology Pane:**
- Shows current symbol
- Symbology type dropdown
- Color, size, and style options

---

## Part 2: Single Symbol Symbology

### When to Use

**Best for:**
- All features represent same thing
- Focus on location, not attributes
- Simple reference layers

**Example:** All parcels same color

### Task 2.1: Apply Single Symbol

1. **Add Quinhagak Parcels Layer**
   - From AGOL or local geodatabase

2. **Open Symbology:**
   - Right-click layer → Symbology

3. **Select "Single Symbol":**
   - Dropdown at top
   - Choose "Single Symbol"

4. **Choose Color:**
   - Click color square
   - Select from palette
   - Or enter RGB values

5. **Adjust Outline:**
   - Outline color
   - Outline width (0.5-1 pt typical)

6. **Apply:**
   - Changes show immediately
   - Close pane when satisfied

---

## Part 3: Using Color Palettes

### Esri Color Palette Resource

**Resource from Training:**
https://cdn.arcgis.com/home/item.html?id=4b2af229785e46baa31c40fadd91fcc3

This provides professional color schemes for mapping.

### Choosing Good Colors

**Considerations:**

1. **Contrast:**
   - Layer vs background
   - Adjacent features distinguishable

2. **Accessibility:**
   - Colorblind-friendly
   - Avoid red-green combinations alone
   - Use patterns or labels too

3. **Meaning:**
   - Intuitive colors (water = blue, vegetation = green)
   - Consistent across related maps

4. **Professional:**
   - Not too bright/garish
   - Harmonious palette
   - Appropriate for audience

### Task 3.1: Apply Color Palette to Parcels

1. **Unique Values Symbology:**
   - Symbology pane → "Unique Values"
   - Field: Choose attribute (e.g., Land_Use, Owner)

2. **Color Scheme:**
   - Click "Color scheme" dropdown
   - Browse available schemes
   - Choose one appropriate for data

3. **Customize:**
   - Click individual symbols to adjust
   - Change colors, sizes, outlines

4. **Result:**
   - Each unique value has different color
   - Legend shows all categories
   - Easy to interpret map

---

## Part 4: Transparency

### Why Use Transparency?

**Benefits:**
- See basemap through features
- Layer multiple datasets
- Show overlapping areas
- Create visual hierarchy

### Task 4.1: Adjust Layer Transparency

**Method 1: Appearance Tab**
1. Select layer in Contents
2. Appearance tab on ribbon
3. "Transparency" slider
4. Adjust: 0% (opaque) to 100% (invisible)
5. Typical: 30-50% for parcels

**Method 2: Layer Properties**
1. Right-click layer → Properties
2. Display tab
3. Layer transparency slider
4. OK to apply

**Best Practices:**
- Basemap/imagery: 0% (opaque)
- Reference polygons: 40-60%
- Highlight layers: 0-30%
- Background context: 60-80%

---

## Part 5: Graduated Colors and Symbols

### When to Use

**Graduated Colors:**
- Showing numeric ranges
- Population density
- Parcel values
- Elevation

**Example:** Parcels colored by assessed value

### Task 5.1: Apply Graduated Colors

1. **Symbology → "Graduated Colors"**

2. **Select Field:**
   - Choose numeric field
   - Example: Parcel_Value, Area

3. **Classification Method:**
   - Natural Breaks (Jenks) - recommended
   - Equal Interval
   - Quantile
   - Manual

4. **Number of Classes:**
   - Typically 4-7
   - More = harder to distinguish

5. **Color Scheme:**
   - Sequential: light to dark (one color)
   - Diverging: two colors (shows above/below)

6. **Normalize (Optional):**
   - Divide by area, population, etc.
   - Shows density rather than totals

---

## Part 6: Labels

### Adding Labels

**Purpose:**
- Identify features
- Show attribute values
- Aid navigation

### Task 6.1: Enable Labels

1. **Right-click Layer:**
   - Select "Label"
   - Labels appear

2. **Configure Labels:**
   - Right-click layer → Labeling Properties
   - Text tab:
     - Field: Choose attribute
     - Font: Size, style, color
   - Symbol tab:
     - Halo for readability
     - Background if needed
   - Position tab:
     - Placement rules

3. **Label Options:**
   - Label only visible features
   - Remove duplicates
   - Scale-dependent (show only when zoomed in)

---

## Part 7: Practical Exercise - Quinhagak Parcels

### Exercise: Style Parcels Map

**Goal:** Create readable parcel map with professional symbology

**Tasks:**

1. **Add Quinhagak Parcels**
   - From AGOL or geodatabase

2. **Apply Color Scheme:**
   - If has Land_Use: Unique Values by Land_Use
   - If has values: Graduated Colors by Parcel_Value
   - Use color palette from Esri resource

3. **Adjust Transparency:**
   - Set to 40-50%
   - Should see satellite basemap through parcels

4. **Add Labels:**
   - Label by Parcel_ID or Owner
   - Add halo for readability
   - Scale-dependent: Show when zoomed in

5. **Final Touches:**
   - Outline color: Dark gray or black
   - Outline width: 0.5 pt
   - Professional appearance

**Deliverable:**
- Styled parcels map
- Easy to read
- Basemap visible
- Professional colors

---

## Part 8: Saving Layer Files

### Why Save Layer Files?

**Benefits:**
- Reuse symbology
- Apply to new data
- Share styling with team
- Maintain consistency

### Save Layer File

1. **Right-click Styled Layer:**
   - Select "Sharing" → "Save As Layer File"

2. **Save Location:**
   - Project folder or shared location
   - Name: `Quinhagak_Parcels_Style.lyrx`

3. **Apply Later:**
   - Drag .lyrx onto map
   - Or right-click layer → Apply Symbology from Layer

---

## Summary

### Key Concepts

1. **Single Symbol:** All features same style
2. **Unique Values:** Different colors for categories
3. **Graduated Colors:** Numeric ranges with color gradients
4. **Transparency:** See multiple layers, show basemap
5. **Color Palettes:** Professional, accessible colors
6. **Labels:** Identify features

### Best Practices

- Choose colors thoughtfully (contrast, accessibility)
- Use transparency to see basemap (30-50% typical)
- Label important features
- Save layer files for reuse
- Keep it professional and readable

---

**Lesson Version:** 1.0  
**Last Updated:** November 2025  
**Module:** 4 - Spatial Analysis in ArcGIS Pro
