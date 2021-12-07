import copy

lines = [l.strip() for l in open('input').read().split('\n')]
lines = filter(lambda l: len(l) > 0, lines)


class InfiniteLoopError(Exception):
    pass


def execute(lines):
    execution_counts = [0] * len(lines)

    pc = 0
    acc = 0
    while True:
        if pc == len(lines):
            break
        if execution_counts[pc] > 0:
            raise InfiniteLoopError()
        execution_counts[pc] += 1

        l = lines[pc]
        opcode, arg = l.split(' ')
        arg = int(arg)
        if opcode == 'nop':
            pc += 1
            continue
        elif opcode == 'acc':
            acc += arg
            pc += 1
        elif opcode == 'jmp':
            pc += arg
        else:
            raise RuntimeError(l)
    return acc

# Generate all possible programs by changing jmp to nop or nop to jmp
possible_programs = []
for i in range(len(lines)):
    new_prog = copy.deepcopy(lines)
    if new_prog[i].startswith('nop'):
        new_prog[i] = new_prog[i].replace('nop', 'jmp')
    elif new_prog[i].startswith('jmp'):
        new_prog[i] = new_prog[i].replace('jmp', 'nop')
    else:
        continue
    #print(new_prog)
    try:
        acc = execute(new_prog)
        print('Yay !', acc)
        break
    except InfiniteLoopError:
        print('Infinite loop')
        pass

#print(execute(lines))
