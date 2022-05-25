target = int(input())

counter = 1
cs_counter = 0
cs_money = 0
cc_counter = 0
cc_money = 0
money = 0

while True:
    product = input()

    if product == "End":
        print("Failed to collect required money for charity.")
        break

    product = int(product)

    if counter % 2 != 0 and product >= 100:
        print(f"Error in transaction!")
    elif counter % 2 == 0 and product <= 10:
        print(f"Error in transaction!")
    else:
        print("Product sold!")

    if product < 100 and counter % 2 == 0:
        cc_money += product
        cc_counter += 1
        money += product
    elif product > 10 and counter % 2 != 0:
        cs_money += product
        cs_counter += 1
        money += product

    if target <= money:
        avg_cs = cs_money / cs_counter
        avg_cc = cc_money / cc_counter
        print(f"Average CS: {avg_cs}")
        print(f"Average CC: {avg_cc}")
        break

    counter += 1

