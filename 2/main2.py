import sys

with open('input') as f:
    lines = [line.strip() for line in f]

def parse(line):
    rule, password = line.split(':')
    password = password.strip()
    counts, letter = rule.split(' ')
    pos1, pos2 = counts.split('-')
    return (int(pos1), int(pos2), letter, password)

lines = map(parse, lines)

def validate(line):
    pos1, pos2, letter, password = line
    valid = (password[pos1 - 1] == letter) != (password[pos2 - 1] == letter)
    #print(password, letter, pos1, pos2, valid)
    return valid

valids = map(validate, lines)
print(sum(valids))
