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
                return False
    return stack

lines = []
with open('input') as f:
    lines = [l.strip() for l in f.read().split('\n')]

print(lines)

scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

final_scores = []
for l in lines:
    stack = validate(l)
    if stack:
        completion = [closings[c] for c in stack[::-1]]
        print('%s => %s' % (l, ''.join(completion)))
        total = 0
        for c in completion:
            total = total * 5 + scores[c]
        final_scores.append(total)

print(final_scores)
print(sorted(final_scores)[len(final_scores)//2])
