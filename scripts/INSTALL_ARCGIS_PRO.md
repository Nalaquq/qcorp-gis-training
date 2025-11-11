# Installing Earth Engine for ArcGIS Pro

## Installation Instructions

### Step 1: Open Python Command Prompt

1. Open **ArcGIS Pro**
2. Click **Project** → **Python** → **Python Command Prompt**
3. This will open a command prompt with ArcGIS Pro's Python environment activated

### Step 2: Install Required Packages

Run these commands in the Python Command Prompt:

```bash
# Install Earth Engine API
python -m pip install earthengine-api

# Install geemap (for interactive mapping)
python -m pip install geemap

# Install ipywidgets (for date pickers)
python -m pip install ipywidgets
```

### Step 3: Authenticate Earth Engine

After installation, you need to authenticate with Google Earth Engine:

```bash
earthengine authenticate
```

This will open a browser window for you to sign in with your Google account and authorize Earth Engine access.

### Step 4: Test Installation

In ArcGIS Pro's Python notebook, run:

```python
import ee
ee.Initialize()
print("Earth Engine successfully initialized!")
```

## Alternative: Clone ArcGIS Pro Environment (Safer Method)

To avoid modifying the default ArcGIS Pro environment:

1. Go to **Project** → **Python** → **Manage Environments**
2. Click **Clone** on the default environment
3. Name it something like `arcgis_earthengine`
4. Select your new cloned environment
5. Click **Add Packages** and search for:
   - `earthengine-api`
   - `geemap`
   - `ipywidgets`
6. Install all three packages
7. Set this as your active environment

## Troubleshooting

### Error: "ModuleNotFoundError: No module named 'ee'"
- Make sure you installed in the correct environment
- Restart ArcGIS Pro after installation
- Verify installation: `pip list | findstr earthengine`

### Error: "Please authenticate Earth Engine"
- Run: `earthengine authenticate`
- Follow the browser authentication flow
- Copy the authorization code back to the command prompt

### Error: "Cannot import geemap"
- Install with: `python -m pip install geemap`
- If conflicts occur, try: `python -m pip install geemap --no-deps`

## Package Versions

Recommended versions (as of November 2025):
- `earthengine-api >= 0.1.384`
- `geemap >= 0.30.0`
- `ipywidgets >= 8.0.0`

## Additional Resources

- [Earth Engine Python API Documentation](https://developers.google.com/earth-engine/guides/python_install)
- [geemap Documentation](https://geemap.org/)
- [ArcGIS Pro Python Documentation](https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/using-conda-with-arcgis-pro.htm)
