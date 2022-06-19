number = input()

def odd_and_even(get_number):
    even_sum = 0
    odd_sum = 0

    for index in get_number:
        index = int(index)
        if index % 2 == 0:
            even_sum += index
        elif index % 2 != 0:
            odd_sum += index

    return(f"Odd sum = {odd_sum}, Even sum = {even_sum}")

print(odd_and_even(number))