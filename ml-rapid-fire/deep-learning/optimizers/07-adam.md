# Adam Optimizer

**Q:** How does Adam work?

**A:**

- Combines **momentum** + **RMSprop**
- Maintains moving averages of gradient (m) and squared gradient (v)
- Includes **bias correction** for early steps
- Default: B1=0.9, B2=0.999, epsilon=1e-8
- Most popular optimizer — good default choice

---
