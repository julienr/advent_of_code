import sys
lines = open('input').read().split('\n')
lines = list(filter(lambda l: len(l) > 0, lines))


NUMBER = 'number'
ADD = 'add'
MUL = 'mul'
LEFT_PAR = 'lpar'
RIGHT_PAR = 'rpar'


def read_number(line, i):
    acc = ''
    for j in range(i, len(line)):
        if str(line[j]).isdigit():
            acc += line[j]
        else:
            break
    # EOF handling
    if j == i:
        j += 1
    return j, (NUMBER, int(acc))


def tokenize(line):
    tokens = []
    acc = ''
    i = 0
    while i < len(line):
        c = line[i]
        if str(c).isdigit():
            i, token = read_number(line, i)
            tokens.append(token)
        elif c == ' ':
            i += 1
        elif c == '+':
            i += 1
            tokens.append((ADD,))
        elif c == '*':
            i += 1
            tokens.append((MUL,))
        elif c == '(':
            i += 1
            tokens.append((LEFT_PAR,))
        elif c == ')':
            i += 1
            tokens.append((RIGHT_PAR,))
    return tokens

precedence = {
    ADD: 2,
    MUL: 1,
}

# https://en.wikipedia.org/wiki/Shunting-yard_algorithm
def evaluate(tokens):
    output_queue = []
    op_stack = []
    while len(tokens) > 0:
        tok = tokens.pop(0)
        if tok[0] == NUMBER:
            output_queue.append(tok[1])
        elif tok[0] == MUL or tok[0] == ADD:
            while len(op_stack) > 0 \
                and op_stack[0] != LEFT_PAR \
                and (precedence[op_stack[0]] >= precedence[tok[0]]):
                output_queue.append(op_stack.pop(0))
            op_stack.insert(0, tok[0])
        elif tok[0] == LEFT_PAR:
            op_stack.insert(0, tok[0])
        elif tok[0] == RIGHT_PAR:
            while op_stack[0] != LEFT_PAR:
                output_queue.append(op_stack.pop(0))
            if len(op_stack) > 0 and op_stack[0] == LEFT_PAR:
                op_stack.pop(0)
    while len(op_stack) > 0:
        output_queue.append(op_stack.pop(0))
    return output_queue

def eval_rpn(tokens):
    stack = []
    for t in tokens:
        #print(stack)
        if type(t) == int:
            stack.insert(0, t)
        else:
            rhs = stack.pop(0)
            lhs = stack.pop(0)
            if t == MUL:
                stack.insert(0, rhs * lhs)
            elif t == ADD:
                stack.insert(0, rhs + lhs)
            else:
                raise RuntimeError(t)

    return stack.pop(0)

#lines = lines[2:3]
#for line in lines:
    #print ('\n---')
    #print(line)
    #print(tokenize(line))
    #rpn = evaluate(tokenize(line))
    #print(rpn)
    #print(eval_rpn(rpn))

acc = 0
for line in lines:
    rpn = evaluate(tokenize(line))
    acc += eval_rpn(rpn)
print(acc)
