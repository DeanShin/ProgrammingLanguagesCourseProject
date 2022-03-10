# Dean Shin and Kunal Babbar -- Phase 2.1
from enum import Enum


class Token(Enum):
    IDENTIFIER = "IDENTIFIER"
    NUMBER = "NUMBER"
    SYMBOL = "SYMBOL"
    KEYWORD = "KEYWORD"
    ERROR = "ERROR"

    def __str__(self):
        return str(self.value)