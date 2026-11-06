# Task 05: Deconstructing the nCUBE 10 Historical Experiment

## 1. Historical Background

In 1988, John Gustafson, Gary Montry, and Robert Benner published groundbreaking experimental results from an 1,024-processor nCUBE 10 hypercube supercomputer at Sandia National Laboratories.

Prior consensus held that parallel computing was severely limited by Amdahl's Law. With observed serial fractions around $s \approx 0.004$ (0.4%), traditional theoretical predictions capped maximum speedup at:

$$S_{\text{Amdahl}}^{\text{max}} = \frac{1}{0.004} = 250\text{x}$$

---

## 2. Experimental Breakthrough

Gustafson et al. demonstrated speedups exceeding **1,000x** on 1,024 cores across three distinct physics applications:
1. Wave Mechanics (Fluid dynamics grid solver)
2. Structural Analysis (Finite element solver)
3. Beam Stress Analysis (Matrix solver)

---

## 3. How Problem Expansion Dismantled Amdahl's Ceiling

The Sandia team scaled grid dimensions proportionally with processing node availability:
- Instead of solving a $64 \times 64$ grid on 1,024 nodes (where serial boundary management dominates), they expanded grid resolution to $2048 \times 2048$.
- Parallel compute workload grew with domain area/volume ($O(N^2)$ or $O(N^3)$), while serial setup and synchronization remained nearly fixed.
- Applying Gustafson's formula for $a = 0.004$ and $P = 1024$:

$$S(1024) = 1024 - 0.004(1023) = 1024 - 4.092 = 1019.9$$

This result proved that serial execution fractions do not inherently constrain parallel computing when problem size expands with hardware capacity.
