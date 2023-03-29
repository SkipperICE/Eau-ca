import sys

if len(sys.argv) != 2:
    print("error")
    sys.exit()

input = sys.argv[1]

if not input.isdigit():
    print("false")
    sys.exit(1)

print("True")