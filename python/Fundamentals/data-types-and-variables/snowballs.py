import sys

snowballs = int(input())

max_value = -sys.maxsize
max_weight = 0
max_time_needed = 0
max_quality = 0
value = 0

for s in range(snowballs):

    weight = int(input())
    time_needed = int(input())
    quality = int(input())

    value = (weight / time_needed) ** quality

    if value > max_value:
        max_value = value
        max_weight = weight
        max_quality = quality
        max_time_needed = time_needed

print(f"{max_weight} : {max_time_needed} = {int(max_value)} ({max_quality})")