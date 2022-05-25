budget = float(input())
nights = int(input())
price_night = float(input())
percent_costs = int(input())


if nights > 7:
    price_night -= price_night * 0.05
else:
    pass
price_for_nights = price_night * nights
percent = (budget * percent_costs) / 100
total = price_for_nights + percent
diff = abs(budget - total)
if budget >= total:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")
