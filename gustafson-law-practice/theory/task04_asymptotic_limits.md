# Task 04: Asymptotic Analysis of Parallel Efficiency

## 1. Formulation

Parallel Efficiency $E(P)$ is defined as ratio of achieved speedup $S(P)$ to total core count $P$:

$$E(P) = \frac{S(P)}{P}$$

---

## 2. Derivation of Limits as $P \to \infty$

### Gustafson's Model Efficiency
Substitute Gustafson's speedup $S(P) = P - a(P - 1)$:

$$E_G(P) = \frac{P - a(P - 1)}{P} = 1 - a \left( \frac{P - 1}{P} \right) = 1 - a \left( 1 - \frac{1}{P} \right)$$

Taking the asymptotic limit as $P \to \infty$:

$$\lim_{P \to \infty} E_G(P) = \lim_{P \to \infty} \left[ 1 - a \left( 1 - \frac{1}{P} \right) \right] = 1 - a$$

### Amdahl's Model Efficiency
Substitute Amdahl's speedup $S_A(P) = \frac{1}{s + \frac{1 - s}{P}}$:

$$E_A(P) = \frac{1}{P \cdot s + (1 - s)}$$

Taking the asymptotic limit as $P \to \infty$ (assuming $s > 0$):

$$\lim_{P \to \infty} E_A(P) = \lim_{P \to \infty} \frac{1}{P \cdot s + 1 - s} = 0$$

---

## 3. Comparative Summary

$$\begin{cases} \lim_{P \to \infty} E_{\text{Gustafson}}(P) = 1 - a & \text{(Non-zero lower bound under weak scaling)} \\ \lim_{P \to \infty} E_{\text{Amdahl}}(P) = 0 & \text{(Decays to zero under strong scaling)} \end{cases}$$

Under weak scaling, parallel efficiency converges to $1 - a$. For a serial fraction $a = 0.04$, hardware utilization remains at 96% even as $P \to \infty$.
