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

def yes_per_group(group):
    return len(set(''.join(group)))

yes_counts = list(map(yes_per_group, groups))
print(sum(yes_counts))
