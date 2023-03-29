import sys

if len(sys.argv) == 1:
    print("Error : no arguments provided")
    sys.exit(1)

args = sys.argv[1:]
args.reverse()

for arg in args:
    print(arg)