import sys

if len(sys.argv) != 2:
    print("Usage: python exo.py n")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("Error: invalid argument")
    sys.exit(1)


def est_premier(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(sys.argv[1])

if n < 0:
    print("-1")
    sys.exit(1)

i = n + 1

while True:
    if est_premier(i):
        print(i)
        break
    i += 1
