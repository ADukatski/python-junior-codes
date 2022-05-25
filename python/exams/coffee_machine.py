type = input()
sugar = input()
number = int(input())

price = 0
total = 0


if type == "Espresso":
    if sugar == "Without":
        price = number * 0.90
        price -= price * 0.35
    elif sugar == "Normal":
        price = number * 1
    elif sugar == "Extra":
        price = number * 1.20
    if number >= 5:
        price -= price * 0.25

elif type == "Cappuccino":
    if sugar == "Without":
        price = number * 1
        price -= price * 0.35
    elif sugar == "Normal":
        price = number * 1.20
    elif sugar == "Extra":
        price = number * 1.60

elif type == "Tea":
    if sugar == "Without":
        price = number * 0.50
        price -= price * 0.35
    elif sugar == "Normal":
        price = number * 0.60
    elif sugar == "Extra":
        price = number * 0.70

if price > 15:
    price -= price * 0.20
else:
    pass

print(f"You bought {number} cups of {type} for {price:.2f} lv.")
