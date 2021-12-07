import sys

with open('input') as f:
    numbers = [int(line) for line in f]
print(numbers)

for i, n1 in enumerate(numbers):
    for n2 in numbers[i:]:
        if n1 + n2 == 2020:
            print(n1 * n2)
            sys.exit()
