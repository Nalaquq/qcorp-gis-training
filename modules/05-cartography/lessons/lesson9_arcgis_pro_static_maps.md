# Lesson 9: Creating Static Maps in ArcGIS Pro

**Duration:** 2-3 hours
**Prerequisites:** Basic ArcGIS Pro knowledge, understanding of coordinate systems
**Training Date Reference:** 2025

---

## Lesson Overview

This lesson teaches you how to create professional static maps in ArcGIS Pro. You'll learn the fundamentals of cartographic design, layout creation, and exporting publication-ready maps. We'll work through a complete example using the AtlantGIS dataset to create a polished static map with all essential map elements.

---

## Learning Objectives

By the end of this lesson, you will be able to:

1. Understand the difference between static, interactive, and dynamic maps
2. Apply cartographic storytelling principles to map design
3. Manage project data and file organization
4. Work with coordinate projection systems
5. Create and apply hillshade visualizations
6. Select appropriate symbology and accessible color schemes
7. Create professional layouts with proper dimensions
8. Add and configure essential map elements (legends, scale bars, north arrows)
9. Use inset maps for geographic context
10. Export maps at appropriate resolutions
11. Save and reuse layout templates

---

## Key Terminology

- **Static Map**: A fixed image or printed map that doesn't change or allow interaction
- **Interactive Map**: A web-based map that users can pan, zoom, and click for information
- **Dynamic Map**: A map that updates automatically based on real-time data or user inputs
- **Coordinate Projection System**: A mathematical framework for representing the 3D Earth on a 2D map
- **Legend**: A key explaining the symbols, colors, and patterns used on the map
- **North Arrow**: An indicator showing the orientation of the map relative to north
- **Scale Bar**: A graphical representation of map scale showing distance relationships
- **Scalable Vector Graphics (SVG)**: Vector-based image format that scales without quality loss
- **DPI (Dots Per Inch)**: Resolution measure for printed or exported maps (300+ DPI recommended for print)
- **Hillshade**: A grayscale 3D representation of terrain showing relief through shadows

---

## Part 1: Understanding Map Types and Cartographic Storytelling

### Types of Maps

**Static Maps:**
- Fixed, non-interactive images
- Used for reports, presentations, and printing
- Complete story told in one view
- Examples: Wall maps, publication figures, handouts

**Interactive Maps:**
- Web-based, allow user exploration
- Pan, zoom, click for information
- Examples: ArcGIS Online maps, web applications

**Dynamic Maps:**
- Update automatically with new data
- Real-time or scheduled updates
- Examples: Weather maps, live tracking systems

### Cartographic Storytelling

> **Key Principle**: When we make maps, we are storytelling. Focus on the story you want to tell.

**Storytelling Guidelines:**
- Identify your audience and their needs
- Determine the key message or question
- Select only relevant layers and data
- Use visualization techniques that highlight your story
- Remove unnecessary clutter that distracts from the message

**Example Stories:**
- "Where are safe relocation sites based on elevation and proximity to services?"
- "How has coastal erosion changed over 20 years?"
- "What archaeological sites exist in our traditional territory?"

### Example Maps Review

Review the example maps in `modules/05-cartography/resources/example-maps/` to see different storytelling approaches and map styles.

---

## Part 2: Project Setup and Data Management

### Best Practices for Data Organization

**Why organize data properly?**
- Prevents broken data links
- Easy to share entire project
- Clear documentation for future reference
- Easier troubleshooting

**Project Directory Structure:**
```
ProjectName/
├── ProjectName.aprx
├── data/
│   ├── raw/
│   └── processed/
├── outputs/
├── layouts/
└── documentation/
```

### Exercise: Download and Organize Data

**Dataset:** AtlantGIS
**Source:** https://github.com/kacebe/AtlantGIS

**Steps:**
1. Create a new project folder on your computer
2. Download the AtlantGIS dataset from GitHub
3. Extract all data to a `data` folder within your project
4. Create a new ArcGIS Pro project (.aprx) in the project folder
5. Add data from your local project directory

**Important:** Always download data to your specific project directory, not to a general downloads folder. This ensures:
- Data remains accessible even if network paths change
- Project can be easily shared with all dependencies
- Clear organization of project resources

---

## Part 3: Coordinate Projection Systems

### Understanding Projections

**Key Concepts:**
- The Earth is 3D (ellipsoid), maps are 2D
- Projections transform 3D coordinates to 2D
- Different projections preserve different properties (area, shape, distance, direction)
- No projection is perfect - all involve some distortion

**ArcGIS Pro Automatic Reprojection:**
- ArcGIS Pro automatically displays layers in the map's coordinate system
- Layers can have different projections and still display together
- "On-the-fly" projection for visualization
- **Important:** For analysis, reproject data to a common system

### Working with Projections

**To check a layer's projection:**
1. Right-click layer → Properties
2. Go to Source tab
3. View Spatial Reference

**To set map projection:**
1. Right-click Map in Contents pane
2. Properties → Coordinate Systems
3. Select appropriate projection for your area

**Common Alaska Projections:**
- Alaska Albers (Equal Area): Good for state-wide area calculations
- NAD83 Alaska State Plane zones: Good for local accuracy
- Web Mercator: For web mapping compatibility

---

## Part 4: Working with Terrain Data

### Adding and Visualizing DEM Layers

**Digital Elevation Model (DEM):** Raster dataset representing terrain elevation

**Exercise: Create a Hillshade**

1. Add DEM layer to your map
2. Open Geoprocessing pane (Analysis tab → Tools)
3. Search for "Hillshade"
4. Select Hillshade tool (3D Analyst or Spatial Analyst)
5. Configure parameters:
   - Input raster: Your DEM layer
   - Output raster: Save to project geodatabase
   - Azimuth: 315° (default - northwest sun)
   - Altitude: 45° (default - sun angle)
6. Run tool
7. Adjust layer transparency to overlay on DEM if desired

**Hillshade Benefits:**
- Adds visual depth and terrain understanding
- Helps identify valleys, ridges, slopes
- Professional cartographic appearance
- Works well as subtle background layer

---

## Part 5: Symbology and Color Theory

### Selecting Appropriate Symbology

**Considerations:**
- Data type (categorical, continuous, sequential)
- Map purpose and audience
- Color blindness accessibility
- Cultural color associations
- Contrast and readability

### Color Selection Tools

**Color Hexa** (https://www.colorhexa.com/)
- Explore colors and their properties
- View complementary, analogous, triadic colors
- Get hexadecimal color codes
- Test color combinations

**Using Hexadecimal Codes in ArcGIS Pro:**
1. Open layer symbology
2. Click color swatch
3. Click "Color Properties"
4. Enter hex code (e.g., #2E8B57)

### Accessibility and Color Blindness

**ArcGIS Pro Color Blindness Simulator:**
1. View tab → Color Vision Simulator
2. Select type of color vision deficiency
3. Preview how your map appears
4. Adjust colors for better accessibility

**Common Types:**
- Deuteranopia (green-blind)
- Protanopia (red-blind)
- Tritanopia (blue-blind)

**Best Practices:**
- Use ColorBrewer schemes (built into ArcGIS Pro)
- Combine color with patterns or symbols
- Test with simulator before finalizing
- Avoid red-green combinations
- Ensure sufficient contrast

**External Tool:** Color Hexa Color Blind Simulator
https://www.colorhexa.com/ → Search color → View "Color Blindness Simulator"

### Changing Point Symbology

**Exercise: Use Custom Symbols**

1. Select point layer in Contents
2. Open Symbology pane
3. Click symbol to open Gallery
4. Search for shapes (e.g., "diamond")
5. Select symbol and adjust:
   - Size
   - Color
   - Outline
   - Rotation

---

## Part 6: Creating Layouts

### Understanding Layout Dimensions

**Standard Print Sizes:**
- Letter: 8.5" × 11"
- Tabloid: 11" × 17"
- Legal: 8.5" × 14"
- A4: 210mm × 297mm (8.27" × 11.69")

**PowerPoint Slides:**
- Width: 13.333"
- Height: 7.5"
- (Standard 16:9 widescreen ratio)

**Poster Sizes:**
- 24" × 36"
- 36" × 48"
- Custom sizes as needed

### Creating a New Layout

1. Insert tab → New Layout
2. Select page size or create custom
3. Set orientation (Portrait/Landscape)

**Layout vs. Map View:**
- **Map View**: Where you design and interact with data
- **Layout View**: Where you arrange map and elements for output

---

## Part 7: Adding Map Elements

### Insert Main Map Frame

1. In Layout view: Insert tab → Map Frame
2. Select which map to insert
3. Draw rectangle on layout page
4. Resize and position as needed

**Map Frame Properties:**
- Right-click frame → Properties
- Set scale, rotation, extent
- Lock scale or extent if needed

### Creating an Inset Map

**Purpose:** Show geographic context - where is this place in relation to a larger area?

**Exercise: Add Inset Map of Island Location**

1. Create a new map: Insert tab → New Map
2. Add appropriate basemap for context
3. Zoom to larger regional extent
4. Insert tab → Map Frame → Select your new map
5. Draw small rectangle (typically in corner)
6. Adjust basemap transparency if needed (Appearance tab)

**Adding Extent Indicator:**
1. Select inset map frame
2. Insert tab → Extent Indicator
3. Select main map to indicate
4. Symbology will show main map extent as box/outline on inset

**Enhancing Extent Indicator:**
- Adjust symbology (color, outline width)
- Add transparency
- Use contrasting color to stand out

**Add Text Over Inset:**
1. Insert tab → Text
2. Add label (e.g., "Location" or place name)
3. Format text (font, size, color)

**Add Drop Shadow:**
1. Select map frame or text
2. Format tab → Drop Shadow
3. Adjust transparency, offset, blur

---

## Part 8: Scale Bars

**Purpose:** Show distance relationships on the map

**Adding a Scale Bar:**
1. Select main map frame first (important!)
2. Insert tab → Scale Bar
3. Select style from gallery
4. Position on layout

**Common Mistake:** Selecting wrong map frame results in scale bar for inset map instead of main map

**Scale Bar Properties:**
- Right-click → Properties
- Change units (miles, kilometers, meters, feet)
- Adjust divisions and subdivisions
- Modify style and size
- Set number of divisions

---

## Part 9: North Arrows and Custom Graphics

### Standard North Arrows

1. Select main map frame
2. Insert tab → North Arrow
3. Select style from gallery
4. Position on layout

### Custom North Arrows and Logos

**Nalaquq Logos and North Arrows:**
Located in: `modules/05-cartography/resources/mapping-assets`

**Adding Custom Graphics:**

**Method 1: Add as Picture**
1. Insert tab → Picture
2. Browse to PNG/SVG file
3. Position and resize

**Method 2: Add Custom North Arrow to Gallery**

Follow tutorial: [How to Add Custom North Arrow](https://community.esri.com/t5/arcgis-pro-questions/layout-custom-north-arrow/td-p/1149595)

**Steps:**
1. Prepare north arrow graphic (SVG or EMF format recommended)
2. Navigate to North Arrow style location
3. Copy custom graphic to style folder
4. Refresh ArcGIS Pro
5. Access from North Arrow gallery

**Adjusting Map Rotation:**
1. Select map frame
2. Properties → Display
3. Adjust Rotation angle
4. Ensure north arrow points correctly (typically straight up)

---

## Part 10: Legends

### Creating a Legend

1. Select main map frame
2. Insert tab → Legend
3. Position and resize

### Customizing Legend

**Remove Unnecessary Items:**
1. Right-click legend → Properties
2. Legend Items section
3. Select items to remove (e.g., basemap, hillshade)
4. Remove or hide

**Rename Layer Labels:**
- Option 1: Change layer name in Contents pane
- Option 2: Right-click legend item → Properties → Rename in legend only

**Make Labels Reader-Friendly:**
- "Archaeological Sites" instead of "arch_sites_2024"
- "Precipitation (inches)" instead of "precip_data"
- "City Names" instead of "cities_pts"

**Legend Formatting:**
- Adjust columns
- Change font and size
- Modify spacing
- Add border or background
- Reorder items

---

## Part 11: Adding Titles and Final Touches

### Map Title

1. Insert tab → Text
2. Type descriptive title
3. Format:
   - Larger font size (18-36pt)
   - Bold weight
   - Clear, descriptive text
   - Position prominently (usually top)

**Good Title Examples:**
- "Archaeological Sites and Precipitation Patterns in Atlantis"
- "Quinhagak Land Manager Reference Map"
- "Traditional Yup'ik Place Names in the Quinhagak Region"

### Additional Text Elements

**Consider adding:**
- Subtitle or description
- Data sources and dates
- Map author/organization
- Production date
- Projection information
- Disclaimers or notes

---

## Part 12: Exporting Maps

### Export Settings

**For Print (PNG, PDF, TIFF):**
- Resolution: 300 DPI minimum
- Color Mode: RGB or CMYK (check with printer)
- Format: PDF (recommended) or high-res PNG

**For Web/Presentations (PNG, JPG):**
- Resolution: 150-200 DPI
- Format: PNG (transparent background option) or JPG
- Optimize file size

**For Large Format Printing:**
- Resolution: 300 DPI
- Large page size
- PDF format recommended
- Embed fonts

### Exporting Your Map

1. Share tab → Export Layout
2. Choose format
3. Set resolution (DPI)
4. Configure format-specific options
5. Specify output location
6. Export

**File Location:**
Example: `modules/05-cartography/resources/example-maps/Atlantis Static Map.png`

---

## Part 13: Saving Layout Templates

### Why Use Layout Templates?

- Reuse consistent design across multiple maps
- Save time on future projects
- Maintain organizational branding
- Ensure consistency in map series

### Creating a Layout Template

**Method 1: Save Layout File (.pagx)**

1. Close all map frames except your template layout
2. File → Save As → Save a Copy
3. Choose "Layout Files (*.pagx)"
4. Name template descriptively
5. Save to templates folder

**Method 2: Export Layout to Template**

Follow ArcGIS Pro documentation:
- [How to Create a Layout Template](https://support.esri.com/en-us/knowledge-base/how-to-create-a-layout-template-from-a-layout-for-diffe-000028072)
- [Layout Files Documentation](https://pro.arcgis.com/en/pro-app/latest/help/layouts/layout-files.htm#ESRI_SECTION1_C30D73392D964D51A8B606128A8A6E8F)

**Video Tutorial:**
[Saving and Using Layout Templates in ArcGIS Pro](https://www.youtube.com/watch?v=dryU9r595t4)

### Using a Saved Template

1. Insert tab → New Layout → Import Layout File
2. Browse to .pagx template file
3. Select and import
4. Update map frames to show your new data
5. Update text elements as needed

**Template Location:**
`modules/05-cartography/resources/layouts/training layout template.pagx`

---

## Hands-On Activities

### Activity 1: Atlantis Map Recreation

Follow along with the instructor to create the complete Atlantis map:

**Requirements:**
- DEM with hillshade
- City labels
- Archaeological sites layer
- Precipitation data
- Main map and inset map showing island location
- Legend, scale bar, north arrow
- Title and descriptive text
- Professional color scheme
- 300 DPI export

**Dataset:** https://github.com/kacebe/AtlantGIS

### Activity 2: Custom Quinhagak Maps

Each GIS technician creates a unique map for Quinhagak:

**Option A: Land Manager Reference Map**
- Purpose: Reusable template for land management office
- Include: Boundaries, facilities, land use zones, access points
- Format: 8.5" × 11" for easy printing
- Save as template for repeated use

**Option B: Yup'ik Place Names Map**
- Purpose: Document and share traditional place names
- Include: Place name labels, geographic features, community context
- Format: Presentation or poster size
- Culturally appropriate colors and design

**Requirements for Both:**
- All essential map elements
- Clear, accessible symbology
- Proper data attribution
- 300 DPI export
- Saved layout template

---

## Troubleshooting Common Issues

**Watch this troubleshooting guide for common layout issues in ArcGIS Pro:**

[![ArcGIS Pro Layout Troubleshooting Guide](https://img.youtube.com/vi/wMMYV1t4cCI/maxresdefault.jpg)](https://www.youtube.com/watch?v=wMMYV1t4cCI&t=1s)

*Click the image above to watch the troubleshooting tutorial on YouTube*

### Broken Data Links
- **Symptom:** Red exclamation mark on layer
- **Solution:** Right-click → Repair Data Source → Navigate to correct file location
- **Prevention:** Always store data in project folder

### Wrong Scale Bar
- **Symptom:** Scale bar doesn't match main map
- **Solution:** Delete scale bar, select main map frame first, then add new scale bar

### Low Quality Export
- **Symptom:** Blurry or pixelated output
- **Solution:** Increase DPI to 300 or higher in export settings

### Text Cut Off in Export
- **Symptom:** Text appears in layout but missing in export
- **Solution:** Increase export resolution or adjust text size/position

### Colors Look Different in Export
- **Symptom:** Colors change between layout view and exported PDF
- **Solution:** Use RGB color mode, check PDF reader settings, try different export format

---

## Key Takeaways

1. **Storytelling First:** Always identify your message before designing the map
2. **Organization Matters:** Keep all data in project folders for portability
3. **Accessibility:** Use color blindness simulators and sufficient contrast
4. **Essential Elements:** Every static map needs title, legend, scale bar, north arrow
5. **Resolution:** Use 300 DPI minimum for print outputs
6. **Templates:** Save layouts as templates for efficiency and consistency
7. **Context:** Inset maps help readers understand location
8. **Less is More:** Include only layers that support your story

---

## Resources

### Data Sources
- AtlantGIS Dataset: https://github.com/kacebe/AtlantGIS

### Tools
- Color Hexa: https://www.colorhexa.com/
- ArcGIS Pro Color Blindness Simulator (built-in)

### Tutorials
- Custom North Arrows: https://community.esri.com/t5/arcgis-pro-questions/layout-custom-north-arrow/td-p/1149595
- Layout Templates Guide: https://support.esri.com/en-us/knowledge-base/how-to-create-a-layout-template-from-a-layout-for-diffe-000028072
- Layout Files Documentation: https://pro.arcgis.com/en/pro-app/latest/help/layouts/layout-files.htm
- Video: Saving Layout Templates: https://www.youtube.com/watch?v=dryU9r595t4

### Project Assets
- Example Maps: `modules/05-cartography/resources/example-maps/`
- Nalaquq Logos and North Arrows: `modules/05-cartography/resources/mapping-assets/`
- Layout Templates: `modules/05-cartography/resources/layouts/`
- Training Output: `modules/05-cartography/resources/example-maps/Atlantis Static Map.png`

---

## Next Steps

After completing this lesson:
1. Practice creating maps with different datasets
2. Build a library of layout templates for common map types
3. Experiment with advanced symbology techniques
4. Create a map series using the same template
5. Explore Python scripting for layout automation
6. Learn about map books and tile indices for large areas

---

**Training Date:** 2025
**Module:** 05 - Cartography
**Lesson Type:** Hands-on Workshop
**Software:** ArcGIS Pro
