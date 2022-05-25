inherited_money = float(input())
year = int(input())

age = 18

for i in range(1800, year + 1):

    if i % 2 == 0:
        inherited_money -= 12000
        age += 1
    else:
        inherited_money -= 12000 + (50 * age)
        age += 1

if inherited_money < 0:
    print(f"He will need {abs(inherited_money):.2f} dollars to survive.")
else:
    print(f"Yes! He will live a carefree life and will have {inherited_money:.2f} dollars left.")