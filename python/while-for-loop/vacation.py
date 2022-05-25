money_for_vacation = float(input())
our_money = float(input())
spending_counter = 0
day_counter = 0

while our_money < money_for_vacation and spending_counter < 5:
    spend_save = input()
    next_money = float(input())
    day_counter += 1

    if spend_save == "save":
        our_money += next_money
        spending_counter = 0

    elif spend_save == "spend":
        our_money -= next_money
        spending_counter += 1
        if our_money < 0:
            our_money = 0

if money_for_vacation <= our_money:
    print(f"You saved the money for {day_counter} days.")

if spending_counter == 5:
    print(f"You can't save the money.")
    print(day_counter)