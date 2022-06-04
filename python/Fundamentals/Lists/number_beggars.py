integers = input().split(", ")
count_of_beggars = int(input())
final_list = []
index_counter = 0

sum_of_money_for_each = []

for c in integers:
    sum_of_money_for_each.append(int(c))

while index_counter < count_of_beggars:
    sum_current_beggar = 0

    for index in range(index_counter, len(sum_of_money_for_each), count_of_beggars):
        sum_current_beggar += sum_of_money_for_each[index]
    index_counter += 1
    final_list.append(sum_current_beggar)

print(final_list)