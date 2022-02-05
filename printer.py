from token import Token
import sys

def printTokens(tokens, output_file):
    for tokenType, tokenValue in tokens:
        if tokenType is Token.NUMBER:
            output_file.write(tokenValue+" : NUMBER\n")
        elif tokenType is Token.IDENTIFIER:
            output_file.write(tokenValue+" : IDENTIFIER\n")
        elif tokenType is Token.SYMBOL:
            output_file.write(tokenValue+" : SYMBOL\n")
        elif tokenType is Token.ERROR:
            output_file.write("ERROR READING \""+ tokenValue + "\"\n")
        else:
            print(f'Unexpected tokenType {tokenType}--aborting.')
            sys.exit()