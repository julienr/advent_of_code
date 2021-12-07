commands = [l for l in open('input').read().split('\n') if len(l) > 0]
print(commands)

faces_right = ['N', 'E', 'S', 'W']
facing = 'E'
# X: west = -1, east = 1
# Y: south = -1, north = 1
pos = [0, 0]

def move_dir(d, value):
    if d == 'N':
        pos[1] += value
    elif d == 'S':
        pos[1] -= value
    elif d == 'E':
        pos[0] += value
    elif d == 'W':
        pos[0] -= value

for c in commands:
    l = c[0]
    value = int(c[1:])
    if l == 'R':
        assert value % 90 == 0
        n = value // 90
        i = (faces_right.index(facing) + n) % len(faces_right)
        facing = faces_right[i]
    elif l == 'L':
        assert value % 90 == 0
        n = value // 90
        i = (faces_right.index(facing) - n) % len(faces_right)
        facing = faces_right[i]
    elif l == 'F':
        move_dir(facing, value)
    else:
        move_dir(l, value)

print(pos)

print(abs(pos[0]) + abs(pos[1]))
