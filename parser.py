# Dean Shin and Kunal Babbar -- Phase 2.1

from token import Token
from ast import AbstractSyntaxTree

class Parser():
    def __init__(self, tokens) -> None:
        self.tokenIdx = 0
        self.tokens = tokens
        self.nextToken = tokens[0]
    
    def parseTokens(self) -> AbstractSyntaxTree:
        return self.parseExpr()

    def parseExpr(self):
        tree = self.parseTerm()
        while self.nextToken[1] == "+":
            self.consumeToken()
            tree = AbstractSyntaxTree(self.nextToken, tree, self.parseTerm())
        return tree

    def parseTerm(self):
        tree = self.parseFactor()
        while self.nextToken[1] == "-":
            self.consumeToken()
            tree = AbstractSyntaxTree(self.nextToken, tree, self.parseFactor())
        return tree

    def parseFactor(self):
        tree = self.parsePiece()
        while self.nextToken[1] == "/":
            self.consumeToken()
            tree = AbstractSyntaxTree(self.nextToken, tree, self.parsePiece())
        return tree

    def parsePiece(self):
        tree = self.parseElement()
        while self.nextToken[1] == "*":
            self.consumeToken()
            tree = AbstractSyntaxTree(self.nextToken, tree, self.parseElement())
        return tree

    def parseElement(self):
        if self.nextToken[1] == "(":
            self.consumeToken()
            tree = self.parseExpr()
            if self.nextToken[1] != ")":
                raise Exception("Expected ')', but got " + self.nextToken, self.nextToken)
            self.consumeToken()
            return tree
        elif self.nextToken[0] == Token.NUMBER:
            tree = AbstractSyntaxTree(self.nextToken)
            self.consumeToken()
            return tree
        elif self.nextToken[0] == Token.IDENTIFIER:
            tree = AbstractSyntaxTree(self.nextToken)
            self.consumeToken()
            return tree
        else:
            raise Exception("Expected '(', NUMBER, or IDENTIFIER, but got " + self.nextToken, self.nextToken)

    def consumeToken(self):
        self.tokenIdx += 1
        self.nextToken = self.tokens[self.tokenIdx]
        return