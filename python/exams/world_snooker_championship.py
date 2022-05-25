stage = input()
ticket_type = input()
ticket_num = int(input())
picture = input()

price = 0
total = 0

if stage == "Quarter final":
    if ticket_type == "Standard":
        price += 55.50 * ticket_num
    elif ticket_type == "Premium":
        price += 105.20 * ticket_num
    elif ticket_type == "VIP":
        price += 118.90 * ticket_num

elif stage == "Semi final":
    if ticket_type == "Standard":
        price += 75.88 * ticket_num
    elif ticket_type == "Premium":
        price += 125.22 * ticket_num
    elif ticket_type == "VIP":
        price += 300.40 * ticket_num

elif stage == "Final":
    if ticket_type == "Standard":
        price += 110.10 * ticket_num
    elif ticket_type == "Premium":
        price += 160.66 * ticket_num
    elif ticket_type == "VIP":
        price += 400 * ticket_num

if price > 4000 and picture == "Y":
    price -= price * 0.25
    print(f"{price:.2f}")
elif 2500 < price <= 4000 and picture == "Y":
    price -= price * 0.10
    total = price + (ticket_num * 40)
    print(f"{total:.2f}")
elif picture == "Y":
    total = price + (ticket_num * 40)
    print(f"{total:.2f}")

elif price > 4000 and picture == "N":
    price -= price * 0.25
    print(f"{price:.2f}")
elif 2500 < price <= 4000 and picture == "N":
    price -= price * 0.10
    print(f"{price:.2f}")
else:
    print(f"{price:.2f}")