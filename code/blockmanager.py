import hashlib
import time
from typing import List, Dict

class Block: # validated
    def __init__(self, index, previous_hash, transactions, nonce=0):
        self.index = index
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.nonce = nonce
        self.hash = self.calculateHash()
        self.minerName = None
        self.minerAddress = None

    def calculateHash(self) -> str:
        block_string = f"{self.index}{self.timestamp}{self.previous_hash}{''.join(self.transactions)}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class BlockManager:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []
        self.fork_detector = ForkDetector(self)

    # def create_genesis_block(self):
    #     return Block(0, "0", ["Genesis Block"])

    def getLatestBlock(self): # validated
        return self.chain[-1]

    def addBlock(self, new_block): # validated
        if self.isValidNewBlock(new_block, self.getLatestBlock()):
            self.chain.append(new_block)
            self.fork_detector.check_for_fork(new_block)
            return True
        return False

    def isValidNewBlock(self, new_block, previous_block): # validated
        if (previous_block.index + 1 != new_block.index) or (previous_block.hash != new_block.previous_hash) or (new_block.calculateHash() != new_block.hash):
            return False
        return True

    def addTransactions(self, transaction): # validated
        self.pending_transactions.append(transaction)

    def minePendingTransactions(self, miner_address):
        new_block = Block(
            index=len(self.chain),
            previous_hash=self.get_latest_block().hash,
            transactions=self.pending_transactions + [f"Reward: {miner_address}"]
        )
        # Simple PoW: Find a hash starting with '00'
        while new_block.hash[:2] != "00":
            new_block.nonce += 1
            new_block.hash = new_block.calculateHash()
        
        if self.addBlock(new_block):
            self.pending_transactions = []
            return new_block
        return None

class ForkDetector:
    def __init__(self, block_manager: BlockManager):
        self.block_manager = block_manager
        self.forks: Dict[int, List[Block]] = {}

    def check_for_fork(self, new_block: Block):
        for block in self.block_manager.chain[:-1]:  # Exclude the latest block
            if block.index == new_block.index and block.hash != new_block.hash:
                if block.index not in self.forks:
                    self.forks[block.index] = []
                self.forks[block.index].append(new_block)
                print(f"Fork detected at block index {block.index}")
                self.resolve_fork(block.index)

    def resolve_fork(self, fork_index: int):
        # Simple resolution: Choose the longest chain
        main_chain = self.block_manager.chain[:fork_index+1]
        fork_chains = [main_chain + [fork] + self.block_manager.chain[fork_index+2:] for fork in self.forks[fork_index]]
        longest_chain = max(fork_chains, key=len)
        
        if len(longest_chain) > len(self.block_manager.chain):
            print(f"Resolving fork: Switching to a new chain of length {len(longest_chain)}")
            self.block_manager.chain = longest_chain

            # Clear the resolved fork
            del self.forks[fork_index]
        elif len(longest_chain) == len(self.block_manager.chain):
            # TODO : If there is anything todo
            pass