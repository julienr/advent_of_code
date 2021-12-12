import numpy as np
import sys

lines = []
with open('input') as f:
    for line in f:
        start, end = line.split(' -> ')
        x1, y1 = [int(v) for v in start.split(',')]
        x2, y2 = [int(v) for v in end.split(',')]

        # Swap to ensure x2 > x1, y2 > y1
        if x2 < x1:
            tmp = x2
            x2 = x1
            x1 = tmp
        if y2 < y1:
            tmp = y2
            y2 = y1
            y1 = tmp

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
    if not (x1 == x2 or y1 == y2):
        #print('skipping %d %d -> %d %d' % (x1, y1, x2, y2))
        continue
    if x1 == x2:
        raster[y1:(y2+1), x1] += 1
    else:
        raster[y1, x1:(x2+1)] += 1

print(raster)
print(np.count_nonzero(raster >= 2))


