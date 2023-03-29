import sys

if len(sys.argv) != 3:
    print("error")
    sys.exit()

try:
    min_val = int(sys.argv[1])
    max_val = int(sys.argv[2])
except ValueError:
    print("error")
    sys.exit()

min_val, max_val = sorted([min_val, max_val])

for val in range(min_val, max_val):
    print(val, end=' ')
print()