import re

lines = open('input').read().split('\n')

rules = []
for i in range(len(lines)):
    line = lines[i].strip()
    if 'your ticket' in line:
        break
    if line == '':
        continue
    rules.append(line)

my_ticket = lines[i+1]
nearby_tickets = []

assert 'nearby tickets' in lines[i+3]
for i in range(i+4, len(lines)):
    line = lines[i].strip()
    if line == '':
        continue
    nearby_tickets.append(line)

prog = re.compile(r'(?P<field_name>[\w\s]+):\s+(?P<min1>\d+)-(?P<max1>\d+)\s+or\s+(?P<min2>\d+)-(?P<max2>\d+)')

def parse_rule(rule_str):
    g = prog.match(rule_str)
    field_name = g.group('field_name')
    min1 = int(g.group('min1'))
    max1 = int(g.group('max1'))
    min2 = int(g.group('min2'))
    max2 = int(g.group('max2'))

    return field_name, (min1, max1), (min2, max2)

rules = map(parse_rule, rules)

print(rules)
print(my_ticket)
print(nearby_tickets)


def validate_ticket(ticket, rules):
    ticket = [int(v) for v in ticket.split(',')]
    for v in ticket:
        valid_any = False
        for r in rules:
            if r[1][0] <= v <= r[1][1] or r[2][0] <= v <= r[2][1]:
                valid_any = True
                break
        if not valid_any:
            return v
    return None

scanning_error_rate = 0
for nearby in nearby_tickets:
    v = validate_ticket(nearby, rules)
    if v is not None:
        scanning_error_rate += v
print(scanning_error_rate)
