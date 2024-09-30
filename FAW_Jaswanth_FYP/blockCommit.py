import copy
import random
from block import Block
from event import Event,Queue
from constants import Constants
from distibuted import DistributedBlockChain
class BlockCommit:
    def fnHandleEvent(event : Event):
        if event.type =='create_block':
            BlockCommit.fnCreateBlock(event)
        elif event.type == 'recieve_block':
            BlockCommit.fnRecieveBlock(event)
            
    def fnCreateBlock(event: Event):
        transaction = event.transaction
        eventTime = event.time
        miner = event.node
        previousBlock = miner.fnLastBlock()
        minerWorkedTime = miner.fnTimeTakenToMine()
        createdBlock = Block(timestamp=eventTime+minerWorkedTime,
                             id = previousBlock.id+1,
                             previous=previousBlock,
                             height=previousBlock.height+1,
                             miner=miner,
                             transactions=transaction)
        if not BlockCommit.fnForkDetection(createdBlock):
            miner.blocksMined+=1
            BlockCommit.fnPropogateCreatedBlock(createdBlock)

    def fnForkDetection(createdBlock : Block):
        for block in DistributedBlockChain.globalBlockChain:
            if block.height == createdBlock.height:
                # case -1 : Largest Chain
                lengthOfChain = len(DistributedBlockChain.globalBlockChain)
                moreNumberOfBlocks = lengthOfChain-createdBlock.height
                if moreNumberOfBlocks>0:
                    miner = createdBlock.miner
                    miner.blockchain = DistributedBlockChain.globalBlockChain
                    return True
                
    def fnPropogateCreatedBlock(block):
        for node in Constants.NODES:
            if node.id != block.miner.id:
                blockCopy = copy.deepcopy(block)           
                Queue.fnAddEvent(Event('recieve_block',blockCopy,blockCopy.timestamp+random.expovariate(1/Constants.blockDelay),node))
    
    def fnRecieveBlock():
        pass