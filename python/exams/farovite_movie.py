import sys

movie_name = input()

total = 0
counter = 0
sum_of_symbols = -sys.maxsize

while movie_name != "STOP" or counter == 7:

    counter += 1

    for char in movie_name:
        value = ord(char)

        if 'a' <= char <= 'z':
            total += value -  (2 * len(movie_name))
        elif 'A' <= char <= 'Z':
            total += value - len(movie_name)
        else:
            total += value

        if sum_of_symbols < value:
            value = sum_of_symbols

    movie_name = input()


print(f"The best movie for you is {movie_name} with {sum_of_symbols} ASCII sum.")