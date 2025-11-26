# Lesson 3: Directory Structure and Data Management

**Duration:** 45 minutes
**Difficulty:** Beginner
**Prerequisites:** Lesson 2 (Adding Content)

---

## Overview

Proper data organization is critical for successful GIS work. This lesson teaches you how to set up a consistent directory structure, understand the geodatabase (.gdb) format, and follow best practices for file management.

You'll learn why we prefer creating features inside geodatabases rather than using shapefiles, and how to organize your ArcGIS Pro projects for efficiency and collaboration.

---

## Learning Objectives

By the end of this lesson, you will be able to:

1. ✅ Navigate to the standard ArcGIS folder location (Documents/ArcGIS)
2. ✅ Create and organize project directories consistently
3. ✅ Understand geodatabase (.gdb) structure and benefits
4. ✅ Create new feature classes inside geodatabases
5. ✅ Explain why geodatabases are preferred over shapefiles
6. ✅ Follow data management best practices

---

## Part 1: Standard Directory Structure

### The Documents/ArcGIS Folder

**Default Location:**
```
C:\Users\[YourName]\Documents\ArcGIS\
```

**Why This Location?**
- ✅ ArcGIS Pro default project location
- ✅ Easy to find and backup
- ✅ Consistent across all users
- ✅ Automatically indexed by ArcGIS Pro
- ✅ Good for collaboration (everyone uses same structure)

### Task 1.1: Navigate to Your ArcGIS Folder

**Using File Explorer:**
1. Open File Explorer (Windows + E)
2. Navigate to Documents
3. Look for "ArcGIS" folder
   - If it exists: Great!
   - If not: Create it (right-click → New → Folder)

**From ArcGIS Pro:**
1. Project tab → Options
2. Application → General
3. See "Default home folder"
4. Should point to Documents\ArcGIS

### Standard Folder Structure

**Recommended Organization:**
```
Documents/
└── ArcGIS/
    ├── Projects/
    │   ├── Quinhagak_Parcels/
    │   ├── Trail_Mapping/
    │   └── Erosion_Monitoring/
    ├── Data/
    │   ├── Quinhagak_Base/
    │   ├── Imagery/
    │   └── GPS_Data/
    └── Outputs/
        ├── Maps/
        └── Exports/
```

**Projects Folder:**
- Contains .aprx project files
- One folder per project
- Includes project-specific .gdb

**Data Folder:**
- Shared datasets used across projects
- Reference layers
- Basemaps and imagery

**Outputs Folder:**
- Exported maps (PDFs)
- Exported data
- Analysis results

---

## Part 2: Understanding Geodatabases (.gdb)

### What is a Geodatabase?

**File Geodatabase (.gdb):**
- A folder that stores GIS data
- Managed by ArcGIS
- Appears as a folder with .gdb extension
- Contains feature classes, tables, and more

**Example:**
```
Quinhagak_Analysis.gdb/
├── Parcels (polygon feature class)
├── Roads (line feature class)
├── Buildings (point feature class)
└── Trail_Data (table)
```

### Why Use Geodatabases?

**Benefits over Shapefiles:**

1. **Better Performance**
   - Faster queries and display
   - Optimized storage
   - Handles large datasets better

2. **More Features**
   - Longer field names (255 vs 10 characters)
   - More field types
   - Support for attachments
   - Topology rules
   - Relationship classes

3. **Better Organization**
   - All related data in one place
   - No scattered files
   - Easy to backup (one folder)

4. **Larger File Sizes**
   - Shapefiles limited to 2GB per file
   - Geodatabases: 1TB default, can go higher

5. **Better Data Integrity**
   - Built-in validation
   - Domain enforcement
   - Prevents corruption

### Geodatabase vs Shapefile Comparison

| Feature | Geodatabase (.gdb) | Shapefile (.shp) |
|---------|-------------------|------------------|
| **Field name length** | 255 characters | 10 characters |
| **File structure** | Single .gdb folder | Multiple files (.shp, .dbf, .shx, .prj, etc.) |
| **Performance** | Fast | Slower with large data |
| **Max file size** | 1 TB+ | 2 GB |
| **Data types** | Many types | Limited types |
| **Topology** | Supported | Not supported |
| **Organization** | All in one place | Scattered files |
| **Recommended for** | ✅ All new work | Legacy compatibility only |

**The Verdict:** Always use geodatabases for new work!

### When to Use Shapefiles

**Only use shapefiles when:**
- Sharing with users who don't have ArcGIS
- Working with very old software
- Explicitly required by a partner

**Otherwise:** Use geodatabases!

---

## Part 3: Creating a Project Geodatabase

### Task 3.1: Create New File Geodatabase

**Method 1: From Catalog Pane**

1. **Open Catalog Pane:**
   - View tab → Catalog Pane

2. **Navigate to Project Folder:**
   - Folders → Project folder

3. **Create Geodatabase:**
   - Right-click in folder area
   - New → File Geodatabase
   - Name: `Quinhagak_Analysis.gdb`
   - Press Enter

4. **Geodatabase Created:**
   - Appears as folder with cylinder icon
   - Ready to store feature classes

**Method 2: Using Geoprocessing Tool**

1. **Open Tool:**
   - Analysis tab → Tools
   - Search: "Create File Geodatabase"

2. **Tool Parameters:**
   - Location: Your project folder
   - Name: `Quinhagak_Analysis.gdb`
   - Version: Current (default)

3. **Run:**
   - Click Run
   - Geodatabase created

### Task 3.2: Understand Default Project Geodatabase

**Every Project Has One:**
When you create a new ArcGIS Pro project, it automatically creates a .gdb

**Location:**
```
MyProject/
├── MyProject.aprx (project file)
├── MyProject.gdb/ (default geodatabase)
├── Index/
└── ImportLog
```

**Using Default Geodatabase:**
- Convenient for project-specific data
- Automatically set as default output location
- Keeps project data together

**Checking Default:**
1. Insert tab → New Map
2. Geoprocessing tools default to this .gdb
3. Can change in Project → Options → Geoprocessing

---

## Part 4: Creating Feature Classes in Geodatabases

### Why Create Features Inside .gdb?

**Benefits:**
- Better organization
- Faster performance
- More field options
- Easier to backup
- Professional workflow

### Task 4.1: Create a Feature Class

**Review from Lesson 11:**
This process was covered in detail in Lesson 11: Creating Layers

**Quick Steps:**

1. **Right-click Geodatabase:**
   - Catalog Pane → Navigate to your .gdb
   - Right-click → New → Feature Class

2. **Name and Type:**
   - Name: `Quinhagak_Buildings`
   - Type: Point, Line, or Polygon
   - Coordinate System: NAD 1983 StatePlane Alaska 7

3. **Add Fields:**
   - Field Name, Type, Length
   - Example: Building_Name (Text, 100)

4. **Finish:**
   - Click Finish
   - Feature class appears in .gdb

**Multiple Feature Classes:**
Create as many as needed:
- Buildings (points)
- Roads (lines)
- Parcels (polygons)
- Erosion_Sites (polygons)

All stored efficiently in one .gdb!

---

## Part 5: Organizing Your Data

### Folder Naming Best Practices

**Do:**
- Use descriptive names: `Quinhagak_Trail_Mapping`
- No spaces: Use underscores `Trail_Mapping` not `Trail Mapping`
- Be consistent: Same naming pattern for all projects
- Include date for versions: `Analysis_2025_11`

**Don't:**
- Use special characters: `Analysis#2!` ❌
- Make names too long: `Quinhagak_Trail_Mapping_Version_2_November_2025_Final_FINAL` ❌
- Use ambiguous names: `Project1`, `New_Folder` ❌

### Project Organization Example

**Good Organization:**
```
Documents/ArcGIS/Projects/Quinhagak_Trail_Mapping/
├── Trail_Mapping.aprx
├── Trail_Mapping.gdb/
│   ├── SAR_Trails
│   ├── Dangerous_Crossings
│   └── Trail_Markers
├── GPS_Data/
│   ├── November_2025/
│   └── Archive/
├── Maps/
│   └── Grant_Application_Map.pdf
└── Documentation/
    └── Field_Notes.docx
```

**Benefits:**
- Everything in one place
- Easy to find files
- Easy to backup
- Easy to share

### Backup Strategy

**Important:** GIS data is valuable - back it up!

**Backup Methods:**

1. **Cloud Storage:**
   - OneDrive (collaborative editing)
   - Google Drive
   - Dropbox

2. **External Drive:**
   - Copy entire project folder
   - Weekly backups recommended

3. **ArcGIS Online:**
   - Upload important layers
   - Serves as backup
   - Enables sharing

**What to Backup:**
- .aprx project files
- .gdb geodatabases
- Original GPS data
- Exported maps
- Documentation

---

## Part 6: Managing Geodatabase Content

### Viewing Geodatabase Contents

**In Catalog Pane:**
1. Navigate to .gdb
2. Expand to see contents
3. See all feature classes and tables

**Feature Classes:**
- Shown with geometry icon (point/line/polygon)
- Double-click to preview

**Tables:**
- Non-spatial data
- Standalone attribute tables

### Geodatabase Best Practices

**1. Organize by Theme:**
Create separate geodatabases for different project types:
- `Quinhagak_Base.gdb` - Reference layers
- `Trail_Analysis.gdb` - Trail mapping project
- `Erosion_Monitoring.gdb` - Environmental monitoring

**2. Don't Overfill:**
- Keep geodatabases focused
- Too many feature classes = hard to manage
- Split into multiple .gdb if needed

**3. Name Clearly:**
- Feature class names should be descriptive
- `Buildings` not `Layer1`
- `SAR_Trails_2025` not `fc_final_v2`

**4. Document:**
- Add metadata to feature classes
- Right-click → Edit Metadata
- Describe what data is, when collected, by whom

---

## Part 7: Connecting to Folders

### Adding Folder Connections

**Why Connect Folders?**
- Quick access to frequently used data
- Don't have to navigate each time
- Can connect to network drives
- Share data locations with team

### Task 7.1: Add Folder Connection

**Steps:**

1. **Catalog Pane:**
   - Right-click "Folders"
   - "Add Folder Connection"

2. **Browse:**
   - Navigate to folder
   - Example: `Documents\ArcGIS\Data\Quinhagak_Base`
   - Click OK

3. **Folder Appears:**
   - Now in Folders list
   - Expand to see contents
   - Quick access anytime

**Disconnect:**
- Right-click folder
- "Remove Folder Connection"
- (Doesn't delete data, just removes shortcut)

---

## Part 8: Common Data Management Mistakes

### Mistake 1: Scattered Files

**Problem:**
```
Desktop/
  map1.aprx
Downloads/
  parcels.shp
Documents/
  trails.shp
C:/
  temp_data.gdb
```

**Solution:**
- Everything in Documents/ArcGIS
- Organized by project
- Easy to find and backup

### Mistake 2: Using Shapefiles for New Work

**Problem:**
- Creates multiple files (.shp, .dbf, .shx, .prj, .cpg, .sbn, .sbx)
- Easy to lose pieces
- Limited features

**Solution:**
- Always use geodatabases
- Create feature classes inside .gdb
- Better organization and performance

### Mistake 3: No Backups

**Problem:**
- Hard drive fails
- Computer stolen
- Files corrupted
- Work lost!

**Solution:**
- Regular backups to cloud or external drive
- Upload important layers to AGOL
- Version control for critical projects

### Mistake 4: Unclear Naming

**Problem:**
```
final.gdb
final_v2.gdb
final_FINAL.gdb
final_2025_really_final.gdb
```

**Solution:**
- Name with purpose: `Quinhagak_Trail_Mapping.gdb`
- Use dates if versioning: `Trail_Mapping_2025_11.gdb`
- Or use version numbers: `Trail_Mapping_v1.gdb`

---

## Part 9: Working with Project Packages

### What is a Project Package?

**Project Package (.ppkx):**
- Bundles project + data into one file
- Easy to share complete project
- Includes maps, data, layouts, everything

**When to Use:**
- Sharing entire project with someone
- Archiving completed work
- Moving project to different computer

### Creating a Package

**Steps:**
1. Share tab → Package Project
2. Choose what to include
3. Add description
4. Save location
5. Create package

**Result:**
- Single .ppkx file
- Contains everything
- Recipient can open and use immediately

---

## Part 10: Practice Exercise

### Exercise: Set Up Your Quinhagak Workspace

**Goal:** Create organized project structure following best practices

**Tasks:**

1. **Navigate to Documents/ArcGIS**
   - Verify folder exists
   - If not, create it

2. **Create Project Folder:**
   ```
   Documents/ArcGIS/Projects/Quinhagak_Analysis/
   ```

3. **Create Geodatabase:**
   - Name: `Quinhagak_Base.gdb`
   - Location: In project folder

4. **Create Feature Classes:**
   Inside geodatabase, create:
   - Points: `Community_Buildings`
   - Lines: `Roads`
   - Polygons: `Land_Parcels`

5. **Add Folder Connection:**
   - Connect to your project folder
   - Verify quick access in Catalog Pane

6. **Organize:**
   - Create subfolders: GPS_Data, Maps, Documentation
   - Move any existing data into structure

**Deliverable:**
- Clean, organized project structure
- Geodatabase with multiple feature classes
- Ready for real work!

---

## Summary

### Key Concepts

1. **Standard Location: Documents/ArcGIS**
   - Consistent across projects
   - Easy to find and backup

2. **Use Geodatabases**
   - Better than shapefiles
   - Better organization, performance, features

3. **Organize by Project**
   - One folder per project
   - All related files together

4. **Name Clearly**
   - Descriptive names
   - No spaces or special characters

5. **Backup Regularly**
   - Cloud storage
   - External drives
   - ArcGIS Online

### Workflow

1. Create project in Documents/ArcGIS/Projects
2. Use default .gdb or create new one
3. Create feature classes inside .gdb
4. Organize supporting files in subfolders
5. Backup important work

---

## Additional Resources

### Documentation
- [Geodatabase overview](https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/overview/what-is-a-geodatabase-.htm)
- [Create file geodatabase](https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/create-file-geodatabase.htm)
- [Organize projects](https://pro.arcgis.com/en/pro-app/latest/help/projects/organize-your-work.htm)

### Related Lessons
- Lesson 2: Adding Content (importing data)
- Lesson 11: Creating Layers (creating feature classes)
- Lesson 10: Exporting (backing up data)

---

## Next Steps

After mastering data organization:
1. Proceed to Lesson 4: Symbology
2. Learn to style your organized data
3. Create professional-looking maps

---

**Lesson Version:** 1.0
**Last Updated:** November 2025
**Module:** 4 - Spatial Analysis in ArcGIS Pro
**Location:** Quinhagak, Alaska
