from math import floor
tournaments = int(input())
starting_points = int(input())

tournament_points = 0
counter_w = 0

for n in range(tournaments):
    stage = input()

    if stage == "W":
        tournament_points += 2000
        counter_w += 1
    elif stage == "F":
        tournament_points += 1200
    elif stage == "SF":
        tournament_points += 720

avg = tournament_points / tournaments
print(f"Final points: {tournament_points + starting_points}")
print(f"Average points: {floor(avg)}")
print(f"{(counter_w / tournaments) * 100:.2f}%")