p1_number_of_eggs = int(input())
p2_number_of_eggs = int(input())

p1 = p1_number_of_eggs
p2 = p2_number_of_eggs

while True:
    winner = input()

    if winner == "End of battle":
        print(f"Player one has {p1} eggs left.")
        print(f"Player two has {p2} eggs left.")
        break

    if winner == "one":
        p2 -= 1
    elif winner == "two":
        p1 -= 1

    if p1 == 0:
        print(f"Player one is out of eggs. Player two has {p2} eggs left.")
        break
    elif p2 == 0:
        print(f"Player two is out of eggs. Player one has {p1} eggs left.")
        break