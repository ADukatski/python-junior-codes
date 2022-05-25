import sys

player_name = input()
goals_scored = 0

top = -sys.maxsize
best_name = ""
best_score = 0

while True:

    if player_name == "END":
        print(f"{best_name} is the best player!")
        if goals_scored >= 3:
            print(f"He has scored {goals_scored} goals and made a hat-trick !!!")
        else:
            print(f"He has scored {goals_scored} goals.")
        break
    else:
        goals_scored = int(input())

    if goals_scored > top:
        top = goals_scored
        best_name = player_name

    if goals_scored >= 10:
        print(f"{best_name} is the best player!")
        if goals_scored >= 3:
            print(f"He has scored {goals_scored} goals and made a hat-trick !!!")
        else:
            print(f"He has scored {goals_scored} goals.")
        break
    player_name = input()