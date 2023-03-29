import sys

def fibonacci(n):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if len(sys.argv) != 2:
    print("Usage: python exo.py n")
    sys.exit(1)

n = int(sys.argv[1])
result = fibonacci(n)

if result == -1:
    print("Error: invalid argument")
else:
    print(result)

    