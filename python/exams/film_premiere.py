movie = input()
pack = input()
tickets = int(input())

total = 0

if movie == "John Wick":
    if pack == "Drink":
        total += 12 * tickets
    elif pack == "Popcorn":
        total += 15 * tickets
    elif pack == "Menu":
        total += 19 * tickets

if movie == "Star Wars":
    if pack == "Drink":
        total += 18 * tickets
    elif pack == "Popcorn":
        total += 25 * tickets
    elif pack == "Menu":
        total += 30 * tickets

if movie == "Jumanji":
    if pack == "Drink":
        total += 9 * tickets
    elif pack == "Popcorn":
        total += 11 * tickets
    elif pack == "Menu":
        total += 14 * tickets

if movie == "Star Wars" and tickets >= 4:
    total -= total * 0.30
elif movie == "Jumanji" and tickets == 2:
    total -= total * 0.15

print(f"Your bill is {total:.2f} leva.")
