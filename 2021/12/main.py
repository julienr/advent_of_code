from collections import defaultdict

g = defaultdict(lambda: [])

with open('input') as f:
    for line in f:
        a, b = line.strip().split('-')
        g[a].append(b)
        g[b].append(a)

print(g)

def is_big(cave):
    return cave.isupper()

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

        if not is_big(neigh) and neigh in visited:
            continue

        count += explore(neigh, g, visited)
    return count

count = explore('start', g, [])
print(count)

