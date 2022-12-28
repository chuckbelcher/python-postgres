import sqlite3
connection = sqlite3.connect("data.db")


def create_table():
    with connection:
        connection.execute("CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT)")
    

def add_entry(entry_content, entry_date):
    with connection:
        connection.execute("insert into entries values (?, ?);", (entry_content, entry_date))

def get_entries():
    cursor = connection.execute('select * from entries;')
    return cursor.fetchall()

def close_db_connection():
    connection.close()