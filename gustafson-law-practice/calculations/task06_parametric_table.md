# Task 06: Parametric Speedup Across Processor Densities

## 1. Problem Formulation

Given an application where the observed parallel machine serial fraction is $a = 0.04$ (4%), calculate theoretical scaled speedup $S(P)$ and parallel efficiency $E(P)$ under Gustafson's model across processor counts $P \in \{16, 64, 256, 1024, 4096, 16384\}$.

### Mathematical Models
- **Gustafson Scaled Speedup:** $S(P) = P - a(P - 1) = 0.96P + 0.04$
- **Parallel Efficiency:** $E(P) = \frac{S(P)}{P} = 0.96 + \frac{0.04}{P}$

---

## 2. Calculation & Evaluation Table

| Processor Count ($P$) | Serial Fraction ($a$) | Scaled Speedup $S(P)$ | Parallel Efficiency $E(P)$ | Efficiency Loss ($1 - E$) |
| :--- | :--- | :--- | :--- | :--- |
| **1** | 0.04 | 1.0000 | 100.00% | 0.00% |
| **16** | 0.04 | 15.4000 | 96.25% | 3.75% |
| **64** | 0.04 | 61.4800 | 96.06% | 3.94% |
| **256** | 0.04 | 245.8000 | 96.02% | 3.98% |
| **1,024** | 0.04 | 983.0800 | 96.00% | 4.00% |
| **4,096** | 0.04 | 3,932.2000 | 96.00% | 4.00% |
| **16,384** | 0.04 | 15,728.6800 | 96.00% | 4.00% |

---

## 3. Evaluation & Analytical Findings

1. **Efficiency Stabilization:** As $P$ expands exponentially from 16 to 16,384, parallel efficiency $E(P)$ asymptotes rapidly to $1 - a = 0.96$ (96.00%).
2. **Contrast with Strong Scaling:** Under Amdahl's Law with $s = 0.04$, speedup would hit a hard ceiling of $S_A(16384) \approx 24.96$ with an efficiency of $E(16384) \approx 0.15\%$. Weak scaling maintains 96% hardware efficiency regardless of core expansion.
