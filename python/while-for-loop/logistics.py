numbers_of_cargo = int(input())

total_weight = 0
microbus = 0
truck = 0
train = 0

for n in range(numbers_of_cargo):
    cargo_weight = int(input())

    if cargo_weight <= 3:
        microbus += cargo_weight
        total_weight += cargo_weight
    elif 4 <= cargo_weight <= 11:
        truck += cargo_weight
        total_weight += cargo_weight
    else:
        train += cargo_weight
        total_weight += cargo_weight

avg_per_ton = ((microbus * 200) + (truck * 175) + (train * 120)) / total_weight

print(f"{avg_per_ton:.2f}")
print(f"{(microbus / total_weight) * 100:.2f}%")
print(f"{(truck / total_weight) * 100:.2f}%")
print(f"{(train / total_weight) * 100:.2f}%")