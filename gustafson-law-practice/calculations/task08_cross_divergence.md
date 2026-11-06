# Task 08: Cross-Over Point & Variance Analysis (Amdahl vs. Gustafson)

## 1. Problem Setup

Evaluate a workload with a static serial fraction of $s = a = 0.08$ (8%) executed across $P = 128$ cores. Compute predictions for both scaling laws and analyze their divergence.

---

## 2. Step-by-Step Arithmetic

### Amdahl's Fixed-Size Model Calculation
$$S_{\text{Amdahl}}(P) = \frac{1}{s + \frac{1 - s}{P}}$$

$$S_{\text{Amdahl}}(128) = \frac{1}{0.08 + \frac{0.92}{128}} = \frac{1}{0.08 + 0.0071875} = \frac{1}{0.0871875} \approx 11.46953$$

### Gustafson's Fixed-Time Model Calculation
$$S_{\text{Gustafson}}(P) = P - a(P - 1)$$

$$S_{\text{Gustafson}}(128) = 128 - 0.08(127) = 128 - 10.16 = 117.84000$$

---

## 3. Discrepancy & Variance Quantifications

- **Absolute Discrepancy:**
  $$\Delta S = S_{\text{Gustafson}} - S_{\text{Amdahl}} = 117.84000 - 11.46953 = 106.37047$$

- **Ratio of Speedups:**
  $$\text{Ratio} = \frac{S_{\text{Gustafson}}}{S_{\text{Amdahl}}} = \frac{117.84000}{11.46953} \approx 10.27418 \quad (10.27\text{x})$$

- **Percentage Discrepancy:**
  $$\text{Variance} = \frac{S_{\text{Gustafson}} - S_{\text{Amdahl}}}{S_{\text{Amdahl}}} \times 100\% = \frac{106.37047}{11.46953} \times 100\% \approx 927.42\%$$

---

## 4. Architectural Reflection

Gustafson's model predicts a speedup over **10.27 times higher** than Amdahl's model on 128 cores. 
- Amdahl assumes problem size is locked ($W = 1$), causing parallel work per core to vanish ($0.92 / 128 = 0.0072$), leaving serial overhead to dominate.
- Gustafson assumes problem size expands with hardware ($W(128) = 117.84$), keeping processing units fully saturated.
