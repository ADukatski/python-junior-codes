product = input()
quantity = int(input())

def shop(type,quant):
    price = 0

    if type == "coffee":
        price = 1.50 * quant

    elif type == "water":
        price = 1.00 * quant

    elif type == "coke":
        price = 1.40 * quant

    elif type == "snacks":
        price = 2.00 * quant

    return(f"{price:.2f}")

print(shop(product, quantity))