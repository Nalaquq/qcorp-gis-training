# Activity 5: Garmin Data Transfer Workshop

**Training Date:** November 13, 2025
**Duration:** 180 minutes
**Difficulty:** Intermediate
**Prerequisites:** Lesson 4 (Handheld Garmin GPS) completed

---

## Overview

In this hands-on activity, you'll learn the complete workflow for transferring data between Garmin handheld GPS devices, ArcGIS Pro, and ArcGIS Online. You'll work with real data: winter trails marked by Quinhagak Search and Rescue volunteers and placenames from the 1990 NVK Elder Place Name project collected by Joe Pleasant.

This workshop covers bidirectional data flow - both importing GPS data into GIS software for editing and analysis, and exporting GIS data back to Garmin devices for field use.

---

## Learning Objectives

By the end of this activity, you will be able to:

1. ✅ Extract GPX data from a Garmin device using Basecamp
2. ✅ Convert GPX files to ArcGIS Pro layers
3. ✅ Edit symbology and geometry in ArcGIS Pro
4. ✅ Convert ArcGIS layers to GPX format
5. ✅ Load GPX data to a Garmin device via Basecamp
6. ✅ Clone an ArcGIS Online layer for local editing
7. ✅ Download and install BirdsEye satellite imagery on Garmin devices

---

## Equipment and Software Required

### Hardware
- Garmin GPSMAP 67i (or similar handheld GPS) - with SAR trail data
- Second Garmin device (for receiving edited data)
- USB cables for both devices
- Computer with Windows or macOS

### Software
- Garmin Basecamp (free download)
- ArcGIS Pro (with valid license)
- ArcGIS Online account

### Data Resources
- Quinhagak Yuuyaraq Place Names Feature Layer:
  https://services6.arcgis.com/HDgSl3KvKJMed1UY/arcgis/rest/services/Quinhagak_Yuuyaraq_Place_Names/FeatureServer

---

## Background

### Winter Trails Data

The Garmin 67i contains waypoints and tracks marked by Quinhagak Search and Rescue volunteers documenting traditional winter snowmachine trails. This data will support:
- Community navigation safety
- Alaska DOT Community Trail Marking Grant application
- SAR operations

### Elder Place Names

The Quinhagak Yuuyaraq Place Names layer contains traditional Yup'ik placenames collected by **Joe Pleasant** as part of an **Elder Place Name project conducted by the Native Village of Kwinhagak (NVK) in 1990**. This invaluable cultural data documents traditional knowledge that supports:
- Cultural preservation
- Navigation and wayfinding
- Search and rescue operations
- Community education

---

## Part 1: Extract Trail Data from Garmin (30 minutes)

### Task 1.1: Install and Open Garmin Basecamp

**If not already installed:**
1. Download from: https://www.garmin.com/en-US/software/basecamp/
2. Install following prompts
3. Launch Garmin Basecamp

### Task 1.2: Connect Garmin Device

1. Connect Garmin 67i to computer via USB cable
2. Turn on device (if not automatic)
3. Wait for device to appear in Basecamp's Devices panel
4. If device doesn't appear:
   - Try different USB port
   - Restart Basecamp
   - Check USB cable

### Task 1.3: View Device Contents

1. Click on device in Devices panel
2. Expand to see:
   - Waypoints
   - Tracks
   - Routes
3. Click on items to view on map
4. Note the SAR winter trail tracks

### Task 1.4: Export GPX Files

**Export Tracks:**
1. Select all trail tracks in device
   - Click first track
   - Shift+click last track (or Ctrl+A)
2. File → Export → Export Selection
3. Format: **GPX**
4. Navigate to project folder
5. Filename: "SAR_Winter_Trails_Raw.gpx"
6. Save

**Export Waypoints:**
1. Select all waypoints
2. File → Export → Export Selection
3. Format: **GPX**
4. Filename: "SAR_Waypoints_Raw.gpx"
5. Save

**Verify Files:**
- Check that .gpx files appear in folder
- Note file sizes

---

## Part 2: Convert GPX to ArcGIS Pro Layers (25 minutes)

### Task 2.1: Create ArcGIS Pro Project

1. Launch ArcGIS Pro
2. Create new project:
   - Name: "Garmin_Data_Transfer_Nov2025"
   - Location: Documents/ArcGIS/
   - Template: Map
3. Save project

### Task 2.2: Convert Tracks to Feature Class

1. Analysis tab → Tools
2. Search for **"GPX to Features"**
3. Open tool
4. **Parameters:**
   - Input GPX File: Browse to "SAR_Winter_Trails_Raw.gpx"
   - Output Feature Class: "SAR_Winter_Trails" (in project .gdb)
   - Output Type: **Tracks**
5. Click Run
6. Track lines added to map

### Task 2.3: Convert Waypoints to Feature Class

1. Open GPX to Features tool again
2. **Parameters:**
   - Input GPX File: "SAR_Waypoints_Raw.gpx"
   - Output Feature Class: "SAR_Waypoints"
   - Output Type: **Waypoints**
3. Click Run
4. Waypoint locations added to map

### Task 2.4: Review Imported Data

1. Zoom to Quinhagak area
2. Examine tracks:
   - Open attribute table
   - Note existing fields (name, timestamp, etc.)
3. Examine waypoints:
   - Open attribute table
   - Note names and coordinates

---

## Part 3: Edit and Style Data in ArcGIS Pro (35 minutes)

### Task 3.1: Add Descriptive Attributes to Tracks

**Add New Fields:**
1. Open SAR_Winter_Trails attribute table
2. Add Field:
   - **Trail_Name** (Text, 100)
   - **Trail_Type** (Text, 50) - Primary, Secondary, Connector
   - **Condition** (Text, 50) - Good, Fair, Poor
   - **Season** (Text, 50) - Winter, Summer, Year-round
   - **Grant_Priority** (Short) - 1-5 for marking priority
   - **Verified_By** (Text, 100)
   - **Notes** (Text, 255)

**Populate Attributes:**
1. Start Edit Session
2. Select each trail segment
3. Fill in attributes based on SAR volunteer knowledge
4. Example:
   - Trail_Name: "Village to Fish Camp Trail"
   - Trail_Type: "Primary"
   - Condition: "Good"
   - Season: "Winter"
   - Grant_Priority: 1
5. Save edits

### Task 3.2: Edit Trail Segments

**Clean Up Tracks:**
1. In Edit tab, select trail layer
2. Review each track:
   - Remove erroneous points (GPS noise)
   - Split tracks at logical break points
   - Delete duplicates
3. Save edits frequently

**Merge Related Segments:**
1. Select segments that should be one trail
2. Edit → Merge
3. Keep attributes from primary segment
4. Save

### Task 3.3: Apply Symbology

**Style Tracks:**
1. Right-click SAR_Winter_Trails → Symbology
2. **Single Symbol:**
   - Line style: Solid
   - Color: Blue
   - Width: 2 pt

**Or by Category:**
1. Symbology → Unique Values
2. Field: Trail_Type
3. Colors:
   - Primary: Red, 3 pt
   - Secondary: Orange, 2 pt
   - Connector: Yellow, 1 pt

**Style Waypoints:**
1. Right-click SAR_Waypoints → Symbology
2. Choose appropriate symbols
3. Size: 10 pt

### Task 3.4: Save Layer Files

1. Right-click layer → Sharing → Save As Layer File
2. Save as .lyrx for future use
3. This preserves your symbology

---

## Part 4: Export to GPX for Garmin (25 minutes)

### Task 4.1: Convert Trails to GPX

1. Analysis → Tools
2. Search for **"Features to GPX"**
3. **Parameters:**
   - Input Features: SAR_Winter_Trails
   - Output File: "SAR_Trails_Edited.gpx"
   - Name Field: Trail_Name (or Name)
   - Description Fields: Trail_Type, Condition, Notes
4. Click Run
5. GPX file created

### Task 4.2: Convert Waypoints to GPX

1. Open Features to GPX again
2. **Parameters:**
   - Input Features: SAR_Waypoints
   - Output File: "SAR_Waypoints_Edited.gpx"
   - Name Field: Name
3. Click Run

### Task 4.3: Import to Basecamp

1. Open Garmin Basecamp
2. File → Import
3. Select "SAR_Trails_Edited.gpx"
4. Tracks appear in Library
5. Repeat for waypoints

### Task 4.4: Transfer to Second Garmin Device

1. Connect second Garmin device
2. In Basecamp, select imported tracks
3. Drag to device in Devices panel
   - Or: Device → Send to Device
4. Select waypoints and transfer
5. Verify data appears on device

**Check on Device:**
1. Navigate to Tracks menu
2. Confirm trails are loaded
3. Navigate to Waypoints menu
4. Confirm waypoints are loaded

---

## Part 5: Clone ArcGIS Online Placenames Layer (25 minutes)

### Task 5.1: Access the Placenames Layer

**Open in ArcGIS Online:**
1. Sign in to ArcGIS Online
2. Navigate to the layer:
   https://services6.arcgis.com/HDgSl3KvKJMed1UY/arcgis/rest/services/Quinhagak_Yuuyaraq_Place_Names/FeatureServer

**Or search:**
1. Content → Search for "Quinhagak Yuuyaraq Place Names"
2. Find the feature service

### Task 5.2: Clone the Layer

**Create Editable Copy:**
1. Open layer item page
2. Click "Export Data" dropdown
3. Select "Export to File Geodatabase" (or Shapefile)
4. Download the .zip file
5. Extract to project folder

**Alternative - Add Directly to ArcGIS Pro:**
1. In ArcGIS Pro, Insert → Connections → Add Portal Connection
2. Sign in to ArcGIS Online
3. Add Data → Portal → ArcGIS Online
4. Search for the layer
5. Add to map

### Task 5.3: Review Placename Data

1. Open attribute table
2. Review fields:
   - Yup'ik placename
   - English translation
   - Description
   - Feature type
   - Source
3. Note: Collected by Joe Pleasant for NVK in 1990

### Task 5.4: Prepare for GPX Export

**Ensure proper fields:**
1. The "Name" field should contain the placename
2. This will become the waypoint name on Garmin
3. Note: Garmin has character limits for names

---

## Part 6: Convert Placenames to GPX for Garmin (20 minutes)

### Task 6.1: Export as GPX

1. Analysis → Tools → Features to GPX
2. **Parameters:**
   - Input Features: Quinhagak_Yuuyaraq_Place_Names
   - Output File: "Quinhagak_Placenames.gpx"
   - Name Field: [Primary name field]
   - Description Fields: English translation, Description
3. Run tool

### Task 6.2: Edit in Basecamp (Optional)

**Import to Basecamp:**
1. File → Import → Select GPX file
2. Waypoints appear in Library

**Edit Symbology:**
1. Select all placename waypoints
2. Right-click → Get Info (or Properties)
3. Change symbol to distinctive icon
4. Choose color to differentiate from trail waypoints

**Organize:**
1. Create new List: "Quinhagak Placenames"
2. Move placename waypoints to this list

### Task 6.3: Load to Garmin Device

1. Connect Garmin device (either one)
2. Select placename waypoints
3. Transfer to device
4. Verify on device

---

## Part 7: Download BirdsEye Satellite Imagery (20 minutes)

### Task 7.1: Access BirdsEye in Basecamp

1. In Garmin Basecamp
2. View → BirdsEye Direct
3. Or: Maps → BirdsEye Direct

### Task 7.2: Select Coverage Area

**Navigate to Quinhagak:**
1. Zoom to Quinhagak area
2. Consider coverage needs:
   - Village area
   - Trail routes
   - Traditional Land Use Area

**Draw Selection:**
1. Use BirdsEye selection tool
2. Draw rectangle around desired area
3. Estimate file size shown
4. Adjust area if too large

### Task 7.3: Download Imagery

1. Click Download or Send to Device
2. Select target device
3. Choose quality setting
4. Begin download
5. Wait for completion (may take several minutes)

**Storage Considerations:**
- Imagery files are large
- Use SD card if device has one
- Only download essential areas

### Task 7.4: Verify on Device

1. On Garmin device, change map display to satellite
2. Zoom to downloaded area
3. Confirm high-resolution imagery appears
4. Repeat for second device if needed

---

## Deliverables

### Required Outputs

1. **✅ ArcGIS Pro Project**
   - Project: Garmin_Data_Transfer_Nov2025
   - SAR_Winter_Trails feature class with edited attributes
   - SAR_Waypoints feature class
   - Quinhagak_Placenames feature class (cloned)

2. **✅ GPX Files**
   - SAR_Trails_Edited.gpx
   - SAR_Waypoints_Edited.gpx
   - Quinhagak_Placenames.gpx

3. **✅ Loaded Garmin Devices**
   - Device 1: Trails, waypoints, placenames, satellite imagery
   - Device 2: Trails, waypoints, placenames, satellite imagery

4. **✅ Documentation**
   - Summary of workflow steps completed
   - Notes on any issues encountered
   - Screenshot of data on both platforms (ArcGIS Pro and Garmin device)

---

## Skills Checklist

By completing this activity, demonstrate proficiency in:

### Garmin Basecamp
- [ ] Connect Garmin device successfully
- [ ] Export GPX files from device
- [ ] Import GPX files from GIS
- [ ] Edit waypoint symbology
- [ ] Transfer data to device
- [ ] Download BirdsEye imagery

### ArcGIS Pro
- [ ] Convert GPX to feature class
- [ ] Add and populate attribute fields
- [ ] Edit feature geometry
- [ ] Apply symbology
- [ ] Export features to GPX format
- [ ] Clone layers from ArcGIS Online

### Workflow Integration
- [ ] Complete Garmin → GIS → Garmin workflow
- [ ] Complete ArcGIS Online → GPX → Garmin workflow
- [ ] Troubleshoot common issues
- [ ] Organize files and projects properly

---

## Common Issues and Solutions

### GPX Conversion Problems

**Issue:** Tracks appear as separate segments after import
- **Solution:** Merge in ArcGIS Pro, or export as single track from Basecamp

**Issue:** Waypoint names truncated
- **Solution:** Garmin has character limits; shorten names before export

**Issue:** No data appears after GPX to Features
- **Solution:** Check Output Type matches data (Tracks vs Waypoints)

### Transfer Problems

**Issue:** Data won't transfer to device
- **Solution:** Check device storage; verify USB connection; restart Basecamp

**Issue:** Tracks don't appear on device
- **Solution:** Check Track Manager on device; may need to enable display

### BirdsEye Issues

**Issue:** Download fails or is very slow
- **Solution:** Select smaller area; check internet connection

**Issue:** Imagery doesn't appear on device
- **Solution:** Change map display settings; check if saved to correct location

---

## Real-World Application

### Trail Marking Grant Support

The edited trail data from this activity will support Quinhagak SAR's application to the Alaska DOT Community Trail Marking Grant program by providing:
- Documented trail routes
- Priority rankings for marking
- Professional GIS data
- Field-verified accuracy

### SAR Operations

With trails and placenames loaded on Garmin devices, SAR volunteers will have:
- Local placenames for communication
- Trail routes for navigation
- Satellite imagery for orientation
- Data created by local knowledge holders

### Cultural Preservation

By working with the Joe Pleasant placenames from 1990, this activity helps:
- Preserve elder knowledge
- Make cultural data accessible
- Support traditional navigation methods
- Bridge traditional knowledge and modern technology

---

## Summary

In this activity, you learned to:

1. **Extract data from Garmin** using Basecamp and GPX export
2. **Convert to GIS layers** using GPX to Features tool
3. **Edit in ArcGIS Pro** including attributes, geometry, and symbology
4. **Export back to GPX** using Features to GPX tool
5. **Load to Garmin devices** via Basecamp transfer
6. **Clone ArcGIS Online layers** for local editing and export
7. **Install satellite imagery** using BirdsEye in Basecamp

These skills enable bidirectional data flow between field GPS devices and professional GIS software, allowing you to:
- Collect data in the field on rugged devices
- Edit and analyze in powerful GIS software
- Deploy improved data back to field devices
- Support community projects with professional tools

---

## Next Steps

**Apply these skills to:**
- Upcoming trail marking projects
- Placename documentation sessions
- SAR training exercises
- Community mapping projects

**Continue learning:**
- [Activity 9: Community Placename and Trail Mapping](../../04-spatial-analysis-arcgis-pro/activities/activity-09-placename-trail-mapping.md) (Module 4)
- [Lesson 5: Data Synchronization](../lessons/05-data-sync.md)

---

**Activity Version:** 1.0
**Last Updated:** November 2025
**Training Date:** November 13, 2025
**Location:** Quinhagak, Alaska
