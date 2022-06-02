number = int(input())

l_numbers = []
l_filtered = []

for n in range(number):

    current_number = int(input())
    l_numbers.append(current_number)

command = input()

if command == "even":
    for n in l_numbers:
        if n % 2 == 0:
            l_filtered.append(n)
elif command == "odd":
    for n in l_numbers:
        if n % 2 != 0:
            l_filtered.append(n)
elif command == "negative":
    for n in l_numbers:
        if n < 0:
            l_filtered.append(n)
elif command == "positive":
    for n in l_numbers:
        if n >= 0:
            l_filtered.append(n)


print(l_filtered)