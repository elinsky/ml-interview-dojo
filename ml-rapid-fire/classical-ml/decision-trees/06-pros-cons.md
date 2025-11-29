# Decision Tree Pros and Cons

**Q:** What are the pros and cons of decision trees?

**A:**

- **Pros**:
  - Interpretable (can print rules), provides **feature importance**
  - No data prep needed, handles mixed types, missing values
  - Captures non-linear relationships (e.g., XOR)
- **Cons**:
  - **Unstable** — small data changes → completely different tree
  - Sensitive to **noisy features** and **training set rotation** (PCA can help)
  - **Axis-aligned splits** → boxy decision boundaries
- Single trees rarely used alone — **ensembles** fix instability

[[202104151745]]

---
