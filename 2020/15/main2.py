numbers = list(map(int, open('input').read().split(',')))
print(numbers)

memory = {}

turn = 1
for n in numbers:
    last_spoken = n
    memory[last_spoken] = (turn, None)
    turn += 1
    #print(last_spoken)

max_turns = 30000000

while turn <= max_turns:
    if turn % 100000 == 0:
        print('%g / %g' % (turn, max_turns))
    #print('-- turn %d' % turn)
    #print('memory: %s' % memory)
    #print('last_spoken: %d' % last_spoken)
    if last_spoken in memory and memory[last_spoken][1] is not None:
        last_spoken = memory[last_spoken][0] - memory[last_spoken][1]
    else:
        last_spoken = 0
    memory[last_spoken] = (turn, memory.get(last_spoken, [None])[0])

    #print('speak %d' % last_spoken)
    turn += 1
print(last_spoken)
