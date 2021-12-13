import numpy as np
import sys

lines = []
with open('input') as f:
    for line in f:
        lines.append([int(v) for v in line.strip()])

h = np.array(lines)
print(h)

lowpoints = []
for i in range(h.shape[0]):
    for j in range(h.shape[1]):
        if i > 0 and h[i, j] >= h[i - 1, j]:
            continue
        if i < h.shape[0] - 1 and h[i, j] >= h[i + 1, j]:
            continue
        if j > 0 and h[i, j] >= h[i, j - 1]:
            continue
        if j < h.shape[1] - 1 and h[i, j] >= h[i, j + 1]:
            continue
        lowpoints.append((i, j))
#print(lowpoints)

#for i, j in lowpoints:
    #print('== lowpoint i=%d, j=%d' % (i, j))
    #print(h[i-2:i+3, j-2:j+3])

def find_bassin(h, lowpoints):
    # watershed anyone ? :)
    bassins = np.zeros_like(h)
    bassins[:] = -1
    # Start by assigning lowpoints
    for value, (i, j) in enumerate(lowpoints):
        bassins[i, j] = value
    #print(bassins)

    sizes = []
    explored = np.zeros((h.shape[0], h.shape[1]), dtype=np.bool)
    for bassin in range(len(lowpoints)):
        size = 0
        to_explore = []
        def _expl(i, j):
            if not explored[i, j]:
                explored[i, j] = True
                to_explore.append((i, j))

        _expl(*lowpoints[bassin])

        while len(to_explore) > 0:
            i, j = to_explore.pop()
            #print('== %d, %d' % (i, j))
            if h[i, j] != 9:
                size += 1
                if i >= 1:
                    _expl(i-1, j)
                if i < h.shape[0] - 1:
                    _expl(i+1, j)
                if j >= 1:
                    _expl(i, j-1)
                if j < h.shape[1] - 1:
                    _expl(i, j+1)
                #print('to_explore: ', to_explore)
        sizes.append(size)

    sizes = sorted(sizes, reverse=True)
    print(sizes[0] * sizes[1] * sizes[2])

find_bassin(h, lowpoints)
