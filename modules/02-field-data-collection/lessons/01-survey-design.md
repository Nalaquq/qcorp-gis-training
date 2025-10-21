# Lesson 1: Survey Design Fundamentals

**Module:** 02 - Field Data Collection  
**Duration:** 90 minutes  
**Difficulty:** Beginner  
**Prerequisites:** Module 1 (ArcGIS Online Basics)

---

## Learning Objectives

By the end of this lesson, you will:

1. Design effective field surveys
2. Choose appropriate question types
3. Build surveys in Survey123 web designer
4. Configure GPS and photo capture
5. Customize maps and layers
6. Set up automated notifications
7. Control data access and privacy

---

## Why Good Survey Design Matters

| Poor Design | Good Design |
|-------------|-------------|
| ❌ Frustrated field workers | ✅ Complete, accurate data |
| ❌ Incomplete data | ✅ Engaged participants |
| ❌ Time wasted fixing errors | ✅ Ready for immediate analysis |
| ❌ Low participation | ✅ Professional results |

---

## Three Principles of Effective Surveys

### 1. Know Your Purpose

Before creating any survey, answer:
- What decision will this data support?
- Who will use the results?
- What's the minimum information needed?
- How will data be analyzed?

**Example - Typhoon Damage Assessment:**
- **Purpose:** Document damage for recovery planning
- **Users:** Emergency management + community leadership
- **Minimum info:** Location, damage type, severity, photos
- **Analysis:** Damage map, repair priorities, cost estimates

### 2. Keep It Simple

**Do:**
- ✅ Ask only essential questions
- ✅ Use clear, plain language
- ✅ Provide helpful hints
- ✅ Test with actual users

**Don't:**
- ❌ Ask "nice to have" questions
- ❌ Use technical jargon
- ❌ Create multi-page surveys
- ❌ Include complex logic without testing

**Rule of Thumb:** If your survey takes more than 5 minutes in the field, it's too long.

### 3. Design for Your Audience

Consider: Technology comfort, language preferences, field conditions (cold, wet, gloves), time constraints

**For Community Members:** Large buttons, minimal typing, visual choices, offline capability

**For Technical Staff:** More detail acceptable, technical terms okay, advanced features

---

## Survey123 Web Designer

### Two Ways to Build Surveys

| Web Designer (Recommended) | Survey123 Connect (Advanced) |
|---------------------------|------------------------------|
| Browser-based | Desktop application |
| Drag-and-drop interface | XLSForm spreadsheet |
| Simple to moderate surveys | Complex surveys with logic |
| Easy to learn | Steeper learning curve |

### Access Web Designer

1. Go to **https://survey123.arcgis.com**
2. Sign in with ArcGIS Online credentials
3. Click **New survey** → **Blank survey**

---

## Essential Question Types

| Type | When to Use | Best Practices | Example |
|------|-------------|----------------|---------|
| **Single Line Text** | Names, IDs, brief notes | Set character limits; provide examples | "Your Name", "Equipment ID" |
| **Multiline Text** | Detailed descriptions | Use sparingly; 500 char max | "Additional Comments" |
| **Single Choice** | Select one from 2-7 options | Keep choices short; add "Other" | "Damage: Minor/Moderate/Severe" |
| **Multiple Choice** | Select multiple items | Limit to 10 choices max | "Utilities: Power/Water/Sewer" |
| **Dropdown** | Long lists (8+ options) | Alphabetize or prioritize common | "Building Type" (20+ options) |
| **Number** | Quantities, measurements | Set min/max; specify units | "Repair Cost ($)" |
| **Date/Time** | Event timing | Default to current | "Assessment Date" |
| **Geopoint (Map)** | **ALL field surveys** | **Required**; 10m accuracy | "Location of Damage" |
| **Image** | Photo documentation | 5 MB max; 3-5 photos | "Damage Photos" |

### Critical GPS Settings

For ALL field surveys:
- **Accuracy threshold:** 10 meters (5m for high-precision)
- **Display accuracy:** ✓ Enabled
- **Auto-capture:** ✓ Enabled
- **Samples to average:** 3
- **Required:** ✓ Yes

### Critical Photo Settings

For field documentation:
- **Maximum images:** 5
- **Maximum file size:** 5 MB
- **Image size:** Medium (1920px)
- **Required:** ✓ Yes
- **Hint:** "Take photos from multiple angles"

---

## Customizing Maps

### Why Customize?

**Default:** Basic basemap, world extent, no reference layers

**You want:** Village extent, infrastructure layers, traditional place names

### Steps

1. Click **Map** question → **More options** → **Map Settings**

2. **Set Default Extent:**
   - Search "Quinhagak, Alaska"
   - Zoom to appropriate level
   - Click "Set as default"
   
   OR use coordinates: Lat 59.7554, Long -161.8846, Zoom 14

3. **Choose Basemap:**
   - **Imagery:** Satellite photos (recommended for Alaska)
   - Streets, Topographic, or Light Gray Canvas

4. **Add Reference Layers:**
   - Click **Add Layer** → Choose source
   - Useful layers: Village infrastructure, property boundaries, subsistence areas
   - Set visibility, opacity, zoom levels

---

## Organization & Content Management

### Folder Structure

```
My Content/
├── Active Surveys/
│   ├── Infrastructure Inspections/
│   ├── Damage Assessments/
│   └── Subsistence Monitoring/
├── Survey Templates/
└── Archive/
```

**Create folders BEFORE publishing surveys!**

### Survey Components

When you publish, Survey123 creates three linked items:
1. **Survey (Form)** - The actual form
2. **Feature Layer** - Data storage
3. **Form Layer** - Backend connector

**Don't delete one without the others!**

### Naming Conventions

| Good ✓ | Bad ✗ |
|--------|-------|
| Quinhagak_Building_Inspection_2025 | Survey1 |
| Typhoon_Damage_Assessment_Oct2025 | Untitled |
| Erosion_Monitoring_Points_Annual | Test |

**Include:** Location + Purpose + Time period

### Tags and Metadata

**Always add:**
- **Tags:** Location, type, topic, year (e.g., Quinhagak, survey, infrastructure, 2025)
- **Summary:** One-sentence description
- **Description:** Purpose, users, instructions, contact

---

## Automated Notifications

### Use Cases

- ✅ Alert manager for critical damage
- ✅ Notify team when inspections complete
- ✅ Trigger follow-up for specific conditions
- ✅ Update stakeholders in real-time

### Setup Methods

**Method 1: Microsoft Power Automate (Recommended)**

1. Go to **https://flow.microsoft.com**
2. Create Flow: **When Survey123 response submitted**
3. Add action: **Send email**
4. Configure recipients, subject, body with survey fields

**Method 2: Survey123 Webhooks**

1. Survey Settings → **Webhooks** → **Add Webhook**
2. Enter Power Automate webhook URL
3. Set trigger: On add feature

### Best Practices

| Do ✓ | Don't ✗ |
|------|---------|
| Test thoroughly | Send for every submission |
| Use clear subjects | Include sensitive data in email |
| Trigger on conditions only | Spam people |
| Provide link to full response | Rely solely on email |

---

## Controlling Access

### Three Access Levels

| Level | Who Can See | Use For |
|-------|-------------|---------|
| **Private** | Only you | Testing, sensitive data |
| **Organization** | Your org members | Internal collaboration |
| **Public** | Anyone on internet | ⚠️ Rarely appropriate |

### Public Submission, Private Viewing

**Problem:** You want public to submit but NOT view others' responses.

**Solution:**

1. **Enable Public Submission:**
   - Survey Settings → Who can submit → **Everyone (public)**

2. **Restrict Data Viewing:**
   - ArcGIS Online → Feature Layer → Settings
   - ✓ Enable editing
   - ☐ Allow query (UNCHECK!)
   - Update: Only owner

### Fine-Grained Control with Groups

1. Create Group: "Building Inspectors"
2. Add authorized users
3. Share survey + feature layer with group (Edit access)
4. Public link: Submission only

### Protecting Sensitive Information

| Do ✓ | Don't ✗ |
|------|---------|
| Keep sensitive surveys private | Make sensitive data public |
| Use coded values vs. names | Include personal info in public surveys |
| Train collectors on sensitivity | Share raw data with unauthorized users |
| Audit permissions regularly | Assume defaults are secure |

---

## Common Mistakes to Avoid

| Mistake | Impact | Solution |
|---------|--------|----------|
| Too many questions | Low completion | Ask only what you'll use |
| Poor GPS config | Useless location data | Set 10m threshold |
| No photos | Can't verify later | Always include images |
| Unclear labels | Inconsistent data | Plain language + hints |
| No offline support | Can't collect remotely | Enable offline |
| Skip testing | Mid-project problems | Always pilot test |
| Public data exposure | Privacy violations | Careful permissions |

---

## Survey Design Checklist

### Before Building
- [ ] Purpose clearly defined
- [ ] Data users identified
- [ ] Questions list drafted
- [ ] Field conditions considered

### While Building
- [ ] Only essential questions
- [ ] GPS location (required)
- [ ] Photo capture included
- [ ] Appropriate question types
- [ ] Minimal required fields

### Before Publishing
- [ ] Tested in web preview
- [ ] Tested on mobile
- [ ] GPS: 10m accuracy threshold
- [ ] Photos: 5MB, 5 images max
- [ ] Maps configured

### After Publishing
- [ ] Downloaded to mobile app
- [ ] Shared with team
- [ ] Access permissions set
- [ ] Field workers trained

---

## Resources

### Official Documentation
- [Survey123 Basics](https://www.esri.com/training/catalog/62d6eb926373de7c095c3d35/arcgis-survey123-basics/) - Free ESRI course
- [Create Smart Surveys](https://www.esri.com/training/catalog/5e14de9636e7e15d09b53b62/create-smart-surveys-and-forms-using-arcgis-survey123/)
- [Survey123 Documentation](https://doc.arcgis.com/en/survey123/)

### Best Practices
- [6 Tips for Public Surveys](https://resources.esri.ca/getting-technical/6-tips-for-your-public-surveys-built-with-arcgis-survey123-2)
- [Limiting Access to Responses](https://www.esri.com/training/catalog/618ac4de4a893555070a7a39/limiting-access-to-public-survey123-responses/)

### Automation
- [Automate Email Notifications](https://www.esri.com/training/catalog/5c392a12dd8b97414e076ae8/automate-email-notifications-with-arcgis-survey123/)

---

## Next Steps

**Ready for hands-on practice?**

👉 [Activity 1: Create a Field Damage Assessment Survey](../activities/activity-01-survey-design.md)

Build a complete typhoon damage assessment survey, configure GPS/photos, test, publish, and collect field data.

📋 [Activity 1 Checklist](../activities/activity-01-checklist.md) - Track your progress

---

## Key Takeaways

1. **Good design** = Complete data + Happy users
2. **Keep it simple** - Essential questions only
3. **GPS + Photos** - Always required for field work
4. **Test thoroughly** - Before deployment
5. **Control access** - Protect sensitive data
6. **Automate wisely** - Critical notifications only
7. **Organize well** - Folders, naming, metadata

---

**Version:** 1.0  
**Last Updated:** October 2025  
**Study Time:** 90 minutes