# Multiple Testing Problem

**Q:** What is the multiple testing problem and how do you address it?
- The problem
- Why it matters
- Correction methods

**A:**

- **Problem**: running many tests inflates overall false positive rate; with m tests at α=0.05, expected false positives = 0.05×m
- **Family-wise error rate (FWER)**: P(≥1 false positive); with m independent tests: FWER ≈ 1-(1-α)^m
- **Corrections**:
  - Bonferroni: use α/m for each test (controls FWER, but conservative)
  - Benjamini-Hochberg: controls False Discovery Rate (FDR) — less conservative
- **Finance example**: testing 100 trading strategies → expect ~5 false positives at α=0.05; need adjustment

---
