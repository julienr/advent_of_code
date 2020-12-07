import sys

with open('input') as f:
    numbers = [int(line) for line in f]
print(numbers)

for i, n1 in enumerate(numbers):
    for j, n2 in enumerate(numbers[i:]):
        for n3 in numbers[j:]:
            if n1 + n2 + n3 == 2020:
                print(n1 * n2 * n3)
                sys.exit()
