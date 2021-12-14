closings = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

def is_opening(c):
    return c in closings.keys()

def validate(line):
    stack = []
    for c in line:
        if is_opening(c):
            stack.append(c)
        else:
            if c != closings[stack.pop()]:
                return c
    return None

lines = []
with open('input') as f:
    lines = [l.strip() for l in f.read().split('\n')]

print(lines)

scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

total = 0
for l in lines:
    c = validate(l)
    if c is not None:
        total += scores[c]
        print('%s => %d' % (l, scores[c]))

print(total)
