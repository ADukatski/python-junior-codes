number = int(input())

positive_number = []
positive = 0
negative_number = []

for n in range(number):

    numbers = int(input())

    if numbers >= 0:
        positive_number.append(numbers)
        positive += 1

    elif numbers < 0:
        negative_number.append(numbers)

print(positive_number)
print(negative_number)
print(f"Count of positives: {positive}")
print(f"Sum of negatives: {sum(negative_number)}")