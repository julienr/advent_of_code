import sys
import numpy as np

arr = [list(l) for l in open('input').read().split('\n') if len(l) > 0]
arr = np.array(arr)

def occupied_seen_from(arr, i, j):
    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1)
    ]
    n_occupied = 0
    # raytrace in each direction
    for di, dj in directions:
        ci, cj = i + di, j + dj
        while True:
            if ci < 0 or cj < 0 or ci >= arr.shape[0] or cj >= arr.shape[1]:
                break
            elif arr[ci, cj] == '.':
                pass
            elif arr[ci, cj] == 'L':
                break
            elif arr[ci, cj] == '#':
                n_occupied += 1
                break
            ci += di
            cj += dj
    return n_occupied

#print(occupied_seen_from(arr, 3, 3))
#sys.exit(-1)

def step(arr):
    new_arr = np.copy(arr)
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if arr[i, j] == '.':
                continue
            n_occupied = occupied_seen_from(arr, i, j)
            if arr[i, j] == 'L' and n_occupied == 0:
                new_arr[i, j] = '#'
            elif arr[i, j] == '#' and n_occupied >= 5:
                new_arr[i, j] = 'L'
    n_changes = np.sum(arr != new_arr)
    return new_arr, n_changes


print(arr)
while True:
    arr, n_changes = step(arr)
    print('n_changes=%d' % n_changes)
    print(arr)
    if n_changes == 0:
        break
print(arr)

print(np.sum(arr == '#'))
