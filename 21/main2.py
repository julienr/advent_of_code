from collections import defaultdict
from functools import reduce

a2i = defaultdict(lambda: [])
all_ingredients = []

with open('input') as f:
    for line in f:
        if '(' in line:
            ingredients = line.split('(')[0].split(' ')
            alergens = line.split('(')[1].strip().strip(')')
            assert 'contains' in alergens
            alergens = alergens[len('contains'):].split(', ')
            alergens = [a.strip() for a in alergens]
        else:
            ingredients = line.split(' ')
            alergens = []
        ingredients = list(filter(lambda i: len(i) != 0, ingredients))
        all_ingredients.append(ingredients)
        for a in alergens:
            a2i[a].append(ingredients)
print(a2i)

candidates = {}

print('Solving')
for a, ilist in a2i.items():
    diff = reduce(lambda a, b: set(a) & set(b), ilist)
    diff = set(diff)
    candidates[a] = diff
print(candidates)

assignment = {}
while True:
    ingredient = None
    for a, candset in candidates.items():
        if len(candset) == 1:
            ingredient = list(candset)[0]
            assignment[ingredient] = a
            break
    if ingredient is None:
        break
    else:
        print('solved ', ingredient)
        for a in candidates.keys():
            if ingredient in candidates[a]:
                candidates[a].remove(ingredient)

print('assignment: ', assignment)


count = 0
for ilist in all_ingredients:
    for ing in ilist:
        if ing not in assignment:
            count += 1
print('count', count)

reverse_assignment = {a: i for i, a in assignment.items()}

canonical_list = []
for a in sorted(reverse_assignment.keys()):
    canonical_list.append(reverse_assignment[a])
print(','.join(canonical_list))
