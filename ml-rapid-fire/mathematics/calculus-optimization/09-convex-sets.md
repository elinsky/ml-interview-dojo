# Convex Sets and Optimization

**Q:** What is a convex set and what is convex optimization?
- Convex set definition
- Convex optimization problem
- Why constraints matter

**A:**

- **Convex set**: for any two points in set, line segment between them is also in set
- **Examples**: hyperplanes, halfspaces, balls, polyhedra
- **Convex optimization**: minimize convex f(x) over convex constraint set
  - Guaranteed global optimum
  - Efficient algorithms exist (polynomial time)
- **Non-convex constraints break convexity**: even with convex objective, non-convex constraints → hard problem
- **ML context**: SVM (convex), logistic regression (convex), neural networks (non-convex)

---
