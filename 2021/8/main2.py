import numpy as np
import sys
from collections import defaultdict
import itertools

lines = []
with open('input') as f:
    for line in f:
        if len(line.strip()) == 0:
            continue
        left, right = line.split('|')
        lines.append((
            [v.strip() for v in left.strip().split(' ')],
            [v.strip() for v in right.strip().split(' ')]
        ))


def count_letter_occurences(words):
    counts = defaultdict(lambda: 0)
    for w in words:
        for c in list(w):
            counts[c] += 1
    return dict(counts)


digits = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg'
}
digits = {k:''.join(sorted(v)) for k, v in digits.items()}


def find_mapping(words_by_len):
    letter_counts = count_letter_occurences(itertools.chain(*[list(ws) for ws in words_by_len.values()]))
    #print(letter_counts)

    #  aaaa
    # b    c
    # b    c
    #  dddd
    # e    f
    # e    f
    #  gggg

    mapping = {}
    # from 7 and 1, find a
    diff = list(
        set(list(words_by_len[3])[0]).difference(list(words_by_len[2])[0])
    )
    assert len(diff) == 1
    diff = diff[0]
    mapping['a'] = diff
    # from letters_count, following are uniques:
    # b appears in 6 digits
    # e appears in 4 digits
    # f appears in 9 digits
    for l, c in letter_counts.items():
        if c == 6:
            mapping['b'] = l
        elif c == 4:
            mapping['e'] = l
        elif c == 9:
            mapping['f'] = l

    # we know the mapping for f, so from 1 we know c
    mapping['c'] = list(set(list(words_by_len[2])[0]).difference([mapping['f']]))[0]

    # we know b, c and f so from 4 we know d
    mapping['d'] = list(set(list(words_by_len[4])[0]).difference([mapping['f'], mapping['b'], mapping['c']]))[0]

    # => only g left
    mapping['g'] = list(set(['a', 'b', 'c', 'd', 'e', 'f', 'g']).difference(mapping.values()))[0]

    #print(mapping)

    # now, from 4 we already know
    # now, we can find d and g using the 6 segments digits:
    # 0, 6, 9
    # because g appears in all 3, whereas d appears in only 2
    #print('\n'.join(['%s = %s' % (k, v) for k, v in mapping.items()]))

    # Build decoding table for each word
    decoding = {
        ''.join(sorted([mapping[v] for v in w])): k for k, w in digits.items()
    }
    #print(decoding)
    return decoding


def decode(words, decoding):
    out = ''
    for word in words:
        d = decoding[''.join(sorted(word))]
        out += str(d)
    return int(out)


# Turns ou we always have one instance of 2, 3, 4 and 7 in each line
# 1 uses 2
# 4 uses 4
# 7 uses 3
# 8 uses 7
# And actually we always have all possibilities (6)
unique = set([2, 4, 3, 7])
total = 0
for left, right in lines:
    words = left + right
    lens = [len(w) for w in words]
    appearing_uniques = set(lens).intersection(unique)
    assert len(appearing_uniques) == 4
    assert len(set(lens)) == 6

    # sort words because order doesn't matter
    words = [''.join(sorted(w)) for w in words]

    words_by_len = defaultdict(lambda : set([]))
    for w in words:
        words_by_len[len(w)].add(w)

    # We always have an instance of each combination
    assert sum(len(w) for w in words_by_len.values()) == 10
    #print(words_by_len)

    decoding = find_mapping(words_by_len)
    v = decode(right, decoding)
    print(v)
    total += v

print(total)

