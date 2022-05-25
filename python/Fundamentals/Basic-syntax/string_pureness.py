rounds = int(input())
not_pure = [".", ",", "_"]

for n in range(rounds):
    string = input()

    if "." in string or "_" in string or "," in string:
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")