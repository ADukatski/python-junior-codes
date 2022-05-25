price_strawberry = float(input())
number_bananas_kg = float(input())
number_oranges_kg = float(input())
number_raspberry_kg = float(input())
number_strawberry_kg = float(input())

sum_strawberry = price_strawberry * number_strawberry_kg
raspberry = price_strawberry / 2
oranges = raspberry - (raspberry * 0.40)
bananas = raspberry - (raspberry * .80)
sum_raspberry = raspberry * number_raspberry_kg
sum_bananas = bananas * number_bananas_kg
sum_oranges = oranges * number_oranges_kg
total = sum_oranges + sum_raspberry + sum_bananas + sum_strawberry

print(f"{total:.2f}")