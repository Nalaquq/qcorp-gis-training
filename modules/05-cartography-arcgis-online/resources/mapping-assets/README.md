# Mapping Assets

Custom cartographic elements for creating professional maps in ArcGIS Pro and ArcGIS Online.

---

## Purpose

This directory contains reusable mapping assets to ensure:
- **Consistent branding** across all Quinhagak maps
- **Professional appearance** for reports and presentations
- **Cultural appropriateness** with Alaska Native design elements
- **Time savings** - no need to recreate elements for each map
- **Quality standards** maintained across all map products

---

## Directory Structure

```
mapping-assets/
├── README.md (this file)
├── north-arrows/          Custom north arrow designs
├── scale-bars/            Custom scale bar styles
├── symbols/               Custom point/line/polygon symbols
├── logos/                 Organization logos and emblems
└── templates/             Pre-configured map templates
```

---

## North Arrows

**Location:** `./north-arrows/`

Custom north arrow designs for Quinhagak maps.

### What to Include

**File formats:**
- **PNG** - Transparent background, 300+ DPI
- **SVG** - Vector format (scales without quality loss)
- **EMF** - Enhanced Metafile for ArcGIS Pro
- **AI/EPS** - Adobe Illustrator source files

**Design variations:**
- Simple/minimal (for technical maps)
- Decorative (for community presentations)
- Cultural designs (Yup'ik patterns/motifs)
- Size variations (small, medium, large)

### Naming Convention

```
north_arrow_[style]_[size].[format]

Examples:
north_arrow_simple_small.png
north_arrow_yupik_pattern_large.svg
north_arrow_minimal_medium.emf
```

### Using in ArcGIS Pro

1. Insert → North Arrow → Browse
2. Navigate to this folder
3. Select your custom north arrow
4. Adjust size and placement

### Using in ArcGIS Online

1. Add image to Content
2. Share appropriately
3. Reference URL in map

---

## Scale Bars

**Location:** `./scale-bars/`

Custom scale bar styles and pre-made scale graphics.

### What to Include

**File formats:**
- **PNG/SVG** - Custom scale bar graphics
- **Style files** - ArcGIS Pro style packages (.stylx)

**Scale types:**
- Metric (meters/kilometers)
- US Survey Feet
- Dual units (metric and imperial)
- Various styles (simple, graduated, alternating)

### Common Alaska Scales

For local/village scale maps:
- 1:1,000 (detailed site plans)
- 1:5,000 (village infrastructure)
- 1:10,000 (community area)

For regional maps:
- 1:50,000 (regional planning)
- 1:100,000 (district scale)
- 1:250,000 (regional overview)

### Naming Convention

```
scale_bar_[units]_[style].[format]

Examples:
scale_bar_feet_simple.png
scale_bar_meters_graduated.svg
scale_bar_dual_alternating.stylx
```

### Using in ArcGIS Pro

1. Insert → Scale Bar
2. For custom graphics: Insert → Picture
3. For style packages: Add to project styles
4. Select from style gallery

---

## Custom Symbols

**Location:** `./symbols/`

Custom point, line, and polygon symbols for Quinhagak-specific features.

### Symbol Categories

#### Infrastructure Symbols
- Water treatment facilities
- Sewer infrastructure
- Power lines/utilities
- Community buildings
- Traditional structures

#### Cultural Symbols
- Fish camps
- Subsistence areas
- Traditional place markers
- Archaeological sites
- Cultural landmarks

#### Environmental Symbols
- Erosion features
- Vegetation types
- Water bodies
- Wildlife habitat
- Hazard areas

### File Formats

- **PNG** - Raster symbols (300 DPI, transparent)
- **SVG** - Vector symbols
- **EMF** - Windows Enhanced Metafile
- **STYLX** - ArcGIS Pro style package
- **STYLE** - ArcGIS Desktop style file

### Naming Convention

```
symbol_[category]_[feature]_[size].[format]

Examples:
symbol_infrastructure_water_treatment_24px.png
symbol_cultural_fish_camp_medium.svg
symbol_environmental_erosion_area.emf
```

### Creating Symbol Packages

For ArcGIS Pro:

1. **Add symbols to project:**
   - Catalog → Project → Styles
   - Right-click → New Style
   - Name it (e.g., "Quinhagak_Symbols")

2. **Import symbols:**
   - Right-click style → Add Symbol
   - Browse to PNG/SVG files
   - Set category and tags

3. **Package for sharing:**
   - Right-click style → Share As → Style Package
   - Save to this directory

4. **Use in other projects:**
   - Add style package to project
   - Symbols appear in symbology pane

---

## Logos and Branding

**Location:** `./logos/`

Official logos and emblems for map attribution and branding.

### What to Include

**Organizations:**
- Qanirtuuq Incorporated logo
- Nalaquq (GIS department) logo
- Village/tribal logos
- Partner organization logos (with permission)

**File formats:**
- **PNG** - Transparent background, high resolution
- **SVG** - Vector format
- **AI/EPS** - Source files

### Naming Convention

```
logo_[organization]_[variation].[format]

Examples:
logo_qanirtuuq_full_color.png
logo_qanirtuuq_black_white.svg
logo_nalaquq_horizontal.png
logo_nalaquq_stacked.ai
```

### Logo Variations

**Color modes:**
- Full color (for color maps)
- Black and white (for printing)
- Grayscale (for photocopies)
- Reverse (white on dark backgrounds)

**Layouts:**
- Horizontal
- Stacked/vertical
- Icon only
- Text only

### Usage Guidelines

**Placement:**
- Bottom right corner (typical)
- Outside map frame
- Consistent size across map series
- Clear space around logo (equal to logo height)

**Size:**
- Large enough to be legible
- Not dominating the map
- Proportional to page size

**Attribution text:**
```
Prepared by: Nalaquq GIS Team
Qanirtuuq Incorporated
Quinhagak, Alaska
[Date]
```

---

## Map Templates

**Location:** `./templates/`

Pre-configured map layouts for common map types.

### Template Types

#### 1. Standard Map Templates

**Portrait layouts:**
- Letter (8.5" × 11")
- Legal (8.5" × 14")
- Tabloid (11" × 17")
- A4 (210mm × 297mm)

**Landscape layouts:**
- Letter landscape
- Legal landscape
- Tabloid landscape
- A3 (297mm × 420mm)

#### 2. Special Purpose Templates

**Community presentation:**
- Large title
- Simplified design
- Minimal text
- Clear symbols

**Technical/engineering:**
- Grid references
- Detailed scale
- Coordinate information
- Data tables

**Funding applications:**
- Professional appearance
- Complete attribution
- Multiple maps on one page
- Comparison layouts

**Emergency response:**
- High contrast
- Large labels
- Critical info highlighted
- Standardized symbols

### Template Contents

Each template should include:
- **Title block** - Positioned, styled
- **Legend area** - Sized appropriately
- **Scale bar** - Positioned
- **North arrow** - Positioned
- **Attribution block** - Organization, date, sources
- **Logo placement** - Sized and positioned
- **Map frame** - Sized with margins
- **Coordinate grid** (optional)

### Naming Convention

```
template_[purpose]_[size]_[orientation].[format]

Examples:
template_standard_letter_portrait.aprx
template_presentation_tabloid_landscape.aprx
template_technical_11x17_landscape.pagx
template_emergency_a3_landscape.aprx
```

### Using Templates in ArcGIS Pro

1. **Open template:**
   - File → Open → Browse to template
   - Or: Catalog → Project → Layout → Import

2. **Save as new project:**
   - File → Save As
   - New name for your specific map

3. **Replace data sources:**
   - Update map layers with your data
   - Adjust symbology as needed
   - Update title and metadata

### Creating Your Own Templates

1. **Start with blank layout:**
   - Insert → New Layout
   - Choose page size

2. **Add all standard elements:**
   - Map frame
   - Title (styled text)
   - Legend
   - Scale bar
   - North arrow
   - Logo
   - Attribution text box

3. **Save as template:**
   - File → Save As
   - Use template naming convention
   - Add to this directory

---

## File Format Guidelines

### Vector vs. Raster

**Use vector (SVG, EMF, AI) when:**
- Need to scale to different sizes
- Creating symbols for different map scales
- Want crisp edges at any zoom
- Creating north arrows or simple graphics

**Use raster (PNG) when:**
- Complex images or photos
- Specific size/resolution known
- Web map compatibility needed
- File size is a concern

### Resolution Standards

**For print:**
- 300 DPI minimum
- 600 DPI for fine details
- Vector preferred

**For screen/web:**
- 96-150 DPI sufficient
- PNG or SVG
- Optimize file size

### Transparent Backgrounds

**Always use transparent backgrounds for:**
- North arrows
- Symbols
- Logos
- Any element overlaying a map

**File formats supporting transparency:**
- PNG (raster)
- SVG (vector)
- GIF (limited colors)
- TIFF with alpha channel

---

## Color Considerations

### Print vs. Screen

**For print maps:**
- Use CMYK color mode
- Test print on actual printer
- Consider grayscale photocopying
- Provide black/white alternative

**For screen maps:**
- RGB color mode
- Test on different displays
- Consider colorblind-friendly palettes
- Ensure sufficient contrast

### Cultural Color Considerations

**Alaska Native color palettes:**
- Earth tones (browns, tans, greens)
- Ocean/water colors (blues, teals)
- Traditional art colors (red, black, white)
- Natural material colors

**Symbolic meanings:**
- Research cultural color associations
- Consult with community members
- Be respectful of traditional uses

---

## Adding New Assets

### Workflow

1. **Create the asset:**
   - Use appropriate software (Illustrator, Inkscape, etc.)
   - Follow design guidelines
   - Export in multiple formats

2. **Name the file:**
   - Use naming convention
   - Be descriptive
   - Include size/variant info

3. **Save to appropriate folder:**
   - North arrows → ./north-arrows/
   - Scale bars → ./scale-bars/
   - Symbols → ./symbols/
   - Logos → ./logos/
   - Templates → ./templates/

4. **Document the asset:**
   - Add entry to this README
   - Note intended use
   - Include any special instructions

5. **Test the asset:**
   - Import into ArcGIS Pro
   - Verify appearance at different scales
   - Check file compatibility

### Quality Control Checklist

Before adding an asset:
- [ ] File named correctly
- [ ] Appropriate format(s) provided
- [ ] Sufficient resolution/quality
- [ ] Transparent background (if applicable)
- [ ] Tested in ArcGIS Pro
- [ ] Documented in README
- [ ] Source file saved (if applicable)
- [ ] Multiple size options (if needed)

---

## Using Assets in Your Maps

### In ArcGIS Pro

**North Arrows:**
1. Layout view → Insert → North Arrow
2. Click "Browse" button
3. Navigate to `north-arrows/` folder
4. Select your asset → OK
5. Position and size on layout

**Scale Bars:**
1. Layout view → Insert → Scale Bar
2. For graphics: Insert → Picture instead
3. Browse to `scale-bars/` folder
4. Position and adjust

**Symbols:**
1. Add style package to project
2. Layer properties → Symbology
3. Gallery → Your custom style
4. Select symbol

**Logos:**
1. Layout view → Insert → Picture
2. Browse to `logos/` folder
3. Position in corner
4. Resize proportionally

**Templates:**
1. File → Open
2. Browse to `templates/` folder
3. Open template project
4. Save As with new name

### In ArcGIS Online

**Note:** ArcGIS Online has more limited custom asset support

**Workarounds:**
1. Upload assets as content items
2. Get shareable URLs
3. Reference in web maps
4. Or: Create in ArcGIS Pro, export to PDF

---

## Asset Library Best Practices

### Organization

- **Group related assets** - Keep all variations together
- **Clear naming** - Immediately understand what the file is
- **Version control** - Keep old versions with "_v1", "_v2" suffix
- **Source files** - Always save original editable files

### Documentation

For each asset category, document:
- **Purpose** - What is it for?
- **Usage** - How to apply it?
- **Variations** - What options exist?
- **Notes** - Any special considerations

### Maintenance

- **Regular review** - Remove outdated assets
- **Update check** - Ensure compatibility with current ArcGIS version
- **Backup** - Keep copies in multiple locations
- **Share** - Make available to all GIS team members

---

## Design Resources

### Creating Custom North Arrows

**Design principles:**
- Simple is better
- Must be readable at small sizes
- Clear directional indicator
- Appropriate for map type and audience

**Tools:**
- Adobe Illustrator
- Inkscape (free)
- ArcGIS Pro (draw directly)
- Online generators

**Tutorials:**
- [Creating Custom North Arrows in Illustrator](https://www.esri.com/arcgis-blog/)
- [Inkscape for GIS Graphics](https://www.qgis.org/)

### Creating Custom Symbols

**Symbol design:**
- Clear and recognizable
- Scales well
- Distinct from other symbols
- Culturally appropriate

**Symbol size guidelines:**
- Small: 12-16 pixels
- Medium: 24-32 pixels
- Large: 48-64 pixels

### Creating Map Templates

**Layout principles:**
- Consistent margins
- Logical element placement
- Adequate white space
- Standard font sizes
- Professional appearance

**Element placement hierarchy:**
1. Map frame (largest element)
2. Title (prominent)
3. Legend (near map)
4. Scale/north arrow (corner)
5. Attribution (small, bottom)

---

## Current Assets Inventory

*Update this section as you add assets to the directories*

### North Arrows

**Available:**
- (Add descriptions as files are added)

**Needed:**
- Simple modern north arrow (small, medium, large)
- Yup'ik cultural design north arrow
- Minimal technical north arrow
- Decorative community presentation north arrow

### Scale Bars

**Available:**
- (Add descriptions as files are added)

**Needed:**
- US Survey Feet scale (graduated)
- Metric scale (meters/kilometers)
- Dual unit scale bar
- Simple scale bar (minimal design)

### Custom Symbols

**Available:**
- (Add descriptions as files are added)

**Needed:**
- Fish camp symbol
- Water treatment facility icon
- Traditional structure marker
- Erosion area symbol
- Subsistence resource markers

### Logos

**Available:**
- (Add descriptions as files are added)

**Needed:**
- Qanirtuuq Incorporated (all variations)
- Nalaquq GIS department logo
- Partnership logos (with permission)

### Templates

**Available:**
- (Add descriptions as files are added)

**Needed:**
- Standard letter portrait template
- Tabloid landscape template
- Community presentation template
- Technical map template

---

## Permissions and Usage Rights

### Internal Use
All assets in this directory are for:
- Qanirtuuq Incorporated projects
- Nalaquq GIS team maps
- Quinhagak community planning
- Training and educational purposes

### External Sharing
Before sharing assets externally:
- [ ] Verify copyright/ownership
- [ ] Get appropriate permissions
- [ ] Include attribution requirements
- [ ] Document any restrictions

### Logo Usage
**Important:** Organization logos have specific usage guidelines
- Obtain logo files officially from each organization
- Follow brand guidelines
- Maintain required clear space
- Don't alter colors or proportions
- Get approval for public-facing maps

---

## Questions and Support

**Need help with:**
- Creating custom assets → Contact GIS team lead
- Design guidelines → Review ESRI cartography resources
- File format issues → Check ArcGIS Pro documentation
- Logo permissions → Contact organization communications office

---

## Additional Resources

### Design Tools

**Free/Open Source:**
- [Inkscape](https://inkscape.org/) - Vector graphics editor
- [GIMP](https://www.gimp.org/) - Image editor
- [QGIS](https://qgis.org/) - Open source GIS

**Commercial:**
- Adobe Illustrator - Industry standard vector graphics
- Adobe Photoshop - Image editing
- CorelDRAW - Vector graphics alternative

### Cartographic Resources

- [ESRI Cartography Guide](https://www.esri.com/en-us/arcgis/products/arcgis-online/resources/cartographic-design)
- [ColorBrewer](https://colorbrewer2.org/) - Color scheme designer
- [Map Symbol Libraries](https://www.esri.com/en-us/arcgis/products/mapping/symbols)

### Alaska-Specific Resources

- [Alaska Native Art Styles](https://www.alaskool.org/projects/traditionalart/)
- [Alaska Geographic Alliance](https://www.alaskageographic.org/)

---

**Last Updated:** November 2025
**Maintainer:** Nalaquq GIS Team
**Contact:** [Insert contact information]
