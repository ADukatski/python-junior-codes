days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

plunder_gather = 0

for d in range(1, days + 1):

    plunder_gather += daily_plunder

    if d % 3 == 0:
        plunder_gather += daily_plunder * 0.50

    if d % 5 == 0:
        plunder_gather -= plunder_gather * 0.30


if plunder_gather >= expected_plunder:
    print(f"Ahoy! {plunder_gather:.2f} plunder gained.")
else:
    percentage = (plunder_gather / expected_plunder) * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")