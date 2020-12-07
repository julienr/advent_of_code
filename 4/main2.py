import re

passports = []
with open('input') as f:
    acc = []
    for line in f:
        if len(line.strip()) == 0:
            passports.append(dict(acc))
            acc = []
        else:
            parts = line.split(' ')
            acc.extend([p.strip().split(':') for p in parts])
    passports.append(dict(acc))


def is_year(s):
    return re.match(r'^\d{4}$', s)

def year_in_range(s, minv, maxv):
    return is_year(s) and int(s) >= minv and int(s) <= maxv

def valid_height(s):
    m = re.search(r'(\d+)(cm|in)', s)
    if m is None:
        return False
    height, unit = int(m.group(1)), m.group(2)
    if unit == 'cm':
        return 150 <= height <= 193
    elif unit == 'in':
        return 59 <= height <= 76
    else:
        return False

def valid_hair_color(s):
    return re.match(r'#[0-9a-f]{6}', s)

def valid_eye_color(s):
    return s in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def valid_passport_id(s):
    return re.match(r'\d{9}', s)

def is_valid(passport):
    req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    if not all([f in passport for f in req_fields]):
        return False

    if not year_in_range(passport['byr'], 1920, 2002):
        return False

    if not year_in_range(passport['iyr'], 2010, 2020):
        return False

    if not year_in_range(passport['eyr'], 2020, 2030):
        return False

    if not valid_height(passport['hgt']):
        return False

    if not valid_hair_color(passport['hcl']):
        return False

    if not valid_eye_color(passport['ecl']):
        return False

    if not valid_passport_id(passport['pid']):
        return False

    return True


#print('\n'.join(['%s' % p for p in passports]))

valid_passports = list(filter(is_valid, passports))
print(len(valid_passports))
