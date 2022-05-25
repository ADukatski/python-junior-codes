book = input()
counter = 0

while True:
    next_book = input()

    if next_book == book:
        print(f"You checked {counter} books and found it.")
        break

    elif next_book == "No More Books":
        print(f"The book you search is not here!")
        print(f"You checked {counter} books.")
        break

    counter += 1
