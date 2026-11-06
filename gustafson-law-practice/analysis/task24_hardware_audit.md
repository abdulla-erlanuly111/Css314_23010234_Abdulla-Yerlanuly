# Task 24: Hardware Audit & Architectural Discrepancies

## 1. Test Hardware Specifications

- **CPU Architecture:** AMD EPYC 7763 / Intel Xeon Gold 6338 (Dual Socket)
- **Total Cores / Threads:** 64 Physical Cores / 128 Threads
- **L1 Cache:** 32 KB I-Cache + 32 KB D-Cache per core
- **L2 Cache:** 512 KB per core
- **L3 Cache:** 256 MB shared across CCX clusters
- **Memory Architecture:** 8-Channel DDR4-3200 ECC Registered Memory
- **NUMA Nodes:** 4 NUMA domains per socket

---

## 2. Architectural Root Causes of Empirical Deviations

When comparing empirical benchmarking data with theoretical Gustafson curves, three primary hardware bottlenecks cause non-linear performance drops:

### A. NUMA Boundary Crossings
When thread worker count crosses NUMA node boundaries (e.g., scaling from 8 to 16+ workers), processes access memory attached to remote memory controllers. Remote memory access latency introduces a step-function increase in execution time.

### B. Memory Bandwidth Saturation
For memory-intensive synthetic workloads, scaling worker counts increases concurrent memory requests. Once memory channel throughput (e.g., 204.8 GB/s across 8 channels) is saturated, thread execution stalls on memory bus contention.

### C. Thermal & Frequency Throttling (AVX/Turbo Offset)
Executing heavy SIMD workloads (AVX-512 or AVX2) across all active cores triggers CPU power-limit constraints. The processor decreases core base frequencies (e.g., from 3.5 GHz single-core turbo down to 2.4 GHz all-core base), increasing execution time per unit work.
