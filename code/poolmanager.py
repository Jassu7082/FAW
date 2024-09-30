import random
import constants

class Miner: # validated
    def __init__(self, address, hashrate):
        self.address = address
        self.hashrate = hashrate
        self.shares = 0
        self.rewards = 0.0

    def getBalance(self):
        return self.rewards
    
    def withdraw(self,amount):#transfer to miner
        if amount <=self.rewards:
            self.rewards -= amount
            return True
        return False

class PoolManager:
    def __init__(self, block_manager): # validated
        self.block_manager = block_manager
        self.miners = {}
        self.pool_hashrate = 0.0
        self.reputation = {} # TODO: Implement reputation system
        self.current_block = None
        self.reward_system = RewardDistributionSystem(self)

    def addMiner(self, address, hashrate): # validated
        self.miners[address] = Miner(address, hashrate)
        self.pool_hashrate += hashrate

    def removeMiner(self, address): # validated
        if address in self.miners:
            self.pool_hashrate -= self.miners[address].hashrate
            del self.miners[address]

    def submitMinerShare(self, miner_address): # validated
        if miner_address in self.miners:
            self.miners[miner_address].shares += 1
            if self.current_block is None:
                self.current_block = self.block_manager.getLatestBlock()

    def simulateMiningRound(self, duration): # TODO: Implement simulation for 6 blocks
        for _ in range(duration):
            for miner in self.miners.values():
                if random.random() < miner.hashrate / self.pool_hashrate:
                    self.submitMinerShare(miner.address)

        if random.random() < self.pool_hashrate / 1000:
            mined_block = self.block_manager.minePendingTransactions("pool_address")
            if mined_block:
                self.distributeRewards(mined_block)
                self.resetShares()

    def distributeRewards(self, block): # TODO: Distribute for some time
        block_reward = constants.block_reward
        self.reward_system.distribute(block_reward)

    def resetShares(self): # correct
        for miner in self.miners.values():
            miner.shares = 0
        self.current_block = None

class RewardDistributionSystem: # validated
    def __init__(self, pool_manager):
        self.pool_manager = pool_manager

    def distribute(self, block_reward):
        total_shares = sum(miner.shares for miner in self.pool_manager.miners.values())
        if total_shares == 0:
            return

        for miner in self.pool_manager.miners.values():
            miner_reward = (miner.shares / total_shares) * block_reward
            miner.rewards += miner_reward

# from block_manager_implementation import BlockManager

# block_manager = BlockManager()
# pool_manager = PoolManager(block_manager)

# # Add miners to the pool
# pool_manager.add_miner("miner1", 50)
# pool_manager.add_miner("miner2", 30)
# pool_manager.add_miner("miner3", 20)

# # Simulate mining for 100 time units
# pool_manager.simulate_mining_round(100)

# # Check miner balances
# for miner_address in pool_manager.miners:
#     balance = pool_manager.reward_system.get_miner_balance(miner_address)
#     print(f"Miner {miner_address} balance: {balance:.8f}")

# # Simulate a withdrawal
# pool_manager.reward_system.withdraw("miner1", 1.0)