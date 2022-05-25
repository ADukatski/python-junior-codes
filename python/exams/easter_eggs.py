import sys

painted_eggs = int(input())

biggest = -sys.maxsize
red = 0
orange = 0
green = 0
blue = 0

for n in range(painted_eggs):
    egg_color = input()

    if egg_color == "red":
        red += 1
    elif egg_color == "orange":
        orange += 1
    elif egg_color == "green":
        green += 1
    elif egg_color == "blue":
        blue += 1

if biggest < red:
    biggest = red
if biggest < orange:
    biggest = orange
if biggest < green:
    biggest = green
if biggest < blue:
    biggest = blue

if biggest == red:
    color = "red"
elif biggest == orange:
    color = "orange"
elif biggest == green:
    color = "green"
elif biggest == blue:
    color = "blue"


print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
print(f"Max eggs: {biggest} -> {color}")