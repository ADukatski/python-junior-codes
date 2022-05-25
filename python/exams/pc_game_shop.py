sold_games = int(input())

hs = 0
fort = 0
ovoerw = 0
others = 0

for n in range(sold_games):
    game = input()

    if game == "Hearthstone":
        hs += 1
    elif game == "Fornite":
        fort += 1
    elif game == "Overwatch":
        ovoerw += 1
    elif game != "Hearthstone" and game != "Fornite" and game != "Overwatch":
        others += 1

total = hs + fort + ovoerw + others

print(f"Hearthstone - {(hs / total) * 100:.2f}%")
print(f"Fornite - {(fort / total)* 100:.2f}%")
print(f"Overwatch - {(ovoerw / total)* 100:.2f}%")
print(f"Others - {(others / total)* 100:.2f}%")