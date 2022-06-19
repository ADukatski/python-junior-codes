numbers = input().split()
sum_list = []

for n in numbers:
    n = int(n)
    sum_list.append(n)

min_number = min(sum_list)
print(f"The minimum number is {min_number}")
max_number = max(sum_list)
print(f"The maximum number is {max_number}")
sum_number = sum(sum_list)
print(f"The sum number is: {sum_number}")