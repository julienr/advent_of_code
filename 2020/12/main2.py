commands = [l for l in open('input').read().split('\n') if len(l) > 0]
print(commands)

facing = 'E'
# X: west = -1, east = 1
# Y: south = -1, north = 1
pos = [0, 0]
way = [10, 1]

#10, 1
#-1, -10

#[[0, -1]]   [10]     [-1]
#[[1, 0]]    [1]    = [10]

#[[0, 1]]


def rotate_way_left(n):
    global way
    for i in range(n):
        new_way = [-way[1], way[0]]
        way = new_way

def rotate_way_right(n):
    global way
    for i in range(n):
        new_way = [way[1], -way[0]]
        way = new_way

def move_waypoint(d, value):
    if d == 'N':
        way[1] += value
    elif d == 'S':
        way[1] -= value
    elif d == 'E':
        way[0] += value
    elif d == 'W':
        way[0] -= value

def move_to_waypoint(n):
    pos[0] += n * way[0]
    pos[1] += n * way[1]

for c in commands:
    l = c[0]
    value = int(c[1:])
    if l == 'R':
        assert value % 90 == 0
        n = value // 90
        rotate_way_right(n)
    elif l == 'L':
        assert value % 90 == 0
        n = value // 90
        rotate_way_left(n)
    elif l == 'F':
        move_to_waypoint(value)
    else:
        move_waypoint(l, value)
    print(pos, way)

print(pos)

print(abs(pos[0]) + abs(pos[1]))
