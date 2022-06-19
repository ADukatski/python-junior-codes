number = int(input())

def is_perfect(n):
    sum = 0

    for divisor in range(1, n):
        if n % divisor == 0:
            sum += divisor

    if n == sum:
        return "We have a perfect number!"
    return "It's not so perfect."

print(is_perfect(number))