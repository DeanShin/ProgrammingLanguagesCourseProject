import sys
import scanner
import printer

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

if not input_file_path:
    print("Input file not specified.")
    sys.exit()
if not output_file_path:
    print("Output file not specified.")
    sys.exit()
    
with open(input_file_path, 'r') as input_file:
    with open(output_file_path, 'w') as output_file:
        line = input_file.readline()
        while(line):
            print(f'Line: {line}')
            tokens = scanner.scan(line)
            printer.printTokens(tokens)
            line = input_file.readline()