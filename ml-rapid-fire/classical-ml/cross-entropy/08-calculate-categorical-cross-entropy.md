# Calculate Categorical Cross-Entropy

**Q:** Calculate categorical cross-entropy loss for one sample: True label is "dog" for classes [cat, dog, bird], model predicts p = [0.1, 0.7, 0.2]

**A:**
Formula: -Σ y_i·log(p_i)

One-hot encode true label: y = [0, 1, 0]

Calculation:
= -[y_cat·log(p_cat) + y_dog·log(p_dog) + y_bird·log(p_bird)]
= -[0·log(0.1) + 1·log(0.7) + 0·log(0.2)]
= -[0 + log(0.7) + 0]
= -log(0.7)
≈ 0.36

---
