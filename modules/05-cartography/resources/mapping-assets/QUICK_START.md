# Mapping Assets - Quick Start Guide

Fast reference for using custom cartographic elements in your maps.

---

## 📂 What's in This Directory?

```
mapping-assets/
├── north-arrows/      Custom north arrow designs (PNG, SVG, EMF)
├── scale-bars/        Custom scale bar styles and graphics
├── symbols/           Point, line, and polygon symbols
├── logos/             Organization logos for map attribution
└── templates/         Pre-configured ArcGIS Pro map layouts
```

---

## 🚀 Quick Usage Guide

### Adding a North Arrow (ArcGIS Pro)

1. **Layout view** → Insert → North Arrow
2. Click **"Browse..."** at bottom of gallery
3. Navigate to: `mapping-assets/north-arrows/`
4. Select your north arrow file
5. Click **OK** and place on map

**Tip:** Use PNG or EMF format for best results

---

### Adding a Scale Bar (ArcGIS Pro)

#### Option 1: Standard scale bar
1. **Layout view** → Insert → Scale Bar
2. Choose style from gallery
3. Properties → Set units (feet/meters)

#### Option 2: Custom graphic scale
1. **Layout view** → Insert → Picture
2. Browse to: `mapping-assets/scale-bars/`
3. Select pre-made scale graphic
4. Place on map

---

### Using Custom Symbols (ArcGIS Pro)

#### Method 1: Add style package
1. **Catalog pane** → Project → Styles
2. Right-click Styles → **Add Style**
3. Browse to: `mapping-assets/symbols/[stylefile.stylx]`
4. Click OK

Symbols now appear in symbology gallery!

#### Method 2: Import individual symbols
1. Layer properties → **Symbology**
2. Click symbol → **Properties**
3. **Layers** → Picture marker
4. Browse to: `mapping-assets/symbols/[symbol.png]`

---

### Adding Organization Logos (ArcGIS Pro)

1. **Layout view** → Insert → Picture
2. Browse to: `mapping-assets/logos/`
3. Select appropriate logo file
4. Place in corner (typically bottom right)
5. Resize proportionally (hold Shift while dragging)

**Standard placement:**
- Bottom right corner
- Outside map frame
- Consistent size across map series

---

### Using Map Templates (ArcGIS Pro)

#### Starting a new map from template:
1. **File** → Open
2. Browse to: `mapping-assets/templates/`
3. Select template (`.aprx` file)
4. **File** → Save As → Give new project name

#### Importing layout from template:
1. Open your current project
2. **Insert** → Import Layout
3. Browse to template `.aprx` or `.pagx` file
4. Layout imports with all elements

---

## 📋 File Format Guide

| Asset Type | Best Format | Notes |
|------------|-------------|-------|
| North Arrows | PNG, EMF, SVG | EMF best for ArcGIS Pro |
| Scale Bars | PNG, SVG | Or use built-in scale bars |
| Symbols | PNG (300 DPI) | 24-64px for best results |
| Logos | PNG (transparent) | High resolution (300+ DPI) |
| Templates | .APRX, .PAGX | ArcGIS Pro project/layout files |

---

## 🎨 Asset Selection Tips

### Choosing North Arrows

**Simple/Minimal** → Technical maps, engineering plans
**Decorative** → Community presentations, public maps
**Cultural designs** → Maps for tribal council, cultural projects

### Choosing Scale Bars

**For village maps:** US Survey Feet
**For regional maps:** Kilometers or miles
**For technical plans:** Dual units (feet and meters)

### Choosing Symbols

**Match symbol to audience:**
- Technical audience → Standard GIS symbols
- Community audience → Recognizable icons
- Cultural context → Culturally appropriate designs

---

## ✅ Common Map Element Checklist

Every professional map should include:

- [ ] **Title** - Clear, descriptive
- [ ] **North Arrow** - From this library (consistent style)
- [ ] **Scale Bar** - Appropriate units
- [ ] **Legend** - All symbols explained
- [ ] **Logo** - Organization branding
- [ ] **Attribution** - Data sources, author, date
- [ ] **Coordinate System** - (If technical map)

---

## 💡 Pro Tips

### Consistent Branding
- Use same north arrow style across map series
- Use same logo placement (bottom right)
- Match fonts and colors project-wide

### File Organization
- Save frequently used assets to ArcGIS Pro favorites
- Create custom style package with all Quinhagak symbols
- Keep master copies of logos in original resolution

### Template Workflow
1. Create template for each common map type
2. Include all standard elements positioned
3. Save in `templates/` directory
4. Start every new map from appropriate template
5. Saves 15-30 minutes per map!

### Symbol Library
- Organize symbols by category (infrastructure, cultural, environmental)
- Use consistent naming convention
- Create thumbnails showing each symbol
- Document meaning of each custom symbol

---

## 🆘 Troubleshooting

**North arrow won't import:**
- Check file format (PNG or EMF work best)
- Verify transparent background
- Try resaving in different format

**Symbol too small/large:**
- In symbol properties, adjust size manually
- For PNG symbols, use different size variation
- For vector symbols (SVG), scale freely

**Logo appears pixelated:**
- Use higher resolution version (300+ DPI)
- Use vector format (SVG, EMF) if available
- Don't enlarge raster images beyond original size

**Template won't open:**
- Check ArcGIS Pro version compatibility
- Try importing layout instead of opening project
- Verify file not corrupted

---

## 📞 Need Help?

**Can't find the asset you need?**
- Check main [README.md](./README.md) for complete inventory
- Request creation of new asset from GIS team
- See design resources section for creating your own

**Technical issues?**
- Review ArcGIS Pro documentation
- Contact GIS team lead
- Check ESRI support forums

---

## 🔗 Related Resources

- [Complete README](./README.md) - Full documentation
- [Example Maps](../example-maps/) - See assets in use
- [Module 5 Lessons](../../lessons/) - Cartography training

---

**Quick Reference Version:** 1.0
**Last Updated:** November 2025
**For:** Quinhagak GIS Training Program
