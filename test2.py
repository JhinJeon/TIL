t = int(input())

for k in range(1, t+1):
    answer = 0
    deck = input()
    cards = []
    for d in deck:
        cards.append(int(d))
    for a in range(len(cards)):
        for b in range(a+1, len(cards)):
            if cards[a] == cards[b] or abs(cards[a] - cards[b]) == 1:
                for c in range(b+1, len(cards)):
                    if (cards[c] + cards[b] + cards[a]) / 3 in [cards[a], cards[b], cards[c]]:
                        answer += 1
    if answer == 2:
        result = 1
    else:
        result = 0

    print(f'#{k} {result}')
