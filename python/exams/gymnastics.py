country = input()
device = input()

points_diff = 0
points_perf = 0

if country == "Russia":
    if device == "ribbon":
        points_diff += 9.100
        points_perf += 9.400
    elif device == "hoop":
        points_diff += 9.300
        points_perf += 9.800
    elif device == "rope":
        points_diff += 9.600
        points_perf += 9.000

elif country == "Bulgaria":
    if device == "ribbon":
        points_diff += 9.600
        points_perf += 9.400
    elif device == "hoop":
        points_diff += 9.550
        points_perf += 9.750
    elif device == "rope":
        points_diff += 9.500
        points_perf += 9.400

elif country == "Italy":
    if device == "ribbon":
        points_diff += 9.200
        points_perf += 9.500
    elif device == "hoop":
        points_diff += 9.450
        points_perf += 9.350
    elif device == "rope":
        points_diff += 9.700
        points_perf += 9.150

total = points_diff + points_perf
diff = 20 - total
print(f"The team of {country} get {total:.3f} on {device}.")
print(f"{(diff / 20)* 100:.2f}%")