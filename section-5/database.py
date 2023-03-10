import os
import datetime
import psycopg2
from dotenv import load_dotenv

load_dotenv()

CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
   id SERIAL PRIMARY KEY,
   title TEXT,
   release_timestamp REAL
);"""

CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTS users (
   username TEXT PRIMARY KEY
);"""

CREATE_WATCHED_TABLE = """CREATE TABLE IF NOT EXISTS watched (
   user_username TEXT references users(username),
   movie_id INTEGER references movies(id)
);"""

# Create lookup table for SQLite
# CREATE_WATCHED_TABLE = """CREATE TABLE IF NOT EXISTS watched (
#    user_username TEXT,
#    movie_id INTEGER,
#    FOREIGN KEY (user_username) references users(username)
#    FOREIGN KEY (movie_id) references movies(id)
# );"""

CREATE_INDEX_MOVIE_RELEASE = "CREATE INDEX IF NOT EXISTS idx_movies_release ON movies(release_timestamp);"

INSERT_MOVIES = "INSERT INTO movies (title, release_timestamp) VALUES (%s, %s)"
INSERT_USER = "INSERT INTO users (username) VALUES (%s)"
DELETE_MOVIE = "DELETE FROM movies WHERE title = %s;"
SEARCH_MOVIES = "SELECT * FROM movies WHERE title like %s;"
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies where release_timestamp > %s;"
INSERT_WATCHED_MOVIES = "INSERT INTO watched (user_username, movie_id) VALUES (%s, %s)"
SET_WATCHED_MOVIE = "UPDATE movies SET watched = 1 WHERE title = %s;"
SELECT_WATCHED_MOVIES = """SELECT movies.*
                            FROM movies
                            JOIN watched ON movies.id = watched.movie_id
                            JOIN users ON users.username = watched.user_username
                            WHERE users.username = %s;"""

connection = psycopg2.connect(os.environ["LOCAL_DATABASE_URL"])


def create_tables():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_MOVIES_TABLE)
            cursor.execute(CREATE_USERS_TABLE)
            cursor.execute(CREATE_WATCHED_TABLE)
            cursor.execute(CREATE_INDEX_MOVIE_RELEASE)


def add_user(username):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_USER, (username,))


def add_movie(title, release_timestamp):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_MOVIES, (title, release_timestamp))


def get_movies(upcoming=False):
    with connection:
        with connection.cursor() as cursor:
            if upcoming:
                today_timestamp = datetime.datetime.today().timestamp()
                cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp,))
            else:
                cursor.execute(SELECT_ALL_MOVIES)
            return cursor.fetchall()


def search_movies(movie):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SEARCH_MOVIES, (f'%{movie}%',))
            return cursor.fetchall()


def watch_movie(username, movie_id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_WATCHED_MOVIES, (username, movie_id))


def get_watched_movies(username):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_WATCHED_MOVIES, (username,))
            return cursor.fetchall()


def delete_movie(title):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(DELETE_MOVIE, (title,))


