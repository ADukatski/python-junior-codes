command = input()
coffee = 0

upper = ["CODING", "CAT", "DOG", "MOVIE"]
lower = ["coding", "cat", "dog", "movie"]

while True:

    if command == "END":
        if coffee > 5:
            print("You need extra sleep")
            break
        else:
            print(coffee)
            break

    if command in lower:
        coffee += 1
    elif command in upper:
        coffee += 2

    command = input()