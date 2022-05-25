number_of_joinery = int(input())
type_of_joinery = input()
dev_or_no = input()

price = 0
total = 0
sum = 0

if type_of_joinery == "90X130":
    price = 110 * number_of_joinery
    if 60 > number_of_joinery > 30:
        price -= price * 0.05
    elif number_of_joinery > 60:
        price -= price * 0.08

elif type_of_joinery == "100X150":
    price = 140 * number_of_joinery
    if 80 > number_of_joinery > 40:
        price -= price * 0.06
    elif number_of_joinery > 80:
        price -= price * 0.10

elif type_of_joinery == "130X180":
    price = 190 * number_of_joinery
    if 50 > number_of_joinery > 20:
        price -= price * 0.07
    elif number_of_joinery > 50:
        price -= price * 0.12

elif type_of_joinery == "200X300":
    price = 250 * number_of_joinery
    if 50 > number_of_joinery > 25:
        price -= price * 0.09
    elif number_of_joinery > 50:
        price -= price * 0.14

if dev_or_no == "With delivery":
    total += 60
elif dev_or_no == "Without delivery":
    pass

sum = total + price

if number_of_joinery > 99:
    sum -= sum * 0.04
    print(f"{sum:.2f} BGN")
elif number_of_joinery < 10:
    print("Invalid order")
else:
    print(f"{sum:.2f} BGN")

