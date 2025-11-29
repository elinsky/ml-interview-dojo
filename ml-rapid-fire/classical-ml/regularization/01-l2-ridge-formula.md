# L2 (Ridge) Penalty Formula

**Q:** What is the L2 (Ridge) regularization penalty formula?

**A:**

- **Formula**: Loss = Original Loss + λ × Σ(wᵢ²)
- Adds **sum of squared weights** to loss
- Also called **weight decay**, Ridge Regression, Tikhonov regularization
- Penalizes **larger weights more severely**
- Bias term typically **not included** in penalty

[[202101171731]] [@nielsen2015neural, p. 87] [@james2013introduction, p. 215]

---
