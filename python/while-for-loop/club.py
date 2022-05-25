wanted_gains = float(input())

gains = 0

while True:
    cocktail = input()
    if cocktail == "Party!":
        diff = abs(gains - wanted_gains)
        print(f"We need {diff} leva more.")
        print(f"Club income - {gains} leva.")
        break

    number_of_cocktails = int(input())

    price = len(cocktail)
    price *= number_of_cocktails

    if price % 2 != 0:
        price -= price * 0.25
    else:
        pass

    gains += price

    if gains >= wanted_gains:
        print(f"Target acquired.")
        print(f"Club income - {gains} leva.")
        break
