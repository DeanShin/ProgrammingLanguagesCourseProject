# Dean Shin and Kunal Babbar -- Phase 3.2
import sys
import scanner
from evaluator import Evaluator
from parser import Parser
import printer

if len(sys.argv) < 2:
    print("Input file not specified.")
    sys.exit()
if len(sys.argv) < 3:
    print("Output file not specified.")
    sys.exit()

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]
    
with open(input_file_path, 'r') as input_file:
    with open(output_file_path, 'w') as output_file:
        tokens = []

        line = input_file.readline()
        while line:
            try:
                tokens.extend(scanner.scan(line))
            except Exception as ex:
                output_file.write(ex.args[0])
                sys.exit()
            line = input_file.readline()

        output_file.write("Tokens: \n\n")
        printer.printTokens(tokens, output_file)
        output_file.write('\n')

        parser = Parser(tokens)
        try:
            ast = parser.parseTokens()
        except Exception as ex:
            output_file.write(ex.args[0])
            sys.exit()

        output_file.write("AST: \n\n")
        printer.printAST(ast, output_file)
        output_file.write('\n')

        evaluator = Evaluator(ast)
        try:
            result = evaluator.evaluate()
        except Exception as ex:
            output_file.write(ex.args[0])
            sys.exit()

        output_file.write(f"Output: \n")
        printer.printOutput(result, output_file)

            