import sqlite3

def create_tables(connection):
    connection.execute(
    """"
    CREATE TABLE students if not exists (
       name TEXT,
       age INTEGER
       city TEXT     
        )
    """)

     def add_students(connection,name,age,city):
         connection.execute("""
         INSERT INTO students 
        """)
        connection.commit()
#последний таблица (с этом случае city) запятая не пишется
if __name__ == '__main__':
    conn = sqlite3.connect('database.db')

    create_tables(conn)