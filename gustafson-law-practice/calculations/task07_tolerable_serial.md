# Task 07: Reverse Engineering Maximum Tolerable Serial Overhead

## 1. Problem Statement

A high-performance supercomputing cluster consists of $P = 8,192$ processing cores. Operational requirements dictate that scaled speedup must achieve at least $S(P) \ge 7,500$. Derive and compute the maximum allowable parallel serial fraction $a_{\max}$.

---

## 2. Algebraic Derivation

Starting from Gustafson's speedup equation:

$$S(P) = P - a(P - 1)$$

Set $S(P) \ge S_{\text{target}}$:

$$P - a(P - 1) \ge S_{\text{target}}$$

Rearrange to solve for serial fraction $a$:

$$P - S_{\text{target}} \ge a(P - 1)$$

$$a \le \frac{P - S_{\text{target}}}{P - 1}$$

Thus, the maximum tolerable serial fraction $a_{\max}$ is:

$$a_{\max} = \frac{P - S_{\text{target}}}{P - 1}$$

---

## 3. Numerical Calculation

Substitute $P = 8,192$ and $S_{\text{target}} = 7,500$:

$$a_{\max} = \frac{8,192 - 7,500}{8,192 - 1} = \frac{692}{8,191}$$

$$a_{\max} \approx 0.084482969 \dots$$

$$a_{\max} \approx 8.4483\%$$

---

## 4. Conclusion

To achieve a speedup of at least 7,500x on an 8,192-core cluster, non-parallelizable overhead (serial initialization, communication, barrier synchronization) cannot exceed **8.4483%** of total parallel execution time.
