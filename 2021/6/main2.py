import numpy as np
import sys
import functools


with open('input') as f:
    ages = [int(v) for v in f.read().split(',')]

def tick(ages):
    n = len(ages)
    for i in range(n):
        ages[i] -= 1
        if ages[i] < 0:
            ages[i] = 6
            ages.append(8)


@functools.lru_cache(maxsize=128)
def num_children(initial_age, remaining_days):
    if remaining_days - initial_age < 0:
        return 0
    else:
        # The initial one after remaining_days - initial_age
        count = 0
        #title = 'initial_age=%d, remaining_days=%d' % (initial_age, remaining_days)
        #print('== %s' % title)
        for i in range(initial_age, remaining_days, 7):
            #print('%s i=%d' % (title, i))
            count += 1 + num_children(8, remaining_days - i - 1)
        return count

#ages = [3]
children = [num_children(v, 256) for v in ages]
#print('children: ', children)
print(len(ages) + sum(children))

