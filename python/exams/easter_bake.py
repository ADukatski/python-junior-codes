import sys
from math import ceil

number_of_bread = int(input())

max_sugar = -sys.maxsize
max_flour = -sys.maxsize
sugar = 0
flour = 0
sugar_pack = 0 # 950
flour_pack = 0 # 750

for n in range(number_of_bread):
    sugar_used = int(input())
    flour_used = int(input())

    if sugar_used > max_sugar:
        max_sugar = sugar_used
    if flour_used > max_flour:
        max_flour = flour_used

    sugar += sugar_used
    flour += flour_used

sugar_pack = ceil(sugar / 950)
flour_pack = ceil(flour / 750)

print(f"Sugar: {sugar_pack}")
print(f"Flour: {flour_pack}")
print(f"Max used flour is {max_flour}"
      f" grams, max used sugar is {max_sugar} grams.")