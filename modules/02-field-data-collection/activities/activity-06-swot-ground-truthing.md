# Activity 6: SWOT Satellite Ground Truthing with DGNSS

**Module:** 02 - Field Data Collection
**Activity Type:** Field Data Collection
**Duration:** 4-6 hours (including setup and calibration)
**Difficulty:** Intermediate
**Prerequisites:** Lesson 3 (DGNSS Field Data Collection) completed, Emlid Flow app installed

---

## Activity Overview

In this activity, you will collect high-accuracy water level measurements at the boat harbor near the old airport to ground-truth NASA's Surface Water and Ocean Topography (SWOT) satellite data. This data supports the National Science Foundation grant to model avulsion risks along the Qanirtuuq River.

### Mission Background

**SWOT (Surface Water and Ocean Topography)** is a NASA satellite mission that measures water surface elevations globally. To validate the satellite's accuracy for the Qanirtuuq region, we need precise ground measurements collected at the exact time the satellite passes overhead.

Learn more: [SWOT Mission Overview](https://swot.jpl.nasa.gov/mission/overview/)

### Why This Matters

- **Avulsion risk modeling** - Understanding how the Qanirtuuq River may shift course
- **Satellite calibration** - Your measurements help NASA improve SWOT accuracy for Arctic regions
- **Community planning** - Better flood and erosion predictions for Quinhagak
- **Scientific contribution** - Local data contributing to global climate research

---

## Learning Objectives

By completing this activity, you will be able to:

- [ ] Plan field work around satellite overpass times
- [ ] Properly calibrate base station with adequate settling time
- [ ] Collect centimeter-accurate water surface elevations
- [ ] Document conditions affecting water level readings
- [ ] Download data from Emlid Flow as shapefile
- [ ] Correct data using OPUS/OPURS correction tools
- [ ] Understand the difference between temporary and permanent datums

---

## Collection Date & Satellite Pass Times

### Date: November 23, 2025

### SWOT Satellite Pass Times

Refer to the pass time schedule in `/resources/UTC_AKST_plus17.xlsx` for exact times.

**Estimated pass times for the SWOT Satellite:**

| Cycle | Pass | Pass# | First UTC +17      | First AKST +17     | Last UTC +17       | Last AKST +17     |
|-------|------|--------|---------------------|----------------------|---------------------|---------------------|
| 0     | 41   | 26     | 2025-11-02 17:10    | 2025-11-02 08:10     | 2025-11-02 17:10    | 2025-11-02 08:10     |
| 1     | 41   | 293    | 2025-11-12 06:42    | 2025-11-11 21:42     | 2025-11-12 06:42    | 2025-11-11 21:42     |
| 2     | 41   | 332    | 2025-11-13 15:33    | 2025-11-13 06:33     | 2025-11-13 15:33    | 2025-11-13 06:33     |
| 3     | 42   | 26     | 2025-11-23 13:55    | 2025-11-23 04:55     | 2025-11-23 13:55    | 2025-11-23 04:55     |
| 4     | 42   | 293    | 2025-12-03 03:27    | 2025-12-02 18:27     | 2025-12-03 03:27    | 2025-12-02 18:27     |
| 5     | 42   | 332    | 2025-12-04 12:17    | 2025-12-04 03:17     | 2025-12-04 12:18    | 2025-12-04 03:18     |
| 6     | 43   | 26     | 2025-12-14 10:39    | 2025-12-14 01:39     | 2025-12-14 10:39    | 2025-12-14 01:39     |
| 7     | 43   | 293    | 2025-12-24 00:11    | 2025-12-23 15:11     | 2025-12-24 00:11    | 2025-12-23 15:11     |
| 8     | 43   | 332    | 2025-12-25 09:02    | 2025-12-25 00:02     | 2025-12-25 09:02    | 2025-12-25 00:02     |


*AKST = Alaska Standard Time (UTC - 9 hours)

**Important:** Let the base station calibrate for approximately an hour and make sure to collect your points at exactly the referenced in the chart below. 

---

## Pre-Field Preparation (Day Before)

### Equipment Checklist

- [ ] **Emlid Reach RS3 Base Station** - fully charged
- [ ] **Emlid Reach RS3 Rover** - fully charged
- [ ] **Tripod with tribrach** - inspect and clean
- [ ] **Range pole** (2m) with bubble level
- [ ] **Tape measure** for antenna heights
- [ ] **Smartphone/tablet** with Emlid Flow app installed
- [ ] **Field notebook** (waterproof)
- [ ] **Camera or phone** for documentation
- [ ] **Spare batteries/power bank**
- [ ] **Weather-appropriate clothing** (November in Quinhagak)
- [ ] **Headlamp/flashlight** (for evening passes)

### Device Charging

**Charge ALL devices the night before collection:**

1. Emlid RS3 Base Station - requires 4+ hours for full charge
2. Emlid RS3 Rover - requires 4+ hours for full charge
3. Smartphone/tablet for Emlid Flow
4. Backup power bank
5. Headlamp batteries

**Charging tip:** Plug in devices by 6:00 PM the evening before to ensure full charge.

### App Preparation

1. Open Emlid Flow app
2. Verify you can connect to both RS3 units
3. Check that firmware is up to date
4. Create a new project: `SWOT_GroundTruth_Nov23_2025`

---

## Field Site: Boat Harbor Near Old Airport

### Location Details

- **Site:** Boat harbor near the old airport
- **Access:** [Provide directions specific to Quinhagak]
- **Collection point:** Water's edge at the harbor

### Site Selection Criteria

Good collection spot should have:
- Clear view of sky (for satellite signals)
- Safe access to water's edge
- Stable footing
- Protection from wind if possible
- Open area for base station setup

---

## Part 1: Base Station Setup (Allow 60+ minutes)

### Base Station Calibration Time

**Allow at least 1 hour for base station calibration before taking measurements.**

This settling time is critical for:
- Achieving stable "Fix" solution
- Reducing position drift
- Ensuring consistent corrections to rover

### Setup Procedure

**Step 1: Select Base Station Location**
- Find open area with clear sky view (horizon to horizon)
- Stay away from buildings, trees, power lines
- Choose stable ground that won't shift
- Within radio range of collection point (~500m typical)

**Step 2: Set Up Tripod and Tribrach**

1. Extend tripod legs to comfortable height
2. Press legs firmly into ground/snow
3. Mount tribrach to tripod
4. Level the tribrach using foot screws
5. Double-check level in all directions

**Step 3: Mount Base Station**

1. Attach RS3 to tribrach
2. Power on the RS3
3. Measure antenna height from ground to antenna reference point
4. **Write down the antenna height immediately**

**Step 4: Configure Base Station in Emlid Flow**

1. Open Emlid Flow app
2. Connect to base station
3. Navigate to Base mode setup
4. Select **Average Single** (for temporary datum)
5. Enter antenna height
6. Set averaging time to **5 minutes minimum** (longer is better)
7. Start base

**Note on Datum Type:**

**This is a TEMPORARY DATUM** - we are letting the base station average its position rather than using known coordinates.

**If we were using a PERMANENT DATUM**, we would:
- Set up over a known benchmark marker
- Use the optical plummet to center exactly over the marker
- Select **Manual** entry mode
- Enter the exact coordinates for the base station from the benchmark documentation
- This provides consistent measurements that can be compared across multiple surveys

**Step 5: Record Base Station Information**

Record all of the following:
- Base station coordinates (screenshot and write down)
- Antenna height
- Start time
- Setup location description
- Photos of setup

**Step 6: Wait for Calibration**

- Set a timer for **60 minutes minimum**
- Monitor solution status - should show "Fix"
- Do not move or bump the tripod
- Use this time to prepare rover and scout collection points

---

## Part 2: Rover Setup

### While Base Station Calibrates

**Step 1: Prepare Rover**

1. Attach RS3 to range pole
2. Secure tightly - no wobble
3. Measure pole height (ground to antenna reference point)
4. Verify bubble level works

**Step 2: Configure Rover in Emlid Flow**

1. Connect to rover via Bluetooth
2. Navigate to Rover mode
3. Select project: `SWOT_GroundTruth_Nov23_2025`
4. Enter antenna height (pole height)
5. Verify receiving corrections from base

**Step 3: Scout Collection Points**

While waiting for base calibration:
- Identify safe access to water's edge
- Note any obstacles or hazards
- Plan your collection path
- Check tide conditions

---

## Part 3: Data Collection

### Timing Your Collection

- **Arrive at water's edge:** 15 minutes before satellite pass
- **Begin collection:** 10 minutes before pass time
- **Continue collection:** until 15 minutes after pass time

### Collection Procedure

**Step 1: Verify System Status**

Before collecting:
- [ ] Solution status shows "Fix"
- [ ] Correction age < 5 seconds
- [ ] RMS values < 2 cm horizontal, < 3 cm vertical
- [ ] Base station still running

**Step 2: Position at Water's Edge**

1. Safely approach the water's edge
2. Place range pole point at exact water line
3. Hold pole vertical using bubble level
4. Keep pole steady

**Step 3: Collect Point**

1. In Emlid Flow, tap **Collect Point**
2. Point name: `SWOT_Pass1_WaterEdge_01` (or similar)
3. Set averaging time: **30 seconds minimum** (60 seconds preferred)
4. Hold pole perfectly vertical and still
5. Wait for collection to complete
6. Save point

**Step 4: Collect Multiple Points**

Collect at least **3 points per satellite pass** at the water's edge:
- Point at water line
- Point slightly up bank (5-10 cm above water)
- Point slightly different location along water edge

**Step 5: Document Conditions**

After each collection set, record:
- Time of collection (to the minute)
- Weather conditions (wind, temperature, precipitation)
- Water conditions (calm, choppy, waves)
- Any unusual observations
- Photos of water surface and collection point

### Repeat for Each Satellite Pass

If collecting during multiple passes:
1. Complete collection for Pass 1
2. Stay in field or return before Pass 2
3. Repeat collection procedure
4. Keep base station running if practical

---

## Part 4: Field Shutdown

### After Final Collection

**Step 1: Final Checks**
- [ ] All planned points collected
- [ ] Notes and photos complete
- [ ] Base station coordinates recorded

**Step 2: Rover Shutdown**
1. Stop rover logging in Emlid Flow
2. Power off rover RS3
3. Disconnect from pole
4. Pack carefully

**Step 3: Base Station Shutdown**
1. Stop base logging
2. **Take final screenshot of coordinates**
3. Power off base RS3
4. Lower tripod
5. Pack carefully

**Step 4: Pack Equipment**
- All components accounted for
- Nothing left at site
- Equipment protected for transport

---

## Part 5: Data Download and Correction

### Download from Emlid Flow

**Step 1: Export Shapefile**

1. Open Emlid Flow app
2. Navigate to your project: `SWOT_GroundTruth_Nov23_2025`
3. Tap **Export**
4. Select format: **Shapefile (.shp)**
5. Select coordinate system (NAD83 or WGS84 as needed)
6. Export and save to device/computer

**Alternative export options:**
- CSV (for spreadsheet analysis)
- GeoJSON (for web mapping)
- DXF (for CAD software)

### OPUS/OPURS Data Correction

To achieve the highest accuracy, post-process your base station data through OPUS.

**Step 1: Export Base Station Raw Data**

1. In Emlid Flow or Emlid 360, find base station logs
2. Export as **RINEX format**
3. You need at least 2 hours of data (you have 4-6 hours from this activity)

**Step 2: Submit to OPUS**

1. Go to [NOAA OPUS](https://www.ngs.noaa.gov/OPUS/)
2. Upload your RINEX file
3. Enter email address
4. Enter antenna type (Emlid Reach RS3)
5. Enter antenna height
6. Submit

**Step 3: Receive Corrected Coordinates**

- Results typically arrive within 1-4 hours
- Email contains PDF report with:
  - Precise base station coordinates
  - Quality metrics
  - Accuracy estimates

**Step 4: Apply Corrections with OPURS**

Use the OPURS (Online Positioning User Service - Rapid Static) correction tool to apply the corrected base coordinates to your rover data:

1. Access OPURS through [NOAA Geodetic Tools](https://geodesy.noaa.gov/TOOLS/)
2. Upload your rover observations
3. Apply the corrected base station position
4. Download corrected point data

**Note:** Detailed OPURS workflow instructions are available in the resources folder.

---

## Deliverables

After completing this activity, submit:

1. **Corrected shapefile** - Point data with OPUS-corrected coordinates
2. **Field notes** - Scanned or digital copy of all field observations
3. **Photos** - Collection site, base station setup, water conditions
4. **Metadata sheet** including:
   - Collection date and times
   - Satellite pass times (from schedule)
   - Base station coordinates (original and corrected)
   - Antenna heights
   - Weather and water conditions
   - Equipment serial numbers

---

## Quality Check

### Before Leaving the Field

- [ ] Solution status was "Fix" for all points
- [ ] All antenna heights recorded
- [ ] Base station coordinates saved (screenshot + written)
- [ ] Multiple points collected per satellite pass
- [ ] Conditions documented
- [ ] Photos taken

### After Post-Processing

- [ ] OPUS results received and reviewed
- [ ] Corrections applied to rover data
- [ ] Final coordinates exported
- [ ] Data backed up in multiple locations

---

## Troubleshooting

| Issue | Possible Cause | Solution |
|-------|---------------|----------|
| Can't get Fix solution | Sky obstructions, interference | Move to more open area |
| Base station lost connection | Distance too far, radio issue | Move closer; check radio link |
| Rover not receiving corrections | Bluetooth issue, base not started | Restart app; verify base is transmitting |
| High RMS values (>5cm) | Poor satellite geometry | Wait for better satellite positions |
| Water edge unsafe to access | High tide, ice, waves | Find alternate safe collection point; document offset |

---

## Safety Considerations

### November Field Conditions

- **Daylight:** Limited daylight hours - bring headlamp for evening passes
- **Temperature:** Expect near or below freezing - dress in layers
- **Ice:** Watch for ice on ground and at water's edge
- **Water hazards:** Do not enter water; stay on stable ground
- **Communication:** Ensure someone knows your field plan and expected return

### Emergency Contacts

- [Add local emergency contacts]
- Satellite phone number (if available): [Add number]

---

## Additional Resources

### Documentation
- [SWOT Mission Overview](https://swot.jpl.nasa.gov/mission/overview/)
- [Emlid RS3 Base Setup Guide](https://docs.emlid.com/reachrs3/base-setup/)
- [NOAA OPUS Service](https://www.ngs.noaa.gov/OPUS/)
- [Lesson 3: DGNSS Field Data Collection](../lessons/03-dgnss-field-collection.md)

### Reference Files
- Satellite pass schedule: `/resources/UTC_AKST_plus17.xlsx`

---

## Key Takeaways

1. **Allow adequate calibration time** - Base station needs 60+ minutes to stabilize
2. **Timing is critical** - Be in position before satellite passes
3. **Document everything** - Conditions affect water levels and data quality
4. **Use temporary datum for this survey** - But understand when permanent datums are needed
5. **Post-process for best accuracy** - OPUS correction improves results significantly
6. **Your data matters** - Contributing to NASA satellite validation and regional flood modeling

---

**Version:** 1.0
**Created:** November 2025
**Project:** NSF Qanirtuuq River Avulsion Risk Modeling
**Satellite:** NASA SWOT (Surface Water and Ocean Topography)
