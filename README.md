
---

# Fork After Withholding (FAW) Attacks on Blockchain

### Group 22
- **U21CS081** - S. Jaswanth Reddy  
- **U21CS096** - J. Prajwala Anand  
- **U21CS074** - P. Mokshajna  

---

### Introduction
Block withholding is an attack similar to selfish mining, where a pool member withholds a mined block to reduce the pool's revenue. Instead of submitting **Full Proof of Work (FPoW)**, they only submit **Partial Proof of Work (PPoW)**, creating the miner’s dilemma. In a **Fork After Withholding (FAW)** attack, an attacker joins a mining pool and submits an FPoW after a non-target miner finds a block, creating a fork. If the attacker’s block is selected, they share the rewards with the pool, potentially earning up to four times more than a **Block Withholding (BWH)** attacker in large pools.

### Problem Statement
The FAW attack targets blockchain mining pools by exploiting block withholding and manipulating block release timing. Attackers delay sharing their mined blocks and submit them to create forks, taking advantage of reward mechanisms that compensate for reported work rather than actual contributions. This weakens the fairness and security of the blockchain without requiring majority hash power.

### Countermeasures
1. **Early Submission Reward**: Ensures fair reward distribution based on actual contributions, encouraging miners to submit blocks promptly.
2. **Cross-Pool Cooperation**: Facilitates real-time detection of suspicious behaviour and fork events across multiple mining pools.
3. **Decentralized Cryptographic Incentives**: A reputation system that incentivizes honest mining behaviour and penalizes malicious actions to enhance pool security.

### Objectives
1. **Create a Blockchain Prototype**: Develop a system that guarantees fair reward distribution among miners, even in the presence of block withholding.
2. **Prevent Manipulation**: Implement mechanisms to detect and prevent block withholding and fork manipulation, ensuring that attackers cannot gain undue rewards.

---

### Mentor  
**Dr. Keyur Parmar**

---

### How to Run:
