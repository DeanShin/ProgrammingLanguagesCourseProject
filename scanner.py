# Dean Shin and Kunal Babbar -- Phase 1.1
import re
from token import Token

identifier_regex = "([a-z]|[A-Z])([a-z]|[A-Z]|[0-9])*"
number_regex = "[0-9]+"
symbol_regex = "\\+|\\-|\\*|/|\\(|\\)"

def scan(line):
    tokens = []
    words = line.split()
    for word in words:
        i = 0
        while(i < len(word)):
            lastValidJ = None
            longestValidSubstring = None
            j = i + 1
            while(j <= len(word)):
                substr = word[i:j]
                if re.fullmatch(identifier_regex, substr) or \
                    re.fullmatch(number_regex, substr) or \
                    re.fullmatch(symbol_regex, substr):
                    lastValidJ = j
                    longestValidSubstring = substr
                j += 1
            if longestValidSubstring is None:
                tokens.append([Token.ERROR, word[i]])
                # Don't read the rest of the line.
                return tokens
            elif re.fullmatch(identifier_regex, longestValidSubstring):
                tokens.append([Token.IDENTIFIER, longestValidSubstring])
            elif re.fullmatch(number_regex, longestValidSubstring):
                tokens.append([Token.NUMBER, longestValidSubstring])
            elif re.fullmatch(symbol_regex, longestValidSubstring):
                tokens.append([Token.SYMBOL, longestValidSubstring])
            else:
                print("Unexpected longestValidSubstring")
                sys.exit()
            i = lastValidJ
    return tokens