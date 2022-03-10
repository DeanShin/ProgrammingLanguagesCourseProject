# Dean Shin and Kunal Babbar -- Phase 2.1
from enum import Enum, auto


class Token(Enum):
    IDENTIFIER = "Identifier"
    NUMBER = "Number"
    SYMBOL = "Symbol"
    KEYWORD = "Keyword"
    ERROR = "Error"

    def __str__(self):
        return str(self.value)


