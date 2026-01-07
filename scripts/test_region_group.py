"""
Test script for region_group.py

This script creates a synthetic binary raster and tests the region grouping
functionality without needing actual satellite data.

Run this to verify that region_group.py works correctly!
"""

import numpy as np
import rasterio
from rasterio.transform import from_origin
from pathlib import Path
import shutil

from region_group import RegionGroup, region_group_workflow


def create_synthetic_test_raster(output_path: str = "test_water_land.tif"):
    """
    Create a synthetic binary water/land raster for testing.

    This creates:
    - 1 main river channel (largest)
    - 2 smaller river channels
    - Several small isolated water bodies
    - Land (value=1) as background
    """
    print("Creating synthetic test raster...")

    # Create 300x300 raster
    height, width = 300, 300
    data = np.ones((height, width), dtype=np.uint8)  # Start with all land (1)

    # Main river channel (horizontal with some curves)
    for i in range(50, 250):
        y = 150 + int(20 * np.sin(i / 20))
        for offset in range(-5, 6):
            if 0 <= y + offset < height:
                data[y + offset, i] = 0  # Water (0)

    # Secondary river channel (diagonal)
    for i in range(100, 200):
        y = i
        x = i
        for offset in range(-3, 4):
            if 0 <= y + offset < height and 0 <= x < width:
                data[y + offset, x] = 0

    # Small tributary
    for i in range(50, 100):
        y = 200
        x = i
        for offset in range(-2, 3):
            if 0 <= y + offset < height:
                data[y + offset, x] = 0

    # Add some isolated small water bodies (ponds)
    # Small pond 1
    data[50:60, 50:60] = 0

    # Small pond 2
    data[250:265, 250:265] = 0

    # Tiny water pixel (noise)
    data[100, 100] = 0
    data[200, 50] = 0

    # Create transform (10m pixel resolution, arbitrary coordinates)
    transform = from_origin(-161.90, 59.75, 10, 10)

    # Write raster
    with rasterio.open(
        output_path,
        'w',
        driver='GTiff',
        height=height,
        width=width,
        count=1,
        dtype=data.dtype,
        crs='EPSG:32603',  # UTM Zone 3N (Alaska)
        transform=transform,
        nodata=255
    ) as dst:
        dst.write(data, 1)

    print(f"✓ Created test raster: {output_path}")
    print(f"  Size: {height}x{width} pixels")
    print(f"  Resolution: 10m")
    print(f"  Water pixels: {np.sum(data == 0):,}")
    print(f"  Land pixels: {np.sum(data == 1):,}")

    return output_path


def test_basic_region_grouping():
    """Test basic region grouping functionality."""
    print("\n" + "="*70)
    print("TEST 1: Basic Region Grouping")
    print("="*70)

    # Create test raster
    test_raster = create_synthetic_test_raster()

    # Run region grouping
    rg = RegionGroup(test_raster)
    labeled = rg.region_group(
        neighbors=8,
        zone_grouping='within',
        excluded_value=1  # Exclude land
    )

    # Calculate statistics
    stats = rg.calculate_region_statistics()

    # Validate
    assert rg.num_regions > 0, "Should detect at least 1 region"
    assert len(stats) > 0, "Should have statistics"
    assert 'area_m2' in stats.columns, "Should calculate area"

    print(f"\n✅ TEST PASSED: Found {rg.num_regions} regions")
    print("\nTop 5 regions by area:")
    print(stats[['region_id', 'area_ha', 'pixel_count']].head())

    # Clean up
    Path(test_raster).unlink()

    return True


def test_4_vs_8_neighbors():
    """Compare 4-neighbor vs 8-neighbor connectivity."""
    print("\n" + "="*70)
    print("TEST 2: 4-Neighbor vs 8-Neighbor Connectivity")
    print("="*70)

    test_raster = create_synthetic_test_raster()

    # Test 8-neighbor
    rg8 = RegionGroup(test_raster)
    rg8.region_group(neighbors=8, excluded_value=1)
    regions_8 = rg8.num_regions

    # Test 4-neighbor
    rg4 = RegionGroup(test_raster)
    rg4.region_group(neighbors=4, excluded_value=1)
    regions_4 = rg4.num_regions

    print(f"\n8-neighbor connectivity: {regions_8} regions")
    print(f"4-neighbor connectivity: {regions_4} regions")
    print(f"Difference: {regions_4 - regions_8} more regions with 4-neighbor")

    # 4-neighbor should find more (or equal) regions than 8-neighbor
    assert regions_4 >= regions_8, "4-neighbor should find >= regions than 8-neighbor"

    print(f"\n✅ TEST PASSED")

    Path(test_raster).unlink()

    return True


def test_filtering():
    """Test region filtering by size."""
    print("\n" + "="*70)
    print("TEST 3: Region Filtering")
    print("="*70)

    test_raster = create_synthetic_test_raster()

    rg = RegionGroup(test_raster)
    rg.region_group(neighbors=8, excluded_value=1)

    all_stats = rg.calculate_region_statistics()
    print(f"\nAll regions: {len(all_stats)}")

    # Filter: Keep only regions > 1000 m² (10 hectares)
    filtered_mask = rg.filter_regions(min_area_m2=1000)

    # Count filtered regions
    filtered_ids = np.unique(rg.labeled_regions[filtered_mask])
    filtered_ids = filtered_ids[filtered_ids > 0]  # Exclude background

    print(f"Regions > 1000 m²: {len(filtered_ids)}")
    print(f"Filtered out: {len(all_stats) - len(filtered_ids)} small regions")

    assert len(filtered_ids) < len(all_stats), "Should filter out some regions"

    print(f"\n✅ TEST PASSED")

    Path(test_raster).unlink()

    return True


def test_largest_region():
    """Test extracting largest region."""
    print("\n" + "="*70)
    print("TEST 4: Extract Largest Region")
    print("="*70)

    test_raster = create_synthetic_test_raster()

    rg = RegionGroup(test_raster)
    rg.region_group(neighbors=8, excluded_value=1)

    # Get largest region
    largest_ids = rg.get_largest_regions(n=1)
    largest_mask = rg.get_region_by_id(largest_ids[0])

    largest_pixels = np.sum(largest_mask)
    print(f"\nLargest region ID: {largest_ids[0]}")
    print(f"Largest region pixels: {largest_pixels}")

    # Get stats
    stats = rg.calculate_region_statistics()
    largest_area = stats.iloc[0]['area_ha']
    print(f"Largest region area: {largest_area:.2f} ha")

    assert largest_pixels > 0, "Should find largest region"

    print(f"\n✅ TEST PASSED")

    Path(test_raster).unlink()

    return True


def test_export_functions():
    """Test export functionality."""
    print("\n" + "="*70)
    print("TEST 5: Export Functions")
    print("="*70)

    test_raster = create_synthetic_test_raster()
    output_dir = Path("test_region_group_output")
    output_dir.mkdir(exist_ok=True)

    rg = RegionGroup(test_raster)
    rg.region_group(neighbors=8, excluded_value=1)
    rg.calculate_region_statistics()

    # Test labeled raster export
    labeled_path = rg.export_labeled_raster(output_dir / "test_labeled.tif")
    assert labeled_path.exists(), "Should create labeled raster"
    print(f"✓ Exported labeled raster: {labeled_path}")

    # Test statistics export
    stats_path = rg.export_statistics(output_dir / "test_stats.csv", format='csv')
    assert stats_path.exists(), "Should create statistics CSV"
    print(f"✓ Exported statistics: {stats_path}")

    # Test polygon export
    gdf = rg.regions_to_polygons(simplify_tolerance=1.0)
    polygon_path = output_dir / "test_polygons.gpkg"
    gdf.to_file(polygon_path, driver='GPKG')
    assert polygon_path.exists(), "Should create polygon GeoPackage"
    print(f"✓ Exported polygons: {polygon_path}")

    print(f"\n✅ TEST PASSED: All exports created successfully")

    # Clean up
    Path(test_raster).unlink()
    shutil.rmtree(output_dir)

    return True


def test_complete_workflow():
    """Test the complete workflow function."""
    print("\n" + "="*70)
    print("TEST 6: Complete Workflow Function")
    print("="*70)

    test_raster = create_synthetic_test_raster()
    output_dir = Path("test_workflow_output")

    # Run complete workflow
    results = region_group_workflow(
        raster_path=test_raster,
        output_dir=output_dir,
        neighbors=8,
        excluded_value=1,
        min_area_m2=500,
        export_polygons=True,
        export_labeled_raster=True,
        visualize=False  # Don't show plots in test
    )

    # Validate results
    assert results['region_group'] is not None, "Should return RegionGroup object"
    assert results['statistics'] is not None, "Should return statistics"
    assert results['polygons'] is not None, "Should return polygons"
    assert output_dir.exists(), "Should create output directory"

    # Check files were created
    files = list(output_dir.glob("*"))
    assert len(files) >= 3, f"Should create at least 3 files, found {len(files)}"

    print(f"\n✅ TEST PASSED: Complete workflow executed successfully")
    print(f"Created {len(files)} output files in {output_dir}")

    # Clean up
    Path(test_raster).unlink()
    shutil.rmtree(output_dir)

    return True


def run_all_tests():
    """Run all tests."""
    print("\n" + "#"*70)
    print("# REGION GROUP TEST SUITE")
    print("#"*70)

    tests = [
        ("Basic Region Grouping", test_basic_region_grouping),
        ("4 vs 8 Neighbors", test_4_vs_8_neighbors),
        ("Region Filtering", test_filtering),
        ("Largest Region", test_largest_region),
        ("Export Functions", test_export_functions),
        ("Complete Workflow", test_complete_workflow)
    ]

    passed = 0
    failed = 0

    for test_name, test_func in tests:
        try:
            test_func()
            passed += 1
        except Exception as e:
            print(f"\n❌ TEST FAILED: {test_name}")
            print(f"Error: {e}")
            failed += 1

    print("\n" + "#"*70)
    print("# TEST RESULTS")
    print("#"*70)
    print(f"Passed: {passed}/{len(tests)}")
    print(f"Failed: {failed}/{len(tests)}")

    if failed == 0:
        print("\n✅ ALL TESTS PASSED! region_group.py is working correctly.")
        print("\nYou can now use region_group.py with confidence on your real data!")
    else:
        print(f"\n⚠️  {failed} test(s) failed. Please review the errors above.")

    return failed == 0


if __name__ == "__main__":
    import sys

    # Check if matplotlib is available (optional for visualization tests)
    try:
        import matplotlib
        matplotlib.use('Agg')  # Use non-interactive backend for testing
    except ImportError:
        print("Note: matplotlib not available, skipping visualization tests")

    success = run_all_tests()

    sys.exit(0 if success else 1)
