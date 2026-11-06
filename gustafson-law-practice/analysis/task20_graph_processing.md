# Task 20: Parallel Graph Traversal & Irregular Workloads

## 1. Structural Comparison: Graph Analytics vs. Dense Linear Algebra

| Characteristic | Dense Linear Algebra (GEMM / Stencil) | Irregular Graph Processing (BFS / PageRank) |
| :--- | :--- | :--- |
| **Memory Access Pattern** | Continuous, predictable strided access | Pointer-chasing, random memory lookups |
| **Data Locality** | High L1/L2 cache spatial & temporal locality | Extremely low cache reuse; cache miss dominated |
| **Communication Pattern** | Structured nearest-neighbor / 3D block | Unstructured all-to-all frontier exchange |
| **Work Distribution** | Uniform grid decomposition | Highly skewed (power-law degree distribution) |
| **Synchronization** | Barrier at phase boundaries | Fine-grained atomic locks / dynamic barriers |

---

## 2. Why Gustafson Weak Scaling Fails on Graphs

1. **Power-Law Vertices (High-Degree Hubs):** Scale-free graphs feature hub vertices connected to a large fraction of total edges. Processing hub neighbors forces high atomic contention and memory channel bottlenecks, creating severe load imbalance.
2. **Frontier Imbalance Across Steps:** In BFS, active frontier sizes vary dramatically per level (small $\to$ giant component $\to$ long tail). Processors assigned to inactive components sit idle during synchronization barriers.
3. **NUMA Interconnect Latency:** Weak scaling expands total vertex count $V$. Cross-node pointer traversals over interconnects (e.g., PCIe / Infinity Fabric) incur memory latencies $10\text{x}$ higher than local L3 cache reads.

Consequently, serial/synchronization overhead $a(P)$ grows monotonically with core count $P$, making constant-runtime weak scaling nearly unachievable for scale-free graph traversals.
