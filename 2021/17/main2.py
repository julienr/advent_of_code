
def step(x, y, vx, vy):
    x2 = x + vx
    y2 = y + vy
    if vx < 0:
        vx2 = vx + 1
    elif vx == 0:
        vx2 = vx
    else:
        vx2 = vx - 1
    vy2 = vy - 1

    return x2, y2, vx2, vy2


#target_area = ((20, 30), (-10, -5))
target_area = ((119, 176), (-141, -84))

def launch(x, y, vx, vy):
    highest_y = y
    for i in range(400):
        x, y, vx, vy = step(x, y, vx, vy)
        if y > highest_y:
            highest_y = y
        in_target = target_area[0][0] <= x <= target_area[0][1] and \
                    target_area[1][0] <= y <= target_area[1][1]
        #print('step=%d, pos=(%d, %d), v=(%d, %d)' % (i, x, y, vx, vy))
        if in_target:
            print('in target at step=%d!' % i)
            return True, highest_y
    else:
        return False, highest_y

count = 0
for vx in range(0, 200):
    for vy in range(-200, 300):
        on_target, launch_highest_y = launch(0, 0, vx, vy)
        if on_target:
            print(vx, vy)
            count += 1
print(count)
