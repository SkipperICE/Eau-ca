import sys

# Vérification des arguments
if len(sys.argv) < 2:
    print("error")
    sys.exit()

# Tri des arguments (sorted trie en Ascii)
sorted_args = sorted(sys.argv[1:])

# Affichage des arguments triés
for arg in sorted_args:
    print(arg, end=' ')
print()