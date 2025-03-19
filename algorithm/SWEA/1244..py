T = int(input())

for tc in range(T):
    cards, turns = input().split()
    cards = list(map(int, cards))
    N = len(cards)
    st = N - 1
    turns = int(turns)
    sorted_cards = sorted(cards, reverse=True)

    left = turns - N
    cnt = 0
    n = 0

    for n in range(N):
        card_value = sorted_cards[n]
        for j in range(st, -1, -1):
            if cards[j] == card_value:
                if j == n:
                    continue
                if j - 1 > -1 and cards[j - 1] == cards[j] and n + 1 < N and cards[n] > cards[n + 1]:
                    cards[n], cards[j - 1] = cards[j - 1], cards[n]
                else:
                    cards[n], cards[j] = cards[j], cards[n]
                cnt += 1
                break
        if cnt == turns:
            break

    if (turns - cnt) % 2 == 1:
        cards[-1], cards[-2] = cards[-2], cards[-1]

    ans = ''.join(map(str, cards))

    print(f'#{tc + 1} {ans}')