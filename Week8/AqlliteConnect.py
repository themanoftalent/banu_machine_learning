# create an sqlite3 database and connect to it that resides in localhost
# and create a table called "users" with 3 columns: "username", "password", "email"
# insert 3 rows of data
# update the password of the user "admin"
# delete the user "guest"
# select all data from the table "users" and display the results line by line

import sqlite3
from sqlite3 import Error


def sql_connection():
    try:
        con = sqlite3.connect('localhost')
        return con
    except Error:
        print(Error)


def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE users(username text, password text, email text)")
    con.commit()


def sql_insert(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO users(username, password, email) VALUES(?, ?, ?)', entities)
    con.commit()


def sql_update(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute('UPDATE users SET password=? WHERE username=?', entities)
    con.commit()


def sql_delete(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute('DELETE FROM users WHERE username=?', entities)
    con.commit()


def sql_fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM users')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)


try:
    con = sql_connection()
    sql_table(con)
    sql_insert(con, ('admin', 'admin', 'admin@localhost'))
    sql_insert(con, ('guest', 'guest', 'guest@localhost'))
    sql_insert(con, ('user', 'user', 'user@localhost'))
    sql_update(con, ('admin123', 'admin'))
    sql_delete(con, ('guest',))
    sql_fetch(con)
except Error:
    print(Error)



# Output:
