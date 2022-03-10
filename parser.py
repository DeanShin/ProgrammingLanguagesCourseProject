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

    def parseExpr(self) -> AbstractSyntaxTree:
        tree = self.parseTerm()
        while self.nextToken and self.nextToken[1] == "+":
            token = self.nextToken
            self.consumeToken()
            tree = AbstractSyntaxTree(token, tree, self.parseTerm())
        return tree

    def parseTerm(self) -> AbstractSyntaxTree:
        tree = self.parseFactor()
        while self.nextToken and self.nextToken[1] == "-":
            token = self.nextToken
            self.consumeToken()
            tree = AbstractSyntaxTree(token, tree, self.parseFactor())
        return tree

    def parseFactor(self) -> AbstractSyntaxTree:
        tree = self.parsePiece()
        while self.nextToken and self.nextToken[1] == "/":
            token = self.nextToken
            self.consumeToken()
            tree = AbstractSyntaxTree(token, tree, self.parsePiece())
        return tree

    def parsePiece(self) -> AbstractSyntaxTree:
        tree = self.parseElement()
        while self.nextToken and self.nextToken[1] == "*":
            token = self.nextToken
            self.consumeToken()
            tree = AbstractSyntaxTree(token, tree, self.parseElement())
        return tree

    def parseElement(self) -> AbstractSyntaxTree:
        if self.nextToken and self.nextToken[1] == "(":
            self.consumeToken()
            tree = self.parseExpr()
            if self.nextToken[1] != ")":
                raise Exception("Expected ')', but got " + self.nextToken, self.nextToken)
            self.consumeToken()
            return tree
        elif self.nextToken and self.nextToken[0] == Token.NUMBER:
            tree = AbstractSyntaxTree(self.nextToken)
            self.consumeToken()
            return tree
        elif self.nextToken and self.nextToken[0] == Token.IDENTIFIER:
            tree = AbstractSyntaxTree(self.nextToken)
            self.consumeToken()
            return tree
        else:
            raise Exception("Expected '(', NUMBER, or IDENTIFIER, but got " + self.nextToken, self.nextToken)

    def consumeToken(self) -> None:
        self.tokenIdx += 1
        if self.tokenIdx >= len(self.tokens):
            self.nextToken = None
            return
        self.nextToken = self.tokens[self.tokenIdx]
        return