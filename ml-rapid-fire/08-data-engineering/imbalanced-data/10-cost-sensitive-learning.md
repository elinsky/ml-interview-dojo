# Cost-Sensitive Learning

**Q:** What is cost-sensitive learning and how does it relate to class imbalance?
- Concept
- Relationship to class weights
- When to use

**A:**

- **Concept**: incorporate misclassification costs directly into training
  - Different types of errors have different costs
  - Cost matrix: C(i,j) = cost of predicting j when true class is i
- **Relationship to class weights**:
  - Class weights are a special case of cost-sensitive learning
  - More general: can have asymmetric costs (FN ≠ FP cost)
- **Example cost matrix** (fraud detection):
  - False negative (miss fraud): $1000 (loss from fraud)
  - False positive (flag legitimate): $10 (customer inconvenience)
- **When to use**: when you can quantify real-world costs of different errors
- **Implementation**: some algorithms support sample_weight, or modify loss function directly
- **Finance**: default prediction — cost of missed default >> cost of denying good customer

---
