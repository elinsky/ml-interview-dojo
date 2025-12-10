# Hierarchical RL

**Q:** What is hierarchical RL and why is it useful?
- Concept
- Options framework
- Benefits

**A:**

- **Concept**: decompose policy into hierarchy of sub-policies
  - High-level policy selects goals or sub-tasks
  - Low-level policy executes primitive actions
- **Options framework**:
  - Option = (initiation set, policy, termination condition)
  - "Temporally extended actions"
  - Example: "go to room A" option contains many primitive actions
- **Benefits**:
  - Temporal abstraction: plan at coarser time scale
  - State abstraction: high-level ignores irrelevant details
  - Transfer: reuse sub-policies across tasks
  - Handles sparse rewards: sub-goals provide denser signal
- **Challenges**: how to discover useful sub-tasks automatically
- **Example**: robot navigation — high-level: which room; low-level: how to walk

---
