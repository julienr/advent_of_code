from collections import defaultdict

groups = []
with open('input') as f:
    accum = []
    for line in f:
        if len(line.strip()) == 0:
            groups.append(accum)
            accum = []
        else:
            accum.append(line.strip())
    groups.append(accum)

print(groups)

def all_yes_per_group(group):
    counts = defaultdict(lambda: 0)
    for answers in group:
        for c in answers:
            counts[c] += 1

    all_yes = 0
    for v in counts.values():
        if v == len(group):
            all_yes += 1
    return all_yes

yes_counts = list(map(all_yes_per_group, groups))
print(sum(yes_counts))
