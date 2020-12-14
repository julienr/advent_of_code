import re

def parse_mem_instruction(instruction):
    m = re.match(r'mem\[(\d+)\] = (\d+)', instruction)
    return (int(m.group(1)), int(m.group(2)))

with open('input') as f:
    instructions = []
    for line in f:
        line = line.strip()
        if line == '':
            continue
        if line.startswith('mask'):
            msk = line.split('=')[1].strip()
            instructions.append(('setmask', msk))
        else:
            instructions.append(('mem', parse_mem_instruction(line)))

print('instructions', instructions)

def bitmask(val, msk):
    assert len(val) == len(msk)
    outval = list(val)
    for i, c in enumerate(msk):
        if c == '0':
            continue
        else:
            outval[i] = c
    return "".join(outval)


def all_addr(addr):
    queue = [addr]
    results = []
    while len(queue) > 0:
        a = queue.pop()
        i = a.index('X')
        # generate two
        a1 = "".join((a[:i], '0', a[i+1:]))
        a2 = "".join((a[:i], '1', a[i+1:]))
        if 'X' not in a1:
            results.append(a1)
            results.append(a2)
        else:
            queue.append(a1)
            queue.append(a2)
    return results

#print('\n'.join(all_addr('000000000000000000000000000000X1101X')))

def execute(instructions):
    memory = {}
    msk = 'X' * 36

    for opcode, params in instructions:
        if opcode == 'setmask':
            msk = params
        else:
            addr, value = params
            binaddr = '{0:0>36b}'.format(addr)
            binaddr = bitmask(binaddr, msk)
            for addr in all_addr(binaddr):
                memory[addr] = value

    return memory

memory = execute(instructions)

sum = 0
for k, v in memory.items():
    print('%s: %s' % (k, v))
    sum += v
print(sum)


