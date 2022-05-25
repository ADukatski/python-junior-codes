budget = float(input())
gender = input()
age = int(input())
sport = input()

total = 0

if gender == "m":
    if sport == "Gym":
        total += 42
    elif sport == "Boxing":
        total += 41
    elif sport == "Yoga":
        total += 45
    elif sport == "Zumba":
        total += 34
    elif sport == "Dances":
        total += 51
    elif sport == "Pilates":
        total += 39

elif gender == "f":
    if sport == "Gym":
        total += 35
    elif sport == "Boxing":
        total += 37
    elif sport == "Yoga":
        total += 42
    elif sport == "Zumba":
        total += 31
    elif sport == "Dances":
        total += 53
    elif sport == "Pilates":
        total += 37

if age <= 19:
    total -= total * 0.20
else:
    pass

diff = abs(total - budget)

if total <= budget:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${diff:.2f} more.")