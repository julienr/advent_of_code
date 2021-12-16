import numpy as np

with open('input') as f:
    m = np.array([[int(i) for i in l.strip()] for l in f.readlines()])


def get_with_min_dist(to_explore, dist):
    dmin = np.inf
    index = None
    for i, v in enumerate(to_explore):
        if dist[v] < dmin:
            dmin = dist[v]
            index = i
    return index

def are_neighbor(v, k):
    return np.sum(np.abs(np.array(v) - np.array(k))) == 1


def neighbors(v, m):
    if v[0] > 0:
        yield (v[0] - 1, v[1])
    if v[0] < m.shape[1] - 1:
        yield (v[0] + 1, v[1])
    if v[1] > 0:
        yield (v[0], v[1] - 1)
    if v[1] < m.shape[0] - 1:
        yield (v[0], v[1] + 1)


def shortest_path(m):
    to_explore = [tuple(v) for v in np.indices((m.shape[0], m.shape[1])).reshape(2, -1).transpose()]
    dist = {k: np.inf for k in to_explore}
    prev = {k: None for k in to_explore}

    # Start top left
    dist[0, 0] = 0
    while len(to_explore) > 0:
        if len(to_explore) % 100 == 0:
            print(len(to_explore))
        i = get_with_min_dist(to_explore, dist)
        v = to_explore[i]
        del to_explore[i]

        # Could early exit if v == target ?
        if v == (m.shape[0] - 1, m.shape[1] - 1):
            break

        #for neigh in to_explore:
        #    if are_neighbor(v, neigh):
        for neigh in neighbors(v, m):
            candidate_dist = dist[v] + m[neigh]
            if candidate_dist < dist[neigh]:
                dist[neigh] = candidate_dist
                prev[neigh] = v

    return dist

print(m)
dist = shortest_path(m)
print(dist[m.shape[0] - 1, m.shape[1] - 1])
