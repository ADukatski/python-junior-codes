list_of_integers = input().split()
count_of_numbers_to_remove = int(input())

output = []

list_of_integers = list(map(int, list_of_integers))

for remove in range(count_of_numbers_to_remove):

    output.append(min(list_of_integers))
    list_of_integers.remove(min(list_of_integers))

list_of_integers = str(list_of_integers)[1:-1]
print(list_of_integers)

