number_bitcoins = int(input())
number_yuan = float(input())
tax = float(input())

price_bitcoin = number_bitcoins * 1168
price_yuan = (number_yuan * 0.15) * 1.76
total = (price_bitcoin + price_yuan) / 1.95
print(f"{total -(total * tax) / 100:.2f}")
