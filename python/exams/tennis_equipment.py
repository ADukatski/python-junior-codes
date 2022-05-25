from math import floor, ceil

rocket_price = float(input())
number_rockets = int(input())
trainers = int(input())

rocket = rocket_price * number_rockets
trainers_price = rocket_price / 6
for_all_trainers = trainers_price * trainers
with_disc = (rocket + for_all_trainers) * 0.20
total = with_disc + rocket + for_all_trainers
djocovic = total / 8
sponsors = total * 7 / 8

print(f"Price to be paid by Djokovic {floor(djocovic)}")
print(f"Price to be paid by sponsors {ceil(sponsors)}")