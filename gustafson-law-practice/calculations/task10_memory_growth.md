# Task 10: Memory Growth Rate vs. Scaled Speedup

## 1. Mathematical Formulation

Under pure weak scaling, aggregate problem workload scales linearly with core count: $W(P) = P \cdot W(1)$.
For a 3D grid-based solver on a cubic domain of dimension $N \times N \times N$:
- Total volume (work / grid points): $V = N^3$
- Aggregate memory footprint: $M(N) = c \cdot N^3$

Given a hardware memory limit of **32 GB per node**, calculate the maximum global domain dimension $N$ for cluster configurations of 64 and 512 nodes.

---

## 2. Per-Node Capacity & Sub-grid Bounds

Assume double-precision floating-point arithmetic ($b = 8$ bytes per grid point scalar):

$$\text{Memory Cap per Node} = 32 \text{ GB} = 32 \times 2^{30} \text{ bytes} = 34,359,738,368 \text{ bytes}$$

Maximum grid points per node $n^3$:

$$n^3 = \frac{34,359,738,368}{8} = 4,294,967,296 \text{ points}$$

Maximum per-node grid edge dimension $n$:

$$n = \sqrt[3]{4,294,967,296} = 1,625.498 \implies n_{\max} = 1,625$$

---

## 3. Global Grid Scaling Calculations

Assuming optimal 3D spatial decomposition across $P$ nodes where global grid dimension $N = P^{1/3} \cdot n_{\max}$:

### Case A: $P = 64$ Nodes
$$N_{64} = (64)^{1/3} \cdot 1,625 = 4 \cdot 1,625 = 6,500$$

- **Global Domain Grid:** $6,500 \times 6,500 \times 6,500$
- **Total Points ($N^3$):** $2.74625 \times 10^{11}$ points
- **Total Aggregate Memory:** $64 \times 32 \text{ GB} = 2,048 \text{ GB} = 2.0 \text{ TB}$

### Case B: $P = 512$ Nodes
$$N_{512} = (512)^{1/3} \cdot 1,625 = 8 \cdot 1,625 = 13,000$$

- **Global Domain Grid:** $13,000 \times 13,000 \times 13,000$
- **Total Points ($N^3$):** $2.197 \times 10^{12}$ points
- **Total Aggregate Memory:** $512 \times 32 \text{ GB} = 16,384 \text{ GB} = 16.0 \text{ TB}$
