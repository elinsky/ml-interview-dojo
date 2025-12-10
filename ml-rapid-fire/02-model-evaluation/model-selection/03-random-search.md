# Random Search

**Q:** What is random search and when is it better than grid search?
- How it differs from grid search
- Key insight (why it often works better)
- When to prefer it

**A:**

- **How it works**: randomly sample n combinations from parameter space (not exhaustive)
- **Key insight** (Bergstra & Bengio 2012): when some hyperparameters matter more than others, random search explores more unique values of *important* dimensions; grid search wastes evaluations on unimportant ones
- **When to prefer**: many hyperparameters, large parameter spaces, limited compute budget

---
