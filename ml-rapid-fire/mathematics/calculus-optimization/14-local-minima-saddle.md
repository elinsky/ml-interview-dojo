# Local Minima and Saddle Points

**Q:** What are the challenges of non-convex optimization in deep learning?
- Local minima
- Saddle points
- Why deep learning still works

**A:**

- **Local minima**: ∇f = 0 and Hessian positive definite; gradient descent can get stuck
- **Saddle points**: ∇f = 0 but Hessian indefinite (some directions up, some down); more common than local minima in high dimensions
- **Why saddle points dominate**: in d dimensions, need ALL eigenvalues positive for local min — unlikely by chance
- **Why deep learning works**:
  - Most local minima are nearly as good as global (empirical observation)
  - SGD noise helps escape saddle points
  - Overparameterization creates many good solutions
  - Loss landscape is "well-behaved" for wide networks

---
