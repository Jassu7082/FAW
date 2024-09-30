from event import Queue
from transaction import FullTransaction
from blockCommit import BlockCommit
from constants import Constants

def main():
    clock = 0
    FullTransaction.fnCreateTransactions()
    
    while not Queue.fnIsEmpty() and clock<=Constants.simulationTime:
        nextEvent = Queue.fnGetNextEvent()
        clock = nextEvent.time
        BlockCommit.fnHandleEvent(nextEvent)
        Queue.fnRemoveEvent(nextEvent)