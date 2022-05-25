budget = float(input())
staff = int(input())
cloth_staff = float(input())

price_cloth_staff = staff * cloth_staff
decor = budget * 0.10

if staff > 150:
    price_cloth_staff -= price_cloth_staff * 0.10
else:
    pass

total = decor + price_cloth_staff
diff = abs(total - budget)
if total <= budget:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")