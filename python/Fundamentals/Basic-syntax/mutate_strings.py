first = input()
second = input()
last = first
for i in range(len(second)):

    left = second[:i + 1]
    right = first[i+1:]
    combine = left + right

    if combine == last:
        continue

    print(combine)
    last = combine