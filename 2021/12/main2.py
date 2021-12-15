from collections import defaultdict, Counter

g = defaultdict(lambda: [])

with open('input') as f:
    for line in f:
        a, b = line.strip().split('-')
        g[a].append(b)
        g[b].append(a)

print(g)

def is_big(cave):
    return cave.isupper()

def has_small_visited_twice(visited):
    counts = Counter(visited)
    for key, count in counts.items():
        if is_big(key):
            continue
        if key == 'start' or key == 'end':
            continue
        if count >= 2:
            return True
    return False

def explore(node, g, visited):
    count = 0
    visited = list(visited) + [node]
    #print('neighbor of %s: %s' % (node, g[node]))
    for neigh in sorted(g[node]):
        if neigh == 'start':
            continue
        if neigh == 'end':
            path = visited + [neigh]
            print(','.join(path))
            count += 1
            continue

        if not is_big(neigh) and neigh in visited and has_small_visited_twice(visited):
            continue

        count += explore(neigh, g, visited)
    return count

count = explore('start', g, [])
print(count)

