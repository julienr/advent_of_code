import numpy as np
import sys

lines = []
with open('input') as f:
    for line in f:
        start, end = line.split(' -> ')
        x1, y1 = [int(v) for v in start.split(',')]
        x2, y2 = [int(v) for v in end.split(',')]

        lines.append([(x1, y1), (x2, y2)])

lines = np.array(lines)
xmin = lines[:,:,0].min()
xmax = lines[:,:,0].max()
ymin = lines[:,:,1].min()
ymax = lines[:,:,1].max()
print(xmin, xmax, ymin, ymax)
#assert xmin == ymin == 0

raster = np.zeros((ymax + 1, xmax + 1), dtype=np.int32)

for line in lines:
    x1, y1 = line[0]
    x2, y2 = line[1]

    x, y = x1, y1
    dx = np.sign(x2 - x1)
    dy = np.sign(y2 - y1)

    diff = max(np.abs(x2 - x1), np.abs(y2 - y1))
    for i in range(diff + 1):
        raster[y + i * dy, x + i * dx] += 1

print(raster)
print(np.count_nonzero(raster >= 2))


