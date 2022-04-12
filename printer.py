# Dean Shin and Kunal Babbar -- Phase 3.2
from token import Token, TokenType
from ast import AbstractSyntaxTree
from typing import List, TextIO, Dict


def printTokens(tokens: List[Token], output_file: TextIO) -> None:
    for token in tokens:
        if token.tokenType is TokenType.ERROR or token.tokenType is TokenType.INTERNAL:
            output_file.write(f'ERROR READING \"{token}\"\n')
        else:
            output_file.write(f'{token}\n')


def printAST(root: AbstractSyntaxTree, output_file: TextIO) -> None:
    # Preorder traversal
    def printASTRec(ast: AbstractSyntaxTree, depth: int) -> None:
        if ast is None:
            return

        # Create the output string for the current node in the AST
        s = ""
        for _ in range(depth):
            s += "\t"
        if ast.token.tokenType is TokenType.INTERNAL:
            s += f'{ast.token.value}\n'
        else:
            s += f'{ast.token}\n'
        output_file.write(s)

        for child in ast.children:
            printASTRec(child, depth + 1)

    printASTRec(root, 0)


def printOutput(memory: Dict, output_file: TextIO) -> None:
    for key, value in memory.items():
        output_file.write(f'{key} = {value}\n')
