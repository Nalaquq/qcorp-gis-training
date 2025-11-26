# Lesson 2: Adding Content from ArcGIS Online

**Duration:** 60 minutes
**Difficulty:** Beginner-Intermediate
**Prerequisites:** Lesson 1 (Projections), Module 1 (ArcGIS Online Basics)

---

## Overview

One of the most powerful features of ArcGIS Pro is the ability to work with layers you've already created in ArcGIS Online. This lesson covers how to search for and add content from AGOL to ArcGIS Pro, including the challenges of public/private sharing and working with hosted data.

You'll learn to add raster imagery, polygon layers, and line layers from your web maps into ArcGIS Pro for advanced analysis. You'll also learn to measure distances and verify imagery resolution.

---

## Learning Objectives

By the end of this lesson, you will be able to:

1. ✅ Search for personal content in ArcGIS Pro
2. ✅ Add content from ArcGIS Online to ArcGIS Pro
3. ✅ Understand public vs private sharing challenges
4. ✅ Download and work with different layer types (raster, polygon, line)
5. ✅ Measure distances on the map
6. ✅ Check imagery resolution through measurement
7. ✅ Troubleshoot common AGOL connectivity issues

---

## Part 1: Understanding ArcGIS Online and ArcGIS Pro Integration

### The Connection Between AGOL and ArcGIS Pro

**ArcGIS Online (AGOL):**
- Web-based mapping platform
- Great for quick maps and sharing
- Mobile-friendly
- Limited analysis capabilities

**ArcGIS Pro:**
- Desktop GIS application
- Advanced analysis tools
- Better performance for large datasets
- Professional cartography
- More complex geoprocessing

**Best Workflow:**
1. Create and organize data in AGOL
2. Download to ArcGIS Pro for analysis
3. Upload results back to AGOL for sharing

### Why Bring AGOL Content into ArcGIS Pro?

**Reasons to use ArcGIS Pro:**
- Perform buffer, intersect, and other spatial analyses
- Work with raster data (adjust HSV, clip extents)
- Create professional map layouts
- Calculate geometry precisely
- Use advanced editing tools
- Work offline with your data

**What You Can Bring In:**
- Layers from your web maps
- Hosted feature layers
- Imagery layers
- Basemaps
- Organizational content
- Public layers

---

## Part 2: Searching for Your Content

### Task 2.1: Sign In to ArcGIS Online

**Before You Start:**
You must be signed in to access your personal content

**Sign In:**
1. Launch ArcGIS Pro
2. Top right corner → Click your profile
3. If not signed in:
   - Click "Sign In"
   - Enter your ArcGIS Online credentials
   - Organizational account for Quinhagak training

**Verify Connection:**
- Profile icon shows your name
- Organization name appears
- You're ready to access content

### Task 2.2: Search Personal Content

**Method 1: Insert Tab → Add Data**

1. **Open Add Data Dialog:**
   - Click "Insert" tab on ribbon
   - Click "Add Data" dropdown
   - Select "Data" or "Data From Path"

2. **Browse to Portal:**
   - In the Add Data window
   - Look for "Portal" or "ArcGIS Online" section
   - Click to expand

3. **My Content:**
   - Click "My Content"
   - See all layers you've created or own
   - Includes layers from web maps

4. **Search:**
   - Type "Quinhagak" in search box
   - Find layers you created in Module 1
   - Filter by content type if needed

**Method 2: Catalog Pane → Portal**

1. **Open Catalog Pane:**
   - View tab → Catalog Pane
   - OR press Ctrl+Alt+C

2. **Navigate to Portal:**
   - Expand "Portal" section
   - Click "My Content"
   - OR click "My Organization"

3. **Browse Your Content:**
   - See folders and layers
   - Right-click any layer → Add to Current Map
   - Drag and drop layers onto map

### Task 2.3: Search Organizational Content

**Access Organization Layers:**

1. In Catalog Pane → Portal
2. Click "My Organization"
3. Search for:
   - Quinhagak layers created by other trainees
   - Shared organizational basemaps
   - Reference layers for Alaska

**Note:** Only shows content that's been shared with your organization

---

## Part 3: The Frustrations of Public/Private Sharing

### Understanding Sharing Permissions

**Common Issue:** You created a layer in AGOL, but can't see it in ArcGIS Pro!

**Why This Happens:**

**Private (Owner Only):**
- Only you can see it when signed in
- Appears in "My Content" but not organizational searches
- Most restrictive

**Shared with Organization:**
- Everyone in your organization can see it
- Appears in "My Organization" searches
- Good for collaborative work

**Public:**
- Anyone on the internet can find it
- Searchable by anyone
- Use carefully - consider data sensitivity

### Troubleshooting Missing Layers

**Problem:** Can't find your Quinhagak web map layers

**Solutions:**

1. **Check Sharing Settings:**
   - Sign in to ArcGIS Online (web browser)
   - Go to Content → My Content
   - Find the layer
   - Click "Share" button
   - Verify sharing level
   - Change to "Organization" or "Public" if needed

2. **Refresh ArcGIS Pro:**
   - Sometimes takes a few minutes to sync
   - Right-click Portal → Refresh
   - Or restart ArcGIS Pro

3. **Check Sign-In:**
   - Verify you're signed in with correct account
   - Try signing out and back in

4. **Search by Different Terms:**
   - Try layer name instead of map name
   - Search by owner name
   - Use tags if you added them

### Hosted Data Challenges

**What is Hosted Data?**
- Data stored on Esri's servers
- Accessed via internet connection
- Not stored on your local computer

**Limitations:**
- Requires internet connection
- Can be slow with large datasets
- May have limits on editing
- Credits consumed for storage/usage

**Solution: Download Locally**
When you need to work offline or improve performance:
1. Right-click layer → Data → Export Features
2. Save to local geodatabase
3. Work with local copy
4. Upload results when done

---

## Part 4: Adding Different Layer Types

### Task 4.1: Add a Raster Layer (Imagery)

**Goal:** Add Quinhagak satellite imagery from your AGOL content

**Steps:**

1. **Find Raster Layer:**
   - Catalog Pane → Portal → My Content
   - Search: "Quinhagak imagery" or similar
   - Look for image service layers

2. **Add to Map:**
   - Right-click layer
   - "Add to Current Map"
   - OR drag and drop

3. **Verify Load:**
   - Layer appears in Contents pane
   - Imagery displays on map
   - May take moment to load (large file)

4. **Zoom to Layer:**
   - Right-click layer in Contents
   - "Zoom to Layer"
   - View full extent

**Common Raster Layers from Quinhagak Project:**
- Georeferenced historical maps
- Recent satellite imagery
- Aerial photography
- Elevation rasters (DEMs)

### Task 4.2: Add a Polygon Layer

**Goal:** Add Quinhagak Parcels layer

**Steps:**

1. **Search for Polygons:**
   - Portal → My Content or My Organization
   - Search: "Quinhagak Parcels" or "Parcels"

2. **Add Layer:**
   - Right-click → Add to Current Map
   - Layer loads faster than raster (vector data)

3. **Inspect Attributes:**
   - Right-click layer → Attribute Table
   - See parcel information
   - Note field names and values

**Other Polygon Layers:**
- Community boundary
- Building footprints
- Land use zones
- Water bodies

### Task 4.3: Add a Line Layer

**Goal:** Add roads, rivers, or trails

**Steps:**

1. **Find Line Layers:**
   - Search: "Quinhagak roads" or "rivers"
   - Line feature services

2. **Add Multiple Layers:**
   - Can add several at once
   - Select multiple (Ctrl+Click)
   - Right-click → Add to Current Map

3. **Organize in Contents:**
   - Drag layers to reorder
   - Group related layers
   - Turn on/off for visibility

**Common Line Layers:**
- Roads and trails
- Rivers and streams
- Utility lines
- Contours

### Task 4.4: Ensure You Have One of Each

**Exercise:** Add these three layer types:
1. ✅ One raster layer (imagery)
2. ✅ One polygon layer (parcels or buildings)
3. ✅ One line layer (roads, rivers, or trails)

**Organize Your Map:**
- Raster on bottom (basemap-like)
- Polygons in middle
- Lines on top
- Points on very top (if you have them)

This layer ordering ensures everything is visible!

---

## Part 5: Measuring Distances

### Why Measure?

**Practical Uses:**
- Verify layer alignment
- Check parcel dimensions
- Measure trail distances
- Calculate distances between features
- Verify coordinate system accuracy

### Task 5.1: Use the Measure Tool

**Access Measure Tool:**
1. Map tab on ribbon
2. Click "Measure" button
3. Measure tool dialog opens

**Measure Tool Options:**

**Distance:**
- Click to start
- Click again to end
- Shows total distance

**Area:**
- Click to create polygon
- Double-click to close
- Shows area and perimeter

**Feature:**
- Click on existing feature
- Shows length or area automatically

**Units:**
- Dropdown menu to change units
- Miles, kilometers, meters, feet
- Choose appropriate for your analysis

### Task 5.2: Measure Known Distances

**Verify Accuracy:**

1. **Find Known Feature:**
   - Building with known dimensions
   - Road segment
   - Runway (if visible)

2. **Measure It:**
   - Use Measure tool
   - Record measurement

3. **Compare to Reality:**
   - Does it match known size?
   - If way off, check coordinate system!
   - Should be reasonably accurate

**Example - Quinhagak School:**
- Measure school building
- Should be approximately 50-100 meters long
- If you get 0.0005 degrees, wrong coordinate system!
- If you get 500+ meters, wrong projection!

---

## Part 6: Checking Imagery Resolution

### Understanding Resolution

**Resolution:** The size of each pixel on the ground

**Common Resolutions:**
- 30m: Landsat satellite (free, global)
- 10m: Sentinel-2 satellite (free, global)
- 2-5m: Commercial satellite (paid)
- 0.3-1m: Aerial photography (high quality)
- 0.05-0.15m: Drone imagery (very high quality)

**Why It Matters:**
- Determines what you can see
- Affects accuracy of digitizing
- Important for project planning

### Task 6.1: Measure to Determine Resolution

**Method: Measure Known Features**

1. **Find Clearly Visible Feature:**
   - Building with known size
   - Vehicle (about 4-5 meters)
   - Road width (about 6-10 meters)

2. **Measure the Feature:**
   - Use Measure tool
   - Record dimension

3. **Look at Pixel Size:**
   - Zoom in very close
   - Can you see individual pixels?
   - How many pixels across the feature?

4. **Calculate Resolution:**
   - Feature width ÷ pixels across = resolution
   - Example: 10m road ÷ 10 pixels = 1m resolution

**Easier Method: Check Metadata**

1. Right-click imagery layer
2. Properties
3. Source tab
4. Look for "Pixel Size" or "Cell Size"
5. Shows resolution directly

### Task 6.2: Assess If Resolution Is Adequate

**Questions to Ask:**

**Can you see what you need?**
- For parcel mapping: Need to see building outlines
- For vegetation: Need to distinguish plant types
- For trails: Need to see trail path

**Resolution Guidelines:**
- Rough analysis: 10-30m okay
- Building mapping: Need 1-2m
- Detailed features: Need 0.3-1m
- Construction/engineering: Need 0.05-0.3m

**Quinhagak Imagery:**
- Check resolution of your layers
- Is it adequate for tracing features?
- May need higher resolution for some tasks

---

## Part 7: Working with Downloaded Content

### Download vs Stream

**Streaming (Default):**
- Data stays on Esri servers
- Loads as you pan/zoom
- Requires internet connection
- May be slower

**Downloaded:**
- Data on your local computer
- Fast performance
- Works offline
- Takes up disk space

### Task 7.1: Export Layer to Local Geodatabase

**When to Download:**
- Working offline
- Large dataset
- Slow internet connection
- Frequent editing

**Steps to Download:**

1. **Right-click Layer:**
   - In Contents pane
   - Select "Data" → "Export Features"

2. **Export Features Tool:**
   - Input Features: Your AGOL layer
   - Output Location: Your project geodatabase
   - Output Name: Descriptive name

3. **Run Tool:**
   - Click Run
   - Tool exports to local geodatabase
   - Adds local copy to map

4. **Remove Streamed Version:**
   - Right-click original AGOL layer
   - Remove
   - Keep local copy in map

**Benefits:**
- ✅ Much faster
- ✅ Works offline
- ✅ No credit usage
- ✅ Can edit freely

---

## Part 8: Organizing Your Layers

### Best Practices

**Layer Ordering:**
1. Points (top)
2. Lines
3. Polygons
4. Rasters (bottom/basemap)

**Grouping:**
- Right-click in Contents → New Group Layer
- Name: "Quinhagak Base Layers" or similar
- Drag related layers into group
- Collapse/expand as needed

**Naming:**
- Rename layers for clarity
- Right-click → Properties → General tab
- Change layer name (doesn't affect data)
- Example: "Parcels" instead of "FeatureLayer_2384"

**Removing:**
- Right-click → Remove
- Only removes from map, doesn't delete data
- Can add back anytime

---

## Part 9: Troubleshooting Common Issues

### Can't Find My Content

**Problem:** Layers don't appear in search

**Solutions:**
1. Check you're signed in with correct account
2. Verify layer is shared appropriately (AGOL settings)
3. Refresh Portal in Catalog Pane
4. Search using exact layer name
5. Check "My Content" vs "My Organization"

### Layer Won't Add

**Problem:** Error when adding layer

**Solutions:**
1. Check internet connection
2. Verify layer hasn't been deleted from AGOL
3. Check if layer is supported type
4. Try restarting ArcGIS Pro
5. Export and add local copy instead

### Layer Loads Very Slowly

**Problem:** Hosted layer is sluggish

**Solutions:**
1. Export to local geodatabase
2. Simplify geometry if possible
3. Check internet connection speed
4. Work at larger scale (zoomed in)

### Layer in Wrong Location

**Problem:** Layer appears in ocean or wrong place

**Solutions:**
1. Check coordinate system
2. Map properties → Coordinate System
3. Layer properties → Source tab → check spatial reference
4. May need to reproject layer

### Can't Edit Hosted Layer

**Problem:** Edit options grayed out

**Solutions:**
1. Export to local geodatabase for full editing
2. Check if you have edit permissions in AGOL
3. Verify layer allows editing (some are read-only)
4. Make sure edit session is started

---

## Part 10: Practice Exercise

### Exercise: Build Your Quinhagak Workspace

**Goal:** Add all your Quinhagak web map content to ArcGIS Pro

**Tasks:**

1. **Sign in to ArcGIS Pro**
   - Verify connection to AGOL

2. **Add Raster Layer**
   - Find Quinhagak imagery
   - Add to map
   - Measure to verify resolution

3. **Add Polygon Layer**
   - Add Quinhagak Parcels
   - Open attribute table
   - Explore data

4. **Add Line Layer**
   - Add roads, rivers, or trails
   - Verify layer loads correctly

5. **Measure Distance**
   - Measure a known feature
   - Verify accuracy
   - Try different units

6. **Export One Layer**
   - Choose one layer
   - Export to local geodatabase
   - Compare performance

7. **Organize Map**
   - Proper layer ordering
   - Create group layer
   - Rename layers for clarity

**Deliverable:**
- ArcGIS Pro project with all Quinhagak content
- At least one local (exported) layer
- Organized and ready for analysis

---

## Summary

### Key Concepts

1. **ArcGIS Pro connects to ArcGIS Online**
   - Access your personal and organizational content
   - Bring web map layers into desktop environment

2. **Sharing matters**
   - Private, Organization, or Public
   - Affects who can see your layers
   - Check settings if layers are missing

3. **Different layer types**
   - Rasters: Imagery and surfaces
   - Polygons: Areas and parcels
   - Lines: Roads, rivers, trails
   - Points: Locations and observations

4. **Measure for verification**
   - Check accuracy of data
   - Determine imagery resolution
   - Verify coordinate systems

5. **Download for performance**
   - Export to local geodatabase
   - Faster, offline-capable
   - Better for editing

### Workflow

1. Search for content in Portal
2. Add to map
3. Verify accuracy (measure, check resolution)
4. Export important layers locally
5. Organize for analysis

---

## Additional Resources

### Documentation
- [Add data from ArcGIS Online](https://pro.arcgis.com/en/pro-app/latest/help/projects/add-data-from-arcgis-online.htm)
- [Work with portal content](https://pro.arcgis.com/en/pro-app/latest/help/projects/work-with-portal-content.htm)
- [Export features](https://pro.arcgis.com/en/pro-app/latest/tool-reference/conversion/export-features.htm)

### Sharing Resources
- [Share layers in ArcGIS Online](https://doc.arcgis.com/en/arcgis-online/share-maps/share-items.htm)
- [Manage sharing permissions](https://doc.arcgis.com/en/arcgis-online/share-maps/share-items.htm)

### Related Lessons
- Lesson 1: Projections (coordinate system verification)
- Lesson 3: Data Management (organizing local data)
- Module 1: ArcGIS Online Basics (creating the content)

---

## Next Steps

After mastering content import:
1. Proceed to Lesson 3: Data Management
2. Learn to organize local files
3. Understand geodatabase structure
4. Begin spatial analysis!

---

**Lesson Version:** 1.0
**Last Updated:** November 2025
**Module:** 4 - Spatial Analysis in ArcGIS Pro
**Location:** Quinhagak, Alaska
