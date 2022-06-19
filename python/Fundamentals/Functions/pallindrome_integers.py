numbers = input().split(", ")
numbers_forward = ""
numbers_backward = ""

for num in numbers:
    numbers_forward = num
    numbers_backward = num[::-1]

    if numbers_forward == numbers_backward:
        print("True")
    else:
        print("False")