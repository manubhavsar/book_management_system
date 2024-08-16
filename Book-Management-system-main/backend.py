import sqlite3

def connect():
    """
    It creates a database called books.db and creates a table called books.
    """
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY AUTOINCREMENT, title text,author text,year integer,price integer)")
    conn.commit()
    conn.close()

def insert(title, author, year,price):
    """
    It takes in 4 parameters (title, author, year, price) and inserts them into the database
    """
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO books VALUES(NULL,?,?,?,?)",(title,author,year,price))
    conn.commit()
    conn.close()

def view():
    """
    It connects to the database, fetches all the items in db, closes the connection, and
    returns the results.
    """
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM books")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",price=""):
    """
    It requires atleast one parameter to be passed in. It connects to the database, fetches all the items in db with particular search criteria, closes the connection, and returns the results.
    """
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR price=?",(title,author,year,price))
    rows=cur.fetchall()
    conn.close()
    return rows


    
def delete(id):
    """
    It takes the id of the book as an argument and deletes the book from the database
    """
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM books WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,price):
    """
    It takes the id of the book, and the new values for the title, author, year, and price, and updates
    the database with the new values
    """
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE books SET title=?, author=?, year=?, price=? WHERE id=?",(title,author,year,price,id))
    conn.commit()
    conn.close()

connect()
