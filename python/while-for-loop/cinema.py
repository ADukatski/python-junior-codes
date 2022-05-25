room_size = int(input())

total_people = 0
money = 0

while True:
    people = input()

    if people == "Movie time!":
        diff = abs (total_people - room_size)
        print(f"There are {diff} seats left in the cinema.")
        print(f"Cinema income - {money} lv.")
        break

    people = int(people)
    total_people += people
    if total_people > room_size:
        print(f"The cinema is full.")
        print(f"Cinema income - {money} lv.")
        break

    money += people * 5

    if people % 3 == 0:
        money -= 5
    else:
        pass

