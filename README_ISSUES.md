# Repository README Issues and Fixes Needed

**Date:** November 10, 2025

---

## 1. Main README.md - Broken/Outdated Links

### Module Links That Need Updating:

**Line 59:** Module 5 link is outdated
```markdown
Current: 5. **[Cartography](./modules/05-cartography/)**
Should be: 5. **[Cartography with ArcGIS Online](./modules/05-cartography-arcgis-online/)**
```

**Lines 56-61, 66:** Links point to placeholder modules that don't have content yet:
- `./modules/03-digitizing-paper-maps/` → Points to `modules/03-module-name/` (placeholder)
- `./modules/04-spatial-analysis/` → Points to `modules/04-module-name/` (placeholder)
- `./modules/06-remote-sensing-satellite/` → Points to `modules/06-module-name/` (placeholder)
- `./modules/08-change-detection/` → Points to `modules/08-module-name/` (placeholder)
- `./modules/09-river-monitoring/` → Points to `modules/09-module-name/` (placeholder)

### Case Study Link:

**Line 72:** Case study link may not exist
```markdown
Current: ### [October 2025 Typhoon Damage Assessment](./case-studies/typhoon-damage-2025/)
Status: Need to verify if this directory/content exists
```

### Documentation Links:

**Lines 92-94:** Links that may not exist:
- `./docs/training-schedule.md`
- `./docs/instructor-notes.md`
- `./docs/assessments/`

---

## 2. Module README.md Files - Missing or Placeholder Content

### Modules WITH Content (✅ Good):

1. **Module 1: ArcGIS Online Basics**
   - Has: `module1_readme.md` (comprehensive, 396 lines)
   - Missing: `README.md`
   - **Action:** Copy module1_readme.md to README.md

2. **Module 2: Field Data Collection**
   - Has: `README.md` (comprehensive content)
   - **Status:** ✅ Good, no action needed

3. **Module 5: Cartography with ArcGIS Online**
   - Has: `module5_readme.md` (comprehensive, 640+ lines)
   - Has: `README.md` (PLACEHOLDER - only 25 lines)
   - **Action:** Replace README.md with module5_readme.md or copy content

4. **Module 7: Remote Sensing: Satellite & Drones**
   - Has: `module7_readme.md` (comprehensive, 800+ lines)
   - Has: `README.md` (PLACEHOLDER - only 25 lines)
   - **Action:** Replace README.md with module7_readme.md or copy content

### Placeholder Module Directories (❌ Need Cleanup):

These are empty placeholder directories created by the template script:

- `modules/02-module-name/` (duplicate - real Module 2 exists as 02-field-data-collection)
- `modules/03-module-name/` (no content)
- `modules/04-module-name/` (no content)
- `modules/06-module-name/` (no content)
- `modules/08-module-name/` (no content)
- `modules/09-module-name/` (no content)

**Recommended Action:** Delete these placeholder directories since they're not being used

---

## 3. Specific Issues by Module

### Module 01: ArcGIS Online Basics ✅
- **Status:** Has complete content in `module1_readme.md`
- **Issue:** Missing `README.md` symlink or copy
- **Fix:**
  ```bash
  cp modules/01-arcgis-online-basics/module1_readme.md modules/01-arcgis-online-basics/README.md
  ```

### Module 02: Field Data Collection ✅
- **Status:** Complete and working
- **No issues**

### Module 03: Digitizing Paper Maps ❌
- **Status:** Placeholder directory only (`03-module-name/`)
- **Content:** None
- **Fix:** Create content OR remove from main README until ready

### Module 04: Spatial Analysis ❌
- **Status:** Placeholder directory only (`04-module-name/`)
- **Content:** None
- **Fix:** Create content OR remove from main README until ready

### Module 05: Cartography with ArcGIS Online ⚠️
- **Status:** Has complete content BUT README.md is placeholder
- **Content:** `module5_readme.md` has full content (640 lines)
- **Fix:**
  ```bash
  cp modules/05-cartography-arcgis-online/module5_readme.md modules/05-cartography-arcgis-online/README.md
  ```

### Module 06: Remote Sensing - Satellite ❌
- **Status:** Placeholder directory only (`06-module-name/`)
- **Content:** None
- **Fix:** Create content OR remove from main README until ready

### Module 07: Remote Sensing: Satellite & Drones ⚠️
- **Status:** Has complete content BUT README.md is placeholder
- **Content:** `module7_readme.md` has full content (800+ lines)
- **Fix:**
  ```bash
  cp modules/07-remote-sensing-satellite-and-drones/module7_readme.md modules/07-remote-sensing-satellite-and-drones/README.md
  ```

### Module 08: Change Detection ❌
- **Status:** Placeholder directory only (`08-module-name/`)
- **Content:** None
- **Fix:** Create content OR remove from main README until ready

### Module 09: River Monitoring ❌
- **Status:** Placeholder directory only (`09-module-name/`)
- **Content:** None
- **Fix:** Create content OR remove from main README until ready

---

## 4. Recommended Action Plan

### Immediate Fixes (Quick):

**1. Fix Module README.md files (copy content from module*_readme.md):**
```bash
# Module 1
cp modules/01-arcgis-online-basics/module1_readme.md modules/01-arcgis-online-basics/README.md

# Module 5
cp modules/05-cartography-arcgis-online/module5_readme.md modules/05-cartography-arcgis-online/README.md

# Module 7
cp modules/07-remote-sensing-satellite-and-drones/module7_readme.md modules/07-remote-sensing-satellite-and-drones/README.md
```

**2. Update main README.md Module 5 link:**
```markdown
Line 59: Change from:
5. **[Cartography](./modules/05-cartography/)**

To:
5. **[Cartography with ArcGIS Online](./modules/05-cartography-arcgis-online/)**
```

**3. Remove placeholder module directories:**
```bash
rm -rf modules/02-module-name
rm -rf modules/03-module-name
rm -rf modules/04-module-name
rm -rf modules/06-module-name
rm -rf modules/08-module-name
rm -rf modules/09-module-name
```

### Medium-Term Fixes:

**4. Update main README.md to mark incomplete modules:**

Change modules 3, 4, 6, 8, 9 in the main README to indicate they're "Coming Soon" or "In Development":

```markdown
### Foundational Modules (November 2025)

1. **[ArcGIS Online Basics](./modules/01-arcgis-online-basics/)** ✅ - User registration, dashboards, Story Maps, web maps
2. **[Field Data Collection](./modules/02-field-data-collection/)** ✅ - Survey123, Field Maps, offline workflows, GNSS integration
3. **Digitizing Paper Maps** 🚧 *(In Development)* - Georeferencing, raster vs vector data
4. **Spatial Analysis** 🚧 *(In Development)* - Geoprocessing tools, buffers, clip operations
5. **[Cartography with ArcGIS Online](./modules/05-cartography-arcgis-online/)** ✅ - Map design, vector data, web publishing
6. **Remote Sensing: Satellite** 🚧 *(In Development)* - Landsat, Sentinel, Wayback imagery
7. **[Remote Sensing: Satellite & Drones](./modules/07-remote-sensing-satellite-and-drones/)** ✅ - Satellite imagery analysis and UAS data collection

### Advanced Modules (Summer 2026)

8. **Change Detection** 🚧 *(Planned for 2026)* - Temporal analysis of landscape change
9. **River Monitoring** 🚧 *(Planned for 2026)* - River migration, avulsion prediction, salmon mapping
```

**5. Verify case study and docs directories exist or remove links**

---

## 5. Summary Statistics

### Modules Status:
- ✅ **Complete with README:** 3 modules (1, 2, 7 after fixes)
- ⚠️ **Complete but README is placeholder:** 2 modules (5, 7) - EASY FIX
- ❌ **Placeholder directories only:** 5 modules (3, 4, 6, 8, 9)

### Files to Fix:
- Main README.md: 1 link, multiple module status updates
- Module README.md files: 3 need copying from module*_readme.md
- Placeholder directories: 6 to remove

---

## 6. Quick Fix Script

Here's a bash script to make the immediate fixes:

```bash
#!/bin/bash
# Fix repository README issues

echo "Fixing Module README files..."

# Copy comprehensive readmes to README.md
cp modules/01-arcgis-online-basics/module1_readme.md modules/01-arcgis-online-basics/README.md
cp modules/05-cartography-arcgis-online/module5_readme.md modules/05-cartography-arcgis-online/README.md
cp modules/07-remote-sensing-satellite-and-drones/module7_readme.md modules/07-remote-sensing-satellite-and-drones/README.md

echo "Removing placeholder module directories..."

# Remove placeholder directories
rm -rf modules/02-module-name
rm -rf modules/03-module-name
rm -rf modules/04-module-name
rm -rf modules/06-module-name
rm -rf modules/08-module-name
rm -rf modules/09-module-name

echo "Done! Now manually update main README.md:"
echo "  - Line 59: Update Module 5 link to 05-cartography-arcgis-online"
echo "  - Lines 56-66: Mark incomplete modules as 'In Development' or remove links"
```

---

## Next Steps:

1. Run the quick fix script (or manually execute the commands)
2. Manually edit main README.md to update module links and statuses
3. Commit changes with message: "Fix module README files and remove placeholder directories"
4. Push to GitHub
