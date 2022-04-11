# Dean Shin and Kunal Babbar -- Phase 3.2
from ast import AbstractSyntaxTree
from token import Token


class Evaluator:
    def __init__(self, ast: AbstractSyntaxTree) -> None:
        self.ast = ast

    def evaluate(self):
        return self.evaluateRec(self.ast)

    def evaluateRec(self, ast: AbstractSyntaxTree):
        if ast.token[0] == Token.NUMBER:
            return int(ast.token[1])
        elif ast.token[0] == Token.SYMBOL:
            left = self.evaluateRec(ast.children[0])
            right = self.evaluateRec(ast.children[1])
            if ast.token[1] == '+':
                return left + right
            if ast.token[1] == '-':
                return left - right
            if ast.token[1] == '*':
                return left * right
            if ast.token[1] == '/':
                if right == 0:
                    raise Exception(f"Evaluator error: cannot divide {left} by {right}")
                return left // right
            else:
                raise Exception(f"Evaluator error: unsupported symbol encountered: {ast.token}")
        else:
            raise Exception(f"Evaluator error: unsupported token type encountered: {ast.token}")