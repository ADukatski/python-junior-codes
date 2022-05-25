number_of_students = int(input())

top = 0
between_4_499 = 0
between_3_399 = 0
fail = 0
avg = 0

for i in range(1, number_of_students + 1):
    exam_grade = float(input())

    if exam_grade >= 5.00:
        top += 1
        avg += exam_grade
    elif 4 <= exam_grade <= 4.99:
        between_4_499 += 1
        avg += exam_grade
    elif 3 <= exam_grade <= 3.99:
        between_3_399 += 1
        avg += exam_grade
    elif 3 > exam_grade:
        fail += 1
        avg += exam_grade

total = top + between_3_399 + between_4_499 + fail
print(f"Top students: {(top / total) * 100:.2f}%")
print(f"Between 4.00 and 4.99: {(between_4_499 / total) * 100:.2f}%")
print(f"Between 3.00 and 3.99: {(between_3_399 / total) * 100:.2f}%")
print(f"Fail: {(fail / total) * 100:.2f}%")
print(f"Average: {avg / number_of_students:.2f}")