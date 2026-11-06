# Task 16: Dense Matrix Multiplication (GEMM) Scaling

## 1. Problem Formulation

For dense matrix multiplication ($C = A \times B$) on $N \times N$ matrices:
- Computational Workload: $W(N) = O(N^3)$ operations
- Memory Space Complexity: $M(N) = O(N^2)$ footprint

Under Gustafson's assumption, parallel wall-clock execution time $T(P)$ remains constant as processor count $P$ increases. Derive how matrix dimension $N$ must scale with $P$.

---

## 2. Derivation of Dimension Growth Rate

Set parallel execution time $T(P)$ as work divided by processor count:

$$T(P) = \frac{O(N^3)}{P} = \text{Constant } K$$

Solve for $N^3$:

$$N^3 = K \cdot P \implies N(P) = (K \cdot P)^{1/3} = O(P^{1/3})$$

Thus, to maintain constant execution time under weak scaling, matrix edge dimension $N$ must scale with the **cube root of processor count** $P^{1/3}$.

---

## 3. Tabular Target Scaling Values

Normalizing baseline at $P = 1$ to $N_1 = 1,000$:

| Processors ($P$) | Scaling Factor ($P^{1/3}$) | Matrix Dimension ($N$) | Total Work ($O(N^3)$) | Memory Footprint ($O(N^2)$) | Memory / Processor |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | 1.0000 | 1,000 | $1 \times 10^9$ ops | 24 MB | 24.0 MB |
| **8** | 2.0000 | 2,000 | $8 \times 10^9$ ops | 96 MB | 12.0 MB |
| **64** | 4.0000 | 4,000 | $64 \times 10^9$ ops | 384 MB | 6.0 MB |
| **512** | 8.0000 | 8,000 | $512 \times 10^9$ ops | 1,536 MB | 3.0 MB |
| **4,096** | 16.0000 | 16,000 | $4,096 \times 10^9$ ops | 6,144 MB | 1.5 MB |

---

## 4. Key Observation

While total workload scales linearly with $P$, per-processor memory requirements decrease as $O(P^{-1/3})$. GEMM under Gustafson weak scaling is compute-bound rather than memory-capacity bound.
