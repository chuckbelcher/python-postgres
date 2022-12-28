import datetime
import database

menu = """Please select one of the following options: 
 1) Add new movie
 2) View upcoming movies
 3) View all movies
 4) Watch a movie
 5) View watched movies
 6) Exit
 
 Your Selection: """
 
welcome_message = "Welcome to the watch list"

def add_movie():
    title = input("What is the name of the movie: ")
    release_date = input("What is the release date (dd-mm-yyyy): ")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed_date.timestamp()
    
    database.add_movie(title, timestamp)

def display_upcoming_movies(heading, movies):
    print(f"{heading} Movies List")
    for movie in movies:
        movie_date = datetime.datetime.fromtimestamp(movie[1]).strftime("%b %d %Y")
        print(f"{movie[0]} - released on {movie_date}")
    print("---\n")


def watch_movie():
    title = input("What movie do you want to watch? ")
    database.watch_movie(title)

print(welcome_message)
database.create_tables()

while (user_input := input(menu)) !='6':
    if user_input == "1":
        add_movie()
    elif user_input == "2":
        movies = database.get_movies(True)
        display_upcoming_movies("Upcoming", movies)
    elif user_input == "3":
        movies = database.get_movies()
        display_upcoming_movies("All", movies)
    elif user_input == "4":
        watch_movie()
    elif user_input == "5":
        movies = database.get_watched_movies()
        display_upcoming_movies("Watched", movies)
    else:
        print("You did not enter a valid selection")