# Task 17: 3D Stencil Hydrodynamics Surface Scaling

## 1. Problem Definition

In a 7-point 3D finite-difference stencil solver on a cubic domain of size $N \times N \times N$:
- **Computation (Interior points):** Scales with volume $V = O(N^3)$
- **Communication (Boundary exchanges):** Scales with surface area $A = O(N^2)$

Demonstrate how the communication-to-computation ratio behaves under Gustafson weak scaling.

---

## 2. Mathematical Proof

### Case 1: 3D Subdomain Block Decomposition (Optimal)
Divide $N \times N \times N$ domain into $P$ cubic subdomains, each of size $n \times n \times n$ where $n = N / P^{1/3}$.
Under weak scaling, volume per process $n^3$ is held constant.

- **Local Computation per process:** $W_{\text{local}} = O(n^3) = \text{Constant}$
- **Local Communication per process:** $C_{\text{local}} = 6 \cdot O(n^2) = \text{Constant}$

Communication-to-computation ratio per process:

$$\frac{\text{Comm}}{\text{Comp}} = \frac{O(n^2)}{O(n^3)} = \frac{1}{O(n)} = \text{Constant}$$

Under 3D block decomposition, the communication-to-computation ratio **remains constant** as $P \to \infty$.

---

### Case 2: 1D Slab Decomposition (Sub-optimal)
Divide domain along a single dimension into $P$ slabs of size $N \times N \times \left(\frac{N}{P}\right)$.
Under weak scaling, $N \propto P^{1/3}$:

- **Local Computation per process:** $W_{\text{local}} = \frac{O(N^3)}{P} = \text{Constant}$
- **Local Communication (2 faces):** $C_{\text{local}} = 2 \cdot O(N^2) \propto O((P^{1/3})^2) = O(P^{2/3})$

Communication-to-computation ratio per process:

$$\frac{\text{Comm}}{\text{Comp}} = \frac{O(P^{2/3})}{\text{Constant}} = O(P^{2/3}) \to \infty$$

### Conclusion
1D slab decomposition causes communication overhead to explode as $O(P^{2/3})$, breaking weak scaling. High-performance hydrodynamics codes must utilize 3D domain decomposition to preserve Gustafson efficiency.
