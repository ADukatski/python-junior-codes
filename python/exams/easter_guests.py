from math import ceil

number_of_guests = int(input())
budget = int(input())

needed_cakes = ceil(number_of_guests / 3)
cake_price = needed_cakes * 4
needed_eggs = ceil(number_of_guests * 2)
egg_price = needed_eggs * 0.45
need = egg_price + cake_price
diff = abs(need - budget)

if need <= budget:
    print(f"Lyubo bought {needed_cakes} Easter bread and {needed_eggs} eggs.")
    print(f"He has {diff:.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {diff:.2f} lv. more.")