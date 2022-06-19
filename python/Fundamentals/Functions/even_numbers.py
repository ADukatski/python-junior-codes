sequence_of_numbers = input().split()
even_list = []

def even():

    for n in sequence_of_numbers:
        n = int(n)
        if n % 2 == 0:
            even_list.append(n)

    return even_list

print(even())