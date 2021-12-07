decks = []
with open('input') as f:
    s = f.read().split('\n\n')
    assert s[0].startswith('Player 1')
    for i in range(2):
        deck = [int(l) for l in s[i].split('\n')[1:] if l != '']
        decks.append(deck)

print(decks)

def round(decks):
    print('Player 1 deck: %s' % decks[0])
    print('Player 2 deck: %s' % decks[1])
    c1 = decks[0].pop(0)
    c2 = decks[1].pop(0)
    print('Player 1 plays: %d' % c1)
    print('Player 2 plays: %d' % c2)
    if c1 > c2:
        print('Player 1 wins the round')
        decks[0].append(c1)
        decks[0].append(c2)
    else:
        print('Player 2 wins the round')
        decks[1].append(c2)
        decks[1].append(c1)


def score(deck):
    tot = 0
    for i in range(len(deck)):
        tot += deck[i] * (len(deck) - i)
    return tot

while True:
    print('-- Round %d --' % i)
    round(decks)
    print('\n')

    if len(decks[0]) == 0:
        print('Player 2 wins, score=%d' % score(decks[1]))
        break
    elif len(decks[1]) == 0:
        print('Player 1 wins, score=%d' % score(decks[0]))
        break

