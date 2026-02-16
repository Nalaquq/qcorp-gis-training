# Lesson 13: 3D Mapping and Structure from Motion

**Duration:** 120 minutes
**Prerequisites:** Lessons 9-12 (Mapping Missions, Data Processing)
**Training Date Reference:** December 4-5, 2024
**Field Scan Date:** November 24, 2025

---

## Lesson Overview

This lesson covers advanced 3D mapping techniques using drone photogrammetry and structure from motion (SfM) technology. You'll learn how to capture imagery for 3D model creation, understand the principles of photogrammetry, work with point clouds, and compare different processing workflows. The lesson also covers mobile 3D scanning for smaller objects and features.

---

## Learning Objectives

By the end of this lesson, you will be able to:

1. Understand structure from motion (SfM) principles and photogrammetry
2. Plan and execute 3D scanning missions with the Skydio X10
3. Apply operational safety protocols for 3D mapping in active environments
4. Identify and mitigate obstacle avoidance limitations with moving objects
5. Understand image overlap requirements for 3D reconstruction
6. Review point clouds and identify coverage gaps
7. Supplement automated scans with manual photography
8. Use Scanniverse for small-object 3D modeling
9. Apply ground control points (GCPs) for accurate positioning
10. Compare processing workflows (Metashape vs ArcGIS Site Scan)
11. Understand hardware limitations for 3D modeling

---

## What is Structure from Motion?

### Definition

**Structure from Motion (SfM)** is a photogrammetric technique that reconstructs 3D structures from sequences of 2D images taken from different viewpoints.

### How SfM Works

**The Basic Principle:**

```
┌─────────────────────────────────────────────────────────────────┐
│                Structure from Motion Workflow                    │
└─────────────────────────────────────────────────────────────────┘

1. CAPTURE: Multiple Overlapping Images
   ┌────┐  ┌────┐  ┌────┐  ┌────┐
   │img1│→ │img2│→ │img3│→ │img4│  (1,269 images for Nunalleq)
   └────┘  └────┘  └────┘  └────┘
      ↓       ↓       ↓       ↓
   [Same features visible from different angles]

2. FEATURE DETECTION: Find distinctive points
   • Corners, edges, texture variations
   • Thousands of keypoints per image
   • Must be identifiable across multiple images

3. FEATURE MATCHING: Link same features across images
   Image 1: Point A ←──matched──→ Image 2: Point A'
   Creates "tie points" between images

4. CAMERA POSITION ESTIMATION (Motion)
   Calculate where each camera was positioned
   ┌───┐    ┌───┐    ┌───┐
   │ ◉ │    │ ◉ │    │ ◉ │  Camera positions in 3D space
   └───┘    └───┘    └───┘

5. 3D RECONSTRUCTION (Structure)
   Triangulate 3D position of each feature point
        Camera 1 ──────→ •
                      ╱   ╲  Point in 3D space
        Camera 2 ────→    ←──── Camera 3

6. DENSE POINT CLOUD: Millions of 3D points
   • • • • • • • •
   • • • • • • • •  (50+ million points possible)
   • • • • • • • •

7. MESH GENERATION: Continuous surface
   Converts points → triangulated mesh

8. TEXTURE MAPPING: Apply original photos
   Result: Photorealistic 3D model
```

**Key Concept:**
By observing how features appear to move between images (parallax), the software can calculate both:
- **Camera positions** (motion) - Where each of 1,269 photos was taken
- **3D structure** (structure) - Exact 3D coordinates of every visible point

### Why Overlap Matters

**Image Overlap Requirements:**

```
OVERLAP VISUALIZATION:

60% Overlap (Minimum):
┌────────┐
│  IMG1  │
└────────┘
     ┌────────┐
     │  IMG2  │  ←─ 60% shared area
     └────────┘
          ┌────────┐
          │  IMG3  │
          └────────┘

80% Overlap (Optimal for 3D):
┌────────┐
│  IMG1  │
└────────┘
   ┌────────┐
   │  IMG2  │  ←─ 80% shared area (Nunalleq scan used this)
   └────────┘
     ┌────────┐
     │  IMG3  │
     └────────┘
      ┌────────┐
      │  IMG4  │
      └────────┘

Result: Each ground point visible in 5-10+ images!
```

**Overlap Guidelines:**

For 2D orthomosaics:
- **60% overlap minimum** - Barely sufficient
- **70-80% overlap optimal** - Standard practice
- **Higher overlap** - Better for 3D reconstruction

For 3D models:
- **80%+ overlap recommended** - Ensures robust feature matching (Nunalleq used 80/80)
- **Multiple viewing angles** - Captures all surfaces
- **Orbital/circular patterns** - Better for vertical structures
- **Three-axis passes** - X, Y, Z for complete coverage

**What Happens with Good Overlap:**
- Each ground point visible in 5-10+ images
- More accurate 3D position calculations
- Better handling of textureless surfaces
- Fewer holes in final model
- Higher quality mesh generation

**What Happens with Poor Overlap:**
- Holes in 3D model
- Less accurate positioning
- Stitching artifacts
- Incomplete reconstruction
- Lower detail quality

---

## 3D Mapping with Skydio X10

### 3D Capture (3DC) Scan Mode

**Skydio 3DC Overview:**
- Automated 3D scanning mode
- Orbital flight patterns around subject
- Multiple altitudes and angles
- Designed for building and structure scanning
- Captures comprehensive imagery for SfM

**Typical 3DC Mission:**
- Subject selection (building, structure)
- Automated flight path planning
- Multiple circular orbits at varying heights
- Nadir (straight down) and oblique (angled) imagery
- Configurable scan volume (ceiling, floor, walls, inside)
- 5-30 minute scan duration depending on size

**3DC Scan Passes:**
- **Z-axis passes** - Horizontal orbits at different heights
- **Y-axis passes** - Vertical sweeps front to back
- **X-axis passes** - Vertical sweeps side to side
- All three passes ensure complete coverage

### Operational Safety Considerations

**Critical Safety Limitation:**

⚠️ **Obstacle avoidance does NOT work with moving objects**

**Why This Matters:**
- Skydio obstacle avoidance is excellent for static objects
- System cannot predict movement of vehicles, people, or animals
- Moving objects can cause collision risk
- Requires active environmental management

**Safety Protocols for 3D Scanning in Active Areas:**

1. **Road Closure:**
   - Close adjacent roads to vehicle traffic
   - Block ATVs, cars, and trucks
   - Use cones, signs, or team members
   - Coordinate with community

2. **Crowd Management:**
   - Keep children at safe distance
   - Manage curious onlookers
   - Establish safety perimeter
   - Brief community members beforehand

3. **Animal Control:**
   - Aware of village dogs
   - Monitor for approaching animals
   - Have plan to pause flight if needed
   - Consider time of day (fewer animals)

4. **Active Monitoring:**
   - Designated spotter for ground activity
   - Pilot maintains situational awareness
   - Ready to pause or abort mission
   - Communication protocols established

5. **Environmental Assessment:**
   - Survey area before flight
   - Identify potential moving hazards
   - Plan mitigation strategies
   - Brief all team members

**Example: Nunalleq Museum Scan**
- Location adjacent to active road
- Required road closure for ATVs, cars, trucks
- Village dogs managed during flight
- Children kept at safe distance
- Team coordination essential for safety

---

## Case Study: Nunalleq Museum 3D Scan

### 3D Model Video

**Watch the final 3D model flythrough:** (Click thumbnail to view on YouTube)

[![Nunalleq Museum 3D Model - Flythrough Video](https://img.youtube.com/vi/0wXSd0GDpUo/maxresdefault.jpg)](https://youtu.be/0wXSd0GDpUo?si=ytVeTywAJKatOsaN)

*This video shows the completed 3D model created from 1,269 images captured during the scan.*

---

### Mission Overview

**Project Details:**
- **Location:** Nunalleq Museum, Quinhagak, Alaska
- **GPS Coordinates:** 59.749749°N, 161.902696°W, 12.2m elevation
- **Field Scan Date:** November 24, 2025
- **Training Discussion:** December 4-5, 2024
- **Equipment:** Skydio X10 (SkydioX10-fz84)
- **Scan Mode:** 3D Capture (3DC)

### Scan Configuration

**Flight Parameters:**
- **Scan area:** 4,878.5 sq ft
- **Distance to surface:** 16.4 feet
- **Overlap:** 80% (front)
- **Sidelap:** 80% (side)
- **Scan volume settings:**
  - Below floor: Enabled
  - Inside: Enabled
  - Above ceiling: Disabled
  - Outside walls: Disabled
  - Extend capture area: 8.2 ft

**Scan Passes:**
- Z-axis: Enabled
- Y-axis: Enabled
- X-axis: Enabled

**Camera Settings:**
- **Camera:** VT300-L Wide
- **Resolution:** 1/4
- **Capture mode:** Standard
- **Thermal camera:** On
- **GSD (Effective):** 0.08 inches (extremely high resolution!)

### Mission Statistics

```
┌────────────────────────────────────────────────────────────────┐
│              NUNALLEQ MUSEUM 3D SCAN STATISTICS                │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  📐 SCAN AREA                        4,878.5 sq ft            │
│  📏 DISTANCE TO SURFACE              16.4 feet                │
│  📊 OVERLAP                          80% front / 80% side     │
│  🎯 EFFECTIVE GSD                    0.08 inches (2mm!)       │
│                                                                │
│  ✈️  FLIGHTS                         2 (battery swap)         │
│  🔋 BATTERIES USED                   2                        │
│  ⏱️  TOTAL FLIGHT TIME               27 minutes               │
│  📍 WAYPOINTS                        4 pillars                │
│                                                                │
│  📸 FLIGHT 1 IMAGES                  908                      │
│  📸 FLIGHT 2 IMAGES                  361                      │
│  📸 TOTAL IMAGES                     1,269 (all autonomous)   │
│  📸 MANUAL IMAGES                    0                        │
│                                                                │
│  ⚙️  SCAN PASSES                     X, Y, Z (all enabled)    │
│  📹 CAMERA                           VT300-L Wide             │
│  🌡️  THERMAL                         On                       │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

**Flight Timeline:**
- **Flight 1 Start:** 10:36:40 PM UTC, November 24, 2025
  - Images: 908
  - Battery swap required
- **Flight 2 Start:** 11:02:33 PM UTC, November 24, 2025
  - Images: 361
  - Scan completion
- **Processing Complete:** 11:11:17 PM UTC (~9 minutes after flight)

**Image Capture Settings:**
- All autonomous capture (0 manual photos)
- "Stop Vehicle for Photo" setting: Disabled
- Continuous capture during automated flight path

### Day 1: Mission Execution

**Preparation:**
- Identified museum building as subject
- Assessed operational environment
- Noted adjacent road with vehicle traffic
- Identified active area with dogs and children

**Safety Protocols Implemented:**
- **Road closure:** Stopped ATVs, cars, and trucks
- **Dog management:** Kept village dogs away during flight
- **Crowd control:** Ensured children at safe distance
- **Team coordination:** Multiple people managing environment
- **Active monitoring:** Constant awareness of moving hazards

**Flight Execution:**
1. Automated 3DC scan mode configured
2. Four scan pillars/waypoints established
3. Multiple orbital passes executed
4. Varying altitudes for complete coverage
5. Battery swap after first flight (908 images)
6. Second flight completed scan (361 images)
7. Total duration: 27 minutes flight time
8. Successful data capture of 1,269 images

### Educational Discussion During Scan

**Topics Covered:**

1. **Structure from Motion Principles:**
   - How computer builds 3D from 2D images
   - Feature matching across images
   - Triangulation of 3D points
   - Why 1,269 images needed for one building

2. **Image Overlap Requirements:**
   - Why 80%/80% overlap essential
   - How overlap affects quality
   - Coverage completeness
   - Trade-off between overlap and flight time

3. **Automated vs Manual Collection:**
   - When automation works well
   - When manual supplement needed
   - Hybrid approaches
   - Stop vehicle setting (disabled for this scan)

4. **Operational Safety:**
   - Obstacle avoidance limitations
   - Need for active environmental management
   - Community coordination essential
   - Team communication protocols

### Day 2: Point Cloud Review and Analysis

**Next Day Activities:**

**Point Cloud Analysis:**
1. Opened processed point cloud from overnight processing
2. Rotated and examined from all angles
3. Identified coverage holes
4. Discussed causes of gaps
5. Reviewed GSD of 0.08 inches - exceptional detail!

**Coverage Assessment:**

**Strengths of the Scan:**
- Extremely high resolution (0.08" GSD)
- 1,269 images provided excellent overlap
- 80/80 overlap settings worked perfectly
- Three-axis scanning (X, Y, Z) ensured comprehensive coverage
- Below floor and inside volume captured ground details

**Coverage Gaps Identified:**
- Areas behind deep overhangs
- Deep shadows under eaves
- Some wall sections in shadow
- Ground areas very close to building foundation
- Areas where strict floor geofence limited access

**Gap Discussion:**

**Why these holes appeared:**
- **Insufficient viewing angles** - Some areas only visible from limited angles
- **Occlusion** - Building features blocking view of some surfaces
- **Automated path limitations** - Strict floor geofence prevented very low angles
- **Shadow areas** - Low light conditions in deeply shadowed regions
- **Visual geofence constraints** - Strict floor and walls prevented closer approach

**Solutions Discussed:**

1. **Additional Drone Photos:**
   - Manual flight to specific gap areas
   - Lower altitude for ground-level details
   - Different angles for overhangs
   - Multiple passes with adjusted geofence

2. **Ground-Based Photography:**
   - Camera on tripod or handheld
   - Walk around building perimeter
   - Capture areas drone couldn't access
   - Maintain 70-80% overlap
   - Match lighting conditions if possible

3. **Adjusted Scan Settings:**
   - Disable or relax strict floor geofence
   - Enable "Outside Walls" for exterior detail
   - Increase "Extend Capture Area" beyond 8.2 ft
   - Adjust distance to surface (lower than 16.4 ft)

4. **Hybrid Approach:**
   - Automated 3DC for main coverage
   - Manual supplement for specific gaps
   - Combine datasets in processing
   - Reprocess with all images

---

## Photogrammetry Fundamentals

### Understanding the Process

**Concepts Covered:**

1. **Keypoint Detection:**
   - Software finds distinctive features
   - Corners, edges, texture variations
   - Must be identifiable across images
   - More keypoints = better reconstruction

2. **Feature Matching:**
   - Same feature in multiple images
   - Creates "tie points" linking images
   - More tie points = stronger model
   - Example: A window corner visible in 15+ images

3. **Bundle Adjustment:**
   - Optimizes camera positions
   - Minimizes reprojection error
   - Refines 3D point positions
   - Iterative refinement process

4. **Dense Reconstruction:**
   - Creates millions of 3D points
   - Based on stereo matching between images
   - Quality depends on overlap and resolution
   - 1,269 images = very dense point cloud

**Why 1,269 Images for One Building?**

**Coverage Requirements:**
- 80% front overlap = each point in 5+ images (front-to-back)
- 80% side overlap = each point in 5+ images (side-to-side)
- Multiple heights (Z-axis passes)
- Multiple viewing angles (X, Y axis passes)
- Ground coverage below building
- Interior volume scanning

**Quality Factors:**
- More images = more viewing angles
- More angles = better 3D accuracy
- Better accuracy = fewer holes
- Higher overlap = better feature matching
- Result: High-fidelity 3D model

---

## Point Cloud Analysis and Gap Identification

### Understanding Point Clouds

**What is a Point Cloud?**
- Collection of millions of 3D points
- Each point represents a position in space (X, Y, Z)
- Often includes color information (RGB)
- Can include intensity data
- Raw output of photogrammetric processing

**Point Cloud Characteristics:**
- **Density** - Points per square meter (very high with 0.08" GSD!)
- **Accuracy** - Positional precision
- **Coverage** - Completeness of scan
- **Color** - Visual information from photos

### Reviewing Point Clouds for Quality

**What to Look For:**

1. **Coverage Holes:**
   - Missing areas in the model
   - Gaps in walls, roofs, or ground
   - Incomplete features
   - Shadow areas with no data

2. **Point Density:**
   - Uniform density across model
   - Higher density in well-photographed areas
   - Lower density in limited-angle areas
   - Very low density = potential gaps

3. **Alignment Quality:**
   - Clean surfaces without noise
   - Sharp edges and corners
   - No duplicate/ghost geometry
   - Consistent scale throughout

### Manual Photo Supplementation

**Filling Gaps with Manual Photography:**

When automated scan misses areas, you can:

**Option 1: Additional Drone Flights**
1. Identify specific areas needing coverage
2. Fly manual mission to those areas
3. Capture overlapping images
4. Multiple angles if needed
5. Focus on problem areas

**Option 2: Ground-Based Photography**
1. Use camera (DSLR, phone, or drone camera)
2. Walk around subject
3. Capture overlapping photos of gap areas
4. Multiple angles and heights
5. Maintain consistent lighting

**Best Practices:**
- **Overlap** - Maintain 70-80% overlap
- **Lighting** - Match original scan lighting if possible
- **Resolution** - Similar photo quality
- **Coverage** - Slightly beyond gap area
- **Metadata** - GPS tag if possible

**Integration:**
- Add manual photos to dataset
- Reprocess in photogrammetry software
- Software integrates new images
- Fills gaps in point cloud
- Improves overall model quality

---

## Scanniverse for Small Objects

### When to Use Scanniverse

**Scanniverse Overview:**
- Mobile phone 3D scanning app
- Uses iPhone/iPad LiDAR sensor (Pro models)
- Quick 3D capture of small objects and features
- No drone required
- Immediate results

**Ideal Use Cases:**
- Archaeological artifacts
- Archaeological trenches
- Small cultural objects
- Building details (doorways, architectural features)
- Equipment and tools
- Personal items for documentation
- Features too small for drone (< 2 meters)

**Advantages Over Drone:**
- **Smaller scale** - Objects too small for drone
- **Indoor** - Works where drones can't fly
- **Quick** - Immediate capture, no flight planning
- **Accessible** - Just need a phone
- **Close detail** - Better for small features
- **Lower cost** - No drone flight needed
- **No FAA regulations** - Not subject to drone rules

### Scanniverse Workflow

**Basic Process:**

1. **Prepare Object:**
   - Clear area around object
   - Good, even lighting
   - Stable placement
   - Consider background

2. **Capture Scan:**
   - Open Scanniverse app
   - Start new scan
   - Walk slowly around object
   - Multiple heights/angles
   - Cover all surfaces
   - 2-5 minutes typical

3. **Process:**
   - App processes automatically
   - Creates 3D mesh
   - Applies textures
   - Usually 1-2 minutes

4. **Export:**
   - Export as OBJ, USDZ, or other formats
   - Share via email, cloud
   - Import to other software

**Archaeological Applications:**
- **Artifact documentation** - Create 3D record
- **Trench documentation** - Capture excavation layers
- **Context recording** - 3D spatial relationships
- **Analysis** - Measurements on 3D model
- **Archiving** - Digital preservation
- **Sharing** - Show finds to others without handling

### Ground Control Points with Scanniverse

**Why Use GCPs with Mobile Scanning:**

While Scanniverse creates accurate 3D shapes, it may not have precise real-world coordinates. Ground Control Points (GCPs) solve this:

**GCP Implementation:**

1. **Place Markers:**
   - Visible targets in scan area
   - Around perimeter of object
   - Multiple heights if possible
   - High-contrast patterns (checkerboard targets)

2. **Survey GCP Positions:**
   - GPS coordinates (high-accuracy GPS unit)
   - Or total station
   - Or RTK/PPK GPS
   - Record precise X, Y, Z coordinates

3. **Capture in Scan:**
   - Include GCPs in Scanniverse scan
   - Clearly visible in multiple views
   - Don't move targets during scan

4. **Post-Processing:**
   - Export model from Scanniverse (OBJ format)
   - Import to software like Metashape, CloudCompare, or ArcGIS Pro
   - Identify GCPs in model
   - Enter surveyed coordinates
   - Software georectifies model

**Result:**
- 3D model in correct location
- Accurate real-world coordinates
- Proper scale and orientation
- Integration with GIS data
- Survey-grade positioning

**Example Application:**
- Archaeological trench with measured GCPs
- Creates georeferenced 3D trench model
- Integrates with site GIS
- Accurate spatial analysis
- Professional documentation standards
- Centimeter-level accuracy possible

---

## Processing Workflows Comparison

### Metashape Processing

**Agisoft Metashape Overview:**
- Professional photogrammetry software
- Desktop application (runs on local computer)
- Full manual control over processing
- Advanced features and settings
- Industry standard for many applications

**Metashape Workflow:**

1. **Import Photos:**
   - Load all 1,269 images
   - Verify GPS data (if available)
   - Organize by camera/flight

2. **Align Photos:**
   - Feature detection and matching
   - Camera position estimation
   - Creates sparse point cloud
   - Moderate processing time (30-90 min for 1,269 images)

3. **Dense Point Cloud:**
   - Detailed 3D reconstruction
   - Quality settings: Low/Medium/High/Ultra
   - Most time-consuming step
   - High quality = 4-12 hours for 1,269 images

4. **Mesh Generation:**
   - Convert point cloud to surface
   - Triangle count settings
   - Texture size options
   - 1-3 hours

5. **Texture Mapping:**
   - Apply photo imagery to mesh
   - Blending modes
   - Texture atlas creation
   - 30-90 minutes

6. **Export Products:**
   - Orthomosaic
   - DSM/DTM
   - 3D models (OBJ, FBX, etc.)
   - Point clouds (LAS, LAZ)

**Advantages:**
- **Full control** - Adjust every parameter
- **Advanced features** - Python scripting, batch processing
- **Quality options** - Choose speed vs quality tradeoff
- **Local processing** - No cloud upload required (good for remote Alaska)
- **Format support** - Many export formats
- **No internet needed** - Process offline

**Disadvantages:**
- **Hardware requirements** - Needs powerful computer
- **Processing time** - Can be very long (8-24 hours for 1,269 images)
- **Technical knowledge** - Steeper learning curve
- **Cost** - Software license required (~$3,500)
- **Manual workflow** - More steps to manage

### ArcGIS Site Scan Processing

**Site Scan Overview:**
- Cloud-based processing
- Automated workflow
- Integrated with ArcGIS Online
- Simplified interface
- Optimized for GIS workflows

**Site Scan Workflow:**

1. **Upload Images:**
   - Web interface upload (requires good internet)
   - Or Skydio Cloud sync
   - Automatic organization
   - 1,269 images = large upload (1-3 hours via Starlink)

2. **Configure Processing:**
   - Select output products
   - Choose quality level
   - Set coordinate system
   - Limited parameter options

3. **Cloud Processing:**
   - Automated processing
   - No local resources used
   - Email notification when complete
   - 4-8 hours typical for 1,269 images

4. **Results:**
   - Orthomosaic
   - DSM
   - Optional 3D mesh
   - Directly in ArcGIS Online

**Advantages:**
- **No hardware required** - Cloud processing
- **Automated** - Simple workflow
- **GIS integration** - Seamless ArcGIS workflow
- **No manual steps** - Set and forget
- **Accessibility** - Process from anywhere

**Disadvantages:**
- **Limited control** - Fewer parameter options
- **Internet required** - Large uploads (challenge in rural Alaska)
- **Processing time** - No control over speed
- **Cost** - Requires Site Scan license
- **Format limitations** - Fewer export options

### Comparison: Metashape vs Site Scan

| Aspect | Metashape | ArcGIS Site Scan |
|--------|-----------|------------------|
| **Processing Location** | Local computer | Cloud |
| **Hardware Requirements** | High-end computer needed | Any computer works |
| **Control** | Full manual control | Automated, limited options |
| **Quality** | Can be higher with optimal settings | Very good, less customization |
| **Processing Time** | Depends on hardware (8-24 hrs) | Fixed, 4-8 hours typical |
| **Learning Curve** | Steep | Gentle |
| **Cost** | One-time license (~$3,500) | Subscription (~$1,000/year) |
| **Outputs** | Many formats | Optimized for GIS |
| **GIS Integration** | Manual export/import | Seamless |
| **Internet Needed** | No (good for Alaska) | Yes (challenge in rural areas) |
| **Best For** | Maximum quality, custom workflows | Standard mapping, GIS projects |

### Nunalleq Museum Processing Comparison

**Processed in Both Platforms:**

**Metashape Processing:**
- Imported all 1,269 images
- High quality settings
- Manual parameter tuning
- Local processing on workstation
- Processing time: ~12 hours
- Result: Highly detailed model with 0.08" effective resolution

**Site Scan Processing:**
- Cloud upload via Starlink (2 hours upload)
- Automated processing
- Default settings
- Processing time: ~6 hours
- Result: Very good quality model, excellent for GIS integration

**Comparison Observations:**
- Visual quality very similar
- Metashape offered slightly more fine detail
- Site Scan faster total time (despite upload)
- Metashape more flexible for export formats
- Site Scan seamless ArcGIS Online integration
- Both suitable for project needs
- Choice depends on workflow priorities

---

## Hardware Limitations for 3D Modeling

### Processing Hardware Requirements

**Computer Specifications Impact:**

**CPU (Processor):**
- Feature matching and alignment
- More cores = faster processing
- High clock speed beneficial
- Intel i7/i9 or AMD Ryzen 7/9 recommended
- 8+ cores optimal for 1,269 images

**RAM (Memory):**
- Critical for large datasets
- **Minimum:** 16 GB (may struggle)
- **Recommended:** 32 GB
- **Optimal:** 64 GB+ for 1,269 images
- Insufficient RAM = slow or failed processing
- 1,269 images at high quality = 40-64 GB RAM recommended

**GPU (Graphics Card):**
- Dense point cloud generation
- Depth map calculation
- **NVIDIA GPUs recommended** (CUDA support)
- More VRAM = larger projects
- Can reduce processing time by 50-70%
- Examples: RTX 3060 (12GB), RTX 3080, RTX 4080, A5000
- 8+ GB VRAM recommended for 1,269 images

**Storage:**
- Project files very large
- 1,269 images = ~10-15 GB raw
- Point clouds = 2-8 GB
- Meshes = 1-3 GB
- **SSD highly recommended** for processing
- NVMe SSD fastest
- Hard drive for archive storage
- Total project size: 20-40 GB

### Processing Time Considerations

**Factors Affecting Processing Time:**

1. **Image Count:**
   - 100 images = 1-2 hours
   - 500 images = 4-8 hours
   - 1,000+ images = 12-24 hours (or more)
   - 1,269 images = 12-20 hours typical

2. **Resolution:**
   - Higher megapixel = longer processing
   - 12 MP vs 20 MP = significant difference
   - 1/4 resolution (X10 setting) = faster than full resolution

3. **Quality Settings:**
   - Low: Fastest, lowest quality
   - Medium: Good balance (4-8 hours)
   - High: Best quality, longest time (12-20 hours)
   - Ultra: Diminishing returns, very slow (24+ hours)

4. **Hardware:**
   - Fast computer (64GB RAM, RTX 3080) = 8-12 hours
   - Moderate computer (32GB RAM, GTX 1660) = 16-24 hours
   - Slow computer (16GB RAM, integrated GPU) = 36+ hours or fail
   - Insufficient RAM = may not complete

5. **Coverage Complexity:**
   - Simple flat area = faster
   - Complex 3D structure (like museum) = slower
   - More overlap = more matching = slower
   - Three-axis scanning = more processing

**Realistic Expectations:**

Nunalleq Museum scan (1,269 images, 0.08" GSD):
- **Laptop (16GB RAM, integrated GPU):** Will likely fail or take 48+ hours
- **Workstation (32GB RAM, RTX 3060):** 12-16 hours
- **High-end (64GB RAM, RTX 3080):** 8-12 hours
- **Cloud (Site Scan):** 4-8 hours (independent of local hardware)

### Mobile Device Limitations (Scanniverse)

**iPhone/iPad LiDAR Capabilities:**

**Strengths:**
- Immediate 3D capture
- No processing wait
- Portable and accessible
- Good for small objects

**Limitations:**
- **Range:** ~5 meters maximum
- **Resolution:** Lower than photogrammetry (typically 5-10mm)
- **Detail:** Less fine detail than DSLR photogrammetry
- **Size:** Not suitable for large structures (use drone instead)
- **Outdoor:** Can struggle in bright sunlight
- **Accuracy:** Lower absolute accuracy (1-5cm without GCPs)
- **Texture quality:** Lower than camera photos

**Best Applications:**
- Objects < 2 meters
- Indoor scanning
- Quick documentation
- Where drone can't access
- Archaeological trenches
- Artifacts

**Comparison to Drone:**
- Drone: 0.08" GSD possible (2mm)
- Scanniverse: ~5-10mm resolution typical
- Drone: Better for buildings
- Scanniverse: Better for small objects

---

## 3D Model Outputs and Applications

### Deliverable Products

**From 3D Scanning Projects:**

1. **Point Cloud:**
   - Raw 3D data
   - Millions of points (10-50 million for Nunalleq scan)
   - Color information from photos
   - Formats: LAS, LAZ, E57, PLY

2. **3D Mesh:**
   - Continuous surface
   - Textured with photo imagery
   - Formats: OBJ, FBX, DAE, PLY, GLTF
   - Suitable for visualization

3. **Orthomosaic:**
   - 2D map view (if creating top-down view)
   - Top-down perspective
   - Georeferenced
   - GeoTIFF format
   - 0.08" resolution possible

4. **Digital Surface Model (DSM):**
   - Elevation raster
   - Includes buildings, trees, features
   - Height values in meters or feet
   - GeoTIFF format

5. **Digital Terrain Model (DTM):**
   - Ground surface only
   - Vegetation/buildings removed (requires classification)
   - Bare earth elevation
   - GeoTIFF format

### Viewing and Sharing 3D Models

**Platforms for Sharing:**

1. **ArcGIS Online:**
   - Publish 3D scene layers
   - Web Scene viewer
   - Share via link
   - Integration with other GIS data
   - Interactive measurement tools

2. **YouTube (3D Video):**
   - Render model as video
   - Flythrough animation
   - Easy sharing with community
   - No special software needed
   - **Example:** [Nunalleq Museum 3D Model](https://youtu.be/0wXSd0GDpUo?si=ytVeTywAJKatOsaN)

3. **Sketchfab:**
   - Online 3D viewer
   - Interactive rotation/zoom
   - Embed in websites
   - Free and paid tiers
   - Annotations possible

4. **Potree Viewer:**
   - Open-source point cloud viewer
   - Web-based
   - High performance for large datasets
   - Self-hosted option

### Applications for 3D Models

**Community Applications:**

**Cultural Heritage:**
- Document traditional buildings (like Nunalleq Museum)
- Archaeological site recording
- Artifact preservation
- Virtual museum exhibits
- Educational resources
- Historical documentation before changes

**Infrastructure:**
- Building condition assessment
- Construction planning
- As-built documentation
- Renovation planning
- Facility management
- Damage assessment

**Monitoring:**
- Erosion tracking (3D change detection)
- Building deterioration over time
- Construction progress
- Facility management
- Weathering/aging documentation

**Planning:**
- Visualization for proposals
- Community engagement
- Design review
- Impact assessment
- Site planning

**Education:**
- Virtual field trips
- Cultural education for youth
- STEM learning
- Historical documentation
- Distance learning resources

---

## Review Questions

1. What is structure from motion and how does it create 3D models?
2. Why is 80/80 image overlap critical for 3D reconstruction?
3. What are the limitations of Skydio obstacle avoidance for 3D scanning?
4. What safety protocols are needed when scanning near roads and in active areas?
5. How many images were captured for the Nunalleq Museum scan and why so many?
6. How do you identify and address gaps in point cloud coverage?
7. When should you use Scanniverse instead of drone photogrammetry?
8. Why are ground control points important for mobile scanning accuracy?
9. What are the main differences between Metashape and Site Scan processing?
10. What hardware specifications are important for processing 1,269 images?
11. What was the effective GSD (resolution) of the Nunalleq Museum scan?
12. What are the three scan pass types (X, Y, Z axes) and why are they all used?

---

## Practical Exercise

**3D Scanning Analysis:**

**Scenario:** You need to create a 3D model of a community building

**Tasks:**

1. **Planning (20 min):**
   - Review Nunalleq Museum capture report
   - Identify environmental hazards for your building
   - Plan safety protocols
   - Determine appropriate scan settings
   - Estimate image count and flight time

2. **Settings Configuration (15 min):**
   - Choose distance to surface
   - Select overlap percentages
   - Configure scan volume (ceiling, floor, walls, inside)
   - Decide on scan pass types (X, Y, Z)
   - Set visual geofence parameters

3. **Gap Analysis Exercise (20 min):**
   - Review screenshots of point cloud gaps (provided)
   - Identify types of gaps
   - Propose solutions for each gap
   - Plan manual supplementation strategy
   - Document findings

4. **Workflow Comparison (15 min):**
   - Compare Metashape vs Site Scan for 1,269 images
   - Consider hardware available
   - Consider internet availability
   - Choose appropriate workflow
   - Justify decision with pros/cons

5. **Small Object Identification (10 min):**
   - List 5 features that would be better scanned with Scanniverse
   - Explain why drone not appropriate for each
   - Describe GCP strategy for accuracy
   - Estimate Scanniverse scan time

**Deliverable:**
- Planning document with safety protocols
- Scan settings table
- Gap analysis report with solutions
- Workflow selection justification
- Small object scanning plan

---

## Key Takeaways

- **Structure from motion** creates 3D models from overlapping 2D images by matching features
- **80%/80% overlap essential** for quality 3D reconstruction and complete coverage
- **1,269 images captured** Nunalleq Museum at 0.08" effective GSD - extremely high resolution
- **Obstacle avoidance doesn't detect moving objects** - requires road closure and crowd management
- **Safety protocols critical** in active environments (roads, people, animals)
- **Three-axis scanning** (X, Y, Z passes) ensures comprehensive coverage from all angles
- **Point cloud review reveals gaps** that need manual supplementation with additional photos
- **Scanniverse complements drone scanning** for small objects (< 2m) and indoor features
- **GCPs enable survey-grade positioning** (centimeter-level) even with mobile scanning
- **Metashape offers control, Site Scan offers simplicity** - choice depends on project needs
- **Hardware significantly impacts processing** - 1,269 images needs 32-64GB RAM and good GPU
- **Processing time: 8-24 hours locally** depending on hardware, or 4-8 hours in cloud
- **3D models enable powerful visualization** and sharing via YouTube, ArcGIS Online, Sketchfab
- **Multiple flights possible** - battery swap enabled 2 flights totaling 27 minutes

---

## Resources

### Video Tutorial

**Nunalleq Museum 3D Model - Final Result:**

[![Nunalleq Museum 3D Model](https://img.youtube.com/vi/0wXSd0GDpUo/maxresdefault.jpg)](https://youtu.be/0wXSd0GDpUo?si=ytVeTywAJKatOsaN)

*Click the image above to watch the 3D model flythrough on YouTube*

---

### Documentation and Guides

- [📄 Nunalleq Museum Capture Report](../resources/Capture_Report.html) - Complete scan settings and statistics
- [Agisoft Metashape Tutorials](https://agisoft.com/tutorials) - Learn advanced processing techniques
- [Scanniverse User Guide](https://scanniverse.com/learn) - Mobile 3D scanning guide
- [ArcGIS Site Scan Documentation](https://doc.arcgis.com/en/site-scan/) - Cloud processing workflow
- [Skydio 3D Scan Documentation](https://support.skydio.com/) - Official X10 3DC scan guide

---

## Next Steps

After completing this lesson:

- ✨ **Practice:** Activity 7 - 3D Scanning Mission
- 📚 **Explore:** Advanced Metashape techniques
- 🎯 **Apply:** Scan cultural sites or infrastructure in your community
- 💬 **Share:** Create 3D models for community viewing on YouTube
- 🔄 **Monitor:** Repeat scans for change detection over time
- 📊 **Analyze:** Compare models processed in Metashape vs Site Scan

---

**Lesson Version:** 1.0
**Created:** December 8, 2025
**Field Scan Date:** November 24, 2025
**Training Discussion:** December 4-5, 2024
**Location:** Quinhagak, Alaska
