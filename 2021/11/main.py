import numpy as np

with open('input') as f:
    energy = []
    for l in f.readlines():
        energy.append([int(c) for c in l.strip()])
    energy = np.array(energy)

def in_bounds(i, j, arr):
    return i >= 0 and i < arr.shape[0] and j >= 0 and j < arr.shape[1]

def step(energy):
    energy += 1
    flashed = np.zeros((energy.shape[0], energy.shape[1]), dtype=np.bool)

    to_flash = np.argwhere(energy > 9).tolist()
    while len(to_flash) > 0:
        i, j = to_flash.pop()
        if flashed[i, j]:
            continue
        flashed[i, j] = True

        spread = [
            (i-1, j-1),
            (i-1, j),
            (i-1, j+1),
            (i, j-1),
            (i, j+1),
            (i+1, j-1),
            (i+1, j),
            (i+1, j+1)
        ]
        for i, j in spread:
            if in_bounds(i, j, energy):
                energy[i, j] += 1
                if energy[i, j] > 9 and not flashed[i, j]:
                    to_flash.append((i, j))
    energy[flashed] = 0
    return np.count_nonzero(flashed)

print(energy)
total = 0
for i in range(100):
    print('== step %d' % (i + 1))
    total += step(energy)
    print(energy)
print(total)
