# Class Weights

**Q:** How do class weights address imbalance and when should you use them?
- How it works
- Setting weights
- Advantages

**A:**

- **How it works**: penalize misclassification of minority class more heavily in loss function
  - Weighted loss: L_weighted = Σ w_i × L(y_i, ŷ_i)
  - Higher weight on minority class → model pays more attention
- **Setting weights**:
  - Inverse frequency: w_i = n_total / (n_classes × n_i)
  - Custom based on business cost
  - Sklearn: `class_weight='balanced'` or pass dictionary
- **Advantages**:
  - No data modification (no synthetic samples, no discarding)
  - Works with any differentiable loss
  - Directly optimizes for desired tradeoff
- **When to use**: first thing to try — simple, effective, no added complexity
- **Sklearn**: most classifiers support `class_weight` parameter

---
