total_eggs = int(input())

total = total_eggs
sold = 0

while True:
    buy_or_fill = input()

    if buy_or_fill == "Close":
        print(f"Store is closed!")
        print(f"{sold} eggs sold.")
        break
    else:
        num_b_or_f = int(input())

    if buy_or_fill == "Buy":
        if num_b_or_f > total:
            print(f"Not enough eggs in store!")
            print(f"You can buy only {total}.")
            break
        total -= num_b_or_f
        sold += num_b_or_f
    elif buy_or_fill == "Fill":
        total += num_b_or_f
