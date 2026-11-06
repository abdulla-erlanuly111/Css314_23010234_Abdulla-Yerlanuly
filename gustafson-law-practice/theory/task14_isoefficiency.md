# Task 14: Isoefficiency Relation with Gustafson Scaling

## 1. Isoefficiency Definition (Kumar & Grama)

The Isoefficiency Function $W = iso(P)$ measures the rate at which problem size $W$ must grow relative to processor count $P$ to maintain a constant parallel efficiency $E$.

Overhead function $T_{o}(P, W)$ is defined as:

$$T_o(P, W) = P \cdot T(P, W) - W$$

Isoefficiency equation:

$$W = K \cdot T_o(P, W) \quad \text{where } K = \frac{E}{1 - E}$$

---

## 2. Evaluation under Gustafson's Model

Under Gustafson's model, problem size grows linearly with processor count: $W(P) = P \cdot W_1$.

Total parallel overhead:

$$T_o(P) = P \cdot 1 - (a \cdot 1 + (1 - a)P) = P - a - P + aP = a(P - 1)$$

Substitute $T_o$ into the isoefficiency equation:

$$W = K \cdot a(P - 1) = O(P)$$

### Conclusion
A Gustafson-compliant application has an **isoefficiency of $O(P)$**, representing an optimal linear scaling workload requirement.
