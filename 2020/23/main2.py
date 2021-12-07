# Real solution is in C++ in main2.cpp
import copy
import tqdm


cups = [int(n) for n in list('389125467')]
#cups = [int(n) for n in list('418976235')]
for i in range(len(cups), 1000000):
    cups.append(i)
current = 0

#print(cups)


def print_cups(current, cups):
    s = 'cups: '
    for i, c in enumerate(cups):
        if i == current:
            s += ' (%d)' % c
        else:
            s += '  %d ' % c
    print(s)


def find_destination(current, cups):
    label = cups[current % len(cups)]
    while True:
        label = label - 1
        if label <= 0:
            label = max(cups)
        for i in range(len(cups)):
            if cups[i] == label:
                return i


def move(current, cups):
    #print_cups(current, cups)

    # pick up
    picked_up = []
    for i in range(3):
        index = current + 1
        if index >= len(cups):
            index = index % len(cups)
            current -= 1
        else:
            pass
        c = cups.pop(index)
        picked_up.append(c)
    #print('pick up :', ', '.join(['%d' % n for n in picked_up]))
    #print('current', cups[current])

    # destination
    dest_index = find_destination(current, cups)
    #print('destination :', cups[dest_index])

    # put after destination
    index = dest_index
    for i in range(3):
        index += 1
        cups.insert(min(index, len(cups)), picked_up[i])
        if index <= current:
            current += 1

    # new current cup
    return (current + 1) % len(cups), cups


nmoves = 10000000
for i in tqdm.tqdm(range(1, nmoves + 1)):
    #print('\n-- move %d --' % i)
    current, cups = move(current, cups)

#print('\n-- final --')
#print_cups(current, cups)


# final string
s = ''
index = cups.index(1) + 1
for i in range(len(cups) - 1):
    s += '%d' % cups[index % len(cups)]
    index += 1
print(s)

