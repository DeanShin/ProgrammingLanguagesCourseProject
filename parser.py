# Dean Shin and Kunal Babbar -- Phase 2.1

class Parser():
    def __init__(self):
        self.tokenIdx = 0
        self.tokens = None
        self.nextToken = None
    
    def parseTokens(self):
        # Do something here
        # Return abstract syntax tree
        return

    def consumeToken(self):
        self.nextToken = self.tokens[self.tokenIdx]
        self.tokenIdx += 1
        return