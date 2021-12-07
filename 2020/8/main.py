lines = [l.strip() for l in open('input_test').read().split('\n')]
lines = filter(lambda l: len(l) > 0, lines)

execution_counts = [0] * len(lines)

pc = 0
acc = 0
while True:
    if pc == len(lines):
        break
    if execution_counts[pc] > 0:
        break
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

print(acc)
