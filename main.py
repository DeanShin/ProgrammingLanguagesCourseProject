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


def driver(input_file_path, output_file_path):
    input_file = open(input_file_path, "r")
    output_file = open(output_file_path,"w")
    for line in input_file:
        first_line = line.strip()
        output_file.write("%s\n"%first_line)
        # scanner function(first_line)
    input_file.close()
    output_file.close()
