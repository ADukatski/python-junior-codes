food_bought = int(input()) * 1000

total = 0

while True:
    eaten_per_meal = input()

    if eaten_per_meal == "Adopted":
        if total <= food_bought:
            left = abs(total - food_bought)
            print(f"Food is enough! Leftovers: {left} grams." )
        else:
            need = abs (total - food_bought)
            print(f"Food is not enough. You need {need} grams more." )
        break

    eaten_per_meal = int(eaten_per_meal)

    total += eaten_per_meal
