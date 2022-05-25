days = int(input())
total_food = float(input())

biscuit = 0
dog = 0
cat = 0

for n in range(1, days + 1):
    eaten_food_dog = int(input())
    eaten_food_cat = int(input())

    dog += eaten_food_dog
    cat += eaten_food_cat

    if n % 3 == 0:
        biscuit += (eaten_food_dog + eaten_food_cat) * 0.10

total = dog + cat
print(f"Total eaten biscuits: {round(biscuit)}gr.")
print(f"{(total / total_food) * 100:.2f}% of the food has been eaten.")
print(f"{(dog / total) * 100:.2f}% eaten from the dog.")
print(f"{(cat / total) * 100:.2f}% eaten from the cat.")