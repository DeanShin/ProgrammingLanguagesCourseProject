# Dean Shin and Kunal Babbar -- Phase 2.1
from enum import Enum, auto


class Token(Enum):
    IDENTIFIER = auto()
    NUMBER = auto()
    SYMBOL = auto()
    KEYWORD = auto()
    ERROR = auto()


