# Lesson 10: Exporting and Sharing

**Duration:** 45 minutes
**Difficulty:** Beginner-Intermediate
**Prerequisites:** Understanding of geodatabases and feature classes

---

## Overview

Exporting data is essential for sharing analysis results, backing up work, and using data in other applications. This lesson covers exporting as layers, shapefiles, and packages, uploading to ArcGIS Online, and using interoperability tools for file type conversion.

---

## Learning Objectives

By the end of this lesson, you will be able to:

1. ✅ Export features to different formats
2. ✅ Understand Layer vs Shapefile vs Package formats
3. ✅ Upload results to ArcGIS Online
4. ✅ Convert between file types using interoperability tools
5. ✅ Use time-saving export workflows
6. ✅ Choose appropriate format for sharing

---

## Part 1: Understanding Export Formats

### Export Format Comparison

| Format | Extension | Best For | File Structure |
|--------|-----------|----------|----------------|
| **Layer File** | .lyrx | Saving symbology | References data, stores styling |
| **Shapefile** | .shp | Legacy compatibility | Multiple files (.shp, .dbf, .shx, .prj) |
| **Feature Class** | (in .gdb) | ArcGIS work | Inside geodatabase |
| **Package** | .ppkx, .lpkx | Sharing complete project/layer | Single file with data |
| **CSV** | .csv | Spreadsheet/database | Text table, no geometry |
| **KML/KMZ** | .kml, .kmz | Google Earth | Compressed spatial file |

---

## Part 2: Export as Layer File

### What is a Layer File?

**Layer File (.lyrx):**
- Stores symbology and properties
- References data (doesn't copy it)
- Small file size
- Reusable styling

**When to Use:**
- Save custom symbology
- Apply styling to new data
- Share visualization settings

### Task 2.1: Save Layer File

**Steps:**
1. Style layer as desired (symbology, labels, etc.)
2. Right-click layer in Contents
3. Sharing → Save As Layer File
4. Choose location and name
5. Save

**Apply Later:**
- Drag .lyrx file onto map
- Or: Right-click layer → Apply Symbology from Layer → Browse to .lyrx

**Limitation:** Doesn't include actual data, only styling

---

## Part 3: Export as Shapefile

### When to Use Shapefiles

**Use Shapefiles When:**
- Sharing with users without ArcGIS
- Required by external partner
- Working with very old software
- Industry standard for your field

**Limitations:**
- 2GB file size limit
- Field names max 10 characters
- Multiple files to manage
- Less efficient than geodatabase

### Task 3.1: Export Features to Shapefile

**Method 1: Export Features**

1. **Right-click layer**
2. **Data → Export Features**
3. **Export Features Tool opens:**
   - Input: Your layer
   - Output: Browse to location
   - Change extension to .shp
   - Example: `Quinhagak_Parcels.shp`
4. **Run**
5. **Result:** Shapefile created

**Method 2: Feature Class to Shapefile Tool**

- Analysis tab → Tools
- Search: "Feature Class to Shapefile"
- Faster for batch exports

**Files Created:**
- .shp (geometry)
- .dbf (attributes)
- .shx (index)
- .prj (projection)
- .cpg (character encoding)
- And sometimes more

**Important:** Keep all files together!

---

## Part 4: Export to Geodatabase (Feature Class)

### Best Format for ArcGIS Work

**When to Use:**
- Sharing with ArcGIS users
- Archiving results
- Moving data between projects
- Best performance and features

### Task 4.1: Export to Feature Class

**Method 1: Export Features**

1. **Right-click layer**
2. **Data → Export Features**
3. **Output Location:**
   - Browse to geodatabase
   - Name feature class
   - Example: `Analysis_Results.gdb/Suitable_Parcels`
4. **Run**

**Method 2: Copy/Paste in Catalog**

1. **Catalog Pane**
2. **Right-click feature class**
3. **Copy**
4. **Navigate to target .gdb**
5. **Right-click → Paste**
6. **Rename if desired**

---

## Part 5: Creating Packages

### What is a Package?

**Layer Package (.lpkx):**
- Single file
- Includes data + symbology
- Easy to share
- Recipient can use immediately

**Project Package (.ppkx):**
- Entire project bundled
- Includes all data, maps, layouts
- Complete workspace sharing

### Task 5.1: Create Layer Package

**Steps:**
1. **Right-click layer**
2. **Sharing → Share As Layer Package**
3. **Package Layer Dialog:**
   - Name and summary
   - Tags
   - Save location or upload to AGOL
4. **Consolidate:** Choose to include data
5. **Create**

**Recipient:**
- Opens .lpkx file
- Data and styling appear
- Ready to use

### Task 5.2: Create Project Package

**For entire project:**

1. **Share tab → Package Project**
2. **Configure:**
   - Name and description
   - What to include
   - Save location
3. **Create Package**

**Use Case:**
- Share complete analysis with team
- Archive completed project
- Move project to different computer

---

## Part 6: Uploading to ArcGIS Online

### Share Analysis Results Online

**Benefits:**
- Access anywhere
- Share with stakeholders
- Web maps and apps
- Collaboration

### Task 6.1: Upload Feature Layer to AGOL

**Method 1: Share As Web Layer**

1. **Right-click layer**
2. **Sharing → Share As Web Layer**
3. **Share As Web Layer Pane:**
   - Layer Type: Feature
   - Name (must be unique in your AGOL)
   - Summary and tags
   - Share with: Organization or Public
4. **Analyze** (check for issues)
5. **Share**
6. **Progress bar → uploads to AGOL**

**Method 2: From AGOL Website**

1. Sign in to ArcGIS Online
2. Content → Add Item → From Computer
3. Browse to shapefile or file geodatabase
4. Upload and publish

### Upload Considerations

**Credits:**
- Uploads may consume credits
- Check organization limits

**Sharing:**
- Set appropriate sharing level
- Private, Organization, or Public

**Size:**
- Large datasets take time
- May hit size limits
- Consider generalizing first

---

## Part 7: File Type Conversion (Interoperability)

### Converting Between Formats

**Need to share with non-ArcGIS users?**

Convert to common formats:
- KML/KMZ (Google Earth)
- GeoJSON (web mapping)
- CSV (spreadsheets - loses geometry for tables)

### Task 7.1: Export to KML

**For Google Earth:**

1. **Analysis tab → Tools**
2. **Search: "Layer To KML"**
3. **Parameters:**
   - Input: Your layer
   - Output: Location and name (.kmz)
   - Layer Output Scale: Determines detail
4. **Run**
5. **Result:** KMZ file for Google Earth

**Share:**
- Email file
- Recipients open in Google Earth
- No ArcGIS needed

### Task 7.2: Table to Excel

**For attribute data:**

1. **Right-click layer**
2. **Data → Export Table**
3. **Output:** Change extension to .csv or .xlsx
4. **Run**

**Result:** 
- Spreadsheet with attributes
- No geometry
- Easy to share

---

## Part 8: Time-Saving Tools

### Batch Processing

**Export Multiple Layers:**

**Feature Class to Geodatabase tool:**
- Add multiple inputs
- Export all at once
- Saves time

**Model Builder:**
- Create repeatable workflows
- Export multiple formats simultaneously
- Advanced automation

### Templates and Defaults

**Set Default Outputs:**
1. Project → Options
2. Geoprocessing
3. Output coordinate system
4. Output geodatabase
5. Saves repetitive configuration

**Save Tool Settings:**
- Many tools have "Save as defaults" option
- Reuse common parameters

---

## Part 9: Backup Strategy

### Regular Backups

**What to Backup:**
- Project files (.aprx)
- Geodatabases (.gdb)
- Original data
- Exported results
- Documentation

**Where to Backup:**
- External drive
- Cloud storage (OneDrive, Google Drive)
- ArcGIS Online
- Network drive

**Frequency:**
- After significant work
- Daily for active projects
- Weekly for ongoing work

---

## Part 10: Practice Exercise

### Exercise: Export Grant Application Data

**Goal:** Prepare data for sharing with grant reviewers

**Tasks:**

1. **Export to Shapefile:**
   - Export trail layer as shapefile
   - For partner without ArcGIS
   - Verify all files present

2. **Create Layer Package:**
   - Package styled parcels layer
   - Include data
   - Ready to share

3. **Upload to AGOL:**
   - Share analysis results to AGOL
   - Set sharing: Organization
   - Verify upload successful

4. **Export Attributes to Excel:**
   - Export trail data table to CSV
   - Open in Excel to verify
   - Include in grant documentation

5. **Create KML:**
   - Export trails to KMZ
   - Open in Google Earth
   - Verify appearance

**Deliverable:**
- Shapefile package (all files)
- Layer package (.lpkx)
- Web layer in AGOL
- CSV attribute table
- KMZ for Google Earth
- Documentation of what's been shared

---

## Summary

### Export Formats

1. **Layer File:** Symbology only
2. **Shapefile:** Legacy compatibility
3. **Feature Class:** Best for ArcGIS
4. **Package:** Complete sharing (data + styling)
5. **KML:** Google Earth
6. **CSV:** Spreadsheets

### Key Concepts

- Choose format based on audience
- Geodatabase best for ArcGIS users
- Packages easiest for complete sharing
- Upload to AGOL for web access
- Convert formats with interoperability tools

### Best Practices

- Organize exports in dedicated folder
- Name clearly and consistently
- Document what you've shared
- Backup important data
- Choose smallest necessary format
- Consider recipient's software

---

**Lesson Version:** 1.0  
**Last Updated:** November 2025  
**Module:** 4 - Spatial Analysis in ArcGIS Pro
