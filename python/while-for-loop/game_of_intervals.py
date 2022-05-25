number_of_rounds = int(input())

points = 0
invalid = 0
from_40_50 = 0
from_30_39 = 0
from_20_29 = 0
from_10_19 = 0
from_0_9 = 0

for i in range(number_of_rounds):
    number = int(input())

    if number > 50 or number < 0:
        invalid += 1
        points /= 2
    elif 40 <= number <= 50:
        from_40_50 += 1
        points += 100
    elif 30 <= number <= 39:
        from_30_39 += 1
        points += 50
    elif 20 <= number <= 29:
        from_20_29 += 1
        points += 0.40 * number
    elif 10 <= number <= 19:
        from_10_19 += 1
        points += 0.30 * number
    elif 0 <= number <= 9:
        from_0_9 += 1
        points += 0.20 * number

total = from_10_19 + from_0_9 + from_20_29 + from_40_50 + from_30_39 + invalid

print(f"{points:.2f}")
print(f"From 0 to 9: {(from_0_9 / total) * 100:.2f}%")
print(f"From 10 to 19: {(from_10_19 / total) * 100:.2f}%")
print(f"From 20 to 29: {(from_20_29 / total) * 100:.2f}%")
print(f"From 30 to 39: {(from_30_39 / total) * 100:.2f}%")
print(f"From 40 to 50: {(from_40_50 / total) * 100:.2f}%")
print(f"Invalid numbers: {(invalid / total) * 100:.2f}%")
