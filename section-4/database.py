import datetime
import sqlite3

CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
   id INTEGER PRIMARY KEY,
   title TEXT,
   release_timestamp REAL
);"""

CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTS users (
   username TEXT PRIMARY KEY
);"""

CREATE_WATCHED_TABLE = """CREATE TABLE IF NOT EXISTS watched (
   user_username TEXT,
   movie_id INTEGER,
   FOREIGN KEY (user_username) references users(username)
   FOREIGN KEY (movie_id) references movies(id)
);"""

CREATE_INDEX_MOVIE_RELEASE = "CREATE INDEX IF NOT EXISTS idx_movies_release ON movies(release_timestamp);"

INSERT_MOVIES = "INSERT INTO movies (title, release_timestamp) VALUES (?, ?)"
INSERT_USER = "INSERT INTO users (username) VALUES (?)"
DELETE_MOVIE = "DELETE FROM movies WHERE title = ?;"
SEARCH_MOVIES = "SELECT * FROM movies WHERE title like ?;"
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies where release_timestamp > ?;"
INSERT_WATCHED_MOVIES = "INSERT INTO watched (user_username, movie_id) VALUES (?, ?)"
SET_WATCHED_MOVIE = "UPDATE movies SET watched = 1 WHERE title = ?;"
SELECT_WATCHED_MOVIES = """SELECT movies.*
                            FROM movies
                            JOIN watched ON movies.id = watched.movie_id
                            JOIN users ON users.username = watched.user_username
                            WHERE users.username = ?;"""

connection = sqlite3.connect("data.db")


def create_tables():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_USERS_TABLE)
        connection.execute(CREATE_WATCHED_TABLE)
        connection.execute(CREATE_INDEX_MOVIE_RELEASE)


def add_user(username):
    with connection:
        connection.execute(INSERT_USER, (username,))


def add_movie(title, release_timestamp):
    with connection:
        connection.execute(INSERT_MOVIES, (title, release_timestamp))


def get_movies(upcoming=False):
    with connection:
        cursor = connection.cursor()
        if upcoming:
            today_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp,))
        else:
            cursor.execute(SELECT_ALL_MOVIES)
        return cursor.fetchall()


def search_movies(movie):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SEARCH_MOVIES, (f'%{movie}%',))
        return cursor.fetchall()


def watch_movie(username, movie_id):
    with connection:
        connection.execute(INSERT_WATCHED_MOVIES, (username, movie_id))


def get_watched_movies(username):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_WATCHED_MOVIES, (username,))
        return cursor.fetchall()


def delete_movie(title):
    with connection:
        connection.execute(DELETE_MOVIE, (title,))
