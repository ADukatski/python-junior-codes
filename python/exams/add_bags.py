price_luggage_over_20_kg = float(input())
kg_luggage = float(input())
days_until_travel = int(input())
number_of_luggage = int(input())
price_luggage = 0
tax = 0


if kg_luggage <= 10:
    tax = price_luggage_over_20_kg * 0.20
elif 10 < kg_luggage <= 20:
    tax = price_luggage_over_20_kg * 0.50
elif 20 < kg_luggage:
    tax = price_luggage_over_20_kg

if days_until_travel > 30:
    tax += tax * 0.10
elif 7 < days_until_travel <= 30:
    tax += tax * 0.15
elif days_until_travel < 7:
    tax += tax * 0.40

total = tax * number_of_luggage
print(f"The total price of bags is: {total:.2f} lv")