# On-Policy vs Off-Policy Learning

**Q:** What's the difference between on-policy and off-policy learning?
- Definitions
- Examples
- Trade-offs

**A:**

- **On-policy**: learn about policy currently being used
  - Evaluate and improve the same policy
  - Example: SARSA — Q(s,a) updated toward Q(s',a') where a' is what policy actually chose
- **Off-policy**: learn about different policy than one generating data
  - Behavior policy (generates data) ≠ target policy (being learned)
  - Example: Q-learning — Q(s,a) updated toward max_a' Q(s',a') regardless of actual action
- **Trade-offs**:
  - On-policy: more stable, directly evaluates what you're doing
  - Off-policy: can reuse old data (experience replay), learn from demonstrations
- **Sample efficiency**: off-policy generally more efficient (reuse data)
- **Key insight**: Q-learning can learn optimal policy while following exploratory policy

---
