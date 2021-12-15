from collections import Counter
import numpy as np

rules = {}

with open('test_input') as f:
    template = f.readline().strip()
    assert f.readline().strip() == ''
    for line in f:
        pair, target = line.strip().split(' -> ')
        rules[pair] = target

def step(template):
    out = template[0]
    for i in range(0, len(template) - 1):
        pair = template[i:i+2]
        out += rules[pair] + pair[1]
    return out

print(template)

for i in range(10):
    template = step(template)
    #print('== step %d' % i)
    #print(template)

counts = Counter(template)
print(counts)

cmax = np.max(list(counts.values()))
cmin = np.min(list(counts.values()))
print(cmax - cmin)
