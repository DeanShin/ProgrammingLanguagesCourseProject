# Dean Shin and Kunal Babbar -- Phase 1.1
from enum import Enum, auto

class Token(Enum):
    IDENTIFIER = auto()
    NUMBER = auto()
    SYMBOL = auto()
    ERROR = auto()