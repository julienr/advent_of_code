from collections import Counter

lst = [int(s) for s in open('input').read().split('\n') if s != '']

lst = sorted(lst)
lst = [0] + lst + [lst[-1] + 3]

diffs = []
for i in range(1, len(lst)):
    diffs.append(lst[i] - lst[i-1])

c = Counter(diffs)
print(c)
print(c[1] * c[3])


