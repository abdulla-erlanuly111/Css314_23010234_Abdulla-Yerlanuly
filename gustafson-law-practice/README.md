# Gustafson's Law & Weak Scaling: Comprehensive Practice Suite

**Course:** Parallel & Distributed Computing Architecture  
**Instructor:** Sufyan bin Uzayr  
**Focus Area:** Scaled Speedup, Amdahl vs. Gustafson, Weak Scaling Analysis, Empirical Benchmarking  

---

## Executive Overview

This repository contains a complete suite of theoretical derivations, parametric numerical calculations, domain-specific scaling analyses, and empirical benchmarking scripts focused on **Gustafson's Law** and **weak scaling architecture**.

While Amdahl's Law models system behavior under **strong scaling** (fixed problem size distributed across an increasing core count $P$), Gustafson's Law models system behavior under **weak scaling** (problem size scales proportionally with $P$ to maintain a constant parallel execution time). This practice suite explores the mathematical foundations, asymptotic limits, real-world algorithmic workloads, and hardware constraints (such as NUMA boundaries and memory bandwidth limits) governing high-performance parallel systems.

---

## Key Mathematical Foundations

| Metric / Model | Mathematical Formulation | Operational Definition |
| :--- | :--- | :--- |
| **Gustafson Scaled Speedup** | $S(P) = P - a(P - 1) = s + p \cdot P$ | Speedup achieved when workload scales linearly with processing units $P$ under constant execution time. |
| **Parallel Efficiency (Weak)** | $E(P) = \frac{S(P)}{P} = 1 - a \left( \frac{P - 1}{P} \right)$ | Fraction of total compute capacity effectively utilized as $P$ scales toward infinity. |
| **Amdahl Speedup (Strong)** | $S_{\text{Amdahl}}(P) = \frac{1}{s + \frac{1 - s}{P}}$ | Speedup bound under fixed problem size, where speedup approaches $\frac{1}{s}$ as $P \to \infty$. |

*Where:*
* $P$ = Number of processing cores / threads.
* $a$ (or $s$) = Observed serial execution fraction ($a + p = 1$).
* $p$ = Observed parallel execution fraction.

---

## Repository Structure & Task Index

```text
gustafson-law-practice/
├── README.md                           # Master repository documentation (Task 25)
├── theory/                             # Analytical derivations, proofs, and comparative essays
│   ├── task01_scaling_models.md        # Strong vs. Weak Scaling Foundations (Task 01)
│   ├── task02_derivation.md            # Formal Derivation of Scaled Speedup (Task 02)
│   ├── task03_serial_invariance.md     # Serial Fraction Invariance Paradox (Task 03)
│   ├── task04_asymptotic_limits.md     # Asymptotic Analysis of Parallel Efficiency (Task 04)
│   ├── task05_historical_ncube.md      # Deconstructing the nCUBE 10 Experiment (Task 05)
│   ├── task11_sun_ni_comparison.md     # Sun-Ni Memory-Bounded Speedup Comparison (Task 11)
│   ├── task12_communication_penalty.md # Communication Overhead Penalty Integration (Task 12)
│   ├── task13_failure_cases.md         # Boundary Cases: When Weak Scaling Fails (Task 13)
│   ├── task14_isoefficiency.md         # Isoefficiency Relation with Gustafson Scaling (Task 14)
│   └── task15_energy_scaling.md        # Energy & Power Proportionality under Scaling (Task 15)
├── calculations/                       # Worked algebraic derivations and parametric tables
│   ├── task06_parametric_table.md      # Parametric Speedup Across Processor Densities (Task 06)
│   ├── task07_tolerable_serial.md      # Reverse Engineering Max Tolerable Overhead (Task 07)
│   ├── task08_cross_divergence.md      # Cross-Over Point: Amdahl vs. Gustafson (Task 08)
│   ├── task09_multicomponent.md        # Multi-Component Workload Partitioning (Task 09)
│   ├── task10_memory_growth.md         # Memory Footprint Limits & 3D Grid Growth (Task 10)
│   ├── task16_gemm_scaling.md          # Dense Matrix Multiplication (GEMM) Scaling (Task 16)
│   └── task17_stencil_scaling.md       # 3D Stencil Hydrodynamics Surface Scaling (Task 17)
├── analysis/                           # Domain-specific algorithmic workload evaluations
│   ├── task18_nbody_scaling.md         # N-Body Simulation: Direct vs. Barnes-Hut (Task 18)
│   ├── task19_monte_carlo.md           # Monte Carlo Reduction & PRNG Overhead (Task 19)
│   ├── task20_graph_processing.md      # Parallel Graph Traversal & Irregular Workloads (Task 20)
│   └── task24_hardware_audit.md        # Hardware Audit & Architectural Discrepancies (Task 24)
├── benchmarks/                         # Simulation tools and empirical benchmark suite
│   ├── simulator.py                    # Parametric Speedup Simulator (Task 21)
│   ├── fit_gustafson.py                # Least-Squares Linear Regression & Curve Fitting (Task 23)
│   ├── results.csv                     # Raw empirical execution benchmarks (Task 23)
│   └── weak_scale_bench/               # Multi-process synthetic workload harness (Task 22)
│       └── bench_harness.py
└── plots/                              # Visualization artifacts
    └── scaling_comparison.png          # Empirical vs. Theoretical Scaling Curves (Task 24)
```

---

## Setup & Quickstart Guide

### Prerequisites

* Python 3.9+
* Required packages: `numpy`, `matplotlib`, `pandas`, `scipy`

Install dependencies:

```bash
pip install numpy matplotlib pandas scipy
```

### Execution Workflow

1. **Run Parametric Speedup Simulator (Task 21):**
   ```bash
   python benchmarks/simulator.py --min-cores 1 --max-cores 65536 --serial-fraction 0.04 --output benchmarks/simulation_data.csv
   ```

2. **Run Empirical Weak-Scaling Benchmark (Task 22):**
   ```bash
   python benchmarks/weak_scale_bench/bench_harness.py --max-workers 8 --work-per-worker 10000000 --runs 5
   ```

3. **Perform Least-Squares Regression Fit (Task 23):**
   ```bash
   python benchmarks/fit_gustafson.py --input benchmarks/results.csv
   ```

4. **Generate High-Resolution Plots (Task 24):**
   ```bash
   python benchmarks/generate_plots.py --output plots/scaling_comparison.png
   ```

---

## Architectural Guidelines for Parallel Software Engineers

When designing HPC applications and parallel software architecture, consider these core rules:

1. **Design for Weak Scaling when Problem Size is Scalable:** If expanding problem resolution (e.g., higher grid density, more particles, larger dataset size) yields higher scientific fidelity, optimize for **Gustafson's Law**. Keep the execution time fixed while expanding processing units.
2. **Account for Memory & Boundary Limits:** Pure weak scaling assumes runtime remains strictly constant. However, for 3D stencil solvers and grid workloads, surface-to-volume ratio changes ($O(N^2)$ communication vs $O(N^3)$ computation), which can lead to communication bottlenecks at ultra-high core counts ($P > 10{,}000$).
3. **Beware of Irregular Workloads:** Algorithms with non-contiguous memory accesses or data-dependent branches (e.g., BFS graph traversals, sparse matrix operations) violate constant parallel fraction assumptions due to synchronization overhead and NUMA memory latency.
