import numpy as np

dots = []
folds = []
with open('input') as f:
    for line in f:
        if len(line.strip()) == 0:
            continue
        if line.startswith('fold'):
            folds.append(line.split(' ')[2].strip().split('='))
        else:
            dots.append([int(v) for v in line.strip().split(',')])

dots = np.array(dots)

xmax, ymax = dots.max(axis=0)
xmax += 1
ymax += 1
if xmax % 2 == 0:
    xmax += 1
if ymax % 2 == 0:
    ymax += 1

arr = np.zeros([ymax, xmax], dtype=np.bool)
for x, y in dots:
    arr[y, x] = True

def p(arr):
    for i in range(arr.shape[0]):
        line = ''
        for j in range(arr.shape[1]):
            if arr[i, j]:
                line += '#'
            else:
                line += '.'
        print(line)
    print()


def fold_x(arr, x):
    first = arr[:, :x]
    second = arr[:, (x+1):]
    return first + second[:, ::-1]

def fold_y(arr, y):
    first = arr[:y, :]
    second = arr[(y+1):, :]
    return first + second[::-1, :]

#p(arr)
for axis, v in folds:
    if axis == 'x':
        arr = fold_x(arr, int(v))
    else:
        arr = fold_y(arr, int(v))
p(arr)

#print(np.count_nonzero(arr))
