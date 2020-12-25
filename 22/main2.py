import copy

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


def history_key(decks):
    return '1: %s, 2: %s' % (
        ','.join(['%d'%d for d in decks[0]]),
        ','.join(['%d'%d for d in decks[1]])
    )

def game(decks, game_id=1):
    history = set([])
    decks = copy.deepcopy(decks)
    i = 0
    while True:
        i += 1
        print('-- Round %d (Game %d)--' % (i, game_id))

        print('Player 1 deck: %s' % decks[0])
        print('Player 2 deck: %s' % decks[1])

        # -- Win by history
        if history_key(decks) in history:
            print('Player 1 win by history')
            return 0
        history.add(history_key(decks))

        # -- Recurse ?
        c1 = decks[0].pop(0)
        c2 = decks[1].pop(0)
        print('Player 1 plays: %d' % c1)
        print('Player 2 plays: %d' % c2)

        if c1 <= len(decks[0]) and c2 <= len(decks[1]):
            print('Playing a sub-game...')
            new_decks = []
            new_decks.append(decks[0][:c1])
            new_decks.append(decks[1][:c2])
            winner = game(new_decks, game_id=game_id + 1)
        else:
            if c1 > c2:
                winner = 0
            else:
                winner = 1

        if winner == 0:
            print('Player 1 wins the round')
            decks[0].append(c1)
            decks[0].append(c2)
        else:
            print('Player 2 wins the round')
            decks[1].append(c2)
            decks[1].append(c1)
        print('\n')

        if len(decks[0]) == 0:
            print('Player 2 wins, score=%d' % score(decks[1]))
            return 1
        elif len(decks[1]) == 0:
            print('Player 1 wins, score=%d' % score(decks[0]))
            return 0

print(game(decks))
