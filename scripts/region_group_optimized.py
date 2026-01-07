"""
Optimized Region Group for Binary Water/Land Classification
=============================================================

Purpose: Identify and extract individual river systems from binary water/land rasters.

Optimized for:
- Quality: Accurate river system identification
- Binary rasters: water=0, land=1
- Large rasters: GPU acceleration when available
- Clean polygons: Morphological operations to remove noise

Author: Nalaquq LLC / QCORP GIS Training
License: MIT
"""

import numpy as np
import rasterio
from rasterio import features
import geopandas as gpd
from shapely.geometry import shape
import pandas as pd
from pathlib import Path
from typing import Optional, Union, Tuple, Dict, List
import time
from skimage.morphology import skeletonize
from scipy import ndimage as scipy_ndimage

# Try GPU acceleration
try:
    import cupy as cp
    from cupyx.scipy import ndimage as cp_ndimage
    GPU_AVAILABLE = True
except ImportError:
    cp = None
    GPU_AVAILABLE = False


class RiverSystemExtractor:
    """
    Extract individual river systems from binary water/land classification.

    Optimized for quality identification of separate river systems.
    """

    def __init__(self, raster_path: Union[str, Path], use_gpu: bool = True):
        """
        Initialize extractor.

        Args:
            raster_path: Path to binary raster (0=water, 1=land)
            use_gpu: Use GPU if available (default: True)
        """
        self.raster_path = Path(raster_path)
        self.data = None
        self.transform = None
        self.crs = None
        self.bounds = None
        self.nodata = None
        self.labeled_regions = None
        self.num_regions = None
        self.region_stats = None
        self.use_gpu = use_gpu and GPU_AVAILABLE
        self.processing_time = None

        self._load_raster()

    def _load_raster(self):
        """Load raster data."""
        with rasterio.open(self.raster_path) as src:
            self.data = src.read(1)
            self.transform = src.transform
            self.crs = src.crs
            self.bounds = src.bounds
            self.nodata = src.nodata

        print(f"\n{'='*70}")
        print(f"RIVER SYSTEM EXTRACTION")
        print(f"{'='*70}")
        print(f"Raster: {self.raster_path.name}")
        print(f"  Size: {self.data.shape} ({self.data.size:,} pixels)")
        print(f"  Memory: {self.data.nbytes / 1024 / 1024:.1f} MB")
        print(f"  CRS: {self.crs}")
        print(f"  Values: {np.unique(self.data)}")
        print(f"  Mode: {'GPU (CuPy)' if self.use_gpu else 'CPU (SciPy)'}")

    def separate_from_ocean(self,
                           water_mask: np.ndarray,
                           remove_largest: bool = True) -> np.ndarray:
        """
        Separate inland rivers from ocean by removing the largest water body.

        This prevents all rivers from being connected as one giant polygon
        when they flow into the ocean.

        Args:
            water_mask: Binary mask (True=water, False=land)
            remove_largest: Remove the largest water body (ocean) (default: True)

        Returns:
            Modified water mask with ocean removed
        """
        if not remove_largest:
            return water_mask

        print(f"\nSeparating rivers from ocean...")

        # First, identify all water bodies
        labeled_temp, num_temp = scipy_ndimage.label(water_mask, structure=np.ones((3, 3)))

        # Count pixels per region
        region_ids = labeled_temp.ravel()
        region_ids = region_ids[region_ids > 0]
        pixel_counts = np.bincount(region_ids)

        # Ocean is the largest water body by far
        if len(pixel_counts) > 1:
            largest_id = np.argmax(pixel_counts[1:]) + 1
            ocean_pixels = pixel_counts[largest_id]
            total_water = np.sum(water_mask)

            print(f"  Largest water body: {ocean_pixels:,} pixels ({ocean_pixels/total_water*100:.1f}% of all water)")
            print(f"  Removing this body (assumed to be ocean/large lake)")

            # Simply remove the ocean entirely
            ocean_mask = (labeled_temp == largest_id)
            water_mask_separated = water_mask & ~ocean_mask

            removed_pixels = np.sum(water_mask) - np.sum(water_mask_separated)
            print(f"  Removed {removed_pixels:,} pixels ({removed_pixels/total_water*100:.1f}% of water)")
            print(f"  Remaining water bodies: {num_temp - 1}")

            return water_mask_separated
        else:
            print("  Only one water body detected, skipping separation")
            return water_mask

    def extract_river_systems(self,
                             water_value: int = 0,
                             land_value: int = 1,
                             connectivity: int = 8,
                             min_area_pixels: int = 0,
                             morphology_cleanup: int = 0,
                             remove_ocean: bool = False) -> np.ndarray:
        """
        Extract individual river systems.

        Args:
            water_value: Pixel value for water (default: 0)
            land_value: Pixel value for land to exclude (default: 1)
            connectivity: 4 or 8 neighbor connectivity (default: 8)
            min_area_pixels: Remove regions smaller than this (default: 0)
            morphology_cleanup: Morphological closing iterations for cleanup (default: 0)
            remove_ocean: Remove largest water body (ocean/large lake) (default: False)

        Returns:
            Labeled array where each river system has unique ID
        """
        print(f"\n{'='*70}")
        print("IDENTIFYING RIVER SYSTEMS")
        print(f"{'='*70}")
        print(f"Parameters:")
        print(f"  Water value: {water_value}")
        print(f"  Connectivity: {connectivity}-neighbor")
        print(f"  Min area filter: {min_area_pixels} pixels")
        print(f"  Morphology cleanup: {morphology_cleanup} iterations")
        print(f"  Remove ocean: {'Yes' if remove_ocean else 'No'}")

        start_time = time.time()

        # Create water mask
        water_mask = (self.data == water_value)
        if self.nodata is not None:
            water_mask = water_mask & (self.data != self.nodata)

        water_pixels = np.sum(water_mask)
        print(f"\nWater pixels: {water_pixels:,} ({water_pixels/water_mask.size*100:.1f}%)")

        # Optional morphological cleanup
        if morphology_cleanup > 0:
            print(f"  Applying morphological closing ({morphology_cleanup} iterations)...")
            structure = np.ones((3, 3))
            water_mask = scipy_ndimage.binary_closing(
                water_mask,
                structure=structure,
                iterations=morphology_cleanup
            )

        # Separate rivers from ocean
        if remove_ocean:
            water_mask = self.separate_from_ocean(water_mask, remove_largest=True)

        # Define connectivity structure
        if connectivity == 8:
            structure = np.array([[1, 1, 1],
                                 [1, 1, 1],
                                 [1, 1, 1]], dtype=np.uint8)
        else:  # 4-neighbor
            structure = np.array([[0, 1, 0],
                                 [1, 1, 1],
                                 [0, 1, 0]], dtype=np.uint8)

        # Connected component labeling
        if self.use_gpu:
            labeled = self._label_gpu(water_mask, structure)
        else:
            labeled = self._label_cpu(water_mask, structure)

        # Filter by minimum area
        if min_area_pixels > 0:
            print(f"\nFiltering regions < {min_area_pixels} pixels...")
            labeled = self._filter_small_regions(labeled, min_area_pixels)

        self.labeled_regions = labeled
        elapsed = time.time() - start_time
        self.processing_time = elapsed

        print(f"\n{'='*70}")
        print(f"EXTRACTION COMPLETE")
        print(f"{'='*70}")
        print(f"River systems identified: {self.num_regions}")
        print(f"Processing time: {elapsed:.2f} seconds")
        print(f"Throughput: {self.data.size / elapsed / 1e6:.1f} million pixels/second")

        return labeled

    def _label_gpu(self, mask: np.ndarray, structure: np.ndarray) -> np.ndarray:
        """GPU-accelerated connected component labeling."""
        print("  [GPU] Transferring data to GPU...")

        gpu_mask = cp.asarray(mask, dtype=cp.uint8)
        gpu_structure = cp.asarray(structure, dtype=cp.uint8)

        print("  [GPU] Running connected component labeling...")
        labeled_gpu, self.num_regions = cp_ndimage.label(gpu_mask, structure=gpu_structure)

        print("  [GPU] Transferring results back to CPU...")
        labeled = cp.asnumpy(labeled_gpu)

        return labeled.astype(np.int32)

    def _label_cpu(self, mask: np.ndarray, structure: np.ndarray) -> np.ndarray:
        """CPU connected component labeling."""
        print("  [CPU] Running connected component labeling...")
        labeled, self.num_regions = scipy_ndimage.label(mask, structure=structure)
        return labeled.astype(np.int32)

    def _filter_small_regions(self, labeled: np.ndarray, min_pixels: int) -> np.ndarray:
        """Remove regions smaller than threshold."""
        # Count pixels in each region
        region_ids, counts = np.unique(labeled[labeled > 0], return_counts=True)

        # Find regions to keep
        keep_regions = region_ids[counts >= min_pixels]

        # Create filtered array
        filtered = np.where(np.isin(labeled, keep_regions), labeled, 0)

        # Renumber regions sequentially
        renumber_map = np.zeros(labeled.max() + 1, dtype=np.int32)
        renumber_map[keep_regions] = np.arange(1, len(keep_regions) + 1)
        filtered = renumber_map[filtered]

        removed = self.num_regions - len(keep_regions)
        self.num_regions = len(keep_regions)
        print(f"  Removed {removed} small regions, kept {self.num_regions}")

        return filtered

    def calculate_region_statistics(self) -> pd.DataFrame:
        """Calculate statistics for each river system (vectorized for speed)."""
        if self.labeled_regions is None:
            raise ValueError("Run extract_river_systems() first!")

        print(f"\n{'='*70}")
        print("CALCULATING RIVER SYSTEM STATISTICS")
        print(f"{'='*70}")

        # Calculate pixel area based on CRS type
        if self.crs.is_geographic:
            # Geographic CRS - convert degrees to meters
            import math
            center_lat = (self.bounds.top + self.bounds.bottom) / 2
            meters_per_degree_lat = 111320
            meters_per_degree_lon = 111320 * math.cos(math.radians(center_lat))
            pixel_width_m = abs(self.transform[0]) * meters_per_degree_lon
            pixel_height_m = abs(self.transform[4]) * meters_per_degree_lat
            pixel_area = pixel_width_m * pixel_height_m
        else:
            # Projected CRS - use transform directly
            pixel_area = abs(self.transform[0] * self.transform[4])

        # Use vectorized operations for speed
        # Count pixels per region using bincount (much faster than loop)
        region_ids = self.labeled_regions.ravel()
        region_ids = region_ids[region_ids > 0]  # Exclude background
        pixel_counts = np.bincount(region_ids)[1:]  # Skip index 0 (background)

        # Get bounding boxes for all regions at once (much faster!)
        slices = scipy_ndimage.find_objects(self.labeled_regions)

        stats_list = []
        for region_id in range(1, self.num_regions + 1):
            if slices[region_id - 1] is None:  # Region doesn't exist (was filtered)
                continue

            pixel_count = int(pixel_counts[region_id - 1])
            area_m2 = pixel_count * pixel_area
            area_ha = area_m2 / 10000

            # Get bounding box from precomputed slices
            slice_obj = slices[region_id - 1]
            min_row = slice_obj[0].start
            max_row = slice_obj[0].stop - 1
            min_col = slice_obj[1].start
            max_col = slice_obj[1].stop - 1

            # Convert to geographic coordinates
            min_x, min_y = rasterio.transform.xy(self.transform, max_row, min_col, offset='ul')
            max_x, max_y = rasterio.transform.xy(self.transform, min_row, max_col, offset='ul')

            # Calculate skeleton-based linearity metrics
            # Only for regions > 100 pixels (skip tiny noise regions for speed)
            if pixel_count > 100:
                # Extract region subset for faster processing
                region_subset = self.labeled_regions[slice_obj[0], slice_obj[1]]
                region_mask = (region_subset == region_id)

                # Calculate morphological skeleton
                if region_mask.size > 0 and np.any(region_mask):
                    skeleton = skeletonize(region_mask)
                    skeleton_length = np.sum(skeleton)

                    # Linearity metrics
                    # Higher values = more elongated (river-like)
                    # Lower values = more compact (lake-like)
                    sqrt_area = np.sqrt(pixel_count)
                    linearity_index = skeleton_length / sqrt_area if sqrt_area > 0 else 0

                    # Compactness (perimeter^2 / area) - approximate with bbox
                    bbox_perimeter = 2 * ((max_row - min_row) + (max_col - min_col))
                    compactness = (bbox_perimeter ** 2) / pixel_count if pixel_count > 0 else 0
                else:
                    skeleton_length = 0
                    linearity_index = 0
                    compactness = 0
            else:
                # Skip skeleton calculation for tiny regions (assume noise)
                skeleton_length = 0
                linearity_index = 0
                compactness = 0

            stats_list.append({
                'river_id': region_id,
                'pixel_count': pixel_count,
                'area_m2': float(area_m2),
                'area_ha': float(area_ha),
                'skeleton_length': int(skeleton_length),
                'linearity_index': float(linearity_index),
                'compactness': float(compactness),
                'min_row': int(min_row),
                'max_row': int(max_row),
                'min_col': int(min_col),
                'max_col': int(max_col),
                'bbox_min_x': float(min_x),
                'bbox_min_y': float(min_y),
                'bbox_max_x': float(max_x),
                'bbox_max_y': float(max_y)
            })

        self.region_stats = pd.DataFrame(stats_list)

        # Sort only if we have data
        if len(self.region_stats) > 0:
            self.region_stats = self.region_stats.sort_values('area_m2', ascending=False).reset_index(drop=True)

        print(f"\nRiver System Statistics:")
        print(f"  Total systems: {len(self.region_stats)}")
        if len(self.region_stats) > 0:
            print(f"  Largest: {self.region_stats['area_ha'].max():.2f} ha")
            print(f"  Smallest: {self.region_stats['area_ha'].min():.2f} ha")
            print(f"  Mean size: {self.region_stats['area_ha'].mean():.2f} ha")

        return self.region_stats

    def get_river_by_id(self, river_id: int) -> np.ndarray:
        """Get binary mask for a specific river system."""
        if self.labeled_regions is None:
            raise ValueError("Run extract_river_systems() first!")
        return (self.labeled_regions == river_id)

    def get_largest_rivers(self, n: int = 1) -> List[int]:
        """Get IDs of the N largest river systems."""
        if self.region_stats is None:
            self.calculate_region_statistics()
        return self.region_stats.head(n)['river_id'].tolist()

    def rivers_to_polygons(self,
                          river_ids: Optional[List[int]] = None,
                          simplify_tolerance: float = 0.0) -> gpd.GeoDataFrame:
        """
        Convert river systems to clean polygon geometries.

        Args:
            river_ids: Specific river IDs to convert (None = all)
            simplify_tolerance: Simplify tolerance in map units (0 = no simplification)

        Returns:
            GeoDataFrame with river polygons
        """
        if self.labeled_regions is None:
            raise ValueError("Run extract_river_systems() first!")

        print(f"\n{'='*70}")
        print("CONVERTING TO POLYGONS")
        print(f"{'='*70}")

        if river_ids is None:
            # Convert all rivers
            mask_to_vectorize = (self.labeled_regions > 0).astype('uint8')
        else:
            # Convert specific rivers
            mask_to_vectorize = np.isin(self.labeled_regions, river_ids).astype('uint8')

        # Extract polygons
        polygons = []
        for geom, value in features.shapes(mask_to_vectorize,
                                          transform=self.transform,
                                          mask=mask_to_vectorize):
            if value == 1:
                poly = shape(geom)

                # Simplify if requested
                if simplify_tolerance > 0:
                    poly = poly.simplify(simplify_tolerance, preserve_topology=True)

                polygons.append(poly)

        # Create GeoDataFrame
        gdf = gpd.GeoDataFrame({'geometry': polygons}, crs=self.crs)
        gdf['river_id'] = range(1, len(gdf) + 1)

        # Calculate area in m² (reproject if geographic CRS)
        if self.crs.is_geographic:
            # Reproject to appropriate UTM zone for accurate area calculation
            # Estimate UTM zone from center longitude
            center_lon = (self.bounds.left + self.bounds.right) / 2
            utm_zone = int((center_lon + 180) / 6) + 1
            utm_epsg = 32600 + utm_zone if self.bounds.bottom >= 0 else 32700 + utm_zone
            gdf['area_m2'] = gdf.to_crs(epsg=utm_epsg).geometry.area
        else:
            gdf['area_m2'] = gdf.geometry.area

        gdf['area_ha'] = gdf['area_m2'] / 10000
        gdf = gdf.sort_values('area_m2', ascending=False).reset_index(drop=True)

        print(f"Created {len(gdf)} polygon(s)")
        if simplify_tolerance > 0:
            print(f"  Simplified with {simplify_tolerance}m tolerance")

        return gdf

    def export_labeled_raster(self, output_path: Union[str, Path]) -> Path:
        """Export labeled river systems as raster."""
        if self.labeled_regions is None:
            raise ValueError("Run extract_river_systems() first!")

        output_path = Path(output_path)

        with rasterio.open(
            output_path,
            'w',
            driver='GTiff',
            height=self.labeled_regions.shape[0],
            width=self.labeled_regions.shape[1],
            count=1,
            dtype=np.int32,
            crs=self.crs,
            transform=self.transform,
            compress='lzw',
            nodata=0
        ) as dst:
            dst.write(self.labeled_regions, 1)

        print(f"Exported labeled raster: {output_path}")
        return output_path

    def export_statistics(self, output_path: Union[str, Path]) -> Path:
        """Export river statistics."""
        if self.region_stats is None:
            self.calculate_region_statistics()

        output_path = Path(output_path)
        self.region_stats.to_csv(output_path, index=False)
        print(f"Exported statistics: {output_path}")
        return output_path


def extract_river_systems_workflow(raster_path: Union[str, Path],
                                   output_dir: Union[str, Path],
                                   water_value: int = 0,
                                   land_value: int = 1,
                                   connectivity: int = 8,
                                   min_area_m2: float = 1000,
                                   morphology_cleanup: int = 0,
                                   remove_ocean: bool = True,
                                   min_linearity: float = 0,
                                   simplify_tolerance: float = 1.0,
                                   use_gpu: bool = True) -> Dict:
    """
    Complete workflow: Extract river systems and export results.

    Args:
        raster_path: Path to binary water/land raster
        output_dir: Output directory
        water_value: Pixel value for water (default: 0)
        land_value: Pixel value for land (default: 1)
        connectivity: 4 or 8 neighbor connectivity (default: 8)
        min_area_m2: Minimum river area in m² (default: 1000)
        morphology_cleanup: Cleanup iterations (default: 0)
        remove_ocean: Remove largest water body (ocean) (default: True)
        min_linearity: Minimum linearity index (0=disabled) (default: 0)
        simplify_tolerance: Polygon simplification in meters (default: 1.0)
        use_gpu: Use GPU if available (default: True)

    Returns:
        Dictionary with results
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    raster_name = Path(raster_path).stem

    # Initialize
    extractor = RiverSystemExtractor(raster_path, use_gpu=use_gpu)

    # Extract river systems
    # Calculate pixel area based on CRS type
    if extractor.crs.is_geographic:
        # Geographic CRS (e.g., EPSG:4326) - convert degrees to meters
        import math
        # Get center latitude
        center_lat = (extractor.bounds.top + extractor.bounds.bottom) / 2

        # Convert degrees to meters at this latitude
        meters_per_degree_lat = 111320  # Constant
        meters_per_degree_lon = 111320 * math.cos(math.radians(center_lat))

        pixel_width_m = abs(extractor.transform[0]) * meters_per_degree_lon
        pixel_height_m = abs(extractor.transform[4]) * meters_per_degree_lat
        pixel_area_m2 = pixel_width_m * pixel_height_m

        print(f"\nGeographic CRS detected (latitude ~{center_lat:.2f}°)")
        print(f"  Pixel size: {pixel_width_m:.2f}m × {pixel_height_m:.2f}m")
    else:
        # Projected CRS - use transform directly (assumed to be in meters)
        pixel_area_m2 = abs(extractor.transform[0] * extractor.transform[4])
        print(f"\nProjected CRS detected")

    min_pixels = max(1, int(min_area_m2 / pixel_area_m2))

    print(f"\nCalculated filter:")
    print(f"  Pixel area: {pixel_area_m2:.2f} m²/pixel")
    print(f"  Min area threshold: {min_area_m2} m² = {min_pixels} pixels")

    labeled = extractor.extract_river_systems(
        water_value=water_value,
        land_value=land_value,
        connectivity=connectivity,
        min_area_pixels=min_pixels,
        morphology_cleanup=morphology_cleanup,
        remove_ocean=remove_ocean
    )

    # Calculate statistics
    stats = extractor.calculate_region_statistics()

    # Filter by linearity if requested
    if min_linearity > 0:
        print(f"\nFiltering by linearity...")
        print(f"  Min linearity index: {min_linearity}")
        before_count = len(stats)
        stats = stats[stats['linearity_index'] >= min_linearity].copy()
        after_count = len(stats)
        print(f"  Kept {after_count} systems (removed {before_count - after_count})")

        # Update region stats in extractor
        extractor.region_stats = stats
        extractor.num_regions = len(stats)

    # Export statistics
    stats_path = output_dir / f'{raster_name}_river_stats.csv'
    extractor.export_statistics(stats_path)

    # Export labeled raster
    labeled_path = output_dir / f'{raster_name}_rivers_labeled.tif'
    extractor.export_labeled_raster(labeled_path)

    # Export polygons
    gdf = extractor.rivers_to_polygons(simplify_tolerance=simplify_tolerance)
    polygon_path = output_dir / f'{raster_name}_rivers.gpkg'
    gdf.to_file(polygon_path, driver='GPKG')

    print(f"\n{'='*70}")
    print("WORKFLOW COMPLETE")
    print(f"{'='*70}")
    print(f"Output directory: {output_dir}")
    print(f"\nGenerated files:")
    print(f"  - {stats_path.name}")
    print(f"  - {labeled_path.name}")
    print(f"  - {polygon_path.name}")

    return {
        'extractor': extractor,
        'labeled_array': labeled,
        'statistics': stats,
        'polygons': gdf,
        'processing_time': extractor.processing_time
    }


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python region_group_optimized.py <raster_path> [output_dir]")
        print("\nExample:")
        print("  python region_group_optimized.py WaterLand_Classification.tif output/")
        print("\nExtracts individual river systems from binary water/land classification.")
        sys.exit(1)

    raster_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "river_systems_output"

    # Run workflow
    results = extract_river_systems_workflow(
        raster_path=raster_path,
        output_dir=output_dir,
        water_value=0,              # Water pixels
        land_value=1,                # Land pixels (excluded)
        connectivity=8,              # 8-neighbor connectivity
        min_area_m2=1000,           # Filter rivers < 0.1 hectare
        morphology_cleanup=0,        # No cleanup (set to 1-2 for noisy data)
        simplify_tolerance=1.0,      # Simplify polygons to 1m
        use_gpu=True                 # Auto GPU/CPU
    )

    print(f"\n✓ Complete! Found {results['extractor'].num_regions} river system(s)")
    print(f"  Processing time: {results['processing_time']:.2f} seconds")
