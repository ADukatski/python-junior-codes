minutes_for_walking_day = int(input())
number_of_walking_day = int(input())
calories_for_day = int(input())

total_walking = minutes_for_walking_day * number_of_walking_day
burned_for_day = total_walking * 5
percent_of_daily = calories_for_day / 2

if burned_for_day >= percent_of_daily:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_for_day}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_for_day}.")