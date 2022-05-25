movie_name = input()

total = 0
student = 0
standard = 0
kids = 0

while movie_name != "Finish":
    free_space = int(input())
    busy = 0

    if movie_name == "Finish":
        break

    for i in range(free_space):
        ticket_type = input()

        if ticket_type == "student":
            student += 1
        elif ticket_type == "standard":
            standard += 1
        elif ticket_type == "kid":
            kids += 1
        elif ticket_type == "End":
            break

        total += 1
        busy += 1

    percent_full = (busy / free_space) * 100
    total = student + standard + kids
    print(f"{movie_name} - {percent_full:.2f}% full.")
    movie_name = input()

print(f'Total tickets: {total:.2f}')
print(f'{(student / total) * 100:.2f}% student tickets.')
print(f'{(standard / total) * 100:.2f}% standard tickets.')
print(f'{(kids / total) * 100:.2f}% kids tickets.')