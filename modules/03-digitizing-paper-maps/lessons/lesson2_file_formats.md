# Lesson 2: File Formats and Image Management

**Duration:** 30 minutes
**Difficulty:** Beginner
**Prerequisites:** Lesson 1 (Photography Basics)

---

## Overview

Understanding file formats is crucial for efficient map digitization workflows. This lesson explains the differences between .tiff, .jpg, and .dng files, when to use each format, and how to manage your digital files effectively.

---

## Learning Objectives

By the end of this lesson, you will:

1. ✅ Understand the differences between RAW (.dng), TIFF, and JPEG formats
2. ✅ Know when to use each file format
3. ✅ Understand compression and quality tradeoffs
4. ✅ Make informed decisions about file formats for different uses
5. ✅ Manage file sizes effectively
6. ✅ Organize digital files for efficient workflows

---

## Part 1: Understanding File Formats (15 minutes)

### The Three Main Formats

When digitizing maps, you'll work with three primary image formats:

**1. RAW (.dng - Digital Negative)**
**2. TIFF (.tiff - Tagged Image File Format)**
**3. JPEG (.jpg - Joint Photographic Experts Group)**

Each has specific advantages and uses.

---

### RAW Format (.dng)

**What is RAW?**
- Unprocessed data directly from camera sensor
- .dng = Digital Negative (Adobe's universal RAW format)
- Sony cameras create .dng files (or Sony's proprietary .arw)
- Contains ALL information captured by sensor

**Advantages:**
- ✅ Maximum quality - no information lost
- ✅ Full editing flexibility
- ✅ Adjust white balance after shooting
- ✅ Recover highlights and shadows
- ✅ No quality loss from editing
- ✅ Archival master file

**Disadvantages:**
- ❌ Very large file size (20-40 MB each)
- ❌ Requires processing software (Adobe Lightroom, Photoshop, etc.)
- ❌ Not all software can open RAW files
- ❌ Can't use directly in ArcGIS Pro without converting
- ❌ Slower to work with

**File Size Example:**
- RAW (.dng): 25-40 MB per image

**When to Use:**
- ✅ Archival master files
- ✅ When color accuracy critical
- ✅ When maximum quality needed
- ✅ When you might need to re-process later

**Workflow:**
1. Shoot in RAW
2. Import to Lightroom/Photoshop
3. Adjust white balance, exposure, color
4. Export as TIFF or JPEG for use

---

### TIFF Format (.tiff)

**What is TIFF?**
- Processed, high-quality raster format
- Widely supported across software
- Can be compressed (lossless) or uncompressed
- Standard for GIS and archival work

**Advantages:**
- ✅ High quality
- ✅ Lossless compression available
- ✅ Widely compatible (ArcGIS Pro, web browsers, etc.)
- ✅ Can include georeferencing information
- ✅ Professional standard for GIS
- ✅ No quality degradation from saving multiple times

**Disadvantages:**
- ❌ Large file size (5-20 MB typical)
- ❌ Slower to upload/download
- ❌ Takes more storage space
- ❌ Not ideal for web display (too large)

**File Size Example:**
- TIFF (uncompressed): 15-25 MB
- TIFF (LZW compressed): 5-15 MB

**When to Use:**
- ✅ Georeferencing in ArcGIS Pro
- ✅ Archival storage after processing
- ✅ When quality is priority over file size
- ✅ Professional GIS work

**Compression Options:**
- None (uncompressed) - Largest, highest quality
- LZW - Lossless compression, good balance
- JPEG - Lossy compression (defeats purpose of TIFF!)

**Recommended:** TIFF with LZW compression for GIS work

---

### JPEG Format (.jpg)

**What is JPEG?**
- Compressed image format
- Universal compatibility
- Small file size
- Lossy compression (quality loss)

**Advantages:**
- ✅ Small file size (1-5 MB typical)
- ✅ Fast to upload/download
- ✅ Opens in any software
- ✅ Good for web sharing
- ✅ Widely compatible
- ✅ Can be used in ArcGIS Pro for georeferencing

**Disadvantages:**
- ❌ Lossy compression (quality degraded)
- ❌ Quality degrades each time you save
- ❌ Not suitable for archival masters
- ❌ Compression artifacts (especially in text/lines)
- ❌ Limited editing flexibility

**File Size Example:**
- JPEG (high quality): 3-8 MB
- JPEG (medium quality): 1-3 MB
- JPEG (low quality): 500 KB - 1 MB

**When to Use:**
- ✅ Uploading to ArcGIS Online (faster)
- ✅ Sharing via email
- ✅ Web display
- ✅ Quick reference copies
- ✅ When storage space limited

**Quality Settings:**
- Maximum/100% - Use for GIS work
- High/90% - Good for most uses
- Medium/75% - Only for quick reference
- Low/50% - Avoid for maps

**Recommended:** JPEG at 90-100% quality for georeferencing

---

## Part 2: Compression and Quality (10 minutes)

### Understanding Compression

**Lossless Compression:**
- Reduces file size without losing data
- Can be decompressed to exact original
- Examples: LZW (TIFF), PNG
- Smaller size reduction (maybe 50%)

**Lossy Compression:**
- Reduces file size by discarding data
- Cannot recover original quality
- Example: JPEG
- Larger size reduction (up to 90%)

**Visual Demonstration:**

Zoom to 400% and compare:
- RAW/TIFF: Text crisp, lines sharp, no artifacts
- JPEG (high): Very slight softness
- JPEG (medium): Visible softness, minor artifacts
- JPEG (low): Obvious artifacts, fuzzy text, blocky areas

### JPEG Compression Artifacts

**What are artifacts?**
- Unwanted visual distortions from compression
- Especially visible in:
  - Text
  - Fine lines
  - Sharp edges
  - Areas of solid color

**8x8 Pixel Blocks:**
- JPEG compresses in 8x8 pixel blocks
- Can create visible "blockiness"
- More visible at lower quality settings
- Less visible in photographs, more visible in maps/text

**Why This Matters for Maps:**
Maps have lots of:
- Text (labels, legends)
- Thin lines (roads, boundaries)
- Sharp edges (symbols, parcels)
- Solid colors (water bodies, zones)

All of these show JPEG artifacts more than natural photos!

**Solution:** Use high quality JPEG (90-100%) or TIFF for maps

---

## Part 3: Choosing the Right Format (10 minutes)

### Decision Tree

**Question 1: Is this the master archival copy?**
- YES → RAW (.dng) or TIFF (uncompressed)
- NO → Continue to Question 2

**Question 2: Will you georeference this in ArcGIS Pro?**
- YES → TIFF (LZW compressed) or JPEG (high quality)
- NO → Continue to Question 3

**Question 3: Will you share this on web/email?**
- YES → JPEG (90-100% quality)
- NO → TIFF

**Question 4: Is storage space very limited?**
- YES → JPEG (high quality)
- NO → TIFF

### Recommended Workflow for Quinhagak Project

**Phase 1: Capture**
- Shoot in RAW (.dng)
- Maximum quality, full flexibility

**Phase 2: Processing**
- Import RAW to Lightroom/Photoshop
- Adjust white balance using color card
- Correct exposure, contrast
- Crop if needed
- Export as TIFF (LZW compression)

**Phase 3: Georeferencing**
- Use TIFF in ArcGIS Pro
- Georeference
- Export georeferenced TIFF

**Phase 4: Sharing**
- Create JPEG version for ArcGIS Online
- Upload JPEG (faster, smaller)
- Keep TIFF as master

**Storage:**
- Keep RAW files as ultimate backup
- Keep processed TIFF as working master
- JPEG for distribution

---

## Part 4: File Size Management (10 minutes)

### Comparing File Sizes

**Example: One Quinhagak Map**

| Format | Settings | File Size | Use Case |
|--------|----------|-----------|----------|
| RAW (.dng) | From camera | 28 MB | Archival master |
| TIFF | Uncompressed | 22 MB | Maximum quality |
| TIFF | LZW compression | 8 MB | **GIS work** ⭐ |
| JPEG | 100% quality | 4 MB | Web sharing |
| JPEG | 90% quality | 2 MB | **AGOL upload** ⭐ |
| JPEG | 75% quality | 1 MB | Quick reference |

**For 40 Maps (Quinhagak Project):**

| Format | File Size Each | Total for 40 |
|--------|----------------|--------------|
| RAW (.dng) | 28 MB | 1,120 MB (1.1 GB) |
| TIFF (LZW) | 8 MB | 320 MB |
| JPEG (90%) | 2 MB | 80 MB |

### Storage Considerations

**SD Card:**
- 32 GB card holds ~1,000 RAW files
- For 40 maps: ~1.1 GB needed
- Plenty of space!

**Computer Hard Drive:**
- Keep RAW + TIFF + JPEG
- Per map: 28 + 8 + 2 = 38 MB
- For 40 maps: ~1.5 GB total
- Modern computers have plenty of space

**ArcGIS Online:**
- Free tier: Limited storage
- Organizational account: More storage
- Upload JPEG to save space
- 40 maps at 2 MB each = 80 MB (manageable!)

**External Backup:**
- 1 TB external drive: $50-100
- Can store thousands of maps
- Good investment for archival work

### Reducing File Size (If Needed)

**If storage is truly limited:**

**Option 1: JPEG Quality**
- Try 85% quality instead of 90%
- Often hard to see difference
- Significant size savings

**Option 2: Image Dimensions**
- If original is 6000x4000 pixels
- Resize to 4000x2667 pixels
- Still excellent quality for most uses
- File size reduced ~50%

**Option 3: Targeted Storage**
- Keep RAW of most important maps only
- TIFF for georeferenced maps
- JPEG for reference copies

**What NOT to Do:**
- ❌ Don't use low-quality JPEG for georeferencing
- ❌ Don't discard RAW files until project complete
- ❌ Don't compress so much that maps become unusable

---

## Part 5: File Management Best Practices (10 minutes)

### Naming Conventions (Review)

**Include:**
- Location: Quinhagak
- Map type: ANCSA, Infrastructure, LandUse
- Year: 1982, 1975, etc.
- Sheet number (if multi-sheet): 01, 02
- Version (if multiple edits): v1, v2

**Examples:**
```
Quinhagak_ANCSA_14c_1982.dng
Quinhagak_ANCSA_14c_1982.tiff
Quinhagak_ANCSA_14c_1982.jpg
Quinhagak_Infrastructure_1975_Sheet01.dng
Quinhagak_LandUse_1990_v2.tiff
```

### Folder Organization

```
Quinhagak_Map_Digitization/
│
├── 01_RAW_Masters/
│   ├── Quinhagak_ANCSA_14c_1982.dng
│   └── Quinhagak_Infrastructure_1975.dng
│
├── 02_Processed_TIFF/
│   ├── Quinhagak_ANCSA_14c_1982.tiff
│   └── Quinhagak_Infrastructure_1975.tiff
│
├── 03_Georeferenced/
│   ├── Quinhagak_ANCSA_14c_1982_georef.tiff
│   └── Quinhagak_Infrastructure_1975_georef.tiff
│
├── 04_For_Web_JPEG/
│   ├── Quinhagak_ANCSA_14c_1982.jpg
│   └── Quinhagak_Infrastructure_1975.jpg
│
└── 05_Documentation/
    ├── Map_Inventory.xlsx
    ├── Georeferencing_Notes.docx
    └── Control_Points.xlsx
```

### Metadata and Documentation

**For Each Map, Document:**
- Original physical location (which box, folder)
- Date photographed
- Camera settings used
- Condition notes
- Georeferencing control points (if applicable)
- Who did the work
- Date uploaded to AGOL
- Group/sharing settings

**Create Spreadsheet:**

| Map Name | Date Photo | Format | Georeferenced | Uploaded AGOL | Notes |
|----------|-----------|--------|---------------|---------------|-------|
| ANCSA 14c 1982 | 10/15/24 | RAW, TIFF, JPG | Yes | Yes | Good condition |
| Infrastructure 1975 | 10/15/24 | RAW, TIFF, JPG | Yes | Yes | Slight fading |

---

## Hands-On Exercise

### Exercise: Format Comparison

**You will need:**
- One photographed map
- Lightroom, Photoshop, or similar software
- 20 minutes

**Steps:**

1. **Export Same Map in Different Formats**
   - Export as TIFF (uncompressed)
   - Export as TIFF (LZW compressed)
   - Export as JPEG (100% quality)
   - Export as JPEG (90% quality)
   - Export as JPEG (75% quality)

2. **Compare File Sizes**
   - Note file size of each
   - Calculate size reduction percentages
   - Create comparison table

3. **Visual Quality Assessment**
   - Open each file
   - Zoom to 200-400%
   - Examine text, lines, edges
   - Note where artifacts appear
   - Identify lowest acceptable quality

4. **Import to ArcGIS Pro**
   - Try adding each format
   - Note any compatibility issues
   - Check display quality
   - Assess load time

5. **Make Recommendations**
   - Which format for archival master?
   - Which format for georeferencing?
   - Which format for AGOL upload?
   - Justify your choices

---

## Key Takeaways

1. **RAW (.dng)** = Maximum quality, archival master, requires processing
2. **TIFF** = High quality, GIS-compatible, professional standard
3. **JPEG** = Small size, web-friendly, lossy compression
4. **Workflow:** Shoot RAW → Process to TIFF → Share as JPEG
5. **For georeferencing:** TIFF (LZW) or JPEG (90-100%)
6. **For AGOL upload:** JPEG (90%) good balance of quality and size
7. **Always keep masters:** Don't delete RAW files until project complete
8. **Document everything:** Future you will thank you

---

## Assessment Questions

1. What does "lossless" compression mean?
2. Why is JPEG considered "lossy"?
3. Which format would you use for an archival master copy? Why?
4. Which format would you upload to ArcGIS Online? Why?
5. What is the advantage of TIFF over JPEG for georeferencing?
6. Why shoot in RAW if you'll convert to TIFF anyway?
7. What quality setting would you use for JPEG intended for georeferencing?

---

## Next Steps

- [Lesson 3: Georeferencing in ArcGIS Pro →](./lesson3_georeferencing.md)
- Experiment with different formats
- Develop your processing workflow
- Set up organized folder structure

---

**Lesson Version:** 1.0
**Last Updated:** November 2025
