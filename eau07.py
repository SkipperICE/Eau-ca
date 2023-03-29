import sys

if len(sys.argv) != 2:
    print("Usage: python exo.py argument en format string")
    sys.exit(1)

chaine = sys.argv[1]

if not chaine.isalpha():
    print("Error: invalid argument")
    sys.exit(1)

resultat = ""

for i, c in enumerate(chaine):
    if c.isalpha() and i % 2 == 0:
        resultat += c.upper()
    else:
        resultat += c

print(resultat)
