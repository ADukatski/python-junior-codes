import sys

num1 = int(input())
num2 = int(input())
num3 = int(input())

max_number = -sys.maxsize

if num1 > max_number:
    max_number = num1

if num2 > max_number:
    max_number = num2

if num3 > max_number:
    max_number = num3

print(max_number)