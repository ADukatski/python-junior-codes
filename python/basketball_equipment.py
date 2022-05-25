year_tax_for_training = int(input())

sneakers = year_tax_for_training - (year_tax_for_training * 0.40)
equip = sneakers - (sneakers * 0.20)
ball = equip / 4
accessories = ball / 5
total = year_tax_for_training + sneakers + equip + ball + accessories


print(f"{total:.2f}")