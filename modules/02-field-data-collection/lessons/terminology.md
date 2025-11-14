# Field Data Collection: Key Terminology

**Module:** 02 - Field Data Collection
**Difficulty:** Beginner
**Reading Level:** 8th Grade

---

## Overview

This guide explains important terms you'll use when collecting precise location data in the field. All definitions are written in plain language to make GPS and mapping concepts easy to understand.

---

## GPS & Navigation Terms

### DGNSS (Differential Global Navigation Satellite System)

**Simple Definition:** A super-accurate GPS system that uses two receivers working together to get very precise locations.

**How it works:**
- One receiver (base station) stays in one spot
- Another receiver (rover) moves around to collect data
- The base station sends corrections to the rover
- This removes errors and gives you locations accurate to within a few centimeters

**Why it matters:** Regular phone GPS is accurate to about 5-10 meters (15-30 feet). DGNSS can be accurate to 1-2 centimeters (less than an inch). This matters when measuring erosion, property boundaries, or building locations.

**Real example:** When measuring how much the riverbank has eroded, you need to know the exact location within a few inches, not a few feet.

---

### RTK (Real-Time Kinematic)

**Simple Definition:** A type of DGNSS that gives you super-accurate locations instantly while you're in the field.

**How it works:**
- The base station sends correction signals to the rover in real-time via radio or internet
- You see the accurate position right away on your device
- No waiting for corrections later

**Why it matters:** You know immediately if your measurement is good enough, so you don't have to come back later.

**Real example:** When marking property corners, you can see right away if your measurement is within 2 centimeters and meets survey standards.

---

### Base Station

**Simple Definition:** The stationary GPS receiver that stays in one location and provides corrections to the rover.

**Key points:**
- Must be set up carefully with the antenna level
- Should be placed in a location with clear view of the sky
- Needs to record its position for the entire survey session
- **Always write down or photograph the base station coordinates!**

**Why it matters:** The base station is the reference point for all your measurements. If you don't record where it was, your data may not be useful.

---

### Rover

**Simple Definition:** The GPS receiver you carry around to collect location data at different points.

**Key points:**
- Connects to the base station wirelessly
- Must be held level over the point you're measuring
- Height of the antenna pole must be measured and entered accurately

**Why it matters:** This is the tool that actually collects your field data. Accurate height measurements are critical for getting correct elevations.

---

## Reference Systems & Coordinates

### Datum

**Simple Definition:** An agreed-upon reference point or surface that all measurements are based on.

**Think of it like:** The starting line of a race. Everyone needs to start from the same place, or the race times don't make sense.

**Types:**
- **Horizontal datum** - For locations (latitude/longitude)
- **Vertical datum** - For elevations (height above sea level)

**Common datums in Alaska:**
- **NAD83 (2011)** - North American horizontal datum
- **NAVD88** - North American vertical datum (for heights)

**Why it matters:** If two people use different datums, their coordinates for the same spot will be slightly different. This causes problems when combining data.

**Real example:** The French team's 2022 survey markers at Nunalleq are permanent datums you can return to for future surveys.

---

### Vertical Datum

**Simple Definition:** The reference surface used to measure heights and elevations.

**Think of it like:** Agreeing on what "sea level" means. Is it high tide? Low tide? Average over 19 years?

**Common vertical datums:**
- **NAVD88** - North American standard (based on tide measurements)
- **Ellipsoid heights** - Mathematical model of Earth's shape
- **Orthometric heights** - "True" height above sea level

**Why it matters:** Elevation data is critical for flood planning, erosion monitoring, and construction. Using the wrong vertical datum can make heights wrong by several feet.

**Real example:** When collecting elevation data during the SWOT satellite pass, you need to use the same vertical datum as the satellite to compare measurements accurately.

---

### Coordinate System

**Simple Definition:** A method of describing where something is on Earth using numbers.

**Common types:**
- **Geographic coordinates** - Latitude and longitude (degrees)
- **Projected coordinates** - Easting and Northing (meters or feet)

**Why it matters:** Different projects may use different coordinate systems. You need to know which one to use so your data lines up with other maps.

---

### Projected Coordinate System

**Simple Definition:** A way of showing the curved Earth on a flat map using coordinates in feet or meters instead of degrees.

**Think of it like:** Peeling an orange and trying to flatten the peel. You have to stretch or compress some parts.

**Common systems in Alaska:**
- **Alaska State Plane** - Split into zones for different regions
- **UTM (Universal Transverse Mercator)** - Zone 3 for Western Alaska

**Why it matters:** When measuring distances or areas, projected coordinates (feet/meters) are easier to work with than latitude/longitude (degrees).

**Real example:** When measuring Warren's Lot to check the housing allotment, you'll use Alaska State Plane coordinates in feet.

---

### Projection

**Simple Definition:** The mathematical method used to convert the round Earth onto a flat map.

**Key points:**
- Every map has a projection
- Projections always distort something (shape, area, distance, or direction)
- Different projections work better for different purposes

**Alaska-specific note:** Alaska is so far north that many common projections don't work well here. Use Alaska-specific projections when possible.

---

## Ground Control & Reference Points

### GCP (Ground Control Point)

**Simple Definition:** A point on the ground whose exact location has been measured very accurately, used to make other maps more accurate.

**How they're used:**
- Mark the point with a visible target
- Measure the exact coordinates with DGNSS
- Take drone or aerial photos that show the GCP
- Use the GCP to correct the position of the aerial photos

**Why it matters:** Drone photos without GCPs can be off by 5-10 meters. With GCPs, accuracy improves to 2-5 centimeters.

**Real example:** When creating the orthomosaic of the sewage lagoon site, GCPs help ensure the aerial images line up perfectly with real-world locations.

---

### Ground Truthing

**Simple Definition:** Going out to a location in person to verify that satellite or aerial data is accurate.

**How it works:**
1. Satellite or sensor collects data remotely
2. You visit the actual location with precise GPS equipment
3. Compare the satellite data to your field measurements
4. Calculate and apply corrections

**Why it matters:** Satellites and drones can have errors. Ground truthing helps calibrate these tools and confirm they're measuring correctly.

**Real example:** The SWOT satellite measures water surface elevation from space. By taking precise elevation measurements on the ground at the same time the satellite passes over, you can check if the satellite readings are accurate.

---

### Known Point

**Simple Definition:** A permanent location whose exact coordinates have been measured and recorded, which can be used as a starting point for future surveys.

**Key points:**
- Physically marked (metal pin, concrete marker, etc.)
- Coordinates are written down and saved
- Can be reused for multiple surveys
- Saves time because you don't need to calculate coordinates from scratch

**Why it matters:** Using a known point as your base station position ensures all surveys are referenced to the same location, making it easy to compare measurements over time.

**Real example:** The datums installed by the French team at Nunalleq in 2022 are known points. By recording their coordinates and manually entering them when you set up your base station there, you ensure your survey connects to theirs.

---

## Field Applications & Workflows

### OPUS (Online Positioning User Service)

**Simple Definition:** A free online service that calculates the exact position of your base station by comparing your GPS data to a network of reference stations.

**How it works:**
1. Record base station data for 2-4 hours
2. Upload the file to OPUS website
3. OPUS compares your data to nearby reference stations
4. Receive a report with precise coordinates (within 2 cm)

**Why it matters:** Instead of guessing where your base station is, OPUS tells you the exact coordinates you can use for future surveys.

**Link:** [NOAA OPUS Service](https://www.ngs.noaa.gov/OPUS/)

---

### Survey vs. Mapping Mode

**Survey Mode:**
- High accuracy (1-2 cm)
- Requires base station and rover
- Takes longer to set up
- Used for legal boundaries, construction, precise monitoring

**Mapping Mode:**
- Medium accuracy (10-30 cm)
- Just a rover, no base station
- Quick setup
- Used for general asset mapping, approximate locations

**When to use which:**
- **Property boundaries** → Survey mode
- **Marking fish camp locations** → Mapping mode
- **Erosion monitoring** → Survey mode
- **Finding where trail damage occurred** → Mapping mode

---

## Best Practices

### Critical Habits for DGNSS Work

1. **Always record your base station position**
   - Take a photo of the coordinates
   - Write them down in a field notebook
   - Save them in the Emlid Flow app

2. **Measure antenna heights carefully**
   - Use a tape measure, not estimates
   - Measure from ground to the bottom of the antenna
   - Write it down before starting

3. **Level your equipment**
   - Base station must be level
   - Use the bubble level
   - Check it doesn't move during the survey

4. **Use optical plummet for known points**
   - When setting up over a marker
   - Sight through the tribrach
   - Make sure crosshairs are directly over the point

5. **Reuse known points properly**
   - Save known point coordinates
   - Manually enter them each time you return
   - Don't rely on auto-positioning over known points

---

## Choosing the Right Tool

### Survey123
**Best for:** Custom forms, detailed inspections, photos with data
**Example use:** Damage assessments, building inspections, incident reports

### Emlid Flow
**Best for:** Precise point collection, boundary surveys, GCPs
**Example use:** Property corners, erosion monitoring points, GCP placement

### ArcGIS Field Maps
**Best for:** Updating existing map data, editing features, general mapping
**Example use:** Updating building footprints, marking utility locations

**Rule of thumb:**
- Need centimeter accuracy? → Emlid Flow with RS3
- Need custom questions and photos? → Survey123
- Updating existing ArcGIS layers? → Field Maps

---

## Common Questions

**Q: Why can't I just use my phone's GPS?**
A: Phone GPS is accurate to 5-10 meters. That's fine for navigation but not for surveys. DGNSS gets you to 1-2 centimeters.

**Q: Do I always need a base station?**
A: For high accuracy work (surveys, GCPs, erosion monitoring) - yes. For general mapping - no, you can use single receiver mode.

**Q: What if I forget to write down my base station coordinates?**
A: Your rover data will still have coordinates, but they may not be as accurate. If you need to continue the survey another day, you won't be able to set up at the exact same base location.

**Q: How long does OPUS take?**
A: You need to collect data for 2-4 hours, then upload it. OPUS usually sends results within a few hours.

**Q: What's the difference between NAD83 and WGS84?**
A: They're different horizontal datums. In Alaska, the difference is less than 1 meter. For most local projects, use NAD83 (2011).

---

## Quick Reference: Quinhagak Survey Settings

**Recommended Settings for Local Work:**

- **Horizontal Datum:** NAD83 (2011)
- **Vertical Datum:** NAVD88 (or ellipsoid heights for OPUS)
- **Coordinate System:** Alaska State Plane Zone 5 (feet)
- **Geoid Model:** Geoid18 (for height conversions)

*Note: These settings may vary by project. Always confirm with project specifications.*

---

## Resources

### Official Documentation
- [NOAA Geodesy Basics](https://geodesy.noaa.gov/corbin/class_description/)
- [NGS Datums Explained](https://geodesy.noaa.gov/datums/)
- [Emlid RS3 Glossary](https://docs.emlid.com/reachrs3/)

### Alaska-Specific Resources
- [Alaska Region Geodetic Control](https://geodesy.noaa.gov/NGS_TOOLKIT/Alaska_toolkit.html)

---

**Version:** 1.0
**Last Updated:** November 2025
**Contributor:** Based on Quinhagak field training (November 2025)
