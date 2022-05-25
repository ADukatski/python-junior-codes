res_1 = input()
res_2 = input()
res_3 = input()

w = 0
l = 0
d = 0

if ord(res_1[0]) > ord(res_1[2]):
    w += 1

elif ord(res_1[0]) < ord(res_1[2]):
    l += 1

elif ord(res_1[0]) == ord(res_1[2]):
    d += 1

if ord(res_2[0]) > ord(res_2[2]):
    w += 1

elif ord(res_2[0]) < ord(res_2[2]):
    l += 1

elif ord(res_2[0]) == ord(res_2[2]):
    d += 1

if ord(res_3[0]) > ord(res_3[2]):
    w += 1

elif ord(res_3[0]) < ord(res_3[2]):
    l += 1

elif ord(res_3[0]) == ord(res_3[2]):
    d += 1

print(f"Team won {w} games.")
print(f"Team lost {l} games.")
print(f"Drawn games: {d}")