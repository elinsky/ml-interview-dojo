# Grid Search

**Q:** How does grid search work for hyperparameter tuning?
- How the grid is formed
- Search process
- Key characteristic
- Tradeoff

**A:**

- **Grid**: define discrete values for each hyperparameter; grid = all combinations
- **Process**: train and evaluate on validation set for *every* combination; select best
- **Exhaustive**: guaranteed to find best in grid (no sampling/randomness)
- **Tradeoff**: computationally expensive O(n₁ × n₂ × ... × nₖ); curse of dimensionality with many hyperparameters

**See also:** [[202101241752 Chollet's Machine Learning Workflow]]

---
