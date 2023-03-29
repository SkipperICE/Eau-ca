import sys

if len(sys.argv) != 3:
    print("Usage: python exo.py n")
    sys.exit(1)

try:
    n = str(sys.argv[1])
except ValueError:
    print("Error: invalid argument")
    sys.exit(1)

try:
    n = str(sys.argv[2])
except ValueError:
    print("Error: invalid argument")
    sys.exit(1)

chaine1 = sys.argv[1]
chaine2 = sys.argv[2]

if chaine2 in chaine1:
    print("true")
else:
    print("false")