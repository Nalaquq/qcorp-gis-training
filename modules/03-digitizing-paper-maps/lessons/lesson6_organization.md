# Lesson 6: Map Organization and Prioritization

**Duration:** 60 minutes
**Difficulty:** Intermediate
**Prerequisites:** Understanding of georeferencing workflow

---

## Overview

With potentially hundreds of paper maps in a collection, knowing how to assess, prioritize, and organize is essential. This lesson teaches you how to evaluate map collections, prioritize digitization efforts, cross-reference with existing GIS data, and create sustainable organizational systems.

---

## Learning Objectives

By the end of this lesson, you will:

1. ✅ Assess a paper map collection systematically
2. ✅ Prioritize maps for digitization
3. ✅ Cross-reference with existing GIS layers
4. ✅ Create physical organization systems
5. ✅ Develop documentation and tracking methods
6. ✅ Plan sustainable digitization programs

---

## Part 1: Assessing the Collection (15 minutes)

### Initial Survey

**Before You Start Digitizing:**
Take time to understand what you have!

**Survey Questions:**

**1. How many maps?**
- Quick count
- Estimate ranges (50-100? 100-200?)
- Helps plan time needed

**2. What types of maps?**
- Survey maps (ANCSA, PLSS, etc.)
- Land use maps
- Infrastructure maps
- Resource maps (hunting, fishing areas)
- Historical maps
- Planning documents
- Other

**3. What condition?**
- Excellent (clean, flat, clear)
- Good (some wear but usable)
- Fair (faded, torn edges, but readable)
- Poor (significant damage, fading)
- Deteriorating urgently (needs immediate attention)

**4. What time periods?**
- When were maps created?
- Range of years (1950s? 1980s? 2000s?)
- Identify oldest maps (may be priority)

**5. What sizes?**
- Standard (8.5×11, 11×17)
- Large format (24×36, 36×48)
- Oversized (rolled maps)
- May affect photography setup needed

**6. Storage conditions?**
- Flat filed (ideal)
- Rolled
- Folded (potential damage along creases)
- Stacked loosely
- Environmental conditions (damp? dry? temperature?)

### Creating an Inventory

**Quick Inventory Form:**

| Map # | Title/Description | Year | Type | Size | Condition | Priority | Notes |
|-------|-------------------|------|------|------|-----------|----------|-------|
| 001 | ANCSA 14(c) Survey | 1982 | Survey | 24×36 | Good | High | Show village lands |
| 002 | Infrastructure Plan | 1975 | Infrastructure | 11×17 | Fair | Medium | Faded colors |
| 003 | Land Use Map | 1990 | Planning | 24×36 | Excellent | Medium | Good condition |

**Capture:**
- Unique ID number (for tracking)
- Brief title or description
- Year (if shown)
- Map type
- Approximate size
- Condition assessment
- Initial priority (you'll refine this)
- Any special notes

**Tools:**
- Spreadsheet (Excel, Google Sheets)
- Simple table
- Can be refined later
- Quick and functional

### Real Example: Qanirtuuq Land Manager's Office

**What Students Found:**
- Decades of paper maps
- ANCSA surveys
- Land use plans
- Infrastructure maps
- Historical records
- Various conditions
- Needed organization!

**What They Did:**
- Surveyed collection
- Identified approximately 40 maps to digitize
- Organized by priority
- Digitized all 40 in one day!
- Uploaded to ArcGIS Online

---

## Part 2: Prioritization Criteria (15 minutes)

### How to Decide What to Digitize First?

With limited time, prioritize strategically!

### Priority Matrix

**High Priority Maps:**
1. **Deteriorating Condition**
   - Urgent need before information lost
   - Fading rapidly
   - Physical damage worsening
   - May not survive much longer

2. **High Community Need**
   - Frequently requested information
   - Supports current decisions
   - Legal/administrative importance
   - Example: ANCSA conveyances

3. **Unique Information**
   - Information not available elsewhere
   - Not yet in digital form
   - No other copies known
   - Irreplaceable knowledge

4. **Historical Significance**
   - Documents important events
   - Shows historical land use
   - Traditional knowledge documentation
   - Cultural importance

5. **Easy to Georeference**
   - Clear features visible
   - Good control points available
   - Recent enough that area recognizable
   - Quick wins build momentum!

**Medium Priority:**
- Important but stable condition
- Information exists elsewhere but map adds detail
- Moderate community interest
- Moderate difficulty to georeference

**Lower Priority:**
- Good condition (can wait)
- Information readily available in other sources
- Limited current use
- Very difficult to georeference (save for when more experienced)

### Scoring System (Optional)

**Rate Each Map 1-5 on:**
- Urgency (condition): 1=excellent, 5=deteriorating
- Importance (community need): 1=low interest, 5=critical
- Uniqueness (information): 1=duplicate, 5=unique
- Difficulty (georeferencing): 1=very hard, 5=easy

**Total Score: Add up (max 20)**
- 16-20: High priority
- 11-15: Medium priority
- 5-10: Lower priority

**Example:**

| Map | Urgency | Importance | Uniqueness | Difficulty | Total | Priority |
|-----|---------|------------|------------|------------|-------|----------|
| ANCSA 14(c) 1982 | 3 | 5 | 5 | 4 | 17 | HIGH |
| Infrastructure 1975 | 4 | 4 | 3 | 3 | 14 | MEDIUM |
| Modern Road Map | 1 | 2 | 1 | 5 | 9 | LOW |

---

## Part 3: Cross-Referencing with GIS (15 minutes)

### Why Cross-Reference?

**Key Question:** Does this information already exist in GIS?

**If YES:**
- Lower priority for digitization
- May still be valuable for historical comparison
- But less urgent

**If NO:**
- Higher priority
- Fills gap in GIS coverage
- Adds value to GIS database

### How to Cross-Reference

**Step 1: Identify Map Subject**
What does this map show?
- Parcels?
- Infrastructure (roads, utilities)?
- Land use?
- Resources?
- Boundaries?

**Step 2: Search ArcGIS Online**

**Search for existing layers:**
1. Go to ArcGIS Online
2. Search for:
   - "Quinhagak [subject]"
   - "Alaska [subject]"
   - Subject generally
3. Look in:
   - Organization content
   - Public content
   - Living Atlas

**Example Searches:**
- "Quinhagak parcels"
- "Alaska villages"
- "ANCSA lands"
- "Alaska roads"

**Step 3: Compare Content**

**If you find similar GIS layer:**
- Is it comprehensive or partial?
- Is it current or outdated?
- Does historical map add information?
- Does historical map show change over time?

**Decision:**
- Identical information → Lower priority
- Partial information → Historical map fills gaps → Higher priority
- Different time period → Historical comparison value → Medium priority

**Step 4: Note in Inventory**

Add column: "Exists in GIS?"
- Yes - same information
- Yes - but outdated
- Partial - map adds detail
- No - unique information

### Example: Quinhagak ANCSA Map

**Map Content:** ANCSA 14(c) land conveyances from 1982

**Search AGOL:** "Alaska ANCSA lands"
- Find general ANCSA layers
- May show conveyances at broad scale
- But historical survey map shows detail!

**Decision:** High priority - adds detailed historical documentation

### Building a Gaps List

**What's NOT in GIS yet?**

Review your map collection and note:
- Subjects/themes not covered in AGOL
- Time periods not represented
- Details not shown in existing data
- Local knowledge not captured

**These gaps = high priority for digitization!**

---

## Part 4: Physical Organization (10 minutes)

### Organizing the Physical Collection

**Goals:**
- Protect maps from damage
- Make maps easy to find
- Track what's been digitized
- Maintain order

### Storage Methods

**Flat File Cabinets (Ideal):**
- Maps stored flat
- Drawers by category or size
- Acid-free folders
- Label each drawer

**Rolled Maps:**
- If too large for flat storage
- Use archival tubes
- Label outside with contents
- Store horizontally if possible (not standing)

**Folders/Binders:**
- For smaller maps (8.5×11, 11×17)
- Organize by category
- Use archival-quality sleeves

### Categorization Systems

**Option 1: By Type**
- Survey Maps
- Infrastructure
- Land Use
- Historical
- Resource Maps
- Planning Documents

**Option 2: By Year**
- 1950s-1960s
- 1970s-1980s
- 1990s-2000s
- 2010s-present

**Option 3: By Status**
- To Be Digitized
- Digitized, Not Georeferenced
- Georeferenced, Not Uploaded
- Complete (Uploaded to AGOL)

**Best: Combination**
- Primary organization by type or year
- Secondary sorting by digitization status

### Labeling

**Label Each Map:**
- Unique ID number (matches inventory)
- Brief title
- Year
- Digitization status

**Can use:**
- Sticky notes (temporary)
- Archival labels (permanent)
- Pencil on back (if appropriate)

**Example Label:**
```
ID: 001
ANCSA 14(c) Survey - 1982
Status: Uploaded to AGOL ✓
Date Digitized: 10/15/2024
```

### Creating a Finding Aid

**Physical Document Near Maps:**
- Location guide
- "Survey maps in drawer 1"
- "Infrastructure maps in drawer 2"
- Quick reference for finding maps

**Can be:**
- Printed spreadsheet
- Handwritten index card
- Posted on wall
- Laminated guide

---

## Part 5: Tracking Progress (10 minutes)

### Digitization Workflow Tracker

**Expand your inventory to track progress:**

| Map ID | Title | Status | Photo Date | Georef Date | Upload Date | AGOL URL | Notes |
|--------|-------|--------|------------|-------------|-------------|----------|-------|
| 001 | ANCSA 14c 1982 | Complete | 10/15/24 | 10/15/24 | 10/15/24 | [URL] | Success! |
| 002 | Infrastructure 1975 | In Progress | 10/15/24 | - | - | - | Need control points |

**Status Options:**
- Not Started
- Photographed
- Georeferencing
- Complete
- Problem (note issue)

**Benefits:**
- See progress at a glance
- Identify bottlenecks
- Celebrate completion!
- Report to land manager or supervisor

### Visual Progress Tracking

**Simple Chart on Wall:**

```
Total Maps: 40
Photographed: 40 ✓
Georeferenced: 38 (95%)
Uploaded: 38 (95%)

In Progress: 2
- Infrastructure 1975 (georeferencing)
- Land Use 1990 (georeferencing)
```

**Benefits:**
- Motivating to see progress
- Team can see status
- Easy to update

### Quality Control Checklist

**For Each Map, Verify:**
- ✅ Photo quality acceptable
- ✅ Georeferencing RMS error < 5 pixels
- ✅ Visual alignment verified
- ✅ Metadata complete (title, tags, description)
- ✅ Uploaded to AGOL
- ✅ Shared to group
- ✅ Tested in web map
- ✅ Documented in tracker

---

## Part 6: Sustainable Programs (10 minutes)

### Planning for Ongoing Work

**One-time project vs. Ongoing program:**

**One-time:**
- Digitize existing collection
- Upload to AGOL
- Done!

**Ongoing:**
- New maps acquired
- Continuous digitization
- Maintained system
- Better long-term!

### Setting Up Ongoing Digitization

**1. Designated Space**
- Photography station always set up
- Or easy to set up
- Equipment stored nearby

**2. Regular Schedule**
- Example: Every Friday afternoon
- Or: One day per month
- Consistency helps

**3. Assigned Responsibility**
- Who's in charge?
- Primary + backup person
- Trained on procedures

**4. Procedures Documented**
- Written instructions
- Step-by-step guides
- So anyone can do it

**5. Quality Standards**
- Defined and written
- Consistent results
- Checklist-based

### Training Others

**To sustain program, train multiple people:**

**Training Program:**
1. Shadow experienced person
2. Practice on sample maps
3. Do one map start-to-finish supervised
4. Do several independently
5. Become trainer for next person!

**Benefits:**
- Doesn't depend on one person
- Builds institutional capacity
- Community skill development

### Integration with Workflow

**When new maps arrive:**
1. Add to inventory immediately
2. Assign priority
3. Add to digitization queue
4. Process based on priority
5. Update tracker

**Routine:**
- Check for new maps weekly
- Process high-priority maps promptly
- Maintain backlog of lower-priority
- Regular uploads to AGOL

### Funding and Resources

**Ongoing program needs:**
- Staff time
- Equipment maintenance
- Storage space
- AGOL account (organizational)
- Computer and software

**Potential Funding Sources:**
- Tribal budget
- BIA grants
- Regional corporation support
- Foundation grants
- Cost-share with partners

---

## Practice Exercise

### Exercise: Organize and Prioritize a Map Collection

**Scenario:** You've been given 20 sample maps to organize

**Tasks:**

**1. Create Inventory (20 min)**
- Examine each map
- Record in spreadsheet:
  - ID number
  - Title
  - Year
  - Type
  - Condition
  - Size

**2. Prioritize (15 min)**
- Score each map (urgency, importance, uniqueness, difficulty)
- Calculate total scores
- Rank from high to low priority
- Identify top 5 for immediate digitization

**3. Cross-Reference (15 min)**
- Search AGOL for similar content
- Note if information already exists in GIS
- Identify unique/gap-filling maps

**4. Create Organization Plan (10 min)**
- How would you store these 20 maps?
- What categories?
- What labeling system?
- Sketch storage layout

**5. Present Recommendations**
- Which 5 maps to digitize first? Why?
- How would you organize the collection?
- What system for tracking progress?

---

## Real-World Success: Quinhagak One-Day Project

### The Challenge
- Qanirtuuq Land Manager's office full of paper maps
- Decades of accumulation
- No organization system
- Maps deteriorating
- Information not accessible

### The Approach

**Day 1: Organization and Digitization**

**Morning:**
- Surveyed entire collection
- Created quick inventory
- Prioritized maps
- Organized physical storage

**Afternoon:**
- Set up photography station
- Photographed ~40 maps
- Maintained consistent workflow
- Documented each map

**Result:**
- Organized office
- 40 maps photographed
- Many georeferenced
- All uploaded to AGOL
- Shared through group: https://arcg.is/0H8S1y1

### Keys to Success

1. **Clear prioritization** - Knew what to focus on
2. **Team effort** - Multiple people working together
3. **Documented system** - Could track progress
4. **Realistic goals** - Focused on high-priority maps
5. **Sustained momentum** - One day intensive work
6. **Accessible results** - Immediate community benefit

### Long-Term Impact

**Immediate:**
- Historical records preserved digitally
- Information accessible online
- Physical maps organized

**Ongoing:**
- System in place for future maps
- Trained GIS technicians
- Community resource established
- Foundation for continued work

---

## Key Takeaways

1. **Survey before you start** - Understand what you have
2. **Prioritize strategically** - Urgency, importance, uniqueness
3. **Cross-reference with GIS** - Focus on unique information
4. **Organize physically** - Protect maps, make findable
5. **Track progress** - Know what's done, what's left
6. **Plan for sustainability** - Ongoing program, not just one-time
7. **Train multiple people** - Build capacity
8. **Document procedures** - Enables continuity

---

## Assessment Questions

1. What factors should you consider when prioritizing maps for digitization?
2. Why is it important to cross-reference with existing GIS layers?
3. Describe an effective physical organization system for paper maps.
4. What should be tracked in a digitization progress spreadsheet?
5. How can you make a digitization program sustainable long-term?
6. Why is training multiple people important?
7. What was the key to Quinhagak's success in digitizing 40 maps in one day?

---

## Final Project: Land Manager's Office Organization

**This is the capstone activity for the module!**

See: [Activity 6: Land Manager's Office Organization Project](../activities/activity-06-office-organization.md)

**You will:**
- Apply all lessons from this module
- Work with real collection
- Produce real results for community
- Build sustainable system

**This is where theory becomes practice!**

---

## Resources

### Map Preservation
- [National Archives - Map Preservation](https://www.archives.gov/preservation/formats/maps-architectural-drawings.html)
- [Library of Congress - Map Care](https://www.loc.gov/preservation/care/map.html)

### Project Management
- [Free Project Templates](https://www.smartsheet.com/free-project-plan-templates)
- [Trello - Simple Project Tracking](https://trello.com/)

### Quinhagak Success
- [Georeferenced Maps Group](https://arcg.is/0H8S1y1)

---

**Lesson Version:** 1.0
**Last Updated:** November 2025
**Achievement:** 40 maps organized and digitized in one day!

**You can do this too!**
