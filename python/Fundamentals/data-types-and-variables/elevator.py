import math

people = int(input())
capacity = int(input())

course = people / capacity
left = people % capacity

if left == 0:
    print(int(course))

elif left != 0:
    l = (course + left / left)
    print(int(l))