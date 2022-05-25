rent_for_room = float(input())

cake = rent_for_room * 0.20
drinks = cake - (cake * 0.45)
animator = rent_for_room / 3

total = rent_for_room + cake + drinks + animator
print(total)