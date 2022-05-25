budget = float(input())
fuel = float(input())
day = input()

fuel_price = fuel * 2.10
total = fuel_price + 100

if day == "Sunday":
    total -= total * 0.20
elif day == "Saturday":
    total -= total * 0.10

diff = abs(total - budget)
if budget >= total:
    print(f"Safari time! Money left: {diff:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {diff:.2f} lv.")