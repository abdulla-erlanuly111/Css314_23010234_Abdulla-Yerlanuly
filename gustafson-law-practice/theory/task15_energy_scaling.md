# Task 15: Energy & Power Proportionality under Scaling

## 1. Power Profile Definition

Let each processing node consume:
- $P_{\text{idle}}$: Static idle power consumption (W)
- $P_{\text{active}}$: Dynamic active execution power consumption (W)

Total active power per node $P_{\text{node}} = P_{\text{idle}} + P_{\text{active}}$.

---

## 2. Energy Consumption Comparison

### Baseline Single-Core Execution ($P = 1$)
Executing scaled problem $W(P) = s + p \cdot P$ on a single core requires execution time $T_1 = s + p \cdot P$:

$$E_1 = P_{\text{node}} \cdot (s + p \cdot P)$$

### Multi-Core Weak Scaling Execution ($P$ cores)
Executing scaled problem on $P$ cores requires fixed time $T_P = 1$. All $P$ nodes operate concurrently for 1 time unit:

$$E_P = P \cdot P_{\text{node}} \cdot 1 = P \cdot (P_{\text{idle}} + P_{\text{active}})$$

---

## 3. Energy Ratio Analysis

$$\frac{E_P}{E_1} = \frac{P \cdot (P_{\text{idle}} + P_{\text{active}})}{(P_{\text{idle}} + P_{\text{active}})(s + p \cdot P)} = \frac{P}{s + p \cdot P} = \frac{P}{S_G(P)}$$

Since Gustafson speedup $S_G(P) \le P$, the energy ratio is always $\ge 1$. Weak scaling maintains execution speed at the cost of linear energy growth $O(P)$.
