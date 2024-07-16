def add_movie(movies):
    """Додає новий фільм до бібліотеки."""
    title = input("Введіть назву фільму: ")
    year = int(input("Введіть рік випуску (2015-2018): "))
    genres = input("Введіть жанри через кому: ").split(",")
    rating = float(input("Введіть рейтинг популярності (0-10): "))
    movies.append({"title": title, "year": year, "genres": genres, "rating": rating})

def search_movies(movies):
    """Пошук фільмів за жанром або рейтингом."""
    search_type = input("Пошук за жанром (g) або рейтингом (r)? ")
    if search_type == "g":
        genre = input("Введіть жанр: ")
        for movie in movies:
            if genre in movie["genres"]:
                print(movie)
    elif search_type == "r":
        min_rating = float(input("Введіть мінімальний рейтинг: "))
        for movie in movies:
            if movie["rating"] >= min_rating:
                print(movie)

# Ініціалізація бібліотеки фільмів (порожній список)
movies = []

while True:
    action = input("Додати фільм (a), шукати (s) або вийти (q)? ")
    if action == "a":
        add_movie(movies)
    elif action == "s":
        search_movies(movies)
    elif action == "q":
        break
