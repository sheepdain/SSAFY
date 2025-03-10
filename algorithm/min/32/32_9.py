from collections import Counter

cards = list(input())
n = int(input())
cards.sort()
card = cards[-n:]
Count = Counter(card)
card.sort(key=lambda x: -Count[x])
print(card[0])
