budget = float(input())
number_of_s = int(input())

for i in range(number_of_s):
    s_name = input()
    s_price = float(input())

    if s_name == "Thrones":
        s_price *= 0.50
    elif s_name == "Lucifer":
        s_price *= 0.40
    elif s_name == "Protector":
        s_price *= 0.30
    elif s_name == "TotalDrama":
        s_price *= 0.20
    elif s_name == "Area":
        s_price *= 0.10

    budget -= s_price

if budget < 0:
    print(f"You need {budget:.2f} lv. more to buy the series!")
else:
    print(f"You bought all the series and left with {budget:.2f} lv.")
