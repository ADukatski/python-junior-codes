number_of_guests = int(input())
price_food_for_man = float(input())
budget = float(input())


if 10 <= number_of_guests <= 15:
    price_food_for_man -= price_food_for_man * 0.15
elif 15 < number_of_guests <= 20:
    price_food_for_man -= price_food_for_man * 0.20
elif 20 < number_of_guests:
    price_food_for_man -= price_food_for_man * 0.25

cake = budget * 0.10
total = (number_of_guests * price_food_for_man) + cake
diff = abs(total - budget)
if total <= budget:
    print(f"It is party time! {diff:.2f} leva left.")
else:
    print(f"No party! {diff:.2f} leva needed.")