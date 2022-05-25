control_min = int(input())
control_sec = int(input())
length_m = float(input())
s_for_100_m = int(input())

total_control_sec = control_sec + control_min * 60
slowed = length_m / 120
total_slowed = slowed * 2.5
his_time = (length_m / 100) * s_for_100_m - total_slowed

total = abs(his_time - total_control_sec)

if his_time > total_control_sec:
    print(f"No, Marin failed! He was {total:.3f} second slower.")
else:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {his_time:.3f}.")