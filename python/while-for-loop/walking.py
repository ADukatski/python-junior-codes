goal = 10000
total_for_today = 0

while True:
    steps = input()

    if steps == "Going home":
        steps = int(input())
        total_for_today += steps
        if total_for_today >= goal:
            over = abs(goal - total_for_today)
            print("Goal reached! Good job!")
            print(f"{over} steps over the goal!")
        else:
            over = abs(goal - total_for_today)
            print(f"{over} more steps to reach goal.")
        break

    total_for_today += int(steps)
    if total_for_today >= goal:
        diff = abs(goal - total_for_today)
        print("Goal reached! Good job!")
        print(f"{diff} steps over the goal!")
        break