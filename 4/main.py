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

def is_valid(passport):
    req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    return all([f in passport for f in req_fields])


#print('\n'.join(['%s' % p for p in passports]))

valid_passports = list(filter(is_valid, passports))
print(len(valid_passports))
