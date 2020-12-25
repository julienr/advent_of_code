with open('input') as f:
    card_pub = int(f.readline())
    door_pub = int(f.readline())


def transform(n, loop_size):
    v = 1
    for i in range(loop_size):
        v *= n
        v = v % 20201227
    return v


def generate(n):
    v = 1
    loop_size = 1
    while True:
        v *= n
        v = v % 20201227
        yield v, loop_size
        loop_size += 1


it = iter(generate(7))
for i in range(10000000):
    v, loop_size = next(it)
    #print(v)
    if v == card_pub:
        card_loop_size = loop_size
        card_pub = v
        print('card loop size = %d' % loop_size)
    if v == door_pub:
        door_loop_size = loop_size
        door_pub = v
        print('door loop size = %d' % loop_size)

print(card_pub)
print('key:', transform(card_pub, door_loop_size))

