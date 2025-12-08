# Calculate Categorical Cross-Entropy

**Q:** Calculate categorical cross-entropy loss for one sample: True label is "dog" for classes [cat, dog, bird], model predicts p = [0.1, 0.7, 0.2]

**A:**
Formula: -Σ y_i·ln(p_i)

One-hot encode true label: y = [0, 1, 0]

Calculation:
= -[y_cat·ln(p_cat) + y_dog·ln(p_dog) + y_bird·ln(p_bird)]
= -[0·ln(0.1) + 1·ln(0.7) + 0·ln(0.2)]
= -[0 + ln(0.7) + 0]
= -ln(0.7)
≈ 0.36

---
