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

with open('input') as f:
    for line in f.readlines():
        coord = execute_line(line.strip())
        if key(coord) in tiles:
            tiles.remove(key(coord))
        else:
            tiles.add(key(coord))

print(len(tiles))

