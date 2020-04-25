import sqlite3

# Open database
conn = sqlite3.connect('db.sqlite3')

def tables_in_sqlite_db(conn):
    cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [
        v[0] for v in cursor.fetchall()
        if v[0] != "sqlite_sequence"
    ]
    cursor.close()
    return tables

# List tables
tables = tables_in_sqlite_db(conn)
# Your code goes here!
# Example:
print(tables)

# list all books in the tables
def list_all_books(conn):
    cursor = conn.execute('select * from quickstart_books;')
    data = [v for v in cursor.fetchall()]
    cursor.close()
    return data


data = list_all_books(conn)
print(data)


def find_books_with_no_chapters(conn, books):
    cursor = conn.execute('select * from quickstart_chapters where book;')
    chapter

