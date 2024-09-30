from block import Block
from constants import Constants
import random

class Node:
    def __init__(self,
                id,
                hashPower):
        
        self.id = id
        self.blockchain = []
        self.balance = 0
        self.hashPower = hashPower
        self.blocksMined = 0
        self.fnGenerateGenesisBlock()
        
    def fnGenerateGenesisBlock(self):
        self.blockchain.append(Block())
        
    def fnGetLastBlock(self):
        return self.blockchain[-1]
    
    def fnBlockchainLength(self):
        return len(self.blockchain)
    
    def fnResetState(self):
        self.balance = 0
        self.blockchain = []
        self.blocksMined = 0
        
    def fnTimeTakenToMine(self):
        TOTAL_HASHPOWER = sum([miner.hashPower for miner in Constants.NODES])
        hashPower = self.hashPower/TOTAL_HASHPOWER
        return random.expovariate(hashPower * 1/Constants.blockInterval)