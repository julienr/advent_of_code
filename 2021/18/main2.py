import sys
import math
from itertools import combinations

def explode(number, pair_start):
    """pair_start is the index of the ["""
    pair_end = number.find(']', pair_start)
    assert number[pair_start] == '['
    pair = number[pair_start:(pair_end+1)]
    #print('pair: ', pair)
    left, right = (int(v) for v in pair[1:-1].split(','))
    # Add left to first regular value on the left
    new_left = number[:pair_start]
    for i in range(pair_start, 0, -1):
        if number[i].isdigit():
            i_end = i
            i -= 1
            while number[i].isdigit():
                i -= 1
            i_start = i
            i_start += 1
            i_end += 1
            #print('to_replace', number[i_start:i_end])
            v = int(number[i_start:i_end])
            v += left
            #print(i_start, i_end)
            new_left = number[:i_start] + str(v) + number[i_end:pair_start]
            break


    # Add right to first regular value on the right
    new_right = number[pair_end+1:]
    for i in range(pair_end, len(number)):
        if number[i].isdigit():
            i_start = i
            i += 1
            while number[i].isdigit():
                i += 1
            i_end = i
            v = int(number[i_start:i_end])
            v += right
            #print(i_start, i_end)
            new_right = number[pair_end+1:i_start] + str(v) + number[i_end:]
            break
    #print('new_left:', new_left, 'new_right :', new_right)
    number = new_left + '0' + new_right
    #number = number[:pair_start] + '0' + number[pair_end+1:]
    return number


def split(number, split_start):
    i_start = split_start
    i = i_start
    while number[i].isdigit():
        i += 1
    i_end = i
    v = int(number[i_start:i_end])
    number = number[:i_start] + '[' + str(v // 2) + ',' + str(int(math.ceil(v / 2))) + ']' + number[i_end:]
    return number


def find_nested(number):
    count = 0
    for i in range(len(number)):
        if number[i] == '[':
            count += 1
            if count == 5:
                return i
        if number[i] == ']':
            count -= 1
    return None

def find_too_large(number):
    i = 0
    while True:
        if number[i].isdigit():
            i_start = i
            i += 1
            while number[i].isdigit():
                i += 1
            v = int(number[i_start:i])
            if v >= 10:
                return i_start
        else:
            i += 1
        if i >= len(number):
            return None

def reduce_number(number):
    while True:
        i = find_nested(number)
        if i is not None:
            number = explode(number, i)
            continue
        i = find_too_large(number)
        if i is not None:
            number =split(number, i)
            continue
        break
    return number

#print(find_too_large('[[2,[2,[1,[10,3]]]],[6,[5,[4,[3,2]]]]]'))

#sys.exit(-1)

def add(number1, number2):
    number = '[' + number1 + ',' + number2 + ']'
    return reduce_number(number)


def magnitude(number):
    if number[0] == '[':
        count = 1
        for i in range(1, len(number)):
            if number[i] == '[':
                count += 1
            if number[i] == ']':
                count -= 1
            if number[i] == ',' and count == 1:
                midpoint = i
            if count == 0:
                i_end = i
                break
        else:
            assert False

        left = magnitude(number[1:midpoint])
        right = magnitude(number[midpoint+1:])
        return 3 * left + 2 * right
    else:
        i = 1
        while i < (len(number) - 1) and number[i].isdigit():
            i += 1
        return int(number[:i])


#print(magnitude('[9,1]'))
#print(magnitude('[[1,2],[[3,4],5]]'))
#print(magnitude('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'))
#print(magnitude('[[[[1,1],[2,2]],[3,3]],[4,4]]'))
#print(magnitude('[[[[3,0],[5,3]],[4,4]],[5,5]]'))
#print(magnitude('[[[[5,0],[7,4]],[5,5]],[6,6]]'))
#print(magnitude('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]'))
#print(magnitude('[[[[7,0],[7,8]],[[7,9],[0,6]]],[[6,[6,6]],[[7,0],[8,9]]]]'))
#sys.exit(-1)


#print(split('[[[[[11,8],1],2],3],4]', 5))

#numbers = [
    #('[[[[[9,8],1],2],3],4]', 4),
    #('[7,[6,[5,[4,[3,2]]]]]', 12),
    #('[[6,[5,[4,[3,2]]]],1]', 10),
    #('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]', 10),
    #('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]', 24),
#]

#for n, explode_at in numbers:
    #print('%s -> %s' % (n, explode(n, explode_at)))

#print(add('[[[[4,3],4],4],[7,[[8,4],9]]]', '[1,1]'))
#print(add('[[[1,1],[2,2]],[3,3]]', '[4,4]'))

max_magnitude = 0
with open('input') as f:
    numbers = [l.strip() for l in f.read().split('\n') if l.strip() != '']
    for number1, number2 in combinations(numbers, 2):
        for n1, n2 in [(number1, number2), (number2, number1)]:
            total = add(n1, n2)
            m = magnitude(total)
            if m > max_magnitude:
                max_magnitude = m
print(max_magnitude)
