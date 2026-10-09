# CUDA Lab 02: Advanced Geometries & Stencils

**Student ID:** 230103234

**Allocated GPU Node:** Tesla T4

**CUDA Compute Capability:** 7.5

**Official Verification Token:** 0EA77240CBC6F793EA66

## Task 1 Benchmark Results

| Kernel | Execution Time (ms) | Hardware Impact / Description |
| :--- | :--- | :--- |
| **Kernel A** | 18.081 ms | Uniform Path (No Divergence) |
| **Kernel B** | 93.496 ms | Full Divergence (Interleaved Threads) |
| **Kernel C** | 46.815 ms | Warp-Aligned Branching (Uniform per Warp) |

## Repository Structure

```text
cuda-lab-02-230103234/
├── README.md
├── task1_divergence.py
├── task2_stencil_1d.py
├── task3_grid_stride.py
├── task4_sobel_2d.py
└── verify_submission.py
