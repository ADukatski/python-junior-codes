p1_name = input()
p2_name = input()

p1_points = 0
p2_points = 0

while True:
    card_from_p1 = input()
    if card_from_p1 == "End of game":
        print(f"{p1_name} has {p1_points} points")
        print(f"{p2_name} has {p2_points} points")
        break
    card_from_p2 = input()

    card_from_p1 = int(card_from_p1)
    card_from_p2 = int(card_from_p2)

    if card_from_p1 > card_from_p2:
        p1_points += card_from_p1 - card_from_p2
    elif card_from_p2 > card_from_p1:
        p2_points += card_from_p2 - card_from_p1

    elif card_from_p1 == card_from_p2:
        card_from_p1 = int(input())
        card_from_p2 = int(input())
        if card_from_p1 > card_from_p2:
            print(f"Number wars!")
            print(f"{p1_name} is winner with {p1_points} points")
            break
        elif card_from_p2 > card_from_p1:
            print(f"Number wars!")
            print(f"{p2_name} is winner with {p2_points} points")
            break