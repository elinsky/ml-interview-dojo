# L1 (Lasso) Penalty Formula

**Q:** What is the L1 (Lasso) regularization penalty formula?

**A:**

- **Formula**: Loss = Original Loss + λ × Σ|wᵢ|
- Adds **sum of absolute values** of weights
- Lasso = **L**east **A**bsolute **S**hrinkage and **S**election **O**perator
- Result: **many weights → zero**, few weights large (do most work)

[[202101171802]] [@nielsen2015neural, p. 79] [@james2013introduction, p. 219]

---
