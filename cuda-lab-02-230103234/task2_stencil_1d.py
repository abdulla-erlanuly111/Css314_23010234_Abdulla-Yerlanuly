import numpy as np
from numba import cuda

@cuda.jit
def stencil_1d(d_in, d_out, N):
    idx = cuda.grid(1)
    if idx < N:
        if idx == 0:
            left = d_in[0]
        else:
            left = d_in[idx - 1]

        if idx == N - 1:
            right = d_in[N - 1]
        else:
            right = d_in[idx + 1]

        center = d_in[idx]

        d_out[idx] = 0.25 * left + 0.5 * center + 0.25 * right

def cpu_stencil(arr):
    padded = np.pad(arr, (1, 1), mode='edge')
    return 0.25 * padded[:-2] + 0.5 * padded[1:-1] + 0.25 * padded[2:]

def run_stencil(h_in):
    N = len(h_in)
    d_in = cuda.to_device(h_in)
    d_out = cuda.device_array(N, dtype=np.float32)

    threads_per_block = 256
    blocks_per_grid = (N + threads_per_block - 1) // threads_per_block

    stencil_1d[blocks_per_grid, threads_per_block](d_in, d_out, N)
    cuda.synchronize()

    return d_out.copy_to_host()

if __name__ == "__main__":
    N = 100007
    test_in = np.sin(np.linspace(0, 10, N)).astype(np.float32)
    h_gpu = run_stencil(test_in)
    h_cpu = cpu_stencil(test_in)

    delta = np.max(np.abs(h_gpu - h_cpu))
    assert np.allclose(h_gpu, h_cpu, atol=1e-4)
    print(f"TASK 2 PASSED: MAX DELTA = {delta}")
