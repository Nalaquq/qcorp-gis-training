# Lesson 5: Content Management

**Module:** 01 - ArcGIS Online Basics  
**Duration:** 30 minutes  
**Difficulty:** Beginner  
**Prerequisites:** Lessons 1-4 completed

---

## Learning Objectives

1. Organize content using folders and Groups
2. Understand sharing permissions and levels
3. Publish feature layers from your data
4. Manage organizational content effectively
5. Apply best practices for data management

---

## Organizing Your Content

### Folders: Personal Organization

**Why use folders?**
- Keep work organized by project
- Find items quickly
- Separate training from real work
- Professional appearance

**Create folder structure:**
```
My Content/
├── GIS Training 2025/
│   ├── Module 01/
│   ├── Module 02/
│   └── Practice/
├── Active Projects/
│   ├── Gravel Pit Documentation/
│   ├── Erosion Monitoring/
│   └── Infrastructure Mapping/
└── Archive/
    └── Completed Projects/
```

**Best Practices:**
- Create folders BEFORE creating content
- Use clear, descriptive names
- Don't nest too deeply (2-3 levels max)
- Archive old projects
- Regular cleanup (monthly)

---

## Groups: Collaborative Organization

### What are Groups?

**Groups** = Shared spaces where multiple people can:
- Share maps and data
- Collaborate on projects
- Organize team content
- Control access to information

### Types of Groups

**Private Group:**
- Invitation only
- Good for sensitive projects
- Team collaboration

**Organization Group:**
- Anyone in your org can join
- Good for department-wide sharing

**Public Group:**
- Anyone can view content
- Good for public resources

### Creating a Group

1. Go to **Groups** tab
2. Click **Create Group**
3. Fill in details:
   - Name: "Quinhagak Land Management"
   - Summary: Brief description
   - Tags: Relevant keywords
   - Access: Choose level
4. Click **Create Group**

### Managing Groups

**Add members:**
- Invite by username or email
- Set member roles (owner, manager, member)

**Share content to group:**
- From item page, click **Share**
- Select group(s)
- Click **Update Sharing**

---

## Understanding Sharing Permissions

### Three Levels of Sharing

**1. Private (Default):**
- Only you can see it
- ✅ Use for: Work in progress, personal drafts
- ❌ Don't use for: Final products meant for others

**2. Organization:**
- Everyone in Qanirtuuq/Nalaquq can see it
- ✅ Use for: Internal collaboration, team resources
- ❌ Don't use for: Public-facing content

**3. Everyone (Public):**
- Anyone on the internet can see it
- ✅ Use for: Community maps, public reports
- ❌ **NEVER use for:** Sensitive data, personal information, draft work

### How to Change Sharing

**From item page:**
1. Open your item
2. Click **Settings** tab
3. Scroll to **Sharing** section
4. Select appropriate level
5. Click **Save**

**Quick share:**
1. Find item in Content
2. Click **Share** button
3. Select level
4. Click **Update Sharing**

### Sharing Best Practices

**Always Ask:**
- Who needs to see this?
- Is there sensitive information?
- Is this final or draft?
- What permissions do viewers need?

**Security Checklist:**
- [ ] No personal information (names, addresses)
- [ ] No culturally sensitive locations
- [ ] No proprietary data
- [ ] No draft/unfinished work shared publicly
- [ ] Appropriate for intended audience

---

## Publishing Feature Layers

### What is a Feature Layer?

**Feature Layer** = Data layer that can be:
- Edited in the field
- Queried and analyzed
- Styled and symbolized
- Shared with others
- Used in multiple maps

### When to Publish Data

**Publish when you want to:**
- Collect field data (Survey123, Field Maps)
- Share editable data with team
- Use same data in multiple maps
- Enable collaboration
- Perform analysis

**Don't publish:**
- Simple reference maps (use map notes instead)
- One-time use data
- Temporary visualizations

### Publishing from CSV

**Example: Infrastructure locations**

1. Prepare CSV file:
```csv
Name,Type,Latitude,Longitude,Condition
Red Building,Public Facility,59.7554,-161.8846,Good
Airstrip,Infrastructure,59.7542,-161.8823,Fair
```

2. Go to **Content** → **Add Item**
3. Select **From my computer**
4. Choose your CSV file
5. Configure settings:
   - Location fields: Latitude, Longitude
   - Coordinate system: WGS84
   - Layer name: "Quinhagak Infrastructure"
6. Click **Add Item**

### Publishing from Shapefile

1. Zip your shapefile (must include .shp, .shx, .dbf, .prj)
2. Go to **Content** → **Add Item**
3. Select **From my computer**
4. Choose zipped shapefile
5. Configure settings
6. Click **Add Item**
7. Click **Publish** to create feature service

---

## Managing Published Layers

### Item Details Page

**Key sections:**
- **Overview:** Description, tags, credits
- **Settings:** Sharing, update capabilities
- **Visualization:** Preview map
- **Data:** View attribute table
- **Usage:** How many views

### Edit Capabilities

**Control who can edit:**
1. Open feature layer
2. Go to **Settings** tab
3. Find **Feature Layer (Hosted) Settings**
4. Check/uncheck editing options:
   - Enable editing
   - Add features
   - Delete features
   - Update feature attributes
   - Update feature geometry

**Important:** Be careful with public editing!

### Update Data

**Replace data in existing layer:**
1. Open feature layer
2. Click **Update Data**
3. Choose **Overwrite Entire Layer**
4. Upload new file
5. Match fields
6. Click **Update**

**Why update vs. new layer?**
- Maps using this layer update automatically
- Maintains sharing settings
- Preserves item ID and URLs

---

## Organizing Team Content

### For Land Manager Role

**Recommended structure:**

**Active Projects folder:**
- Current mapping projects
- In-progress assessments
- Updated regularly

**Reference Data folder:**
- Base layers (boundaries, infrastructure)
- Historical data
- Rarely changes

**Training Materials folder:**
- Practice exercises
- Example maps
- Learning resources

**Archive folder:**
- Completed projects
- Historical records
- Old versions

### Naming Conventions

**Be consistent:**
```
Good names:
- Infrastructure_Map_2025_10_15
- Gravel_Pit_Analysis_Final
- Erosion_Monitoring_Points

Bad names:
- Map1
- Untitled
- Copy of Copy of Map
```

**Include:**
- Project name
- Date (YYYY_MM_DD format)
- Version if multiple
- Descriptive keywords

---

## Best Practices Summary

### Do's ✓

- ✅ Create folder structure early
- ✅ Use descriptive names and tags
- ✅ Delete old test items regularly
- ✅ Document data sources in descriptions
- ✅ Set appropriate sharing levels
- ✅ Archive completed work
- ✅ Use Groups for collaboration
- ✅ Review content quarterly

### Don'ts ✗

- ❌ Leave everything in root folder
- ❌ Use generic names
- ❌ Keep old test data forever
- ❌ Share sensitive data publicly
- ❌ Forget to add descriptions
- ❌ Create duplicate copies unnecessarily
- ❌ Give everyone edit access
- ❌ Ignore storage limits

---

## Quick Reference

### Common Tasks

**Move item to folder:**
Content → Select item → Move → Choose folder

**Share item with group:**
Item page → Share → Select group → Update

**Change item sharing:**
Item page → Settings → Sharing section → Update

**Delete old item:**
Content → Select item → Delete (be sure!)

**Update feature layer data:**
Item page → Update Data → Overwrite

---

# Lesson 6: Integrating GIS into Resources

**Module:** 01 - ArcGIS Online Basics  
**Duration:** 30 minutes  
**Difficulty:** Beginner-Intermediate  
**Prerequisites:** Lessons 1-5 completed

---

## Learning Objectives

1. Embed maps in websites and documents
2. Create simple dashboards
3. Share maps with stakeholders effectively
4. Integrate GIS into reports and presentations
5. Understand use cases for different sharing methods

---

## Embedding Maps

### Why Embed?

**Instead of sending a link**, you can embed maps directly in:
- Websites
- Blog posts
- Online reports
- Presentations (using web view)
- Email newsletters

**Benefits:**
- Viewers don't leave your page
- More professional appearance
- Interactive within your content
- Updates automatically

### How to Embed a Web Map

1. Open your web map
2. Click **Share** button
3. Check **Embed in website**
4. Copy the iframe code:
```html
<iframe width="500" height="400" frameborder="0" scrolling="no" 
  src="https://arcgis.com/apps/Embed/index.html?webmap=YOUR_ID">
</iframe>
```
5. Paste into website HTML
6. Adjust width/height as needed

### Embedding Story Maps

1. Open your Story Map
2. Click **Share** button
3. Copy URL
4. Can embed using iframe OR just link

---

## Creating Dashboards

### What is a Dashboard?

**Dashboard** = Real-time display combining:
- Maps
- Charts
- Statistics
- Lists
- Gauges

**Use cases:**
- Monitor ongoing projects
- Display live data
- Track metrics
- Show multiple views simultaneously

### Quick Start Dashboard

1. Go to https://arcgis.com/apps/dashboards/
2. Click **Create Dashboard**
3. Add elements:
   - Map (your feature layer)
   - Indicator (show count)
   - List (show attributes)
   - Chart (visualize data)
4. Configure each element
5. Arrange layout
6. Save and share

**Example use:**
"Infrastructure Status Dashboard"
- Map showing all infrastructure
- Count of buildings by type
- List of items needing repair
- Chart showing condition ratings

---

## Sharing with Stakeholders

### For Community Members

**Best methods:**
- Story Maps (most accessible)
- Simple web maps with clear symbology
- Printed maps with QR codes to online version
- Email with direct link and instructions

**Tips:**
- Test on mobile devices
- Use familiar landmarks for orientation
- Include both English and Yup'ik labels
- Provide context (what am I looking at?)
- Simple is better

### For Board/Leadership

**Best methods:**
- Dashboards (show key metrics)
- Story Maps (provide narrative)
- Printed maps (for meetings without internet)
- PowerPoint with embedded maps

**Tips:**
- Executive summary upfront
- Clear takeaways
- Professional design
- Print-ready versions
- Supporting data available

### For Technical Partners/Agencies

**Best methods:**
- Feature layers (can download/analyze)
- Web maps (with full metadata)
- REST service endpoints
- Downloadable datasets

**Tips:**
- Complete metadata
- Data quality documentation
- Proper coordinate systems noted
- Contact information for questions
- Clear data license/usage terms

---

## Integration into Reports

### Adding Maps to Documents

**Method 1: Screenshot**
1. Configure map view
2. Take high-resolution screenshot
3. Insert into Word/PDF
4. Add figure caption

**Method 2: Print to PDF**
1. In Map Viewer, click Print
2. Configure layout
3. Export as PDF
4. Insert into document

**Method 3: Link**
1. Share map with appropriate permissions
2. Add URL to document
3. Include QR code for easy access

### In Presentations

**PowerPoint/Google Slides:**
- Screenshot for static slides
- Embed URL for interactive demo
- Use Story Map URL for narrative
- QR code for audience follow-along

**Live Presentations:**
- Open map in browser
- Use bookmarks to navigate
- Demonstrate interactive features
- Have backup screenshots

---

## Email and Communications

### Sharing via Email

**Structure:**
```
Subject: Gravel Pit Analysis - Before and After Comparison

Hi [Name],

As requested, I've completed the analysis of gravel pit changes 
from 1992 to 2024. Here's what I found:

[Brief summary - 2-3 sentences]

Interactive Map: [URL]
Story Map with Details: [URL]

Key Findings:
• Finding 1
• Finding 2
• Finding 3

Let me know if you need any additional information.

Best,
[Your name]
```

**Tips:**
- Test links before sending
- Include brief text summary (not everyone clicks links)
- Provide context
- Multiple formats if possible (link + PDF)
- Clear subject line

---

## Use Cases and Applications

### Infrastructure Planning

**Scenario:** Present development options to Board

**Tools:**
- Web map showing 3 potential sites
- Story Map with pros/cons of each
- Dashboard with cost estimates
- Printable summary map

### Environmental Monitoring

**Scenario:** Track erosion over time

**Tools:**
- Feature layer of erosion points
- Dashboard showing erosion rate trends
- Story Map documenting annual changes
- Shareable map for partners

### Community Education

**Scenario:** Explain subsistence area changes

**Tools:**
- Story Map with historical photos and maps
- Simple web map with place names
- Printable map for elders without internet
- QR code for community center display

### Grant Applications

**Scenario:** Support funding request

**Tools:**
- Professional maps showing need
- Story Map providing context
- Dashboard quantifying impact
- PDF export for official submission

---

## Best Practices

### Testing Before Sharing

**Always test:**
- Links work correctly
- Maps load on mobile
- Appropriate permissions set
- No sensitive data visible
- Works in different browsers
- Print quality (if applicable)

### Access and Permissions

**Consider:**
- Does everyone have ArcGIS accounts? (if organization sharing)
- Is internet reliable for intended audience?
- Should this be public or restricted?
- Do people need to edit or just view?

### Maintenance

**Remember to:**
- Update maps when data changes
- Fix broken links
- Archive old versions
- Notify stakeholders of major changes
- Check periodically that shares still work

---

## Quick Reference

### Sharing Decision Tree

```
Need to share a map?
│
├─ Community members without GIS experience?
│  └─ Use: Story Map or simple web map
│
├─ Board/leadership presentation?
│  └─ Use: Dashboard or Story Map + printed maps
│
├─ Technical partners?
│  └─ Use: Feature layer + web map + metadata
│
└─ General public?
   └─ Use: Story Map (most accessible)
```

### Embedding Checklist

Before embedding:
- [ ] Map is shared appropriately
- [ ] Tested in target website
- [ ] Mobile-responsive
- [ ] Loads quickly
- [ ] Has clear title/legend
- [ ] Contact info if needed

---

## Summary

### Key Takeaways

**Content Management:**
- Use folders and Groups for organization
- Set appropriate sharing levels
- Publish feature layers for editable data
- Follow naming conventions
- Regular cleanup and archiving

**Integration:**
- Embed maps in websites for professional appearance
- Create dashboards for monitoring
- Tailor sharing method to audience
- Provide multiple formats when possible
- Test thoroughly before sharing

### What You Can Do Now

✅ Organize all your ArcGIS Online content  
✅ Share maps appropriately with different audiences  
✅ Embed maps in websites and documents  
✅ Create simple dashboards  
✅ Integrate GIS into reports and presentations  
✅ Support decision-making with geographic information

---

## Module 1 Complete!

You've now learned:
1. ✅ ArcGIS Online basics and navigation
2. ✅ Accessing and using satellite imagery
3. ✅ Creating professional web maps
4. ✅ Building Story Maps for communication
5. ✅ Managing and organizing content
6. ✅ Integrating GIS into your work

**Next:** Module 2 - Field Data Collection

---

**Version:** 1.0  
**Last Updated:** October 2025  
**Total Module Time:** ~8-10 hours (lessons + activities)