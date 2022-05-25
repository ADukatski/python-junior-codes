movie_name = input()
day_number = int(input())
ticket_number = int(input())
ticket_price = float(input())
tax = int(input())

ticket_day = ticket_price * ticket_number
income = ticket_day * day_number
percent = income - (income * tax) / 100
print(f"The profit from the movie {movie_name} is {percent:.2f} lv.")