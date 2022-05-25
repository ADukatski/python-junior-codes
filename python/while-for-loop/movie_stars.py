budget_left = float(input())
after_salary = 0
actor_name = input()

while actor_name != "ACTION":

    if len(actor_name) <= 15:
        after_salary = float(input())
    else:
        after_salary = budget_left * 0.20

    budget_left -= after_salary

    if budget_left <= 0:
        print(f"We need {abs(budget_left):.2f} leva for our actors.")
        break

    actor_name = input()

if budget_left > 0:
    print(f"We are left with {budget_left:.2f} leva.")