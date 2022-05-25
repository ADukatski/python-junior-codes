from math import ceil

number_of_people = int(input())
price_entrance = float(input())
price_for_one_chair = float(input())
price_for_one_umbrella = float(input())

entrance = number_of_people * price_entrance
for_chairs = ceil(number_of_people * 0.75)
price_chairs = for_chairs * price_for_one_chair
for_umbrella = ceil(number_of_people * 0.50)
price_umbrella = for_umbrella * price_for_one_umbrella
total = entrance + price_umbrella + price_chairs
print(f"{total:.2f} lv.")