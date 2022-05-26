numbers = int(input())

for n in range(1, numbers + 1):
    digits = 0
    dig = n
    while dig > 0:
        digits += dig % 10
        dig = int(dig / 10)
    if digits == 5 or digits == 7 or digits == 11:
        print(f"{n} -> True")
    else:
        print(f"{n} -> False")