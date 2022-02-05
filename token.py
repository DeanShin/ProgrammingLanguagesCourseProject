from enum import Enum, auto

class Token(Enum):
    IDENTIFIER = auto()
    NUMBER = auto()
    SYMBOL = auto()
    ERROR = auto()
