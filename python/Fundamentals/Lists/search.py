number = int(input())
word = input()

strings_list = []
strings_word = []

for n in range(number):

    strings = input()
    strings_list.append(strings)

    if word in strings:
        strings_word.append(strings)


print(strings_list)
print(strings_word)
