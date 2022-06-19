operator = input()
num_one = int(input())
num_two = int(input())

def calculations(a, b, op):
    result = 0

    if op == "multiply":
        result = a * b
    elif op == "divide":
        result = a / b
    elif op == "add":
        result = a + b
    elif op == "subtract":
        result = a - b

    return int(result)

print(calculations(num_one, num_two, operator))