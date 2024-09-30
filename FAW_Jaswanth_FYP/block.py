class Block:
    def __init__(self,
                depth=0,
                id=0,
                previous=None,
                timestamp=0,
                miner=None,
                size=1.0,
                height=1.0,
                transactions = []):
        
        self.depth = depth
        self.id = id
        self.previous = previous
        self.timestamp = timestamp
        self.miner = miner
        self.size = size
        self.height = height
        self.transactions = transactions