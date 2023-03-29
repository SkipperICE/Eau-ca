

# 1 - crrer une liste des elements
#s'assurer que les argument sont bien des nombres
#2- trier la liste en ordre croissant
#3- regarder la difference entre tout les elements 
#4- print result 


import sys

if len(sys.argv) < 2:
    print("error")
    sys.exit()


try:
    nums = [int(arg) for arg in sys.argv[1:]]
except ValueError:
    print("Donne des nombres chackal")
    sys.exit()

min_diff = float('inf')
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        diff = abs(nums[i] - nums[j])
        if diff < min_diff:
            min_diff = diff

print(min_diff)