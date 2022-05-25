visitors = int(input())

back = 0
chest = 0
legs = 0
abs = 0
protein_shake = 0
protein_bar = 0


for n in range(visitors):
    part = input()

    if part == "Back":
        back += 1
    elif part == "Chest":
        chest += 1
    elif part == "Legs":
        legs += 1
    elif part == "Abs":
        abs += 1
    elif part == "Protein shake":
        protein_shake += 1
    elif part == "Protein bar":
        protein_bar += 1

total_trainers = back + abs + chest + legs
total_protein = protein_shake + protein_bar
total = total_protein + total_trainers


print(f"{back:} - back")
print(f"{chest:} - chest")
print(f"{legs:} - legs")
print(f"{abs:} - abs")
print(f"{protein_shake:} - protein shake")
print(f"{protein_bar:} - protein bar")
print(f"{(total_trainers / total) * 100:.2f}% - work out")
print(f"{(total_protein / total) * 100:.2f}% - protein")