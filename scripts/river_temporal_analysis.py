"""
Temporal River Change Analysis

This module compares river polygons across multiple dates to detect:
- Channel migration
- New channels (avulsion, braiding)
- Abandoned channels
- Area changes

Author: Nalaquq LLC / QCORP GIS Training
License: MIT
"""

import numpy as np
import geopandas as gpd
from shapely.geometry import shape, mapping
from shapely.ops import unary_union
from pathlib import Path
from typing import List, Dict, Tuple, Union, Optional
import pandas as pd
from datetime import datetime


class RiverTemporalAnalyzer:
    """
    Analyze changes in river channel geometry over time.
    """

    def __init__(self, river_gdfs: List[gpd.GeoDataFrame], dates: List[str]):
        """
        Initialize with river polygons from multiple dates.

        Args:
            river_gdfs: List of GeoDataFrames, one per date
            dates: List of date strings (e.g., ['2024-05-01', '2024-10-30'])
        """
        if len(river_gdfs) != len(dates):
            raise ValueError("Number of GeoDataFrames must match number of dates")

        self.river_gdfs = river_gdfs
        self.dates = dates
        self.n_dates = len(dates)

        # Create unified geometries
        self.unified_geoms = [gdf.unary_union for gdf in river_gdfs]

        print(f"Initialized temporal analysis with {self.n_dates} dates")

    def calculate_area_changes(self) -> pd.DataFrame:
        """
        Calculate river area for each date.

        Returns:
            DataFrame with dates and areas
        """
        areas = []
        for gdf, date in zip(self.river_gdfs, self.dates):
            total_area_m2 = gdf.geometry.area.sum()
            areas.append({
                'date': date,
                'area_m2': total_area_m2,
                'area_ha': total_area_m2 / 10000,
                'num_polygons': len(gdf)
            })

        df = pd.DataFrame(areas)
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values('date')

        # Calculate changes
        df['area_change_ha'] = df['area_ha'].diff()
        df['area_change_pct'] = df['area_ha'].pct_change() * 100

        return df

    def detect_gains_and_losses(self,
                                date_idx1: int,
                                date_idx2: int) -> Dict[str, gpd.GeoDataFrame]:
        """
        Compare two dates to detect new water (gains) and lost water (losses).

        Args:
            date_idx1: Index of earlier date
            date_idx2: Index of later date

        Returns:
            Dictionary with 'gained', 'lost', 'stable' GeoDataFrames
        """
        date1 = self.dates[date_idx1]
        date2 = self.dates[date_idx2]

        geom1 = self.unified_geoms[date_idx1]
        geom2 = self.unified_geoms[date_idx2]

        print(f"\nComparing {date1} → {date2}")

        # Calculate differences
        gained = geom2.difference(geom1)  # New water in date2
        lost = geom1.difference(geom2)    # Water lost from date1
        stable = geom1.intersection(geom2)  # Unchanged water

        # Convert to GeoDataFrames
        crs = self.river_gdfs[0].crs

        gained_gdf = gpd.GeoDataFrame(
            {'geometry': [gained], 'change_type': 'gained'},
            crs=crs
        )
        gained_gdf['area_m2'] = gained_gdf.geometry.area

        lost_gdf = gpd.GeoDataFrame(
            {'geometry': [lost], 'change_type': 'lost'},
            crs=crs
        )
        lost_gdf['area_m2'] = lost_gdf.geometry.area

        stable_gdf = gpd.GeoDataFrame(
            {'geometry': [stable], 'change_type': 'stable'},
            crs=crs
        )
        stable_gdf['area_m2'] = stable_gdf.geometry.area

        # Add date information
        for gdf in [gained_gdf, lost_gdf, stable_gdf]:
            gdf['date1'] = date1
            gdf['date2'] = date2

        # Print statistics
        print(f"  Gained water: {gained_gdf['area_m2'].sum() / 10000:.2f} ha")
        print(f"  Lost water: {lost_gdf['area_m2'].sum() / 10000:.2f} ha")
        print(f"  Stable water: {stable_gdf['area_m2'].sum() / 10000:.2f} ha")

        return {
            'gained': gained_gdf,
            'lost': lost_gdf,
            'stable': stable_gdf
        }

    def create_change_map(self,
                         date_idx1: int,
                         date_idx2: int,
                         output_path: Optional[Union[str, Path]] = None) -> gpd.GeoDataFrame:
        """
        Create a combined change map showing gains, losses, and stable areas.

        Args:
            date_idx1: Index of earlier date
            date_idx2: Index of later date
            output_path: Optional path to save output

        Returns:
            Combined GeoDataFrame with all change types
        """
        changes = self.detect_gains_and_losses(date_idx1, date_idx2)

        # Combine all change types
        change_map = pd.concat([
            changes['gained'],
            changes['lost'],
            changes['stable']
        ], ignore_index=True)

        # Add color codes for visualization
        color_map = {
            'gained': '#00FF00',   # Green
            'lost': '#FF0000',     # Red
            'stable': '#0000FF'    # Blue
        }
        change_map['color'] = change_map['change_type'].map(color_map)

        if output_path:
            output_path = Path(output_path)
            change_map.to_file(output_path, driver='GPKG')
            print(f"\nSaved change map to: {output_path}")

        return change_map

    def calculate_migration_distance(self,
                                     date_idx1: int,
                                     date_idx2: int,
                                     num_samples: int = 100) -> Dict:
        """
        Estimate channel migration distance by sampling boundary points.

        Args:
            date_idx1: Index of earlier date
            date_idx2: Index of later date
            num_samples: Number of points to sample along boundary

        Returns:
            Dictionary with migration statistics
        """
        geom1 = self.unified_geoms[date_idx1]
        geom2 = self.unified_geoms[date_idx2]

        # Sample points along boundary of date1
        boundary1 = geom1.boundary

        # Sample evenly spaced points
        distances_list = []
        for i in np.linspace(0, boundary1.length, num_samples):
            point = boundary1.interpolate(i)
            distance = point.distance(geom2.boundary)
            distances_list.append(distance)

        distances = np.array(distances_list)

        stats = {
            'mean_migration_m': float(np.mean(distances)),
            'max_migration_m': float(np.max(distances)),
            'min_migration_m': float(np.min(distances)),
            'std_migration_m': float(np.std(distances)),
            'date1': self.dates[date_idx1],
            'date2': self.dates[date_idx2]
        }

        print(f"\nMigration Statistics ({self.dates[date_idx1]} → {self.dates[date_idx2]}):")
        print(f"  Mean migration: {stats['mean_migration_m']:.2f} m")
        print(f"  Max migration: {stats['max_migration_m']:.2f} m")
        print(f"  Min migration: {stats['min_migration_m']:.2f} m")

        return stats

    def detect_new_channels(self,
                           date_idx1: int,
                           date_idx2: int,
                           min_area_m2: float = 1000) -> gpd.GeoDataFrame:
        """
        Identify new channels (potential avulsions or braiding).

        Args:
            date_idx1: Index of earlier date
            date_idx2: Index of later date
            min_area_m2: Minimum area to consider as a new channel

        Returns:
            GeoDataFrame with new channel polygons
        """
        changes = self.detect_gains_and_losses(date_idx1, date_idx2)
        gained = changes['gained']

        # Explode to separate polygons
        gained_exploded = gained.explode(index_parts=True).reset_index(drop=True)

        # Filter by minimum area
        new_channels = gained_exploded[gained_exploded.geometry.area >= min_area_m2].copy()

        new_channels['channel_area_m2'] = new_channels.geometry.area
        new_channels['channel_area_ha'] = new_channels.channel_area_m2 / 10000

        print(f"\nDetected {len(new_channels)} new channels (>{min_area_m2} m²)")

        return new_channels

    def detect_abandoned_channels(self,
                                 date_idx1: int,
                                 date_idx2: int,
                                 min_area_m2: float = 1000) -> gpd.GeoDataFrame:
        """
        Identify abandoned channels.

        Args:
            date_idx1: Index of earlier date
            date_idx2: Index of later date
            min_area_m2: Minimum area to consider as an abandoned channel

        Returns:
            GeoDataFrame with abandoned channel polygons
        """
        changes = self.detect_gains_and_losses(date_idx1, date_idx2)
        lost = changes['lost']

        # Explode to separate polygons
        lost_exploded = lost.explode(index_parts=True).reset_index(drop=True)

        # Filter by minimum area
        abandoned = lost_exploded[lost_exploded.geometry.area >= min_area_m2].copy()

        abandoned['channel_area_m2'] = abandoned.geometry.area
        abandoned['channel_area_ha'] = abandoned.channel_area_m2 / 10000

        print(f"\nDetected {len(abandoned)} abandoned channels (>{min_area_m2} m²)")

        return abandoned

    def generate_report(self, output_dir: Union[str, Path]) -> Dict:
        """
        Generate comprehensive temporal analysis report.

        Args:
            output_dir: Directory to save report files

        Returns:
            Dictionary with all analysis results
        """
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        print(f"\n{'='*70}")
        print("GENERATING TEMPORAL ANALYSIS REPORT")
        print(f"{'='*70}")

        report = {}

        # 1. Area changes over time
        print("\n[1/4] Calculating area changes...")
        area_df = self.calculate_area_changes()
        area_df.to_csv(output_dir / 'area_changes.csv', index=False)
        report['area_changes'] = area_df

        # 2. Pairwise comparisons
        print("\n[2/4] Detecting gains and losses...")
        change_maps = []
        for i in range(self.n_dates - 1):
            change_map = self.create_change_map(
                i, i + 1,
                output_path=output_dir / f'change_map_{self.dates[i]}_to_{self.dates[i+1]}.gpkg'
            )
            change_maps.append(change_map)
        report['change_maps'] = change_maps

        # 3. Migration distances
        print("\n[3/4] Calculating migration distances...")
        migration_stats = []
        for i in range(self.n_dates - 1):
            stats = self.calculate_migration_distance(i, i + 1)
            migration_stats.append(stats)

        migration_df = pd.DataFrame(migration_stats)
        migration_df.to_csv(output_dir / 'migration_distances.csv', index=False)
        report['migration_stats'] = migration_df

        # 4. New and abandoned channels
        print("\n[4/4] Detecting channel changes...")
        for i in range(self.n_dates - 1):
            new_channels = self.detect_new_channels(i, i + 1)
            abandoned_channels = self.detect_abandoned_channels(i, i + 1)

            if len(new_channels) > 0:
                new_channels.to_file(
                    output_dir / f'new_channels_{self.dates[i]}_to_{self.dates[i+1]}.gpkg',
                    driver='GPKG'
                )

            if len(abandoned_channels) > 0:
                abandoned_channels.to_file(
                    output_dir / f'abandoned_channels_{self.dates[i]}_to_{self.dates[i+1]}.gpkg',
                    driver='GPKG'
                )

        print(f"\n{'='*70}")
        print("REPORT COMPLETE")
        print(f"{'='*70}")
        print(f"All results saved to: {output_dir}")

        return report


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python river_temporal_analysis.py <output_dir> <polygon1.gpkg> <date1> <polygon2.gpkg> <date2> ...")
        print("\nExample:")
        print("  python river_temporal_analysis.py analysis_output river_2024-05.gpkg 2024-05-01 river_2024-10.gpkg 2024-10-30")
        sys.exit(1)

    output_dir = sys.argv[1]
    args = sys.argv[2:]

    if len(args) % 2 != 0:
        print("ERROR: Must provide pairs of <polygon_file> <date>")
        sys.exit(1)

    # Parse polygon files and dates
    gdfs = []
    dates = []

    for i in range(0, len(args), 2):
        polygon_path = args[i]
        date = args[i + 1]

        print(f"Loading: {polygon_path} ({date})")
        gdf = gpd.read_file(polygon_path)
        gdfs.append(gdf)
        dates.append(date)

    # Run analysis
    analyzer = RiverTemporalAnalyzer(gdfs, dates)
    report = analyzer.generate_report(output_dir)

    print("\n✓ Done! Check output directory for results.")
