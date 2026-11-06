# Task 19: Monte Carlo Reduction & PRNG Overhead

## 1. Sources of Serial Fraction in Embarrassingly Parallel Engines

Monte Carlo integration is often cited as an embarrassingly parallel workload. However, at extreme processor scale ($P \ge 1,024$), three physical sources introduce a non-zero serial fraction $a$:

1. **Pseudo-Random Number Generator (PRNG) Seed Management:** Sequential initialization of independent PRNG streams (e.g., Mersenne Twister initialization or counter-based seed hashing) to prevent inter-process sequence correlation.
2. **Global Parallel Reduction:** Summing local sample counts and function values across processes via a tree reduction ($\log_2 P$ latency).
3. **Output Serialization:** Disk I/O serialization for summary statistics and convergence logs.

---

## 2. Mathematical Impact of Tree Reduction

Let sample count per worker process be $k = 10^7$. On $P$ processes, compute time per worker is $t_{\text{comp}} = \gamma \cdot k$.
Global reduction via MPI tree reduction requires $\lceil \log_2 P \rceil$ communication steps:

$$t_{\text{comm}}(P) = \beta \cdot \log_2 P$$

Total parallel execution time:

$$T(P) = t_{\text{comp}} + t_{\text{comm}}(P) = \gamma \cdot k + \beta \log_2 P$$

Effective parallel fraction $p(P)$:

$$p(P) = \frac{\gamma \cdot k}{\gamma \cdot k + \beta \log_2 P}$$

Effective serial fraction $a(P)$:

$$a(P) = 1 - p(P) = \frac{\beta \log_2 P}{\gamma \cdot k + \beta \log_2 P}$$

---

## 3. Scaled Speedup Under Tree Reductions

Substituting $a(P)$ into Gustafson's formula:

$$S(P) = P - \left(\frac{\beta \log_2 P}{\gamma \cdot k + \beta \log_2 P}\right)(P - 1)$$

As $P \to \infty$, the $\log_2 P$ term causes $a(P)$ to increase, creating a soft sublinear ceiling on achieved speedup unless sample size per process $k$ is expanded faster than $\log_2 P$.
