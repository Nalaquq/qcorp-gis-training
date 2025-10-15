# Activity 1: Create a Field Damage Assessment Survey

**Module:** 02 - Field Data Collection  
**Activity Type:** Hands-on Practice  
**Duration:** 75 minutes  
**Difficulty:** Beginner  
**Prerequisites:** Lesson 1 completed, ArcGIS Online account access

---

## Activity Overview

In this activity, you will create a complete damage assessment survey that can be used to document typhoon damage in Quinhagak. You'll design the survey using the web-based Survey123 designer, test it, publish it to ArcGIS Online, and collect practice data in the field.

### What You'll Build

A mobile survey form for documenting:
- GPS locations of damaged sites
- Photos of damage
- Basic categorization of damage type
- Date, time, and surveyor information

### Real-World Application

This same workflow can be used for:
- Future storm damage assessments
- Erosion monitoring
- Infrastructure inspections
- Subsistence resource documentation

---

## Learning Objectives

By completing this activity, you will be able to:

✅ Create a simple survey using Survey123 web designer  
✅ Configure GPS location capture  
✅ Add photo capture capability  
✅ Implement dropdown menus for damage categories  
✅ Publish a survey to ArcGIS Online  
✅ Download and use the survey on mobile device  
✅ Collect field data with GPS locations  
✅ Sync data back to ArcGIS Online

---

## Materials Needed

### Software
- [ ] Web browser (Chrome, Firefox, or Edge recommended)
- [ ] Survey123 app (mobile device)
- [ ] ArcGIS Online account (Creator or Field Worker license)

### Hardware
- [ ] Computer with internet connection
- [ ] Smartphone or tablet (iOS or Android)
- [ ] Emlid Reach RS3 (optional, for higher accuracy)
- [ ] Charged batteries for mobile device

---

## Part 1: Design Your Survey (20 minutes)

### Step 1: Access Survey123 Web Designer

1. Open your web browser
2. Navigate to **https://survey123.arcgis.com**
3. Sign in with your ArcGIS Online credentials
4. Click **New survey** button
5. Select **Blank survey**

### Step 2: Create New Survey

1. Survey title: `Quinhagak Typhoon Damage Assessment (2025)`
2. Tags: Add `typhoon, damage, infrastructure, Quinhagak, 2025`
3. Summary: "Field survey for documenting infrastructure and subsistence area damage from October 2025 typhoon"
4. Folder: Select or create "Disaster Response" folder
5. Click **Create**

**⚠️ Important:** The survey title will be visible to users. Survey names are auto-generated based on the title.

### Step 3: Configure Survey Settings

Before building your form, click the **Settings** tab (gear icon):

**General:**
- Enable **Allow multiple submissions per device**
- Enable **Store data in an existing feature layer**: No (leave unchecked)

**Appearance:**
- Theme color: Blue
- Logo: Upload Quinhagak logo if available

**Map:**
- Basemap: Streets or Imagery
- Default extent: Quinhagak area

### Step 4: Build Your Survey Form

Click the **Design** tab to start adding questions. You'll create a simple 6-question survey.

**Question 1: Respondent Name**
- Click **Add** → **Single line text**
- Label: `Your Name`
- Hint: "Enter first and last name"
- Required: ✓ Yes

**Question 2: Survey Date & Time**
- Click **Add** → **Date Time**
- Label: `Date Time"
- Default value: Select **Today's date**
- Required: ✓ Yes

**Question 3: Location**
- Click **Add** → **Map** (geopoint)
- Label: `Location of Damage`
- Required: ✓ Yes
- Click **More options** (three dots):
  - Location accuracy: 10 meters
  - Enable **Show location button**
  - Enable **Show accuracy**

**Question 4: Damage Photos**
- Click **Add** → **Image**
- Label: `Photos`
- Description: "Take photos showing the damage"
- Maximum number of images: 5
- Required: ✓ Yes
- Click **More options**:
  - Image size: Medium (1920px)
  - Maximum file size: 5 MB

**Question 5: Type of Damage**
- Click **Add** → **Dropdown**
- Label: `What was damaged?`
- Required: ✓ Yes
- Add these choices (click **Add choice** for each):
  - Airport/Airstrip
  - Building (home)
  - Building (public)
  - Boat/Dock
  - Fish rack/Drying rack
  - Road/Trail
  - Subsistence area (berry patch, hunting area)
  - Utilities (power, water, fuel)
  - Other

That's it! Your survey is complete with 6 essential questions.

### Step 5: Customize Survey Appearance (Optional)

Click the **Appearance** settings:

1. **Add a header image:**
   - Click the paint brush icon at top
   - Upload Quinhagak logo or relevant photo (if available)
   - Set header style to **Large**

2. **Add instructions:**
   - At the top, click **Add** → **Note**
   - Add text: "Document typhoon damage by taking photos and marking locations. Make sure GPS accuracy is good before submitting."

3. **Choose theme color:**
   - Select a color that represents your community

---

## Part 2: Configure Advanced Settings (10 minutes)

### GPS Accuracy Configuration

For the GPS location question (Question 4):
1. Click the question to select it
2. Click **More options** (three dots)
3. Under **Validation**:
   - Location accuracy: 10 meters
   - Enable **Display accuracy on map**
4. Under **Behavior**:
   - Enable **Automatically capture location**
   - Number of location samples to average: 3

### Photo Settings

For the photos question (Question 5):
1. Click the question
2. Click **More options**
3. Verify settings:
   - Image size: Medium (1920px) - reduces file size
   - Maximum file size: 5 MB
   - Maximum number of images: 5

That's it! Your survey is configured and ready to test.

---

## Part 3: Test Your Survey (10 minutes)

### Web Preview

1. Click **Preview** button (eye icon at top right)
2. This opens your survey in a new browser tab
3. Fill out the entire form with test data

### Test with Sample Scenario

**Scenario:** Red Building has roof damage from typhoon

Fill out the preview:
- Your Name: [Your name]
- Date: Today's date
- Time: Current time
- Location of Damage: Click on map to place point (use approximate Quinhagak location)
- Photos: Upload 1-2 test photos from your computer (any photos for testing)
- What was damaged?: Building (public)

**Do NOT submit** this test data - just verify everything works correctly.

### Verification Checklist

Confirm in preview:
- [ ] All 6 questions display correctly
- [ ] Required fields are marked with red asterisk
- [ ] Date defaults to today
- [ ] Time defaults to current time
- [ ] GPS map is interactive and allows clicking
- [ ] Photo upload button works
- [ ] Dropdown shows all damage type choices

Take screenshot of completed preview for your records.

---

## Part 4: Publish Survey (10 minutes)

### Publishing Steps

1. Click **Publish** button (top right)
2. Review the publish dialog:
   - Feature layer will be created
   - Survey will be available in mobile app
   - Link will be generated
3. Click **Publish** to confirm
4. Wait for "Successfully published" message (usually 10-30 seconds)

### Get Survey Link

After publishing:
1. Click **Collaborate** tab
2. Copy the **Survey link** - you'll need this
3. Note the QR code - useful for sharing

### Verify in ArcGIS Online

1. Open a new browser tab
2. Navigate to **https://arcgis.com**
3. Sign in and go to **Content**
4. Find your survey items (there will be multiple):
   - Survey (form)
   - Feature layer (for data storage)
   - Form layer
5. Click the Feature Layer to verify fields are present

---

## Part 5: Download to Mobile Device (10 minutes)

### Install Survey123 App

If not already installed:
- **iOS:** Download from App Store
- **Android:** Download from Google Play Store

### Download Your Survey

1. Open **Survey123 app**
2. Sign in with same ArcGIS Online account
3. You should see your survey in the list
4. If not visible, tap **Download surveys** and search for it
5. Tap **Download** next to your survey
6. Wait for "Ready to collect" status

### Configure Offline Settings

1. Tap your survey to open it
2. Tap **Settings** (gear icon)
3. Enable **Collect in Inbox** - this allows collecting data without internet
4. Set **Download area**: Can download map tiles for offline use
5. Return to survey list

---

## Part 6: Field Data Collection Practice (30 minutes)

### Safety First

Before going outside:
- [ ] Check weather conditions
- [ ] Dress appropriately for weather
- [ ] Ensure phone/tablet is fully charged
- [ ] Bring paper backup sheet (in case of technical issues)
- [ ] Go with partner for safety

### Collection Sites

Collect data at **3 practice locations** around your area:

**Practice Site 1: Any Building**
- Find any building or structure
- Take 2-3 photos from different angles
- Select appropriate damage category (or "Other" for practice)

**Practice Site 2: Infrastructure**
- Road, trail, walkway, dock, or airstrip area
- Take 2-3 photos showing the feature
- Practice using the dropdown menu

**Practice Site 3: Open/Subsistence Area**
- Natural area, berry patch, or open space
- Take 2-3 photos
- Practice GPS accuracy

### Collection Best Practices

For each site:

1. **Approach the location**
   - Get as close as safely possible
   - Clear view of sky for better GPS signal

2. **Wait for GPS accuracy**
   - Open the survey and start new record
   - Watch the location accuracy indicator
   - Wait until accuracy is <10 meters (preferably <5 meters)

3. **Take photos first**
   - Tap the photo question
   - Take 2-3 clear photos
   - Multiple angles showing the location
   - Make sure photos are in focus

4. **Fill out form**
   - Enter your name
   - Verify date and time
   - Confirm GPS location looks correct on map
   - Select damage type from dropdown

5. **Review and save**
   - Scroll through entire form
   - Check all required fields are complete
   - Verify photos uploaded
   - Tap **Submit** button

6. **Watch for confirmation**
   - "Sent successfully" or "Saved to outbox"
   - Return to survey list

---

## Part 7: Data Synchronization (10 minutes)

### If You Have Internet Connection

Data syncs automatically when you save if connected:
1. Open Survey123 app
2. Tap **Inbox** or **Outbox** tab
3. Should show sent records or be empty if all synced
4. If any show "Error", tap to retry sending

### If Working Offline

1. Connect to Wi-Fi or enable cellular data
2. Open Survey123 app
3. Tap **Outbox** tab
4. Tap **Send** button (if present)
5. Wait for all records to sync
6. Verify "Sent" status on all records

### Verify Data in ArcGIS Online

1. Open web browser
2. Go to **https://survey123.arcgis.com**
3. Sign in to your account
4. Find your survey in the list
5. Click **Data** tab
6. You should see your 3 practice records
7. Click **Open in Map Viewer** to see points on map
8. Click each point to view attributes and photos

**Alternative viewing:**
- Go to ArcGIS Online **Content**
- Open your survey's feature layer
- Click **Open in Map Viewer**

---

## Deliverables

### What to Submit

Create a folder called `Activity_01_[YourLastName]` containing:

1. **Survey Link**
   - File: `survey_link.txt`
   - Content: Your published survey URL

2. **Screenshots** (PNG or JPG):
   - `screenshot_01_survey_design.png` - Survey123 web designer showing all questions
   - `screenshot_02_mobile_app.png` - Survey open in mobile app
   - `screenshot_03_data_table.png` - Data tab showing your 3 records
   - `screenshot_04_map_view.png` - Your 3 points in ArcGIS Online map

3. **Field Photos**
   - 2-3 photos from each collection site (6-9 total)
   - Named: `site1_photo1.jpg`, `site1_photo2.jpg`, etc.

4. **Completed Worksheet**
   - `activity_01_worksheet_completed.pdf`

5. **Reflection Document** 
   - See reflection questions below

### Submission

Upload your folder to:
- Google Drive shared folder, OR
- Submit via email to training team, OR
- Upload to designated submission platform

**Due Date:** TBD

---

## Reflection Questions

Prepare to answer the following reflection questions at our next meeting:

### Technical Reflection

1. What challenges did you encounter while designing the survey in the web interface?
2. How did GPS accuracy affect your data collection? Did you need to wait long for good accuracy?
3. Was it easy to take photos and upload them? What would you change about the photo process?

### Application Reflection

4. What additional information would be helpful to collect for real damage assessment in Quinhagak?
5. What are the advantages of mobile data collection compared to paper forms for damage assessment?
6. How could community members use this survey data to make decisions about repairs or recovery?

### Future Planning

7. What other types of simple surveys would be useful for your community (erosion, subsistence, infrastructure)?
8. Would you feel comfortable teaching this process to other community members?
9. What support would you need to use this survey in a real emergency situation?

---

## Assessment Rubric

Your activity will be evaluated on:

| Criteria | Points | Description |
|----------|--------|-------------|
| **Survey Design** | 25 | All 6 required fields included, appropriate field types, proper GPS and photo settings |
| **Data Quality** | 25 | Complete records, accurate GPS (<10m), clear photos, detailed descriptions |
| **Technical Execution** | 20 | Successfully published, synced data visible online, proper workflow followed |
| **Documentation** | 15 | All deliverables submitted, screenshots clear and complete, organized folder structure |
| **Reflection** | 15 | Thoughtful answers with specific examples, demonstrates learning, considers community application |
| **TOTAL** | 100 | |

**Grading Scale:**
- 90-100: Excellent - Ready for real deployment
- 80-89: Good - Minor improvements needed
- 70-79: Satisfactory - Needs practice
- Below 70: Needs Improvement - Requires additional support

---

## Common Issues and Solutions

### Issue: GPS Won't Lock or Accuracy Stays Poor

**Symptoms:** Location accuracy stays above 50m or won't update

**Solutions:**
- Move away from buildings, trees, and power lines
- Wait longer (initial GPS lock can take 2-5 minutes)
- Check that device Location Services are enabled in system settings
- Ensure Survey123 app has location permissions
- Restart the Survey123 app
- Try toggling airplane mode on/off
- As last resort, manually place point on map

### Issue: Photos Won't Attach or Upload

**Symptoms:** Camera opens but photo doesn't appear in form

**Solutions:**
- Check that Survey123 has camera permissions in system settings
- Verify available storage space on device
- Try taking smaller/lower resolution photos
- If offline, photos will upload when you sync - be patient
- Check file size limit (5MB per photo)

### Issue: Survey Not Appearing in Mobile App

**Symptoms:** Can't find survey in download list

**Solutions:**
- Verify you're signed into the correct ArcGIS Online account
- Check that survey was published successfully (go to survey123.arcgis.com)
- Pull down to refresh the survey list in app
- Sign out and sign back in
- Check that survey sharing settings allow your account to access it

### Issue: Data Not Syncing from Outbox

**Symptoms:** Records stuck in outbox, won't send

**Solutions:**
- Verify strong internet connection (Wi-Fi preferred)
- Check that ArcGIS Online is accessible (open in browser)
- Try sending one record at a time
- Check for error messages on individual records
- Verify your account has edit permissions on the feature layer
- Try signing out and back in

### Issue: Required Fields Allow Submission

**Symptoms:** Can submit incomplete forms

**Solutions:**
- In web designer, verify "Required" is toggled on for each field
- Republish the survey after making changes
- In mobile app, delete the old survey and re-download
- Force refresh by signing out and back in

### Issue: Conditional Logic Not Working

**Symptoms:** Questions show or hide unexpectedly

**Solutions:**
- This simplified survey doesn't use conditional logic
- If you add rules later, check question name matching
- Verify rule syntax in web designer
- Republish and re-download survey after changes

---

## Extension Activities

### For Advanced Learners

If you complete the basic activity early, try these enhancements:

1. **Add More Questions**
   - Add a text field for detailed damage description
   - Add severity level (minor, moderate, severe)
   - Add estimated repair cost field
   - Add conditional logic (show follow-up questions based on damage type)

2. **Create a Dashboard**
   - Go to ArcGIS Online
   - Create a dashboard showing:
     - Map of damage locations
     - Chart showing count by damage type
     - Summary statistics

3. **Add Survey123 Website**
   - Enable web form for data entry
   - Customize appearance
   - Test browser-based data collection
   - Compare to mobile app experience

4. **Export and Analyze Data**
   - Download data as CSV or Excel
   - Create summary statistics in spreadsheet
   - Count damages by category
   - Map patterns in damage locations

5. **Create a Story Map**
   - Build a story map using your collected data
   - Add narrative about damage assessment process
   - Include photos and maps
   - Share with community

---

## Additional Resources

### Online Help
- **Survey123 Documentation:** https://doc.arcgis.com/en/survey123/
- **Survey123 Community Forum:** https://community.esri.com/t5/survey123/ct-p/survey123
- **ArcGIS Online Help:** https://doc.arcgis.com/en/arcgis-online/

### Video Tutorials
- [Survey123 Web Designer Quick Start](https://www.youtube.com/c/survey123)
- [Field Data Collection Best Practices](https://www.esri.com/training)

### Templates
- Browse Survey123 gallery for more templates
- Access sample surveys in Survey123 website
- Check Esri's Living Atlas for field survey examples

### Community Support
- [Troubleshooting Guide](../troubleshooting/README.md)
- [Training Discussion Forum](https://github.com/Nalaquq/qcorp-gis-training/discussions)
- [Create an Issue](https://github.com/Nalaquq/qcorp-gis-training/issues/new)

---

## Completion Checklist

Before submitting, verify you have:

- [ ] Created survey with all 6 required questions
- [ ] Configured GPS accuracy to 10m threshold
- [ ] Set photo limit to 5 images
- [ ] Successfully published to ArcGIS Online
- [ ] Downloaded survey to mobile device
- [ ] Collected 3 complete practice records
- [ ] Synced all data to ArcGIS Online
- [ ] Verified data appears in Data tab and map viewer
- [ ] Taken all 4 required screenshots
- [ ] Saved 6-9 field photos with proper naming
- [ ] Organized all deliverables in properly named folder
- [ ] Completed reflection questions (1-2 pages)
- [ ] Submitted by deadline

---

## Next Steps

After completing this activity:

✨ **Continue to:** [Activity 2: Offline Map Preparation](./activity-02-offline-maps.md)

📚 **Review:** [Lesson 1: Survey Design Fundamentals](../lessons/01-survey-design.md)

🎯 **Practice:** Create a survey for your own work needs or community project

💬 **Share:** Discuss your experience with other learners in the forum

---

**Activity Version:** 2.0 (Survey123 Web Designer - Simplified)  
**Last Updated:** October 2025  
**Estimated Completion Time:** 75 minutes  
**Interface:** Survey123 Web Designer (browser-based)  
**Instructor:** Nalaquq Training Team

---

## Instructor Notes

### Preparation Needed
- Verify all students have ArcGIS Online Creator accounts
- Test the simplified 6-question survey creation beforehand
- Scout and mark practice collection sites
- Prepare backup mobile devices
- Have paper forms ready as backup

### Common Student Challenges
- Understanding GPS accuracy requirements and waiting for good signal
- Taking clear, useful photos
- Managing photo file sizes on device
- Confusion about when data syncs (online vs offline)
- Finding published surveys in ArcGIS Online Content

### Teaching Tips
- Emphasize that simple surveys are often better for rapid data collection
- Demonstrate entire workflow before students begin
- Encourage students to work in pairs for field collection
- Show the importance of good photo documentation
- Discuss how to expand this simple survey later if needed
- Allow extra time for first-time mobile GPS collection
- Have students verify data in ArcGIS Online together as a group

### Technology Contingencies
- Have offline paper forms pre-printed with the 6 questions
- Prepare loaner devices with Survey123 pre-installed
- Know locations with reliable Wi-Fi for syncing
- Have backup survey already created for demonstration

### Assessment Focus
- Survey completeness (all 6 questions present and configured correctly)
- Data quality (GPS accuracy, photo clarity, appropriate categorization)
- Ability to troubleshoot common issues independently
- Understanding of basic workflow from design to data viewing

### Expansion Ideas
Students who finish early can be challenged to add more questions to make the survey more detailed, or create a completely different survey for another community need.

