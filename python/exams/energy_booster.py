fruit = input()
size_of_set = input()
numb_of_sets = int(input())

price = 0
with_set = 0

if size_of_set == "small":
    if fruit == "Watermelon":
        price = 2 * 56
        with_set = price * numb_of_sets
    elif fruit == "Mango":
        price = 2 * 36.66
        with_set = price * numb_of_sets
    elif fruit == "Pineapple":
        price = 2 * 42.10
        with_set = price * numb_of_sets
    elif fruit == "Raspberry":
        price = 2 * 20
        with_set = price * numb_of_sets

elif size_of_set == "big":
    if fruit == "Watermelon":
        price = 5 * 28.70
        with_set = price * numb_of_sets
    elif fruit == "Mango":
        price = 5 * 19.60
        with_set = price * numb_of_sets
    elif fruit == "Pineapple":
        price = 5 * 24.80
        with_set = price * numb_of_sets
    elif fruit == "Raspberry":
        price = 5 * 15.20
        with_set = price * numb_of_sets

if 400 <= with_set <= 1000:
    with_set -= with_set * 0.15
elif with_set > 1000:
    with_set -= with_set * 0.50

print(f"{with_set:.2f} lv.")