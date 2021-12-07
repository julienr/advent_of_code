from collections import defaultdict

def parse_instructions(line):
    instructions = []
    line = list(line)
    while len(line) > 0:
        inst = line.pop(0)
        if inst != 'e' and inst != 'w':
            inst += line.pop(0)
        instructions.append(inst)
    return instructions


def execute_line(line):
    instructions = parse_instructions(line)
    # We use double-width horiz layout
    # https://www.redblobgames.com/grids/hexagons/#coordinates-doubled
    # (col, row)
    coord = [0, 0]
    for inst in instructions:
        if inst == 'e':
            coord[0] += 2
        elif inst == 'se':
            coord[0] += 1
            coord[1] += 1
        elif inst == 'sw':
            coord[0] -= 1
            coord[1] += 1
        elif inst == 'w':
            coord[0] -= 2
        elif inst == 'nw':
            coord[0] -= 1
            coord[1] -= 1
        elif inst == 'ne':
            coord[0] += 1
            coord[1] -= 1
        assert (coord[0] + coord[1]) % 2 == 0
    return coord

tiles = set([])

def key(coord):
    return '%d:%d' % (coord[0], coord[1])

def unkey(key):
    return [int(v) for v in key.split(':')]

with open('input') as f:
    for line in f.readlines():
        coord = execute_line(line.strip())
        if key(coord) in tiles:
            tiles.remove(key(coord))
        else:
            tiles.add(key(coord))


def day(tiles):
    adj_black_counts = defaultdict(lambda : 0)

    for t in tiles:
        coord = unkey(t)
        displacements = [
            (2, 0),   # e
            (1, 1),   # se
            (-1, 1),  # sw
            (-2, 0),  # w
            (-1, -1), # nw
            (1, -1),  # ne
        ]

        for d in displacements:
            neigh_coord = [coord[0] + d[0], coord[1] + d[1]]
            adj_black_counts[key(neigh_coord)] += 1

    new_tiles = set(list(tiles))

    #print(adj_black_counts)

    for tile, black_count in adj_black_counts.items():
        coord = unkey(tile)
        if tile in tiles:
            # Any black tile with zero or more than 2 black tiles immediately
            # adjacent to it is flipped to white.
            if black_count > 2:
                #print('Flipping black tile %s' % tile)
                new_tiles.remove(tile)
        else:
            # Any white tile with exactly 2 black tiles immediately adjacent
            # to it is flipped to black.
            if black_count == 2:
                #print('Flipping white tile %s' % tile)
                new_tiles.add(tile)
    # Also need to flip black tiles with zero adjacent (won't be in adj_black_counts)
    for tile in tiles:
        if tile not in adj_black_counts:
            #print('Flipping black tile with no adj %s' % tile)
            new_tiles.remove(tile)

    return new_tiles

for i in range(1, 101):
    tiles = day(tiles)
    print('Day %d: %d' % (i, len(tiles)))

