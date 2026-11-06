# Task 01: Strong Scaling vs. Weak Scaling Foundations

## Executive Summary

Parallel computing performance modeling is dominated by two foundational frameworks: Gene Amdahl's Strong Scaling Model (1967) and John Gustafson's Weak Scaling Model (1988). This document contrasts their philosophical assumptions, physical realities, and mathematical limiting behavior as processor count $P \rightarrow \infty$.

---

## 1. Foundational Assumptions: Amdahl vs. Gustafson

### Gene Amdahl's Model (1967) — Strong Scaling
Amdahl's Law assumes a **fixed problem size** ($W_{total} = \text{const}$). When additional processing units $P$ are applied to the workload:
* The workload is divided into a strictly serial fraction $s \in [0, 1]$ and a perfectly parallelizable fraction $p = 1 - s$.
* As $P$ increases, the parallel portion scales down as $\frac{p}{P}$, while the serial execution time $s$ remains unchanged.
* **Philosophical Premise:** "How fast can we solve a fixed-size problem by throwing more hardware at it?"

### John Gustafson's Model (1988) — Weak Scaling
Gustafson's Law assumes a **fixed execution time** ($T(P) = \text{const}$). As processing power expands:
* The problem size $W(P)$ expands linearly with processor count $P$.
* The serial overhead $s$ remains invariant in absolute clock time, while the parallel workload $p \cdot P$ grows proportionally to available compute capacity.
* **Philosophical Premise:** "How large a problem can we solve in a given, acceptable timeframe using more hardware?"

---

## 2. Mathematical Definition of Problem Dimension Scaling

Let $N$ represent the characteristic dimension of the problem (e.g., matrix size $N \times N$, or grid count in a 3D simulation domain).

### Amdahl's Model: $N(P) = O(1)$
Under Amdahl's formulation:
$$\lim_{P \rightarrow \infty} N(P) = N_0$$

The total computational work $W(N)$ is invariant:
$$W(P) = W_s + W_p = \text{const}$$

As $P \rightarrow \infty$, execution time $T(P)$ asymptotically approaches the serial bottleneck:
$$\lim_{P \rightarrow \infty} T(P) = T_s = s \cdot T(1)$$

### Gustafson's Model: $N(P) \rightarrow \infty$
Under Gustafson's weak scaling formulation, workload scales linearly with processor count $P$:
$$W(P) = W_s + P \cdot W_p$$

For a computational workload with complexity $O(N^d)$ in $d$ dimensions:
$$N(P) = O\left(P^{1/d}\right)$$

As processor count scales to infinity:
$$\lim_{P \rightarrow \infty} N(P) = \infty$$

While execution time remains bounded:
$$T(P) = T_s + T_p = \text{const}$$

---

## 3. Comparison Matrix: Fixed-Size vs. Fixed-Time Scaling

| Feature / Dimension | Amdahl's Law (Strong Scaling) | Gustafson's Law (Weak Scaling) |
| :--- | :--- | :--- |
| **Primary Metric** | Time-to-solution reduction | Workload capacity expansion |
| **Problem Size $W$** | Fixed ($W(P) = W_0$) | Scaled ($W(P) = s + p \cdot P$) |
| **Execution Time $T$** | Decreases ($T(P) \rightarrow s \cdot T(1)$) | Constant ($T(P) = T_{target}$) |
| **Serial Fraction** | Measured on uniprocessor ($s$) | Observed on parallel system ($a$) |
| **Speedup Ceiling** | $\lim_{P \to \infty} S_{Amdahl} = \frac{1}{s}$ | $\lim_{P \to \infty} S_{Gustafson} = \infty$ (linear in $P$) |
| **Parallel Efficiency** | $\lim_{P \to \infty} E(P) = 0$ | $\lim_{P \to \infty} E(P) = 1 - a$ |
| **Target Application** | Time-critical real-time processing | High-resolution scientific simulation |

---

## 4. Physical & Architectural Divergence

1. **Hardware Memory Contraction vs. Expansion:** In strong scaling, per-core memory footprint decreases ($\frac{M_{total}}{P}$), eventually causing cache fits or memory access latencies to dominate overhead. In weak scaling, per-core memory footprint stays constant ($M_{node} = \text{const}$), fully utilizing distributed memory architectures.
2. **Serial Overhead Interpretation:** Amdahl treats serial fraction $s$ as a fundamental property of the algorithm. Gustafson demonstrates that serial fraction $a$ shrinks relative to total work as problem capacity grows, exposing the "Amdahl's Pessimism" fallacy for scalable HPC workloads.
