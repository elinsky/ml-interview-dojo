# How Decision Trees Split

**Q:** How does a decision tree decide where to split?

**A:**

- **Recursive binary splitting** — greedy, locally optimal
- Evaluates all splits on all features, chooses **lowest cost**
- **Cost** = (m_left/m)×Cost_left + (m_right/m)×Cost_right
- **Classification**: Gini impurity or entropy
- **Regression**: MSE in each child node
- Finding optimal tree is **NP-Complete** — hence greedy approach

[[202104160853]]

---
