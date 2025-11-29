# Preventing Overfitting in Decision Trees

**Q:** How do you prevent overfitting in decision trees?

**A:**

- **Pre-pruning (stopping criteria)**:
  - Max depth, min samples per leaf (typically 5-10), min samples to split, max leaf nodes
- **Post-pruning**:
  - Grow full tree, remove nodes that don't improve holdout performance
  - **Cost complexity pruning** — uses α to penalize tree size
- **Max features** — limit features considered per split
- Decision trees are **non-parametric** → prone to overfitting without constraints

[[202104151745]] [[202104170846]]

---
