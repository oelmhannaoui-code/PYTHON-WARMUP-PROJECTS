# MOVIE DATABASE:


movies = []

# search by title, delete movies, show higher rankings

def menu():
    print("1. Add movie ")
    print("2. Remove movie ")
    print("3. Search by title ")
    print("4. Show higher rankings ")
    print("5. Exit ")
def add_movie():
    title = input("Enter movie title: ")
    year = int(input("Enter movie year: "))
    rating = int(input("Enter movie rating: "))

    movies.append({"title":title,"year":year,"rating":rating})
def remove_movie():
    title = input("Enter movie title: ")
    for movie in movies:
     if title.lower() == movie['title'].lower():
        movies.remove(movie)
        print(f"{title} removed")
        return
    else:
        print("Movie not found")
def search_movie():
    title = input("Enter movie title: ")
    for movie in movies:
     if title.lower() == movie['title'].lower():
        print(f"{title} found")
        print(f'YEAR: {movie["year"]}')
        print(f'Rating: {movie["rating"]}')
        return
    else:
        print("Movie not found")
def show_higher_rankings():
    if len(movies) == 0:
        print("No movies in the database.")
        return
    highest_rating = movies[0]
    for movie in movies:
        if movie['rating'] > highest_rating['rating']:
            highest_rating = movie
    print(f"\nHighest rated movie: {highest_rating['title']}")
    print(f"Rating : {highest_rating['rating']}")
choice = 0

while choice != 5:
    menu()
    choice = int(input("Choose: "))

    if choice == 1:
        add_movie()
    elif choice == 2:
        remove_movie()
    elif choice == 3:
        search_movie()
    elif choice == 4:
        show_higher_rankings()
