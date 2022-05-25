from math import floor

balls = int(input())

total = 0
red = 0
orange = 0
yellow = 0
white = 0
others = 0
divided = 0

for n in range(balls):
    colors = input()

    if colors == "red":
        total += 5
        red += 1
    elif colors == "orange":
        total += 10
        orange += 1
    elif colors == "yellow":
        total += 15
        yellow += 1
    elif colors == "white":
        total += 20
        white += 1
    elif colors == "black":
        total = floor(total / 2)
        divided += 1
    if colors != "red" and colors != "orange" and colors != "yellow" and colors != "white" and colors != "black":
        others += 1

print(f"Total points: {total}")
print(f"Red balls: {red}")
print(f"Orange balls: {orange}")
print(f"Yellow balls: {yellow}")
print(f"White balls: {white}")
print(f"Other colors picked: {others}")
print(f"Divides from black balls: {divided}")