# How CV Works for Hyperparameter Tuning

**Q:** How does cross-validation work for hyperparameter tuning?

**A:**

- For each hyperparameter setting: train on k-1 folds, evaluate on held-out fold, repeat k times
- Average performance across all folds to get score for that setting
- Compare averaged scores across all hyperparameter settings; select best

---
