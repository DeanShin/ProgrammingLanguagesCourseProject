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
                if re.match(identifier_regex, substr) or \
                    re.match(number_regex, substr) or \
                    re.match(symbol_regex, substr):
                    lastValidJ = j
                    longestValidSubstring = substr
                j += 1
            if longestValidSubstring is None:
                tokens.append([Token.ERROR, word[i]])
                break
            elif re.match(identifier_regex, longestValidSubstring):
                tokens.append([Token.IDENTIFIER, longestValidSubstring])
            elif re.match(number_regex, longestValidSubstring):
                tokens.append([Token.NUMBER, longestValidSubstring])
            elif re.match(symbol_regex, longestValidSubstring):
                tokens.append([Token.SYMBOL, longestValidSubstring])
            i = lastValidJ
    return tokens