from collections import Counter
import numpy as np

rules = {}

with open('input') as f:
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

def expand(template, steps):
    for i in range(steps):
        template = step(template)
    return template

N = 40
lookup = {}
for pair in rules.keys():
    lookup[pair] = Counter(expand(pair, N//2)[1:])
#print(lookup_5)

#def get_counts(template, iterations):
    #for i in range(iterations):
        #template = step(

tpl_half = expand(template, N//2)
totals = Counter()
for i in range(0, len(tpl_half)):
    if i == len(tpl_half) - 1:
        continue
    totals += lookup[tpl_half[i:i+2]]
# Compensate for the topmost beginning letter that is skipped above because
# of the 1:
totals += Counter(template[0])
print(totals)

#counts = Counter(expand(template, N))
#print(counts)

cmax = np.max(list(totals.values()))
cmin = np.min(list(totals.values()))
print(cmax - cmin)
