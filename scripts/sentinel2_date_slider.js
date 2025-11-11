// Sentinel-2 RGB Composite with Date Slider
//
// This script creates an RGB composite from Sentinel-2 imagery
// with an interactive date slider for selecting the time range.
//
// Instructions:
// 1. Draw a polygon on the map to define your area of interest (use the polygon drawing tool)
// 2. Use the two date sliders in the panel to select your start and end dates
// 3. Click "Run Analysis" to generate the composite
// 4. Check the Tasks tab to export to Google Drive

// Cloud masking function
function maskS2clouds(image) {
  var qa = image.select('QA60');

  // Bits 10 and 11 are clouds and cirrus, respectively.
  var cloudBitMask = 1 << 10;
  var cirrusBitMask = 1 << 11;

  // Both flags should be set to zero, indicating clear conditions.
  var mask = qa.bitwiseAnd(cloudBitMask).eq(0)
      .and(qa.bitwiseAnd(cirrusBitMask).eq(0));

  return image.updateMask(mask).divide(10000);
}

// Main analysis function
function runAnalysis(earliest, latest, statusLabel) {
  // Get the current geometry from drawing tools
  var drawnGeometry = Map.drawingTools().layers().get(0).toGeometry();

  // Check if geometry exists and is not empty
  if (!drawnGeometry) {
    statusLabel.setValue('ERROR: Please draw a polygon on the map first!');
    statusLabel.style().set('color', 'red');
    return;
  }

  // Update status
  statusLabel.setValue('Processing imagery...');
  statusLabel.style().set('color', 'blue');

  // Clear previous layers
  Map.layers().reset();

  var dataset = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
                    .filterDate(earliest, latest)
                    // Pre-filter to get less cloudy granules.
                    .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE',5))
                    .map(maskS2clouds);

  // Clip the RGB composite images to the specified region.
  var composite = dataset.mean();
  var clippedComposite = composite.clip(drawnGeometry);

  var visualization = {
    bands: ['TCI_R', 'TCI_G', 'TCI_B'],
  };

  Map.setCenter(-161.90402886481778, 59.750359237437635, 10);

  Map.addLayer(clippedComposite, visualization, 'RGB Composite');

  // Update status
  statusLabel.setValue('✓ Composite added to map. Check Tasks tab to export.');
  statusLabel.style().set('color', 'green');

  // Define the export parameters
  var RGBexportParams = {
    image: clippedComposite.select(['TCI_R', 'TCI_G', 'TCI_B']),
    description: 'RGB_Sentinel2',
    scale: 10, // set the scale in meters
    region: drawnGeometry,
    fileFormat: 'GeoTIFF',
  };

  // Export the clipped composite to Google Drive.
  Export.image.toDrive(RGBexportParams);
}

// Create UI Panel
var panel = ui.Panel({
  style: {
    width: '350px',
    position: 'top-left',
    padding: '8px'
  }
});

// Add title
var title = ui.Label({
  value: 'Sentinel-2 Image Composite',
  style: {
    fontSize: '20px',
    fontWeight: 'bold',
    margin: '0 0 10px 0'
  }
});
panel.add(title);

// Add instructions
var instructions = ui.Label({
  value: '1. Draw a polygon on the map\n2. Set start and end dates below\n3. Click "Run Analysis"',
  style: {
    fontSize: '13px',
    margin: '0 0 10px 0',
    whiteSpace: 'pre'
  }
});
panel.add(instructions);

// Add separator
panel.add(ui.Panel({
  style: {
    height: '1px',
    backgroundColor: 'gray',
    margin: '10px 0'
  }
}));

// Start Date Section
var startDateLabel = ui.Label({
  value: 'Start Date:',
  style: {
    fontSize: '14px',
    fontWeight: 'bold',
    margin: '5px 0 2px 0'
  }
});
panel.add(startDateLabel);

var startDateSlider = ui.DateSlider({
  start: '2020-01-01',
  end: Date.now(),
  value: '2024-05-01',
  period: 1,
  style: {
    stretch: 'horizontal'
  }
});
panel.add(startDateSlider);

// End Date Section
var endDateLabel = ui.Label({
  value: 'End Date:',
  style: {
    fontSize: '14px',
    fontWeight: 'bold',
    margin: '10px 0 2px 0'
  }
});
panel.add(endDateLabel);

var endDateSlider = ui.DateSlider({
  start: '2020-01-01',
  end: Date.now(),
  value: '2024-10-30',
  period: 1,
  style: {
    stretch: 'horizontal'
  }
});
panel.add(endDateSlider);

// Status label
var statusLabel = ui.Label({
  value: 'Ready. Draw a polygon and click Run Analysis.',
  style: {
    fontSize: '12px',
    color: 'gray',
    margin: '10px 0',
    whiteSpace: 'pre-wrap'
  }
});
panel.add(statusLabel);

// Run button
var runButton = ui.Button({
  label: '▶ Run Analysis',
  style: {
    stretch: 'horizontal',
    margin: '5px 0'
  },
  onClick: function() {
    var earliest = ee.Date(startDateSlider.getValue()[0]);
    var latest = ee.Date(endDateSlider.getValue()[0]);
    runAnalysis(earliest, latest, statusLabel);
  }
});
panel.add(runButton);

// Add info section
panel.add(ui.Panel({
  style: {
    height: '1px',
    backgroundColor: 'gray',
    margin: '10px 0'
  }
}));

var infoLabel = ui.Label({
  value: 'Cloud coverage: < 5%\nResolution: 10m\nBands: RGB (Natural Color)',
  style: {
    fontSize: '11px',
    color: 'gray',
    whiteSpace: 'pre'
  }
});
panel.add(infoLabel);

// Add panel to map
ui.root.insert(0, panel);

// Set initial map center
Map.setCenter(-161.90402886481778, 59.750359237437635, 10);
