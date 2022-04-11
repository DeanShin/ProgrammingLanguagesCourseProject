# Dean Shin and Kunal Babbar -- Phase 3.2
from enum import Enum


class TokenType(Enum):
    IDENTIFIER = "IDENTIFIER"
    NUMBER = "NUMBER"
    SYMBOL = "SYMBOL"
    KEYWORD = "KEYWORD"
    INTERNAL = "INTERNAL"
    ERROR = "ERROR"

    def __str__(self):
        return str(self.value)


class Token:
    def __init__(self, tokenType: TokenType, value: str):
        self.tokenType = tokenType
        self.value = value

    def __str__(self):
        return f'{self.tokenType} : {self.value}'
