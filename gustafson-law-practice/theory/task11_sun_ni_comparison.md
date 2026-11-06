# Task 11: Sun and Ni Memory-Bounded Speedup Comparison

## 1. Context and Motivation

In 1993, Sun and Ni introduced **Memory-Bounded Speedup** as a generalized formulation unifying Amdahl's fixed-size model and Gustafson's fixed-time model based on physical memory availability.

---

## 2. Mathematical Formulation

Let $M$ be memory capacity per node, and $G(M)$ represent compute workload growth permitted by $M$ units of memory:

$$S_{\text{Sun-Ni}}(P) = \frac{s + (1 - s) \cdot G(P)}{s + \frac{(1 - s) \cdot G(P)}{P}}$$

- **Case 1 ($G(P) = 1$):** Memory utilization is fixed $\implies$ Reduces to Amdahl's Law.
- **Case 2 ($G(P) = P$):** Workload scales linearly with memory capacity $\implies$ Reduces to Gustafson's Law.
- **Case 3 ($G(P) > P$):** Compute work grows faster than memory footprint (e.g., matrix multiplication $O(N^3)$ ops vs $O(N^2)$ memory) $\implies$ Super-Gustafson scaling.

---

## 3. Conditions of Divergence

1. **Overestimation by Gustafson:** If memory access bandwidth limits execution or memory growth forces disk swapping ($G(P) < P$), Gustafson's law overestimates speedup.
2. **Underestimation by Gustafson:** For algorithms where compute complexity outpaces spatial complexity ($G(P) > P$), Sun-Ni predicts higher speedup than Gustafson's linear model.
