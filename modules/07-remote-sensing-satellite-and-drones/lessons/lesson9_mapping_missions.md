# Lesson 9: Mapping Missions and Data Collection

**Duration:** 120 minutes
**Prerequisites:** Lessons 1-6 (Skydio X10 basics, preflight, hand launch/catch, controller, manual skills)
**Training Date Reference:** November 7, 2025

---

## Lesson Overview

This lesson covers planning and executing mapping missions with the Skydio X10 to create orthomosaic maps. You'll learn flight planning parameters, data collection procedures, and critical operational considerations discovered during real-world mapping operations.

---

## Learning Objectives

By the end of this lesson, you will be able to:

1. Plan a mapping mission for orthomosaic creation
2. Configure appropriate flight parameters (altitude, overlap)
3. Execute a systematic mapping flight
4. Understand the importance of takeoff/landing location consistency
5. Properly save and manage scan data
6. Handle the drone during controller pairing
7. Retrieve imagery data from SD cards
8. Estimate data volumes and flight requirements

---

## Mapping Mission Planning

### Defining Your Area of Interest

**Mission Objective:**
Create a high-resolution orthomosaic map of a specific area for:
- Infrastructure documentation
- Site analysis
- Change detection baseline
- Measurement and planning
- 3D modeling

**Area Selection Considerations:**
- Size of area (affects flight time and battery needs)
- Obstacles present (buildings, trees, power lines)
- Access for takeoff/landing
- Lighting conditions
- Time of day for optimal imagery

### Flight Parameters for Orthomosaic Creation

**Altitude:**
- **Higher altitude** = Larger coverage area, lower resolution
- **Lower altitude** = Smaller coverage area, higher resolution
- **Recommended starting point:** 150-250 feet AGL

**Ground Sample Distance (GSD):**
- GSD = size of one pixel on the ground
- At 200 feet: ~0.5-0.7 inches per pixel
- At 150 feet: ~0.4-0.5 inches per pixel
- At 300 feet: ~0.8-1.0 inches per pixel

**Overlap Settings:**
- **Front overlap (along flight path):** 70-80%
- **Side overlap (between flight lines):** 70-80%
- **Higher overlap = Better 3D reconstruction**
- **80/80 overlap is excellent for orthomosaics and 3D models**

**Flight Speed:**
- Automatically adjusted by flight planning software
- Slower at lower altitudes (sharper images)
- Consider wind conditions

**Camera Settings:**
- Auto-exposure typically works well
- Ensure camera pointing straight down (nadir)
- Consistent settings throughout mission

---

## Case Study: Quinhagak Grocery Store Mapping

### Mission Details (November 7, 2025)

**Area Mapped:**
- Quinhagak grocery store building
- Area behind grocery store
- Total coverage area: [approximately X acres/hectares]

**Flight Parameters:**
- **Altitude:** 200 feet AGL
- **Overlap:** 80% front / 80% side
- **Images captured:** Approximately 1,000 images
- **Flight time:** [estimated based on coverage]
- **Batteries used:** [number]

**Why These Parameters?**
- **200 feet altitude:**
  - Balances coverage area with resolution
  - Safe clearance over buildings
  - Good detail for infrastructure analysis
  - ~0.5-0.7 inch GSD

- **80/80 overlap:**
  - Excellent for photogrammetry processing
  - Ensures good tie points between images
  - Allows for high-quality 3D model creation
  - Provides redundancy for image quality issues

**Results:**
- High-quality orthomosaic created
- Sufficient detail for infrastructure analysis
- Good coverage of entire target area
- Successfully processed in ESRI Site Scan

---

## Pre-Mission Preparation

### Flight Planning Software

**Skydio Flight Planning:**
1. Define area boundaries on map
2. Set altitude (200 feet)
3. Configure overlap (80/80)
4. Review flight path
5. Check estimated flight time
6. Calculate battery requirements
7. Save mission/scan plan

**Calculations:**
- **1000 images at 80/80 overlap** indicates substantial area
- Typical capture rate: 2-3 seconds per image
- Total flight time estimation: 30-40 minutes (may require multiple batteries)

### Equipment Checklist

**Required:**
- [ ] Skydio X10 fully charged
- [ ] Multiple batteries (charged and pre-warmed)
- [ ] Flight Deck controller (charged)
- [ ] SD card(s) with adequate space (64GB+ recommended)
- [ ] Safety equipment
- [ ] FAA radio for weather/traffic monitoring

**Recommended:**
- [ ] Backup SD card
- [ ] Extra batteries (warm)
- [ ] Portable power bank
- [ ] Flight plan printed or on device
- [ ] Weather meter

---

## Critical Operational Procedures

### 1. Controller Pairing Protocol

**CRITICAL: Do Not Move Drone During Pairing**

**Discovered Issue:**
Moving the Skydio X10 while pairing with the Flight Deck controller can cause:
- Connection failures
- Compass calibration errors
- Takeoff issues
- Need to restart pairing process

**Proper Pairing Procedure:**
1. Place drone on stable surface
2. Power on drone
3. **Do not touch or move drone**
4. Power on controller
5. Wait for connection to establish
6. Verify "Ready to Fly" status
7. **Only then proceed with preflight checks**

**Why This Matters:**
- IMU and compass calibrate during initialization
- Movement during calibration causes errors
- GPS lock acquisition needs stable platform
- Sensor fusion requires stationary reference

### 2. Takeoff and Landing Location Consistency

**CRITICAL: Return to Same Location**

**Discovered Requirement:**
The Skydio X10 must take off and land at approximately the same location.

**Why This Is Required:**
- Home point set at takeoff location
- Return-to-Home (RTH) programmed to original spot
- GPS accuracy considerations (~3-10 feet)
- Battery reserve calculations based on return distance
- Mission planning assumes same start/end point

**Practical Implications:**

**✅ DO:**
- Mark takeoff spot clearly (cone, marker, person)
- Plan for adequate landing area at takeoff site
- Ensure area remains clear for entire flight
- Account for GPS drift tolerance (~10 foot radius)
- Have spotter maintain position awareness

**❌ DON'T:**
- Plan to launch from one location and land at another
- Move vehicles/equipment from takeoff area during flight
- Allow people to occupy landing zone
- Attempt to change landing location mid-mission

**Workarounds for Multi-Battery Missions:**
- Battery swaps must occur at same location
- Use hand catch/launch at takeoff point
- Or land, swap battery, takeoff from same spot
- Keep extra batteries warm and ready

### 3. Saving Scans Properly

**CRITICAL: Data Management**

**Discovered Challenges:**
Properly saving scan data is critical to avoid data loss and ensure successful processing.

**Proper Save Procedure:**
1. **During mission planning:**
   - Give scan descriptive name (date, location, purpose)
   - Example: "2025-11-07_Grocery_Store_200ft"
   - Save mission plan before flight

2. **After flight completion:**
   - Wait for drone to fully land and disarm
   - Verify flight data recorded
   - Check image count on drone status
   - Allow time for data finalization (30 seconds)

3. **Before powering down:**
   - Confirm scan appears in flight log
   - Verify image count matches expected
   - Note any warnings or errors

4. **SD Card Management:**
   - Don't remove SD card immediately after landing
   - Wait for all writes to complete
   - Safely remove (don't power off drone with card mid-write)

**Common Mistakes to Avoid:**
- ❌ Powering off drone too quickly after landing
- ❌ Not naming missions descriptively
- ❌ Pulling SD card before data write completes
- ❌ Overwriting previous scans unintentionally
- ❌ Not verifying image count before moving on

---

## Executing the Mapping Mission

### Step-by-Step Flight Procedure

**1. Setup and Preflight (20 minutes)**
- Complete full preflight checklist
- Verify mission loaded in controller
- Confirm weather acceptable
- Mark takeoff/landing location
- Clear area of people/obstacles
- Pair controller (without moving drone)

**2. Takeoff (2 minutes)**
- Hand launch or ground takeoff
- Climb to safe altitude (50 feet)
- Verify controls responsive
- Check GPS lock and home point
- Position for mission start

**3. Mission Execution (30-40 minutes for 1000 images)**
- Start automated mission
- Monitor progress on controller
- Watch for obstacles
- Check battery levels continuously
- Monitor wind conditions
- Verify camera capturing images

**4. Landing (2 minutes)**
- Return to home point (automated or manual)
- Descend to landing area
- Hand catch or ground landing
- Disarm motors
- Wait for data save completion

**5. Post-Flight (10 minutes)**
- Remove and secure battery
- Verify scan saved properly
- Check image count (~1000 expected)
- Log flight details
- Prepare for battery swap if needed

---

## Data Volume and Storage

### Understanding Data Requirements

**Image File Sizes:**
- Visual camera: ~8-12 MB per image
- 1000 images = ~8-12 GB total
- Plus flight logs and metadata

**SD Card Requirements:**
- Minimum: 32 GB
- Recommended: 64 GB or larger
- Use high-speed cards (U3 or V30 rated)
- Have backup card available

**Storage Planning:**
- Multiple missions per day = 20-40 GB
- Allow 2x space for safety margin
- Format cards between projects (after backup)

---

## Monitoring Flight Progress

### What to Watch During Mission

**Controller Display:**
- Battery level (return before 20% remaining)
- GPS signal strength (should stay strong)
- Altitude (should remain consistent)
- Flight path progress
- Image capture indicator
- Obstacle alerts

**Visual Observation:**
- Maintain visual line of sight
- Watch for aircraft
- Monitor wind effects
- Check for obstacles in path
- Verify systematic coverage

**Decision Points:**
- **Battery at 30%:** Consider returning
- **Wind increasing:** May need to abort
- **GPS issues:** Land and troubleshoot
- **Obstacle detected:** Verify clearance
- **People in area:** Pause mission

---

## Lessons Learned from Quinhagak Grocery Store Mission

### Key Takeaways

**1. Controller Pairing:**
- Stationary drone during pairing is essential
- Prevents initialization errors
- Saves time and frustration
- Worth the extra care

**2. Landing Location:**
- Same spot takeoff/landing is required
- Mark location clearly
- Keep area clear throughout flight
- Plan for GPS accuracy tolerance

**3. Data Saving:**
- Proper naming prevents confusion
- Verify saves before moving on
- Allow time for data write completion
- Check image counts

**4. Flight Parameters:**
- 200 feet altitude works well for building-scale mapping
- 80/80 overlap provides excellent results
- 1000 images is manageable but requires planning
- Multiple batteries likely needed

**5. Time Management:**
- Allow full mission time plus buffers
- Don't rush setup or teardown
- Data management takes time
- Weather windows may be limited

---

## Review Questions

1. What altitude was used for the grocery store mapping mission?
2. What overlap percentages were configured, and why?
3. Why must the drone not be moved during controller pairing?
4. Why must the drone take off and land at the same location?
5. How many images were captured in the grocery store mission?
6. What are the risks of powering down the drone too quickly after landing?
7. What SD card capacity is recommended for mapping missions?
8. At what battery percentage should you consider returning to home?

---

## Practical Exercise

**Plan a Mapping Mission:**

**Objective:** Plan a mapping mission for a building or area in your community

**Requirements:**
1. Select target area
2. Determine appropriate altitude (150-250 feet)
3. Set overlap (75-80%)
4. Estimate number of images
5. Calculate flight time
6. Determine battery requirements
7. Identify takeoff/landing location
8. Create equipment checklist
9. Document potential obstacles

**Time:** 30 minutes

---

## Key Takeaways

- **Mapping missions require careful planning** - altitude, overlap, batteries
- **80/80 overlap is excellent** for orthomosaics and 3D models
- **Do not move drone during pairing** - causes initialization errors
- **Takeoff and landing at same location is required** - GPS and RTH functionality
- **Proper scan saving is critical** - avoid data loss
- **1000 images = substantial dataset** - requires adequate storage and processing
- **Monitor battery levels constantly** - plan for return with reserve
- **Documentation and checklists prevent mistakes**

---

## Next Lesson

[Lesson 10: Data Upload Workflows - Site Scan and Skydio Cloud](./lesson10_data_upload.md)

You'll learn how to transfer imagery from the drone to processing platforms using SD cards and direct network connections.
