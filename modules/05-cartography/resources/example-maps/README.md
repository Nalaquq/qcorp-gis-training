# Example Maps of Quinhagak

This directory contains example maps created in past projects that serve as references for students learning cartography principles.

---

## Purpose

These example maps demonstrate:
- Professional cartographic design
- Effective use of map elements
- Clear communication of spatial information
- Different map types and purposes
- Real-world applications in Quinhagak

Students should review these examples before creating their own maps to understand:
- What makes an effective map
- How to organize information visually
- Appropriate use of symbols and colors
- Professional map layout and composition

---

## Map Categories

### Infrastructure & Planning Maps
Place infrastructure planning maps, utility maps, and development plans here.

**Examples:**
- Village layout maps
- Utility system maps
- Infrastructure planning documents
- Site selection maps

### Environmental & Resource Maps
Place environmental monitoring, erosion documentation, and natural resource maps here.

**Examples:**
- Coastal erosion maps
- Habitat maps
- Subsistence resource areas
- Water body mapping

### Emergency & Damage Assessment Maps
Place disaster response, damage assessment, and emergency planning maps here.

**Examples:**
- Typhoon damage assessment maps
- Flood extent maps
- Evacuation route maps
- Emergency response maps

### Community & Cultural Maps
Place community planning, cultural resource, and general reference maps here.

**Examples:**
- Community facility maps
- Traditional place names
- Historical site documentation
- General community reference maps

---

## File Naming Convention

Use clear, descriptive file names that include:
- **Subject matter** - What the map shows
- **Date** - When created or data date
- **Version** (if applicable)

**Good examples:**
```
quinhagak_infrastructure_2024.pdf
coastal_erosion_assessment_sept2022.pdf
merbok_damage_map_v2_2022.pdf
village_relocation_planning_2025.pdf
sewer_system_layout_2023.pdf
```

**Avoid:**
```
map1.pdf
untitled.pdf
final_final_v3.pdf
```

---

## File Formats

**Recommended formats:**
- **PDF** - Best for finished maps (preserve layout and quality)
- **PNG** - Good for images, web use (300+ DPI recommended)
- **JPG** - Acceptable for photos, not ideal for maps with text
- **TIFF** - High quality, large files

**Source files:**
- Keep ArcGIS Pro project files (.aprx) in a separate location
- PDFs should be the primary reference format here

---

## Using Example Maps in Training

### In Lessons
Reference example maps in lesson documents like this:

```markdown
See this example of an effective infrastructure map:
![Village Planning Map](../resources/example-maps/village_planning_2024.pdf)
```

### In Activities
Point students to relevant examples:

```markdown
**Before you start:**
Review these example maps to see what a professional damage assessment map looks like:
- [Typhoon Merbok Damage Assessment](../resources/example-maps/merbok_damage_2022.pdf)
- [Coastal Erosion Map](../resources/example-maps/coastal_erosion_2023.pdf)

**What to notice:**
- Clear title and date
- Complete legend
- Appropriate symbols
- Professional layout
- Data sources cited
```

### In README
Highlight best examples in the main module README:

```markdown
## 📋 Example Maps

Review professional maps created for Quinhagak projects:
- [Village Relocation Planning Map](./resources/example-maps/relocation_planning_2025.pdf)
- [Typhoon Damage Assessment](./resources/example-maps/typhoon_damage_2022.pdf)
- [Infrastructure System Map](./resources/example-maps/infrastructure_2024.pdf)
```

---

## Map Quality Checklist

When selecting maps to include as examples, ensure they have:

### Required Elements
- [ ] Clear, descriptive title
- [ ] Complete legend
- [ ] Scale bar with units
- [ ] North arrow
- [ ] Data sources and dates
- [ ] Author/organization
- [ ] Creation date

### Design Quality
- [ ] Appropriate symbolization
- [ ] Readable text (all sizes)
- [ ] Effective color choices
- [ ] Clear visual hierarchy
- [ ] Professional layout
- [ ] Proper balance and composition

### Technical Accuracy
- [ ] Correct geographic information
- [ ] Accurate feature placement
- [ ] Appropriate projection
- [ ] Correct attribute information
- [ ] Proper scale

---

## Adding New Maps

To add a new example map:

1. **Prepare the file:**
   - Export at high resolution (300 DPI minimum for PDFs)
   - Use descriptive file name
   - Ensure all map elements are included

2. **Add the file:**
   ```bash
   cp your_map.pdf /path/to/module/resources/example-maps/
   ```

3. **Document the map:**
   - Add entry to this README in appropriate category
   - Note what makes it a good example
   - Include any special context

4. **Reference in lessons/activities:**
   - Update relevant lesson documents
   - Add to activity instructions where appropriate
   - Update main module README if it's a key example

---

## Current Example Maps

*Add descriptions of maps as you add them to this directory*

### Infrastructure Maps

**[Example: Village Planning Map](./village_planning_2024.pdf)** *(Add when available)*
- Shows proposed infrastructure layout
- Demonstrates effective use of different line styles for utilities
- Good example of clear labeling and legend organization

### Damage Assessment Maps

**[Example: Typhoon Merbok Damage](./merbok_damage_2022.pdf)** *(Add when available)*
- Documents storm damage locations
- Shows effective use of point symbols for different damage types
- Good example of context layers (basemap, infrastructure)

### Resource Maps

**[Example: Coastal Erosion Monitoring](./coastal_erosion_2023.pdf)** *(Add when available)*
- Shows erosion extent over time
- Demonstrates effective use of polygons
- Good example of before/after comparison

---

## Credits and Permissions

**Created by:** Qanirtuuq Incorporated / Nalaquq GIS Team
**Training Program:** Yup'ik GIS Technician Training
**Use:** Educational purposes for GIS training

**Note:** Some maps may contain sensitive information. Review before sharing outside the training program. Coordinate with Qanirtuuq Inc. and tribal leadership before public distribution.

---

## Questions?

Contact the training team if you need:
- Help finding specific example maps
- Assistance preparing maps for inclusion
- Guidance on referencing maps in lessons
- Clarification on what makes a good example

---

**Last Updated:** November 2025
**Maintainer:** Nalaquq Training Team
