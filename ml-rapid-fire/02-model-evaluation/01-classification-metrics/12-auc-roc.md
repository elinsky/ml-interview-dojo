# AUC-ROC

**Q:** What is AUC-ROC and how do you interpret it?
- What it stands for
- Value range and interpretation
- Probabilistic meaning
- Why it's useful

**A:**

- **What it stands for**: Area Under the ROC Curve
- **Value range**: 0.5 = random classifier, 1.0 = perfect
- **Probabilistic meaning**: Probability that a random positive ranks higher than a random negative
  - E.g., AUC = 0.8 on cancer detection: pick a random cancer patient and random healthy person, 80% of the time the model gives the cancer patient a higher risk score
- **Why useful**: Threshold-independent measure for comparing models without committing to a threshold

---
