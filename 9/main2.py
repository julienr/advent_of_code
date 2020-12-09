PREAMBLE = 25
message = [int(s) for s in open('input').read().split('\n') if s != '']
#print(message)

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

invalid_index = i
invalid_number = message[invalid_index]
print(invalid_number)

# Find contiguous range summing
def find_contiguous_range(message, invalid_number):
    for i in range(len(message)):
        acc = message[i]
        for j in range(i + 1, len(message)):
            acc += message[j]
            if acc == invalid_number:
                return i, j

i, j = find_contiguous_range(message, invalid_number)
print(i, j)
# Find smallest and largest numbers in contiguous range
smallest = min(message[i:j])
largest = max(message[i:j])
print(smallest + largest)
