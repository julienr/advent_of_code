import numpy as np

with open('input') as f:
    earliest = int(f.readline().strip())
    buses = f.readline().strip().split(',')

buses = [int(b) for b in buses if b != 'x']

min_id = 0
min_t = np.inf

for b in buses:
    closest_depart = int(np.ceil(earliest / b) * b)
    if closest_depart < min_t:
        min_t = closest_depart
        min_id = b

print(min_id, min_t)
print(min_id * (min_t - earliest))
