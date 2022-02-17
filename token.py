# Dean Shin and Kunal Babbar -- Phase 1.2
from enum import Enum, auto


class Token(Enum):
    IDENTIFIER = auto()
    NUMBER = auto()
    SYMBOL = auto()
    KEYWORD = auto()
    ERROR = auto()


