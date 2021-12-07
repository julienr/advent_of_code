from collections import defaultdict

lines = open('input').read().split('\n')
lines = [l.strip() for l in lines]
lines = [l for l in lines if len(l) > 0]

def clean_name(bag_name):
    if bag_name.endswith('s'):
        return bag_name[:-1]
    return bag_name

def parse_contained(contained):
    first_space = contained.find(' ')
    count = int(contained[:first_space])
    bag_name = contained[first_space:].strip()
    bag_name = clean_name(bag_name)
    return count, bag_name

def parse_rule(l):
    name, rest = l.split(' contain ')
    name = clean_name(name.strip())
    rest = rest.strip('.')
    contained = rest.split(',')
    if rest == 'no other bags':
        contained = []
    else:
        contained = [c.strip() for c in contained]
        contained = list(map(parse_contained, contained))
        #print(name, ':', ' | '.join([str(c) for c in contained]))
    return name, contained

# 'container' => 'content'
rules = list(map(parse_rule, lines))
rules = dict(rules)
print(rules)

# Build reverse tree from 'bag_name' => 'can be contained in'
reverse_rules = defaultdict(lambda: [])
for container, containees in rules.items():
    for (containee_count, containee_name) in containees:
        reverse_rules[containee_name].append(container)
print(reverse_rules)

my_bag = 'shiny gold bag'

can_contain = set()
to_visit = [my_bag]
while len(to_visit) > 0:
    bag_name = to_visit.pop()
    containers = reverse_rules[bag_name]
    for c in containers:
        can_contain.add(c)
        to_visit.append(c)

print(can_contain)
print(len(can_contain))
