grade = float(input())

def grades(value):

    if value >= 2.00 and value <= 2.99:
        return 'Fail'

    elif value >= 3.00 and value <= 3.49:
        return "Poor"

    elif value >= 3.50 and value <= 4.49:
        return "Good"

    elif value >= 4.50 and value <= 5.49:
        return "Very Good"

    elif value >= 5.50 and value <= 6.00:
        return "Excellent"

print(grades(grade))