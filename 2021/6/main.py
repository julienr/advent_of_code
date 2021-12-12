import numpy as np
import sys

with open('input') as f:
    ages = [int(v) for v in f.read().split(',')]

def tick(ages):
    n = len(ages)
    for i in range(n):
        ages[i] -= 1
        if ages[i] < 0:
            ages[i] = 6
            ages.append(8)

for day in range(80 + 1):
    #print('After %d days (%d fishes): %s' % (day, len(ages), str(ages)))
    print('After %d days (%d fishes)' % (day, len(ages)))
    tick(ages)
