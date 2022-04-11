# Dean Shin and Kunal Babbar -- Phase 3.2
import re
import sys
from token import Token, TokenType
from typing import List, Tuple

identifier_regex = "([a-z]|[A-Z])([a-z]|[A-Z]|[0-9])*"
number_regex = "[0-9]+"
symbol_regex = "\\+|\\-|\\*|/|\\(|\\)|:=|;"
keyword_regex = "if|then|else|endif|while|do|endwhile|skip"


def scan(line: str) -> List[Token]:
    line = line.strip()
    tokens = []
    words = line.split()
    for word in words:
        i = 0
        while i < len(word):
            lastValidJ = None
            longestValidSubstring = None
            j = i + 1
            while j <= len(word):
                substring = word[i:j]
                if re.fullmatch(identifier_regex, substring) or \
                        re.fullmatch(number_regex, substring) or \
                        re.fullmatch(symbol_regex, substring) or \
                        re.fullmatch(keyword_regex, substring):
                    lastValidJ = j
                    longestValidSubstring = substring
                j += 1
            if longestValidSubstring is None:
                raise Exception(f'Scanner Error: Encountered invalid character "{word[i]}" in line "{line}"')
            elif re.fullmatch(keyword_regex, longestValidSubstring):
                tokens.append(Token(TokenType.KEYWORD, longestValidSubstring))
            elif re.fullmatch(identifier_regex, longestValidSubstring):
                tokens.append(Token(TokenType.IDENTIFIER, longestValidSubstring))
            elif re.fullmatch(number_regex, longestValidSubstring):
                tokens.append(Token(TokenType.NUMBER, longestValidSubstring))
            elif re.fullmatch(symbol_regex, longestValidSubstring):
                tokens.append(Token(TokenType.SYMBOL, longestValidSubstring))
            else:
                print("Unexpected longestValidSubstring")
                sys.exit()
            i = lastValidJ
    return tokens
