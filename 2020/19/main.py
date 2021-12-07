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

print(rules)
print(messages)

def match(rule, rules, message):
    #print('match', rule, message)
    if '|' in rule:
        lhs, rhs = rule.split('|')
        m, i = match(lhs, rules, message)
        if m:
            return True, i
        m, i = match(rhs, rules, message)
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
                return False, i
        return True, i

n_matches = 0
for m in messages:
    res, i = match(rules[0], rules, m)
    # must match whole message
    res = i == len(m)
    print(m, res)
    if res:
        n_matches += 1
print(n_matches)

