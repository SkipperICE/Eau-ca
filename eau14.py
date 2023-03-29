import sys

# Définition de la fonction de tri par sélection
def my_selection_sort(array):
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array

# Vérification des arguments
if len(sys.argv) < 2:
    print("error")
    sys.exit()

# Conversion des arguments en nombres
try:
    nums = [int(arg) for arg in sys.argv[1:]]
except ValueError:
    print("Donne des nombres chackal")
    sys.exit()

# Tri de la liste
sorted_nums = my_selection_sort(nums)

# Affichage de la liste triée
for num in sorted_nums:
    print(num, end=' ')
print()