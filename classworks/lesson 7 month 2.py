import sqlite3

def create_tables(connection):
    connection.execute("""
    CREATE TABLE IF NOT EXISTS students (
        name TEXT,
        age INTEGER,
        city TEXT
    )
    """)
    connection.commit()
#последний таблица (с этом случае city) запятая не пишется
def add_students(connection, name, age, city):
    connection.execute("""
    INSERT INTO students (name, age, city)
    VALUES (?, ?, ?)
    """, (name, age, city))
    connection.commit()

if __name__ == '__main__':
    conn = sqlite3.connect('database.db')

    create_tables(conn)
    add_students(conn, 'Alina', 16, 'Bishkek')
    add_students(conn, 'Abakir',15,'Bishkek')