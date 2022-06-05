import sys

number_students = int(input())
number_lectures = int(input())
additional_bonus = int(input())

max_bonus = -sys.maxsize
attend = 0

if number_lectures == 0:
    print(f'Max Bonus: 0.')
    print(f'The student has attended 0 lectures.')
else:
    for s in range(1, number_students + 1):
        attendance_of_student = int(input())

        total_bonus = (attendance_of_student / number_lectures) * (5 + additional_bonus)

        if total_bonus > max_bonus:
            max_bonus = total_bonus
            attend = attendance_of_student

    print(f"Max Bonus: {round(max_bonus)}.")
    print(f"The student has attended {attend} lectures.")