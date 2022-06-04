cards = input().split()
shuffle_counts = int(input())


for shuffle in range(shuffle_counts):
    full_deck = []

    middle = len(cards) // 2
    left_part = cards[0:middle]
    right_part = cards[middle::]

    for i in range(len(left_part)):
        full_deck.append(left_part[i])
        full_deck.append(right_part[i])

    cards = full_deck

print(cards)