import sqlite3

def connect():
    return sqlite3.connect("books.db")

def create_table(connection):
    connection.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT
    )
    """)
    connection.commit()

def add_book(connection, title):
    connection.execute(
        "INSERT INTO books (title) VALUES (?)",
        (title,)
    )
    connection.commit()

def get_all_books(connection):
    return connection.execute(
        "SELECT * FROM books"
    ).fetchall()

def update_book(connection, book_id, new_title):
    connection.execute(
        "UPDATE books SET title = ? WHERE id = ?",
        (new_title, book_id)
    )
    connection.commit()

def delete_book(connection, book_id):
    connection.execute(
        "DELETE FROM books WHERE id = ?",
        (book_id,)
    )
    connection.commit()

if __name__ == "__main__":
    connection = connect()
    create_table(connection)

    add_book(connection, "Book One")
    add_book(connection, "Book Two")

    get_all_books(connection)

    update_book(connection, 1, "Updated Book One")

    delete_book(connection, 2)

    get_all_books(connection)

    connection.close()
