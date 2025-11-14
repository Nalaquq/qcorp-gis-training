# Lesson 5: Uploading to ArcGIS Online

**Duration:** 45 minutes
**Difficulty:** Beginner to Intermediate
**Prerequisites:** Georeferenced map ready to share

---

## Overview

Once you've georeferenced your maps, the next step is sharing them with the community through ArcGIS Online. This lesson teaches you how to export from ArcGIS Pro, upload to ArcGIS Online, organize content in Groups, and make your work accessible.

---

## Learning Objectives

By the end of this lesson, you will:

1. ✅ Export georeferenced maps from ArcGIS Pro
2. ✅ Upload rasters to ArcGIS Online
3. ✅ Add metadata (title, tags, description)
4. ✅ Join and share to Groups
5. ✅ Set appropriate sharing permissions
6. ✅ Test maps in web map viewer
7. ✅ Manage and organize uploaded content

---

## Part 1: Exporting from ArcGIS Pro (10 minutes)

### Why Export?

**Your georeferenced map in ArcGIS Pro:**
- Saved as .tiff on your computer
- Includes georeferencing information
- Ready to share

**To upload to ArcGIS Online, you need:**
- Properly formatted file
- Reasonable file size
- Georeferencing intact

### Export Method 1: Export Raster (Recommended)

**Step 1: Right-click georeferenced layer**
- In Contents pane
- Right-click on georeferenced raster
- Data → Export Raster

**Step 2: Set Export Parameters**

**Output Location:**
- Choose folder you can find easily
- Example: Documents/Quinhagak_Maps_Export/

**Output Name:**
- Use descriptive name
- Example: Quinhagak_ANCSA_14c_1982_geo.tif

**Format:**
- **TIFF** - Lossless, high quality (larger file)
- **JPEG** - Compressed, smaller file (recommended for AGOL)
- For AGOL: JPEG at 90-100% quality is good balance

**Coordinate System:**
- Keep as-is (should be georeferenced already)
- Or specify if needed

**Compression (if TIFF):**
- LZW - Lossless compression
- JPEG - Lossy compression
- None - Uncompressed (largest)

**For AGOL Upload: Choose JPEG format**

**Step 3: Run Export**
- Click Run
- Wait for processing (may take a minute)
- Verify file created in output location

**Step 4: Verify Export**
- Add exported file to new map in ArcGIS Pro
- Check that georeferencing preserved
- Verify alignment with basemap
- If good, ready to upload!

### Export Method 2: Share as Web Layer (Advanced)

**Direct Upload to AGOL:**
- Right-click layer → Sharing → Share As Web Layer
- Publishes directly to ArcGIS Online
- More complex settings
- Creates image service

**When to use:**
- Large rasters
- Need to serve tiles
- Advanced publishing needs

**For Quinhagak project:** Export Raster method is simpler and sufficient

---

## Part 2: Uploading to ArcGIS Online (15 minutes)

### Sign In to ArcGIS Online

**Step 1: Navigate to ArcGIS Online**
- Go to: https://www.arcgis.com
- Or: Your organization's URL
- Example: quinhagak.maps.arcgis.com

**Step 2: Sign In**
- Click "Sign In"
- Enter username and password
- Should be organizational account
- Verify you're in correct organization

### Upload Your Georeferenced Map

**Step 1: Go to Content**
- Click "Content" tab at top
- This shows your personal content
- You should see your content folder

**Step 2: Add Item**
- Click "Add Item" button
- Choose "From your computer"

**Step 3: Select File**
- Click "Choose File"
- Browse to your exported raster
- Select the .tif or .jpg file
- Click Open

**Step 4: Set Item Details**

This is IMPORTANT - good metadata helps others find and use your map!

**Title:**
- Descriptive and clear
- Include location, type, year
- Example: "Quinhagak ANCSA 14(c) Conveyance Survey Map - 1982"

**Tags:**
- Keywords for searching
- Separate with commas
- Example: quinhagak, ANCSA, historical, survey, 1982, land, map
- Include:
  - Location (Quinhagak, Alaska)
  - Type (ANCSA, survey, historical)
  - Year (1982)
  - Subject (land, conveyance)

**Summary:**
- Brief description (1-3 sentences)
- What is this map?
- Why is it important?
- Example: "Georeferenced ANCSA 14(c) land conveyance survey map from 1982 showing village lands. Digitized from paper map in Qanirtuuq Land Manager's office. Georeferenced using village features and PLSS grid."

**Description (optional but recommended):**
- More detailed information
- How was it created?
- What does it show?
- How to use it?
- Known limitations?

**Credits:**
- Who created it?
- Who photographed and georeferenced it?
- Example: "Original survey by BLM. Photographed and georeferenced by [Your Name], Quinhagak GIS Training Program, October 2024."

**Terms of Use (optional):**
- Any restrictions on use?
- Usually: Available for community use

**Step 5: Add Item**
- Click "Add Item"
- Upload begins
- Progress bar shows upload
- May take several minutes for large files

**Step 6: Wait for Processing**
- After upload, AGOL processes the file
- Creates preview
- Extracts metadata
- Status shows "Processing" then "Ready"

---

## Part 3: Managing Item Settings (10 minutes)

### Item Page

Once uploaded, you'll see the Item Page for your map.

**Tabs:**
- **Overview** - Details, description, metadata
- **Data** - View/download the actual file
- **Usage** - Statistics on views and usage
- **Settings** - Publishing and sharing settings

### Setting Sharing Permissions

**This is critical - controls who can see your map!**

**Step 1: Click "Share" Button**
- Top right of item page
- Opens sharing dialog

**Step 2: Choose Sharing Level**

**Owner:**
- Only you can see
- Default when first uploaded
- Use for: Work in progress

**Organization:**
- Anyone in your organization can see
- Good for: Internal work

**Everyone (Public):**
- Anyone on internet can see
- Good for: Community resources, public information

**Groups:**
- Share with specific groups
- Best option for Quinhagak project!

**Step 3: Share to Group**

**For Quinhagak Georeferenced Maps:**
1. Check "Groups" option
2. Select "Quinhagak Georeferenced Maps" group
3. This shares to group members
4. Group can be public or private

**Real Example:** https://arcg.is/0H8S1y1

### Joining a Group

**If Group Already Exists:**

**Step 1: Find Group**
- Click "Groups" tab
- Search for group name
- Example: "Quinhagak Georeferenced Maps"

**Step 2: Request to Join**
- Click on group
- Click "Join this group"
- May require approval from group owner
- Or may be auto-join

**Step 3: Share Your Content**
- Once member, can share to group
- All group members see shared content

**If Group Doesn't Exist:**

You or instructor can create one!

**Create Group:**
1. Groups → Create a Group
2. Name: "Quinhagak Georeferenced Maps"
3. Summary: "Historical and current maps of Quinhagak area, digitized and georeferenced for community use"
4. Tags: quinhagak, maps, historical
5. Access: Public or Organization
6. Who can contribute: Group members
7. Create

### Adding Thumbnail Image

**What is Thumbnail?**
- Small preview image
- Shows in search results
- Helps identify content

**How to Add:**
1. Item page → Edit Thumbnail
2. Choose:
   - Generate from item (auto-creates from map)
   - Upload image (custom screenshot)
3. Save

**Tip:** Auto-generate works well for maps!

---

## Part 4: Using Your Map in a Web Map (10 minutes)

### Test Your Georeferenced Map

**Important:** Always test that upload worked correctly!

**Step 1: Create New Web Map**
- Top menu → Map
- Opens Map Viewer
- Blank map with basemap

**Step 2: Add Your Georeferenced Map**
- Click "Add" → Browse Living Atlas Layers
- Switch to "My Content"
- Find your uploaded map
- Click "+" to add to map

**Step 3: Verify Alignment**
- Map should appear in correct location
- Should overlay basemap properly
- Zoom in to check details
- Pan around to test different areas

**If map appears in wrong location:**
- ❌ Georeferencing didn't export properly
- Go back to ArcGIS Pro
- Re-export with georeferencing
- Re-upload

**If map looks good:**
- ✅ Success! Georeferencing preserved
- Map is ready for use

### Adjusting Layer Properties

**Transparency:**
- Layer options → Transparency
- Set to 40-60%
- Can see basemap underneath
- Helps compare historical to current

**Blend Mode:**
- Try different blend modes
- "Multiply" often works well for old maps
- Helps overlay on basemap

**Visibility Range:**
- Set zoom levels where layer appears
- Prevent display when zoomed out (if desired)

### Saving and Sharing Web Map

**Step 1: Save Web Map**
- Click "Save" → Save As
- Title: "Quinhagak Historical Maps"
- Tags: quinhagak, historical, comparison
- Summary: "Georeferenced historical maps overlaid on current basemap"
- Save

**Step 2: Share Web Map**
- Same sharing options as items
- Share to same group
- Or make public

**Now others can:**
- View your georeferenced maps
- Compare historical to current
- Use in their own projects

---

## Part 5: Best Practices and Organization (10 minutes)

### Naming Conventions for AGOL

**Consistent Naming:**
All Quinhagak maps follow same pattern:
- Quinhagak_[Type]_[Year]
- Example: Quinhagak_ANCSA_14c_1982
- Example: Quinhagak_Infrastructure_1975

**Benefits:**
- Easy to find related maps
- Sort alphabetically
- Professional appearance
- Clear communication

### Tagging Strategy

**Always Include:**
- Location: quinhagak, alaska
- Type: historical, survey, ANCSA, infrastructure, etc.
- Year: 1982, 1975, etc.
- General: maps, georeferenced, digitized

**Be Consistent:**
- Use same tags across related items
- Makes searching easier
- Helps group related content

### Organizing with Folders

**Create Folders in My Content:**

Example structure:
- Georeferenced_Maps_Historical
- Georeferenced_Maps_Current
- Web_Maps
- Field_Data

**Move Items to Folders:**
- Select items
- Move to folder
- Keeps content organized

### Managing Multiple Maps

**For 40 Maps:**
- Upload in batches
- Set aside time (uploading takes time)
- Use consistent naming
- Tag consistently
- Share all to same group

**Track Progress:**
Create spreadsheet:
| Map Name | Photographed | Georeferenced | Uploaded | Shared to Group |
|----------|-------------|---------------|----------|-----------------|
| ANCSA 14c 1982 | ✓ | ✓ | ✓ | ✓ |
| Infrastructure 1975 | ✓ | ✓ | ✓ | ✓ |

---

## Real-World Success: Quinhagak Group

**What Was Accomplished:**
- Approximately 40 maps digitized in one day
- All uploaded to ArcGIS Online
- All shared to group: https://arcg.is/0H8S1y1
- Accessible to community

**Group Benefits:**
- Centralized location for all maps
- Easy to find related content
- Community can access all maps
- Preserved for future use

**Impact:**
- Historical knowledge preserved
- Land records accessible digitally
- Supports land management decisions
- Educational resource

---

## Practice Exercise

### Exercise: Upload and Share Your Map

**You will need:**
- Georeferenced map from Lesson 3
- ArcGIS Online account
- 30 minutes

**Steps:**

1. **Export from ArcGIS Pro**
   - Export as JPEG (90% quality)
   - Note file size and location

2. **Upload to ArcGIS Online**
   - Sign in to AGOL
   - Add item from computer
   - Complete all metadata fields
   - Be thorough and descriptive

3. **Set Sharing**
   - Share to appropriate group
   - Or share with organization
   - Document sharing settings

4. **Create Test Web Map**
   - Create new web map
   - Add your uploaded map
   - Verify alignment
   - Adjust transparency
   - Save web map

5. **Share Web Map**
   - Share web map to group
   - Test access from different account (if possible)

6. **Document**
   - URL of uploaded item
   - URL of web map
   - Sharing settings
   - Any issues encountered

---

## Troubleshooting

### Problem: Upload Fails

**Possible Causes:**
- File too large
- Internet connection interrupted
- File format not supported
- Storage limit reached

**Solutions:**
- Reduce file size (export as smaller JPEG)
- Check internet connection
- Try different browser
- Check AGOL storage quota

### Problem: Map Appears in Wrong Location

**Cause:** Georeferencing information not included

**Solution:**
- Re-export from ArcGIS Pro
- Ensure georeferencing saved
- Check coordinate system
- Re-upload

### Problem: Can't Find Uploaded Item

**Cause:** Looking in wrong location

**Solution:**
- Check "My Content"
- Check correct folder
- Search by name
- Check if upload completed

### Problem: Others Can't See Map

**Cause:** Sharing settings

**Solution:**
- Check sharing permissions
- Ensure shared to correct group
- Verify others are group members
- Check organization settings

---

## Key Takeaways

1. **Export from ArcGIS Pro** as JPEG for smaller file size
2. **Complete metadata thoroughly** - helps others find and use maps
3. **Use consistent naming and tagging** - professional and searchable
4. **Share to Groups** - best way to organize community content
5. **Always test in web map** - verify georeferencing preserved
6. **Organize content with folders** - keep things tidy
7. **Document what you upload** - track your work

---

## Assessment Questions

1. What file format is recommended for uploading to ArcGIS Online? Why?
2. What should you include in the "Tags" field?
3. What's the difference between sharing to "Organization" vs "Groups"?
4. How can you verify that georeferencing was preserved in the upload?
5. Why is metadata (title, tags, description) important?
6. What is a Group and why use it for Quinhagak maps?
7. How can you make content public vs. private?

---

## Next Steps

- [Lesson 6: Map Organization and Prioritization →](./lesson6_organization.md)
- Upload your georeferenced maps
- Join Quinhagak Georeferenced Maps group
- Share your work with the community!

---

## Resources

- [ArcGIS Online Help - Add Items](https://doc.arcgis.com/en/arcgis-online/manage-data/add-items.htm)
- [Share Items](https://doc.arcgis.com/en/arcgis-online/share-maps/share-items.htm)
- [Quinhagak Georeferenced Maps Group](https://arcg.is/0H8S1y1)

---

**Lesson Version:** 1.0
**Last Updated:** November 2025
**Community Achievement:** 40 maps uploaded in one day!
