import numpy as np
import sys

with open('input') as f:
    positions = [int(v) for v in f.read().split(',')]

print(positions)

s = sorted(positions)
median = s[len(s) // 2]

costs = np.abs(np.array(positions) - median)
print(sum(costs))


