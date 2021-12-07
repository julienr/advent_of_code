PREAMBLE = 25
message = [int(s) for s in open('input').read().split('\n') if s != '']
print(message)

def validate(message, i):
    candidates = message[i-PREAMBLE:i]
    for c1 in candidates:
        for c2 in candidates:
            if c1 + c2 == message[i]:
                return True
    return False

for i in range(PREAMBLE, len(message)):
    if not validate(message, i):
        print(i, message[i])
        break
