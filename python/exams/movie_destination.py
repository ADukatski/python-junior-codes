budget = float(input())
destination = input()
season = input()
days = int(input())

price = 0

if season == "Winter":
    if destination == "Dubai":
        price += 45000
        price -= price * 0.30
    elif destination == "Sofia":
        price += 17000
        price += price * 0.25
    elif destination == "London":
        price += 24000

elif season == "Summer":
    if destination == "Dubai":
        price += 40000
        price -= price * 0.30
    elif destination == "Sofia":
        price += 12500
        price += price * 0.25
    elif destination == "London":
        price += 20250

total = price * days
diff = abs(total - budget)
if budget >= total:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")