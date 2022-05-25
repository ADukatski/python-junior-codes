from math import ceil

wall_height = int(input())
wall_weight = int(input())
percent_from_total_not_for_painting = int(input())

painting = 0
paint_count = 0

total_w_h = (wall_height * wall_weight) * 4
for_paint = total_w_h - ((total_w_h * percent_from_total_not_for_painting) / 100)

while True:
    l_painting = input()

    if l_painting == "Tired!":
        print(f"{ceil(for_paint)} quadratic m left.")
        break
    l_painting = int(l_painting)

    for_paint -= l_painting

    if for_paint < 0:
        diff = abs(for_paint)
        print(f"All walls are painted and you have {ceil(diff)} l paint left!")
        break
    elif for_paint == 0:
        print(f"All walls are painted! Great job, Pesho!")
        break