bad_grades = int(input())
count_bad_grades = 0
score = 0
total = 0
last_exercise = " "

while True:
    exam_name = input()
    if exam_name == "Enough":
        print(f"Average score: {score / total:.2f}")
        print(f"Number of problems: {total}")
        print(f"Last problem: {last_exercise}")
        break

    grade = int(input())
    total += 1
    score += grade
    last_exercise = exam_name

    if grade <= 4:
        count_bad_grades += 1

    if bad_grades <= count_bad_grades:
        print(f"You need a break, {count_bad_grades} poor grades.")
        break
