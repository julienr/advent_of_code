import numpy as np

arr = [list(l) for l in open('input').read().split('\n') if len(l) > 0]
arr = np.array(arr)

print(arr)

def step(arr):
    new_arr = np.copy(arr)
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if arr[i, j] == '.':
                continue
            neigh = arr[
                max(0, i-1):min(arr.shape[0], i+2),
                max(0, j-1):min(arr.shape[1], j+2)
            ]
            #if i == 0 and j == 2:
                #print(neigh)
            n_occupied = np.sum(neigh == '#')
            if arr[i, j] == 'L' and n_occupied == 0:
                new_arr[i, j] = '#'
            # 5 because we count ourselves
            elif arr[i, j] == '#' and n_occupied >= 5:
                new_arr[i, j] = 'L'
    n_changes = np.sum(arr != new_arr)
    return new_arr, n_changes


while True:
    arr, n_changes = step(arr)
    if n_changes == 0:
        break
print(arr)

print(np.sum(arr == '#'))
