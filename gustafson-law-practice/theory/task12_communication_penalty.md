# Task 12: Communication Overhead Penalty Integration

## 1. Model Extension

Classic Gustafson's Law assumes communication overhead is constant or encapsulated within serial fraction $a$. In real distributed clusters, inter-node communication latency $C(P)$ scales as a function of node count $P$.

---

## 2. Mathematical Formulation

Let $C(P)$ denote communication overhead function per process. Modifying total parallel runtime equation:

$$T(P) = a + (1 - a) + C(P) = 1 + C(P)$$

The modified scaled speedup $S_{\text{comm}}(P)$ becomes:

$$S_{\text{comm}}(P) = \frac{T(1)}{T(P)} = \frac{a + (1 - a) \cdot P}{1 + C(P)} = \frac{P - a(P - 1)}{1 + C(P)}$$

---

## 3. Asymptotic Scaling Analysis

### Case A: Hypercube / Torus Topologies ($C(P) = \gamma \log_2 P$)

$$S_{\text{comm}}(P) = \frac{P - a(P - 1)}{1 + \gamma \log_2 P} \implies \lim_{P \to \infty} E(P) = \lim_{P \to \infty} \frac{1 - a}{1 + \gamma \log_2 P} = 0$$

### Case B: 2D Mesh Topologies ($C(P) = \gamma P^{1/2}$)

$$S_{\text{comm}}(P) = \frac{P - a(P - 1)}{1 + \gamma P^{1/2}}$$

Including non-zero network communication scaling causes efficiency to decay asymptotically, emphasizing the need for latency-hiding techniques in large systems.
