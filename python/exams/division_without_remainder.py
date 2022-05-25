numbers = int(input())

two = 0
three = 0
four = 0


for n in range(numbers):
    next_numb = int(input())

    if next_numb % 2 == 0:
        two += 1
    if next_numb % 3 == 0:
        three += 1
    if next_numb % 4 == 0:
        four += 1


print(f"{(two / numbers) * 100:.2f}%")
print(f"{(three / numbers) * 100:.2f}%")
print(f"{(four / numbers) * 100:.2f}%")