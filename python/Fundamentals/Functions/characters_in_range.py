import re

first_character = input()
second_character = input()

def between(first, second):
    first = ord(first_character)
    second = ord(second_character)
    collected_list = []

    for number in range(first, second + 1):
        if number == first or number == second:
            continue
        else:
            collected_list.append(chr(number))

    return collected_list
result = between(first_character, second_character)
print(" ".join(result))