# Lesson 4: Handheld Garmin GPS Data Collection

**Module:** 02 - Field Data Collection
**Duration:** 90 minutes
**Difficulty:** Beginner to Intermediate
**Prerequisites:** Module 1 completed, basic understanding of GPS

---

## Learning Objectives

By the end of this lesson, you will be able to:

1. ✅ Understand the capabilities and limitations of handheld GPS devices
2. ✅ Collect waypoints and tracks on a Garmin handheld device
3. ✅ Export data from Garmin devices using Garmin Basecamp
4. ✅ Convert GPX files to ArcGIS layers
5. ✅ Edit and style GPS data in ArcGIS Pro
6. ✅ Convert ArcGIS layers back to GPX format for transfer to Garmin devices
7. ✅ Download and install satellite imagery (BirdsEye) on Garmin devices

---

## Understanding Handheld GPS Accuracy

### Accuracy Comparison

**It's important to understand that handheld GPS devices are significantly less accurate than differential GPS (DGNSS) systems:**

| Device Type | Horizontal Accuracy | Best For |
|-------------|---------------------|----------|
| **Handheld Garmin GPS** | 3-10 meters (10-30 feet) | Trail marking, general navigation, waypoints |
| **Smartphone GPS** | 3-15 meters (10-50 feet) | General location, field forms |
| **DGNSS (RTK) like Emlid RS3** | 1-2 centimeters (<1 inch) | Surveys, boundaries, GCPs, precise measurements |

### When to Use Handheld GPS vs DGNSS

**Use Handheld Garmin When:**
- Marking trails and routes
- Recording general waypoints and placenames
- Navigation and wayfinding
- Tracking travel routes
- Marking approximate locations of features
- Field use in harsh conditions (rugged, waterproof)
- Battery life is critical (days vs hours)

**Use DGNSS (Emlid RS3) When:**
- Surveying property boundaries
- Collecting ground control points for drone mapping
- Measuring erosion over time
- Any work requiring legal-grade accuracy
- Precise infrastructure measurements
- Scientific data collection requiring centimeter accuracy

### Why the Accuracy Difference Matters

**Example: Marking a Trail**
- Handheld GPS: Trail may be shown 10 meters off from actual location
- This is acceptable for navigation - you can still find the trail
- NOT acceptable for property boundaries or precise measurements

**Example: Property Corner**
- 10-meter error could place corner inside neighbor's property
- Legal surveys require centimeter accuracy
- Always use DGNSS for boundary work

### Factors Affecting Handheld GPS Accuracy

**Environmental Factors:**
- Tree canopy (reduces satellite visibility)
- Steep terrain (blocks satellites on one side)
- Buildings and structures (multipath errors)
- Weather (heavy clouds can affect signal)

**Device Factors:**
- Antenna quality
- Number of satellite systems supported (GPS, GLONASS, Galileo)
- Age of device
- Time since last use (cold start vs warm start)

**Best Practices for Improved Accuracy:**
- Wait for device to acquire full satellite constellation
- Use in open areas when possible
- Use averaging feature if available
- Stand still when marking waypoints
- Enable WAAS/EGNOS if available

---

## Garmin Handheld Devices

### Common Models for Field Work

**Garmin GPSMAP Series:**
- Rugged, waterproof construction
- Large screens for map viewing
- Long battery life
- Examples: GPSMAP 67i, GPSMAP 66s

**Garmin inReach Series:**
- Includes satellite communication
- Two-way messaging
- SOS capabilities
- Example: GPSMAP 67i (combines GPS and inReach)

### Key Features for GIS Work

**Data Collection:**
- Waypoints: Individual point locations
- Tracks: Continuous recording of movement
- Routes: Planned paths with waypoints

**Storage:**
- Internal memory for waypoints and tracks
- MicroSD card for maps and imagery
- Can store thousands of waypoints

**Connectivity:**
- USB connection to computer
- Bluetooth (some models)
- ANT+ (some models)

---

## Collecting Data on Garmin Devices

### Marking Waypoints

**To Mark a Waypoint:**
1. Navigate to location
2. Stand still and wait for best accuracy
3. Press "Mark" button or select from menu
4. Enter waypoint information:
   - Name (short code)
   - Symbol (icon)
   - Notes (optional)
5. Save waypoint

**Waypoint Naming Tips:**
- Keep names short (8-12 characters)
- Use consistent naming scheme
- Example: "PN001" for Placename 001
- Can rename later in Basecamp or ArcGIS

### Recording Tracks

**To Record a Track:**
1. Enable track recording in settings
2. Begin traveling the route
3. Device automatically records points at intervals
4. Stop recording when complete
5. Save track with descriptive name

**Track Settings:**
- Recording interval (time or distance)
- Auto-pause when stopped
- Track color for display

### Organizing Data

**On Device:**
- Create folders for different projects
- Use consistent naming
- Clear old data before new projects
- Note: Limited editing capability on device

---

## Garmin Basecamp Software

### Overview

Garmin Basecamp is free desktop software for managing GPS data. It serves as the bridge between your Garmin device and GIS software.

**Download:** [Garmin Basecamp](https://www.garmin.com/en-US/software/basecamp/)

### Key Functions

1. **Import/Export:** Transfer data between device and computer
2. **Edit:** Rename, organize, and modify waypoints and tracks
3. **Convert:** Export to various formats including GPX
4. **Maps:** View and install maps on devices
5. **Plan:** Create routes and transfer to device

### Basecamp Interface

**Main Components:**
- **Library Panel:** Organizes your data into lists
- **Map Panel:** Displays data on maps
- **Device Panel:** Shows connected Garmin devices
- **Trip Planner:** Create and manage trips

---

## Workflow 1: Garmin → ArcGIS Pro

### Step 1: Connect Device and Open Basecamp

1. Connect Garmin to computer via USB
2. Launch Garmin Basecamp
3. Device appears in Devices panel
4. View waypoints and tracks on device

### Step 2: Export GPX File

1. Select data to export:
   - Click waypoints/tracks in device list
   - Or select from map
   - Can select multiple items
2. File → Export → Export Selection
3. Choose format: **GPX**
4. Save to project folder with descriptive name:
   - Example: "SAR_Winter_Trails_2024.gpx"
   - Example: "Quinhagak_Placenames_Nov2025.gpx"

### Step 3: Convert GPX to ArcGIS Layer

**In ArcGIS Pro:**

1. Open or create project
2. Analysis tab → Tools
3. Search for **"GPX to Features"**
4. Open tool

**Tool Parameters:**
- **Input GPX File:** Browse to your .gpx file
- **Output Feature Class:** Name for new layer (in geodatabase)
- **Output Type:**
  - Waypoints → Points
  - Tracks → Polylines
  - Both → Creates multiple feature classes

5. Click Run
6. Layer added to map

### Step 4: Edit in ArcGIS Pro

**Add/Edit Attributes:**
1. Open attribute table
2. Add fields as needed:
   - English_Name
   - Description
   - Category
   - Date_Collected
   - Source
3. Populate attributes from field notes

**Edit Geometry:**
1. Start edit session
2. Modify track segments if needed:
   - Split tracks
   - Delete erroneous points
   - Smooth lines
3. Save edits

**Apply Symbology:**
1. Right-click layer → Symbology
2. Style by category or attribute
3. Set appropriate colors and sizes
4. Save layer file (.lyrx) for reuse

---

## Workflow 2: ArcGIS → Garmin

### Step 1: Prepare Data in ArcGIS Pro

**Ensure data is ready:**
- Appropriate coordinate system
- Clean geometry
- Attributes you want to preserve

**Create output geodatabase or folder** for exports

### Step 2: Convert to GPX Format

**Use Features to GPX Tool:**

1. Analysis tab → Tools
2. Search for **"Features to GPX"**
3. Open tool

**Tool Parameters:**
- **Input Features:** Your point or line layer
- **Output GPX File:** Location and filename
- **Name Field:** Which attribute to use for waypoint names
- **Description Fields:** (Optional) Additional attributes

4. Click Run
5. GPX file created

### Step 3: Import to Garmin via Basecamp

1. Open Garmin Basecamp
2. File → Import
3. Select your GPX file
4. Data appears in Library

**Organize in Basecamp:**
- Create List for project
- Move imported data to list
- Edit names/symbols if needed

### Step 4: Transfer to Garmin Device

1. Connect Garmin device
2. Select data to transfer
3. Drag to device in Devices panel
4. Or: Device → Send to Device
5. Verify data appears on device

---

## Workflow 3: ArcGIS Online → Garmin

### Step 1: Clone or Export Layer

**From ArcGIS Online:**

1. Open the feature layer item page
2. Options:
   - **Export:** Download as Shapefile, File Geodatabase, or GeoJSON
   - **Clone:** Create editable copy in your account

**Example - Quinhagak Placenames Layer:**
https://services6.arcgis.com/HDgSl3KvKJMed1UY/arcgis/rest/services/Quinhagak_Yuuyaraq_Place_Names/FeatureServer

### Step 2: Download/Open in ArcGIS Pro

**Method A - Direct Connection:**
1. In ArcGIS Pro, Add Data
2. Portal → ArcGIS Online
3. Search for layer
4. Add to map

**Method B - Export and Download:**
1. Export from ArcGIS Online as File Geodatabase
2. Download .zip file
3. Extract and add to ArcGIS Pro

### Step 3: Convert to GPX

Use **Features to GPX** tool as described above

### Step 4: Edit in Basecamp (Optional)

**Basecamp allows:**
- Change waypoint symbols
- Edit names
- Organize into folders
- Preview before loading to device

**Symbology in Basecamp:**
- Select waypoints
- Right-click → Properties
- Change symbol/color
- Garmin devices have limited symbol options

### Step 5: Load to Garmin

Transfer via Basecamp as described above

---

## Installing BirdsEye Satellite Imagery

### What is BirdsEye?

BirdsEye provides high-resolution satellite imagery for Garmin devices, allowing you to see aerial views on your GPS instead of just topo lines.

**Benefits:**
- See actual terrain features
- Identify landmarks more easily
- Better context for navigation
- Essential for areas without detailed topo maps

### Downloading Imagery in Basecamp

1. **Open Garmin Basecamp**

2. **Access BirdsEye:**
   - View → BirdsEye Direct
   - Or: Maps → BirdsEye Direct

3. **Select Area:**
   - Navigate to Quinhagak area on map
   - Draw box around area you want
   - Consider Traditional Land Use Area boundaries

4. **Download Options:**
   - Resolution/quality setting
   - Storage location (device or SD card)
   - Note: Large areas = large files

5. **Transfer to Device:**
   - Select imagery in Library
   - Send to connected device
   - Or copy files to device SD card

### BirdsEye Tips

**Storage:**
- Imagery files can be large (100s of MB)
- Use SD card in device
- Only download areas you need

**Updates:**
- Imagery is static (not updated automatically)
- Re-download if newer imagery needed

**Coverage:**
- Coverage may vary by region
- Alaska generally has good satellite imagery
- Some areas may have limited high-resolution coverage

---

## Data Management Best Practices

### File Organization

**Create consistent folder structure:**
```
Projects/
├── Quinhagak_Placenames/
│   ├── GPX_Raw/
│   │   └── SAR_Waypoints_Nov2025.gpx
│   ├── GDB/
│   │   └── Placenames.gdb
│   └── GPX_Export/
│       └── Placenames_ForGarmin.gpx
└── Winter_Trails/
    ├── GPX_Raw/
    ├── GDB/
    └── GPX_Export/
```

### Backup Procedures

**Always backup:**
- Original GPX files from device
- Edited data before export
- Final GPX files for device loading

**Multiple locations:**
- Local drive
- External drive or cloud
- ArcGIS Online (if hosting)

### Metadata Documentation

**Record for each dataset:**
- Collection date
- Device used
- Collector name
- Purpose/project
- Known accuracy limitations
- Processing steps applied

---

## Common Issues and Solutions

### GPX Import Problems

**Issue:** GPX won't import to ArcGIS Pro
- **Solution:** Check file is valid GPX format; may need to re-export from Basecamp

**Issue:** No features appear after conversion
- **Solution:** Check if waypoints or tracks; use correct output type setting

**Issue:** Features in wrong location
- **Solution:** Check coordinate system; GPX is typically WGS84

### Garmin Transfer Problems

**Issue:** Device not recognized in Basecamp
- **Solution:** Try different USB port; restart Basecamp; update device drivers

**Issue:** Data won't transfer to device
- **Solution:** Check device storage space; verify data format compatibility

**Issue:** Waypoints don't appear on device
- **Solution:** Check if saved to internal memory vs SD card; enable waypoints display

### Symbology Issues

**Issue:** Symbols don't match after transfer
- **Solution:** Garmin has limited symbols; use closest available match

**Issue:** Names truncated on device
- **Solution:** Garmin has character limits; use short names

---

## Comparison with DGNSS Workflow

### Key Differences

| Aspect | Handheld Garmin | DGNSS (Emlid RS3) |
|--------|-----------------|-------------------|
| **Accuracy** | 3-10 meters | 1-2 centimeters |
| **Setup time** | Turn on and go | 15-30 min base setup |
| **Learning curve** | Easy | Moderate to difficult |
| **Cost** | $300-700 | $3,000-10,000+ |
| **Battery life** | Days | Hours |
| **Weather resistance** | Excellent | Good |
| **Best use** | Navigation, trail marking | Surveys, precise measurements |
| **Field editing** | Limited | None on device |
| **Export format** | GPX | Multiple (CSV, SHP, etc.) |

### When to Use Each

**Handheld Garmin Scenarios:**
- SAR marking trails for grant applications
- Recording travel routes
- Marking fishing spots (approximate)
- General placename documentation
- Navigation aid for field crews

**DGNSS Scenarios:**
- Property boundary surveys
- Erosion measurement
- GCPs for drone mapping
- Infrastructure as-builts
- Scientific monitoring requiring precision

---

## Integration with Community Projects

### Quinhagak Placenames

**Historical Context:**
The Quinhagak Yuuyaraq Place Names layer contains placenames collected by Joe Pleasant as part of an Elder Place Name project conducted by the Native Village of Kwinhagak (NVK) in 1990. This valuable cultural data can be:

- Loaded onto Garmin devices for SAR navigation
- Updated with new placenames from community members
- Shared with community programs

**Workflow:**
1. Clone layer from ArcGIS Online
2. Convert to GPX
3. Load to SAR volunteer devices
4. Collect additional placenames in field
5. Import new waypoints back to master layer

### Trail Documentation

**For Alaska DOT Grants:**
Trails documented on Garmin devices can support applications to programs like the Community Trail Marking Grant by providing:

- Trail routes as GPS tracks
- Dangerous crossing waypoints
- Distance and route information
- Evidence of community use

---

## Summary

### Key Points

1. **Handheld Garmin devices provide 3-10 meter accuracy** - suitable for navigation and trail marking, not for surveys requiring precision

2. **Garmin Basecamp is essential** - bridges the gap between Garmin devices and GIS software

3. **GPX is the standard format** - universal GPS exchange format works with most software

4. **Two-way workflow** - data can flow from Garmin → GIS and from GIS → Garmin

5. **BirdsEye imagery enhances navigation** - provides satellite views on device

6. **Know when to use DGNSS instead** - for surveys, boundaries, and precise measurements

7. **Consistent file organization** - essential for managing multiple projects

### Skills to Practice

- [ ] Connect Garmin device and export GPX in Basecamp
- [ ] Convert GPX to ArcGIS layer
- [ ] Edit attributes and symbology in ArcGIS Pro
- [ ] Export ArcGIS layer to GPX
- [ ] Transfer GPX to Garmin via Basecamp
- [ ] Download BirdsEye imagery for device

---

## Resources

### Software Downloads
- [Garmin Basecamp](https://www.garmin.com/en-US/software/basecamp/)
- [Garmin Express](https://www.garmin.com/en-US/software/express/) (device updates)

### ArcGIS Tools
- [GPX to Features Tool](https://pro.arcgis.com/en/pro-app/latest/tool-reference/conversion/gpx-to-features.htm)
- [Features to GPX Tool](https://pro.arcgis.com/en/pro-app/latest/tool-reference/conversion/features-to-gpx.htm)

### Garmin Support
- [Garmin Support Center](https://support.garmin.com/)
- [GPSMAP 67i Manual](https://www8.garmin.com/manuals/webhelp/GPSMAP67i/EN-US/)

### Related Lessons
- [Lesson 3: DGNSS Field Collection](./03-dgnss-field-collection.md)
- [Terminology Guide](./terminology.md)

---

## Next Steps

**Continue to:**
- [Activity 5: Garmin Data Transfer Workshop](../activities/activity-05-garmin-data-transfer.md)
- [Lesson 5: Data Synchronization](./05-data-sync.md)

**Related content:**
- [Module 4: Spatial Analysis](../../04-spatial-analysis-arcgis-pro/) - for editing imported data
- [Module 5: Cartography](../../05-cartography/) - for creating maps from GPS data

---

**Version:** 1.0
**Last Updated:** November 2025
**Training Date:** November 13, 2025
**Location:** Quinhagak, Alaska
