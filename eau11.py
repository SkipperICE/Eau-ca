import sys

if len(sys.argv) <= 2:
    print("il manque au moins un argument")
    sys.exit()

tableau = sys.argv[1:-1]
search_elem = sys.argv[-1]

try:
    index = tableau.index(search_elem)
    print(index)
except ValueError:
    print("-1")