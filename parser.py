# Dean Shin and Kunal Babbar -- Phase 3.2

from token import Token, TokenType
from ast import AbstractSyntaxTree
from typing import List


class Parser:
    def __init__(self, tokens: List[Token]) -> None:
        self.tokenIdx = 0
        self.tokens = tokens
        self.nextToken = tokens[0] if len(tokens) > 0 else None

    def parseTokens(self) -> AbstractSyntaxTree:
        return self.parseExpr()
        # return self.parseStatement()

    def parseStatement(self) -> AbstractSyntaxTree:
        tree = self.parseBaseStatement()
        while self.nextToken and self.nextToken.value == ";":
            token = self.nextToken
            self.consumeToken()
            tree = AbstractSyntaxTree(token, tree, self.parseBaseStatement())
        return tree

    def parseBaseStatement(self) -> AbstractSyntaxTree:
        if self.nextToken and self.nextToken.value == "skip":
            token = self.nextToken
            self.consumeToken()
            tree = AbstractSyntaxTree(token)
            return tree
        elif self.nextToken and self.nextToken.value == "if":
            return self.parseIfStatement()
        elif self.nextToken and self.nextToken.value == "while":
            return self.parseWhileStatement()
        elif self.nextToken and self.nextToken.tokenType == TokenType.IDENTIFIER:
            return self.parseAssignment()
        else:
            raise Exception(
                f'Parser Error: Expected "skip", "if", "while" or IDENTIFIER but encountered token: {self.nextToken}')

    def parseAssignment(self) -> AbstractSyntaxTree:
        if not self.nextToken or self.nextToken.tokenType != TokenType.IDENTIFIER:
            raise Exception(
                f'Parser Error: Expected IDENTIFIER but encountered token: {self.nextToken}')
        identifier = self.nextToken
        self.consumeToken()
        if not self.nextToken or self.nextToken.value != ":=":
            raise Exception(
                f'Parser Error: Expected ":=" but encountered token: {self.nextToken}')
        symbol = self.nextToken
        self.consumeToken()
        tree = AbstractSyntaxTree(symbol, AbstractSyntaxTree(identifier), self.parseExpr())
        return tree

    def parseIfStatement(self) -> AbstractSyntaxTree:
        if not self.nextToken or self.nextToken.value != "if":
            raise Exception(f"Expected 'if', but encountered token: {self.nextToken}")
        self.consumeToken()
        expr = self.parseExpr()
        if not self.nextToken or self.nextToken.value != "then":
            raise Exception(f"Expected 'then', but encountered token: {self.nextToken}")
        self.consumeToken()
        ifStatement = self.parseStatement()
        if not self.nextToken or self.nextToken.value != "else":
            raise Exception(f"Expected 'else', but encountered token: {self.nextToken}")
        self.consumeToken()
        elseStatement = self.parseStatement()
        if not self.nextToken or self.nextToken.value != "endif":
            raise Exception(f"Expected 'endif', but encountered token: {self.nextToken}")
        self.consumeToken()
        return AbstractSyntaxTree(Token(TokenType.INTERNAL, "IF-STATEMENT"), expr, ifStatement, elseStatement)

    def parseWhileStatement(self) -> AbstractSyntaxTree:
        if not self.nextToken or self.nextToken.value != "while":
            raise Exception(f"Expected 'while', but encountered token: {self.nextToken}")
        self.consumeToken()
        expr = self.parseExpr()
        if not self.nextToken or self.nextToken.value != "do":
            raise Exception(f"Expected 'do', but encountered token: {self.nextToken}")
        self.consumeToken()
        statement = self.parseStatement()
        if not self.nextToken or self.nextToken.value != "endwhile":
            raise Exception(f"Expected 'endwhile', but encountered token: {self.nextToken}")
        self.consumeToken()
        return AbstractSyntaxTree(Token(TokenType.INTERNAL, "WHILE-LOOP"), expr, statement)

    def parseExpr(self) -> AbstractSyntaxTree:
        tree = self.parseTerm()
        while self.nextToken and self.nextToken.value == "+":
            token = self.nextToken
            self.consumeToken()
            tree = AbstractSyntaxTree(token, tree, self.parseTerm())
        return tree

    def parseTerm(self) -> AbstractSyntaxTree:
        tree = self.parseFactor()
        while self.nextToken and self.nextToken.value == "-":
            token = self.nextToken
            self.consumeToken()
            tree = AbstractSyntaxTree(token, tree, self.parseFactor())
        return tree

    def parseFactor(self) -> AbstractSyntaxTree:
        tree = self.parsePiece()
        while self.nextToken and self.nextToken.value == "/":
            token = self.nextToken
            self.consumeToken()
            tree = AbstractSyntaxTree(token, tree, self.parsePiece())
        return tree

    def parsePiece(self) -> AbstractSyntaxTree:
        tree = self.parseElement()
        while self.nextToken and self.nextToken.value == "*":
            token = self.nextToken
            self.consumeToken()
            tree = AbstractSyntaxTree(token, tree, self.parseElement())
        return tree

    def parseElement(self) -> AbstractSyntaxTree:
        if self.nextToken and self.nextToken.value == "(":
            self.consumeToken()
            tree = self.parseExpr()
            if not self.nextToken or self.nextToken.value != ")":
                raise Exception(f'Parser Error: Expected ")", but encountered token: {self.nextToken}')
            self.consumeToken()
            return tree
        elif self.nextToken and self.nextToken.tokenType == TokenType.NUMBER:
            tree = AbstractSyntaxTree(self.nextToken)
            self.consumeToken()
            return tree
        elif self.nextToken and self.nextToken.tokenType == TokenType.IDENTIFIER:
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
