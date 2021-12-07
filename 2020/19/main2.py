import sys
from collections import OrderedDict
rules = OrderedDict()
messages = []
with open('input') as f:
    for line in f:
        if line.strip() == '':
            break
        rule_no, rule = line.strip().split(': ')
        rules[int(rule_no)] = rule
    for line in f:
        messages.append(line.strip())

print('%d rules' % len(rules))
print('%d messages' % len(messages))

def gen_8():
    tmp = []
    for i in range(1, 10):
        tmp.append(' '.join(['42'] * i))
    return ' | '.join(tmp)


def gen_11():
    tmp = []
    for i in range(1, 10):
        tmp.append(
            ' '.join(['42'] * i) + ' ' + ' '.join(['31'] * i)
        )
    return ' | '.join(tmp)

rules[8] = gen_8()
rules[11] = gen_11()
#print(rules[8])
#print(rules[11])

def match(rule, rules, message):
    if len(message) == 0:
        return False, 0
    #print('match', rule, message)
    if '|' in rule:
        options = rule.split('|')
        for r in options:
            m, i = match(r, rules, message)
            if m:
                return True, i
        return False, 0
    elif rule.startswith('"'):
        char = rule[1]
        if message[0] == char:
            return True, 1
        else:
            return False, 0
    else:
        subrules = [int(s) for s in rule.strip().split(' ')]
        i = 0
        for sr in subrules:
            r = rules[sr]
            m, mi = match(r, rules, message[i:])
            i += mi
            if not m:
                return False, 0
        return True, i

# Rules 8 and 11 are the top-level rules (0: 8 11)
def match_n8_n11(m, n8, n11):
    i = 0
    for n in range(n8):
        res, mi = match(rules[8], rules, m[i:])
        i += mi
        #print('8: i=%d, m[i:]=%s, res=%s' % (i, m[i:], res))
        if not res:
            return False
    for n in range(n11):
        res, mi = match(rules[11], rules, m[i:])
        i += mi
        #print('11: i=%d, m[i:]=%s, res=%s' % (i, m[i:], res))
        if not res or i > len(m):
            return False
    if i != len(m):
        return False
    return True


def is_valid(message):
    for n8 in range(1, 10):
        for n11 in range(1, 10):
            if match_n8_n11(message, n8, n11):
                return True
    return False

#messages = messages[:1]
n_matches = 0
for m in messages:
    if is_valid(m):
        n_matches += 1
print(n_matches)

# This gives 283, but the real answer is 282
# I had to compare with other's solutions, but not sure what's wrong in this
# one...
