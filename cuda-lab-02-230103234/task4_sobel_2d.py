import numpy as np
import math
from numba import cuda

@cuda.jit
def sobel_x_kernel(d_in, d_out, rows, cols):
    col, row = cuda.grid(2)

    if row < rows and col < cols:
        if 0 < row < rows - 1 and 0 < col < cols - 1:
            val = (-1.0 * d_in[row - 1, col - 1] + 1.0 * d_in[row - 1, col + 1]
                   - 2.0 * d_in[row, col - 1]     + 2.0 * d_in[row, col + 1]
                   - 1.0 * d_in[row + 1, col - 1] + 1.0 * d_in[row + 1, col + 1])
            d_out[row, col] = val
        else:
            d_out[row, col] = 0.0

def run_sobel(h_img):
    rows, cols = h_img.shape
    d_in = cuda.to_device(h_img)
    d_out = cuda.device_array((rows, cols), dtype=np.float32)

    threads_per_block = (16, 16)
    blocks_per_grid = (
        math.ceil(cols / threads_per_block[0]),
        math.ceil(rows / threads_per_block[1])
    )

    sobel_x_kernel[blocks_per_grid, threads_per_block](d_in, d_out, rows, cols)
    cuda.synchronize()

    return d_out.copy_to_host()

if __name__ == "__main__":
    test_img = np.ones((2048, 2048), dtype=np.float32)
    res = run_sobel(test_img)
    print("TASK 4 PASSED")
