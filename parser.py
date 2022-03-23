# Dean Shin and Kunal Babbar -- Phase 2.1

from token import Token
from ast import AbstractSyntaxTree


class Parser:
    def __init__(self, tokens) -> None:
        self.tokenIdx = 0
        self.tokens = tokens
        self.nextToken = tokens[0]

    def parseTokens(self) -> AbstractSyntaxTree:
        return self.parseStatement()

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

    def parseStatement(self) -> AbstractSyntaxTree:
        tree = self.parseBaseStatement()
        while self.nextToken and self.nextToken[1] == ";":
            token = self.nextToken
            self.consumeToken()
            tree = AbstractSyntaxTree(token, tree, self.parseBaseStatement())
        return tree

    def parseBaseStatement(self) -> AbstractSyntaxTree:
        if self.nextToken and self.nextToken[1] == "skip":
            token = self.nextToken
            self.consumeToken()
            tree = AbstractSyntaxTree(token)
            return tree
        elif self.nextToken and self.nextToken[1] == "if":
            return self.parseIfStatement()
        elif self.nextToken and self.nextToken[1] == "while":
            return self.parseWhileStatement()
        elif self.nextToken and self.nextToken[0] == Token.IDENTIFIER:
            return self.parseAssignment()
        else:
            raise Exception(
                f'Parser Error: Expected "skip", "if", "while" or IDENTIFIER but encountered token: {self.nextToken}')

    def parseAssignment(self) -> AbstractSyntaxTree:
        if not self.nextToken or self.nextToken[0] != Token.IDENTIFIER:
            raise Exception(
                f'Parser Error: Expected IDENTIFIER but encountered token: {self.nextToken}')
        identifier = self.nextToken
        self.consumeToken()
        if not self.nextToken or self.nextToken[1] != ":=":
            raise Exception(
                f'Parser Error: Expected ":=" but encountered token: {self.nextToken}')
        symbol = self.nextToken
        self.consumeToken()
        tree = AbstractSyntaxTree(symbol, AbstractSyntaxTree(identifier), self.parseExpr())
        return tree

    def parseIfStatement(self) -> AbstractSyntaxTree:
        tree = self.parseWhileStatement()
        while self.nextToken and self.nextToken[1] == "*":
            token = self.nextToken
            self.consumeToken()
            tree = AbstractSyntaxTree(token, tree, self.parseWhileStatement())
        return tree

    def parseWhileStatement(self) -> AbstractSyntaxTree:
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
                raise Exception(f'Parser Error: Expected ")", but encountered token: {self.nextToken}')
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
            raise Exception(
                f'Parser Error: Expected "(", NUMBER, or IDENTIFIER, but encountered token: {self.nextToken}')

    def consumeToken(self) -> None:
        self.tokenIdx += 1
        if self.tokenIdx >= len(self.tokens):
            self.nextToken = None
            return
        self.nextToken = self.tokens[self.tokenIdx]
        return
