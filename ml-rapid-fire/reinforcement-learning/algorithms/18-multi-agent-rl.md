# Multi-Agent RL

**Q:** What challenges arise in multi-agent RL?
- Types of settings
- Key challenges
- Approaches

**A:**

- **Types of settings**:
  - Cooperative: agents share reward (team tasks)
  - Competitive: zero-sum (games)
  - Mixed: some cooperation, some competition
- **Key challenges**:
  - **Non-stationarity**: other agents' policies change (breaks Markov property from one agent's view)
  - **Credit assignment**: who contributed to team reward?
  - **Exploration**: exponentially larger joint action space
  - **Equilibrium concepts**: Nash equilibrium vs optimal play
- **Approaches**:
  - Independent learners: each agent treats others as environment
  - Centralized training, decentralized execution (CTDE)
  - Communication: agents share information
  - Self-play: train against yourself (AlphaGo)
- **Finance**: market making, auction bidding (multi-agent competition)

---
