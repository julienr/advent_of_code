import re
import numpy as np

lines = open('input').read().split('\n')

rules = []
for i in range(len(lines)):
    line = lines[i].strip()
    if 'your ticket' in line:
        break
    if line == '':
        continue
    rules.append(line)

my_ticket = lines[i+1].split(',')
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

rules = list(map(parse_rule, rules))

print('len rules :', len(rules))
print('len ticket :', len(my_ticket))
#print(my_ticket)
#print(nearby_tickets)


def validate_ticket(ticket, rules):
    ticket = [int(v) for v in ticket.split(',')]
    for v in ticket:
        valid_any = False
        for r in rules:
            if r[1][0] <= v <= r[1][1] or r[2][0] <= v <= r[2][1]:
                valid_any = True
                break
        if not valid_any:
            return False
    return True

valid_nearby = list(filter(lambda t: validate_ticket(t, rules), nearby_tickets))
print('valid nearby: ', len(valid_nearby))

tickets = [[int(v) for v in ticket.split(',')] for ticket in valid_nearby]
tickets = np.array(tickets)
print('tickets shape', tickets.shape)

def validate_column(arr, rule):
    return np.all(np.logical_or(
        np.logical_and(rule[1][0] <= arr, arr <= rule[1][1]),
        np.logical_and(rule[2][0] <= arr, arr <= rule[2][1])
    ))

# result (i, j) indicate if rule i is valid on field j
result = np.zeros((len(rules), tickets.shape[1]), dtype=np.bool)
for i, r in enumerate(rules):
    for j in range(tickets.shape[1]):
        result[i, j] = validate_column(tickets[:, j], r)

print(result)
print(result.shape)

for j in range(result.shape[1]):
    print(np.count_nonzero(result[:, j]))

N = len(my_ticket)
labels = [''] * N
arr = result.copy()
for _ in range(N):
    #print('\n--')
    #print(arr)
    for j in range(arr.shape[1]):
        if np.count_nonzero(arr[:, j]) == 1:
            break
    i = np.flatnonzero(arr[:, j])[0]
    # Column j is rule i
    #print("found", i, j)
    labels[j] = rules[i][0]
    arr[i, :] = False

print(labels)

# multiply the ones starting by departure
tot = 1
for i, l in enumerate(labels):
    if l.startswith('departure'):
        print(my_ticket[i])
        tot *= int(my_ticket[i])
print(tot)

