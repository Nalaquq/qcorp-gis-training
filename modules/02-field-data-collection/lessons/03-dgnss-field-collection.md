# Lesson 3: DGNSS Field Data Collection

**Module:** 02 - Field Data Collection
**Duration:** Full day (8 hours field time)
**Difficulty:** Intermediate
**Prerequisites:** Understanding of GPS basics, Module 1 completed

---

## Learning Objectives

By the end of this lesson, you will be able to:

1. ✅ Set up Emlid Reach RS3 base station and rover correctly
2. ✅ Level equipment and measure antenna heights accurately
3. ✅ Use the optical plummet to sight over known points
4. ✅ Manually enter coordinates for known datum points
5. ✅ Select appropriate survey locations based on community needs
6. ✅ Collect high-accuracy ground control points (GCPs)
7. ✅ Record base station coordinates and survey metadata
8. ✅ Choose the right tool (Survey123, Emlid Flow, or Field Maps) for each task

---

## What is DGNSS and Why Does It Matter?

**DGNSS (Differential GNSS)** uses two GPS receivers working together to achieve centimeter-level accuracy:

- **Base Station** - Stays in one location, sends corrections
- **Rover** - Moves to points you want to measure

**Accuracy comparison:**
- Phone GPS: 5-10 meters (15-30 feet)
- Single GNSS receiver: 1-2 meters (3-6 feet)
- DGNSS (RTK): 1-2 centimeters (less than 1 inch)

**When you need DGNSS:**
- Property boundary surveys
- Erosion monitoring (measuring change over time)
- Ground control points for drone mapping
- Ground truthing satellite data
- Infrastructure as-built surveys
- Any work requiring legal-grade accuracy

👉 **[See Terminology Guide](./terminology.md)** for detailed definitions of all DGNSS terms

---

## Field Scenario 1: SWOT Satellite Ground Truthing

### Background

The **SWOT (Surface Water and Ocean Topography)** satellite measures water surface elevations from space. To verify the satellite's accuracy, we collected ground elevation data at the same time the satellite passed over Quinhagak.

### Objectives

- Collect precise elevation measurements during satellite overpass
- Use DGNSS for centimeter-accurate heights
- Compare ground measurements to satellite readings
- Calibrate/validate satellite data for the region

### What We Did

1. **Timing coordination:**
   - Determined SWOT overpass time for Quinhagak
   - Planned to be in position 30 minutes before pass

2. **Equipment setup:**
   - Set up base station in open area near water
   - Measured and recorded antenna height
   - Allowed system to reach fixed solution

3. **Data collection:**
   - Collected points along water's edge during overpass
   - Recorded water surface elevations
   - Took photos and notes about conditions

4. **Metadata recording:**
   - Base station coordinates
   - Time of collection
   - Weather conditions
   - Water conditions (calm, windy, etc.)

### Key Lessons

- **Vertical accuracy matters most** for water elevation work
- **Timing is critical** - satellite passes quickly
- **Document everything** - conditions affect water levels
- **Use proper vertical datum** - must match satellite reference system

---

## Field Scenario 2: Nunalleq Archaeological Site

### Background

In 2022, a French archaeological team installed permanent datum markers at the Nunalleq site. These markers have known, precisely measured coordinates that can be reused for future surveys.

### Objectives

- Learn how to use known fixed points
- Practice setting up base station over existing datums
- Understand why manual coordinate entry is important
- Collect data tied to existing control network

### What We Did

1. **Located the 2022 datums:**
   - Two permanent markers installed by French team
   - Coordinates were documented in their report
   - Physical markers are metal pins in concrete

2. **Base station setup:**
   - Set up base station directly over one datum
   - Used tribrach's optical plummet to center over marker
   - Leveled the tripod carefully
   - **Manually entered the known coordinates** from 2022 report

3. **Rover measurements:**
   - Shot the second datum with rover
   - Compared measured position to known position
   - Verified system accuracy (should match within 2 cm)

4. **Practice without instructor:**
   - Yup'ik GIS techs set up equipment themselves
   - Reinforced leveling and height measurement procedures
   - Emphasized always photographing/recording base coordinates

### Key Lessons

- **Always manually enter known point coordinates** - Don't rely on auto-positioning
- **Save known points** in Emlid Flow for future use
- **Optical plummet is critical** for setup over markers
- **Leveling affects both horizontal and vertical accuracy**
- **Taking photos** of setup is essential documentation

### Why This Matters

When you return to a known point:
1. You connect new surveys to old surveys
2. All measurements are in the same reference system
3. You can measure change over time accurately
4. You don't have to wait for OPUS processing

---

## Selecting Survey Locations: Community-Based Planning

Before going to the field, we identified survey priorities based on **community needs and ongoing projects**.

### Quinhagak 2025 Survey Sites

#### 1. USDA Gravel Sample Site

**Purpose:** Support materials testing for construction projects

**Why DGNSS:**
- Exact sample location needed for records
- May need to return to same spot
- Links physical sample to GIS database

**Data collected:**
- Precise coordinates of sample location
- Elevation
- Photos of site conditions
- Sample ID linked to location

---

#### 2. Sewage Lagoon Site

**Purpose:**
- Assess accuracy of state-produced orthomosaic
- Measure erosion face
- Document current conditions

**Why DGNSS:**
- Ground control points for drone mapping
- Verify/correct state aerial imagery
- Monitor erosion over time

**Data collected:**
- GCPs around lagoon perimeter (at least 5 points)
- Elevation profile of erosion face
- Top and bottom of bank measurements
- Photos from GCP locations

**Follow-up:**
- Compare GCP coordinates to orthomosaic
- Calculate horizontal/vertical accuracy of imagery
- Plan erosion mitigation if needed

---

#### 3. Nunalleq Archaeological Field Site

**Purpose:**
- Obtain coordinates for French team's 2022 datums
- Add to permanent control point database
- Enable future surveys to tie into same system

**Why DGNSS:**
- Datums are reference points for all future work
- Archaeological sites need precise measurements
- Enables long-term site monitoring

**Data collected:**
- Coordinates of both datum markers
- Photos of markers and surrounding area
- Marker descriptions and conditions
- Offset measurements to site features

**Follow-up:**
- Add to Qanirtuuq GIS known points database
- Share with archaeological team
- Use as base station locations for future surveys

---

#### 4. Warren's Lot

**Purpose:**
- Verify housing allotment boundaries
- Check buffer zones for recent land deal
- Resolve boundary questions

**Why DGNSS:**
- Legal boundaries require survey-grade accuracy
- Property decisions depend on precise measurements
- May be used in legal documents

**Data collected:**
- Corner points of lot
- Offset distances to physical features
- Photos of each corner
- Nearby reference features

**Follow-up:**
- Compare to platted lot dimensions
- Calculate acreage
- Verify buffer zone compliance
- Provide documentation for land transaction

---

#### 5. The Old Point (Nuk)

**Purpose:**
- Evaluate as alternative barge landing site
- Current city dock requires sharp turn causing barges to get stuck
- Elevation data needed for feasibility assessment

**Why DGNSS:**
- Elevation determines if suitable for barge access
- Need accurate topography for planning
- Compare elevations at different tide levels

**Data collected:**
- Shoreline elevation profile
- High water mark elevation
- Points along potential access route
- Distance from water at different tide stages
- Photos showing approach angles

**Follow-up:**
- Create elevation profile drawing
- Compare to barge draft requirements
- Assess suitability vs. current dock
- Cost-benefit analysis for Qanirtuuq Inc board

**Community Impact:**
- Could solve long-standing logistics problem
- Reduce risk of barge delays
- Improve delivery of heating fuel and supplies

---

## Equipment Setup: Step-by-Step

### 🎥 Video Resources

**Must-watch before field work:**
- [Reach RS3 Base and Rover Setup and Config](https://www.youtube.com/watch?v=6Ju4bLvkdRc) - 8 minutes
- [Emlid RS3 Documentation Homepage](https://docs.emlid.com/reachrs3/)

---

### Base Station Setup

#### Location Selection

**Good locations:**
- Clear view of sky (horizon to horizon if possible)
- Away from buildings, trees, power lines
- Stable ground that won't shift
- Safe from traffic/equipment

**Poor locations:**
- Under trees (blocks satellite signals)
- Next to metal buildings (causes interference)
- Areas that flood or have soft ground
- Near radio towers or power lines

#### Setup Procedure

**📋 [Detailed Guide: Choosing Base Setup Method](https://docs.emlid.com/reachrs3/base-setup/choosing-base-setup-method/)**

1. **Set up tripod:**
   - Extend legs to comfortable height (eye level)
   - Press legs firmly into ground
   - Adjust legs so top is roughly level

2. **Mount tribrach:**
   - Attach tribrach to tripod
   - Don't fully tighten yet

3. **Level the tribrach:**
   - Adjust foot screws to center bubble level
   - Check level in multiple directions
   - This is critical - take your time
   - **Check level again before starting!**

4. **Mount base station:**
   - Attach RS3 to tribrach
   - Ensure secure connection
   - Cable management - keep cables from pulling

5. **Measure antenna height:**
   - Use tape measure
   - Measure from ground to **antenna reference point** (marked on device)
   - Typical height: 1.5 - 2.0 meters
   - **Write it down immediately**
   - Enter into Emlid Flow app

6. **If using known point:**
   - Use optical plummet to sight through tribrach
   - Adjust tripod position until crosshairs center on marker
   - Re-level after moving
   - Verify still centered on marker

---

### Rover Setup

1. **Attach to range pole:**
   - Secure RS3 to top of pole
   - Standard pole height: 2 meters
   - Ensure tight connection

2. **Measure pole height:**
   - From bottom of pole to antenna reference point
   - Typical: 2.0 - 2.2 meters depending on pole
   - **Enter into Emlid Flow before collecting points**

3. **Bubble level:**
   - Range pole should have built-in level
   - Keep pole vertical when collecting points
   - Check level before each measurement

---

### Emlid Flow App Configuration

**📱 [How to use Emlid Flow App](https://docs.emlid.com/emlid-flow/survey-with-ef/points/collector/)**

#### Base Station Settings

1. Open Emlid Flow app
2. Connect to base station via Bluetooth/Wi-Fi
3. **Base mode setup:**
   - Choose setup method:
     - **Average Single** - for new points (collects 5 min of data)
     - **Manual** - for known points (enter saved coordinates)
   - If Manual: Enter known coordinates exactly as recorded
   - Enter antenna height
   - Start base

4. **Record base position:**
   - Take screenshot of coordinates
   - Write in field notebook
   - Photo of setup

#### Rover Settings

1. Connect to rover via Bluetooth
2. **Rover mode:**
   - Ensure receiving corrections from base
   - Check correction age (should be <5 seconds)
   - Solution status should show "Fix"

3. **Point collection settings:**
   - Enter antenna height (pole length)
   - Set averaging time (3-5 seconds for most work)
   - Enable auto-save if desired

4. **Verify accuracy:**
   - Check RMS values (should be <2 cm for horizontal, <3 cm for vertical)
   - If not achieving "Fix" solution, troubleshoot before continuing

---

## Field Techniques & Best Practices

### Critical Habits

**These practices prevent 90% of field data problems:**

#### 1. Always Record Base Station Coordinates

**Why:** If you don't know where base was, rover data may not be usable

**How:**
- Take photo of app screen showing coordinates
- Write in waterproof field notebook
- Save in app with project name and date
- Email coordinates to yourself

**When:** Immediately after base starts logging

---

#### 2. Measure and Record Antenna Heights

**Base station:**
- Measure before starting
- Record in app and notebook
- Verify hasn't changed during day

**Rover:**
- Measure pole before field work
- Enter in app before first point
- Re-measure if pole is adjusted

**Common mistake:** Forgetting to enter height in app - this makes elevations wrong!

---

#### 3. Level Everything

**Base station:**
- Use circular bubble level
- Check before starting
- Check again after 30 minutes
- Check if tripod is bumped

**Rover:**
- Use pole bubble level
- Hold vertical for each point
- Take multiple measurements if windy

---

#### 4. Wait for "Fix" Solution

**Solution status meanings:**
- **Single** - Standard GPS, ~1 meter accuracy - NOT ACCEPTABLE
- **Float** - Partial RTK, ~10 cm accuracy - WAIT LONGER
- **Fix** - Full RTK, 1-2 cm accuracy - GOOD TO COLLECT

**Best practice:** Only collect points when status shows "Fix"

---

#### 5. Use Known Points Correctly

**If returning to a known datum:**

1. Find saved point in Emlid Flow
2. Set up base station over the marker
3. Use optical plummet to center exactly
4. **Manually enter the saved coordinates** - Don't auto-average
5. Enter antenna height
6. Start base

**Why manual entry matters:**
Even if you're perfectly centered over a known point, averaging will give slightly different coordinates (due to GPS noise). Using the manually entered coordinates ensures all surveys reference the exact same position.

---

#### 6. Document Everything

**Take photos of:**
- Base station setup
- Each rover point location
- Any features being surveyed
- Screen shots of coordinates

**Record in notes:**
- Project name and date
- Base station coordinates
- Antenna heights
- Weather conditions
- Any issues or unusual circumstances
- Names of crew members

---

### Common Field Issues & Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| Can't get Fix solution | Obstructions, interference | Move to open area; check base position |
| Base won't start | Bluetooth/config issue | Restart app; verify antenna height entered |
| Rover loses connection | Distance too far (>10km) | Move closer to base; check radio link |
| Elevations seem wrong | Antenna height not entered | Double-check heights in app |
| Position jumps around | Base station moved/not level | Re-level base; restart if necessary |
| Low accuracy (>5cm) | Poor satellite visibility | Wait for more satellites; move to better location |

---

## Choosing the Right Data Collection Tool

Depending on your task, you'll use different apps and workflows.

### Decision Tree

```
Do you need centimeter accuracy?
├─ YES → Use Emlid RS3 + Emlid Flow app
│         • Property surveys
│         • Erosion monitoring
│         • GCPs
│         • Ground truthing
│
└─ NO → Is this a custom survey form?
          ├─ YES → Use Survey123
          │         • Damage assessments
          │         • Inspections with checklists
          │         • Community data collection
          │
          └─ NO → Use ArcGIS Field Maps
                    • Updating existing layers
                    • General mapping
                    • Asset inventory
```

---

### Tool Comparison

| Tool | Accuracy | Best For | Equipment | Complexity |
|------|----------|----------|-----------|------------|
| **Emlid Flow** | 1-2 cm | Surveys, GCPs, boundaries | RS3 base + rover | High |
| **Survey123** | 3-10 m (phone GPS) | Custom forms, inspections | Phone/tablet (+ RS3 optional) | Medium |
| **Field Maps** | 3-10 m (phone GPS) | Editing existing data, general mapping | Phone/tablet | Low |

---

### Emlid Flow

**📱 [Emlid Flow Documentation](https://docs.emlid.com/emlid-flow/)**

**Use for:**
- Survey-grade point collection
- Boundary corners
- Ground control points (GCPs) for drones
- Erosion monitoring points
- Known datums and benchmarks

**Workflow:**
1. Set up base and rover
2. Create project in Emlid Flow
3. Collect points with descriptions
4. Export to desired format (CSV, Shapefile, GeoJSON)
5. Import into ArcGIS Online or QGIS

**Integration:**
- 🎥 [Survey123 Integration](https://docs.emlid.com/reachrs3/integration/arcgis-survey123/)
- 🎥 [Skydio X10 Drone Integration](https://docs.emlid.com/reachrs3/integration/skydio-rtk/) - For real-time RTK during drone flights

---

### Survey123

**📱 [Survey123 in Module Lesson 1](./01-survey-design.md)**

**Use for:**
- Damage assessments
- Building inspections
- Community needs assessments
- Any data collection with structured questions

**Can be paired with RS3:**
- Connect RS3 to phone/tablet via Bluetooth
- Survey123 will use RS3 positions instead of phone GPS
- Get cm-accuracy with custom forms

**Workflow:**
1. Design form in Survey123 web or Connect
2. Download to mobile device
3. Collect data (offline capable)
4. Sync to ArcGIS Online when connected
5. View results in dashboard or map

---

### ArcGIS Field Maps

**Use for:**
- Updating existing feature layers
- General asset mapping
- Quick field edits
- Navigation to features

**Workflow:**
1. Download offline map area
2. Find or add features
3. Update attributes
4. Sync changes back to ArcGIS Online

**Best when:**
- You already have layers configured
- Don't need highly customized forms
- Need to edit existing features rather than add new

---

## Coordinate Systems & Projections: Practical Workflow

**📖 [See Terminology Guide](./terminology.md) for detailed definitions**

### The Simple Version

**Three things you need to know:**

1. **What coordinate system is your project using?**
   - Alaska State Plane? UTM? Geographic (lat/lon)?

2. **What is everyone else using?**
   - Match the coordinate system of existing data

3. **Configure your equipment to match**
   - Set RS3 to collect in the same system
   - Save yourself reprojection work later

---

### Recommended Settings for Quinhagak Projects

**For most local work:**

- **Horizontal Datum:** NAD83 (2011)
- **Coordinate System:** Alaska State Plane Zone 5
- **Units:** US Survey Feet (or Meters, depending on project)
- **Vertical Datum:** NAVD88 (for orthometric heights)
- **Geoid Model:** Geoid18

**For OPUS submissions:**
- **Horizontal:** NAD83 (2011)
- **Vertical:** Ellipsoid heights (not orthometric)
- *OPUS will provide both ellipsoid and orthometric heights in results*

---

### Configuring RS3 Coordinate System

**In Emlid Flow:**

1. Settings → Output Coordinates
2. Select Coordinate System:
   - **Quick option:** Geographic (WGS84 lat/lon) - works everywhere, easy to reproject
   - **Project-specific:** Alaska State Plane Zone 5 - matches local surveys

3. Select Vertical Reference:
   - **Ellipsoid** - for OPUS, SWOT comparisons
   - **Geoid (orthometric)** - for construction, practical heights

---

### When Coordinate Systems Don't Match

**Problem:** Your field data is in one system, but the office map is in another.

**Solution:** Reproject the data

**In ArcGIS Pro:**
1. Right-click layer → Data → Export Features
2. Set output coordinate system to match project
3. Use the exported layer

**In QGIS:**
1. Right-click layer → Export → Save Features As
2. Change CRS to match project

**Online tool:**
- [NOAA Coordinate Conversion](https://geodesy.noaa.gov/NCAT/)

**Best practice:** Agree on coordinate system before starting fieldwork!

---

## Data Download and Post-Processing

### Downloading Data from Emlid 360

**🌐 [Emlid 360 Cloud Platform](https://emlid.com/emlid-360/)**

After field work:

1. **Log into Emlid 360:**
   - Projects automatically sync from Emlid Flow
   - Access from any device

2. **Review collected data:**
   - See all points on map
   - Check solution quality
   - View photos

3. **Export data:**
   - Choose format (CSV, Shapefile, DXF, etc.)
   - Select coordinate system for export
   - Download to computer

---

### OPUS Post-Processing

**📋 [OPUS Workflow Guide](https://docs.emlid.com/reachrs3/base-setup/determining-base-position/online-post-processing-services/opus-workflow/)**

**When to use OPUS:**
- Need precise base station coordinates
- No nearby known points
- Creating new control points
- Legal surveys

**Requirements:**
- Base station data logged for 2-4 hours
- Stationary position entire time
- RINEX file format

**Process:**

1. **Collect base data:**
   - Start base station logging
   - Log raw satellite data for 2-4 hours
   - More time = better results

2. **Export RINEX file:**
   - In Emlid Flow or Emlid 360
   - Export as RINEX (not CSV or Shapefile)

3. **Submit to OPUS:**
   - Go to [NOAA OPUS website](https://www.ngs.noaa.gov/OPUS/)
   - Upload RINEX file
   - Enter your email address
   - Submit

4. **Receive results:**
   - Usually within a few hours
   - Email contains PDF report
   - Precise coordinates for base station location
   - Quality metrics and accuracy estimates

5. **Use for future surveys:**
   - Save coordinates as a known point
   - Use manual entry when returning to this location
   - Now you have a permanent control point

---

### Correction Workflows

*Note: Awaiting specific workflow from Jon Lim*

**General concept:**
- Base station records errors
- Post-processing applies corrections to rover data
- Results in most accurate possible positions

**When post-processing is needed:**
- Base station wasn't perfectly positioned
- Want to improve beyond real-time accuracy
- Legal or engineering surveys

**When real-time (RTK) is sufficient:**
- Fix solution achieved in field
- Accuracy meets project requirements (1-2 cm)
- Most standard survey work

---

## Integration with Other Workflows

### Using GCPs for Drone Mapping

**Workflow:**

1. **Pre-flight:**
   - Place GCP targets in area to be mapped
   - Distribute evenly throughout site
   - Minimum 5 GCPs, more is better

2. **Survey GCPs:**
   - Use DGNSS to measure each GCP center
   - Collect 30-60 seconds of data per point
   - Label each point clearly (GCP01, GCP02, etc.)
   - Take photos

3. **Fly drone mission:**
   - Ensure photos capture GCPs
   - GCPs should be visible in at least 3 photos each

4. **Post-processing:**
   - Import GCP coordinates into photogrammetry software
   - Mark GCPs in photos
   - Process with GCP constraints
   - Result: Highly accurate orthomosaic and elevation model

**Example use:** Sewage lagoon site - GCPs improve accuracy from ~5 meters to ~2 centimeters

---

### Ground Truthing Satellite Data

**Workflow for SWOT validation:**

1. **Coordinate timing:**
   - Know when satellite passes over your area
   - Be set up 30 minutes before

2. **Collect reference data:**
   - Use DGNSS to measure ground elevations
   - Take water level readings
   - Record exact time
   - Note conditions (wind, waves, etc.)

3. **Request satellite data:**
   - Download SWOT data for your location and time
   - Extract elevation measurements

4. **Compare:**
   - Calculate difference between satellite and ground measurements
   - Assess satellite accuracy
   - Report results to NASA/JPL (helps improve satellite algorithms)

---

## Field Data Collection Day: Sample Schedule

**Full-day DGNSS training session:**

### Morning (8:00 AM - 12:00 PM)

- **8:00 - 9:00:** Equipment overview, site planning review
  - Discuss day's objectives
  - Review target locations
  - Check equipment and batteries

- **9:00 - 10:00:** Base station setup practice
  - Near old airport or open area
  - Each person sets up base station
  - Practice leveling, height measurement
  - Configure Emlid Flow

- **10:00 - 11:00:** Rover practice and workflow
  - Collect practice points
  - Check for Fix solution
  - Practice point descriptions and photos
  - Verify accuracy

- **11:00 - 12:00:** Known point exercise at Nunalleq
  - Set up over 2022 French datums
  - Practice optical plummet
  - Manual coordinate entry
  - Verify setup by checking second datum

### Lunch Break (12:00 - 1:00 PM)

### Afternoon (1:00 PM - 5:00 PM)

- **1:00 - 2:30:** Priority site 1 (e.g., Warren's Lot)
  - Survey boundary corners
  - Measure offsets
  - Document with photos

- **2:30 - 4:00:** Priority site 2 (e.g., Sewage Lagoon)
  - Collect GCPs
  - Measure erosion face
  - Profile measurements

- **4:00 - 5:00:** Final site or return to office
  - Download data from devices
  - Review day's work
  - Backup data
  - Discuss next steps

### Evening (Optional)

- Export data from Emlid 360
- Begin OPUS submission if applicable
- Import data to ArcGIS Online
- Prepare for next day

---

## Assessment: Skills Checklist

To demonstrate proficiency in DGNSS field data collection, you should be able to:

### Equipment Setup
- [ ] Set up and level a tripod-mounted base station
- [ ] Use optical plummet to position over a known marker
- [ ] Measure and record antenna heights accurately
- [ ] Configure Emlid Flow app for base and rover
- [ ] Achieve and recognize "Fix" solution status

### Field Procedures
- [ ] Select appropriate survey locations
- [ ] Manually enter known point coordinates
- [ ] Collect rover points with proper descriptions
- [ ] Take photos and field notes for each point
- [ ] Record base station position every time

### Data Management
- [ ] Download data from Emlid 360
- [ ] Export data in multiple formats
- [ ] Submit base station data to OPUS
- [ ] Import field data into ArcGIS Online
- [ ] Archive projects with proper metadata

### Decision Making
- [ ] Choose appropriate tool (Emlid Flow vs Survey123 vs Field Maps)
- [ ] Determine when DGNSS accuracy is required
- [ ] Troubleshoot common field issues
- [ ] Verify data quality before leaving site

---

## Resources

### Official Documentation
- [Emlid Reach RS3 Main Documentation](https://docs.emlid.com/reachrs3/)
- [Base Station Setup Guide](https://docs.emlid.com/reachrs3/base-setup/)
- [Choosing Base Setup Method](https://docs.emlid.com/reachrs3/base-setup/choosing-base-setup-method/)
- [OPUS Workflow](https://docs.emlid.com/reachrs3/base-setup/determining-base-position/online-post-processing-services/opus-workflow/)
- [Emlid Flow App Guide](https://docs.emlid.com/emlid-flow/survey-with-ef/points/collector/)

### Video Tutorials
- [Reach RS3 Base and Rover Setup and Config](https://www.youtube.com/watch?v=6Ju4bLvkdRc) - 8 min
- [What is Differential GPS?](https://www.youtube.com/watch?v=8DAImUwJ_gE) - 2 min

### Integration Guides
- [Survey123 Integration](https://docs.emlid.com/reachrs3/integration/arcgis-survey123/)
- [Skydio X10 RTK Integration](https://docs.emlid.com/reachrs3/integration/skydio-rtk/)

### Reference Materials
- [NOAA OPUS Service](https://www.ngs.noaa.gov/OPUS/)
- [NOAA Geodetic Toolkit](https://geodesy.noaa.gov/TOOLS/)
- [NGS Data Sheets - Find existing control points](https://www.ngs.noaa.gov/datasheets/)

---

## Key Takeaways

1. **Base station coordinates must be recorded every time** - This is the #1 cause of field data problems

2. **Level equipment and measure heights carefully** - These directly affect your elevation accuracy

3. **Manual coordinate entry for known points** - Don't rely on auto-positioning

4. **Wait for Fix solution before collecting points** - Float or Single is not accurate enough

5. **Plan survey locations based on community needs** - Field time is valuable; collect data that will be used

6. **Choose the right tool for the job:**
   - Centimeter accuracy → Emlid Flow
   - Custom forms → Survey123
   - Edit existing layers → Field Maps

7. **Document everything** - Photos, notes, coordinates, conditions

8. **Test your setup before leaving** - Shoot a check point with known coordinates

9. **Coordinate systems matter** - Match your project from the start

10. **OPUS provides permanent control** - Worth the wait for establishing reference points

---

## Next Steps

**Continue to:**
- [Activity: DGNSS Field Practice](../activities/activity-03-field-practice.md)
- [Lesson 4: Field Data Collection Techniques](./04-field-techniques.md)
- [Creating Drone GCPs with RS3](../activities/gcp-workflow.md)

**Related lessons:**
- [Terminology Guide](./terminology.md) - Detailed definitions
- [Survey Design Fundamentals](./01-survey-design.md)
- [Offline Maps](./02-offline-maps.md)

---

**Version:** 1.0
**Last Updated:** November 2025
**Field Training:** Quinhagak, Alaska (November 2025)
**Contributors:** Based on Nalaquq Yup'ik GIS Technician Training
