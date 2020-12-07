def interpret_binary(s, one, maxv):
    tot = 0
    for i, c in enumerate(s):
        if c in one:
            tot += 2**(maxv - i)
    return tot


def compute_row(s):
    assert len(s) == 7
    return interpret_binary(s, one=['B'], maxv=6)

def compute_column(s):
    assert len(s) == 3
    return interpret_binary(s, one=['R'], maxv=2)

def seat_id(s):
    return interpret_binary(s, one=['B', 'R'], maxv=9)

#print(compute_row('FBFBBFF'))
#print(compute_column('RLR'))
#print(seat_id('BFFFBBFRRR'))
#print(seat_id('FFFBBBFRRR'))
#print(seat_id('BBFFBBFRLL'))


seat_ids = []
with open('input') as f:
    for line in f:
        seat_ids.append(seat_id(line.strip()))
#print(max(seat_ids))

seat_ids = sorted(seat_ids)
print(len(seat_ids))


# Find non-consecutive seats
min_id = min(seat_ids)
for i, seat_id in enumerate(seat_ids):
    if seat_ids[i] != min_id + i:
        print(i, seat_id)
        break

# we are in the middle of this
print(seat_ids[i-1])
print(seat_ids[i])
