import sys

number_of_targeted_movies = int(input())

high = -sys.maxsize
best_movie = ""
low = sys.maxsize
worst_movie = ""
rating = 0

for i in range(number_of_targeted_movies):
    movie_name = input()
    movie_rating = float(input())
    rating += movie_rating

    if movie_rating > high:
        high = movie_rating
        best_movie = movie_name
    if movie_rating < low:
        low = movie_rating
        worst_movie = movie_name


avg = rating / number_of_targeted_movies

print(f"{best_movie} is with highest rating: {high}")
print(f"{worst_movie} is with lowest rating: {low}")
print(f"Average rating: {avg:.1f}")