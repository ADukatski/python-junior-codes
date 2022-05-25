from math import ceil

budget = float(input())

total = 0
counter = 0

while True:
    product_name = input()
    if product_name == "Stop":
        print(f"You bought {counter} products for {total:.2f} leva.")
        break
    else:
        product_price = float(input())

    if (counter + 1) % 3 == 0:
        product_price -= product_price * 0.50

    if product_price + total > budget:
        diff = product_price + total - budget
        print(f"You don't have enough money!")
        print(f"You need {diff:.2f} leva!")
        break

    counter += 1
    total += product_price