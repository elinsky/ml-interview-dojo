# A/B Testing

**Q:** What is A/B testing and what are the key design considerations?
- What it is
- Key design decisions
- Common pitfalls

**A:**

- **What it is**: randomized controlled experiment comparing two variants (A=control, B=treatment)
- **Key design decisions**:
  - Sample size: power analysis to detect minimum effect of interest
  - Randomization: ensure groups are comparable
  - Metric: define primary success metric upfront
  - Duration: long enough to capture variation (day-of-week effects, etc.)
- **Common pitfalls**:
  - Peeking: checking results early inflates false positives
  - Multiple comparisons: testing many metrics without correction
  - Simpson's paradox: aggregate results hide subgroup differences

---
