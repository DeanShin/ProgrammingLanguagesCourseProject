def printTokens(tokens):
    for tokenType, tokenValue in tokens:
        if tokenType is Token.NUMBER:
            print(tokenValue+": NUMBER")
        if tokenType is Token.IDENTIFIER:
            print(tokenValue+": IDENTIFIER")
        if tokenType is Token.SYMBOL:
            print(tokenValue+": SYMBOL")
    return