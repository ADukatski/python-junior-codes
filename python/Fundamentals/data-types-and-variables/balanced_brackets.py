lines = int(input())

opened = 0
closed = 0

for l in range(lines):
    symbol = input()

    if symbol == "(":
        opened += 1
    elif symbol == ")":
        closed += 1

    if opened >= 2 and closed == 0 or closed >= 2 and opened == 0:
        print("UNBALANCED")
        exit()

if opened >= 2 and closed == 0 or closed >= 2 and opened == 0:
    print("UNBALANCED")
else:
    print("BALANCED")

