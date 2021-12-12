import numpy as np
import sys

with open('input') as f:
    positions = [int(v) for v in f.read().split(',')]

#print(positions)
positions = np.array(positions)
pmin, pmax = positions.min(), positions.max()

def cost(positions, v):
    diff = np.abs(positions - v)
    # Sum of integers up to n
    # (n * (n + 1)) / 2
    return (diff * (diff + 1)) / 2


all_costs = [sum(cost(positions, v)) for v in range(pmin, pmax)]
#print(all_costs)
print(int(min(all_costs)))
