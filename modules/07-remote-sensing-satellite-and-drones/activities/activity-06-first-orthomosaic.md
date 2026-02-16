# Activity 6: First Orthomosaic Mapping Mission

**Training Date:** November 7, 2025
**Duration:** 4-5 hours (full mission workflow)
**Prerequisites:** Lessons 1-12 completed

---

## Activity Overview

This activity guides you through planning, executing, and processing your first complete orthomosaic mapping mission. You'll map a real-world location (grocery store), collect imagery data, upload to processing platforms, and integrate the results into ArcGIS Online.

---

## Learning Objectives

By completing this activity, you will be able to:

1. Plan a complete mapping mission from start to finish
2. Execute a mapping flight with appropriate parameters
3. Collect ~1000 images for orthomosaic creation
4. Upload data using SD card and network methods
5. Monitor processing in ESRI Site Scan
6. Publish orthomosaics to ArcGIS Online
7. Understand and work with DSM data
8. Manage drone-derived content effectively

---

## Mission Overview

**Target Area:** Quinhagak Grocery Store and surrounding area

**Mission Objectives:**
- Create high-resolution orthomosaic of grocery store
- Document building conditions and infrastructure
- Generate baseline data for future comparison
- Practice complete drone mapping workflow
- Produce GIS products for community use

**Expected Outcomes:**
- Orthomosaic map (~0.5-0.7 inch resolution)
- Digital Surface Model (DSM)
- ~1000 georeferenced images
- Published layers in ArcGIS Online

---

## Part 1: Mission Planning (30 minutes)

### Task 1.1: Define Mission Parameters

**Area Selection:**
- [ ] Identify grocery store location on map
- [ ] Define coverage area:
  - Entire grocery store building
  - Parking areas
  - Area behind store
  - ~50 foot buffer around targets
- [ ] Mark boundaries on map or flight planning software

**Flight Parameters:**

| Parameter | Value | Reason |
|-----------|-------|--------|
| Altitude | 200 feet AGL | Balances coverage with resolution |
| Front Overlap | 80% | Excellent for photogrammetry |
| Side Overlap | 80% | Ensures complete coverage |
| Flight Speed | Auto | Software calculates based on altitude |
| Camera Angle | Nadir (90° down) | Standard for orthomosaics |

**Calculations:**
- [ ] Estimate flight time: ~30-40 minutes
- [ ] Calculate coverage area: ___________ acres
- [ ] Expected image count: ~1000 images
- [ ] Batteries required: 2-3 (depending on conditions)
- [ ] Data storage needed: ~12 GB

### Task 1.2: Regulatory and Safety Checks

**Airspace:**
- [ ] Check airspace class (should be Class G)
- [ ] Verify no TFRs (Temporary Flight Restrictions)
- [ ] Note local airport location and traffic pattern
- [ ] Plan to monitor CTAF on FAA radio

**Weather Assessment:**
- [ ] Current conditions acceptable?
  - Wind: _______ mph (under 20 mph ideal)
  - Temperature: _______ °F (battery considerations)
  - Visibility: _______ miles (minimum 3 miles)
  - Cloud ceiling: _______ feet (must stay below clouds)
  - Precipitation: None (required)

**Safety:**
- [ ] Identify takeoff/landing location
- [ ] Mark location clearly
- [ ] Establish safety perimeter
- [ ] Identify emergency landing areas
- [ ] Brief any team members/spotters

### Task 1.3: Equipment Preparation

**Checklist:**
- [ ] Skydio X10 charged and inspected
- [ ] 3 batteries fully charged and pre-warmed
- [ ] Flight Deck controller charged
- [ ] SD card formatted with adequate space (32GB+)
- [ ] FAA radio with fresh batteries
- [ ] Safety equipment (vest, first aid)
- [ ] Backup equipment (propellers, SD card)
- [ ] Documentation materials (logbook, checklists)

**Data Management Preparation:**
- [ ] Belkin USB-C to Ethernet adapter
- [ ] Ethernet cable
- [ ] Starlink unit operational
- [ ] Computer ready for SD card reading
- [ ] ESRI Site Scan account access verified
- [ ] Skydio Cloud account access verified
- [ ] ArcGIS Online account ready

---

## Part 2: Flight Operations (60-90 minutes)

### Task 2.1: Pre-Flight Procedures

**Complete Official Checklist:**
- [ ] Follow [Skydio X10 Flight Checklist](../resources/SkydioX10_Flight_Checklist_A0460.pdf)
- [ ] Visual inspection of aircraft
- [ ] Battery installation and check
- [ ] Controller setup and pairing (DO NOT MOVE DRONE)
- [ ] GPS lock verification (6+ satellites)
- [ ] Camera checks (visual and thermal if available)
- [ ] System status check (no errors)
- [ ] Home point verification

**Flight Planning Software:**
- [ ] Load or create mission in Flight Deck
- [ ] Name mission: "2025-11-07_Grocery_Store_200ft"
- [ ] Verify flight path covers entire area
- [ ] Check estimated flight time vs battery capacity
- [ ] Save mission plan

**Final Checks:**
- [ ] Weather still acceptable?
- [ ] Area clear of people/obstacles?
- [ ] FAA radio monitoring active?
- [ ] Team briefed on procedures?
- [ ] Emergency procedures reviewed?

### Task 2.2: Execute Mapping Flight

**Takeoff:**
1. [ ] Mark takeoff location clearly (CRITICAL: must return here)
2. [ ] Hand launch drone following proper procedure
3. [ ] Climb to safe altitude (50-75 feet)
4. [ ] Verify controls responsive
5. [ ] Check GPS lock and home point
6. [ ] Position for mission start

**Mission Execution:**
1. [ ] Start automated mapping mission
2. [ ] Monitor progress on Flight Deck display
3. [ ] Watch for:
   - Battery levels (constant monitoring)
   - GPS signal strength
   - Image capture indicators
   - Obstacle alerts
   - Aircraft traffic (visual and radio)
4. [ ] Note flight time: _______ minutes
5. [ ] Monitor wind conditions

**Mission Checklist During Flight:**
- [ ] Maintain visual line of sight
- [ ] Monitor battery (don't go below 25% in cold)
- [ ] Listen to FAA radio
- [ ] Check systematic coverage pattern
- [ ] Verify camera capturing images
- [ ] Watch for people/vehicles entering area

**Landing:**
1. [ ] Return to original takeoff location (automatic or manual)
2. [ ] Descend carefully to landing area
3. [ ] Hand catch or ground landing
4. [ ] Disarm motors
5. [ ] **WAIT 30 seconds for data write completion**

### Task 2.3: Post-Flight Procedures

**Immediate:**
- [ ] Verify scan saved properly
- [ ] Check image count on controller (~1000 expected)
- [ ] Note any warnings or errors
- [ ] Remove and secure battery
- [ ] Log flight details:
  - Time: _______
  - Duration: _______ minutes
  - Images: _______ captured
  - Weather conditions: _______
  - Issues: _______

**Data Verification:**
- [ ] Confirm mission appears in flight log
- [ ] Note battery performance
- [ ] Document any unusual observations

---

## Part 3: Data Upload (60-90 minutes)

### Task 3.1: Method A - SD Card to ESRI Site Scan

**SD Card Removal:**
1. [ ] Ensure drone powered off completely
2. [ ] Wait 30 seconds after power off
3. [ ] Locate and remove SD card carefully
4. [ ] Store drone safely

**Transfer to Computer:**
1. [ ] Insert SD card into card reader
2. [ ] Verify card mounts successfully
3. [ ] Navigate to DCIM folder
4. [ ] Confirm ~1000 images present
5. [ ] Check file sizes (should be ~8-12 MB each)

**Upload to Site Scan:**
1. [ ] Access https://sitescan.arcgis.com
2. [ ] Sign in with ArcGIS Online credentials
3. [ ] Create new project: "Quinhagak Grocery Store Mapping"
4. [ ] Create new flight: "2025-11-07 200ft 80-80 overlap"
5. [ ] Select all images from SD card DCIM folder
6. [ ] Click Upload
7. [ ] **Do not close browser or remove SD card**
8. [ ] Monitor upload progress
9. [ ] Upload time: _______ minutes
10. [ ] Verify image count: _______ uploaded successfully

**Verify Upload:**
- [ ] All images uploaded (count matches)
- [ ] No upload errors reported
- [ ] Coverage map shows complete coverage
- [ ] Images georeferenced properly (dots on map)

### Task 3.2: Method B - Network Upload to Skydio Cloud

**Setup Network Connection:**
1. [ ] Keep drone powered on after flight
2. [ ] Verify Starlink unit operational
3. [ ] Connect Belkin USB-C to Ethernet adapter to X10
4. [ ] Connect Ethernet cable to adapter
5. [ ] Connect other end to Starlink
6. [ ] **Do not move drone during connection**
7. [ ] Wait for network connection (30-60 seconds)
8. [ ] Verify connection established

**Upload to Skydio Cloud:**
1. [ ] Access https://cloud.skydio.com on computer
2. [ ] Sign in with Skydio account
3. [ ] Verify X10 appears as online
4. [ ] Select grocery store flight
5. [ ] Choose "Upload to Cloud"
6. [ ] Select all data (images, logs, metadata)
7. [ ] Start upload
8. [ ] **Keep drone connected and powered**
9. [ ] Monitor upload progress
10. [ ] Upload time: _______ minutes
11. [ ] Verify completion (100%)

**Post-Upload:**
- [ ] Verify all data uploaded successfully
- [ ] Safely disconnect Ethernet
- [ ] Remove USB-C adapter
- [ ] Power off drone
- [ ] Store equipment properly

---

## Part 4: Processing (Waiting Period: 4-8 hours)

### Task 4.1: Initiate Processing in Site Scan

**Configure Processing:**
1. [ ] In Site Scan, access uploaded flight
2. [ ] Click "Process" or "Start Processing"
3. [ ] Select outputs:
   - ✅ Orthomosaic (2D map)
   - ✅ Digital Surface Model (DSM)
   - ✅ 3D Mesh (optional)
   - ⬜ Point Cloud (optional - very large file)

4. [ ] Set processing options:
   - Quality: High
   - Resolution: Auto (based on 200ft altitude)
   - Coordinate System: WGS 84 Web Mercator (or local)
   - Format: GeoTIFF

5. [ ] Start processing
6. [ ] Note start time: _______

**Expected Processing Time:**
- Orthomosaic: 2-4 hours
- DSM: 1-2 hours
- Total: 4-8 hours (typically processes overnight)

**Monitor Processing:**
- [ ] Check status periodically
- [ ] Watch for error notifications
- [ ] Note completion email

---

## Part 5: Results Review (45 minutes)

### Task 5.1: Processing Quality Assessment

**When Processing Complete:**

1. [ ] Return to Site Scan project
2. [ ] Access processing results
3. [ ] Open quality report
4. [ ] Review key metrics:
   - Coverage: _______% (expect 100%)
   - Resolution (GSD): _______ inches/pixel (expect ~0.5-0.7")
   - Images used: _______ of _______ (should be most/all)
   - Reprojection error: _______ pixels (lower is better)

### Task 5.2: Visual Inspection

**Orthomosaic Quality:**
- [ ] Zoom to grocery store building
- [ ] Check building details sharp and clear
- [ ] Inspect roof features visible
- [ ] Examine area behind store
- [ ] Look for stitching artifacts (seams)
- [ ] Check color consistency
- [ ] Verify no distortion
- [ ] Inspect edges of coverage area

**Quality Assessment:**
- Overall quality: ☐ Excellent ☐ Good ☐ Acceptable ☐ Poor
- Issues found: _______________________________
- Suitable for intended use: ☐ Yes ☐ No

### Task 5.3: DSM Review

**Digital Surface Model:**
- [ ] Access DSM layer
- [ ] Apply elevation color ramp
- [ ] Visually inspect:
  - Building elevation visible
  - Trees showing height
  - Ground elevations reasonable
  - No obvious errors or holes

**Sample Measurements:**
- Grocery store roof elevation: _______ feet
- Ground elevation (parking lot): _______ feet
- Estimated building height: _______ feet
- Tree heights behind store: _______ feet

---

## Part 6: ArcGIS Online Integration (60 minutes)

### Task 6.1: Publish Orthomosaic

**From Site Scan to ArcGIS Online:**
1. [ ] In Site Scan, select orthomosaic
2. [ ] Click "Publish to ArcGIS Online"
3. [ ] Configure item details:
   - Title: "Quinhagak Grocery Store Orthomosaic 2025-11-07"
   - Summary: "High-resolution drone orthomosaic of grocery store and surrounding area"
   - Description: "Captured November 7, 2025 at 200ft altitude with 80/80 overlap. ~1000 images processed. Resolution ~0.5-0.7 inches/pixel."
   - Tags: "drone, orthomosaic, Quinhagak, grocery store, November 2025, Skydio X10"
   - Credits: "Nalaquq Inc. / Qanirtuuq Inc."

4. [ ] Set publish options:
   - Type: Imagery Layer
   - Format: Cloud Optimized GeoTIFF
   - Sharing: Private (initially)

5. [ ] Click "Publish"
6. [ ] Wait for publication to complete
7. [ ] Note item URL: _______________________

### Task 6.2: Content Organization

**In ArcGIS Online:**

1. [ ] Navigate to Content tab
2. [ ] Create folder structure:
   ```
   Drone Missions/
   └── 2025-11/
       └── 2025-11-07_Grocery_Store/
   ```

3. [ ] Move orthomosaic to folder
4. [ ] Add/edit item details if needed
5. [ ] Review metadata

**Create Group:**
- [ ] Create group: "Quinhagak Drone Mapping Team"
- [ ] Add relevant team members
- [ ] Share orthomosaic with group

### Task 6.3: Create Web Map

**Build Interactive Map:**

1. [ ] Open Map Viewer in ArcGIS Online
2. [ ] Add orthomosaic layer
3. [ ] Add World Imagery basemap for comparison
4. [ ] Configure swipe tool to compare drone vs satellite
5. [ ] Add bookmarks for key areas:
   - Building overview
   - Parking area
   - Behind store
   - Building details

6. [ ] Configure pop-ups with metadata
7. [ ] Set appropriate scale ranges
8. [ ] Save map: "Grocery Store Drone Survey 2025-11-07"
9. [ ] Share with appropriate groups

---

## Part 7: Analysis and Documentation (45 minutes)

### Task 7.1: Conduct Basic Analysis

**Measurements:**

Using measurement tools on orthomosaic:

1. [ ] Measure building dimensions:
   - Length: _______ feet
   - Width: _______ feet
   - Roof area: _______ sq ft

2. [ ] Measure parking lot area: _______ sq ft

3. [ ] Count visible features:
   - Vehicles: _______
   - Doors: _______
   - Other: _______

**Observations:**
Document building condition, infrastructure, and notable features:
_________________________________________
_________________________________________
_________________________________________

### Task 7.2: Create Mission Report

**Complete Mission Summary:**

**Mission Details:**
- Date: November 7, 2025
- Location: Quinhagak Grocery Store
- Pilot: _______________________
- Weather: _______________________

**Flight Parameters:**
- Altitude: 200 feet AGL
- Overlap: 80% front / 80% side
- Images captured: ~1000
- Flight time: _______ minutes
- Batteries used: _______

**Processing:**
- Platform: ESRI Site Scan
- Processing time: _______ hours
- Output resolution: _______ inches/pixel
- Products created: Orthomosaic, DSM

**Results:**
- Quality: ☐ Excellent ☐ Good ☐ Acceptable
- Issues encountered: _______________________
- Lessons learned: _______________________
- Recommendations: _______________________

**Data Products:**
- Orthomosaic URL: _______________________
- Web Map URL: _______________________
- Shared with: _______________________

---

## Part 8: Lessons Learned Discussion

### Reflection Questions

Discuss with team or document individually:

1. **Flight Planning:**
   - Were flight parameters appropriate?
   - What would you change next time?
   - How was the coverage area size?

2. **Operational Challenges:**
   - What challenges did you encounter?
   - How did weather affect operations?
   - Were there any equipment issues?
   - How was the takeoff/landing location choice?

3. **Data Management:**
   - Which upload method worked better?
   - Was SD card or network upload faster?
   - Any data management issues?
   - Was storage adequate?

4. **Processing and Results:**
   - Was processing time as expected?
   - Quality of final products?
   - Any processing errors?
   - What would improve results?

5. **Critical Lessons:**
   - Not moving drone during pairing
   - Importance of same takeoff/landing location
   - Proper scan saving procedures
   - Data backup strategies

---

## Assessment Criteria

### Successful Completion Requires:

**Planning (20 points)**
- [ ] Complete mission plan documented
- [ ] Appropriate flight parameters selected
- [ ] Safety protocols followed
- [ ] Equipment prepared properly

**Flight Operations (30 points)**
- [ ] Preflight checklist completed
- [ ] Safe flight execution
- [ ] ~1000 images captured
- [ ] Proper landing and post-flight procedures
- [ ] Critical lessons applied (no moving during pairing, same landing spot)

**Data Management (20 points)**
- [ ] Successful data upload (either or both methods)
- [ ] Proper file management
- [ ] Backup procedures followed

**Processing and Integration (20 points)**
- [ ] Processing initiated correctly
- [ ] Quality assessment completed
- [ ] Published to ArcGIS Online successfully
- [ ] Content organized properly

**Documentation (10 points)**
- [ ] Mission report complete
- [ ] Measurements and analysis documented
- [ ] Lessons learned recorded

---

## Deliverables

Submit the following:

1. [ ] Completed preflight checklist (with signatures)
2. [ ] Flight log with details
3. [ ] Mission report (2-3 pages)
4. [ ] Screenshot of orthomosaic in ArcGIS Online
5. [ ] Screenshot of web map with comparison tool
6. [ ] Quality assessment notes
7. [ ] Lessons learned summary (1 page)
8. [ ] ArcGIS Online item URL

---

## Key Takeaways

- **Complete workflow requires 6-10 hours** (including processing time)
- **Planning is critical** - don't skip any steps
- **Critical operational lessons:**
  - Do not move drone during controller pairing
  - Must takeoff and land at same location
  - Allow time for proper scan saving
- **80/80 overlap produces excellent results** for orthomosaics
- **200 feet altitude appropriate** for building-scale mapping
- **Both upload methods work** - SD card and network via Starlink
- **Processing takes several hours** - plan accordingly
- **Content organization matters** - structure from the start
- **Documentation is valuable** - record everything for future reference

---

## Next Steps

After completing this activity:

1. **Practice:** Plan and execute additional mapping missions
2. **Expand:** Map other areas of community
3. **Compare:** Create time series with repeat flights
4. **Share:** Present results to community partners
5. **Apply:** Use orthomosaics for planning and analysis

**Future Activities:**
- Change detection (comparing multiple dates)
- Advanced analysis (3D visualization, volume calculations)
- Integration with other data sources
- Community presentation

---

**Congratulations on completing your first orthomosaic mapping mission!**

This is a foundational skill that opens many possibilities for community mapping, monitoring, and analysis. With practice, you'll become more efficient and be able to tackle increasingly complex mapping projects.
