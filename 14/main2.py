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
        if c == 'X':
            continue
        else:
            outval[i] = c
    return "".join(outval)


def execute(mask, instructions):
    memory = {}
    msk = 'X' * 36

    for opcode, params in instructions:
        if opcode == 'setmask':
            msk = params
        else:
            addr, value = params
            binval = '{0:0>36b}'.format(value)
            memory[addr] = bitmask(binval, msk)

    return memory


memory = execute(msk, instructions)

sum = 0
for k, v in memory.items():
    iv = int(v, 2)
    print('%s: %s' % (k, iv))
    sum += iv
print(sum)


