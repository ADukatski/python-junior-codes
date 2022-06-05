quantity_of_food_kg = float(input())
food = quantity_of_food_kg * 1000
quantity_hay_kg = float(input())
hay = quantity_hay_kg * 1000
quantity_cover_kg = float(input())
cover = quantity_cover_kg * 1000
pig_weight = float(input())
weight = pig_weight * 1000

for d in range(1, 30 + 1):

    if d % 2 == 0:
        food -= 300
        hay -= food * 0.05
    else:
        food -= 300

    if d % 3 == 0:
        cover -= weight / 3

    if food < 0 or cover < 0 or hay < 0:
        break

if food > 0 and cover > 0 and hay > 0:
    print(f"Everything is fine! Puppy is happy! Food: {(food)/1000:.2f}, Hay: "
            f"{(hay)/1000:.2f}, Cover: {(cover)/1000:.2f}.")
else:
    print(f"Merry must go to the pet store!")