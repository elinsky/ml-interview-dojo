# Why Cross-Entropy Instead of MSE

**Q:** Why use cross-entropy instead of MSE for classification?

**A:**
- MSE with sigmoid creates **flat gradients** (slow learning when saturated)
- Cross-entropy produces **gradients proportional to the error**

"The primary benefit of cross-entropy cost over quadratic cost is that cross-entropy cost does not suffer from a learning slowdown when the sigmoid neuron is saturated" [@nielsen2015neural, p. 63]. — 202101120828 Cross-Entropy Cost

"The rate at which the weight learns is controlled by σ(z) - y, i.e., by the error in the output. The larger the error, the faster the neuron will learn." [@nielsen2015neural, p. 63]. — 202101120828 Cross-Entropy Cost

---
