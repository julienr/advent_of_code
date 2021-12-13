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
print(lowpoints)

#for i, j in lowpoints:
    #print('== lowpoint i=%d, j=%d' % (i, j))
    #print(h[i-2:i+3, j-2:j+3])

risk = sum([h[i, j] + 1 for (i, j) in lowpoints])
print('risk=%d' % risk)
