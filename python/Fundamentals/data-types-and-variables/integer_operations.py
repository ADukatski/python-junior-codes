from math import floor

x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())

x1_x2 = x1 + x2
x2_x3 = floor(x1_x2 / x3)
x3_x4 = x2_x3 * x4

print(f"{x3_x4:.0f}")