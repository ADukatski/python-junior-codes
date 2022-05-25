player_name = input()

points = 301
new = 0
shots = 0
missed = 0

while True:
    arena = input()

    if arena == "Retire":
        print(f"{player_name} retired after {missed} unsuccessful shots.")
        break

    new_points = int(input())

    if arena == "Triple":
        new = new_points * 3
    elif arena == "Double":
        new = new_points * 2
    elif arena == "Single":
        new = new_points * 1

    if new > points:
        missed += 1
    else:
        points = points - new
        shots += 1

    if points == 0:
        print(f"{player_name} won the leg with {shots} shots.")
        break