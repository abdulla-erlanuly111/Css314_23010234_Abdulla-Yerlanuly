# Task 13: Boundary Cases: When Weak Scaling Fails

## 1. Failure Mode 1: Algorithmic Complexity Shift

### Case: Fast Fourier Transform (FFT) & Sorting
In 1D FFT or Parallel Radix Sort, computational complexity scales as $O(N \log N)$. Under weak scaling, work per core $K = N/P$ is kept constant, making total work $N = K \cdot P$:

$$\text{Work}_{\text{total}} = O(K \cdot P \log(K \cdot P))$$

Per-core execution time becomes:

$$T(P) = O\left(\frac{K \cdot P \log(K \cdot P)}{P}\right) = O(\log P)$$

Because execution time increases as $O(\log P)$ rather than remaining constant, the constant runtime premise of Gustafson's Law breaks down.

---

## 2. Failure Mode 2: Global Synchronization Bottlenecks

### Case: Parallel Graph Breadth-First Search (BFS)
In graph processing on scale-free power-law graphs (e.g., Graph500 benchmark), frontier expansion requires global barriers and all-to-all communication at each tree level:
- As processor count $P$ expands, message counts scale as $O(P^2)$ due to high-degree hub vertices.
- Network congestion leads to barrier synchronization stalls.
- Serial fraction $a(P)$ grows monotonically with $P$, causing performance degradation at scale.
