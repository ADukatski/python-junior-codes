word = input()
word_count = 0
casefold = word.casefold()

for w in ('sand', 'water', 'fish', 'sun'):
    word_count += casefold.count(w)


print(word_count)