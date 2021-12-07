import numpy as np
with open('input') as f:
    lines = [l for l in f.read().split('\n') if l.strip() != '']
    state = np.array([[list(l) for l in lines]])
print(state)
#state = np.array([[
    #['.', '#', '.'],
    #['.', '.', '#'],
    #['#', '#', '#'],
#]])


def print_state(state):
    for z in range(state.shape[0]):
        s = state[z]
        print('z=%d' % z)
        for i in range(s.shape[0]):
            print(''.join(list(s[i])))
        print()


def get_neighbors(state, z, i, j):
    neigh = []
    for dz in [-1, 0, 1]:
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if dz == di == dj == 0:
                    continue
                neigh.append(get_state(state, z + dz, i + di, j + dj))
    return np.array(neigh)


def get_state(state, z, i, j):
    if z < 0 or z >= state.shape[0]:
        return '.'
    if i < 0 or i >= state.shape[1]:
        return '.'
    if j < 0 or j >= state.shape[2]:
        return '.'
    return state[z, i, j]


def step(state):
    new_state = np.zeros((
        state.shape[0] + 2,
        state.shape[1] + 2,
        state.shape[2] + 2
    ), dtype=state.dtype)

    for nz in range(new_state.shape[0]):
        for ni in range(new_state.shape[1]):
            for nj in range(new_state.shape[2]):
                z = nz - 1
                i = ni - 1
                j = nj - 1
                curr = get_state(state, z, i, j)
                neighbors = get_neighbors(state, z, i, j)
                if curr == '#':
                    num_neigh_active = np.count_nonzero(neighbors == '#')
                    if num_neigh_active == 2 or num_neigh_active == 3:
                        new_state[nz, ni, nj] = '#'
                    else:
                        new_state[nz, ni, nj] = '.'
                elif curr == '.':
                    num_neigh_active = np.count_nonzero(neighbors == '#')
                    if num_neigh_active == 3:
                        new_state[nz, ni, nj] = '#'
                    else:
                        new_state[nz, ni, nj] = '.'

    return new_state


for cycle in range(6):
    print('After %d cycles' % cycle)
    print_state(state)
    state = step(state)

    print('%d active' % np.count_nonzero(state == '#'))
