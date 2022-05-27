number = int(input())

suma = 0
for i in range(number):
    char = input()

    char_sum = ord(char)
    suma += char_sum
print(f"The sum equals: {suma}")