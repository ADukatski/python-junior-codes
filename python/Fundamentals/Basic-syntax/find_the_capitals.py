word = input()

index = []

for w in range(len(word)):

    if word[w].isupper():
        index.append(w)

print(index)