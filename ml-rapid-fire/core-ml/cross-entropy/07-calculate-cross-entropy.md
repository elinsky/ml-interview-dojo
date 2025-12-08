# Calculate Cross-Entropy

**Q:** Calculate cross-entropy loss for one sample: True label y=1 (spam), model predicts p=0.7

**A:**
Formula: -[y·ln(p) + (1-y)·ln(1-p)]

Where y is the true label and p is the predicted probability for class 1.

Calculation:
= -[1·ln(0.7) + (1-1)·ln(1-0.7)]
= -[1·ln(0.7) + 0·ln(0.3)]
= -[ln(0.7) + 0]
= -ln(0.7)
≈ 0.36

---
