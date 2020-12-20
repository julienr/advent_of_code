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


def parse_expr(tokens):
    if tokens[0][0] == NUMBER:
        return tokens[0], 1
    elif tokens[0][0] == LEFT_PAR:
        # Find matching rpar
        nopens = 1
        for j in range(1, len(tokens)):
            if tokens[j] == LEFT_PAR:
                nopens += 1
            elif tokens[j] == RIGHT_PAR:
                nopens -= 1
            if nopens == 0:
                break
        return parse_expr(tokens[:j]), j
    else:
        raise RuntimeError('Unexpected expression beginning with %s' % str(tokens[0]))


def evaluate(tokens):
    #print('evaluate ', tokens)
    assert len(tokens) != 0
    if len(tokens) == 1:
        assert tokens[0][0] == NUMBER
        return tokens[0][1]

    rhs_tokens = []
    nopens = 0
    for i in range(len(tokens) - 1, 0, -1):
        if tokens[i][0] == RIGHT_PAR:
            if nopens > 0:
                # inner parenthesis, keep
                rhs_tokens.insert(0, tokens[i])
            nopens += 1
        elif tokens[i][0] == LEFT_PAR:
            nopens -= 1
            if nopens > 0:
                # inner parenthesis, keep
                rhs_tokens.insert(0, tokens[i])
        else:
            rhs_tokens.insert(0, tokens[i])
        if nopens == 0:
            break
    rhs = evaluate(rhs_tokens)
    #print('rhs_tokens', rhs_tokens)

    op = tokens[i-1]
    # This will happen if expression start with (
    if op[0] == LEFT_PAR:
        return rhs
    lhs = evaluate(tokens[:i-1])

    if op[0] == ADD:
        return rhs + lhs
    elif op[0] == MUL:
        return rhs * lhs

#lines = lines[-1:]
#for line in lines:
    #print ('\n---')
    #print(line)
    #print(tokenize(line))
    #print('=', evaluate(tokenize(line)))

acc = 0
for line in lines:
    acc += evaluate(tokenize(line))
print(acc)
