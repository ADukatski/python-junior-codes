actor_name = input()
academy_points = float(input())
jury = int(input())


for i in range(jury):
    jury_name = input()
    jury_points = float(input())

    current = (len(jury_name) * jury_points) / 2

    academy_points += current

    if academy_points >= 1250.5:
        break

if academy_points >= 1250.5:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!')
else:
    needed_score = 1250.5 - academy_points
    print(f"Sorry, {actor_name} you need {needed_score:.1f} more!")

