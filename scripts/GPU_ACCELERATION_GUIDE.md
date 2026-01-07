# GPU Acceleration for Region Grouping

**Speed up region grouping 10-100x for large rasters**

Your system: **NVIDIA RTX A4000 Laptop GPU** + **Intel i7-11850H (8-core)** + **15GB RAM**

---

## Performance Comparison (Estimated)

| Method | Time for 290M pixels | Speedup | Requirements |
|--------|---------------------|---------|--------------|
| **CPU (scipy)** | 3-5 minutes | 1x (baseline) | None |
| **Multi-core (Dask)** | 30-60 seconds | 3-6x | Multi-core CPU |
| **GPU (CuPy)** | 5-15 seconds | **12-36x** | NVIDIA GPU + CUDA |
| **GPU (cuCIM)** | 3-10 seconds | **18-60x** | NVIDIA GPU + CUDA |

---

## Option 1: CuPy (RECOMMENDED for your system)

**Best for:** Quick setup, drop-in replacement for NumPy/SciPy

### Installation

```bash
# Check CUDA version
nvidia-smi

# Install CuPy (for CUDA 11.x)
pip install cupy-cuda11x

# OR for CUDA 12.x
pip install cupy-cuda12x
```

### Usage

```python
import cupy as cp
from cupyx.scipy import ndimage as cp_ndimage

# Load raster to GPU
gpu_data = cp.asarray(cpu_data)

# Run region grouping on GPU
labeled_gpu, num_regions = cp_ndimage.label(
    gpu_data == 0,  # water mask
    structure=cp.ones((3, 3))  # 8-neighbor
)

# Copy result back to CPU
labeled_cpu = cp.asnumpy(labeled_gpu)
```

**Pros:**
- ✅ Easy drop-in replacement for scipy
- ✅ 10-30x faster for your RTX A4000
- ✅ Works with existing code structure

**Cons:**
- ⚠️ Requires NVIDIA GPU + CUDA
- ⚠️ Limited to GPU memory (~8GB for A4000)

---

## Option 2: Dask (CPU Parallelization)

**Best for:** No GPU, or rasters larger than GPU memory

### Installation

```bash
pip install "dask[array]" dask-image
```

### Usage

```python
import dask.array as da
from dask_image.ndmeasure import label

# Load raster as Dask array (chunked)
dask_data = da.from_array(cpu_data, chunks=(2000, 2000))

# Run region grouping in parallel
labeled, num_regions = label(dask_data == 0)

# Compute result
labeled_cpu = labeled.compute()
```

**Pros:**
- ✅ No GPU required
- ✅ Handles rasters larger than RAM
- ✅ 3-6x faster on your 8-core CPU

**Cons:**
- ⚠️ Slower than GPU
- ⚠️ More complex setup for optimal chunking

---

## Option 3: RAPIDS cuCIM (Advanced)

**Best for:** Production workflows, maximum speed

### Installation

```bash
# Requires CUDA 11.x or 12.x
# Best installed via conda
conda create -n rapids-env -c rapidsai -c conda-forge \
    cudf=24.02 cucim=24.02 python=3.10 cudatoolkit=11.8

conda activate rapids-env
```

### Usage

```python
import cupy as cp
from cucim.skimage.measure import label

# Load to GPU
gpu_data = cp.asarray(cpu_data)

# Run region grouping
labeled_gpu = label(gpu_data == 0, connectivity=2)  # 2=8-neighbor

# Copy back
labeled_cpu = cp.asnumpy(labeled_gpu)
```

**Pros:**
- ✅ Fastest option (18-60x speedup)
- ✅ Full suite of GPU-accelerated image processing

**Cons:**
- ⚠️ Complex installation (conda recommended)
- ⚠️ Requires NVIDIA GPU + CUDA

---

## Hybrid Approach (RECOMMENDED)

Use GPU when available, fall back to CPU:

```python
try:
    import cupy as cp
    from cupyx.scipy import ndimage as ndimage_module
    USE_GPU = True
    print("Using GPU acceleration")
except ImportError:
    import numpy as np
    from scipy import ndimage as ndimage_module
    USE_GPU = False
    print("Using CPU (install cupy for GPU acceleration)")

def region_group_accelerated(data, neighbors=8):
    if USE_GPU:
        # Transfer to GPU
        gpu_data = cp.asarray(data)
        structure = cp.ones((3, 3)) if neighbors == 8 else ...
        labeled, num = ndimage_module.label(gpu_data, structure=structure)
        # Transfer back to CPU
        return cp.asnumpy(labeled), int(num)
    else:
        # CPU fallback
        structure = np.ones((3, 3)) if neighbors == 8 else ...
        return ndimage_module.label(data, structure=structure)
```

---

## Memory Considerations

### Your RTX A4000 Specs:
- **GPU Memory:** ~8 GB GDDR6
- **System RAM:** 15 GB

### Memory Requirements (approximate):

| Raster Size | Pixels | CPU RAM | GPU RAM |
|-------------|--------|---------|---------|
| Small | 10M | ~80 MB | ~80 MB |
| **Your raster** | **290M** | **~2.3 GB** | **~2.3 GB** |
| Large | 500M | ~4 GB | ~4 GB |
| Very Large | 1B+ | ~8+ GB | Use Dask + chunking |

**Your 290M pixel raster will fit comfortably in GPU memory!**

---

## Implementation Plan

### Phase 1: Add CuPy Support (Quick Win)

1. Install CuPy:
   ```bash
   pip install cupy-cuda11x  # or cuda12x
   ```

2. Modify `region_group.py` to detect and use GPU

3. Test with your WaterLand_Classification(4).tif

**Expected speedup:** 10-30x faster (3-5 min → 10-20 sec)

### Phase 2: Optimize for Very Large Rasters

1. Add Dask support for chunked processing
2. Handle rasters > 8GB (larger than GPU memory)
3. Implement progressive processing with progress bars

**Expected speedup:** Handle rasters up to 2 billion pixels

### Phase 3: Batch Processing Optimization

1. Keep data on GPU between multiple operations
2. Batch temporal analysis (process multiple dates together)
3. GPU-accelerated raster to polygon conversion

**Expected speedup:** 5-10x additional speedup for batch workflows

---

## Quick Test: Check if GPU is Ready

```bash
# Test CUDA availability
python3 -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}')"

# Check CuPy installation
python3 -c "import cupy as cp; print(f'CuPy version: {cp.__version__}'); print(cp.cuda.runtime.getDeviceCount(), 'GPU(s) detected')"
```

---

## Next Steps

**Immediate (today):**
1. Install CuPy
2. Create `region_group_gpu.py` with GPU support
3. Test on your WaterLand_Classification(4).tif

**Short-term (this week):**
1. Benchmark CPU vs GPU performance
2. Integrate GPU version into main workflow
3. Add progress bars for user feedback

**Long-term (next month):**
1. Add Dask support for distributed processing
2. Implement GPU batch processing for temporal analysis
3. Optimize memory usage for 1B+ pixel rasters

---

## Troubleshooting

### "CUDA out of memory"
- Raster too large for GPU memory (> 8GB)
- Solution: Use Dask chunking or smaller tiles

### "ImportError: No module named 'cupy'"
- CuPy not installed
- Solution: `pip install cupy-cuda11x`

### "cupy.cuda.compiler.CompileException"
- CUDA version mismatch
- Solution: Check `nvidia-smi`, install matching cupy version

### "Slower than CPU!"
- Data transfer overhead for small rasters
- Solution: Only use GPU for rasters > 10M pixels

---

## References

- [CuPy Documentation](https://docs.cupy.dev/)
- [RAPIDS cuCIM](https://docs.rapids.ai/api/cucim/stable/)
- [Dask Image](https://image.dask.org/)
- [Region Grouping Performance Study](https://github.com/rapidsai/cucim/blob/main/benchmarks/)

---

**Author:** Nalaquq LLC / QCORP GIS Training
**Hardware:** Optimized for NVIDIA RTX A4000
