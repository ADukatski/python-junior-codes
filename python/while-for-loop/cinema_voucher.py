voucher_price = float(input())

total = 0
price = 0
ticket = 0
buy = 0

while True:
    product = input()

    if product == "End":
        print(ticket)
        print(buy)
        break

    if len(product) > 8:
        total += ord(product[0]) + ord(product[1])
        if total > voucher_price:
            print(ticket)
            print(buy)
            break

        ticket += 1

    elif len(product) < 8:
        total += ord(product[0])
        if total > voucher_price:
            print(ticket)
            print(buy)
            break
        buy += 1

    price = voucher_price - total

    if ord(product[0]) > price:
        print(ticket)
        print(buy)
        break