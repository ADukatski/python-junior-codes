height = int(input())
weight = int(input())

counter = 0
total = height * weight

while True:
    cake_number = input()

    if cake_number == "STOP":
        left = abs(counter - total)
        print(f"{left} pieces are left.")
        break

    cake_number = int(cake_number)
    counter += cake_number

    if counter >= total:
        diff = abs (counter - total)
        print(f"No more cake left! You need {diff} pieces more.")
        break