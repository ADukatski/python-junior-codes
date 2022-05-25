contract = input()
contract_type = input()
internet = input()
months_to_pay = int(input())

tax = 0
sum = 0

if contract == "one":
    if contract_type == "Small":
        tax += 9.98
    elif contract_type == "Middle":
        tax += 18.99
    elif contract_type == "Large":
        tax += 25.98
    elif contract_type == "ExtraLarge":
        tax += 35.99

elif contract == "two":
    if contract_type == "Small":
        tax += 8.58
    elif contract_type == "Middle":
        tax += 17.09
    elif contract_type == "Large":
        tax += 23.59
    elif contract_type == "ExtraLarge":
        tax += 31.79

if internet == "yes":
    if tax <= 10:
        tax += 5.50
    elif tax <= 30:
        tax += 4.35
    elif tax > 30:
        tax += 3.85
else:
    pass

sum = tax * months_to_pay

if contract == "two":
    sum -= sum * 0.0375
else:
    pass

print(f"{sum:.2f} lv.")