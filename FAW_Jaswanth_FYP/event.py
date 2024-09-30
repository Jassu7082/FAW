import operator

class Event:
    def __init__(self,type, time, node,transaction=None,block=None):
        self.type = type
        self.node = node
        self.time = time
        self.transaction = transaction
        self.block = block
        
class Queue:
    eventList = []
    
    def fnAddEvent(event):
        Queue.eventList += [event]
        
    def fnRemoveEvent(event):
        del Queue.eventList[0]
    
    def fnGetNextEvent():
        Queue.eventList.sort(key=operator.attrgetter('time'), reverse=False)
        return Queue.eventList[0]
    
    def fnSize():
        return len(Queue.eventList)
    
    def fnIsEmpty():
        return len(Queue.eventList) == 0