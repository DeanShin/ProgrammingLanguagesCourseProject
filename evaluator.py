# Dean Shin and Kunal Babbar -- Phase 3.2
from ast import AbstractSyntaxTree
from token import TokenType


class Evaluator:
    def __init__(self, ast: AbstractSyntaxTree) -> None:
        self.ast = ast
        self.memory = {}

    def evaluate(self):
        self.evaluateStatement(self.ast)
        return self.memory

    def evaluateStatement(self, ast: AbstractSyntaxTree):
        if ast.token.value == ';':
            self.evaluateStatement(ast.children[0])
            self.evaluateStatement(ast.children[1])
        elif ast.token.value == ':=':
            self.evaluateAssignment(ast)
        elif ast.token.value == 'skip':
            return
        elif ast.token.tokenType == TokenType.INTERNAL:
            if ast.token.value == 'IF-STATEMENT':
                self.evaluateIfStatement(ast)
            elif ast.token.value == 'WHILE-LOOP':
                self.evaluateWhileStatement(ast)
        else:
            raise Exception(f"Unexpected token: {ast.token}")

    def evaluateAssignment(self, ast: AbstractSyntaxTree):
        self.memory[ast.children[0].token.value] = self.evaluateExpression(ast.children[1])

    def evaluateIfStatement(self, ast: AbstractSyntaxTree):
        expression = self.evaluateExpression(ast.children[0])
        if expression != 0:
            self.evaluateStatement(ast.children[1])
        else:
            self.evaluateStatement(ast.children[2])

    def evaluateWhileStatement(self, ast: AbstractSyntaxTree):
        while self.evaluateExpression(ast.children[0]) != 0:
            self.evaluateStatement(ast.children[1])

    def evaluateExpression(self, ast: AbstractSyntaxTree):
        if ast.token.tokenType == TokenType.NUMBER:
            return int(ast.token.value)
        elif ast.token.tokenType == TokenType.IDENTIFIER:
            if ast.token.value not in self.memory:
                raise Exception(f"Evaluator error: identifier {ast.token.value} has not been initialized.")
            return self.memory[ast.token.value]
        elif ast.token.tokenType == TokenType.SYMBOL:
            left = self.evaluateExpression(ast.children[0])
            right = self.evaluateExpression(ast.children[1])
            if ast.token.value == '+':
                return left + right
            if ast.token.value == '-':
                return max(left - right, 0)
            if ast.token.value == '*':
                return left * right
            if ast.token.value == '/':
                if right == 0:
                    raise Exception(f"Evaluator error: cannot divide by 0")
                return left // right
            else:
                raise Exception(f"Evaluator error: unsupported symbol encountered: {ast.token}")
        else:
            raise Exception(f"Evaluator error: unsupported token type encountered: {ast.token}")