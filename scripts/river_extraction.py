"""
River Polygon Extraction from Binary Water/Land Rasters

This module extracts river channel polygons (including braids) from binary
water/land classification rasters produced by Google Earth Engine.

Author: Nalaquq LLC / QCORP GIS Training
License: MIT
"""

import numpy as np
import rasterio
from rasterio import features
from scipy import ndimage
from scipy.ndimage import label
from shapely.geometry import shape, mapping
from shapely.ops import unary_union
import geopandas as gpd
import json
from typing import Optional, Tuple, List, Union
from pathlib import Path


class RiverExtractor:
    """
    Extract river polygons from binary water/land rasters.

    Handles braided river systems by extracting all connected water pixels
    that belong to the main river network.
    """

    def __init__(self, raster_path: Union[str, Path]):
        """
        Initialize with path to binary raster.

        Args:
            raster_path: Path to GeoTIFF with water=0, land=1 (or vice versa)
        """
        self.raster_path = Path(raster_path)
        self.data = None
        self.transform = None
        self.crs = None
        self.nodata = None
        self._load_raster()

    def _load_raster(self):
        """Load raster data and metadata."""
        with rasterio.open(self.raster_path) as src:
            self.data = src.read(1)
            self.transform = src.transform
            self.crs = src.crs
            self.nodata = src.nodata

        print(f"Loaded raster: {self.raster_path.name}")
        print(f"  Shape: {self.data.shape}")
        print(f"  CRS: {self.crs}")
        print(f"  Unique values: {np.unique(self.data)}")

    def identify_water_value(self) -> int:
        """
        Automatically identify which value represents water.
        Assumes water is the minority class (less than 50% of pixels).

        Returns:
            Value representing water (0 or 1)
        """
        unique, counts = np.unique(self.data, return_counts=True)

        # Remove nodata if present
        if self.nodata is not None:
            mask = unique != self.nodata
            unique = unique[mask]
            counts = counts[mask]

        # Water is typically the minority class
        water_value = unique[np.argmin(counts)]
        print(f"Identified water value: {water_value}")
        return water_value

    def preprocess(self,
                   water_value: Optional[int] = None,
                   min_size_pixels: int = 10,
                   morphology_iterations: int = 0) -> np.ndarray:
        """
        Preprocess binary raster to remove noise while preserving braids.

        Args:
            water_value: Value representing water (auto-detected if None)
            min_size_pixels: Remove water features smaller than this
            morphology_iterations: Apply morphological closing (0=none, 1-2=light cleaning)

        Returns:
            Cleaned binary mask (True=water, False=land)
        """
        if water_value is None:
            water_value = self.identify_water_value()

        # Create binary mask (True = water)
        water_mask = (self.data == water_value)

        # Optional: Remove very small isolated features (noise)
        if min_size_pixels > 0:
            labeled, num_features = label(water_mask)
            sizes = ndimage.sum(water_mask, labeled, range(num_features + 1))
            mask_size = sizes < min_size_pixels
            remove_small = mask_size[labeled]
            water_mask[remove_small] = False
            print(f"Removed {np.sum(remove_small)} small noise pixels")

        # Optional: Morphological closing to fill small gaps
        if morphology_iterations > 0:
            from scipy.ndimage import binary_closing
            structure = np.ones((3, 3))
            water_mask = binary_closing(water_mask,
                                       structure=structure,
                                       iterations=morphology_iterations)
            print(f"Applied {morphology_iterations} iterations of morphological closing")

        return water_mask

    def extract_largest_component(self, water_mask: np.ndarray) -> np.ndarray:
        """
        Extract the largest connected water component (main river).

        Args:
            water_mask: Binary mask (True=water)

        Returns:
            Binary mask with only the largest connected component
        """
        labeled, num_features = label(water_mask)

        if num_features == 0:
            print("WARNING: No water features found!")
            return np.zeros_like(water_mask, dtype=bool)

        # Find largest component
        sizes = ndimage.sum(water_mask, labeled, range(num_features + 1))
        largest_label = np.argmax(sizes[1:]) + 1  # Skip background (0)

        river_mask = (labeled == largest_label)

        print(f"Found {num_features} water components")
        print(f"Largest component: {sizes[largest_label]} pixels")

        return river_mask

    def extract_by_seed_point(self,
                              water_mask: np.ndarray,
                              lon: float,
                              lat: float) -> np.ndarray:
        """
        Extract river component containing a seed point.

        Args:
            water_mask: Binary mask (True=water)
            lon: Longitude of seed point
            lat: Latitude of seed point

        Returns:
            Binary mask with connected component containing seed point
        """
        # Convert geographic coordinates to pixel coordinates
        from rasterio.transform import rowcol
        row, col = rowcol(self.transform, lon, lat)

        if not (0 <= row < water_mask.shape[0] and 0 <= col < water_mask.shape[1]):
            raise ValueError(f"Seed point ({lon}, {lat}) is outside raster bounds")

        if not water_mask[row, col]:
            print(f"WARNING: Seed point is not on water. Finding nearest water pixel...")
            # Find nearest water pixel
            from scipy.ndimage import distance_transform_edt
            distances = distance_transform_edt(~water_mask)
            row, col = np.unravel_index(np.argmin(distances), distances.shape)

        # Label all components
        labeled, num_features = label(water_mask)

        # Get label at seed point
        seed_label = labeled[row, col]

        if seed_label == 0:
            raise ValueError("Seed point is on background/land")

        river_mask = (labeled == seed_label)

        print(f"Extracted component at seed point ({lon:.6f}, {lat:.6f})")
        print(f"Component size: {np.sum(river_mask)} pixels")

        return river_mask

    def mask_to_polygons(self,
                        river_mask: np.ndarray,
                        simplify_tolerance: float = 0.0) -> List[dict]:
        """
        Convert binary mask to polygon geometries.

        Args:
            river_mask: Binary mask (True=river)
            simplify_tolerance: Simplify polygons (0=no simplification)

        Returns:
            List of polygon geometries in GeoJSON format
        """
        # Convert mask to uint8 for rasterio
        mask_uint8 = river_mask.astype('uint8')

        # Extract shapes
        polygons = []
        for geom, value in features.shapes(mask_uint8,
                                          transform=self.transform,
                                          mask=mask_uint8):
            if value == 1:  # Water pixels
                poly = shape(geom)

                # Simplify if requested
                if simplify_tolerance > 0:
                    poly = poly.simplify(simplify_tolerance, preserve_topology=True)

                polygons.append(mapping(poly))

        print(f"Extracted {len(polygons)} polygon(s)")

        return polygons

    def extract_river(self,
                     method: str = 'largest',
                     seed_point: Optional[Tuple[float, float]] = None,
                     water_value: Optional[int] = None,
                     min_size_pixels: int = 10,
                     morphology_iterations: int = 0,
                     simplify_tolerance: float = 0.0) -> gpd.GeoDataFrame:
        """
        Complete workflow: extract river polygons from raster.

        Args:
            method: 'largest' or 'seed_point'
            seed_point: (lon, lat) tuple if using seed_point method
            water_value: Value representing water (auto-detected if None)
            min_size_pixels: Remove noise features smaller than this
            morphology_iterations: Morphological closing iterations (0-2 recommended)
            simplify_tolerance: Simplify polygon tolerance in map units

        Returns:
            GeoDataFrame with river polygon(s)
        """
        print(f"\n{'='*60}")
        print(f"EXTRACTING RIVER POLYGONS")
        print(f"{'='*60}")

        # Step 1: Preprocess
        print("\n[1/3] Preprocessing...")
        water_mask = self.preprocess(water_value, min_size_pixels, morphology_iterations)

        # Step 2: Extract river component
        print(f"\n[2/3] Extracting river using '{method}' method...")
        if method == 'largest':
            river_mask = self.extract_largest_component(water_mask)
        elif method == 'seed_point':
            if seed_point is None:
                raise ValueError("seed_point required for 'seed_point' method")
            river_mask = self.extract_by_seed_point(water_mask, seed_point[0], seed_point[1])
        else:
            raise ValueError(f"Unknown method: {method}")

        # Step 3: Convert to polygons
        print(f"\n[3/3] Converting to polygons...")
        polygons = self.mask_to_polygons(river_mask, simplify_tolerance)

        # Create GeoDataFrame
        gdf = gpd.GeoDataFrame(
            {'geometry': [shape(p) for p in polygons]},
            crs=self.crs
        )

        # Add metadata
        gdf['source_raster'] = self.raster_path.name
        gdf['extraction_method'] = method
        gdf['area_m2'] = gdf.geometry.area
        gdf['perimeter_m'] = gdf.geometry.length

        print(f"\n{'='*60}")
        print(f"EXTRACTION COMPLETE")
        print(f"{'='*60}")
        print(f"Total river area: {gdf['area_m2'].sum() / 10000:.2f} hectares")
        print(f"Number of polygons: {len(gdf)}")

        return gdf

    def save_vector(self,
                   gdf: gpd.GeoDataFrame,
                   output_path: Union[str, Path],
                   driver: str = 'GPKG') -> Path:
        """
        Save river polygons to file.

        Args:
            gdf: GeoDataFrame with river polygons
            output_path: Output file path
            driver: Output format ('GPKG', 'GeoJSON', 'ESRI Shapefile')

        Returns:
            Path to saved file
        """
        output_path = Path(output_path)

        # Ensure correct extension
        extensions = {'GPKG': '.gpkg', 'GeoJSON': '.geojson', 'ESRI Shapefile': '.shp'}
        if driver in extensions:
            output_path = output_path.with_suffix(extensions[driver])

        gdf.to_file(output_path, driver=driver)
        print(f"\nSaved to: {output_path}")

        return output_path


def batch_extract_rivers(raster_paths: List[Union[str, Path]],
                        output_dir: Union[str, Path],
                        method: str = 'largest',
                        **kwargs) -> List[gpd.GeoDataFrame]:
    """
    Batch process multiple rasters for temporal analysis.

    Args:
        raster_paths: List of paths to binary rasters
        output_dir: Directory to save outputs
        method: Extraction method ('largest' or 'seed_point')
        **kwargs: Additional arguments passed to extract_river()

    Returns:
        List of GeoDataFrames, one per raster
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    results = []

    for raster_path in raster_paths:
        print(f"\n\n{'#'*70}")
        print(f"Processing: {Path(raster_path).name}")
        print(f"{'#'*70}")

        try:
            extractor = RiverExtractor(raster_path)
            gdf = extractor.extract_river(method=method, **kwargs)

            # Save
            output_path = output_dir / Path(raster_path).stem
            extractor.save_vector(gdf, output_path, driver='GPKG')

            results.append(gdf)

        except Exception as e:
            print(f"ERROR processing {raster_path}: {e}")
            results.append(None)

    print(f"\n\n{'='*70}")
    print(f"BATCH PROCESSING COMPLETE")
    print(f"{'='*70}")
    print(f"Processed {len([r for r in results if r is not None])}/{len(raster_paths)} files successfully")

    return results


if __name__ == "__main__":
    # Example usage
    import sys

    if len(sys.argv) < 2:
        print("Usage: python river_extraction.py <raster_path> [output_path]")
        print("\nExample:")
        print("  python river_extraction.py WaterLand_Classification.tif river_polygons.gpkg")
        sys.exit(1)

    raster_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else "river_extracted.gpkg"

    # Extract river
    extractor = RiverExtractor(raster_path)
    gdf = extractor.extract_river(
        method='largest',
        min_size_pixels=50,  # Remove small noise
        morphology_iterations=1,  # Light cleaning
        simplify_tolerance=1.0  # Simplify to 1 meter tolerance
    )

    # Save
    extractor.save_vector(gdf, output_path)

    print("\n✓ Done! Open in ArcGIS Pro or QGIS to view results.")
