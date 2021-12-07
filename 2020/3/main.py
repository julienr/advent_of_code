import numpy as np

with open('input') as f:
    terrain = [list(line.strip()) for line in f]
terrain = np.array(terrain)
print(terrain, terrain.shape)

#terrain = np.tile(terrain, (1, int(np.ceil(terrain.shape[0] / terrain.shape[1]))))


def traverse(terrain, slope):
    i, j = (slope[0], slope[1])
    trees = 0
    while i < terrain.shape[0]:
        wrapped_j = j % terrain.shape[1]
        print(i, j, '   |', wrapped_j)
        if terrain[i, wrapped_j] == '#':
            trees += 1
        i += slope[0]
        j += slope[1]

    return trees

slopes = [
    (1, 1),
    (1, 3),
    (1, 5),
    (1, 7),
    (2, 1)
]
answer = 1
for slope in slopes:
    answer *= traverse(terrain, slope)
print(answer)
