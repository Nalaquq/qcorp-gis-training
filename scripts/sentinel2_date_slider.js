// Sentinel-2 Multi-Band Composite with Date Slider
//
// This script creates an RGB composite from Sentinel-2 imagery
// with an interactive date slider for selecting the time range
// and a band selector for exporting multiple bands.
//
// Instructions:
// 1. Draw a polygon on the map to define your area of interest (use the polygon drawing tool)
// 2. Use the two date sliders in the panel to select your start and end dates
// 3. Select which bands you want to export (RGB is selected by default)
// 4. Click "Run Analysis" to generate the composite
// 5. Check the Tasks tab to export to Google Drive

// Define all available bands organized by category
var bandDefinitions = {
  'True Color Image': [
    {name: 'TCI_R', description: 'True Color Red', resolution: '10m'},
    {name: 'TCI_G', description: 'True Color Green', resolution: '10m'},
    {name: 'TCI_B', description: 'True Color Blue', resolution: '10m'}
  ],
  'Visible & NIR': [
    {name: 'B2', description: 'Blue (496nm)', resolution: '10m'},
    {name: 'B3', description: 'Green (560nm)', resolution: '10m'},
    {name: 'B4', description: 'Red (665nm)', resolution: '10m'},
    {name: 'B8', description: 'NIR (835nm)', resolution: '10m'}
  ],
  'Red Edge': [
    {name: 'B5', description: 'Red Edge 1 (704nm)', resolution: '20m'},
    {name: 'B6', description: 'Red Edge 2 (740nm)', resolution: '20m'},
    {name: 'B7', description: 'Red Edge 3 (783nm)', resolution: '20m'},
    {name: 'B8A', description: 'Red Edge 4 (865nm)', resolution: '20m'}
  ],
  'SWIR': [
    {name: 'B11', description: 'SWIR 1 (1614nm)', resolution: '20m'},
    {name: 'B12', description: 'SWIR 2 (2202nm)', resolution: '20m'}
  ],
  'Atmospheric': [
    {name: 'B1', description: 'Aerosols (443nm)', resolution: '60m'},
    {name: 'B9', description: 'Water Vapor (945nm)', resolution: '60m'}
  ],
  'Level-2 Products': [
    {name: 'AOT', description: 'Aerosol Optical Thickness', resolution: '10m'},
    {name: 'WVP', description: 'Water Vapor Pressure', resolution: '10m'},
    {name: 'SCL', description: 'Scene Classification', resolution: '20m'}
  ]
};

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

// Function to get selected bands from checkboxes
function getSelectedBands(bandCheckboxes) {
  var selectedBands = [];
  for (var category in bandCheckboxes) {
    for (var i = 0; i < bandCheckboxes[category].length; i++) {
      var checkbox = bandCheckboxes[category][i];
      if (checkbox.getValue()) {
        selectedBands.push(checkbox.getLabel().split(' - ')[0]);
      }
    }
  }
  return selectedBands;
}

// Main analysis function
function runAnalysis(earliest, latest, statusLabel, bandCheckboxes) {
  // Get the current geometry from drawing tools
  var drawnGeometry = Map.drawingTools().layers().get(0).toGeometry();

  // Check if geometry exists and is not empty
  if (!drawnGeometry) {
    statusLabel.setValue('ERROR: Please draw a polygon on the map first!');
    statusLabel.style().set('color', 'red');
    return;
  }

  // Get selected bands
  var selectedBands = getSelectedBands(bandCheckboxes);

  // Check if at least one band is selected
  if (selectedBands.length === 0) {
    statusLabel.setValue('ERROR: Please select at least one band to export!');
    statusLabel.style().set('color', 'red');
    return;
  }

  // Update status
  statusLabel.setValue('Processing imagery with ' + selectedBands.length + ' band(s)...');
  statusLabel.style().set('color', 'blue');

  // Clear previous layers
  Map.layers().reset();

  var dataset = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
                    .filterDate(earliest, latest)
                    // Pre-filter to get less cloudy granules.
                    .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE',5))
                    .map(maskS2clouds);

  // Clip the composite images to the specified region.
  var composite = dataset.mean();
  var clippedComposite = composite.clip(drawnGeometry);

  // Visualization based on selected bands
  var selectedImage = clippedComposite.select(selectedBands);

  // Determine how to visualize based on number of selected bands
  if (selectedBands.length === 1) {
    // Single band - show as grayscale
    Map.addLayer(selectedImage, {min: 0, max: 0.3}, selectedBands[0] + ' (grayscale)');
  } else if (selectedBands.length === 2) {
    // Two bands - show first band as grayscale
    Map.addLayer(selectedImage.select([selectedBands[0]]), {min: 0, max: 0.3}, selectedBands[0] + ' (grayscale)');
  } else {
    // Three or more bands - show first 3 as RGB composite
    var visName = selectedBands[0] + ', ' + selectedBands[1] + ', ' + selectedBands[2];
    Map.addLayer(selectedImage, {
      bands: [selectedBands[0], selectedBands[1], selectedBands[2]],
      min: 0,
      max: 0.3
    }, visName + ' (RGB)');
  }

  // Update status
  statusLabel.setValue('✓ Composite added to map. Check Tasks tab to export.');
  statusLabel.style().set('color', 'green');

  // Determine the finest resolution among selected bands
  var exportScale = 10; // default to finest resolution
  var hasCoarseBands = false;
  for (var i = 0; i < selectedBands.length; i++) {
    var band = selectedBands[i];
    if (band === 'B1' || band === 'B9') {
      hasCoarseBands = true;
    }
  }

  // Export all selected bands
  var exportParams = {
    image: clippedComposite.select(selectedBands),
    description: 'Sentinel2_' + selectedBands.length + '_bands',
    scale: exportScale,
    region: drawnGeometry,
    fileFormat: 'GeoTIFF',
    maxPixels: 1e9
  };

  // Export the clipped composite to Google Drive.
  Export.image.toDrive(exportParams);
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
  value: '1. Draw a polygon on the map\n2. Set start and end dates below\n3. Select bands to export\n4. Click "Run Analysis"',
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

// Add separator
panel.add(ui.Panel({
  style: {
    height: '1px',
    backgroundColor: 'gray',
    margin: '10px 0'
  }
}));

// Band Selection Section
var bandSelectionLabel = ui.Label({
  value: 'Select Bands to Export:',
  style: {
    fontSize: '14px',
    fontWeight: 'bold',
    margin: '5px 0 5px 0'
  }
});
panel.add(bandSelectionLabel);

// Create band selection panel (scrollable)
var bandPanel = ui.Panel({
  style: {
    maxHeight: '250px',
    border: '1px solid lightgray',
    padding: '5px',
    margin: '5px 0'
  }
});

// Object to store all checkboxes by category
var bandCheckboxes = {};

// Add checkboxes for each category
for (var category in bandDefinitions) {
  // Category header
  var categoryLabel = ui.Label({
    value: category,
    style: {
      fontWeight: 'bold',
      fontSize: '12px',
      margin: '5px 0 2px 0',
      color: '#2c5aa0'
    }
  });
  bandPanel.add(categoryLabel);

  // Store checkboxes for this category
  bandCheckboxes[category] = [];

  // Add checkbox for each band in category
  var bands = bandDefinitions[category];
  for (var i = 0; i < bands.length; i++) {
    var band = bands[i];
    var isDefaultSelected = (band.name === 'TCI_R' || band.name === 'TCI_G' || band.name === 'TCI_B');

    var checkbox = ui.Checkbox({
      label: band.name + ' - ' + band.description + ' [' + band.resolution + ']',
      value: isDefaultSelected,
      style: {
        fontSize: '11px',
        margin: '1px 0 1px 10px'
      }
    });

    bandCheckboxes[category].push(checkbox);
    bandPanel.add(checkbox);
  }
}

panel.add(bandPanel);

// Add "Select All" and "Clear All" buttons
var buttonPanel = ui.Panel({
  layout: ui.Panel.Layout.flow('horizontal'),
  style: {
    margin: '5px 0'
  }
});

var selectAllButton = ui.Button({
  label: 'Select All',
  style: {
    fontSize: '11px',
    padding: '2px 5px',
    margin: '0 5px 0 0'
  },
  onClick: function() {
    for (var category in bandCheckboxes) {
      for (var i = 0; i < bandCheckboxes[category].length; i++) {
        bandCheckboxes[category][i].setValue(true);
      }
    }
  }
});

var clearAllButton = ui.Button({
  label: 'Clear All',
  style: {
    fontSize: '11px',
    padding: '2px 5px'
  },
  onClick: function() {
    for (var category in bandCheckboxes) {
      for (var i = 0; i < bandCheckboxes[category].length; i++) {
        bandCheckboxes[category][i].setValue(false);
      }
    }
  }
});

buttonPanel.add(selectAllButton);
buttonPanel.add(clearAllButton);
panel.add(buttonPanel);

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
    runAnalysis(earliest, latest, statusLabel, bandCheckboxes);
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
  value: 'Cloud coverage: < 5%\nResolution: 10m-60m (band dependent)\nExport: Selected bands as multi-band GeoTIFF',
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
