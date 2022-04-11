# Dean Shin and Kunal Babbar -- Phase 3.2
from typing import List
from token import Token


class AbstractSyntaxTree:
    def __init__(self, token: Token, *children: 'AbstractSyntaxTree'):
        self.token = token
        self.children = children
