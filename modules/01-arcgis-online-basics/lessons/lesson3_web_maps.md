# Lesson 3: Creating Web Maps

**Module:** 01 - ArcGIS Online Basics  
**Duration:** 45 minutes  
**Difficulty:** Beginner  
**Prerequisites:** Lessons 1 & 2 completed

---

## Learning Objectives

By the end of this lesson, you will be able to:

1. Understand what web maps are and how they differ from paper maps
2. Create a new web map in Map Viewer
3. Add and manage map layers
4. Choose appropriate basemaps for Alaska
5. Style and symbolize features
6. Add bookmarks and notes
7. Save and share your web map
8. Publish maps for specific audiences

---

## What is a Web Map?

### Definition

A **web map** is an interactive map you can view in a web browser. Unlike paper maps:
- ✅ Viewers can zoom in and out
- ✅ Turn layers on and off
- ✅ Click features for more information
- ✅ Share via URL (link)
- ✅ Embed in websites or emails
- ✅ Update content anytime

### Why Create Web Maps?

**For Land Management:**
- Show infrastructure locations to stakeholders
- Share project plans with community
- Document conditions before/after events
- Support grant applications with visual evidence
- Provide context for reports and presentations

**Advantages over Paper:**
- Always accessible (no need to print/mail)
- Always current (update anytime)
- Interactive (viewers explore themselves)
- Shareable (send a link)
- Professional appearance

---

## Map Viewer Interface

### Opening Map Viewer

**Three ways to start:**

1. From **Home page:** Click "Map" button
2. From **Content:** Click "Create" → "Map"
3. Direct URL: https://arcgis.com/home/webmap/viewer.html

### Interface Tour

**Top Toolbar:**
- **Save** - Save your work
- **Share** - Get shareable link
- **Basemap** - Change background map
- **Add** - Add layers and data
- **Analysis** - Spatial analysis tools (advanced)
- **More options** - Additional settings

**Left Panel:**
- **Contents** - List of layers in your map
- **Legend** - Symbology key
- **Layer settings** - Configure each layer

**Map Canvas (Center):**
- Your actual map
- Zoom in/out with scroll or +/- buttons
- Pan by clicking and dragging

**Search Bar (Top):**
- Find places
- Search for data
- Add layers from ArcGIS Online

---

## Creating Your First Web Map

### Step 1: Start a New Map

1. Sign in to ArcGIS Online
2. Click **Map** button (top toolbar)
3. Map Viewer opens with default view

### Step 2: Navigate to Quinhagak

**Using Search:**
1. Click **Search bar** (top)
2. Type: `Quinhagak, Alaska`
3. Select from results
4. Map zooms to location

**Manual Navigation:**
1. Use scroll wheel to zoom out
2. Click and drag to pan
3. Navigate to southwestern Alaska
4. Zoom in on Quinhagak

**Pro Tip:** Set an appropriate zoom level - not too far out, not too close in. You want to show context but also detail.

### Step 3: Choose a Basemap

**What's a Basemap?**
- Background layer showing general geography
- Provides context for your data
- Different basemaps for different purposes

**Click "Basemap" button and choose:**

**For Quinhagak area, good options:**
- **Imagery** - Aerial/satellite photos (shows actual landscape)
- **Streets** - Road network and labels (if navigation matters)
- **Topographic** - Shows terrain and elevation
- **Light Gray Canvas** - Neutral background (data stands out)

**Try several** - See which works best for your purpose

### Step 4: Save Your Map

**Important: Save frequently!**

1. Click **Save** → **Save As**
2. **Title:** Give it a descriptive name
   - Example: "Quinhagak Infrastructure Map"
3. **Tags:** Add keywords
   - Example: Quinhagak, infrastructure, 2025
4. **Summary:** Brief description
   - Example: "Map showing key infrastructure locations in Quinhagak"
5. **Folder:** Select "GIS Training 2025"
6. Click **Save Map**

**Your map now appears in:** Content → My Content → GIS Training 2025

---

## Adding Layers to Your Map

### What are Layers?

**Layers** = Different types of information stacked on your map

Think of them like transparencies:
- Basemap (bottom layer - background)
- Roads layer (on top of basemap)
- Buildings layer (on top of roads)
- Labels layer (on top of everything)

### Method 1: Add from ArcGIS Online

1. Click **Add** button (top toolbar)
2. Select **Search for Layers**
3. In search box, try:
   - "Alaska villages"
   - "Alaska infrastructure"
   - "Yukon-Kuskokwim"
4. Browse results
5. Click **+** (plus) next to layer to add

**Practice:** Add a layer showing Alaska villages

### Method 2: Add URL

If you have a feature service URL:
1. Click **Add** → **Add Layer from URL**
2. Paste URL
3. Click **Add Layer**

### Method 3: Add File

Add your own data:
1. Click **Add** → **Add Layer from File**
2. Supported formats: Shapefile (zipped), CSV, KML, GPX, GeoJSON
3. Select file
4. Configure settings
5. Click **Import**

---

## Managing Layers

### Layer List (Left Panel)

**Each layer has controls:**
- **Eye icon** - Show/hide layer
- **More options (...)** - Additional settings
- **Drag** - Reorder layers (top = on top of map)

### Common Layer Operations

**Rename a Layer:**
1. Click **... (More options)**
2. Select **Rename**
3. Type new name
4. Press Enter

**Remove a Layer:**
1. Click **... (More options)**
2. Select **Remove**

**Zoom to Layer:**
1. Click **... (More options)**
2. Select **Zoom to**
3. Map zooms to show full extent of layer

**Adjust Transparency:**
1. Click **... (More options)**
2. Select **Transparency**
3. Drag slider (0% = opaque, 100% = invisible)

**Best Practice:** Keep layer names clear and descriptive

---

## Styling and Symbolizing

### Why Style Matters

**Good styling:**
- Makes maps easy to understand
- Highlights important information
- Looks professional
- Guides viewer's attention

### Basic Styling

**Change Layer Style:**
1. Select your layer
2. Click **Change Style** button
3. Choose attribute to show
4. Select style type:
   - **Location only** - All same symbol
   - **Counts and Amounts** - Size by numbers
   - **Types (Unique symbols)** - Different symbols per category

**Example: Color by Type**
If you have building types:
1. Choose "Type" attribute
2. Select "Types (Unique symbols)"
3. Each building type gets different color

### Symbol Options

**Change Symbol:**
1. Click the symbol
2. Choose from gallery, OR
3. Upload custom symbol
4. Adjust size, color, outline

**For Points:**
- Shape (circle, square, pin, etc.)
- Color
- Size (in pixels)
- Outline color and width

**For Lines:**
- Color
- Width
- Line style (solid, dashed, dotted)

**For Polygons:**
- Fill color
- Outline color
- Outline width
- Fill pattern (solid, hatched, etc.)

---

## Adding Information

### Pop-ups

**What are Pop-ups?**
When someone clicks a feature, a pop-up window shows information.

**Configure Pop-ups:**
1. Select layer
2. Click **Configure Pop-up**
3. Choose fields to display
4. Format the display:
   - Title
   - Fields list
   - Custom HTML (advanced)
5. Test by clicking feature on map

**Best Practice:**
- Show relevant information only
- Use clear field names
- Include photos if available
- Format for readability

### Bookmarks

**Save specific views:**

1. Zoom to location you want to save
2. Click **Bookmarks** (in map toolbar)
3. Click **Add Bookmark**
4. Name it: "Gravel Pits" or "Village Center"
5. Click **Add**

**Use bookmarks:**
- Quickly jump to saved views
- Help viewers navigate your map
- Useful for large project areas

### Notes

**Add text annotations:**

1. Click **Add** → **Add Map Notes**
2. Choose symbol type
3. Click on map where you want note
4. Type your text
5. Style the symbol/text

**Use for:**
- Labeling areas
- Adding context
- Marking points of interest
- Highlighting changes

---

## Practical Exercise: Build Infrastructure Map

### Task

Create a map showing Quinhagak infrastructure for a grant application.

**Requirements:**
1. Centered on Quinhagak village
2. Imagery basemap
3. At least one layer showing infrastructure
4. Styled appropriately
5. Pop-ups configured
6. Bookmarks for key areas
7. Saved with descriptive title

**Time:** 20 minutes

**Steps:**
1. Create new map
2. Navigate to Quinhagak
3. Select Imagery basemap
4. Add infrastructure layer (search or create)
5. Style buildings/features
6. Configure pop-ups with key information
7. Add 2-3 bookmarks
8. Save map with good title and description

---

## Sharing Your Web Map

### Sharing Options

**Private (default):**
- Only you can see it
- Good for work in progress

**Organization:**
- Anyone in Qanirtuuq/Nalaquq org
- Most common for internal work

**Everyone (Public):**
- Anyone on internet can view
- Use for public-facing content
- **Be careful with sensitive info!**

**Groups:**
- Share with specific groups only
- Good for projects with defined stakeholders

### How to Share

1. Click **Share** button (top right)
2. Select sharing level
3. **Get shareable link:**
   - Copy URL
   - Send via email
   - Embed in website
4. Click **OK**

**Important:** Check what you're sharing!
- Are all layers appropriate for this audience?
- Is there any sensitive data?
- Are permissions set correctly?

---

## Publishing for Different Audiences

### For Community Members

**Considerations:**
- Simple, clear design
- Not too much information
- Labels in both Yup'ik and English
- Focus on what matters to community
- Mobile-friendly (many view on phones)

**Best practices:**
- Large, clear symbols
- Readable text sizes
- Familiar landmarks for orientation
- Cultural sensitivity in naming

### For Technical Partners/Agencies

**Considerations:**
- More detail acceptable
- Technical terms okay
- Data accuracy critical
- Metadata important
- Professional appearance

**Best practices:**
- Include data sources
- Show accuracy/quality
- Proper symbology
- Clear legend
- Citation information

### For Grant Applications

**Considerations:**
- Clear visual impact
- Shows need or opportunity
- Professional quality
- Print-ready if needed
- Supporting narrative in pop-ups

**Best practices:**
- High contrast for printing
- Clear title and labels
- North arrow and scale bar
- Legend included
- Export as PDF option

---

## Tips for Effective Web Maps

### Design Principles

**Keep It Simple:**
- Don't add every possible layer
- Focus on your message
- 3-5 layers maximum (usually)

**Use Color Wisely:**
- High contrast for important features
- Color-blind friendly palettes
- Consistent color meaning

**Label Appropriately:**
- Not too many labels (cluttered)
- Not too few (confusing)
- Clear, readable fonts
- Both languages when possible

**Think Mobile:**
- Many viewers use phones/tablets
- Large, tappable features
- Readable text sizes
- Simple navigation

### Common Mistakes to Avoid

**Don't:**
- ❌ Use too many bright colors
- ❌ Clutter with unnecessary data
- ❌ Forget to test your links
- ❌ Share private/sensitive data publicly
- ❌ Use jargon in public-facing maps
- ❌ Ignore pop-up configuration
- ❌ Forget to save your work!

---

## Troubleshooting

### Issue: Layer Won't Add

**Solutions:**
- Check internet connection
- Verify layer is compatible
- Try refreshing browser
- Check if layer requires authentication
- Try adding from different source

### Issue: Symbols Don't Look Right

**Solutions:**
- Zoom to appropriate level
- Check layer order (may be hidden)
- Verify styling applied correctly
- Clear browser cache
- Try different browser

### Issue: Pop-ups Are Empty

**Solutions:**
- Verify layer has attribute data
- Check pop-up configuration
- Enable pop-ups for that layer
- Refresh map

### Issue: Can't Share Map

**Solutions:**
- Save map first
- Check your permissions
- Verify organization allows sharing
- Check item sharing settings

---

## Practice Assignment

Before next lesson:

1. **Create a "My Quinhagak" map**
   - Show places important to you
   - Use appropriate basemap
   - Add at least 3 features or areas
   - Style meaningfully
   - Configure pop-ups
   - Share with training group

2. **Document your process**
   - Screenshot of final map
   - List layers used
   - Description of styling choices
   - Share URL

---

## Resources

### Official Documentation
- [Create a Web Map Tutorial](https://developers.arcgis.com/documentation/mapping-and-location-services/mapping/tutorials/tools/create-a-web-map/)
- [Map Viewer Documentation](https://doc.arcgis.com/en/arcgis-online/create-maps/make-your-first-map.htm)
- [Style Features Guide](https://doc.arcgis.com/en/arcgis-online/create-maps/change-style.htm)

### Video Tutorials
- [📹 Your First Web Map](../videos/06-first-map.md) (18 min)
- [📹 Styling Features](../videos/06b-styling.md) (12 min)

### Quick Reference
- [📄 Basemap Selection Guide](../resources/basemap-guide.pdf)
- [📄 Color Scheme Best Practices](../resources/color-schemes.pdf)

---

## Summary

### Key Takeaways

1. **Web maps** are interactive, shareable, and updatable
2. **Map Viewer** is your main tool for creating maps
3. **Basemaps** provide context - choose wisely
4. **Layers** stack to show different information
5. **Styling** makes maps clear and professional
6. **Pop-ups** provide detailed information
7. **Sharing** can be private, organizational, or public

### What's Next

In the next lesson, we'll learn how to:
- Create Story Maps
- Combine narrative with maps
- Add multimedia content
- Publish stories for community audiences

---

**Lesson complete!** Practice creating maps before moving forward.

---

**Version:** 1.0  
**Last Updated:** October 2025  
**Estimated Time:** 45 minutes + 30 minutes practice