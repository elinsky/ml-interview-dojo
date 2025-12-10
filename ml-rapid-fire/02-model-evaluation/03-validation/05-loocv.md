# Leave-One-Out Cross-Validation (LOOCV)

**Q:** What is LOOCV and what are its tradeoffs?
- How it works (relation to k-fold)
- Pro (benefit)
- Con (drawback)
- When to use

**A:**

- **How it works**: k-fold where k = n (each sample is its own fold)
- **Pro**: maximum training data used; deterministic (no random sampling)
- **Con**: computationally expensive (n model fits); high variance in estimate
- **When to use**: very small datasets where accurate estimate matters more than compute cost

**See also:** [[202107270653 Model Selection for Linear Regression]], [[202101080742 Cross Validation (K-Fold)]]

---
