# Dean Shin and Kunal Babbar -- Phase 2.1

class AbstractSyntaxTree():
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right