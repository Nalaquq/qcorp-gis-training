# Lesson 8: Exporting Maps to PDF

**Duration:** 45 minutes
**Prerequisites:** Lessons 1-7 (especially Lesson 7 - Map Elements)
**Training Date Reference:** November 8, 2025

---

## Lesson Overview

This lesson teaches you how to export your web maps to PDF format for printing, presentations, and sharing. You'll learn export settings, how to include map elements, and best practices for creating professional print-ready maps.

---

## Learning Objectives

By the end of this lesson, you will be able to:

1. Access the export/print function in ArcGIS Online
2. Configure page size and orientation
3. Set appropriate resolution for different uses
4. Include map elements (scale bar, north arrow, legend)
5. Export maps to PDF format
6. Create maps suitable for different purposes (print, presentation, reports)
7. Troubleshoot common export issues
8. Optimize file size and quality

---

## Why Export Maps?

### Use Cases

**Printed Maps:**
- Community meetings and presentations
- Field work reference
- Wall displays
- Reports and documentation

**Digital Sharing:**
- Email attachments
- Website downloads
- Grant applications
- Social media (as images)

**Presentations:**
- PowerPoint slides
- Project briefings
- Tribal council meetings
- Public information sessions

**Official Documentation:**
- Permits and applications
- Legal records
- Historical archives
- Emergency response plans

**From Your Work:**
- Typhoon Merbok damage assessment map → Recovery planning meetings
- Village relocation map → Funding applications and community engagement

---

## Accessing the Export Function

### In ArcGIS Online Map Viewer

**Method 1: Print Button**
1. Open your map
2. Click **"Print"** button (printer icon)
3. Print dialog opens

**Method 2: Share Menu**
1. Click "Share" button
2. Select "Print"
3. Print dialog opens

### Print Dialog Overview

**Key Sections:**
- **Layout Options:** Page size, orientation
- **Map Settings:** Scale, extent
- **Format Options:** PDF, PNG, JPG
- **Advanced Options:** Resolution, quality
- **Map Elements:** Which to include

---

## Configuring Page Layout

### Page Size

**Standard Sizes:**

**Letter (8.5" x 11"):**
- Most common
- Standard printer size
- Good for reports, handouts
- Use for: Meeting materials, field maps

**Legal (8.5" x 14"):**
- Taller format
- More room for legends
- Use for: Detailed maps with extensive legends

**Tabloid (11" x 17"):**
- Large format
- Good for detailed maps
- Requires large-format printer
- Use for: Wall maps, detailed site plans

**A4 (210mm x 297mm):**
- International standard
- Similar to Letter
- Use for: International sharing

**Custom:**
- Define your own dimensions
- For specific display needs
- Poster sizes (24" x 36", 36" x 48")

**For Your Maps:**
- Typhoon Merbok Map: Letter or Tabloid (depending on detail needed)
- Relocation Site Map: Tabloid or larger (more detail and complexity)

### Orientation

**Portrait (vertical):**
- Taller than wide
- Good for north-south oriented areas
- More room for title and legend at top/bottom

**Landscape (horizontal):**
- Wider than tall
- Good for east-west oriented areas
- More room for legend on side
- Better for presentations (screen format)

**Choosing Orientation:**
- Match the shape of your area
- Consider where legend will go
- Think about final use (presentation screens are landscape)

**Quinhagak Maps:**
- Consider coastline orientation
- Relocation site layout
- Space needed for legend

---

## Map Scale and Extent

### Setting the Extent

**What Shows in Export:**
- Exactly what's visible in your map view
- Zoom and pan before exporting
- Ensure all important features visible

**Best Practice:**
1. Arrange map view exactly as you want it
2. Include small buffer around area of interest
3. Verify all labels visible
4. Check legend items all included
5. Then export

### Map Scale

**Fixed Scale:**
- Set specific scale (1:24,000, 1:10,000)
- Ensures consistent scale across multiple maps
- Important for technical/engineering uses

**Current Extent:**
- Uses whatever is displayed
- May have odd scale (1:17,843)
- Fine for general use

**For Professional Maps:**
- Use standard scales when possible
- 1:1,200 - Detailed site plans
- 1:2,400 - Site vicinity
- 1:12,000 - Community scale
- 1:24,000 - Regional

**Your Maps:**
- Typhoon Merbok: Scale depends on damage area size
- Relocation Site: Detailed scale (1:2,400 or 1:5,000) to show proposed infrastructure

---

## Including Map Elements

### Essential Map Elements

**Always Include:**
1. **Title**
   - Clear, descriptive
   - "Typhoon Merbok Damage Assessment - Quinhagak, Alaska"
   - "Proposed Village Relocation Site - Quinhagak"

2. **Legend**
   - Shows what symbols mean
   - Auto-generated from visible layers
   - Can customize which layers included

3. **Scale Bar**
   - Shows distance on map
   - Both units (feet and meters, or miles and kilometers)
   - Appropriate size for map scale

4. **North Arrow**
   - Shows map orientation
   - Standard symbol
   - Not needed if map is north-up (but include anyway)

5. **Date**
   - When map created
   - "November 8, 2025"
   - Or "Map Date: 11/8/2025"

6. **Data Source**
   - Where data came from
   - "Source: Qanirtuuq Inc., USGS, Esri"
   - Required for credibility

### Optional Elements

**Depending on Purpose:**
- Author/organization name
- Coordinate grid
- Scale statement (1:24,000)
- Inset maps (location context)
- Disclaimers
- Contact information
- Project information

### Configuring Elements in Export

**In Print Dialog:**

**Title:**
- Enter in "Title" field
- Or include in map itself before export
- Font size and style

**Legend:**
- ☑ Include legend (checkbox)
- Choose which layers to show
- Position (right side, bottom, etc.)
- Size

**Scale Bar:**
- ☑ Include scale bar
- Choose style
- Units (feet, miles, meters, km)
- Position

**North Arrow:**
- ☑ Include north arrow
- Choose style
- Position (typically upper right)

**Date and Attribution:**
- May auto-include based on settings
- Or add to title/description field
- Example title: "Typhoon Merbok Damage Assessment - November 8, 2025"

---

## File Format Options

### PDF (Recommended)

**Advantages:**
- ✅ High quality
- ✅ Vector format (scales well)
- ✅ Small file size
- ✅ Universal compatibility
- ✅ Can include metadata
- ✅ Professional standard

**Use PDF For:**
- Print production
- Official documents
- Email sharing
- Archiving
- Grant applications
- Reports

**Your Maps:**
- Export both maps as PDF
- Suitable for all professional uses

### Other Formats

**PNG (Image):**
- Raster image
- Good for web
- Larger file size than PDF
- Specify resolution (DPI)

**JPG (Image):**
- Compressed image
- Smallest file size
- Some quality loss
- Good for web, email (if size matters)

**SVG (Vector):**
- Scalable vector graphics
- For graphic design software
- Editable after export

**Choose PDF** unless specific reason to use other format.

---

## Resolution Settings

### Understanding DPI

**DPI (Dots Per Inch):**
- How detailed the output is
- Higher DPI = more detail = larger file
- Appropriate DPI depends on use

### Recommended DPI Settings

**Screen Display:**
- **96 DPI** - Good for on-screen viewing
- **150 DPI** - Better quality for screen
- Use for: PowerPoint, website, digital sharing

**Print:**
- **300 DPI** - Standard print quality (recommended)
- **600 DPI** - High quality (large format, posters)
- Use for: Printed materials, professional documents

**Your Maps:**
- **For meetings/presentations:** 150 DPI
- **For printing/official documents:** 300 DPI
- **For posters/displays:** 300-600 DPI

### DPI vs. File Size

Higher DPI = Larger file size

**Example:**
- Letter size, 96 DPI: ~1-2 MB
- Letter size, 300 DPI: ~5-10 MB
- Tabloid, 300 DPI: ~15-20 MB

**Considerations:**
- Email attachments: Keep under 10 MB if possible
- Website downloads: 300 DPI but compress if needed
- Professional printing: 300 DPI uncompressed

---

## Export Process Step-by-Step

### Complete Export Workflow

**1. Prepare Your Map**
- Arrange extent (what shows in view)
- Verify all layers visible and styled
- Check labels readable
- Ensure legend clear
- Zoom to final view

**2. Open Export Dialog**
- Click "Print" button
- Export options appear

**3. Configure Layout**
- **Page size:** Letter, Tabloid, etc.
- **Orientation:** Portrait or Landscape
- **Format:** PDF

**4. Set Map Properties**
- **Title:** Enter descriptive title
- **Scale:** Use current or set specific
- **Extent:** Use current view

**5. Configure Map Elements**
- ☑ Include legend
  - Select which layers
  - Position: Right side
- ☑ Include scale bar
  - Style: Bar with labels
  - Units: Feet and miles (or meters and km)
  - Position: Bottom left
- ☑ Include north arrow
  - Style: Simple compass
  - Position: Upper right

**6. Set Quality**
- **Resolution:** 300 DPI (for print)
- **Quality:** High

**7. Export**
- Click "Export" or "Print"
- Processing begins (may take 30 seconds to 2 minutes)
- Download link appears
- Click to download PDF

**8. Review**
- Open PDF
- Check quality
- Verify all elements present
- Check text readable
- If issues, adjust and re-export

---

## Creating Multiple Versions

### Different Audiences, Different Maps

**For Technical/Planning Use:**
- Detailed, all layers
- Technical terminology
- Precise scale bar
- Coordinate grid
- 300 DPI

**For Community Presentation:**
- Simplified
- Clear labels in plain language
- Larger text
- Essential features only
- 150-300 DPI

**For Funding Application:**
- Professional appearance
- Complete attribution
- High quality (300 DPI)
- Clean, uncluttered
- Official formatting

**Example: Relocation Site Map**

**Version 1 - Technical:**
- All proposed infrastructure
- Detailed dimensions
- Coordinate grid
- Engineering details
- For: Engineers, designers

**Version 2 - Community:**
- Simplified infrastructure
- Clear labels ("New Water Plant", "New Roads")
- Color-coded phases
- Easy to understand
- For: Community meetings

**Version 3 - Funding:**
- Professional layout
- Cost information
- Project phases
- Clean design
- For: Grant applications

---

## Best Practices

### Before Export

**Check List:**
- [ ] Map zoomed to correct extent
- [ ] All important features visible
- [ ] Labels readable (not overlapping)
- [ ] Legend includes all necessary items
- [ ] Basemap appropriate
- [ ] Layers in correct order
- [ ] Styling clear and professional

### During Export

**Settings:**
- Use PDF format for professional use
- 300 DPI for print, 150 for screen
- Include all essential map elements
- Descriptive title
- Appropriate page size for content

### After Export

**Quality Check:**
- Open and review PDF
- Zoom to 100% and check text clarity
- Verify all labels visible
- Check legend complete
- Ensure no cut-off elements
- Test print if intended for printing

### File Naming

**Good File Names:**
- Descriptive
- Include date
- Version number if multiple versions
- No spaces (use underscores)

**Examples:**
- Quinhagak_Typhoon_Merbok_Damage_Map_2025-11-08.pdf
- Quinhagak_Relocation_Site_Plan_Technical_v2.pdf
- Quinhagak_Relocation_Community_Version_2025-11-08.pdf

---

## Troubleshooting

### Common Issues

**Issue: Legend Too Large**
- Solution: Reduce number of layers in legend
- Solution: Shorten layer names
- Solution: Use larger page size

**Issue: Text Too Small**
- Solution: Increase text size in layer styling
- Solution: Use larger page size
- Solution: Zoom in more (but may cut off area)

**Issue: Map Elements Cut Off**
- Solution: Adjust map extent (zoom out slightly)
- Solution: Reposition elements
- Solution: Choose different page orientation

**Issue: File Size Too Large**
- Solution: Reduce DPI (300 → 150)
- Solution: Reduce page size
- Solution: Simplify layers (remove unnecessary detail)
- Solution: Compress PDF after export

**Issue: Poor Quality When Printed**
- Solution: Increase DPI to 300
- Solution: Use vector format (PDF not JPG)
- Solution: Check printer settings

**Issue: Colors Look Different on Screen vs. Print**
- Solution: Use print-safe colors
- Solution: Test print first
- Solution: Avoid very light colors

---

## Exporting for Different Uses

### For Email

**Requirements:**
- File size < 10 MB
- Readable on screen

**Settings:**
- Format: PDF
- DPI: 150
- Page size: Letter
- Compress if needed

### For Printing

**Requirements:**
- High quality
- Correct page size
- Readable text

**Settings:**
- Format: PDF
- DPI: 300
- Page size: Match printer
- Include crop marks if needed

### For Presentations

**Requirements:**
- Landscape orientation
- Screen-readable
- Fast to load

**Settings:**
- Format: PDF or PNG
- DPI: 150
- Page size: Letter landscape
- Or 16:9 aspect ratio for slides

### For Posters

**Requirements:**
- Large format
- High resolution
- Professional quality

**Settings:**
- Format: PDF
- DPI: 300-600
- Page size: 24"x36" or larger
- Vector graphics preferred

---

## Review Questions

1. What file format is recommended for professional map exports?
2. What DPI setting is appropriate for printing?
3. What are the five essential map elements to include?
4. How do you set what area appears in the export?
5. When would you choose landscape vs. portrait orientation?
6. What's the difference between 150 DPI and 300 DPI?
7. How can you reduce file size if the PDF is too large?
8. Why is it useful to create multiple versions of the same map?

---

## Practical Exercise

**Export Practice:**

**Exercise 1: Export Typhoon Merbok Map**
1. Open your Typhoon Merbok damage map
2. Configure export:
   - Page size: Letter
   - Orientation: Choose appropriate
   - Format: PDF
   - DPI: 300
   - Include: Title, legend, scale bar, north arrow, date
3. Export to PDF
4. Review quality
5. File name: Quinhagak_Merbok_Damage_2025-11-08.pdf

**Exercise 2: Export Relocation Site Map**
1. Open village relocation site map
2. Create TWO versions:

   **Version A - Technical:**
   - Tabloid size
   - All infrastructure details
   - 300 DPI
   - File name: Quinhagak_Relocation_Technical_2025-11-08.pdf

   **Version B - Community:**
   - Letter size
   - Simplified labels
   - 150 DPI
   - File name: Quinhagak_Relocation_Community_2025-11-08.pdf

3. Compare the two versions
4. Discuss which is better for which audience

---

## Key Takeaways

- **PDF is the professional standard** for map exports
- **300 DPI for print**, 150 DPI for screen display
- **Include all essential map elements** (title, legend, scale, north arrow, date)
- **Page size should match intended use** (Letter for reports, Tabloid for detail)
- **Always review exports** before sharing or printing
- **Create multiple versions** for different audiences
- **Use descriptive file names** with dates
- **Test print** if map will be printed
- **Larger page size = more room** for detail and legends
- **Quality matters** - take time to configure settings properly

---

## Next Steps

After mastering map export:
- Create print-ready maps for community meetings
- Generate professional maps for grant applications
- Produce field maps for data collection
- Archive important maps as PDFs
- Share maps digitally with stakeholders

---

**Congratulations! You can now create professional maps from start to finish:**
- Create data layers ✅
- Design effective maps ✅
- Export publication-ready PDFs ✅

Time to apply these skills to real community needs!
