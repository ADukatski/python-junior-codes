lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

shield_broke = 0
cost = 0

for lost in range(1, lost_fights + 1):

    if lost % 2 == 0:
        cost += helmet_price

    if lost % 3 == 0:
        cost += sword_price

    if lost % 2 == 0 and lost % 3 == 0:
        cost += shield_price
        shield_broke += 1
        if shield_broke % 2 == 0:
            cost += armor_price

print(f"Gladiator expenses: {cost:.2f} aureus")
