from collections import Counter

lst = [int(s) for s in open('input').read().split('\n') if s != '']

lst = sorted(lst)
lst = [0] + lst + [lst[-1] + 3]

#lst = [0, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 16, 19, 22]
print(lst)

def lst_diffs(lst):
    diffs = []
    for i in range(1, len(lst)):
        diffs.append(lst[i] - lst[i-1])
    return diffs

diffs = lst_diffs(lst)
print(diffs)

d = reduce(lambda a, b: a + b, map(str, diffs))
d = d.split('3')
d = filter(lambda l: len(l) > 0, d)
print(d)

lengths = map(len, d)
print(max(lengths))

#    1 1 1 1
#    1 0 1 1
#    1 1 0 1
#    1 0 0 1
#    0 1 1 1
#    0 0 1 1
#    0 1 0 1
#
#    1 1 1
#    1 0 1
#    0 1 1
#    0 0 1
#
#    1 1
#    0 1
#
#    1
#    0
#
solution = {
    '1111': 7,
    '111': 4,
    '11': 2,
    '1': 1
}

combinations = 1
for s in d:
    combinations *= solution[s]
print(combinations)
