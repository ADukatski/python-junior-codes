months = int(input())

electricity = 0
water = 0
internet = 0
others = 0

for m in range(months):
    electricity_bill = float(input())

    water_m = 20
    water = 20 * months

    internet_m = 15
    internet = 15 * months

    electricity_m = electricity_bill
    electricity += electricity_m

    others += (water_m + internet_m + electricity_bill) + 0.20 * 100

print(electricity)
print(water)
print(internet)
print(others)