int_one = int(input())
int_two = int(input())
int_three = int(input())

sum_numbers = lambda one, two: one + two

sum_numbers_result = sum_numbers(int_one, int_two)

subtract = lambda sum_result, three: sum_result - three

subtract_result = subtract(sum_numbers_result, int_three)

print(subtract_result)