numbers = input().split()

sorted_numbers = []

for n in numbers:

    n = int(n)
    sorted_numbers.append(n)

sorted_numbers = sorted(sorted_numbers)
print(sorted_numbers)