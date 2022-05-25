from math import floor

record_in_s = float(input())
distance_in_m = float(input())
time_for_1_m = float(input())

climb_s = distance_in_m * time_for_1_m
slowed_s = floor(distance_in_m / 50) * 30
total_time = climb_s + slowed_s
diff = floor(record_in_s - total_time)

if total_time < record_in_s:
    print(f" Yes! The new record is {total_time:.2f} seconds.")
elif total_time >= record_in_s:
    print(f"No! He was {abs(diff):.2f} seconds slower.")