# Task 03: The Serial Fraction Invariance Paradox

## 1. The Paradox Defined

A longstanding source of confusion between Amdahl's Law and Gustafson's Law stems from the frame of reference used to measure the serial fraction:
- **Amdahl's serial fraction ($s_A$):** Measured on a single processor system ($P=1$) for a fixed problem size.
- **Gustafson's serial fraction ($a_G$):** Measured on a parallel system ($P$ cores) for an expanded problem size.

---

## 2. Analytical Resolution

Suppose a workload consists of a fixed serial component $W_s$ and a parallel component $W_p(P)$ that scales linearly with processor count $P$:

$$W_p(P) = P \cdot W_{p,0}$$

### Single-Processor Perspective (Amdahl)
On a single processor, total work is $W_{total}(1) = W_s + W_{p,0}$. The serial fraction $s_A$ is:

$$s_A = \frac{W_s}{W_s + W_{p,0}}$$

### Multi-Processor Perspective (Gustafson)
On $P$ processors, the total serial workload remains $W_s$, but parallel work expands to $P \cdot W_{p,0}$. Total parallel execution time normalized to 1 unit gives parallel serial fraction $a_G$:

$$a_G = \frac{W_s}{W_s + P \cdot W_{p,0}} = \frac{\frac{W_s}{W_s + W_{p,0}}}{1 + (P - 1) \frac{W_{p,0}}{W_s + W_{p,0}}} = \frac{s_A}{s_A + P(1 - s_A)}$$

### Asymptotic Invariance Analysis
Taking the limit of observed serial fraction $a_G$ as $P \to \infty$:

$$\lim_{P \to \infty} a_G(P) = \lim_{P \to \infty} \frac{s_A}{s_A + P(1 - s_A)} = 0$$

Measuring serial overhead on parallel hardware demonstrates that as domain volume expands, the relative impact of fixed serial overhead $W_s$ diminishes asymptotically toward zero. This resolves the apparent paradox: massive scaling succeeds because the effective serial fraction $a_G$ shrinks as problem size expands.
