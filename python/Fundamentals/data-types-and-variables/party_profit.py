from math import floor

companions = int(input())
days = int(input())

coins = 0

for d in range(1, days+1):

    if d % 10 == 0:
        companions -= 2

    if d % 15 == 0:
        companions += 5

    if d % 3 == 0:
        coins -= companions * 3

    if d % 5 == 0:
        coins += companions * 20
        if d % 3 == 0:
            coins -= companions * 2

    coins += 50
    coins -= companions * 2

coins_per_companion = floor(coins / companions)
print(f"{companions} companions received {coins_per_companion} coins each.")
