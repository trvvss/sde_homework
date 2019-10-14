import sqlite3
import csv


def create_tables(connection, cursor):
    sql_command = """
        DROP TABLE IF EXISTS users;
        DROP TABLE IF EXISTS books;
        DROP TABLE IF EXISTS authors;
        DROP TABLE IF EXISTS wishlists;
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            email TEXT UNIQUE,
            password TEXT
        );
        CREATE TABLE books (
            id INTEGER PRIMARY KEY,
            author_id INTEGER,
            title TEXT UNIQUE,
            isbn INTEGER UNIQUE, 
            year_published INTEGER,
            FOREIGN KEY (author_id) REFERENCES authors(id)
        );
        CREATE TABLE authors (
            id INTEGER PRIMARY KEY, 
            first_name TEXT,
            last_name TEXT
        );
        CREATE TABLE wishlists (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            book_id INTEGER,
            last_updated INTEGER,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (book_id) REFERENCES books(id)
        )
    """
    cursor.executescript(sql_command)
    connection.commit()



def populate_tables(connection, cursor):

    # I read that string constructors are bad practice, because they create vulnerabilites to SQL
    # injection attacks. I'd like to learn if there's any way to use variables for new table names.

    with open('users.csv','r') as f:
        dr = csv.DictReader(f)
        to_users_table = [(i['first_name'], i['last_name'], i['email'], i['password']) for i in dr]
    cursor.executemany("INSERT INTO users (first_name, last_name, email, password) VALUES (?, ?, ?, ?);", to_users_table)
    
    with open('authors.csv','r') as f:
        dr = csv.DictReader(f)
        to_authors_table = [(i['first_name'], i['last_name']) for i in dr]
    cursor.executemany("INSERT INTO authors (first_name, last_name) VALUES (?, ?);", to_authors_table)
    
    with open('books.csv','r') as f:
        dr = csv.DictReader(f)
        to_books_table = [(i['author_id'], i['title'], i['isbn'], i['year_published']) for i in dr]
    cursor.executemany("INSERT INTO books (author_id, title, isbn, year_published) VALUES (?, ?, ?, ?);", to_books_table)
    
    with open('wishlists.csv','r') as f:
        dr = csv.DictReader(f)
        to_wishlists_table = [(i['user_id'], i['book_id'], i['last_updated']) for i in dr]
    cursor.executemany("INSERT INTO wishlists (user_id, book_id, last_updated) VALUES (?, ?, ?);", to_wishlists_table)
    
    connection.commit()


def main():
    conn = sqlite3.connect('book_wishlists.db')
    c = conn.cursor()
    create_tables(conn, c)
    populate_tables(conn, c)
    conn.close()


if __name__ == "__main__":
    main()
