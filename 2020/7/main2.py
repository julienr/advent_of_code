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

my_bag = 'shiny gold bag'

def visit(bag):
    total = 0
    for (count, bag_name) in rules[bag]:
        total += count + count * visit(bag_name)
    return total

print(visit(my_bag))
