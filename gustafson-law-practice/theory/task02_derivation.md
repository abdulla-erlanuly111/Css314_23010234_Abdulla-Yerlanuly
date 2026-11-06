# Task 02: Formal Derivation of Scaled Speedup

## 1. Theorem Statement

Let execution time on a parallel system of $P$ processing units be normalized to unity:

$$T(P) = s + p = 1$$

where $s$ is the time spent in serial execution and $p$ is the time spent in parallel execution. The equivalent serial runtime $T(1)$ to compute the expanded workload is given by:

$$T(1) = s + p \cdot P$$

Then Gustafson's scaled speedup $S(P)$ is expressed as:

$$S(P) = P - a(P - 1)$$

where $a = s$ represents the observed serial fraction on the parallel machine.

---

## 2. Step-by-Step Derivation

### Step 1: Normalization of Parallel Runtime
Define parallel execution time on $P$ cores as normalized wall-clock time:

$$T_P(P) = 1$$

Decompose this execution time into serial fraction $s$ and parallel fraction $p$:

$$s + p = 1 \implies p = 1 - s$$

### Step 2: Formulating Equivalent Workload on 1 Core
If the expanded problem computed on $P$ cores in time $T_P(P) = 1$ were executed sequentially on a single core:
- The serial part $s$ takes time $s \cdot 1 = s$.
- The parallel part $p$ took time $p$ using $P$ cores, so executing it sequentially requires $p \cdot P$ time units.

Therefore, the total single-core equivalent time $T(1)$ is:

$$T(1) = s + p \cdot P$$

### Step 3: Speedup Definition & Algebraic Substitution
Speedup is defined as ratio of single-core time to multi-core execution time:

$$S(P) = \frac{T(1)}{T(P)} = \frac{s + p \cdot P}{1} = s + p \cdot P$$

Substitute $p = 1 - s$:

$$S(P) = s + (1 - s) \cdot P$$

$$S(P) = s + P - s \cdot P$$

$$S(P) = P - s(P - 1)$$

Setting $a = s$ as the observed serial fraction yields the final Gustafson-Barsis formula:

$$S(P) = P - a(P - 1) \quad \blacksquare$$
