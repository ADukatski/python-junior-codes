full_energy = int(input())
battles_won = 0

while True:

    command = input()

    if command == "End of battle":
        print(f"Won battles: {battles_won}. Energy left: {full_energy}")
        break
    else:
        command = int(command)

    if full_energy < command:
        print(f"Not enough energy! Game ends with {battles_won} won battles and {full_energy} energy")
        break
    else:
        full_energy -= command
        battles_won += 1
        if battles_won % 3 == 0:
            full_energy += battles_won