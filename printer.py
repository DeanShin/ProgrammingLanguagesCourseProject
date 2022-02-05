from token import Token

def printTokens(tokens):
    for tokenType, tokenValue in tokens:
        if tokenType is Token.NUMBER:
            print(tokenValue+" : NUMBER")
        elif tokenType is Token.IDENTIFIER:
            print(tokenValue+" : IDENTIFIER")
        elif tokenType is Token.SYMBOL:
            print(tokenValue+" : SYMBOL")
        elif tokenType is Token.ERROR):
            print("ERROR READING \""+ tokenValue + "\"")