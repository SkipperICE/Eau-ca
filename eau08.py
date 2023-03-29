import sys

if len(sys.argv) != 2:
    print("error")
    sys.exit()

input_str = sys.argv[1]

if not input_str.isalpha():
    print("Error: invalid argument")
    sys.exit(1)


output_str = input_str.title()

print(output_str)