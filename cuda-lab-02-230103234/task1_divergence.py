import numpy as np
import time
from numba import cuda

N = 1048576

@cuda.jit
def kernel_a(y):
    idx = cuda.grid(1)
    if idx < y.size:
        val = y[idx]
        for _ in range(1000):
            val = val * 1.0001 + 0.0001
        y[idx] = val

@cuda.jit
def kernel_b(y):
    idx = cuda.grid(1)
    if idx < y.size:
        val = y[idx]
        if idx % 2 == 0:
            for _ in range(1000):
                val = val * 1.0001 + 0.0001
        else:
            for _ in range(1000):
                val = (val - 0.0001) / 1.0001
        y[idx] = val

@cuda.jit
def kernel_c(y):
    idx = cuda.grid(1)
    if idx < y.size:
        val = y[idx]
        warp_id = idx // 32
        if warp_id % 2 == 0:
            for _ in range(1000):
                val = val * 1.0001 + 0.0001
        else:
            for _ in range(1000):
                val = (val - 0.0001) / 1.0001
        y[idx] = val

def benchmark_kernel(kernel, d_data, threads_per_block, blocks_per_grid):
    kernel[blocks_per_grid, threads_per_block](d_data)
    cuda.synchronize()

    times = []
    for _ in range(10):
        t0 = time.perf_counter()
        kernel[blocks_per_grid, threads_per_block](d_data)
        cuda.synchronize()
        t1 = time.perf_counter()
        times.append((t1 - t0) * 1000.0)

    return np.mean(times)

def run():
    h_data = np.ones(N, dtype=np.float32)
    d_data = cuda.to_device(h_data)

    threads_per_block = 256
    blocks_per_grid = (N + threads_per_block - 1) // threads_per_block

    time_a = benchmark_kernel(kernel_a, d_data, threads_per_block, blocks_per_grid)
    time_b = benchmark_kernel(kernel_b, d_data, threads_per_block, blocks_per_grid)
    time_c = benchmark_kernel(kernel_c, d_data, threads_per_block, blocks_per_grid)

    print(f"Kernel A (Uniform Path): {time_a:.3f} ms")
    print(f"Kernel B (Full Divergence): {time_b:.3f} ms")
    print(f"Kernel C (Warp-Aligned Branching): {time_c:.3f} ms")

if __name__ == "__main__":
    run()
