import sqlite3

def create_table(connection):
    connection.execute("DROP TABLE IF EXISTS books")
    connection.execute("""
    
    CREATE TABLE books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    author TEXT,
    publication_year INTEGER,
    genre TEXT,
    number_of_pages INTEGER,
    number_of_copies INTEGER
    )
    """)
    connection.commit()

def add_books(connection,id,name,author,publication_year,genre,number_of_pages,number_of_copies):
    connection.execute(
        "INSERT INTO books (id,name,author,publication_year,genre,number_of_pages,number_of_copies) VALUES (?,?,?,?,?,?,?)",
     (id,name,author,publication_year,genre,number_of_pages,number_of_copies)
    )
    connection.commit()

if __name__ == "__main__":
    connection = sqlite3.connect("database.db")

    create_table(connection)
    add_books(connection,7,'Harry Potter','J.K. Rowling','1997','fantasy','358','120 million')
    connection.close()