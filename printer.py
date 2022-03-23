# Dean Shin and Kunal Babbar -- Phase 2.2
from token import Token
from ast import AbstractSyntaxTree
from typing import Tuple, List, TextIO


def printTokens(tokens: List[Tuple[Token, str]], output_file: TextIO) -> None:
    for tokenType, tokenValue in tokens:
        if tokenType is Token.ERROR or tokenType is Token.INTERNAL:
            output_file.write("ERROR READING \"" + tokenValue + "\"\n")
        else:
            output_file.write(f'{tokenValue} : {tokenType}\n')


def printAST(root: AbstractSyntaxTree, output_file: TextIO) -> None:
    # Preorder traversal
    def printASTRec(ast: AbstractSyntaxTree, depth: int) -> None:
        if ast is None:
            return

        # Create the output string for the current node in the AST
        s = ""
        for _ in range(depth):
            s += "\t"
        (tokenType, tokenValue) = ast.token
        if tokenType is Token.INTERNAL:
            s += f'{tokenValue}\n'
        else:
            s += f'{tokenValue} : {tokenType}\n'
        output_file.write(s)

        for child in ast.children:
            printASTRec(child, depth + 1)

    printASTRec(root, 0)
