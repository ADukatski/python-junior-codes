bottles = int(input())

counter = 0
consumed_ml_plates = 0
consumed_ml_pots = 0
consumed_ml = 0
pots = 0
plates = 0
total_in_bottles = bottles * 750

while True:
    dishes = input()

    if dishes == "End":
        print("Detergent was enough!")
        print(f"{plates} dishes and {pots} pots were washed.")
        left = abs(consumed_ml - total_in_bottles)
        print(f"Leftover detergent {left} ml.")
        break

    dishes = int(dishes)
    counter += 1

    if counter % 3 == 0:
        consumed_ml_pots += dishes
        pots += dishes
    else:
        consumed_ml_plates += dishes
        plates += dishes

    consumed_ml = consumed_ml_plates * 5 + consumed_ml_pots * 15

    if consumed_ml > total_in_bottles:
        diff = abs(consumed_ml - total_in_bottles)
        print(f"Not enough detergent, {diff} ml. more necessary!")
        break