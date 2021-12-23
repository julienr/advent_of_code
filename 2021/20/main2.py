import numpy as np

with open('input') as f:
    algo = ''
    for line in f:
        line = line.strip()
        if line == '':
            break
        algo += line
    algo = np.array([1 if c == '#' else 0 for c in algo])

    image = []
    for line in f:
        image.append([1 if c == '#' else 0 for c in line.strip()])
    image = np.array(image)


def prettyprint(arr):
    for row in arr:
        print(''.join(['#' if v == 1 else '.' for v in row]))
    print()


assert len(algo) == 512
print(len(algo), algo)
print(image)

def apply_filter(arr, lookup, cval=0):
    # Amount of padding: 2 out to be enough, but it's interesting to increase
    # it and check the result doesn't change for algo where the first bit
    # flips
    p = 2
    out = np.zeros((arr.shape[0] + 2*p, arr.shape[1] + 2*p))
    arr = np.pad(arr, (p + 2, p + 2), constant_values=cval)
    for i in range(out.shape[0]):
        for j in range(out.shape[1]):
            i2 = i + 2
            j2 = j + 2
            w = arr[(i2 - 1):(i2 + 2), (j2 - 1):(j2 + 2)]
            value = w.ravel().tolist()
            value = ''.join(['%d' % v for v in value])
            value = int(value, 2)
            out[i, j] = lookup[value]
    return out


enhanced = image.copy()
for i in range(50):
    #prettyprint(enhanced)
    if i % 2 == 0:
        cval = 0
    else:
        cval = algo[0]
    enhanced = apply_filter(enhanced, algo, cval=cval)
print(np.count_nonzero(enhanced))
