# Lesson 10: Data Upload Workflows - Site Scan and Skydio Cloud

**Duration:** 90 minutes
**Prerequisites:** Lesson 9 - Mapping Missions and Data Collection
**Training Date Reference:** November 7, 2025

---

## Lesson Overview

This lesson covers two methods for uploading drone imagery data for processing: transferring images via SD card to ESRI Site Scan, and direct upload to Skydio Cloud using network connectivity. You'll learn when to use each method and how to execute both workflows successfully.

---

## Learning Objectives

By the end of this lesson, you will be able to:

1. Safely remove SD cards from the Skydio X10
2. Transfer imagery data to ESRI Site Scan
3. Connect the X10 to internet via USB-C to Ethernet adapter
4. Upload data directly to Skydio Cloud
5. Understand advantages and limitations of each method
6. Troubleshoot common upload issues
7. Manage large datasets efficiently
8. Verify successful data transfers

---

## Understanding Processing Platforms

### ESRI Site Scan

**What is Site Scan?**
- ESRI's drone-to-GIS platform
- Processes imagery into orthomosaics, 3D models, and elevation data
- Integrates directly with ArcGIS Online
- Cloud-based processing (no local computer power needed)

**Key Features:**
- Automated photogrammetry processing
- Generates orthomosaics
- Creates Digital Surface Models (DSM)
- Produces 3D point clouds and meshes
- Direct publishing to ArcGIS Online
- Project and mission management
- Measurement and analysis tools

**Best For:**
- GIS integration workflows
- Publishing to ArcGIS Online
- Sharing with team via ESRI ecosystem
- Analysis in ArcGIS Pro

### Skydio Cloud

**What is Skydio Cloud?**
- Skydio's cloud platform for drone data
- Stores flight logs, imagery, and metadata
- Processing capabilities
- Fleet management features
- Collaboration tools

**Key Features:**
- Automatic flight log backup
- Image storage and organization
- 3D model creation
- Thermal imagery management
- Flight analytics
- Team collaboration
- Skydio ecosystem integration

**Best For:**
- Drone fleet management
- Long-term data archival
- Thermal data workflows
- Skydio-specific features
- Multiple pilot coordination

---

## Method 1: SD Card Transfer to ESRI Site Scan

### Equipment Needed

- Skydio X10 (powered off after flight)
- Computer with SD card reader (or USB adapter)
- Internet connection
- ESRI Site Scan account/license

### Step-by-Step Procedure

#### Step 1: Prepare the Drone

**After Landing:**
1. Complete post-flight procedures
2. Disarm motors
3. **Wait 30 seconds** for data write completion
4. Verify scan saved (check flight logs on controller)
5. Power off controller
6. Power off drone

**Important:** Allow adequate time for all data to write to SD card before removal.

#### Step 2: Remove SD Card

**SD Card Location:**
- SD card slot location on X10: [reference manual]
- Typically under battery or side panel

**Removal Procedure:**
1. Ensure drone is powered off
2. Locate SD card slot
3. Press card gently to release (push-push mechanism)
4. Card will pop out slightly
5. Remove card carefully
6. Store drone safely

**SD Card Handling:**
- Hold card by edges (avoid touching contacts)
- Don't force card removal
- Keep card in protective case when not in use
- Label cards with date/mission for organization

#### Step 3: Insert SD Card into Computer

**Connection:**
1. Insert SD card into computer's card reader
2. Or use USB SD card adapter
3. Wait for computer to recognize card
4. Card should mount/appear as drive

**What You'll See:**
- DCIM folder with images
- Flight log files
- Metadata files
- Possibly thermal imagery (if captured)

**Data Organization:**
```
SD Card/
├── DCIM/
│   └── 100MEDIA/
│       ├── DJI_0001.JPG
│       ├── DJI_0002.JPG
│       └── ... (~1000 images for grocery store mission)
├── FlightLogs/
└── [other metadata folders]
```

#### Step 4: Upload to ESRI Site Scan

**Access Site Scan:**
1. Open web browser
2. Navigate to [https://sitescan.arcgis.com](https://sitescan.arcgis.com)
3. Sign in with ArcGIS Online account
4. Select your organization

**Create New Project:**
1. Click "New Project"
2. Name project: "2025-11-07 Quinhagak Grocery Store"
3. Add description and tags
4. Set privacy/sharing settings
5. Click "Create"

**Upload Images:**
1. Within project, click "New Flight"
2. Name flight: "Grocery Store 200ft 80-80 overlap"
3. Click "Upload Images"
4. Navigate to SD card DCIM folder
5. **Select all images** (~1000 images)
6. Click "Upload"

**Upload Progress:**
- Progress bar will show
- Large datasets take time (8-12 GB = 30-60 minutes depending on connection)
- **Do not close browser or remove SD card during upload**
- Site Scan will verify image quality during upload

**Verify Upload:**
1. Check that all images uploaded (count: ~1000)
2. Review upload report for errors
3. Check coverage map (Site Scan shows image locations)
4. Verify no corrupt images

#### Step 5: SD Card Management

**After Successful Upload:**
1. Safely eject SD card from computer
2. **Backup data locally** before formatting (optional but recommended)
3. Return SD card to drone or storage case
4. Label or log which card contains which data

**Before Next Flight:**
- Verify adequate space on SD card
- Consider formatting if backed up elsewhere
- Check card for errors (format periodically)

---

## Method 2: Direct Upload via Network Connection

### Equipment Needed

- Skydio X10 (powered on after flight)
- Belkin USB-C to Ethernet adapter
- Ethernet cable
- Starlink unit (or other internet source with Ethernet port)
- Skydio Cloud account

### Understanding the Setup

**Why Use Network Upload?**
- No need to remove SD card
- Faster for large datasets (if good connection)
- Direct to Skydio Cloud
- Can upload while in field
- Preserves all metadata automatically

**Connection Chain:**
```
Skydio X10 → USB-C to Ethernet adapter → Ethernet cable → Starlink → Internet → Skydio Cloud
```

**Key Equipment:**
- **Belkin USB-C to Ethernet adapter:** Converts X10's USB-C port to wired Ethernet
- **Starlink:** Provides high-speed internet in remote Alaska locations
- **Ethernet cable:** Standard Cat5e or Cat6

### Step-by-Step Procedure

#### Step 1: Prepare Equipment

**After Flight:**
1. Land drone
2. Disarm motors
3. **Keep drone powered on** (important for network upload)
4. Verify scan saved properly
5. Place drone in stable location (table, case)

**Network Setup:**
1. Ensure Starlink unit is powered on and connected
2. Verify Starlink has internet connectivity
3. Have Belkin USB-C to Ethernet adapter ready
4. Have Ethernet cable connected to Starlink

**Important:** Drone must remain powered on for network connection. Monitor battery level and use AC power if available for X10 (if supported).

#### Step 2: Connect Drone to Network

**Physical Connection:**
1. Locate USB-C port on Skydio X10
2. Connect Belkin USB-C to Ethernet adapter to drone port
3. Ensure adapter seated firmly
4. Connect Ethernet cable to adapter
5. Other end of Ethernet cable connects to Starlink

**Verify Connection:**
1. Check drone status lights
2. X10 should indicate network connection
3. May take 30-60 seconds to establish
4. Verify internet connectivity detected

**Troubleshooting Connection:**
- Adapter must be USB-C to Ethernet (not just USB)
- Ensure Ethernet cable is good quality
- Check Starlink internet is working
- Try disconnecting and reconnecting
- Restart drone if necessary

#### Step 3: Access Skydio Cloud

**On Computer or Tablet:**
1. Open web browser
2. Navigate to [https://cloud.skydio.com](https://cloud.skydio.com)
3. Sign in with Skydio account
4. Access your organization/workspace

**Verify Drone Connected:**
1. Drone should appear in device list
2. Check "Online" status
3. View available flights/scans

#### Step 4: Initiate Upload

**Select Flight to Upload:**
1. Navigate to Flights section
2. Find the grocery store mapping flight
3. Select flight
4. Click "Upload to Cloud"

**Upload Options:**
- Full resolution images
- Flight logs
- Metadata
- Thermal data (if applicable)

**Configure Upload:**
1. Verify all data selected
2. Choose processing options (if available)
3. Add tags/notes
4. Click "Start Upload"

**Monitor Upload:**
- Progress indicator will show
- Large datasets (1000 images) take time:
  - With Starlink: 20-40 minutes typical
  - Speed depends on Starlink performance and weather
- **Keep drone connected and powered**
- **Do not disconnect during upload**

**Upload Completion:**
1. Verify upload finished (100%)
2. Check for error messages
3. Confirm all images uploaded
4. Note upload time for future planning

#### Step 5: Disconnect and Store

**After Successful Upload:**
1. Safely disconnect from Skydio Cloud interface
2. Remove Ethernet cable from adapter
3. Remove USB-C adapter from drone
4. Power off drone (if not already done)
5. Store equipment

**Data Verification:**
1. In Skydio Cloud, verify flight data accessible
2. Check image count matches expectations (~1000)
3. Review flight logs uploaded
4. Confirm processing options set correctly

---

## Comparison: When to Use Each Method

### ESRI Site Scan (SD Card Transfer)

**Advantages:**
✅ Direct integration with ArcGIS Online
✅ ESRI ecosystem compatibility
✅ Excellent orthomosaic processing
✅ Publish directly to ArcGIS
✅ No need to keep drone powered on
✅ Can upload from any computer

**Disadvantages:**
❌ Requires SD card removal
❌ Physical transfer needed
❌ SD card reader required
❌ Manual file handling

**Best For:**
- GIS workflows
- ArcGIS Online publishing
- When drone needed immediately for next flight
- Limited field internet
- ESRI-centric organizations

### Skydio Cloud (Direct Network)

**Advantages:**
✅ No SD card removal needed
✅ Can upload in field
✅ Automatic metadata preservation
✅ Fleet management features
✅ Faster with good connection

**Disadvantages:**
❌ Requires network adapter
❌ Drone must stay powered
❌ Needs reliable internet (Starlink)
❌ Requires additional equipment
❌ Less direct ArcGIS integration

**Best For:**
- Field operations with Starlink
- Quick data backup
- Thermal imagery workflows
- Fleet/multi-drone operations
- Skydio-centric workflows

---

## Alaska-Specific Considerations

### Starlink Performance

**Advantages in Remote Alaska:**
- High-speed internet in remote locations
- No need for cellular coverage
- Reliable in clear weather
- Supports large data uploads

**Considerations:**
- Heavy snow/ice can affect signal
- Wind may affect dish alignment
- Power requirements (battery or generator)
- Setup time needed

### Cold Weather Data Management

**SD Card Handling:**
- SD cards can become brittle in extreme cold
- Warm cards slowly before handling
- Condensation risk when bringing cold card to warm computer
- Keep spare cards warm

**Network Equipment:**
- USB-C adapters may be stiff in cold
- Ethernet cables less flexible in cold
- Starlink requires power (generator or battery)
- Keep equipment protected from snow/ice

---

## Data Backup Best Practices

### Redundancy Strategy

**Recommended Approach:**
1. **Primary:** Upload to Site Scan or Skydio Cloud
2. **Secondary:** Keep images on SD card until processing confirmed
3. **Tertiary:** Copy to external hard drive or backup location

**Why Multiple Copies:**
- Upload failures can occur
- Processing may reveal image issues
- Original data invaluable
- Re-flying missions is expensive

### Backup Workflow

**After Each Mission:**
1. Upload to primary platform (Site Scan or Skydio Cloud)
2. Verify upload successful
3. Copy raw images to external drive
4. Label with mission date and location
5. Only format SD card after confirmed backups

**Long-Term Storage:**
- External hard drives
- Network Attached Storage (NAS)
- Cloud backup services
- Multiple locations (if critical data)

---

## Troubleshooting Common Issues

### SD Card Upload Problems

**Issue:** Images won't upload or upload fails
**Solutions:**
- Check internet connection
- Verify file formats correct
- Try smaller batches
- Check for corrupt images
- Restart browser
- Clear browser cache

**Issue:** Some images skipped
**Solutions:**
- Review upload log
- Check image quality
- Verify GPS data in images
- Re-upload missing images

### Network Connection Problems

**Issue:** Drone won't connect to network
**Solutions:**
- Verify adapter compatibility
- Check Ethernet cable
- Restart drone
- Check Starlink connectivity
- Verify cable connections secure

**Issue:** Upload very slow
**Solutions:**
- Check Starlink signal strength
- Weather affecting Starlink?
- Try different time of day
- Consider SD card method instead

---

## Review Questions

1. What are the two methods for uploading drone imagery data?
2. How long should you wait after landing before removing the SD card?
3. What equipment is needed to connect the X10 to Starlink?
4. What is the advantage of using ESRI Site Scan for uploads?
5. Why must the drone remain powered on for network uploads?
6. How many images were uploaded from the grocery store mission?
7. What is a recommended backup strategy for drone data?
8. What Alaska-specific factors affect network uploads via Starlink?

---

## Practical Exercise

**Data Upload Comparison:**

**Objective:** Practice both upload methods with sample data

**Part 1: SD Card Upload (30 minutes)**
1. Remove SD card from drone (training scenario)
2. Insert into computer
3. Navigate file structure
4. Upload subset of images to Site Scan
5. Verify upload success
6. Document time required

**Part 2: Network Upload Setup (20 minutes)**
1. Connect USB-C to Ethernet adapter to drone
2. Connect to Starlink
3. Verify network connection
4. Access Skydio Cloud
5. Initiate upload (can cancel for practice)
6. Document setup process

**Deliverable:** Comparison chart of both methods with pros/cons based on your experience

---

## Key Takeaways

- **Two upload methods:** SD card to Site Scan, or direct network to Skydio Cloud
- **SD card method:** Requires removal but integrates with ArcGIS easily
- **Network method:** Requires USB-C to Ethernet adapter and internet (Starlink)
- **Wait 30 seconds after landing** before SD card removal
- **Large datasets (1000 images) take time** - plan accordingly
- **Starlink enables field uploads** in remote Alaska
- **Backup strategy is critical** - multiple copies recommended
- **Choose method based on workflow needs** and available equipment

---

## Next Lesson

[Lesson 11: Orthomosaic Processing and ArcGIS Online Integration](./lesson11_orthomosaic_processing.md)

You'll learn how processed orthomosaics are created and how to integrate them into ArcGIS Online for analysis and sharing.
