import sys

# Définition de la fonction de tri à bulle
def my_bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
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
sorted_nums = my_bubble_sort(nums)

# Affichage de la liste triée sans [] et sans,
for num in sorted_nums:
    print(num, end=' ')
print()