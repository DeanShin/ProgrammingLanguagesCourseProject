# Dean Shin and Kunal Babbar -- Phase 2.1

class Parser():
    def __init__(self, tokens):
        self.tokenIdx = 0
        self.tokens = tokens
        self.nextToken = tokens[0]
    
    def parseTokens(self):
        # Do something here
        # Return abstract syntax tree
        return

    def consumeToken(self):
        self.tokenIdx += 1
        self.nextToken = self.tokens[self.tokenIdx]
        return