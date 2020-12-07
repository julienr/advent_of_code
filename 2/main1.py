import sys

with open('input') as f:
    lines = [line.strip() for line in f]

def parse(line):
    rule, password = line.split(':')
    password = password.strip()
    counts, letter = rule.split(' ')
    min_count, max_count = counts.split('-')
    return (int(min_count), int(max_count), letter, password)

lines = map(parse, lines)

def validate(line):
    min_count, max_count, letter, password = line
    count = 0
    for c in password:
        if c == letter:
            count += 1
    valid = min_count <= count <= max_count
    #print(password, letter, count, min_count, max_count, valid)
    return valid

valids = map(validate, lines)
print(sum(valids))
