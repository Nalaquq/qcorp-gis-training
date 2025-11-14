# Alaska EPSG Codes Quick Reference

## What is an EPSG Code?

An EPSG code is a unique identifier for a coordinate system. It's named after the European Petroleum Survey Group (now part of IOGP - International Association of Oil & Gas Producers).

**Why it matters:**
- Easier than typing full coordinate system name
- Universally recognized
- Required for many GIS operations
- Makes sharing data easier

**How to use:**
- Search for EPSG code in ArcGIS Pro coordinate system selector
- Use epsg.io website to look up codes
- Include in metadata for your data

---

## Essential Codes for Quinhagak

### WGS 84 (GPS Standard)

**EPSG:4326**
- **Name:** WGS 84
- **Type:** Geographic (latitude/longitude)
- **Units:** Degrees
- **Use for:**
  - GPS data
  - Global mapping
  - Web applications
  - Data sharing

**When you see coordinates like:**
- Latitude: 59.76°
- Longitude: -161.9°
- **This is WGS84 (EPSG:4326)**

---

### Alaska State Plane Zone 7 (Quinhagak Area)

**EPSG:26937**
- **Name:** NAD83 / Alaska Albers
- **Type:** Projected (X, Y)
- **Units:** Feet
- **Use for:**
  - Local analysis in Quinhagak
  - Accurate distance measurements
  - Parcel mapping
  - Infrastructure planning

**When you see coordinates like:**
- X: 1,847,000 feet
- Y: 460,000 feet
- **This is likely Alaska State Plane Zone 7**

**Area covered:** Southwest Alaska including Quinhagak, Bethel region

**View details:** https://epsg.io/26937

---

## All Alaska State Plane Zones

Alaska is divided into 10 State Plane zones. Each zone is optimized for accuracy in its specific region.

### Zone 1 (Panhandle)
**EPSG:26931** - NAD83 / Alaska State Plane Zone 1
- **Area:** Southeast Alaska (Juneau, Sitka, Ketchikan)
- **Units:** Feet

### Zone 2 (Southeast)
**EPSG:26932** - NAD83 / Alaska State Plane Zone 2
- **Area:** Southeast Alaska coast
- **Units:** Feet

### Zone 3 (South-Central Coast)
**EPSG:26933** - NAD83 / Alaska State Plane Zone 3
- **Area:** South-central coast (Cordova, Valdez)
- **Units:** Feet

### Zone 4 (South-Central)
**EPSG:26934** - NAD83 / Alaska State Plane Zone 4
- **Area:** Anchorage, Matanuska-Susitna Valley
- **Units:** Feet

### Zone 5 (Southwest Peninsula)
**EPSG:26935** - NAD83 / Alaska State Plane Zone 5
- **Area:** Alaska Peninsula, Aleutians
- **Units:** Feet

### Zone 6 (Southwest)
**EPSG:26936** - NAD83 / Alaska State Plane Zone 6
- **Area:** Bristol Bay region
- **Units:** Feet

### Zone 7 (West) - **QUINHAGAK IS HERE**
**EPSG:26937** - NAD83 / Alaska State Plane Zone 7
- **Area:** Yukon-Kuskokwim Delta (Quinhagak, Bethel)
- **Units:** Feet

### Zone 8 (Interior)
**EPSG:26938** - NAD83 / Alaska State Plane Zone 8
- **Area:** Interior Alaska (Fairbanks, Yukon River)
- **Units:** Feet

### Zone 9 (Northwest)
**EPSG:26939** - NAD83 / Alaska State Plane Zone 9
- **Area:** Northwest Alaska (Nome, Kotzebue)
- **Units:** Feet

### Zone 10 (North Slope)
**EPSG:26940** - NAD83 / Alaska State Plane Zone 10
- **Area:** North Slope (Utqiaġvik/Barrow, Prudhoe Bay)
- **Units:** Feet

---

## Other Common Alaska Projections

### Alaska Albers Equal Area

**EPSG:3338**
- **Name:** NAD83 / Alaska Albers
- **Type:** Projected
- **Units:** Meters
- **Use for:**
  - Statewide mapping
  - Regional analysis
  - Preserves area (good for size comparisons)
  - Common for Alaska-wide GIS projects

**Advantages:**
- Optimized for entire state
- Equal-area (good for calculating areas)
- Single projection for all of Alaska

**Disadvantages:**
- Not as accurate as State Plane for local work
- Distorts shape somewhat

---

### Web Mercator (For Web Maps)

**EPSG:3857**
- **Name:** WGS 84 / Pseudo-Mercator
- **Type:** Projected
- **Units:** Meters
- **Use for:**
  - Web maps (Google Maps, ArcGIS Online)
  - Online basemaps
  - Web applications

**Important Notes:**
- ⚠️ **NOT recommended for analysis or measurement!**
- Designed for display, not accuracy
- Distorts area significantly at high latitudes
- Makes Greenland look huge!
- Alaska appears distorted

**When to use:**
- Only for web display
- Never for distance/area calculations
- Not for scientific analysis

---

## UTM Zones (Alternative to State Plane)

Universal Transverse Mercator (UTM) is another projected coordinate system option.

### UTM Zone 3N (Western Alaska)
**EPSG:26903** - NAD83 / UTM Zone 3N
- **Area:** Includes Quinhagak
- **Units:** Meters
- **Use for:** Scientific studies, international projects

### UTM Zone 4N
**EPSG:26904** - NAD83 / UTM Zone 4N
- **Area:** South-central Alaska

### UTM Zone 5N
**EPSG:26905** - NAD83 / UTM Zone 5N
- **Area:** Southeast Alaska

### UTM Zone 6N
**EPSG:26906** - NAD83 / UTM Zone 6N
- **Area:** Eastern Alaska

### UTM Zone 7N
**EPSG:26907** - NAD83 / UTM Zone 7N
- **Area:** Easternmost Alaska

---

## Choosing the Right Coordinate System

### Use WGS84 (EPSG:4326) when:
- ✅ Collecting GPS data
- ✅ Sharing data globally
- ✅ Working with web services
- ✅ Need maximum compatibility
- ✅ Displaying locations on web maps

### Use Alaska State Plane Zone 7 (EPSG:26937) when:
- ✅ Working in Quinhagak area
- ✅ Measuring distances accurately
- ✅ Calculating areas
- ✅ Parcel mapping
- ✅ Local infrastructure planning
- ✅ Survey-grade accuracy needed

### Use Alaska Albers (EPSG:3338) when:
- ✅ Mapping entire state of Alaska
- ✅ Regional analysis
- ✅ Calculating areas across Alaska
- ✅ Statewide projects

### Use UTM Zone 3N (EPSG:26903) when:
- ✅ Scientific research
- ✅ International projects (UTM used worldwide)
- ✅ Prefer meters to feet
- ✅ Working with data in UTM

### AVOID Web Mercator (EPSG:3857) for:
- ❌ Measuring distances
- ❌ Calculating areas
- ❌ Scientific analysis
- ❌ Anything requiring accuracy at high latitudes

---

## Quick Lookup Table

| **EPSG Code** | **Name** | **Type** | **Units** | **Best For** |
|---------------|----------|----------|-----------|--------------|
| **4326** | WGS 84 | Geographic | Degrees | GPS, global data |
| **26937** | Alaska State Plane Zone 7 | Projected | Feet | Quinhagak local work |
| **3338** | Alaska Albers | Projected | Meters | Statewide mapping |
| **26903** | UTM Zone 3N | Projected | Meters | Scientific studies |
| **3857** | Web Mercator | Projected | Meters | Web maps only |

---

## How to Find EPSG Codes

### Method 1: EPSG.io Website

1. Go to https://epsg.io/
2. Search for:
   - Place name: "Quinhagak"
   - Coordinate system name: "Alaska State Plane Zone 7"
   - EPSG code: "26937"
3. View details:
   - Area of use (map showing coverage)
   - Coordinate system parameters
   - Export formats
   - Alternative codes

**Example:** https://epsg.io/26937

### Method 2: ArcGIS Pro

1. Open Map Properties → Coordinate Systems
2. Browse or search for coordinate system
3. Right-click coordinate system → Copy
4. EPSG code is part of full name
5. Or check Properties to see Authority Code

### Method 3: Layer Properties

1. Right-click layer in Contents
2. Properties → Source
3. Spatial Reference section
4. Authority: EPSG
5. Code: [number]

---

## NAD83 vs NAD27

You might see coordinate systems with NAD83 or NAD27 in the name.

**NAD27** (North American Datum 1927)
- Older datum
- Less accurate
- Rarely used for new projects
- Historical data may be in NAD27

**NAD83** (North American Datum 1983)
- Current standard
- More accurate
- Used for all modern GPS
- Use this for new projects!

**For Quinhagak work: Always use NAD83**

---

## Common EPSG Code Errors

### Error 1: Using Wrong Zone
**Problem:** Using State Plane Zone 4 (Anchorage) for Quinhagak data
**Result:** Data appears in wrong location, measurements inaccurate
**Solution:** Use Zone 7 (EPSG:26937) for Quinhagak

### Error 2: Confusing Geographic with Projected
**Problem:** Trying to buffer in WGS84 (EPSG:4326)
**Result:** Buffer uses degrees instead of meters/feet
**Solution:** Project to State Plane or UTM first

### Error 3: Undefined Coordinate System
**Problem:** Data has no coordinate system defined
**Result:** Data doesn't display or appears in wrong place
**Solution:** Define projection (don't project it!) using correct EPSG code

### Error 4: Data in Wrong Hemisphere
**Problem:** Alaska data appears off coast of Africa
**Result:** Coordinate system misinterpreted
**Solution:** Check if coordinates are negative (West longitude should be negative)

---

## Coordinate System Strings

Sometimes you need the full coordinate system name, not just EPSG code:

### For EPSG:4326 (WGS84):
```
GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]
```

### For EPSG:26937 (Alaska State Plane Zone 7):
```
PROJCS["NAD_1983_StatePlane_Alaska_7_FIPS_5007_Feet",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",1640416.666666667],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-162.0],PARAMETER["Scale_Factor",0.9999],PARAMETER["Latitude_Of_Origin",54.0],UNIT["Foot_US",0.3048006096012192]]
```

**Good news:** You rarely need these strings! EPSG codes are much easier.

---

## Resources

### Official Sources
- [EPSG.io - Coordinate Systems Database](https://epsg.io/)
- [Spatial Reference List](https://spatialreference.org/)
- [EPSG Registry](https://epsg.org/home.html)

### Alaska-Specific
- [Alaska State Plane Information](https://www.commerce.alaska.gov/web/portals/4/pub/StatePlane.pdf)
- [Alaska Geospatial Council](https://agc.dnr.alaska.gov/)
- [Alaska DOT Coordinate Systems](https://dot.alaska.gov/stwddes/)

### Learning Resources
- [Understanding Coordinate Systems (Esri)](https://pro.arcgis.com/en/pro-app/latest/help/mapping/properties/coordinate-systems-and-projections.htm)
- [State Plane Coordinate System Guide](https://gisgeography.com/state-plane-coordinate-system-spcs/)

---

## Printable Cheat Sheet

**For Quinhagak GIS Work:**

| **Task** | **Use This EPSG** | **Why** |
|----------|-------------------|---------|
| GPS field collection | 4326 | GPS standard |
| Local measurements | 26937 | Quinhagak area accuracy |
| Statewide maps | 3338 | Alaska-wide coverage |
| Web maps | 3857 | Web display only |
| Share with scientists | 26903 | UTM standard |

**Quick Check:**
- Coordinates in degrees (59.76, -161.9)? → Probably EPSG:4326
- Coordinates in large numbers (1847000, 460000)? → Probably EPSG:26937
- Working in Quinhagak? → Use EPSG:26937

---

**Bookmark https://epsg.io/ and keep this guide handy!**

---

**Version:** 1.0
**Last Updated:** November 2025
**For:** Quinhagak GIS Training, Module 4
