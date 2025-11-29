# Feature Scaling for KNN

**Q:** Why is feature scaling important for KNN?

**A:**

- KNN uses **distance** — features on larger scales dominate
- Example: age (0-100) vs salary (0-1,000,000) → salary dominates distance
- **Must normalize** features to equal scales
- Common methods:
  - **Min-max**: scale to [0, 1] — good general choice
  - **Standardization**: mean=0, std=1 — good if Gaussian distribution
- Fit scaler on training data only; transform both train and test
- Also: handle **missing data** (impute or exclude) — can't compute distance otherwise

---
