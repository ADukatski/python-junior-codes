rent = int(input())

doll = rent - (rent * 0.30)
food = doll - (doll * 0.15)
sound = food / 2

total = doll + food + sound + rent
print(f"{total:.2f}")