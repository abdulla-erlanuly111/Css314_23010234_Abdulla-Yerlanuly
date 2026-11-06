# Task 18: N-Body Gravitational Problem Scaling

## 1. Algorithmic Regimes Overview

Simulating gravitational interactions among $N$ particles under weak scaling (keeping iteration time constant on $P$ processors) yields fundamentally different scaling behaviors depending on the algorithm used:
1. **Direct All-Pairs Method:** Computational complexity $O(N^2)$, spatial complexity $O(N)$.
2. **Barnes-Hut Octree Method:** Computational complexity $O(N \log N)$, spatial complexity $O(N)$.

---

## 2. Scaling Derivations under Constant Iteration Time

### Regime A: Direct All-Pairs Method ($O(N^2)$)
Per-iteration time on $P$ processors:

$$T(P) = \frac{c_1 \cdot N^2}{P} = K \implies N(P) = \sqrt{\frac{K \cdot P}{c_1}} = O(P^{1/2})$$

- **Particle Growth:** Particle count $N$ scales with $P^{1/2}$.
- **Communication Overhead:** All-to-all particle position exchange requires $O(N)$ data transfer per node:

$$C_{\text{comm}} = O(P^{1/2})$$

- **Ratio Shift:** Compute per process stays constant ($O(1)$), while communication scales as $O(P^{1/2})$. The serial/communication fraction $a(P)$ **increases** with processor count, degrading efficiency at large $P$.

---

### Regime B: Barnes-Hut Octree Method ($O(N \log N)$)
Per-iteration time on $P$ processors:

$$T(P) = \frac{c_2 \cdot N \log N}{P} = K \implies N \log N = O(P)$$

Using the Lambert $W$ function asymptote, $N(P) \approx O\left(\frac{P}{\log P}\right)$:
- **Particle Growth:** $N$ scales almost linearly with $P$.
- **Tree Construction Overhead:** Building and synchronizing global octrees introduces an $O(\log P)$ serial synchronization term per iteration.
- **Ratio Shift:** Tree traversals cause irregular memory lookups and cache misses, making the non-parallelizable fraction $a$ sensitive to tree depth expansion as $P$ grows.
