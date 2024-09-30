import copy
import random
from constants import Constants
from event import Queue,Event

class Transaction:
    def __init__(self,
                id=0,
                timestamp=0 or [],
                sender=0,
                to=0,
                value=0,
                size=0.000546,
                fee=0):

        self.id = id
        self.timestamp = timestamp
        self.sender = sender
        self.to= to
        self.value=value
        self.size = size
        self.fee= fee
        
        
class FullTransaction:
    def fnCreateTransactions():
        count = int(Constants.transactionsPerSecond * Constants.simulationTime)
        
        for i in range(count):
            transaction = Transaction()
            transaction.id= random.randrange(100000000000)
            creation_time= random.randint(0,Constants.simulationTime-1)
            receive_time= creation_time
            transaction.timestamp= [creation_time,receive_time]
            sender= random.choice(Constants.NODES)
            transaction.sender = sender.id
            transaction.to= random.choice(Constants.NODES).id
            transaction.size= random.expovariate(1/Constants.transactionSize)
            transaction.fee= random.expovariate(1/Constants.transactionFee)
            
            FullTransaction.fnPropogateTransaction(transaction)
            
    def fnPropogateTransaction(transaction):
        for node in Constants.NODES:
            if node.id != transaction.sender:
                transactionCopy = copy.deepcopy(transaction)                
                Queue.fnAddEvent(Event('create_block',node,transactionCopy.timestamp[1]+random.expovariate(1/Constants.blockDelay),transactionCopy))