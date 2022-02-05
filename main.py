# Dean Shin and Kunal Babbar -- Phase 1.1
import sys
import scanner
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
        line = input_file.readline().strip()
        while(line):
            output_file.write(f'Line: {line}\n')
            tokens = scanner.scan(line)
            printer.printTokens(tokens, output_file)
            output_file.write('\n')
            line = input_file.readline().strip()