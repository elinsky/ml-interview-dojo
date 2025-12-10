# Bagging (Bootstrap Aggregating)

**Q:** What is bagging (bootstrap aggregating)?

**A:**

- **B**ootstrap **AGG**regat**ING** (Leo Breiman)
- **Bootstrap sample**: draw rows with replacement (row may appear 0, 1, or multiple times)
- Train model on each sample, **aggregate** via voting/averaging
- "Bagging **unstable** classifiers improves them. Bagging stable classifiers is not a good idea."
- Reduces **variance** — works best with high-variance models (deep trees)

[[202104161606]] [[202101080707]]

---
