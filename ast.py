# Dean Shin and Kunal Babbar -- Phase 2.1

class AbstractSyntaxTree:
    def __init__(self, token, *children):
        self.token = token
        self.children = children
