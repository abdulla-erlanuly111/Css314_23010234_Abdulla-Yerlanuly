# Task 09: Multi-Component Workload Partitioning

## 1. Application Profile Breakdown

A scientific simulation pipeline consists of three distinct computational phases measured during parallel execution:
- **Phase A (Initial disk I/O & parameter broadcast):** 2% of runtime ($a_A = 0.02$) — *Serial*
- **Phase B (Boundary message passing & synchronization):** 6% of runtime ($a_B = 0.06$) — *Serial Overhead*
- **Phase C (Core domain flux computation):** 92% of runtime ($p_C = 0.92$) — *Parallel*

---

## 2. Aggregate Serial Fraction Calculation

The total unparallelized fraction $a$ is the sum of non-scalable component overheads:

$$a = a_A + a_B = 0.02 + 0.06 = 0.08 \quad (8\%)$$

Corresponding parallel execution fraction:

$$p = 1 - a = 0.92 \quad (92\%)$$

---

## 3. Speedup & Efficiency Evaluations

### Scenario 1: $P = 512$ cores
$$S(512) = 512 - 0.08(512 - 1) = 512 - 0.08(511) = 512 - 40.88 = 471.12$$

$$E(512) = \frac{471.12}{512} \approx 0.920156 \quad (92.02\%)$$

### Scenario 2: $P = 2,048$ cores
$$S(2048) = 2048 - 0.08(2048 - 1) = 2048 - 0.08(2047) = 2048 - 163.76 = 1884.24$$

$$E(2048) = \frac{1884.24}{2048} \approx 0.920039 \quad (92.00\%)$$

---

## 4. Phase-Sensitive Bottleneck Analysis

Phase B (boundary synchronization) represents 75% of total serial overhead ($0.06 / 0.08$). Optimizing network non-blocking primitives in Phase B would yield significantly greater speedup gains than reducing Phase A disk I/O.
