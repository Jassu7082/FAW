import random
from typing import Dict, List

class Miner:
    def __init__(self, address: str, hashrate: float):
        self.address = address
        self.hashrate = hashrate
        self.shares = 0
        self.rewards = 0.0

class PoolManager:
    def __init__(self, block_manager):
        self.block_manager = block_manager
        self.miners: Dict[str, Miner] = {}
        self.pool_hashrate = 0.0
        
        self.current_block = None
        self.reward_system = RewardDistributionSystem(self)

    def add_miner(self, address: str, hashrate: float):
        self.miners[address] = Miner(address, hashrate)
        self.pool_hashrate += hashrate

    def remove_miner(self, address: str):
        if address in self.miners:
            self.pool_hashrate -= self.miners[address].hashrate
            del self.miners[address]

    def submit_share(self, miner_address: str):
        if miner_address in self.miners:
            self.miners[miner_address].shares += 1
            if self.current_block is None:
                self.current_block = self.block_manager.get_latest_block()

    def simulate_mining_round(self, duration: int):
        # Simulate miners submitting shares based on their hashrate
        for _ in range(duration):
            for miner in self.miners.values():
                if random.random() < miner.hashrate / self.pool_hashrate:
                    self.submit_share(miner.address)

        # Attempt to mine a block
        if random.random() < self.pool_hashrate / 1000:  # Simplified difficulty
            mined_block = self.block_manager.mine_pending_transactions("pool_address")
            if mined_block:
                self.distribute_rewards(mined_block)
                self.reset_shares()

    def distribute_rewards(self, block):
        block_reward = 6.25  # Example block reward
        self.reward_system.distribute(block_reward)

    def reset_shares(self):
        for miner in self.miners.values():
            miner.shares = 0
        self.current_block = None

class RewardDistributionSystem:
    def __init__(self, pool_manager: PoolManager):
        self.pool_manager = pool_manager

    def distribute(self, block_reward: float):
        total_shares = sum(miner.shares for miner in self.pool_manager.miners.values())
        if total_shares == 0:
            return

        for miner in self.pool_manager.miners.values():
            miner_reward = (miner.shares / total_shares) * block_reward
            miner.rewards += miner_reward
            print(f"Miner {miner.address} received {miner_reward:.8f} reward")

    def get_miner_balance(self, miner_address: str) -> float:
        if miner_address in self.pool_manager.miners:
            return self.pool_manager.miners[miner_address].rewards
        return 0.0

    def withdraw(self, miner_address: str, amount: float) -> bool:
        if miner_address in self.pool_manager.miners:
            miner = self.pool_manager.miners[miner_address]
            if miner.rewards >= amount:
                miner.rewards -= amount
                print(f"Miner {miner_address} withdrew {amount:.8f}")
                return True
        return False

# Usage example
from block_manager_implementation import BlockManager

block_manager = BlockManager()
pool_manager = PoolManager(block_manager)

# Add miners to the pool
pool_manager.add_miner("miner1", 50)
pool_manager.add_miner("miner2", 30)
pool_manager.add_miner("miner3", 20)

# Simulate mining for 100 time units
pool_manager.simulate_mining_round(100)

# Check miner balances
for miner_address in pool_manager.miners:
    balance = pool_manager.reward_system.get_miner_balance(miner_address)
    print(f"Miner {miner_address} balance: {balance:.8f}")

# Simulate a withdrawal
pool_manager.reward_system.withdraw("miner1", 1.0)