# Instructor Notes: Module 4 - Spatial Analysis in ArcGIS Pro

**Instructor:** Sean Gleason
**Training Location:** Quinhagak, Alaska (Red Building training room)
**Training Date:** October 2025
**Students:** Yup'ik community members
**Module Duration:** 2-3 days (approximately 12-16 hours total)

---

## Overview

This module is the heart of the ArcGIS Pro training. It transitions students from web-based GIS (AGOL) to desktop GIS, introducing powerful spatial analysis tools while maintaining focus on real-world Quinhagak applications.

**Critical Success Factors:**
1. The balloon activity makes projections concrete and memorable
2. Using actual Quinhagak data maintains relevance and engagement
3. The rusting rivers activity connects GIS to urgent environmental issues
4. Balancing technical skills with traditional knowledge creates meaningful learning
5. Patience with software learning curve - ArcGIS Pro is complex!

---

## Module Philosophy

### Learning Approach

**Hands-On First:**
- Physical balloon activity before computer work
- Touch and feel the distortion problem
- Connect abstract concepts to tangible experience

**Real Data, Real Questions:**
- Use actual Quinhagak parcels, not sample data
- Work with georeferenced Quinhagak maps they created earlier
- Address actual community planning questions
- Connect to environmental issues (rusting rivers)

**Build Complexity Gradually:**
- Start with simple (change coordinate system)
- Progress to intermediate (create features, basic buffers)
- Advance to complex (multi-step spatial analysis)
- Allow mastery at each level before advancing

**Honor Multiple Ways of Knowing:**
- GIS analysis AND traditional knowledge
- Satellite imagery AND elder observations
- Technical measurements AND lived experience
- Western science AND Indigenous knowledge systems

---

## Day-by-Day Breakdown

### Day 1: Foundations (6-7 hours)

**Morning (3-4 hours):**
- **9:00-10:30:** Balloon activity + projections lecture (Lesson 1)
  - Budget 90 minutes - this is critical foundation
  - Allow time for discussion and questions
  - Show EPSG.io website live
  - Demonstrate projection changes in ArcGIS Pro

- **10:30-10:45:** Break

- **10:45-12:00:** Adding content from AGOL (Lesson 2)
  - Expect frustrations with sharing permissions
  - Have backup plan if internet is slow
  - Pre-download critical layers if possible
  - Troubleshoot sign-in issues patiently

**Lunch: 12:00-1:00**

**Afternoon (3-4 hours):**
- **1:00-2:00:** Directory structure and geodatabases (Lesson 3)
  - Emphasize organization from the start
  - Create standard folder structure all students use
  - Explain .gdb advantages over shapefiles clearly
  - Practice creating feature classes together

- **2:00-2:15:** Break

- **2:15-3:30:** Symbology and styling parcels (Lesson 4)
  - Use Quinhagak Parcels data
  - Explore color palette website together
  - Practice transparency adjustments
  - Save layer files for reuse

- **3:30-4:00:** Wrap-up, questions, save work

### Day 2: Creating and Analyzing Features (6-7 hours)

**Morning (3-4 hours):**
- **9:00-9:15:** Review Day 1 concepts

- **9:15-10:45:** Creating features - tracing activity (Lesson 5)
  - Load georeferenced Quinhagak map
  - Demonstrate creating point, line, polygon feature classes
  - Practice tracing old FAA building together
  - Students trace old sewer lagoon and housing plots independently
  - Emphasize saving edits frequently!

- **10:45-11:00:** Break

- **11:00-12:00:** Buffer analysis (Lesson 6)
  - Create buffers around traced features
  - Demonstrate dissolve function
  - Practice pairwise intersect
  - Discuss real-world applications

**Lunch: 12:00-1:00**

**Afternoon (3-4 hours):**
- **1:00-3:00:** Rusting Rivers Activity (Activity 7)
  - Introduction to phenomenon (20 min)
  - Read articles together, discuss
  - Load satellite imagery
  - Identify orange/rust streams as group first
  - Create feature classes together
  - Begin individual digitizing

- **3:00-3:15:** Break

- **3:15-4:00:** Continue rusting rivers work
  - Buffer analysis around affected streams
  - Begin thinking about subsistence impacts
  - Start planning maps

### Day 3: Advanced Analysis and Synthesis (4-5 hours)

**Morning (3-4 hours):**
- **9:00-10:00:** Complete rusting rivers analysis
  - Finish digitizing
  - Complete spatial analysis
  - Begin creating maps

- **10:00-10:15:** Break

- **10:15-12:00:** Advanced spatial analysis tools (Lesson 7)
  - Demonstrate: Merge, Clip, Erase, Spatial Join
  - Explain when to use each tool
  - Practice scenarios with Quinhagak data
  - Troubleshoot common errors together

**Lunch: 12:00-1:00**

**Afternoon (2-3 hours):**
- **1:00-2:00:** Raster data, graphics, exporting (Lessons 8-10)
  - Adjust imagery HSV and contrast
  - Add graphics and text to maps
  - Practice different export formats
  - Upload to ArcGIS Online

- **2:00-3:00:** Final project work time
  - Complete rusting rivers maps
  - Finalize documentation
  - Prepare brief presentations

- **3:00-4:00:** Student presentations and wrap-up
  - Each student presents one finding
  - Discuss next steps and applications
  - Module assessment

---

## The Balloon Activity: Critical Teaching Notes

### Why This Matters

This physical activity is **THE KEY** to students understanding projections. Without it, coordinate systems remain abstract and confusing. With it, students immediately grasp why projections exist and why they matter.

### Preparation

**Materials per group (2-3 students):**
- 1 inflated balloon (round shape, about 9-12 inches diameter)
- 1 permanent marker (fine point, dark color)
- Paper and pencil for notes
- Scissors for popping
- Towel or mat (balloon pieces may fly)

**Setup:**
- Arrange students in small groups
- Clear table space for each group
- Have extra balloons (some will pop early)
- Consider doing one demonstration balloon first

### Step-by-Step Facilitation

**Step 1: Introduction (5 min)**
- "Today we're going to understand why all maps lie a little bit"
- "This balloon represents Earth - a sphere"
- "We're going to try to make a flat map of it"

**Step 2: Drawing Alaska (10 min)**
- Show reference image of Alaska
- Guide groups to draw rough Alaska outline on balloon
- Add 5-6 Yup'ik village points:
  - Quinhagak (home!)
  - Bethel
  - Nome
  - Kotzebue
  - Barrow/Utqiaġvik
  - Optional: Anchorage

**Teaching tip:** Don't worry about perfect accuracy. Rough shapes are fine.

**Step 3: Observation on Sphere (5 min)**
- "Look at your Alaska on the curved surface"
- "Notice the distances between villages"
- "See how Alaska's shape looks"
- Optional: Measure distances with string along balloon surface

**Step 4: The Big Moment - Popping (5 min)**
- Build anticipation: "Now we're going to try to make this into a flat map"
- "First, let's pop it and see what happens"
- Safety: "Stay seated, balloon pieces may fly"
- Pop balloons (or let students do it)
- **Watch their reactions!**

**Step 5: Attempting to Flatten (10 min)**
- "Now try to lay it completely flat on the table"
- Let students struggle with this
- **Key realization:** "Can you do it without tearing, stretching, or folding?"
- **Answer:** NO!

**Observations to highlight:**
- Some areas stretched (especially edges)
- Some areas compressed
- Material tears if forced completely flat
- Distances changed
- Village relationships distorted
- Alaska shape warped

**Step 6: Discussion (15 min)**

**Essential questions:**
1. "What happened when you tried to flatten the balloon?"
   - Expected: "It stretched!" "It tore!" "Can't make it flat!"

2. "Why couldn't you make it perfectly flat?"
   - Guide to: "Because it's a curved surface being forced to be flat"

3. "Is this any different than making a map of Earth?"
   - **AH-HA:** "No! Same problem!"

4. "If we can't avoid distortion, what choices do we have?"
   - Introduce: "We can choose WHAT to distort"
   - Some projections keep shapes accurate (but areas wrong)
   - Some keep areas accurate (but shapes wrong)
   - Some keep distances accurate (but only in certain directions)

**Step 7: Connect to GIS (10 min)**
- "This is why we have different coordinate systems"
- "Each one is a different way to flatten the Earth"
- "Like different ways to cut and flatten your balloon"
- "Alaska Department of Transportation uses State Plane zones - 10 different 'cuts' for Alaska"
- "Your GPS uses WGS84 - one 'cut' for the whole world"

### Common Student Reactions

**"Oh! That's why maps look different!"**
- Perfect! They get it.
- Reinforce: Yes, different projections = different ways to flatten

**"So there's no perfect map?"**
- Exactly right!
- Emphasize: All maps involve compromise
- We choose projection based on what we need (area? shape? distance?)

**"Does this mean GPS coordinates are wrong?"**
- No! GPS coordinates are correct for the 3D Earth
- But when we show them on a 2D map, we have to project them
- Distortion happens in the projection, not the GPS measurement

### Connecting to ArcGIS Pro Demo

**Immediately after balloon activity:**

1. **Open ArcGIS Pro**
   - "Let's see this in the software"

2. **Add Alaska basemap**
   - "Here's Alaska in Web Mercator projection"

3. **Change to WGS84**
   - Right-click Map → Properties → Coordinate Systems
   - Select WGS84
   - Click OK
   - **"Watch Alaska change shape!"**

4. **Change to Alaska State Plane**
   - Properties → Coordinate Systems
   - Alaska State Plane Zone 7
   - **"Now it looks different again!"**

5. **Discussion:**
   - "Same Earth, same Alaska, different projections"
   - "Like different ways to flatten your balloon"
   - "Which is 'right'? All of them! And none of them!"
   - "We choose based on what we need"

### Troubleshooting the Activity

**Problem:** Balloons pop before drawing complete
- **Solution:** Have extras ready, use gentler markers

**Problem:** Students can't draw Alaska shape
- **Solution:** Project reference image, or draw together

**Problem:** Students get silly/off-task
- **Solution:** Redirect to science, but allow some fun - popping is exciting!

**Problem:** Cultural sensitivity about "Alaska" vs Indigenous territories
- **Solution:** Acknowledge Alaska as Yup'ik, Inupiaq, Athabascan, Tlingit, Haida, Tsimshian lands
- Can draw traditional territories instead if preferred

### Why This Works

**Learning Theory:**
- **Kinesthetic learning** - hands-on, physical manipulation
- **Visual learning** - see the distortion happen
- **Concrete to abstract** - physical balloon → digital projections
- **Memorable** - students will remember popping balloons!
- **Active engagement** - doing, not just listening
- **Group learning** - peer discussion and discovery

**Cultural Relevance:**
- Yup'ik culture values experiential learning
- Hands-on activities respected teaching method
- Connects to traditional knowledge transmission
- Makes Western GIS concept accessible through universal experience

---

## Teaching Projections and Coordinate Systems

### Key Concepts to Emphasize

**1. Two Main Types:**

**Geographic Coordinate System (GCS):**
- Latitude and longitude
- Measures in degrees
- 3D system on Earth surface
- Example: WGS84
- Your GPS uses this!

**Projected Coordinate System (PCS):**
- X and Y coordinates
- Measures in feet or meters
- 2D system on flat map
- Example: Alaska State Plane Zone 7
- Used for accurate measurement and analysis

**Memory aid:** "GPS = Geographic = 'G'lobal positioning"

**2. WGS84 - The GPS Standard:**
- World Geodetic System 1984
- Most common GCS
- What GPS satellites broadcast
- What your phone uses
- What handheld GPS units collect
- Global coverage

**Why students need to know:**
- Field data collection will be in WGS84
- Need to recognize it
- ArcGIS Pro will transform it automatically
- But you need to know that's happening

**3. Alaska State Plane - Local Accuracy:**
- Designed for accurate measurement in Alaska
- Divided into 10 zones
- Quinhagak is in Zone 7 (EPSG:26937)
- Uses feet (or meters, depending on version)
- Optimized for minimal distortion in this region

**Why students need to know:**
- Best for local analysis
- Required for legal surveys
- Alaska DOT uses it
- What parcels data likely uses
- Most accurate for Quinhagak work

**4. "On-the-Fly" Projection:**
- ArcGIS Pro's magic trick
- Automatically transforms layers to match map
- Layers can be in different coordinate systems
- They'll still display together correctly
- Software does the math behind the scenes

**Why this is amazing:**
- GPS data in WGS84? No problem!
- Basemap in Web Mercator? No problem!
- Parcels in State Plane? No problem!
- They all work together!

**But warn students:**
- Set map coordinate system FIRST
- Know what coordinate system your data is in
- Don't assume - check!
- Document coordinate systems in metadata

### Common Misconceptions to Address

**Misconception #1:** "One coordinate system is 'right' and others are 'wrong'"
- **Truth:** Different coordinate systems for different purposes
- **Analogy:** Like using feet vs meters - both valid, different uses

**Misconception #2:** "GPS coordinates are the 'real' location"
- **Truth:** GPS gives lat/lon, which is projected to show on map
- **Clarity:** Location is real, representation on 2D map varies by projection

**Misconception #3:** "We should always use the same coordinate system"
- **Truth:** Choose based on task
- **Examples:**
  - Local analysis → State Plane
  - Global mapping → WGS84
  - Web maps → Web Mercator
  - Field collection → Whatever GPS provides (usually WGS84)

**Misconception #4:** "If layers don't line up, one must be wrong"
- **Truth:** May have wrong coordinate system assigned
- **Troubleshooting:** Check defined coordinate system vs actual coordinate system
- **Solution:** Define correct coordinate system (don't project it yet!)

### Teaching Strategies

**Use Analogies:**
- Balloon = Earth (you did this!)
- Different ways to peel an orange and lay it flat
- Different ways to unfold a cardboard box
- Map projections = different recipes, same ingredients

**Make it Local:**
- Always use Quinhagak in examples
- Show State Plane Zone 7 specifically
- Reference Alaska DOT usage
- Connect to actual community planning needs

**Show, Don't Just Tell:**
- Demonstrate every coordinate system change
- Let students see basemap transform
- Point out coordinate changes at bottom of screen
- Compare same point in different coordinate systems

**Provide Resources:**
- https://epsg.io/ - bookmark this!
- Print EPSG codes reference for Alaska zones
- Create decision tree: "Which coordinate system should I use?"

### Assessment Strategies

**Formative (during lesson):**
- Ask questions frequently
- "What coordinate system is our map in right now?"
- "Why would we choose State Plane for this?"
- Have students explain to each other

**Practical:**
- Give coordinates, ask them to identify coordinate system
- 59.76, -161.9 → WGS84 (lat/lon)
- 1847000, 460000 → State Plane feet
- Have them change map coordinate system independently

**Conceptual:**
- "Explain to someone who wasn't here: why do projections exist?"
- "When would you use WGS84 vs State Plane?"
- "What happens to GPS data when you load it into ArcGIS Pro?"

---

## Data Management: Critical Best Practices

### The Folder Structure Standard

**Establish this on Day 1:**

```
Documents/
└── ArcGIS/
    └── [ProjectName]/
        ├── [ProjectName].aprx
        ├── [ProjectName].gdb/
        ├── Data/
        │   ├── GPS/
        │   ├── Downloaded/
        │   └── External/
        ├── Maps/
        └── Documentation/
```

**Why this matters:**
- Consistency across all students
- Easy to find files later
- Prevents "where did I save that?" problems
- Professional standard
- Makes troubleshooting easier

**Enforce it:**
- Create together on Day 1
- Every project follows this structure
- Check during class
- Help students organize if they deviate

### Geodatabase vs Shapefile

**This is crucial - spend time on it:**

**Geodatabase Advantages:**
- Faster performance
- More feature types supported
- No file name limits (shapefiles have 10-character limit!)
- Can store rasters, feature datasets, networks
- Better data integrity
- Multiple editors (with proper licensing)
- Attribute table supports more field types
- Can have domains, subtypes, relationship classes

**When Shapefile Might Be Used:**
- Sharing with non-Esri software
- Some external tools require it
- Sometimes requested by agencies

**Teaching Approach:**
- Demonstrate creating both
- Show file structure differences:
  - Shapefile = 3+ files (.shp, .shx, .dbf, .prj, etc.)
  - Geodatabase = one .gdb folder containing everything
- Emphasize: "Always create new features in geodatabase"
- Create standard project geodatabase for each project

### Naming Conventions

**Establish standards:**

**Good names:**
- Quinhagak_Parcels_2024
- Historical_Buildings_Digitized
- Rusting_Rivers_Points
- FAA_Building_Buffer_100m

**Bad names:**
- data1
- NEW
- Copy_of_Copy_of_shapefile
- test

**Rules:**
- No spaces (use underscores)
- Descriptive
- Include date if relevant
- Include key details (buffer distance, source, etc.)
- Start with place name for geographic data

**Memory aid:** "Name it so your future self knows what it is"

### Saving and Backing Up

**Critical habits:**

**Save Early, Save Often:**
- ArcGIS Pro can crash
- Save project every 15-20 minutes
- Save edits when editing features
- "Save" different from "Save edits"!

**Backup Strategy:**
- Copy entire project folder weekly
- Upload to OneDrive or external drive
- Never have only one copy of important data
- Before major changes, save a copy

**Teach this first day:**
- Demonstrate saving project
- Demonstrate saving edits
- Show how to copy project folder
- Make it a habit

---

## Working with AGOL Content in ArcGIS Pro

### The Frustrations (Prepare Students)

**Public vs Private Sharing:**
- This confuses EVERYONE initially
- Private content only visible when signed in
- Organizational content may have restrictions
- Group membership affects visibility

**Common Issues:**

**Problem:** "I can't see my layers from AGOL"
- **Cause:** Not signed in to organizational account
- **Solution:** Sign in at top right, ensure correct organization

**Problem:** "Layer is there but won't add"
- **Cause:** Sharing permissions or layer type incompatibility
- **Solution:** Check sharing settings in AGOL, try different add method

**Problem:** "Download takes forever"
- **Cause:** Large raster files, slow internet
- **Solution:** Clip to smaller extent first, or work with stream service

### Teaching Strategies

**Pre-download critical layers:**
- Before class, download key Quinhagak layers
- Have backups ready
- Reduces dependency on internet
- Students can use local copies if needed

**Demonstrate multiple add methods:**
1. Add from Portal (organizational content)
2. Add from Living Atlas
3. Add by URL
4. Add data from folder (downloaded)

**Practice with each:**
- Students need to try all methods
- Understand when to use which
- Troubleshoot together

### Resolution Checking

**Important skill:**

**How to measure imagery resolution:**
1. Add imagery to map
2. Measure known feature (e.g., building)
3. Zoom in until you see pixels
4. Measure single pixel
5. Pixel size = spatial resolution

**Example:**
- Measure building you know is 50 feet wide
- Count pixels
- If 50 feet = 50 pixels, resolution is ~1 foot
- If 50 feet = 5 pixels, resolution is ~10 feet

**Why this matters:**
- Know what detail you can see
- Understand imagery limitations
- Choose appropriate imagery for task
- Don't try to digitize features smaller than resolution!

---

## Creating Features: Tracing from Georeferenced Maps

### Setup

**Ensure students have:**
- Georeferenced Quinhagak map from earlier module
- Map loaded as basemap in ArcGIS Pro
- Created geodatabase ready
- Understanding of how to create feature classes

### Starting with Points (Easiest)

**Demonstration:**
1. Create point feature class
2. Start edit session
3. Create Features pane
4. Click to add point
5. Add attributes
6. Save edits

**Common mistakes:**
- Forgetting to start edit session
- Not saving edits (losing work!)
- Clicking wrong feature class (editing wrong layer)

### Lines (Intermediate)

**Demonstrate techniques:**
- Click to add vertices
- Double-click to finish
- Use streaming (for smooth curves)
- Right-click for vertex options
- F2 to finish line

**Practice feature:**
- Roads
- Shoreline
- River courses

### Polygons (Most Complex)

**Critical skills:**
- Click vertices around perimeter
- Close polygon (return to start)
- Right-click → Finish
- Or double-click to auto-close

**Common problems:**
- Polygon doesn't close (topology error)
- Vertices in wrong places (zoom closer!)
- Accidentally creating holes
- Overlapping features

**Teaching approach:**
- Do first one together as class
- Instructor drives, students guide
- Then students try individually
- Circulate and help

### The Old FAA Building Activity

**Why this feature:**
- Clear boundary visible on georeferenced map
- Historical significance (building no longer exists)
- Good size (not too big, not too small)
- Rectangular shape (easier to trace)

**Step-by-step:**
1. Zoom to FAA building location
2. Create "Historical_Buildings" polygon feature class
3. Start edit session
4. Carefully click corners of building
5. Close polygon
6. Add attributes:
   - Name: "Old FAA Building"
   - Year: ~1970s (if known)
   - Status: "Demolished"
   - Notes: "Visible on [year] map, no longer standing"
7. Save edits

**Discussion:**
- Why document buildings that don't exist anymore?
- How can this help community planning?
- What other historical features should be preserved?

### Attribute Table Management

**Essential teaching:**

**Adding fields:**
- Right-click layer → Design → Fields
- Add new field
- Choose appropriate data type
- Set field length (for text)

**Field types to teach:**
- Text - names, descriptions
- Short Integer - counts, ratings (1-5)
- Long Integer - IDs
- Double - measurements, percentages
- Date - observation dates

**Populating attributes:**
- During editing (in Create Features pane)
- After editing (in attribute table)
- Calculate field (for bulk updates)
- Field calculator expressions

**Best practices:**
- Plan fields before creating feature class
- Use domains for standardized values (advanced)
- Required fields vs optional
- Document field meanings (metadata)

---

## Buffer Analysis: Making it Meaningful

### Why Buffers Matter

**Real-world applications for Quinhagak:**

1. **Infrastructure planning**
   - Utility line setbacks (buffer roads)
   - Building setbacks (buffer property lines)
   - Airport clear zones (buffer runway)

2. **Environmental protection**
   - Stream buffers (protect water quality)
   - Wetland buffers (regulatory requirements)
   - Contamination zones (old dump sites)

3. **Cultural resources**
   - Protection zones around archaeological sites
   - Traditional use areas
   - Sacred sites

4. **Emergency planning**
   - Evacuation distances
   - Emergency service coverage
   - Flood zones

### Teaching Buffer Concepts

**Start with physical analogy:**
- "If you walked 100 meters in every direction from this building, what area would you cover?"
- "That's a buffer!"

**Demonstrate with familiar feature:**
1. Add point for community building (e.g., school)
2. Create 100m buffer
3. "This shows everywhere within 100 meters of the school"
4. Create 500m buffer
5. "This shows service area or walking distance"

**Distance considerations:**
- Meters vs feet (check units!)
- Choose meaningful distances
  - 10m = narrow setback
  - 50m = typical stream buffer
  - 100m = moderate protection zone
  - 500m = walking distance
  - 1000m = neighborhood scale

### Multiple Buffer Distances

**Demonstrate:**
1. Select feature
2. Run buffer tool
3. Distance: 100
4. Name: Feature_Buffer_100m
5. Repeat with 200m, 500m

**Show concentric rings:**
- Multiple buffers from same feature
- Visualize graduated impact zones
- Different regulations at different distances

**Styling tip:**
- Use graduated colors
- Lighter farther out
- Transparency to see overlaps

### Dissolve Buffers

**When to use:**
- Multiple features buffered
- Overlapping buffers
- Want single combined zone

**Example:**
- Buffer all historical buildings
- Dissolve to create "historical district"
- Represents combined protection zone

**Demonstrate:**
1. Create buffers around 3+ features
2. Note overlaps
3. Analysis Tools → Dissolve
4. Input: buffer layer
5. Dissolve field: (leave blank to dissolve all)
6. Output: single combined polygon

### Pairwise Intersect

**Concept:**
- "Where do these buffers overlap?"
- Intersection = area in both

**Example:**
- 100m buffer around old FAA building
- 100m buffer around old sewer lagoon
- Intersect = area affected by both

**Teach:**
1. Create two buffer layers
2. Analysis Tools → Pairwise Intersect
3. Input: both buffer layers
4. Output: overlap zones
5. Examine attribute table (shows which buffers)

**Real application:**
- Contamination zones from multiple sources
- Cumulative impact areas
- Finding suitable locations (must be in multiple buffers)

### Common Buffer Errors

**Problem:** Buffer creates nothing
- **Cause:** Wrong units, distance too large or too small
- **Solution:** Check coordinate system units

**Problem:** Buffer looks wrong
- **Cause:** Map in geographic coordinates (degrees)
- **Solution:** Project to meters or feet before buffering

**Problem:** Dissolve doesn't work
- **Cause:** Gaps between features
- **Solution:** Check dissolve settings, may need larger buffer

---

## The Rusting Rivers Activity: Handling Sensitive Topics

### Emotional Context

**This activity touches on:**
- Climate change impacts (can be distressing)
- Threats to subsistence resources (culturally critical)
- Environmental degradation (loss of pristine areas)
- Uncertain future (anxiety-producing)

**Student reactions may include:**
- Concern for fish and food security
- Sadness about environmental change
- Anger at climate injustice
- Anxiety about future
- Determination to document and act

### Creating Safe Learning Space

**Acknowledge feelings:**
- "This is hard to look at"
- "It's okay to feel concerned"
- "Your traditional foods are important"

**Emphasize agency:**
- "GIS helps us document what's happening"
- "This analysis can support action"
- "We're learning tools to protect what we value"
- "Community knowledge is powerful"

**Avoid:**
- Minimizing concerns ("It's probably fine")
- Doom and gloom ("Everything is ruined")
- Blaming ("This is because of...")
- Helplessness ("Nothing we can do")

**Frame positively:**
- "We're learning to monitor"
- "We can share findings with authorities"
- "Traditional knowledge + GIS = powerful combination"
- "Community-driven science"

### Integrating Traditional Knowledge

**Before computer work:**
- Ask: "Have elders noticed water quality changes?"
- Invite: "Share what you know about these streams"
- Record: Document community observations
- Honor: Traditional knowledge is data too!

**During analysis:**
- Compare: "Does what we see in satellite imagery match what community members have observed?"
- Validate: If elder says stream changed, that's legitimate observation
- Question: "Are there affected areas not visible from satellite?"

**After analysis:**
- Discuss: "How can we share this with community?"
- Plan: "What traditional monitoring can continue?"
- Act: "Who needs to see this information?"

### Scientific Accuracy

**While honoring traditional knowledge, maintain scientific rigor:**

**Teach students to:**
- Document sources (satellite imagery date, elder interview, field visit)
- Distinguish observation from interpretation
- Use evidence-based analysis
- Cite scientific literature
- Make appropriate claims based on data

**Avoid:**
- Overstating findings ("This will kill all fish" - we don't know that)
- Understating findings ("It's just a little color" - heavy metals are serious)
- Speculation without evidence
- Alarmism

**Appropriate framing:**
- "Satellite imagery shows orange coloration consistent with rusting rivers"
- "Heavy metal contamination is documented in similar streams"
- "Potential impacts on fish populations require water quality testing"
- "Community observations align with satellite findings"

### Action Planning

**Help students think beyond the assignment:**

**Immediate:**
- Share maps with Tribal Environmental Coordinator
- Present to Council
- Post findings in community spaces

**Short-term:**
- Request water quality testing
- Connect with university researchers
- Submit to EPA or state agencies
- Create community awareness materials

**Long-term:**
- Establish monitoring protocol
- Train community environmental monitors
- Contribute to regional databases
- Advocate for climate action

**Connect to careers:**
- "Environmental monitoring is a real job"
- "Tribal environmental programs hire GIS technicians"
- "You could do this professionally"

---

## Troubleshooting Common ArcGIS Pro Issues

### "ArcGIS Pro is Running Slow"

**Common causes:**
1. Too many layers loaded
2. Large raster files
3. Complex analysis running
4. Insufficient RAM
5. Background processes

**Solutions:**
- Remove unused layers
- Clip rasters to study area
- Close other programs
- Wait for processes to complete
- Check system resources (Task Manager)
- Simplify symbology (graduated symbols can slow things down)

**Teach students:**
- Be patient - some operations take time
- Save before running intensive analysis
- Work with smaller datasets when learning
- Use lower resolution imagery for practice

### Geoprocessing Tools Failing

**Read the error message!** (Students often don't)

**Common errors:**

**"Invalid topology"**
- Polygon doesn't close properly
- Self-intersecting features
- **Fix:** Use Check Geometry tool, Repair Geometry

**"Scratch workspace is read-only"**
- Permissions issue
- **Fix:** Tools → Geoprocessing Options → Environments → Set scratch workspace to Documents folder

**"Output already exists"**
- Trying to overwrite without setting enabled
- **Fix:** Geoprocessing Options → Allow overwriting, or rename output

**"Feature class is locked"**
- Still being edited
- **Fix:** Save edits, stop editing

**"Missing spatial reference"**
- Coordinate system not defined
- **Fix:** Define projection (don't project it yet!)

### Edits Not Saving

**Checklist:**
1. Did you start an edit session? (Edit tab → Create)
2. Did you click Save in Edit ribbon?
3. Is geodatabase read-only? (check file permissions)
4. Is someone else editing? (multi-user geodatabase)
5. Did ArcGIS Pro crash? (edits lost if not saved)

**Prevent this:**
- Save edits every 5-10 minutes
- Teach "Save early, save often"
- Watch for save confirmation
- Don't assume auto-save (it's not automatic!)

### Layers Not Displaying

**Troubleshooting steps:**

1. **Is layer checked on in Contents?**
   - Solution: Check the box

2. **Are you zoomed to wrong location?**
   - Solution: Right-click layer → Zoom to Layer

3. **Is coordinate system wrong?**
   - Solution: Check layer properties → Source → Spatial Reference
   - Define projection if undefined

4. **Is layer in scale range for visibility?**
   - Solution: Right-click layer → Properties → Display → Scale Range

5. **Is symbology invisible?**
   - Solution: Check symbology, change color

**Teach systematic troubleshooting:**
- Check one thing at a time
- Verify basics first
- Read properties
- Look for error symbols (yellow triangles)

### Keyboard Shortcuts to Teach

**Essential shortcuts:**
- **Ctrl + S** - Save project
- **Ctrl + Z** - Undo
- **C** - Explore tool
- **Z** - Zoom tool
- **F2** - Finish sketch
- **Ctrl + Delete** - Delete selected feature
- **Spacebar** - Pan tool
- **V** - Vertex editing

**Print reference sheet!**
- Put on wall
- Hand out copies
- Practice using them

---

## Cultural Considerations and Best Practices

### Language

**Place names:**
- Use Yup'ik names when they exist
- Ask elders for correct names
- Include both Yup'ik and English in attributes
- Spell correctly (ask for verification)

**Examples:**
- Quinhagak (not alternative spellings)
- Kuinerrarmiut (People of Quinhagak)
- Use locally-preferred terms

### Traditional Knowledge Protocol

**Asking permission:**
- Some knowledge may be sensitive
- Some locations may be culturally significant
- Not all knowledge is appropriate to map publicly
- Always ask before sharing

**Documentation:**
- Record who shared knowledge
- Note if information is public or restricted
- Respect wishes about sharing
- Credit knowledge holders

**Integration:**
- Traditional knowledge = legitimate data
- Equal weight to scientific observation
- Both ways of knowing are valuable
- GIS is a tool, not a replacement for traditional knowledge

### Community Ownership

**Who owns the data?**
- Community data belongs to community
- Students are creating resources for community
- Not for personal portfolios without permission
- Respect Tribal Council oversight

**Sharing decisions:**
- Tribal Council should approve public sharing
- Environmental data may have advocacy implications
- Some information kept internal
- Students should ask before posting online

### Employment and Future Opportunities

**Frame this training as career pathway:**
- Tribal environmental programs hire GIS staff
- Natural resources departments need these skills
- Regional corporations employ GIS technicians
- Federal/state agencies have positions
- Consulting firms work with tribes

**Build confidence:**
- "You can do this professionally"
- "These are marketable skills"
- "Tribes need local GIS expertise"
- "You understand community context that outsiders don't"

**Connect to opportunities:**
- Internships with regional entities
- Tribal environmental programs
- Natural resources departments
- Regional nonprofit organizations
- Educational pathways (UAF, community colleges)

---

## Assessment Strategies

### Formative Assessment (During Learning)

**Observation:**
- Watch students work
- Note who's struggling, who's excelling
- Provide just-in-time help
- Adjust pacing based on class

**Questioning:**
- Ask students to explain what they're doing
- "Why did you choose that coordinate system?"
- "What tool would you use for this?"
- Check understanding frequently

**Practice exercises:**
- Small tasks during lessons
- Immediate feedback
- Opportunity to correct
- Build confidence

### Summative Assessment (End of Module)

**Required deliverables:**
1. Completed geodatabase with features
2. Three professional maps
3. Written analysis (3-5 pages)
4. Brief presentation

**Rubric categories:**
- Technical skills (correct use of tools)
- Data quality (complete, accurate features)
- Cartography (clear, professional maps)
- Analysis (thoughtful interpretation)
- Traditional knowledge integration
- Community relevance
- Communication (writing, presenting)

### Alternative Assessments

**For diverse learners:**

**Visual learners:**
- Create annotated map series
- Infographic instead of written report
- Visual story of analysis process

**Verbal learners:**
- Oral presentation to community
- Recorded explanation of findings
- Interview format assessment

**Hands-on learners:**
- Live demonstration of skills
- Field verification of GIS findings
- Teaching skill to another student

**Portfolio option:**
- Collection of work from all activities
- Reflection on learning process
- Application plan for community use

---

## Differentiation Strategies

### For Students Who Need More Support

**Strategies:**
- Pair with stronger student (peer mentoring)
- Provide step-by-step written instructions
- Slow down pacing for this student
- One-on-one help during class
- Simplified version of activities
- Focus on core skills, skip advanced topics
- Extra time for assignments

**Encouragement:**
- Celebrate small successes
- Emphasize progress over perfection
- GIS is hard - learning curve is normal
- Everyone learns at own pace

### For Advanced Students

**Challenge them:**
- Additional analysis techniques
- More complex spatial questions
- Statistical analysis
- Programming (Python in ArcGIS Pro)
- Help other students (teaching reinforces learning)
- Independent project on topic of interest
- Deeper integration with traditional knowledge

**Extensions:**
- Google Earth Engine analysis
- Time-series analysis
- 3D visualization
- ModelBuilder workflows
- Automated processes

### Language Considerations

**If English is second language:**
- Use visual demonstrations
- Provide vocabulary lists
- Allow extra processing time
- Yup'ik terms when applicable
- Buddy system
- Write key terms on board
- Check understanding frequently

---

## Logistical Notes

### Computer Lab Setup

**Before students arrive:**
- All computers turned on
- ArcGIS Pro installed and licensed
- Internet connection verified
- AGOL accounts tested
- Quinhagak data accessible
- Balloons inflated (or materials ready)
- Markers distributed
- Scissors available

**During class:**
- Projector connected and tested
- Instructor machine mirrors to screen
- Students can see clearly
- Enough space to work
- Power cords available
- Mouse for each computer (trackpads hard for GIS)

### Timing and Pacing

**Be flexible:**
- Some activities take longer than planned
- Students learn at different rates
- Technical issues cause delays
- Important discussions emerge

**Buffer time:**
- Build in extra 15-30 min each half-day
- Use for questions, troubleshooting, catch-up
- Better to have extra time than rush

**Breaks:**
- Every 60-75 minutes
- Allow bathroom, water, phone calls
- Students need mental breaks from screen
- 10-15 minutes sufficient

### Materials Checklist

**Per student:**
- Computer with ArcGIS Pro
- Mouse
- Notepad and pen
- Folder for handouts

**Per group (for balloon activity):**
- 2 balloons (one backup)
- Permanent marker
- Paper for notes
- Scissors
- Mat or towel

**Classroom:**
- Projector
- Whiteboard/markers
- Printed handouts
- Reference sheets
- EPSG codes printout
- Keyboard shortcuts reference

### Documentation

**Keep:**
- Student work samples
- Screenshots of common errors (for troubleshooting guide)
- Photos of balloon activity
- Notes on what worked/didn't work
- Student feedback
- Timing notes (adjust future modules)

---

## Reflection and Improvement

### After Each Day

**Quick reflection:**
- What went well?
- What was confusing?
- What took longer than expected?
- What should be added/removed?
- Individual student needs identified?

### After Module Completion

**Comprehensive review:**
- Survey students (what helped most? what was hard?)
- Review student work (common errors? gaps in understanding?)
- Compare to learning objectives (all met?)
- Update materials based on experience
- Revise timing estimates
- Improve troubleshooting guide

### Continuous Improvement

**Update this guide with:**
- New common errors discovered
- Better explanations that worked
- Additional teaching strategies
- Student feedback incorporated
- Real-world applications from community
- Success stories

---

## Resources for Instructors

### ArcGIS Pro Teaching Resources

- [Esri Training Catalog](https://www.esri.com/training/)
- [Learn ArcGIS Lessons](https://learn.arcgis.com/)
- [ArcGIS Pro Documentation](https://pro.arcgis.com/en/pro-app/latest/help/main/welcome-to-the-arcgis-pro-app-help.htm)

### Coordinate Systems

- [EPSG.io](https://epsg.io/)
- [Projection Wizard](https://projectionwizard.org/)
- [Alaska State Plane Zones Map](https://www.commerce.alaska.gov/web/portals/4/pub/StatePlane.pdf)

### Rusting Rivers Science

- Scientific American article
- National Geographic article
- USGS permafrost research
- Alaska Native Science Commission

### Cultural Competency

- Working with Alaska Native Communities
- Traditional Knowledge protocols
- Tribal consultation best practices

---

## Final Notes

**This module is intensive:**
- Lots of new concepts
- Complex software
- Challenging activities
- But incredibly rewarding!

**Focus on:**
- Building confidence with software
- Connecting to community applications
- Honoring multiple ways of knowing
- Creating useful products for community
- Preparing for careers

**Success looks like:**
- Students comfortable opening ArcGIS Pro
- Understanding when to use which tools
- Able to create basic features and analysis
- Excited about GIS applications
- Proud of work created
- Sharing findings with community

**Remember:**
- Be patient with technology learning curve
- Celebrate successes
- Troubleshoot with calm
- Connect to culture and community
- Make it relevant
- Have fun!

**The balloon activity, rusting rivers analysis, and tracing historical features make this module memorable and meaningful. Keep those core activities central.**

---

**Quyana!** (Thank you!)

**Good luck teaching this module!**

---

**Document Version:** 1.0
**Last Updated:** November 2025
**Instructor:** Sean Gleason
**Location:** Quinhagak, Alaska
