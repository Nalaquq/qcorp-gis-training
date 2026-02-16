# Activity 7: 3D Scanning Mission - Structure from Motion

**Training Date:** December 4-5, 2024
**Field Scan Reference:** November 24, 2025 (Nunalleq Museum)
**Duration:** Full day (8+ hours including processing)
**Prerequisites:** Lessons 9-13, Activity 6 completed

---

## Activity Overview

This activity guides you through planning, executing, and analyzing a complete 3D scanning mission using the Skydio X10's 3D Capture (3DC) mode. Based on the successful Nunalleq Museum scan, you'll learn to create high-resolution 3D models of buildings and structures, manage operational safety in active environments, and process results using both Metashape and Site Scan workflows.

### 🎥 Example: Nunalleq Museum 3D Model

**See what you'll create:** (Click thumbnail to watch on YouTube)

[![Nunalleq Museum 3D Model - Reference Example](https://img.youtube.com/vi/0wXSd0GDpUo/maxresdefault.jpg)](https://youtu.be/0wXSd0GDpUo?si=ytVeTywAJKatOsaN)

*This is the final 3D model created from 1,269 images captured during the reference scan. Your activity will follow the same workflow to create a similar model.*

---

## Learning Objectives

By completing this activity, you will be able to:

1. Plan a 3D scanning mission with appropriate safety protocols
2. Configure 3DC scan settings for optimal coverage
3. Manage operational environment (roads, crowds, animals)
4. Execute multi-flight scanning missions with battery swaps
5. Capture 1,000+ images for structure from motion processing
6. Review point clouds and identify coverage gaps
7. Process 3D models in both Metashape and ArcGIS Site Scan
8. Compare processing workflows and results
9. Share 3D models via multiple platforms
10. Document lessons learned and best practices

---

## Mission Overview

**Reference Project:** Nunalleq Museum 3D Scan
**Your Target:** [Community building to be determined]

**Mission Objectives:**
- Create high-resolution 3D model of building
- Document all surfaces with 80/80 overlap
- Practice operational safety protocols
- Generate point cloud, mesh, and orthomosaic products
- Compare Metashape vs Site Scan processing
- Share results with community

**Expected Outcomes:**
- 1,000-1,500 georeferenced images
- Dense 3D point cloud
- Textured 3D mesh
- High-resolution orthomosaic (< 0.1" GSD)
- DSM (Digital Surface Model)
- Published visualization (YouTube or web viewer)

---

## Part 1: Mission Planning (60 minutes)

### Task 1.1: Site Selection and Assessment

**Choose Target Building:**
- [ ] Select appropriate building for 3D scanning
- [ ] Size similar to Nunalleq Museum (4,000-6,000 sq ft recommended)
- [ ] Architectural interest or community importance
- [ ] Accessible location for drone operations
- [ ] Permission obtained from building owner/community

**Environmental Assessment:**
- [ ] Survey surrounding area
- [ ] Identify adjacent roads and traffic patterns
- [ ] Note pedestrian activity areas
- [ ] Observe animal patterns (dogs, etc.)
- [ ] Assess lighting conditions
- [ ] Check for overhead obstacles (power lines, etc.)
- [ ] Identify safe takeoff/landing location

**Safety Hazards Checklist:**

| Hazard Type | Present? | Mitigation Strategy |
|-------------|----------|---------------------|
| Adjacent road with vehicle traffic | ☐ Yes ☐ No | _________________________ |
| ATVs/snowmobiles | ☐ Yes ☐ No | _________________________ |
| Pedestrian foot traffic | ☐ Yes ☐ No | _________________________ |
| Children playing | ☐ Yes ☐ No | _________________________ |
| Village dogs | ☐ Yes ☐ No | _________________________ |
| Power lines | ☐ Yes ☐ No | _________________________ |
| Other: __________ | ☐ Yes ☐ No | _________________________ |

### Task 1.2: 3DC Scan Configuration

**Review Nunalleq Museum Settings:**
- Scan area: 4,878.5 sq ft
- Distance to surface: 16.4 ft
- Overlap: 80% / Sidelap: 80%
- Scan passes: X, Y, Z all enabled
- Images captured: 1,269
- Flight time: 27 minutes (2 flights)
- Batteries: 2
- Effective GSD: 0.08 inches

**Your Scan Parameters:**

| Parameter | Value | Reason |
|-----------|-------|--------|
| Building size estimate | _______ sq ft | Measured/estimated |
| Distance to surface | _______ ft | 15-20 ft recommended for buildings |
| Overlap (front) | _______% | 80% recommended |
| Sidelap (side) | _______% | 80% recommended |
| Scan volume - Above ceiling | ☐ Enable ☐ Disable | Usually disabled for exterior scans |
| Scan volume - Below floor | ☐ Enable ☐ Disable | Enable for ground detail |
| Scan volume - Outside walls | ☐ Enable ☐ Disable | Enable for exterior facades |
| Scan volume - Inside | ☐ Enable ☐ Disable | Enable for coverage |
| Extend capture area | _______ ft | 8-10 ft recommended |
| Scan passes - X axis | ☐ Enable ☐ Disable | Enable all three for complete coverage |
| Scan passes - Y axis | ☐ Enable ☐ Disable | Enable all three |
| Scan passes - Z axis | ☐ Enable ☐ Disable | Enable all three |

**Camera Settings:**
- [ ] Camera: VT300-L Wide (standard for X10)
- [ ] Resolution: 1/4 (balance of quality and processing time)
- [ ] Capture mode: Standard
- [ ] Thermal camera: ☐ On ☐ Off (optional, interesting for analysis)

**Visual Geofence:**
- [ ] Strict ceiling: ☐ Enable ☐ Disable
- [ ] Strict floor: ☐ Enable ☐ Disable (enable for safety)
- [ ] Strict walls: ☐ Enable ☐ Disable (enable for safety)

**Projections:**
- [ ] Estimated images: _______ (compare to Nunalleq: 1,269)
- [ ] Estimated flight time: _______ minutes
- [ ] Batteries required: _______ (minimum 2 recommended)
- [ ] Battery swap needed: ☐ Yes ☐ No

### Task 1.3: Safety Protocol Planning

**Road Closure Plan:**
- [ ] Roads needing closure: _________________________
- [ ] Closure method: ☐ Cones ☐ Signs ☐ Team members ☐ Coordination with authorities
- [ ] Closure duration estimate: _______ minutes
- [ ] Communication plan with drivers: _________________________
- [ ] Emergency vehicle access maintained: ☐ Yes ☐ No

**Crowd Management Plan:**
- [ ] Safety perimeter distance: _______ feet
- [ ] Method of crowd control: _________________________
- [ ] Team member assignments:
  - Pilot: _________________________
  - Visual observer: _________________________
  - Road monitor 1: _________________________
  - Road monitor 2: _________________________
  - Crowd management: _________________________
- [ ] Children safety briefing plan: _________________________
- [ ] Community notification: ☐ Advance notice ☐ Day-of notice

**Animal Management Plan:**
- [ ] Known dog issues in area: ☐ Yes ☐ No
- [ ] Animal management strategy: _________________________
- [ ] Pause/abort procedures: _________________________

### Task 1.4: Regulatory and Weather Checks

**Airspace:**
- [ ] Airspace class: _______
- [ ] TFR check: ☐ Clear ☐ Restricted
- [ ] Local airport distance: _______ miles
- [ ] CTAF frequency: _______
- [ ] NOTAMs checked: ☐ Yes ☐ No

**Weather Assessment:**
- [ ] Wind speed: _______ mph (< 20 mph ideal)
- [ ] Temperature: _______ °F (battery performance consideration)
- [ ] Visibility: _______ miles (minimum 3 miles)
- [ ] Cloud ceiling: _______ feet (must stay below)
- [ ] Precipitation: ☐ None ☐ Light ☐ Heavy (none required)
- [ ] Forecast for mission window: _________________________
- [ ] Backup date if needed: _________________________

### Task 1.5: Equipment Preparation

**Essential Equipment:**
- [ ] Skydio X10 charged and inspected
- [ ] Minimum 3 batteries fully charged and pre-warmed
- [ ] Flight Deck controller fully charged
- [ ] SD card formatted (minimum 32GB, 64GB+ recommended)
- [ ] FAA radio with fresh batteries
- [ ] Safety vests for all team members
- [ ] First aid kit
- [ ] Backup propellers
- [ ] Backup SD card
- [ ] Weather meter (wind/temp)
- [ ] Documentation materials (logbook, checklists)
- [ ] Traffic cones/signs (if needed for road closure)
- [ ] Portable power bank for controller
- [ ] Team communication devices (radios or phones)

**Data Management Equipment:**
- [ ] Computer for reviewing images
- [ ] SD card reader
- [ ] External hard drive for backup (project may be 20-40 GB)
- [ ] Metashape software installed and licensed
- [ ] ArcGIS Site Scan account access verified
- [ ] Skydio Cloud account access verified
- [ ] Internet connection tested (Starlink or other)

---

## Part 2: Mission Execution (90-120 minutes)

### Task 2.1: Site Setup and Team Briefing

**Site Setup:**
- [ ] Arrive at site 30 minutes before planned flight
- [ ] Set up safety perimeter with cones/signs
- [ ] Position team members at key locations
- [ ] Test communication between team members
- [ ] Identify and mark takeoff/landing location
- [ ] Clear takeoff/landing area of obstacles
- [ ] Set up equipment staging area

**Team Briefing:**
- [ ] Review mission objectives
- [ ] Assign roles and responsibilities
- [ ] Review safety protocols
- [ ] Establish communication procedures
- [ ] Review hand signals (if radios fail)
- [ ] Discuss abort procedures
- [ ] Review emergency procedures
- [ ] Questions and concerns addressed

**Community Coordination:**
- [ ] Road closure initiated
- [ ] Community members notified
- [ ] Children moved to safe distance
- [ ] Dogs secured or managed
- [ ] Brief curious onlookers on what's happening

### Task 2.2: Pre-Flight Procedures

**Official Skydio X10 Checklist:**
- [ ] Follow [Skydio X10 Flight Checklist](../resources/SkydioX10_Flight_Checklist_A0460.pdf) completely
- [ ] Visual inspection of aircraft (propellers, arms, body, sensors)
- [ ] Battery 1 fully charged: _______% (should be 100%)
- [ ] Battery 1 installed and secured
- [ ] Controller powered on
- [ ] Controller paired with X10 (**DO NOT MOVE DRONE during pairing**)
- [ ] GPS lock achieved: _______ satellites (6+ required)
- [ ] Home point set and verified
- [ ] Camera checks (visual and thermal if enabled)
- [ ] System status: ☐ All clear ☐ Warnings (note: _______)
- [ ] FAA radio monitoring active on CTAF

**3DC Scan Configuration:**
- [ ] Open Skydio app on Flight Deck
- [ ] Select "3D Scan" mode
- [ ] Name scan: "___________ 3D Scan [DATE]"
- [ ] Point to building and frame scan volume
- [ ] Adjust pillars (waypoints) as needed: _______ pillars
- [ ] Review auto-generated flight path
- [ ] Verify scan settings:
  - Distance to surface: _______ ft
  - Overlap: _______% / Sidelap: _______%
  - Scan passes: X ☐ Y ☐ Z ☐
  - Scan volume options confirmed
- [ ] Flight time estimate: _______ minutes
- [ ] Save scan plan

**Final Go/No-Go Check:**
- [ ] Weather acceptable: ☐ Yes ☐ No
- [ ] Team in position: ☐ Yes ☐ No
- [ ] Area secure: ☐ Yes ☐ No
- [ ] Aircraft ready: ☐ Yes ☐ No
- [ ] Clearance to launch: ☐ Yes ☐ No

### Task 2.3: Flight 1 Execution

**Takeoff:**
1. [ ] Final area scan for hazards
2. [ ] Announce "Launching" to team
3. [ ] Hand launch drone following proper technique
4. [ ] Climb to safe altitude (50-75 feet)
5. [ ] Verify controls responsive
6. [ ] Check GPS lock maintained
7. [ ] Verify home point
8. [ ] Position at scan start point

**Mission Start:**
- [ ] Start 3DC scan mission
- [ ] Scan start time: _______
- [ ] Initial battery level: _______%

**During Flight 1 Monitoring:**
- [ ] Monitor Flight Deck display continuously
- [ ] Watch for:
  - Battery levels (constant attention)
  - GPS signal strength
  - Image capture indicators (should see count increasing)
  - Obstacle alerts
  - Aircraft in area (visual and radio)
  - Ground hazards (vehicles, people, animals entering area)
- [ ] Team members reporting:
  - Road monitor: Any approaching vehicles?
  - Crowd monitor: Area still secure?
  - Visual observer: Aircraft visible and safe?

**Flight 1 Log:**
- Start battery: _______%
- Image count at 50%: _______ images
- Image count at 25% battery: _______ images
- Weather changes: _________________________
- Issues encountered: _________________________
- Team communications: _________________________

**Landing for Battery Swap:**
- [ ] Monitor battery - plan landing at 20-25%
- [ ] Announce "Returning for battery swap" to team
- [ ] Return to original takeoff location (CRITICAL - same location for scan continuity)
- [ ] Hand catch drone
- [ ] **DO NOT MOVE DRONE from landing location**
- [ ] Flight 1 end time: _______
- [ ] Flight 1 duration: _______ minutes
- [ ] Images captured in Flight 1: _______ images
- [ ] Battery 1 remaining: _______%

### Task 2.4: Battery Swap and Flight 2

**Quick Battery Change:**
- [ ] Keep drone in place at landing spot
- [ ] Remove Battery 1
- [ ] Install Battery 2 (pre-warmed if cold weather)
- [ ] Battery 2 level: _______% (should be 100%)
- [ ] Power on drone
- [ ] Wait for GPS lock (30-60 seconds)
- [ ] Verify home point still set
- [ ] Verify scan can resume
- [ ] Team status check: All clear?

**Flight 2 Execution:**
- [ ] Resume 3DC scan mission
- [ ] Scan resumes where it left off
- [ ] Flight 2 start time: _______
- [ ] Initial battery: _______%

**During Flight 2 Monitoring:**
- [ ] Continue all monitoring procedures
- [ ] Watch for fatigue in team members
- [ ] Maintain communication
- [ ] Monitor completion percentage on controller
- [ ] Note scan progress: 25% 50% 75% 90% 100%

**Flight 2 Log:**
- Start battery: _______%
- Image count at 50%: _______ images (total)
- Weather changes: _________________________
- Issues encountered: _________________________

**Mission Completion:**
- [ ] Scan reaches 100%
- [ ] Drone automatically returns to home
- [ ] Or manual return to landing spot
- [ ] Hand catch drone
- [ ] Motors disarmed
- [ ] **WAIT 30 seconds for data write to complete**
- [ ] Flight 2 end time: _______
- [ ] Flight 2 duration: _______ minutes
- [ ] Images captured in Flight 2: _______ images
- [ ] Battery 2 remaining: _______%

### Task 2.5: Post-Flight Procedures

**Immediate Actions:**
- [ ] Verify scan saved successfully
- [ ] Check total image count: _______ images (expect 1,000-1,500)
- [ ] Note any errors or warnings
- [ ] Remove batteries
- [ ] Remove SD card (wait 30 seconds after power off)
- [ ] Secure equipment

**Mission Log:**
- [ ] Total mission duration: _______ minutes
- [ ] Total flight time: _______ minutes
- [ ] Batteries used: _______
- [ ] Total images captured: _______
- [ ] Weather conditions: _________________________
- [ ] Issues/incidents: _________________________
- [ ] Lessons learned: _________________________

**Site Breakdown:**
- [ ] Thank and dismiss team members
- [ ] Remove traffic control measures
- [ ] Reopen roads
- [ ] Thank community members for patience
- [ ] Pack up all equipment
- [ ] Check for left items

**Data Backup:**
- [ ] Insert SD card into computer
- [ ] Verify images on SD card: _______ images
- [ ] Copy images to computer: /path/to/project/
- [ ] Backup to external hard drive
- [ ] Verify file sizes: ~8-12 MB per image
- [ ] Keep SD card as backup until processing complete

---

## Part 3: Point Cloud Review and Gap Analysis (60 minutes)

**Note:** This section is typically done the next day after initial processing

### Task 3.1: Initial Processing for Review

**Quick Processing in Metashape:**
- [ ] Import all images to Metashape
- [ ] Align photos (Medium quality for speed)
- [ ] Processing time for alignment: _______ minutes
- [ ] Generate sparse point cloud
- [ ] Export sparse cloud for review (PLY format)

**OR Use Site Scan Quick Preview:**
- [ ] Upload images to Site Scan
- [ ] Wait for automatic preview generation
- [ ] Preview available: ☐ Yes ☐ No

### Task 3.2: Point Cloud Quality Review

**Open Point Cloud in Viewer:**
- [ ] Software used: ☐ Metashape ☐ CloudCompare ☐ ArcGIS Pro ☐ Other: _______
- [ ] Load point cloud file
- [ ] Initial observation: _________________________

**Coverage Assessment:**

**Rotate and View from Multiple Angles:**
- [ ] Top view: Coverage complete? ☐ Yes ☐ Partial ☐ Gaps
- [ ] Front view: All surfaces visible? ☐ Yes ☐ Partial ☐ Gaps
- [ ] Side views (both): Complete? ☐ Yes ☐ Partial ☐ Gaps
- [ ] Back view: Coverage? ☐ Yes ☐ Partial ☐ Gaps
- [ ] Ground level: Captured? ☐ Yes ☐ Partial ☐ Gaps

**Identify Gaps:**

| Location | Size (estimate) | Likely Cause | Priority (H/M/L) |
|----------|----------------|--------------|------------------|
| _______________ | _______ sq ft | _________________ | ☐ H ☐ M ☐ L |
| _______________ | _______ sq ft | _________________ | ☐ H ☐ M ☐ L |
| _______________ | _______ sq ft | _________________ | ☐ H ☐ M ☐ L |
| _______________ | _______ sq ft | _________________ | ☐ H ☐ M ☐ L |
| _______________ | _______ sq ft | _________________ | ☐ H ☐ M ☐ L |

**Common Gap Causes:**
- Insufficient viewing angles
- Occlusion by building features (overhangs, alcoves)
- Deep shadows
- Strict geofence preventing close approach
- Featureless surfaces (blank walls, glass)
- Moving objects during scan (vehicles, people)

### Task 3.3: Plan Manual Supplementation

**For Each High-Priority Gap:**

**Gap 1: _________________________**
- [ ] Method: ☐ Additional drone flight ☐ Ground photography ☐ Both
- [ ] Equipment needed: _________________________
- [ ] Estimated images needed: _______
- [ ] Overlap to maintain: 70-80%
- [ ] Special considerations: _________________________

**Gap 2: _________________________**
- [ ] Method: ☐ Additional drone flight ☐ Ground photography ☐ Both
- [ ] Equipment needed: _________________________
- [ ] Estimated images needed: _______
- [ ] Overlap to maintain: 70-80%
- [ ] Special considerations: _________________________

**Manual Photo Collection Plan:**
- [ ] Schedule follow-up flight/photo session: _______
- [ ] Weather requirements: _________________________
- [ ] Team members needed: _______
- [ ] Estimated time: _______ minutes
- [ ] Execute manual collection: ☐ Complete ☐ Pending

---

## Part 4: Processing Comparison (Variable time)

### Task 4.1: Metashape Processing

**Setup Project:**
- [ ] Create new Metashape project
- [ ] Project name: "___________ 3D Scan"
- [ ] Save location: /path/to/project/
- [ ] Import all images: _______ images
- [ ] Verify GPS data present: ☐ Yes ☐ No

**Processing Steps:**

**Step 1: Align Photos**
- [ ] Menu: Workflow → Align Photos
- [ ] Accuracy: ☐ Highest ☐ High ☐ Medium
- [ ] Key point limit: 40,000 (default)
- [ ] Tie point limit: 4,000 (default)
- [ ] Start alignment
- [ ] Start time: _______
- [ ] Completion time: _______
- [ ] Duration: _______ minutes
- [ ] Cameras aligned: _______ of _______
- [ ] Tie points generated: _______

**Step 2: Build Dense Cloud**
- [ ] Menu: Workflow → Build Dense Cloud
- [ ] Quality: ☐ Ultra ☐ High ☐ Medium (High recommended)
- [ ] Depth filtering: ☐ Aggressive ☐ Moderate ☐ Mild
- [ ] Start processing
- [ ] Start time: _______
- [ ] Estimated completion: _______ hours
- [ ] **Note:** This step takes longest (4-12 hours for 1,000+ images)
- [ ] Can check progress periodically
- [ ] Completion time: _______
- [ ] Duration: _______ hours
- [ ] Point count: _______ million points

**Step 3: Build Mesh**
- [ ] Menu: Workflow → Build Mesh
- [ ] Source data: Dense cloud
- [ ] Surface type: ☐ Arbitrary ☐ Height field (Arbitrary for buildings)
- [ ] Face count: ☐ High ☐ Medium ☐ Low
- [ ] Start processing
- [ ] Duration: _______ minutes
- [ ] Face count: _______ triangles

**Step 4: Build Texture**
- [ ] Menu: Workflow → Build Texture
- [ ] Texture size: 4096 or 8192
- [ ] Start processing
- [ ] Duration: _______ minutes

**Step 5: Export Products**
- [ ] Export mesh: File → Export → Export Model (OBJ format)
- [ ] Export point cloud: File → Export → Export Points (LAS format)
- [ ] Build orthomosaic: Workflow → Build Orthomosaic
- [ ] Build DEM: Workflow → Build DEM
- [ ] Export orthomosaic: File → Export → Export Orthomosaic (GeoTIFF)
- [ ] Export DEM: File → Export → Export DEM (GeoTIFF)

**Metashape Results:**
- [ ] Total processing time: _______ hours
- [ ] Point cloud size: _______ million points
- [ ] Mesh size: _______ MB
- [ ] Orthomosaic resolution: _______ inches/pixel
- [ ] Success: ☐ Yes ☐ Partial ☐ Issues (note: _______)

### Task 4.2: ArcGIS Site Scan Processing

**Upload Images:**
- [ ] Access https://sitescan.arcgis.com
- [ ] Sign in with ArcGIS Online credentials
- [ ] Create new project: "__________ 3D Scan"
- [ ] Create new mission: "[DATE] 3DC Scan"
- [ ] Select upload method:
  - ☐ Direct SD card upload
  - ☐ Skydio Cloud sync
  - ☐ Manual file upload
- [ ] Start upload
- [ ] Upload start time: _______
- [ ] Upload completion time: _______
- [ ] Upload duration: _______ hours (can be long via Starlink)
- [ ] Images uploaded: _______ of _______
- [ ] Verify coverage map shows complete coverage

**Configure Processing:**
- [ ] Select outputs:
  - ☐ Orthomosaic (2D map)
  - ☐ Digital Surface Model (DSM)
  - ☐ 3D Mesh
  - ☐ Point Cloud (optional - large file)
- [ ] Quality: ☐ High ☐ Medium
- [ ] Coordinate system: WGS 84 or local CRS
- [ ] Format: GeoTIFF for rasters
- [ ] Start processing
- [ ] Processing start time: _______

**Monitor Processing:**
- [ ] Check status periodically
- [ ] Email notification when complete: ☐ Received
- [ ] Processing completion time: _______
- [ ] Processing duration: _______ hours

**Review Results:**
- [ ] Access processed outputs
- [ ] Review quality report:
  - Coverage: _______%
  - Resolution (GSD): _______ inches/pixel
  - Images used: _______ of _______
  - Reprojection error: _______ pixels
- [ ] Visual inspection quality: ☐ Excellent ☐ Good ☐ Fair ☐ Poor

**Site Scan Results:**
- [ ] Total time (upload + processing): _______ hours
- [ ] Orthomosaic resolution: _______ inches/pixel
- [ ] 3D mesh generated: ☐ Yes ☐ No
- [ ] Published to ArcGIS Online: ☐ Yes ☐ No
- [ ] Success: ☐ Yes ☐ Partial ☐ Issues (note: _______)

### Task 4.3: Processing Comparison

**Side-by-Side Comparison:**

| Metric | Metashape | Site Scan | Winner |
|--------|-----------|-----------|--------|
| **Total processing time** | _______ hrs | _______ hrs | _______ |
| **User effort** | ☐ High ☐ Med ☐ Low | ☐ High ☐ Med ☐ Low | _______ |
| **Point cloud detail** | _______ M pts | _______ M pts | _______ |
| **Mesh quality** | ☐ Excellent ☐ Good ☐ Fair | ☐ Excellent ☐ Good ☐ Fair | _______ |
| **Orthomosaic resolution** | _______ in/px | _______ in/px | _______ |
| **Visual quality** | ☐ Excellent ☐ Good ☐ Fair | ☐ Excellent ☐ Good ☐ Fair | _______ |
| **Export options** | ☐ Many ☐ Some | ☐ Many ☐ Some | _______ |
| **GIS integration** | ☐ Manual ☐ Automatic | ☐ Manual ☐ Automatic | _______ |
| **Cost consideration** | License: $______ | Subscription: $______ | _______ |
| **Internet requirement** | ☐ Not needed ☐ Needed | ☐ Not needed ☐ Needed | _______ |
| **Hardware requirement** | ☐ High-end ☐ Any | ☐ High-end ☐ Any | _______ |

**Your Preference:** ☐ Metashape ☐ Site Scan

**Justification:**
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________

---

## Part 5: Results Sharing (90 minutes)

### Task 5.1: Create YouTube Flythrough

**Render Animation in Metashape:**
- [ ] Open Metashape project
- [ ] Menu: View → Animation
- [ ] Create flythrough path around building
- [ ] Set keyframes at interesting viewpoints
- [ ] Preview animation
- [ ] Menu: File → Export → Export Animation
- [ ] Format: MP4 or AVI
- [ ] Resolution: 1920x1080 (HD)
- [ ] Frame rate: 30 fps
- [ ] Render animation
- [ ] Render time: _______ minutes

**Upload to YouTube:**
- [ ] Sign in to YouTube
- [ ] Upload video
- [ ] Title: "__________ 3D Model - [Location], [Date]"
- [ ] Description: Include scan details, image count, date, equipment
- [ ] Tags: 3D model, drone, photogrammetry, [location], Skydio X10
- [ ] Set privacy: ☐ Public ☐ Unlisted ☐ Private
- [ ] Publish video
- [ ] Video URL: _________________________________

**Example Reference - Nunalleq Museum:**

[![Nunalleq Museum 3D Model Example](https://img.youtube.com/vi/0wXSd0GDpUo/maxresdefault.jpg)](https://youtu.be/0wXSd0GDpUo?si=ytVeTywAJKatOsaN)

*Click to view the reference example - your video should look similar to this*

### Task 5.2: Publish to ArcGIS Online

**From Site Scan:**
- [ ] Already published during Site Scan processing: ☐ Yes ☐ No
- [ ] If not, select "Publish to ArcGIS Online"
- [ ] Configure item details:
  - Title: "__________ 3D Model [DATE]"
  - Summary: Brief description
  - Description: Full scan details
  - Tags: Relevant keywords
- [ ] Publish as 3D Scene Layer
- [ ] Publication complete
- [ ] Item URL: _________________________________

**Create Web Scene:**
- [ ] Open Scene Viewer in ArcGIS Online
- [ ] Add 3D scene layer
- [ ] Configure visualization
- [ ] Add basemap for context
- [ ] Create bookmarks for key views
- [ ] Enable measurement tools
- [ ] Save scene: "__________ 3D Scene [DATE]"
- [ ] Share with appropriate groups/public
- [ ] Scene URL: _________________________________

### Task 5.3: Share with Community

**Prepare Presentation Materials:**
- [ ] Screenshots of 3D model from multiple angles
- [ ] Key statistics (image count, resolution, etc.)
- [ ] YouTube video link
- [ ] Web scene link
- [ ] Explanation of what 3D scanning is
- [ ] Applications for community use

**Sharing Options:**
- [ ] Present at community meeting
- [ ] Share via social media
- [ ] Email to stakeholders
- [ ] Add to community website
- [ ] Create simple one-page handout

---

## Part 6: Scanniverse Supplemental Activity (30 minutes)

### Task 6.1: Small Object Scanning

**Identify Small Features:**
- [ ] Select 2-3 small objects or features related to building:
  - Door handle or architectural detail
  - Plaque or sign
  - Artifact or decoration
  - Other: ______________

**Scan with Scanniverse:**
- [ ] Open Scanniverse app on iPhone/iPad Pro
- [ ] Start new scan
- [ ] Scan object 1: ______________
  - Duration: _______ minutes
  - Quality: ☐ Excellent ☐ Good ☐ Fair
- [ ] Scan object 2: ______________
  - Duration: _______ minutes
  - Quality: ☐ Excellent ☐ Good ☐ Fair

**Export and Compare:**
- [ ] Export scans as OBJ files
- [ ] Compare resolution to drone scan
- [ ] Note advantages of each method
- [ ] Discuss when to use each approach

---

## Part 7: Documentation and Reflection (45 minutes)

### Task 7.1: Complete Mission Report

**Mission Summary Report:**

**Project Information:**
- Building scanned: _________________________
- Location: _________________________
- Date: _________________________
- Team members: _________________________

**Mission Statistics:**
- Total flight time: _______ minutes
- Batteries used: _______
- Images captured: _______
- Scan area: _______ sq ft
- Distance to surface: _______ ft
- Overlap: _______% / Sidelap: _______%
- Effective GSD: _______ inches

**Safety Protocols:**
- Road closure: ☐ Yes ☐ No ☐ N/A
- Crowd management: ☐ Yes ☐ No ☐ N/A
- Incidents: ☐ None ☐ Described below
- Incident details: _________________________

**Processing Results:**
- Metashape processing time: _______ hours
- Site Scan processing time: _______ hours
- Preferred workflow: _________________________
- Reason: _________________________

**Outputs Created:**
- ☐ Point cloud (_______ million points)
- ☐ 3D mesh
- ☐ Orthomosaic (_______ in/px resolution)
- ☐ DSM
- ☐ YouTube video
- ☐ ArcGIS Online scene

**Data Products URLs:**
- YouTube: _________________________________
- ArcGIS Online: _________________________________
- Other: _________________________________

### Task 7.2: Lessons Learned

**What Worked Well:**
1. _________________________________________________
2. _________________________________________________
3. _________________________________________________

**Challenges Encountered:**
1. _________________________________________________
2. _________________________________________________
3. _________________________________________________

**Solutions Applied:**
1. _________________________________________________
2. _________________________________________________
3. _________________________________________________

**Would Do Differently Next Time:**
1. _________________________________________________
2. _________________________________________________
3. _________________________________________________

**Key Insights:**
1. _________________________________________________
2. _________________________________________________
3. _________________________________________________

### Task 7.3: Technical Analysis

**Compare to Nunalleq Museum Scan:**

| Metric | Nunalleq Museum | Your Scan | Comparison |
|--------|-----------------|-----------|------------|
| Images captured | 1,269 | _______ | ☐ More ☐ Less ☐ Similar |
| Flight time | 27 min | _______ min | ☐ More ☐ Less ☐ Similar |
| Batteries | 2 | _______ | ☐ More ☐ Less ☐ Same |
| GSD | 0.08 in | _______ in | ☐ Better ☐ Worse ☐ Similar |
| Scan area | 4,878 sq ft | _______ sq ft | ☐ Larger ☐ Smaller ☐ Similar |

**Performance Notes:**
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________

---

## Assessment Criteria

### Successful Completion Requires:

**Planning (15 points)**
- [ ] Complete mission plan with appropriate parameters
- [ ] Comprehensive safety protocols
- [ ] Environmental assessment
- [ ] Team coordination plan

**Safety (25 points)**
- [ ] Effective road/crowd management implemented
- [ ] Team coordination successful
- [ ] No safety incidents
- [ ] Professional operations

**Execution (25 points)**
- [ ] Successful multi-flight mission
- [ ] 1,000+ images captured
- [ ] Complete coverage achieved
- [ ] Proper procedures followed

**Processing (20 points)**
- [ ] Both Metashape and Site Scan processing completed
- [ ] Quality assessment performed
- [ ] Gap analysis documented
- [ ] Thoughtful workflow comparison

**Sharing (10 points)**
- [ ] 3D model shared via at least 2 platforms
- [ ] Community presentation prepared
- [ ] Professional documentation

**Documentation (5 points)**
- [ ] Complete mission report
- [ ] Thoughtful lessons learned
- [ ] Technical analysis

**Total:** ______ / 100 points

---

## Deliverables

Submit the following:

1. [ ] Mission planning document with scan parameters
2. [ ] Safety protocol documentation
3. [ ] Flight logs with times and statistics
4. [ ] Point cloud gap analysis with screenshots
5. [ ] Processing comparison report (Metashape vs Site Scan)
6. [ ] YouTube video link
7. [ ] ArcGIS Online scene link
8. [ ] Mission summary report (3-5 pages)
9. [ ] Lessons learned document (1-2 pages)
10. [ ] Community presentation materials

---

## Key Takeaways

- **3D scanning requires meticulous planning** - Safety protocols essential
- **1,000+ images typical** for building-scale 3D models with 80/80 overlap
- **Multi-flight missions common** - Battery swaps must be at same location
- **Environmental management critical** - Road closure and crowd control necessary
- **Point cloud gaps are normal** - Manual supplementation often needed
- **Both processing workflows have merits** - Choose based on project needs
- **Sharing engages community** - Multiple platforms reach different audiences
- **Team coordination essential** - Communication and clear roles key to success
- **Hardware limitations real** - Plan processing time realistically
- **Documentation valuable** - Lessons learned improve future missions

---

## Next Steps

After completing this activity:

1. **Practice:** Plan and execute additional 3D scans
2. **Expand:** Try indoor scanning or larger structures
3. **Advance:** Experiment with GCPs for survey-grade accuracy
4. **Compare:** Multi-temporal scanning for change detection
5. **Share:** Present results to community stakeholders
6. **Teach:** Help others learn 3D scanning techniques

**Future Projects:**
- Cultural site documentation
- Infrastructure monitoring (erosion, buildings)
- Construction progress tracking
- Archaeological site recording
- Virtual museum exhibits

---

**Congratulations on completing your first 3D scanning mission!**

This advanced skill enables high-fidelity documentation of buildings, cultural sites, and infrastructure. With 1,000+ images processed into detailed 3D models, you've mastered one of the most powerful applications of drone technology for community mapping and cultural preservation.

---

**Activity Version:** 1.0
**Created:** December 8, 2025
**Reference Scan:** November 24, 2025 (Nunalleq Museum)
**Training Date:** December 4-5, 2024
