while True:
    string = input()

    if string == "End":
        break

    if string != "SoftUni":
        for char in string:
            print(char * 2, end="")
        print()