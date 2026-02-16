// Landsat Monthly Water Mask Generator
//
// This script generates monthly multiband rasters and NIR-based binary water masks
// from Landsat imagery for a user-defined area and date range.
//
// Supported Sensors:
//   Landsat 5 TM (1984-2012), Landsat 7 ETM+ (1999-2024),
//   Landsat 8 OLI (2013-present), Landsat 9 OLI-2 (2021-present)
//
// Instructions:
// 1. Draw a polygon on the map to define your area of interest
// 2. Set start and end dates using the sliders
// 3. Enter a filename prefix for exported files
// 4. Click "Query Imagery" to see available images
// 5. Adjust the NIR threshold to fine-tune water detection
// 6. Click "Generate Monthly Masks" to create exports for each month
// 7. Check the Tasks tab to run the exports to Google Drive
//
// Author: Nalaquq LLC / QCORP GIS Training
// Date: February 2026

// ============================================================
// Landsat Sensor Configuration
// Collection 2 Level 2 Surface Reflectance
// ============================================================

var LANDSAT_SENSORS = {
  'L5': {
    collection: 'LANDSAT/LT05/C02/T1_L2',
    startYear: 1984,
    endYear: 2012,
    bands: ['SR_B1', 'SR_B2', 'SR_B3', 'SR_B4', 'SR_B5', 'SR_B7'],
    commonNames: ['Blue', 'Green', 'Red', 'NIR', 'SWIR1', 'SWIR2'],
    name: 'Landsat 5 TM'
  },
  'L7': {
    collection: 'LANDSAT/LE07/C02/T1_L2',
    startYear: 1999,
    endYear: 2024,
    bands: ['SR_B1', 'SR_B2', 'SR_B3', 'SR_B4', 'SR_B5', 'SR_B7'],
    commonNames: ['Blue', 'Green', 'Red', 'NIR', 'SWIR1', 'SWIR2'],
    name: 'Landsat 7 ETM+'
  },
  'L8': {
    collection: 'LANDSAT/LC08/C02/T1_L2',
    startYear: 2013,
    endYear: 2099,
    bands: ['SR_B2', 'SR_B3', 'SR_B4', 'SR_B5', 'SR_B6', 'SR_B7'],
    commonNames: ['Blue', 'Green', 'Red', 'NIR', 'SWIR1', 'SWIR2'],
    name: 'Landsat 8 OLI'
  },
  'L9': {
    collection: 'LANDSAT/LC09/C02/T1_L2',
    startYear: 2021,
    endYear: 2099,
    bands: ['SR_B2', 'SR_B3', 'SR_B4', 'SR_B5', 'SR_B6', 'SR_B7'],
    commonNames: ['Blue', 'Green', 'Red', 'NIR', 'SWIR1', 'SWIR2'],
    name: 'Landsat 9 OLI-2'
  }
};

// ============================================================
// Cloud Masking & Scaling Functions
// ============================================================

// Mask clouds and cloud shadows using QA_PIXEL band
// Bit 3 = cloud, Bit 4 = cloud shadow
function maskCloudsLandsat(image) {
  var qa = image.select('QA_PIXEL');
  var cloudBit = 1 << 3;
  var shadowBit = 1 << 4;
  var mask = qa.bitwiseAnd(cloudBit).eq(0)
      .and(qa.bitwiseAnd(shadowBit).eq(0));
  return image.updateMask(mask);
}

// Apply Collection 2 Level 2 surface reflectance scaling
// SR = pixel_value * 0.0000275 - 0.2
function applyScaleFactors(image) {
  var optical = image.select(['Blue', 'Green', 'Red', 'NIR', 'SWIR1', 'SWIR2']);
  var scaled = optical.multiply(0.0000275).add(-0.2);
  return image.addBands(scaled, null, true);
}

// Create harmonization function for a specific sensor
function makeHarmonizer(sensorKey) {
  var sensor = LANDSAT_SENSORS[sensorKey];
  return function(image) {
    var harmonized = maskCloudsLandsat(image);
    harmonized = harmonized.select(sensor.bands, sensor.commonNames);
    harmonized = applyScaleFactors(harmonized);
    return harmonized;
  };
}

// ============================================================
// Collection Auto-Selection
// ============================================================

// Given a date range and geometry, return a merged harmonized collection
// and the list of sensor names used
function getLandsatCollection(startDate, endDate, geometry, maxCloud) {
  var startYear = ee.Date(startDate).get('year').getInfo();
  var endYear = ee.Date(endDate).get('year').getInfo();
  var collections = [];
  var sensorsUsed = [];

  var sensorKeys = ['L5', 'L7', 'L8', 'L9'];
  for (var i = 0; i < sensorKeys.length; i++) {
    var key = sensorKeys[i];
    var sensor = LANDSAT_SENSORS[key];

    if (startYear <= sensor.endYear && endYear >= sensor.startYear) {
      var col = ee.ImageCollection(sensor.collection)
          .filterDate(startDate, endDate)
          .filterBounds(geometry)
          .filter(ee.Filter.lt('CLOUD_COVER', maxCloud))
          .map(makeHarmonizer(key));
      collections.push(col);
      sensorsUsed.push(sensor.name);
    }
  }

  if (collections.length === 0) {
    return {collection: null, sensors: []};
  }

  var merged = collections[0];
  for (var j = 1; j < collections.length; j++) {
    merged = merged.merge(collections[j]);
  }

  return {collection: merged, sensors: sensorsUsed};
}

// ============================================================
// Spectral Indices
// ============================================================

// All indices use the harmonized band names: Blue, Green, Red, NIR, SWIR1, SWIR2

var INDEX_DEFINITIONS = {

  // --- Vegetation Health & Biomass ---

  'NDVI': {
    name: 'NDVI',
    description: 'Normalized Difference Vegetation Index — biomass, greenness',
    compute: function(img) {
      return img.normalizedDifference(['NIR', 'Red']).rename('NDVI');
    }
  },
  'EVI': {
    name: 'EVI',
    description: 'Enhanced Vegetation Index — corrects atmospheric/canopy effects',
    compute: function(img) {
      // EVI = 2.5 * (NIR - Red) / (NIR + 6*Red - 7.5*Blue + 1)
      var nir = img.select('NIR');
      var red = img.select('Red');
      var blue = img.select('Blue');
      return nir.subtract(red).multiply(2.5)
          .divide(nir.add(red.multiply(6)).subtract(blue.multiply(7.5)).add(1))
          .rename('EVI');
    }
  },
  'GNDVI': {
    name: 'GNDVI',
    description: 'Green NDVI — nitrogen status, chlorophyll',
    compute: function(img) {
      // GNDVI = (NIR - Green) / (NIR + Green)
      return img.normalizedDifference(['NIR', 'Green']).rename('GNDVI');
    }
  },
  'SAVI': {
    name: 'SAVI',
    description: 'Soil-Adjusted Vegetation Index — sparse vegetation',
    compute: function(img) {
      // SAVI = 1.5 * (NIR - Red) / (NIR + Red + 0.5)
      var nir = img.select('NIR');
      var red = img.select('Red');
      return nir.subtract(red).multiply(1.5)
          .divide(nir.add(red).add(0.5))
          .rename('SAVI');
    }
  },
  'MSAVI': {
    name: 'MSAVI',
    description: 'Modified SAVI — minimizes soil noise',
    compute: function(img) {
      // MSAVI = (2*NIR + 1 - sqrt((2*NIR+1)^2 - 8*(NIR-Red))) / 2
      var nir = img.select('NIR');
      var red = img.select('Red');
      var twoNirPlusOne = nir.multiply(2).add(1);
      return twoNirPlusOne
          .subtract(twoNirPlusOne.pow(2).subtract(nir.subtract(red).multiply(8)).sqrt())
          .divide(2)
          .rename('MSAVI');
    }
  },
  'CIG': {
    name: 'CIG',
    description: 'Chlorophyll Index Green — leaf chlorophyll content',
    compute: function(img) {
      // CIG = (NIR / Green) - 1
      return img.select('NIR').divide(img.select('Green')).subtract(1).rename('CIG');
    }
  },
  'VARI': {
    name: 'VARI',
    description: 'Visible Atmospherically Resistant Index — visual greenness',
    compute: function(img) {
      // VARI = (Green - Red) / (Green + Red - Blue)
      var green = img.select('Green');
      var red = img.select('Red');
      var blue = img.select('Blue');
      return green.subtract(red)
          .divide(green.add(red).subtract(blue))
          .rename('VARI');
    }
  },
  'ARVI': {
    name: 'ARVI',
    description: 'Atmospherically Resistant Vegetation Index',
    compute: function(img) {
      // ARVI = (NIR - (2*Red - Blue)) / (NIR + (2*Red - Blue))
      var nir = img.select('NIR');
      var red = img.select('Red');
      var blue = img.select('Blue');
      var rb = red.multiply(2).subtract(blue);
      return nir.subtract(rb).divide(nir.add(rb)).rename('ARVI');
    }
  },

  // --- Water ---

  'NDWI': {
    name: 'NDWI',
    description: 'Normalized Difference Water Index — water stress, moisture',
    compute: function(img) {
      return img.normalizedDifference(['Green', 'NIR']).rename('NDWI');
    }
  },
  'MNDWI': {
    name: 'MNDWI',
    description: 'Modified NDWI — better water/built-up separation',
    compute: function(img) {
      return img.normalizedDifference(['Green', 'SWIR1']).rename('MNDWI');
    }
  },

  // --- Burn / Disturbance ---

  'NBR': {
    name: 'NBR',
    description: 'Normalized Burn Ratio — fire severity, vegetation disturbance',
    compute: function(img) {
      return img.normalizedDifference(['NIR', 'SWIR2']).rename('NBR');
    }
  },

  // --- Soil / Moisture ---

  'BSI': {
    name: 'BSI',
    description: 'Bare Soil Index — exposed soil detection',
    compute: function(img) {
      // BSI = ((SWIR1 + Red) - (NIR + Blue)) / ((SWIR1 + Red) + (NIR + Blue))
      var swir1 = img.select('SWIR1');
      var red = img.select('Red');
      var nir = img.select('NIR');
      var blue = img.select('Blue');
      var num = swir1.add(red).subtract(nir.add(blue));
      var den = swir1.add(red).add(nir.add(blue));
      return num.divide(den).rename('BSI');
    }
  },
  'NDMI': {
    name: 'NDMI',
    description: 'Normalized Difference Moisture Index — canopy moisture',
    compute: function(img) {
      return img.normalizedDifference(['NIR', 'SWIR1']).rename('NDMI');
    }
  }
};

// Compute selected indices and return as a multi-band image
function computeIndices(composite, selectedIndexNames) {
  var indexBands = [];
  for (var i = 0; i < selectedIndexNames.length; i++) {
    var def = INDEX_DEFINITIONS[selectedIndexNames[i]];
    indexBands.push(def.compute(composite));
  }
  if (indexBands.length === 0) {
    return null;
  }
  var result = indexBands[0];
  for (var j = 1; j < indexBands.length; j++) {
    result = result.addBands(indexBands[j]);
  }
  return result;
}

// ============================================================
// Monthly Composite & Water Mask Generation
// ============================================================

// Generate monthly median composites, water masks, and spectral indices,
// then submit export tasks to Google Drive
function generateMonthlyMasks(collection, geometry, startDate, endDate,
                              nirThreshold, prefix, statusLabel,
                              selectedIndexNames) {
  var start = ee.Date(startDate);
  var end = ee.Date(endDate);

  var startYear = start.get('year').getInfo();
  var startMonth = start.get('month').getInfo();
  var endYear = end.get('year').getInfo();
  var endMonth = end.get('month').getInfo();

  var taskCount = 0;
  var emptyCount = 0;
  var year = startYear;
  var month = startMonth;

  while (year < endYear || (year === endYear && month <= endMonth)) {
    var monthStr = (month < 10) ? '0' + month : '' + month;
    var mStart = year + '-' + monthStr + '-01';
    var nextMonth, nextYear;
    if (month === 12) {
      nextMonth = 1;
      nextYear = year + 1;
    } else {
      nextMonth = month + 1;
      nextYear = year;
    }
    var nextMonthStr = (nextMonth < 10) ? '0' + nextMonth : '' + nextMonth;
    var mEnd = nextYear + '-' + nextMonthStr + '-01';

    var monthly = collection.filterDate(mStart, mEnd);
    var count = monthly.size().getInfo();

    if (count > 0) {
      var composite = monthly.median().clip(geometry);
      var dateStr = year + '-' + monthStr;

      // Export multiband composite (Blue, Green, Red, NIR, SWIR1, SWIR2)
      Export.image.toDrive({
        image: composite,
        description: prefix + '_multiband_' + dateStr,
        folder: 'landsat_water_masks',
        fileNamePrefix: prefix + '_multiband_' + dateStr,
        region: geometry,
        scale: 30,
        crs: 'EPSG:4326',
        maxPixels: 1e13
      });

      // Generate binary water mask: NIR < threshold = water (1), else land (0)
      var waterMask = composite.select('NIR').lt(nirThreshold)
          .rename('water').toUint8();

      Export.image.toDrive({
        image: waterMask,
        description: prefix + '_water_mask_' + dateStr,
        folder: 'landsat_water_masks',
        fileNamePrefix: prefix + '_water_mask_' + dateStr,
        region: geometry,
        scale: 30,
        crs: 'EPSG:4326',
        maxPixels: 1e13
      });

      taskCount += 2;

      // Export spectral indices if any are selected
      if (selectedIndexNames && selectedIndexNames.length > 0) {
        var indices = computeIndices(composite, selectedIndexNames);
        if (indices !== null) {
          Export.image.toDrive({
            image: indices,
            description: prefix + '_indices_' + dateStr,
            folder: 'landsat_water_masks',
            fileNamePrefix: prefix + '_indices_' + dateStr,
            region: geometry,
            scale: 30,
            crs: 'EPSG:4326',
            maxPixels: 1e13
          });
          taskCount += 1;
        }
      }
    } else {
      emptyCount++;
    }

    // Advance to next month
    month = nextMonth;
    year = nextYear;
  }

  var monthsExported = taskCount - emptyCount;
  var indexNote = (selectedIndexNames && selectedIndexNames.length > 0)
      ? '\nIndices: ' + selectedIndexNames.join(', ')
      : '';
  statusLabel.setValue(
    '✓ Export tasks created!\n' +
    'Tasks submitted: ' + taskCount + '\n' +
    'Empty months skipped: ' + emptyCount + indexNote + '\n' +
    'Check the Tasks tab to run exports.'
  );
  statusLabel.style().set('color', 'green');
}

// ============================================================
// Main Analysis Functions
// ============================================================

var currentCollection = null;
var currentGeometry = null;

function queryImagery(startDate, endDate, statusLabel) {
  var drawnGeometry = Map.drawingTools().layers().get(0).toGeometry();

  if (!drawnGeometry) {
    statusLabel.setValue('ERROR: Please draw a polygon on the map first!');
    statusLabel.style().set('color', 'red');
    return;
  }

  currentGeometry = drawnGeometry;

  statusLabel.setValue('Querying Landsat imagery...');
  statusLabel.style().set('color', 'blue');

  var result = getLandsatCollection(startDate, endDate, drawnGeometry, 30);

  if (result.collection === null) {
    statusLabel.setValue('ERROR: No Landsat collections cover this date range.');
    statusLabel.style().set('color', 'red');
    return;
  }

  currentCollection = result.collection;

  var count = currentCollection.size().getInfo();
  if (count === 0) {
    statusLabel.setValue('No images found. Try expanding your date range or area.');
    statusLabel.style().set('color', 'orange');
    return;
  }

  // Clear previous layers and show RGB preview
  Map.layers().reset();
  var preview = currentCollection.median().clip(drawnGeometry);
  Map.addLayer(preview, {bands: ['Red', 'Green', 'Blue'], min: 0.0, max: 0.3},
               'Landsat RGB Preview');

  statusLabel.setValue(
    '✓ Found ' + count + ' images\n' +
    'Collections: ' + result.sensors.join(', ') + '\n' +
    'RGB preview added to map.'
  );
  statusLabel.style().set('color', 'green');
}

function previewWaterMask(startDate, endDate, nirThreshold, statusLabel) {
  if (currentCollection === null || currentGeometry === null) {
    statusLabel.setValue('ERROR: Run "Query Imagery" first!');
    statusLabel.style().set('color', 'red');
    return;
  }

  statusLabel.setValue('Generating water mask preview...');
  statusLabel.style().set('color', 'blue');

  var composite = currentCollection.median().clip(currentGeometry);
  var waterMask = composite.select('NIR').lt(nirThreshold).rename('water');

  // Remove previous water mask layer if present
  var layers = Map.layers();
  for (var i = layers.length() - 1; i >= 0; i--) {
    var layer = layers.get(i);
    if (layer.getName().indexOf('Water Mask') === 0) {
      layers.remove(layer);
    }
  }

  Map.addLayer(waterMask.selfMask(),
               {min: 0, max: 1, palette: ['0000FF']},
               'Water Mask Preview (NIR<' + nirThreshold.toFixed(2) + ')');

  // Calculate water area statistics
  var pixelArea = ee.Image.pixelArea();
  var waterAreaM2 = waterMask.multiply(pixelArea).reduceRegion({
    reducer: ee.Reducer.sum(),
    geometry: currentGeometry,
    scale: 30,
    maxPixels: 1e9,
    bestEffort: true
  });
  var totalAreaM2 = pixelArea.rename('total').reduceRegion({
    reducer: ee.Reducer.sum(),
    geometry: currentGeometry,
    scale: 30,
    maxPixels: 1e9,
    bestEffort: true
  });

  var waterHa = ee.Number(waterAreaM2.get('water')).divide(10000);
  var totalHa = ee.Number(totalAreaM2.get('total')).divide(10000);

  ee.Dictionary({water: waterHa, total: totalHa}).evaluate(function(result) {
    if (!result || result.water === null || result.total === null) {
      statusLabel.setValue(
        '✓ Water mask preview added to map.\n' +
        'Threshold: ' + nirThreshold.toFixed(3) + '\n' +
        '(Area statistics unavailable — try a smaller AOI)'
      );
      statusLabel.style().set('color', 'green');
      return;
    }
    var wh = result.water;
    var th = result.total;
    var pct = th > 0 ? (wh / th * 100).toFixed(1) : '0.0';
    statusLabel.setValue(
      '✓ Water mask preview added to map.\n' +
      'Threshold: ' + nirThreshold.toFixed(3) + '\n' +
      'Water area: ' + wh.toFixed(2) + ' ha (' + pct + '% of AOI)\n' +
      'Total AOI: ' + th.toFixed(2) + ' ha'
    );
    statusLabel.style().set('color', 'green');
  });
}

// ============================================================
// UI Panel
// ============================================================

var panel = ui.Panel({
  style: {
    width: '370px',
    position: 'top-left',
    padding: '8px'
  }
});

// Title
var title = ui.Label({
  value: 'Landsat Monthly Water Mask',
  style: {
    fontSize: '20px',
    fontWeight: 'bold',
    margin: '0 0 10px 0'
  }
});
panel.add(title);

// Instructions
var instructions = ui.Label({
  value: '1. Draw a polygon on the map\n' +
         '2. Set start and end dates\n' +
         '3. Enter a filename prefix\n' +
         '4. Click "Query Imagery"\n' +
         '5. Adjust NIR threshold & preview\n' +
         '6. Click "Generate Monthly Masks"',
  style: {
    fontSize: '13px',
    margin: '0 0 10px 0',
    whiteSpace: 'pre'
  }
});
panel.add(instructions);

// Separator helper
function addSeparator() {
  panel.add(ui.Panel({
    style: {
      height: '1px',
      backgroundColor: 'gray',
      margin: '10px 0'
    }
  }));
}

addSeparator();

// --- Start Date ---
panel.add(ui.Label({
  value: 'Start Date:',
  style: {fontSize: '14px', fontWeight: 'bold', margin: '5px 0 2px 0'}
}));

var startDateSlider = ui.DateSlider({
  start: '1984-01-01',
  end: Date.now(),
  value: '1990-01-01',
  period: 1,
  style: {stretch: 'horizontal'}
});
panel.add(startDateSlider);

// --- End Date ---
panel.add(ui.Label({
  value: 'End Date:',
  style: {fontSize: '14px', fontWeight: 'bold', margin: '10px 0 2px 0'}
}));

var endDateSlider = ui.DateSlider({
  start: '1984-01-01',
  end: Date.now(),
  value: '1995-12-31',
  period: 1,
  style: {stretch: 'horizontal'}
});
panel.add(endDateSlider);

addSeparator();

// --- Filename Prefix ---
panel.add(ui.Label({
  value: 'Filename Prefix:',
  style: {fontSize: '14px', fontWeight: 'bold', margin: '5px 0 2px 0'}
}));

var prefixTextbox = ui.Textbox({
  value: 'landsat_aoi',
  placeholder: 'e.g. quinhagak_river',
  style: {stretch: 'horizontal'}
});
panel.add(prefixTextbox);

addSeparator();

// --- NIR Threshold ---
panel.add(ui.Label({
  value: 'NIR Threshold (Water Detection):',
  style: {fontSize: '14px', fontWeight: 'bold', margin: '5px 0 2px 0'}
}));

panel.add(ui.Label({
  value: 'Lower = More Water | Higher = Less Water',
  style: {fontSize: '11px', color: 'gray', margin: '0 0 5px 0', fontStyle: 'italic'}
}));

var thresholdValueLabel = ui.Label({
  value: 'Current: 0.150',
  style: {fontSize: '12px', margin: '0 0 5px 0', color: '#2c5aa0'}
});
panel.add(thresholdValueLabel);

var thresholdSlider = ui.Slider({
  min: 0.05,
  max: 0.50,
  value: 0.15,
  step: 0.01,
  style: {stretch: 'horizontal'},
  onChange: function(value) {
    thresholdValueLabel.setValue('Current: ' + value.toFixed(3));
  }
});
panel.add(thresholdSlider);

// Preset buttons
var presetPanel = ui.Panel({
  layout: ui.Panel.Layout.flow('horizontal'),
  style: {margin: '5px 0'}
});
presetPanel.add(ui.Label({
  value: 'Presets:',
  style: {fontSize: '11px', margin: '2px 5px 0 0'}
}));
presetPanel.add(ui.Button({
  label: 'Conservative',
  style: {fontSize: '10px', padding: '2px 4px', margin: '0 2px'},
  onClick: function() { thresholdSlider.setValue(0.10); }
}));
presetPanel.add(ui.Button({
  label: 'Moderate',
  style: {fontSize: '10px', padding: '2px 4px', margin: '0 2px'},
  onClick: function() { thresholdSlider.setValue(0.15); }
}));
presetPanel.add(ui.Button({
  label: 'Aggressive',
  style: {fontSize: '10px', padding: '2px 4px', margin: '0 2px'},
  onClick: function() { thresholdSlider.setValue(0.20); }
}));
panel.add(presetPanel);

addSeparator();

// --- Spectral Indices ---
panel.add(ui.Label({
  value: 'Spectral Indices to Export:',
  style: {fontSize: '14px', fontWeight: 'bold', margin: '5px 0 2px 0'}
}));

panel.add(ui.Label({
  value: 'Select indices to compute for each monthly composite.\n' +
         'Exported as a separate multi-band GeoTIFF per month.',
  style: {fontSize: '11px', color: 'gray', margin: '0 0 5px 0', fontStyle: 'italic',
          whiteSpace: 'pre-wrap'}
}));

var indexPanel = ui.Panel({
  style: {
    maxHeight: '300px',
    border: '1px solid lightgray',
    padding: '5px',
    margin: '5px 0'
  }
});

// Checkbox style helper
var cbStyle = {fontSize: '11px', margin: '1px 0 1px 10px'};

// --- Vegetation Health & Biomass ---
indexPanel.add(ui.Label({
  value: 'Vegetation Health & Biomass',
  style: {fontWeight: 'bold', fontSize: '12px', color: '#228b22', margin: '2px 0'}
}));

var ndviCheckbox = ui.Checkbox({label: 'NDVI - Biomass, greenness', value: true, style: cbStyle});
indexPanel.add(ndviCheckbox);

var eviCheckbox = ui.Checkbox({label: 'EVI - Enhanced vegetation', value: true, style: cbStyle});
indexPanel.add(eviCheckbox);

var gndviCheckbox = ui.Checkbox({label: 'GNDVI - Nitrogen status', value: true, style: cbStyle});
indexPanel.add(gndviCheckbox);

var saviCheckbox = ui.Checkbox({label: 'SAVI - Soil-adjusted NDVI', value: false, style: cbStyle});
indexPanel.add(saviCheckbox);

var msaviCheckbox = ui.Checkbox({label: 'MSAVI - Minimize soil noise', value: false, style: cbStyle});
indexPanel.add(msaviCheckbox);

var cigCheckbox = ui.Checkbox({label: 'CIG - Chlorophyll Index Green', value: true, style: cbStyle});
indexPanel.add(cigCheckbox);

var variCheckbox = ui.Checkbox({label: 'VARI - Visual greenness', value: false, style: cbStyle});
indexPanel.add(variCheckbox);

var arviCheckbox = ui.Checkbox({label: 'ARVI - Atmosphere resistant', value: false, style: cbStyle});
indexPanel.add(arviCheckbox);

// --- Water ---
indexPanel.add(ui.Label({
  value: 'Water',
  style: {fontWeight: 'bold', fontSize: '12px', color: '#2c5aa0', margin: '5px 0 2px 0'}
}));

var ndwiCheckbox = ui.Checkbox({label: 'NDWI - Water stress, moisture', value: true, style: cbStyle});
indexPanel.add(ndwiCheckbox);

var mndwiCheckbox = ui.Checkbox({label: 'MNDWI - Modified water index', value: false, style: cbStyle});
indexPanel.add(mndwiCheckbox);

// --- Burn / Disturbance ---
indexPanel.add(ui.Label({
  value: 'Burn & Disturbance',
  style: {fontWeight: 'bold', fontSize: '12px', color: '#cc4400', margin: '5px 0 2px 0'}
}));

var nbrCheckbox = ui.Checkbox({label: 'NBR - Fire severity, disturbance', value: false, style: cbStyle});
indexPanel.add(nbrCheckbox);

// --- Soil / Moisture ---
indexPanel.add(ui.Label({
  value: 'Soil & Moisture',
  style: {fontWeight: 'bold', fontSize: '12px', color: '#8B6914', margin: '5px 0 2px 0'}
}));

var bsiCheckbox = ui.Checkbox({label: 'BSI - Bare soil detection', value: false, style: cbStyle});
indexPanel.add(bsiCheckbox);

var ndmiCheckbox = ui.Checkbox({label: 'NDMI - Canopy moisture', value: false, style: cbStyle});
indexPanel.add(ndmiCheckbox);

panel.add(indexPanel);

// Select All / Clear All for indices
var indexBtnPanel = ui.Panel({
  layout: ui.Panel.Layout.flow('horizontal'),
  style: {margin: '3px 0'}
});
indexBtnPanel.add(ui.Button({
  label: 'Select All',
  style: {fontSize: '10px', padding: '2px 5px', margin: '0 5px 0 0'},
  onClick: function() {
    for (var n in indexCheckboxMap) { indexCheckboxMap[n].setValue(true); }
  }
}));
indexBtnPanel.add(ui.Button({
  label: 'Clear All',
  style: {fontSize: '10px', padding: '2px 5px'},
  onClick: function() {
    for (var n in indexCheckboxMap) { indexCheckboxMap[n].setValue(false); }
  }
}));
panel.add(indexBtnPanel);

// Note about unavailable indices
panel.add(ui.Label({
  value: 'Note: RTVICore, PRI, CRI, CIrededge require red edge\n' +
         'bands not available on Landsat. Use Sentinel-2 for those.',
  style: {fontSize: '10px', color: 'gray', fontStyle: 'italic', margin: '3px 0',
          whiteSpace: 'pre-wrap'}
}));

// Helper to collect selected index names from checkboxes
var indexCheckboxMap = {
  'NDVI': ndviCheckbox,
  'EVI': eviCheckbox,
  'GNDVI': gndviCheckbox,
  'SAVI': saviCheckbox,
  'MSAVI': msaviCheckbox,
  'CIG': cigCheckbox,
  'VARI': variCheckbox,
  'ARVI': arviCheckbox,
  'NDWI': ndwiCheckbox,
  'MNDWI': mndwiCheckbox,
  'NBR': nbrCheckbox,
  'BSI': bsiCheckbox,
  'NDMI': ndmiCheckbox
};

function getSelectedIndices() {
  var selected = [];
  for (var name in indexCheckboxMap) {
    if (indexCheckboxMap[name].getValue()) {
      selected.push(name);
    }
  }
  return selected;
}

addSeparator();

// --- Status Label ---
var statusLabel = ui.Label({
  value: 'Ready. Draw a polygon and click Query Imagery.',
  style: {
    fontSize: '12px',
    color: 'gray',
    margin: '10px 0',
    whiteSpace: 'pre-wrap'
  }
});
panel.add(statusLabel);

// --- Action Buttons ---
var queryButton = ui.Button({
  label: '🔍 Query Imagery',
  style: {stretch: 'horizontal', margin: '5px 0'},
  onClick: function() {
    var earliest = ee.Date(startDateSlider.getValue()[0]);
    var latest = ee.Date(endDateSlider.getValue()[0]);
    queryImagery(earliest, latest, statusLabel);
  }
});
panel.add(queryButton);

var previewButton = ui.Button({
  label: '👁 Preview Water Mask',
  style: {stretch: 'horizontal', margin: '5px 0'},
  onClick: function() {
    var earliest = ee.Date(startDateSlider.getValue()[0]);
    var latest = ee.Date(endDateSlider.getValue()[0]);
    previewWaterMask(earliest, latest, thresholdSlider.getValue(), statusLabel);
  }
});
panel.add(previewButton);

var generateButton = ui.Button({
  label: '▶ Generate Monthly Masks',
  style: {stretch: 'horizontal', margin: '5px 0'},
  onClick: function() {
    if (currentCollection === null || currentGeometry === null) {
      statusLabel.setValue('ERROR: Run "Query Imagery" first!');
      statusLabel.style().set('color', 'red');
      return;
    }
    statusLabel.setValue('Generating monthly exports...\nThis may take a moment.');
    statusLabel.style().set('color', 'blue');

    var earliest = ee.Date(startDateSlider.getValue()[0]);
    var latest = ee.Date(endDateSlider.getValue()[0]);
    var prefix = prefixTextbox.getValue();
    var threshold = thresholdSlider.getValue();
    var selectedIndices = getSelectedIndices();

    generateMonthlyMasks(currentCollection, currentGeometry,
                         earliest, latest, threshold, prefix, statusLabel,
                         selectedIndices);
  }
});
panel.add(generateButton);

addSeparator();

// --- Info Section ---
var infoLabel = ui.Label({
  value: 'Sensors: L5 TM, L7 ETM+, L8 OLI, L9 OLI-2\n' +
         'Resolution: 30m (Landsat native)\n' +
         'Bands: Blue, Green, Red, NIR, SWIR1, SWIR2\n' +
         'Cloud masking: QA_PIXEL (cloud + shadow)\n' +
         'Scaling: Collection 2 L2 SR\n' +
         'Compositing: Monthly median\n' +
         'Outputs per month:\n' +
         '  • 6-band multiband GeoTIFF\n' +
         '  • Binary water mask GeoTIFF (1=water, 0=land)\n' +
         '  • Spectral indices GeoTIFF (if selected)\n' +
         'Available indices (13):\n' +
         '  Veg: NDVI, EVI, GNDVI, SAVI, MSAVI, CIG, VARI, ARVI\n' +
         '  Water: NDWI, MNDWI\n' +
         '  Burn: NBR | Soil: BSI, NDMI',
  style: {
    fontSize: '11px',
    color: 'gray',
    whiteSpace: 'pre'
  }
});
panel.add(infoLabel);

// --- Legend ---
addSeparator();

panel.add(ui.Label({
  value: 'Legend:',
  style: {fontSize: '12px', fontWeight: 'bold', margin: '5px 0'}
}));

var waterLegend = ui.Panel({
  layout: ui.Panel.Layout.flow('horizontal'),
  style: {margin: '2px 0'}
});
waterLegend.add(ui.Label({
  style: {backgroundColor: '0000FF', padding: '8px', margin: '0 5px 0 0'}
}));
waterLegend.add(ui.Label({
  value: 'Water (1) - NIR below threshold',
  style: {fontSize: '11px', margin: '2px 0'}
}));
panel.add(waterLegend);

var landLegend = ui.Panel({
  layout: ui.Panel.Layout.flow('horizontal'),
  style: {margin: '2px 0'}
});
landLegend.add(ui.Label({
  style: {backgroundColor: 'CCCCCC', padding: '8px', margin: '0 5px 0 0'}
}));
landLegend.add(ui.Label({
  value: 'Land (0) - NIR above threshold',
  style: {fontSize: '11px', margin: '2px 0'}
}));
panel.add(landLegend);

// ============================================================
// Initialize Map
// ============================================================

ui.root.insert(0, panel);

// Center on Quinhagak, Alaska
Map.setCenter(-161.90402886481778, 59.750359237437635, 10);

// Enable drawing tools
Map.drawingTools().setShown(true);
Map.drawingTools().setDrawModes(['polygon', 'rectangle']);
