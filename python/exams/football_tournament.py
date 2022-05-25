football_teams = input()
played_matches = int(input())

w = 0
l = 0
d = 0

for n in range(played_matches):

    result = input()

    if result == "W":
        w += 1
    elif result == "L":
        l += 1
    elif result == "D":
        d += 1

if played_matches <= 0:
    print(f"{football_teams} hasn't played any games during this season.")
else:
    total_p = (w * 3) + (d * 1)
    total = w + l + d
    total_w_ratio = (w / total) * 100

    print(f"{football_teams} has won {total_p} points during this season.")
    print(f"Total stats:")
    print(f"## W: {w}")
    print(f"## D: {d}")
    print(f"## L: {l}")
    print(f"Win rate: {total_w_ratio:.2f}%")