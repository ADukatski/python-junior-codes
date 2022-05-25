decoration_quantity = int(input())
days_to_christmas = int(input())

price = 0
points = 0

for i in range(1, days_to_christmas + 1):

    if i % 11 == 0:
        decoration_quantity += 2

    if i % 2 == 0:
        price += 2 * decoration_quantity
        points += 5

    if i % 3 == 0:
        price += (5 + 3) * decoration_quantity
        points += (3 + 10)

    if i % 5 == 0:
        price += 15 * decoration_quantity
        points += 17

    if i % 10 == 0:
        points -= 20
        price += 5 + 3 + 15
        if i == days_to_christmas:
            points -= 30

    if i % 15 == 0:
        points += 30


print(f"Total cost: {price}")
print(f"Total spirit: {points}")