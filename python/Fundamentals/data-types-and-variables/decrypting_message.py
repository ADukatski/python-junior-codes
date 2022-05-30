key = int(input())
lines = int(input())
word = ""

for l in range(lines):

    char = input()
    char1 = ord(char) + key
    letters = chr(char1)
    word += letters

print(word)