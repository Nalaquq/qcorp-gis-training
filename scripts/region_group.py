"""
Region Group Analysis for Binary Rasters
=========================================

Open-source replacement for ArcGIS Pro's Region Group tool.

This module identifies connected regions in a raster and assigns unique IDs to each
region. Equivalent to ArcGIS Spatial Analyst's Region Group tool.

Key Features:
- 4-neighbor or 8-neighbor connectivity
- Exclude specific values (e.g., land pixels)
- Zone grouping (group pixels of same value)
- Region statistics (area, pixel count, bounding box)
- Export labeled raster and statistics

Author: Nalaquq LLC / QCORP GIS Training
License: MIT
"""

import numpy as np
import rasterio
from rasterio import features
from scipy import ndimage
from scipy.ndimage import label
import geopandas as gpd
from shapely.geometry import box, shape
import pandas as pd
from pathlib import Path
from typing import Optional, Union, Tuple, Dict, List
import json


class RegionGroup:
    """
    Identify and analyze connected regions in a raster.

    Replicates ArcGIS Pro's Region Group tool functionality using scipy.
    """

    def __init__(self, raster_path: Union[str, Path]):
        """
        Initialize with path to raster.

        Args:
            raster_path: Path to input raster (typically binary water/land classification)
        """
        self.raster_path = Path(raster_path)
        self.data = None
        self.transform = None
        self.crs = None
        self.nodata = None
        self.labeled_regions = None
        self.num_regions = None
        self.region_stats = None
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
        print(f"  NoData value: {self.nodata}")

    def region_group(self,
                     neighbors: int = 8,
                     zone_grouping: str = 'within',
                     excluded_value: Optional[int] = None,
                     add_link: bool = False) -> np.ndarray:
        """
        Perform region grouping on raster.

        Args:
            neighbors: Connectivity (4 or 8). Default is 8.
                - 4: Only horizontal and vertical neighbors
                - 8: Include diagonal neighbors
            zone_grouping: How to group regions. Default is 'within'.
                - 'within': Group connected pixels with same value
                - 'cross': Group all pixels regardless of value (not common)
            excluded_value: Pixel value to exclude from grouping (e.g., 1 for land)
            add_link: Add LINK field showing original pixel value (default: False)

        Returns:
            Labeled array where each region has unique ID (0 = background/excluded)
        """
        print(f"\n{'='*60}")
        print("REGION GROUP ANALYSIS")
        print(f"{'='*60}")
        print(f"Parameters:")
        print(f"  Neighbors: {neighbors}")
        print(f"  Zone grouping: {zone_grouping}")
        print(f"  Excluded value: {excluded_value}")

        # Define connectivity structure
        if neighbors == 8:
            # 8-neighbor connectivity (includes diagonals)
            structure = np.array([[1, 1, 1],
                                 [1, 1, 1],
                                 [1, 1, 1]])
        elif neighbors == 4:
            # 4-neighbor connectivity (only horizontal/vertical)
            structure = np.array([[0, 1, 0],
                                 [1, 1, 1],
                                 [0, 1, 0]])
        else:
            raise ValueError("neighbors must be 4 or 8")

        # Create mask for pixels to include in grouping
        if excluded_value is not None:
            # Exclude specified value (e.g., land=1, only group water=0)
            mask = (self.data != excluded_value)
            if self.nodata is not None:
                mask = mask & (self.data != self.nodata)
        else:
            # Include all pixels except nodata
            if self.nodata is not None:
                mask = (self.data != self.nodata)
            else:
                mask = np.ones_like(self.data, dtype=bool)

        print(f"\nPixels to group: {np.sum(mask):,} ({np.sum(mask)/mask.size*100:.1f}%)")

        if zone_grouping == 'within':
            # Group connected pixels with SAME value
            # For binary water/land, this groups water regions separately
            labeled = np.zeros_like(self.data, dtype=np.int32)

            unique_values = np.unique(self.data[mask])
            print(f"Unique values to group: {unique_values}")

            current_label = 1
            for value in unique_values:
                # Get pixels with this value
                value_mask = (self.data == value) & mask

                # Label connected components
                value_labeled, n_features = label(value_mask, structure=structure)

                if n_features > 0:
                    # Renumber to avoid conflicts
                    value_labeled[value_labeled > 0] += (current_label - 1)
                    labeled[value_labeled > 0] = value_labeled[value_labeled > 0]
                    current_label += n_features

                    print(f"  Value {value}: {n_features} region(s)")

            self.num_regions = current_label - 1

        elif zone_grouping == 'cross':
            # Group ALL connected pixels regardless of value
            labeled, self.num_regions = label(mask, structure=structure)

        else:
            raise ValueError("zone_grouping must be 'within' or 'cross'")

        self.labeled_regions = labeled

        print(f"\n{'='*60}")
        print(f"REGION GROUP COMPLETE")
        print(f"{'='*60}")
        print(f"Total regions identified: {self.num_regions}")

        return labeled

    def calculate_region_statistics(self,
                                    min_pixels: int = 0) -> pd.DataFrame:
        """
        Calculate statistics for each labeled region.

        Args:
            min_pixels: Filter out regions smaller than this (default: 0)

        Returns:
            DataFrame with region statistics
        """
        if self.labeled_regions is None:
            raise ValueError("Run region_group() first!")

        print(f"\n{'='*60}")
        print("CALCULATING REGION STATISTICS")
        print(f"{'='*60}")

        stats_list = []

        for region_id in range(1, self.num_regions + 1):
            region_mask = (self.labeled_regions == region_id)
            pixel_count = np.sum(region_mask)

            if pixel_count < min_pixels:
                continue

            # Get original pixel value for this region
            original_value = self.data[region_mask][0]

            # Calculate area (m²) using pixel size from transform
            pixel_area = abs(self.transform[0] * self.transform[4])  # width * height
            area_m2 = pixel_count * pixel_area
            area_ha = area_m2 / 10000

            # Get bounding box
            rows, cols = np.where(region_mask)
            min_row, max_row = rows.min(), rows.max()
            min_col, max_col = cols.min(), cols.max()

            # Convert to geographic coordinates
            min_x, min_y = rasterio.transform.xy(self.transform, max_row, min_col, offset='ul')
            max_x, max_y = rasterio.transform.xy(self.transform, min_row, max_col, offset='ul')

            stats_list.append({
                'region_id': region_id,
                'value': int(original_value),
                'pixel_count': int(pixel_count),
                'area_m2': float(area_m2),
                'area_ha': float(area_ha),
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

        # Sort by area descending
        self.region_stats = self.region_stats.sort_values('area_m2', ascending=False)
        self.region_stats = self.region_stats.reset_index(drop=True)

        print(f"\nRegion Statistics Summary:")
        print(f"  Total regions: {len(self.region_stats)}")
        print(f"  Largest region: {self.region_stats['area_ha'].max():.2f} ha")
        print(f"  Smallest region: {self.region_stats['area_ha'].min():.2f} ha")
        print(f"  Mean region size: {self.region_stats['area_ha'].mean():.2f} ha")

        return self.region_stats

    def get_region_by_id(self, region_id: int) -> np.ndarray:
        """
        Get binary mask for a specific region.

        Args:
            region_id: Region ID to extract

        Returns:
            Binary mask (True = region, False = other)
        """
        if self.labeled_regions is None:
            raise ValueError("Run region_group() first!")

        return (self.labeled_regions == region_id)

    def get_largest_regions(self, n: int = 1) -> List[int]:
        """
        Get IDs of the N largest regions.

        Args:
            n: Number of largest regions to return

        Returns:
            List of region IDs sorted by size (largest first)
        """
        if self.region_stats is None:
            self.calculate_region_statistics()

        return self.region_stats.head(n)['region_id'].tolist()

    def filter_regions(self,
                       min_area_m2: Optional[float] = None,
                       max_area_m2: Optional[float] = None,
                       value: Optional[int] = None) -> np.ndarray:
        """
        Filter regions by criteria.

        Args:
            min_area_m2: Minimum area in square meters
            max_area_m2: Maximum area in square meters
            value: Filter by original pixel value

        Returns:
            Binary mask of pixels in filtered regions
        """
        if self.region_stats is None:
            self.calculate_region_statistics()

        # Start with all regions
        filtered = self.region_stats.copy()

        # Apply filters
        if min_area_m2 is not None:
            filtered = filtered[filtered['area_m2'] >= min_area_m2]
        if max_area_m2 is not None:
            filtered = filtered[filtered['area_m2'] <= max_area_m2]
        if value is not None:
            filtered = filtered[filtered['value'] == value]

        print(f"Filtered regions: {len(filtered)}/{len(self.region_stats)}")

        # Create mask
        filtered_ids = filtered['region_id'].values
        mask = np.isin(self.labeled_regions, filtered_ids)

        return mask

    def export_labeled_raster(self,
                              output_path: Union[str, Path],
                              dtype: str = 'int32') -> Path:
        """
        Export labeled regions as a raster.

        Args:
            output_path: Output file path
            dtype: Data type for output ('int16', 'int32', etc.)

        Returns:
            Path to saved file
        """
        if self.labeled_regions is None:
            raise ValueError("Run region_group() first!")

        output_path = Path(output_path)

        # Convert dtype
        dtype_map = {
            'int16': np.int16,
            'int32': np.int32,
            'uint16': np.uint16,
            'uint32': np.uint32
        }

        if dtype not in dtype_map:
            raise ValueError(f"dtype must be one of {list(dtype_map.keys())}")

        output_data = self.labeled_regions.astype(dtype_map[dtype])

        # Write raster
        with rasterio.open(
            output_path,
            'w',
            driver='GTiff',
            height=output_data.shape[0],
            width=output_data.shape[1],
            count=1,
            dtype=output_data.dtype,
            crs=self.crs,
            transform=self.transform,
            compress='lzw',
            nodata=0
        ) as dst:
            dst.write(output_data, 1)

        print(f"\nExported labeled raster to: {output_path}")
        return output_path

    def export_statistics(self,
                         output_path: Union[str, Path],
                         format: str = 'csv') -> Path:
        """
        Export region statistics to file.

        Args:
            output_path: Output file path
            format: Output format ('csv', 'json', 'excel')

        Returns:
            Path to saved file
        """
        if self.region_stats is None:
            self.calculate_region_statistics()

        output_path = Path(output_path)

        if format == 'csv':
            self.region_stats.to_csv(output_path, index=False)
        elif format == 'json':
            self.region_stats.to_json(output_path, orient='records', indent=2)
        elif format == 'excel':
            self.region_stats.to_excel(output_path, index=False)
        else:
            raise ValueError("format must be 'csv', 'json', or 'excel'")

        print(f"Exported statistics to: {output_path}")
        return output_path

    def regions_to_polygons(self,
                           region_ids: Optional[List[int]] = None,
                           simplify_tolerance: float = 0.0) -> gpd.GeoDataFrame:
        """
        Convert regions to polygon geometries.

        Args:
            region_ids: Specific region IDs to convert (None = all)
            simplify_tolerance: Simplify tolerance in map units

        Returns:
            GeoDataFrame with polygon geometries
        """
        if self.labeled_regions is None:
            raise ValueError("Run region_group() first!")

        if region_ids is None:
            # Convert all regions
            mask_to_vectorize = (self.labeled_regions > 0).astype('uint8')
        else:
            # Convert specific regions
            mask_to_vectorize = np.isin(self.labeled_regions, region_ids).astype('uint8')

        # Extract polygons
        polygons = []
        for geom, value in features.shapes(mask_to_vectorize,
                                          transform=self.transform,
                                          mask=mask_to_vectorize):
            if value == 1:
                poly = shape(geom)

                if simplify_tolerance > 0:
                    poly = poly.simplify(simplify_tolerance, preserve_topology=True)

                polygons.append(poly)

        # Create GeoDataFrame
        gdf = gpd.GeoDataFrame({'geometry': polygons}, crs=self.crs)

        # Add region information
        if self.region_stats is not None:
            # Match polygons to regions (this is approximate)
            gdf['area_m2'] = gdf.geometry.area
            gdf = gdf.sort_values('area_m2', ascending=False).reset_index(drop=True)

        print(f"\nConverted {len(gdf)} region(s) to polygons")

        return gdf

    def visualize_regions(self,
                         show_labels: bool = False,
                         figsize: Tuple[int, int] = (12, 10)):
        """
        Visualize the labeled regions.

        Args:
            show_labels: Whether to show region IDs as text
            figsize: Figure size (width, height)
        """
        import matplotlib.pyplot as plt
        from matplotlib import colors

        if self.labeled_regions is None:
            raise ValueError("Run region_group() first!")

        # Create figure
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize)

        # Plot original raster
        ax1.imshow(self.data, cmap='Blues_r')
        ax1.set_title('Original Raster', fontsize=14, fontweight='bold')
        ax1.axis('off')

        # Plot labeled regions with random colors
        cmap = plt.cm.tab20
        norm = colors.Normalize(vmin=0, vmax=self.num_regions)

        im = ax2.imshow(self.labeled_regions, cmap=cmap, norm=norm)
        ax2.set_title(f'Region Groups (n={self.num_regions})', fontsize=14, fontweight='bold')
        ax2.axis('off')

        # Add colorbar
        plt.colorbar(im, ax=ax2, label='Region ID')

        # Optionally add region ID labels
        if show_labels and self.region_stats is not None:
            for _, row in self.region_stats.head(10).iterrows():  # Show top 10
                center_row = (row['min_row'] + row['max_row']) // 2
                center_col = (row['min_col'] + row['max_col']) // 2
                ax2.text(center_col, center_row, str(row['region_id']),
                        color='white', fontsize=8, ha='center', va='center',
                        bbox=dict(boxstyle='round', facecolor='black', alpha=0.5))

        plt.tight_layout()
        plt.show()


def region_group_workflow(raster_path: Union[str, Path],
                         output_dir: Union[str, Path],
                         neighbors: int = 8,
                         excluded_value: Optional[int] = 1,
                         min_area_m2: float = 1000,
                         export_polygons: bool = True,
                         export_labeled_raster: bool = True,
                         visualize: bool = False) -> Dict:
    """
    Complete region group workflow.

    Args:
        raster_path: Path to input binary raster
        output_dir: Directory for outputs
        neighbors: Connectivity (4 or 8)
        excluded_value: Value to exclude (e.g., 1 for land)
        min_area_m2: Minimum region area to keep
        export_polygons: Export regions as polygons
        export_labeled_raster: Export labeled raster
        visualize: Show visualization

    Returns:
        Dictionary with results
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    raster_name = Path(raster_path).stem

    # Initialize
    rg = RegionGroup(raster_path)

    # Run region grouping
    labeled = rg.region_group(
        neighbors=neighbors,
        zone_grouping='within',
        excluded_value=excluded_value
    )

    # Calculate statistics
    stats = rg.calculate_region_statistics(min_pixels=0)

    # Filter by minimum area
    if min_area_m2 > 0:
        filtered_mask = rg.filter_regions(min_area_m2=min_area_m2)
        print(f"\nFiltered regions (min area: {min_area_m2} m²)")

    # Export statistics
    stats_path = output_dir / f'{raster_name}_region_stats.csv'
    rg.export_statistics(stats_path, format='csv')

    # Export labeled raster
    if export_labeled_raster:
        labeled_path = output_dir / f'{raster_name}_labeled.tif'
        rg.export_labeled_raster(labeled_path, dtype='int32')

    # Export polygons
    if export_polygons:
        gdf = rg.regions_to_polygons(simplify_tolerance=1.0)
        polygon_path = output_dir / f'{raster_name}_regions.gpkg'
        gdf.to_file(polygon_path, driver='GPKG')
        print(f"Exported polygons to: {polygon_path}")

    # Visualize
    if visualize:
        rg.visualize_regions(show_labels=True)

    return {
        'region_group': rg,
        'labeled_array': labeled,
        'statistics': stats,
        'polygons': gdf if export_polygons else None
    }


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python region_group.py <raster_path> [output_dir]")
        print("\nExample:")
        print("  python region_group.py WaterLand_Classification.tif output/")
        print("\nThis script performs region grouping on a binary raster,")
        print("identifying connected regions (like ArcGIS Region Group tool).")
        sys.exit(1)

    raster_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "region_group_output"

    print("\n" + "="*70)
    print("REGION GROUP ANALYSIS")
    print("="*70)
    print(f"Input raster: {raster_path}")
    print(f"Output directory: {output_dir}")
    print("="*70 + "\n")

    # Run workflow
    results = region_group_workflow(
        raster_path=raster_path,
        output_dir=output_dir,
        neighbors=8,              # 8-neighbor connectivity
        excluded_value=1,         # Exclude land (value=1)
        min_area_m2=1000,        # Filter regions < 0.1 hectare
        export_polygons=True,
        export_labeled_raster=True,
        visualize=False
    )

    print("\n" + "="*70)
    print("ANALYSIS COMPLETE")
    print("="*70)
    print(f"Total regions: {results['region_group'].num_regions}")
    print(f"Output directory: {output_dir}")
    print("\nGenerated files:")
    print(f"  - {Path(raster_path).stem}_region_stats.csv")
    print(f"  - {Path(raster_path).stem}_labeled.tif")
    print(f"  - {Path(raster_path).stem}_regions.gpkg")
    print("\nOpen in QGIS or ArcGIS Pro to view results.")
