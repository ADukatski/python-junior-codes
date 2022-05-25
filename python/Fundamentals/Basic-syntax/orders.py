orders = int(input())
total = 0
for i in range(orders):
    price_capsule = float(input())
    days = int(input())
    capsule_per_day = int(input())

    if price_capsule < 0.01 or price_capsule > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsule_per_day < 1 or capsule_per_day > 2000:
        continue
    coffee = price_capsule * days * capsule_per_day
    total += coffee
    print(f"The price for the coffee is: ${coffee:.2f}")
print(f"Total: ${total:.2f}")


