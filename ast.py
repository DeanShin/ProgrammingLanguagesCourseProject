# Dean Shin and Kunal Babbar -- Phase 2.1

class AbstractSyntaxTree():
    def __init__(self, token, left = None, right = None):
        self.token = token
        self.left = left
        self.right = right