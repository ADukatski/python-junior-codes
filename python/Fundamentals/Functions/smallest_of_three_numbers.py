import sys

number_one = int(input())
number_two = int(input())
number_three = int(input())

def smallest_is(one,two,three):
    small = sys.maxsize

    if small > number_one:
        small = number_one

    if small > number_two:
        small = number_two

    if small > number_three:
        small = number_three

    return small

print(smallest_is(number_one, number_two, number_three))