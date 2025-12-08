# Activity 6: Creating a Professional SAR Trail Marking Grant Map

**Duration:** 120 minutes
**Difficulty:** Intermediate-Advanced
**Prerequisites:** Module 4 Activity 10 (SAR Trail Marking Grant), Module 5 Lessons 1-7, basic cartography knowledge

---

## Overview

Creating a professional map for a grant application requires more than just adding data to a layout—it demands careful attention to cartographic design, visual hierarchy, and clarity. This activity walks through the detailed process of creating the SAR Trail Marking Grant map, demonstrating advanced cartographic techniques that transform GIS data into a compelling, professional document.

You'll learn how to create inset maps, adjust symbology for optimal visibility, use advanced label settings, and apply professional design principles to create a grant-ready map that effectively communicates your project's value.

**Example Map:**

![SAR Trail Marking Grant Map](../../../assets/images/adotfinalmap.jpg)
*Professional grant application map showing snowmachine trails, dangerous intersections, and halfway houses. Map prepared by Patrick Jones and Byron Phillips, November 2025.*

---

## Learning Objectives

By the end of this activity, you will be able to:

1. ✅ Create professional inset maps with extent indicators
2. ✅ Adjust map elements (text, scale bars, north arrows) for visibility
3. ✅ Apply advanced symbology for clear feature representation
4. ✅ Configure advanced label settings for professional appearance
5. ✅ Design and format legends for clarity
6. ✅ Apply cartographic principles to grant application maps
7. ✅ Create publication-ready maps for funding applications

---

## Background: The Importance of Professional Cartography

### Why Professional Maps Matter for Grants

**Grant Reviewers Look For:**
- Clear, professional presentation
- Easy-to-understand information
- Attention to detail
- Credible, well-documented data
- Maps that tell a compelling story

**A Professional Map:**
- Increases application credibility
- Demonstrates technical competency
- Makes complex data accessible
- Shows respect for the review process
- Improves chances of funding

**This Activity's Context:**
Building on Module 4 Activity 10 where you prepared the trail data, this activity focuses on creating the professional map that accompanies your Alaska DOT Community Trail Marking Grant application.

---

## Part 1: Project Setup and Data Preparation (15 minutes)

### Task 1.1: Open ArcGIS Pro Project

**Prerequisites:**
- Completed Module 4, Activity 10
- Trail data cleaned and attributed
- Trail lengths calculated in miles
- Dangerous crossings layer created
- Halfway houses layer created

**Steps:**
1. Open your `SAR_Trail_Marking_Grant` project from Activity 10
2. Verify all layers are present:
   - SAR_Trails (line layer)
   - Dangerous_Intersections (point layer)
   - Halfway_Houses (point layer)
   - Community boundaries or points (if available)
3. Check basemap is set (will be changed in layout)

### Task 1.2: Review Map Requirements

**Grant Map Must Show:**
- All trail routes clearly visible
- Dangerous intersections prominently marked
- Halfway houses with recognizable symbols
- Community locations labeled
- Geographic context (inset map)
- Professional legend
- Scale and north arrow
- Proper attribution

**Design Goals:**
- High contrast for visibility
- Professional appearance
- Print-ready quality (300 DPI)
- Clear visual hierarchy
- Accessible to all readers

---

## Part 2: Creating the Main Map Layout (20 minutes)

### Task 2.1: Insert New Layout

**Steps:**

1. **Create Layout**
   - Insert tab → New Layout
   - Page Size: Letter (8.5" x 11")
   - Orientation: **Landscape**
   - Layout appears with default map frame

2. **Configure Map Frame**
   - Map frame already inserted
   - Contains your current map view
   - Resize if needed to leave room for title, legend, and inset

3. **Set Appropriate Extent**
   - Activate map frame (click inside it)
   - Pan and zoom to show all trails
   - Include some surrounding context
   - Ensure all features fit comfortably
   - Leave margins around data

### Task 2.2: Choose Basemap

**For Dark Satellite Imagery:**

1. **Why Dark Imagery?**
   - Provides geographic context
   - Makes white text and symbols stand out
   - Professional appearance
   - Shows terrain and water features

2. **Change Basemap:**
   - Map tab → Basemap dropdown
   - Select **World Imagery**
   - OR: Add Imagery (Clarity) for high-resolution imagery
   - Basemap loads in map frame

3. **Verify Basemap Quality:**
   - Zoom to various scales
   - Check image resolution is adequate
   - Ensure imagery loads completely

---

## Part 3: Advanced Symbology - Trails (20 minutes)

### Task 3.1: Style Trail Lines for Maximum Visibility

**Goal:** Make trails the most prominent feature on the map

**Steps:**

1. **Open Symbology Pane**
   - Select SAR_Trails layer
   - Appearance tab → Symbology
   - OR: Right-click layer → Symbology

2. **Choose Symbol Type**

   **Option A: Single Symbol (Simpler)**
   - Single Symbol
   - Choose a bright, high-contrast color
   - Recommended colors for dark backgrounds:
     - Bright Yellow (#FFFF00)
     - Cyan (#00FFFF)
     - Bright Orange (#FF8C00)
     - Hot Pink (#FF1493)

   **Option B: Unique Values (Differentiate Trails)**
   - Unique Values
   - Field: `Trail_Name` or `Grant_Priority`
   - Apply
   - Assign different colors to each trail
   - Use complementary colors that work on dark background

3. **Adjust Line Width**
   - Width: **3-4 points** for main trails
   - Wider lines = more visible
   - Test different widths
   - Balance: Visible but not overwhelming

4. **Add Line Effects for Emphasis**
   - Click symbol to open Format Symbol pane
   - Layers tab
   - Add Layer → Add new symbol layer
   - Set second layer:
     - Slightly wider (5-6 pt)
     - Darker color or black
     - Place below main color layer
   - Creates outline effect for even more visibility

### Task 3.2: Apply Multiple Colors for Trail Differentiation

**If You Have Multiple Trail Routes:**

**Example Color Scheme:**

| Trail Name | Color | RGB Values | Reasoning |
|------------|-------|------------|-----------|
| Quinhagak to Goodnews | Bright Yellow | 255, 255, 0 | High priority, high visibility |
| Fish Camp Trail | Cyan | 0, 255, 255 | Secondary route, distinct |
| Village Loop | Hot Pink | 255, 20, 147 | Short trail, needs differentiation |

**Steps:**
1. Symbology → Unique Values → Field: Trail_Name
2. For each trail:
   - Click color chip
   - Choose high-contrast color
   - Set line width (3-4 pt)
3. Arrange in legend order

---

## Part 4: Advanced Symbology - Dangerous Intersections (15 minutes)

### Task 4.1: Create Distinctive Warning Symbols

**Goal:** Dangerous crossings must be immediately recognizable

**Steps:**

1. **Open Symbology**
   - Select Dangerous_Intersections layer
   - Symbology pane opens

2. **Choose Symbol Style**
   - Gallery tab
   - Search: "danger" or "warning"
   - OR use circle with cross pattern

3. **Custom Symbol Configuration**

   **Recommended Approach: Red Circle with Dot**

   - Symbol: Circle 1
   - Color: **Red (#FF0000)**
   - Size: **14-16 points**
   - Outline: White
   - Outline width: 1.5 pt

   **Add Inner Dot:**
   - Properties → Layers
   - Add symbol layer
   - Second layer: Solid circle
   - Color: White
   - Size: 6 points
   - Result: Red circle with white center (target symbol)

4. **Test Visibility**
   - Zoom to various scales
   - Ensure symbols visible at all relevant scales
   - Adjust size if needed

### Task 4.2: Label Dangerous Crossings

**Add Descriptive Labels:**

1. **Enable Labels**
   - Right-click layer → Label Properties
   - Check: Enable labels

2. **Configure Label Field**
   - Field: Create expression combining location and hazard
   - Example: `$feature.Location + " (" + $feature.Hazard_Type + ")"`

3. **Label Appearance**
   - Font: Arial or Helvetica
   - Size: 9 pt
   - Color: **White (#FFFFFF)**
   - Bold: Yes
   - Halo: Black, 2 pt
   - Result: Labels clearly visible on imagery

---

## Part 5: Advanced Symbology - Halfway Houses (15 minutes)

### Task 5.1: Apply Cabin Symbols

**Goal:** Halfway houses should look like shelters/cabins

**Steps:**

1. **Open Symbology**
   - Select Halfway_Houses layer
   - Symbology pane

2. **Search for Cabin Symbol**
   - Gallery tab
   - Search: "cabin" or "house" or "shelter"
   - Browse emergency symbols
   - Select recognizable cabin/shelter icon

3. **Adjust Symbol Properties**
   - Size: **14-18 points**
   - Color: Bright color that contrasts with imagery
     - Recommended: Yellow (#FFFF00) or Orange (#FFA500)
   - Outline: White or Black (1 pt) for definition

4. **Alternative: Custom Symbol**

   If no cabin symbol available:
   - Use square symbol
   - Add roof shape on top (second layer)
   - Color: Brown for cabin, Red for roof
   - Size: 14-16 pt

### Task 5.2: Label Halfway Houses

**Steps:**

1. **Enable Labels**
   - Label Properties
   - Enable labels

2. **Label Configuration**
   - Field: `House_Name` or `Location`
   - Font: Arial, Bold
   - Size: 9 pt
   - Color: **White**
   - Halo: Black, 2 pt
   - Position: Above right of symbol

---

## Part 6: Community Labels with Advanced Settings (15 minutes)

### Task 6.1: Create Professional Community Labels

**Goal:** Community names must be prominent, readable, and professional

**Steps:**

1. **Enable Community Labels**
   - If you have community points or boundary layer
   - Right-click → Label Properties
   - Enable labels

2. **Configure Label Appearance**

   **Font Settings:**
   - Font: **Arial** or **Helvetica**
   - Style: **Bold**
   - Size: **12-14 pt** (larger than other labels)
   - Color: **White (#FFFFFF)**

   **Halo:**
   - Color: Black (#000000)
   - Size: **2-3 pt** (thick halo for high visibility)
   - Result: White text "pops" off dark background

3. **Advanced Label Settings**

   **Access Advanced Settings:**
   - Label Properties → Position tab

   **Position Configuration:**
   - Position: Specify best position
   - For points: Above center or centered
   - Buffer: 2 pt around label
   - Never overlap: Yes

   **Conflict Resolution:**
   - Remove duplicates: Yes
   - Never remove labels: Check (for important communities)

4. **Label Classes (If Multiple Community Types)**

   **Create Label Classes:**
   - Label Class tab → Add class
   - Class 1: Main communities (larger, bold)
   - Class 2: Smaller settlements (smaller text)
   - Set SQL query to filter each class

---

## Part 7: Creating the Inset Map (25 minutes)

### Task 7.1: Understanding Inset Maps

**Purpose:**
- Show where your project area is located
- Provide geographic context
- Help readers unfamiliar with Alaska
- Professional cartographic element

**Design:**
- Small map of Alaska
- Project area indicated with rectangle or marker
- Simple, uncluttered
- Position: Corner of main map

### Task 7.2: Create Inset Map Frame

**Steps:**

1. **Insert New Map Frame**
   - Layout must be active
   - Insert tab → Map Frame dropdown
   - Select: Default map OR Create new map
   - Draw frame in corner (typically upper right)
   - Size: ~1.5" x 1.5" to 2" x 2"

2. **Configure Inset Map**
   - Right-click new map frame → Properties
   - Name: "Inset - Alaska"
   - Frame tab → Border
   - Add thin black border (0.5 pt)

### Task 7.3: Set Up Inset Map Content

**Steps:**

1. **Activate Inset Map**
   - Click inside inset map frame
   - Opens new map view
   - Contents pane shows this map's layers

2. **Add Alaska Basemap**
   - Map tab → Basemap
   - Select: **National Geographic**
     - Shows state boundaries
     - Clean, simple appearance
     - Good for reference
   - OR: **Light Gray Canvas**
     - Minimal distraction
     - Clear boundaries

3. **Zoom to Alaska**
   - Zoom to show entire state
   - Include surrounding area for context
   - Canada and Russia visible if helpful

4. **Remove Unnecessary Layers**
   - In Contents (for inset map)
   - Remove detail layers
   - Keep only:
     - Alaska boundary
     - Major water bodies
     - Minimal labels

### Task 7.4: Add Extent Indicator

**Purpose:** Show where your main map is located within Alaska

**Steps:**

1. **Insert Extent Indicator**
   - Inset map frame active
   - Insert tab → Extent Indicator
   - Select: Main map frame name
   - Extent indicator appears as rectangle on inset

2. **Style Extent Indicator**
   - Right-click extent indicator → Properties
   - Symbol: Outline box
   - Color: **Red (#FF0000)** or **Yellow (#FFFF00)**
   - Width: **2-3 pt** (thick enough to see clearly)
   - Fill: None OR semi-transparent red (20% opacity)

3. **Verify Extent**
   - Extent indicator shows your main map area
   - Should be clearly visible
   - If too small: Main map zoomed in too close
   - If too large: Main map zoomed out too far
   - Adjust main map extent if needed

### Task 7.5: Label Inset Map

**Add "Location" or "Project Area" Text:**

1. Insert tab → Text
2. Type: "Location" or "Project Area"
3. Font: Arial, Bold, 8-9 pt
4. Position: Below inset map frame
5. Color: Black (will be on white layout background)

---

## Part 8: Adjusting Map Elements to White (20 minutes)

### Task 8.1: Change Scale Bar to White

**Why White?**
- Dark satellite imagery background
- White elements stand out clearly
- Professional appearance
- Consistent color scheme

**Steps:**

1. **Insert Scale Bar**
   - Insert tab → Scale Bar
   - Choose style: Scale Line 1 (simple, clean)
   - Position: Lower left or lower right corner

2. **Format Scale Bar**
   - Right-click scale bar → Properties
   - Display tab:
     - Units: **Miles** (for Alaska DOT grant)
     - Division units: 10 or 20 miles

3. **Change Colors to White**
   - Properties → Symbol
   - Bar: Color → **White (#FFFFFF)**
   - Text: Color → **White (#FFFFFF)**
   - Text: Font → Bold for visibility
   - Division line: **White**
   - Background: None (transparent)

4. **Add Background for Readability (Optional)**
   - Properties → Frame
   - Background: Semi-transparent black (50% opacity)
   - Border: None OR thin white line
   - Result: White scale bar on dark background stands out

### Task 8.2: Change North Arrow to White

**Steps:**

1. **Insert North Arrow**
   - Insert tab → North Arrow
   - Choose simple style: ESRI North 1 or similar
   - Position: Near scale bar or upper corner

2. **Format North Arrow**
   - Right-click → Properties
   - Symbol tab
   - Click: Edit symbol
   - Change all elements to **White**:
     - Arrow outline: White
     - Arrow fill: White
     - Text ("N"): White
     - Border: None OR white

3. **Adjust Size**
   - Size: 0.25" - 0.5" (subtle, not dominating)
   - North arrows should be visible but not prominent

### Task 8.3: Change Title Text to White

**Steps:**

1. **Insert Title**
   - Insert tab → Dynamic Text → Title
   - OR: Insert → Text (for custom title)
   - Position: Top center or top left

2. **Configure Title Text**
   - Text: "Quinhagak Community Trail System"
   - Subtitle: "Alaska DOT Community Trail Marking Grant Application"

3. **Format Title**
   - Font: Arial or Helvetica
   - Style: **Bold**
   - Size: **18-24 pt**
   - Color: **White (#FFFFFF)**
   - Alignment: Center (if centered) or Left

4. **Add Halo or Background**
   - Text Symbol → Appearance
   - Halo: Black, 3 pt
   - OR: Add semi-transparent black background box
   - Result: Title clearly visible on imagery

---

## Part 9: Creating a Professional Legend (15 minutes)

### Task 9.1: Insert and Configure Legend

**Steps:**

1. **Insert Legend**
   - Insert tab → Legend
   - Click and drag on layout to create legend
   - Position: Right side or bottom right
   - Size: Compact but readable

2. **Configure Legend Content**
   - Right-click legend → Properties
   - Legend Items tab
   - **Remove unnecessary layers:**
     - Basemaps
     - Reference layers
     - Inset map layers

   - **Keep only:**
     - Trails (with names/colors)
     - Dangerous Intersections
     - Halfway Houses
     - Community points (if separate layer)

3. **Arrange Legend Order**
   - Drag items in Properties to reorder
   - Logical order (most important first):
     1. Trails
     2. Dangerous Intersections
     3. Halfway Houses
     4. Communities

### Task 9.2: Format Legend for Professional Appearance

**Advanced Formatting:**

1. **Open Legend Properties**
   - Properties → General tab

2. **Title Configuration**
   - Title: "Map Legend" or "Trail System Features"
   - Font: Arial, Bold, 12 pt
   - Color: White (if on imagery) OR Black (if on white background)

3. **Item Text Formatting**
   - Appearance tab → Text Symbol
   - Font: Arial, 10 pt
   - Color: **White** (for visibility on imagery)
   - OR place legend on white background box

4. **Layout and Spacing**
   - Arrangement tab
   - Patch: Size → Width: 20 pt, Height: 10 pt
   - Gap: 5 pt between symbol and text
   - Item Spacing: 3 pt
   - Column spacing: 10 pt (if using columns)

5. **Background and Border**

   **Option A: White Background**
   - Frame tab → Background
   - Color: White
   - Border: Black, 1 pt
   - Result: Clean, traditional legend box

   **Option B: Semi-transparent Dark Background**
   - Background: Black with 50-70% opacity
   - Border: White, 1 pt
   - Text: All white
   - Result: Integrates with dark imagery

### Task 9.3: Refine Legend Labels

**Make Legend More Descriptive:**

1. **Rename Layer Items**
   - Right-click layer in Contents → Properties
   - General tab → Name
   - Change from "SAR_Trails" to "Winter Snowmachine Trails"
   - Changes what appears in legend

2. **Customize Feature Labels**
   - Legend Properties → Legend Items
   - Select item → Properties button
   - Customize label text
   - Example:
     - "Dangerous River Crossings" instead of "Dangerous_Intersections"
     - "Emergency Shelters" instead of "Halfway_Houses"

---

## Part 10: Final Layout Elements and Polish (15 minutes)

### Task 10.1: Add Data Sources and Metadata

**Professional Attribution:**

1. **Insert Text Box**
   - Insert tab → Text
   - Position: Lower left corner
   - Size: Small (8 pt font)

2. **Content:**
   ```
   Map prepared by [Your Name]
   From Garmin GPX data collected by Quinhagak SAR volunteers

   Data Sources:
   Trail GPS Data: Quinhagak SAR Team, November 2025
   Basemap: Esri World Imagery
   Projection: NAD 1983 StatePlane Alaska 7 FIPS 5007
   ```

3. **Format:**
   - Font: Arial, 8 pt
   - Color: **White**
   - Add semi-transparent black background box
   - Border: None

### Task 10.2: Add Contact Information (Optional)

**For Grant Submission:**

1. Insert text box
2. Content:
   ```
   Contact: [Name]
   Organization: Quinhagak Tribal Council
   Phone: (907) XXX-XXXX
   Email: xxx@xxx.com
   Date: November 2025
   ```

3. Format: Small text, white on dark background

### Task 10.3: Add Trail Statistics Table (Optional but Impressive)

**Summary Table for Grant:**

1. **Insert Text Box**
   - Position: Available space (right side or bottom)

2. **Create Formatted Table:**
   ```
   TRAIL SYSTEM SUMMARY

   Trail Name                      Length (Miles)   Priority
   ────────────────────────────────────────────────────────
   Quinhagak to Goodnews Bay       47.3            High
   Fish Camp Trail                 8.7             Medium
   Village Loop                    3.2             High
   ────────────────────────────────────────────────────────
   Total Trail System:             59.2 miles
   ```

3. **Format:**
   - Font: Courier New (monospace for alignment)
   - Size: 9 pt
   - Color: White
   - Background: Semi-transparent black box

---

## Part 11: Final Review and Quality Control (10 minutes)

### Task 11.1: Cartographic Review Checklist

**Visual Hierarchy:**
- [ ] Trails are most prominent feature
- [ ] Dangerous intersections clearly marked
- [ ] Halfway houses recognizable
- [ ] Text readable at all scales
- [ ] Title is largest text element
- [ ] Legend organized logically

**Map Elements:**
- [ ] Title present and descriptive
- [ ] Scale bar shows appropriate units (miles)
- [ ] North arrow included and oriented correctly
- [ ] Legend includes all relevant layers
- [ ] Inset map shows project location
- [ ] Data sources attributed
- [ ] All text uses consistent white color
- [ ] All elements visible on dark background

**Accuracy:**
- [ ] All trails present and correctly positioned
- [ ] All dangerous crossings marked
- [ ] All halfway houses shown
- [ ] Scale bar matches map scale
- [ ] North arrow points true north
- [ ] Coordinate system documented

**Professional Quality:**
- [ ] Layout balanced (not crowded)
- [ ] Consistent fonts throughout
- [ ] Consistent colors and styles
- [ ] No overlapping elements
- [ ] Clean, professional appearance
- [ ] Print-ready resolution

### Task 11.2: Test Print Quality

**Before Final Export:**

1. **Check at 100% View**
   - Layout View → Zoom to 100%
   - Simulates printed size
   - Verify all text readable
   - Check symbol sizes appropriate

2. **Check Color Contrast**
   - All white elements visible?
   - Color-blind accessible?
   - Use online color-blind simulator if available

3. **Review with Others**
   - Show to SAR team members
   - Verify accuracy of trails and crossings
   - Get feedback on clarity
   - Make final adjustments

---

## Part 12: Export Final Map (10 minutes)

### Task 12.1: Export High-Quality PDF

**For Grant Submission:**

1. **Share Tab → Export Layout**
2. **Configure Export Settings:**
   - **Format: PDF**
   - **Resolution: 300 DPI** (high quality for printing)
   - **Color Mode: RGB**
   - **Embed fonts: Yes**
   - **Output layers: No** (single image)
   - **Compress vector graphics: No** (maintain quality)
   - **Image compression: LZW** (lossless)

3. **Filename:**
   - `SAR_Trail_Marking_Grant_Map_2025.pdf`
   - Save to project folder

4. **Verify PDF:**
   - Open PDF in Adobe Reader
   - Check all elements visible
   - Verify text readable
   - Confirm colors accurate
   - Test printing (if possible)

### Task 12.2: Export Image Version (JPG)

**For Digital Sharing and Web:**

1. **Share Tab → Export Layout**
2. **Format: JPEG**
3. **Settings:**
   - Resolution: 300 DPI
   - Color Mode: RGB
   - Quality: Maximum

4. **Filename:**
   - `SAR_Trail_Marking_Grant_Map_2025.jpg`
   - Copy to `assets/images/` folder

---

## Deliverables

### Required Submissions

1. **✅ High-Quality PDF Map**
   - Resolution: 300 DPI
   - All elements visible and professional
   - Print-ready quality
   - Filename: `SAR_Trail_Marking_Grant_Map_2025.pdf`

2. **✅ JPG Version**
   - For digital distribution
   - Same quality as PDF
   - Filename: `SAR_Trail_Marking_Grant_Map_2025.jpg`

3. **✅ ArcGIS Pro Project Package**
   - Complete project with all data
   - Layout saved
   - Ready for revisions if needed

### Map Must Include:

- [ ] Professional title
- [ ] All trail routes clearly visible with distinct colors
- [ ] Dangerous intersections prominently marked (red circles)
- [ ] Halfway houses with recognizable cabin symbols
- [ ] Community labels in white
- [ ] Inset map showing project location in Alaska
- [ ] Scale bar in miles (white)
- [ ] North arrow (white)
- [ ] Professional legend with clear labels
- [ ] Data sources and attribution
- [ ] All text elements in white for visibility

---

## Assessment Criteria

| Criteria | Excellent (4) | Good (3) | Satisfactory (2) | Needs Work (1) |
|----------|---------------|----------|------------------|----------------|
| **Visual Hierarchy** | Clear, trails dominant, perfect balance | Good hierarchy, trails prominent | Some hierarchy, improvements needed | Cluttered, unclear focus |
| **Symbology** | Professional, highly visible, intuitive | Good symbols, mostly clear | Basic symbols, some visibility issues | Poor symbol choices |
| **Map Elements** | All elements present, professionally formatted | Most elements, good quality | Some elements, adequate quality | Missing elements or poor quality |
| **Inset Map** | Professional, clear extent indicator, perfect context | Good inset, clear indicator | Basic inset, adequate | Poor or missing inset |
| **Text Visibility** | All text white, highly readable, perfect contrast | Most text visible, good contrast | Some visibility issues | Text hard to read |
| **Legend** | Professional, clear, well-organized, custom labels | Good legend, organized | Basic legend, adequate | Poor or confusing legend |
| **Overall Design** | Grant-ready, exceptional quality, publishable | Professional, strong quality | Adequate for submission | Not ready for submission |

---

## Discussion Questions

### Cartographic Design

1. Why is visual hierarchy important in grant application maps?
2. How does the choice of basemap affect readability and professionalism?
3. What role does color contrast play in map effectiveness?

### Technical Decisions

4. Why create an inset map showing Alaska? What does it add to the application?
5. How do you decide which map elements to make white vs. other colors?
6. What makes a legend "professional" versus just functional?

### Real-World Application

7. How does the quality of your map affect grant review outcomes?
8. What feedback would you seek before submitting a map with a grant application?
9. How might you adapt this map design for a different grant or purpose?

### Professional Skills

10. What cartographic principles are most important for funding applications?
11. How do you balance data accuracy with visual appeal?
12. What role does attention to detail play in professional cartography?

---

## Real-World Outcome: Quinhagak SAR Grant Application

### The Complete Process

**Data Collection (Module 2):**
- GPS tracks collected by SAR volunteers
- Garmin units used on actual trail routes
- Dangerous crossings identified in field

**Data Preparation (Module 4):**
- GPX files converted to feature classes
- Edit tools used to clean and merge segments
- Trail lengths calculated in US Survey Miles
- Attribute fields populated with grant requirements

**Professional Map Creation (This Activity):**
- Advanced cartography applied
- Professional layout designed
- High-quality export created
- Grant-ready document produced

### Map Features That Made a Difference

**Technical Excellence:**
- Accurate trail routes from GPS data
- Precise measurements for cost estimation
- Professional symbology for clarity
- Proper coordinate system and attribution

**Cartographic Quality:**
- Clear visual hierarchy (trails most prominent)
- Intuitive symbols (cabins, danger markers)
- Effective use of color and contrast
- Professional legend and inset map

**Communication Impact:**
- Grant reviewers could quickly understand project
- Trail system clearly visible and documented
- Safety concerns prominently shown
- Professional presentation demonstrated competence

### Files Created

**Example Map:** `assets/images/adotfinalmap.jpg`
- Shows complete trail system
- Dangerous intersections clearly marked
- Halfway houses with cabin symbols
- White text and map elements for visibility
- Professional inset map of Alaska
- Complete attribution and metadata

**This map demonstrates:**
- Professional GIS and cartographic skills
- Attention to detail and accuracy
- Understanding of grant requirements
- Community commitment to safety

---

## Extension Activities

### Advanced Cartography

1. **Create Multiple Map Versions:**
   - Poster size (24" x 36") for community display
   - Website version (smaller, optimized)
   - Presentation version (slides)

2. **Add Elevation Profile:**
   - Show trail elevation changes
   - Highlight steep sections
   - Add to map layout as supplementary graphic

3. **Create Story Map:**
   - ArcGIS Online Story Map
   - Embed your professional map
   - Add photos and narrative
   - Interactive trail exploration

### Alternative Map Designs

1. **Winter Conditions Map:**
   - Same trails, different focus
   - Show ice conditions, overflow areas
   - Temperature and wind exposure
   - For SAR emergency reference

2. **Historical Comparison Map:**
   - Show traditional routes vs. current
   - Add historical placenames
   - Document changes over time

3. **Future Planning Map:**
   - Show proposed marker locations
   - Phase implementation over years
   - Budget allocation by segment

---

## Resources

### Cartographic Principles

- [Esri Cartography Guide](https://www.esri.com/en-us/maps-we-love/gallery)
- [NACIS (North American Cartographic Information Society)](https://nacis.org/)
- Color Brewer: [colorbrewer2.org](https://colorbrewer2.org) (accessible color schemes)

### ArcGIS Pro Documentation

- [Map Layouts in ArcGIS Pro](https://pro.arcgis.com/en/pro-app/latest/help/layouts/)
- [Inset Maps](https://pro.arcgis.com/en/pro-app/latest/help/layouts/add-an-extent-indicator-to-a-layout.htm)
- [Advanced Symbology](https://pro.arcgis.com/en/pro-app/latest/help/mapping/symbols-and-styles/)
- [Label Expression Guide](https://pro.arcgis.com/en/pro-app/latest/help/mapping/text/label-basics.htm)

### Related Activities

- Module 4, Activity 10: SAR Trail Marking Grant (data preparation)
- Module 5, Lesson 6: Styling Data
- Module 5, Lesson 7: Map Elements

---

## Instructor Notes

### Preparation

**Before Activity:**
- Review completed example map: `assets/images/adotfinalmap.jpg`
- Ensure students completed Module 4, Activity 10
- Verify all students have required trail data
- Test export settings on department printers

**Time Management:**
- Inset map creation takes longer than expected
- Allow flexibility for experimentation with symbology
- Consider breaking into two sessions if needed

### Teaching Tips

**Emphasize Real-World Impact:**
- This map will be submitted with actual grant
- Professional quality directly affects funding outcomes
- Attention to detail demonstrates community commitment

**Encourage Creativity Within Constraints:**
- Grant requirements are fixed
- Design choices within requirements show skill
- Balance creativity with professionalism

**Demonstrate Before Students Do:**
- Show completed map first
- Walk through key techniques
- Allow students to replicate and adapt

### Common Challenges

**Issue: Text Not Visible on Imagery**
**Solution:**
- Increase halo size (3 pt minimum)
- Try semi-transparent background boxes
- Consider adjusting basemap transparency

**Issue: Inset Map Extent Indicator Too Small**
**Solution:**
- Main map may be zoomed out too far
- Adjust main map extent
- Or make inset map show smaller area of Alaska

**Issue: Legend Overlaps with Data**
**Solution:**
- Move legend to less-critical area
- Reduce legend size
- Use columns to make legend more compact

**Issue: Export Quality Poor**
**Solution:**
- Verify 300 DPI setting
- Check embed fonts option
- Use PDF format (better than JPG for text)

### Assessment Tips

**Evaluate:**
- Technical execution of cartographic principles
- Professional appearance and attention to detail
- Whether map meets grant requirements
- Creativity within professional constraints

**Provide Feedback On:**
- Specific symbology choices and effectiveness
- Text readability at print size
- Legend clarity and organization
- Overall visual hierarchy

---

## Acknowledgments

This activity is based on the real SAR Trail Marking Grant application map prepared by Patrick Jones and Byron Phillips for Quinhagak Search and Rescue's Alaska DOT Community Trail Marking Grant application. The map demonstrates professional cartographic techniques applied to community safety and grant funding.

The example map (`assets/images/adotfinalmap.jpg`) serves as a model for students creating their own professional grant application maps.

---

**Activity Version:** 1.0
**Last Updated:** December 2025
**Module:** 5 - Cartography
**Location:** Quinhagak, Alaska
**Real-World Application:** Alaska DOT Grant Support
