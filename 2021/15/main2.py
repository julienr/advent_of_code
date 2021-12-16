import sys
import numpy as np
import heapq

with open('input') as f:
    m = np.array([[int(i) for i in l.strip()] for l in f.readlines()])

if True:
    print(m)
    row = m.copy()
    for j in range(4):
        tmp = row[-m.shape[0]:, -m.shape[1]:].copy()
        tmp += 1
        tmp[tmp > 9] = 1
        row = np.concatenate((row, tmp), axis=1)

    for i in range(4):
        row2 = row[-m.shape[0]:, :].copy()
        row2 += 1
        row2[row2 > 9] = 1
        row = np.concatenate((row, row2), axis=0)

    m = row

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
    nodes = [tuple(v) for v in np.indices((m.shape[0], m.shape[1])).reshape(2, -1).transpose()]
    dist = {k: np.inf for k in nodes}
    prev = {k: None for k in nodes}

    # Start top left
    dist[0, 0] = 0

    #to_explore = [(dist[v], v) for v in nodes]
    #heapq.heapify(to_explore)
    to_explore = [(0, (0, 0))]

    while len(to_explore) > 0:
        if len(to_explore) % 100 == 0:
            print(len(to_explore))
        #i = get_with_min_dist(to_explore, dist)
        #v = to_explore[i]
        #del to_explore[i]
        _, v = heapq.heappop(to_explore)

        # Could early exit if v == target ?
        if v == (m.shape[0] - 1, m.shape[1] - 1):
            break

        for neigh in neighbors(v, m):
            candidate_dist = dist[v] + m[neigh]
            if candidate_dist < dist[neigh]:
                curr_dist = dist[neigh]
                dist[neigh] = candidate_dist
                prev[neigh] = v

                # update if in list, otherwise add
                try:
                    index = to_explore.index((curr_dist, neigh))
                    to_explore[index] = (dist[neigh], neigh)
                    heapq.heapify(to_explore)
                except ValueError as e:
                    heapq.heappush(to_explore, (dist[neigh], neigh))


    return dist

print(m)
dist = shortest_path(m)
print(dist[m.shape[0] - 1, m.shape[1] - 1])
