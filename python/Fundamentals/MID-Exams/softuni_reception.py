employee1_per_h = int(input())
employee2_per_h = int(input())
employee3_per_h = int(input())
students_number = int(input())

time = 0

combination_of_employees = employee3_per_h + employee2_per_h + employee1_per_h

while students_number > 0:

    students_number -= combination_of_employees
    time += 1

    if time % 4 == 0:
        time += 1

print(f"Time needed: {time}h.")