number_of_groups = int(input())

musalla = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0

for n in range(number_of_groups):
    people_in_group = int(input())

    if people_in_group <= 5:
        musalla += people_in_group
    elif 6 <= people_in_group <= 12:
        monblan += people_in_group
    elif 13 <= people_in_group <= 25:
        kilimandjaro += people_in_group
    elif 26 <= people_in_group <= 40:
        k2 += people_in_group
    elif people_in_group >= 41:
        everest += people_in_group

total_people = musalla + monblan + kilimandjaro + k2 + everest

print(f"{(musalla / total_people) * 100:.2f}%")
print(f"{(monblan / total_people) * 100:.2f}%")
print(f"{(kilimandjaro / total_people) * 100:.2f}%")
print(f"{(k2 / total_people) * 100:.2f}%")
print(f"{(everest / total_people) * 100:.2f}%")