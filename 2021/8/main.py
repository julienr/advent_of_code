import numpy as np
import sys

lines = []
with open('test_input') as f:
    for line in f:
        if len(line.strip()) == 0:
            continue
        print(line)
        left, right = line.split('|')
        lines.append((left.strip(), right.strip()))

print(lines)

# 1 uses 2
# 4 uses 4
# 7 uses 3
# 8 uses 7
unique = set([2, 4, 3, 7])

count = 0
for left, right in lines:
    words = [v.strip() for v in right.split(' ') if len(v.strip()) > 0]
    for w in words:
        if len(w) in unique:
            count += 1

print(count)


