# create an sql connection to a database that resides in the memory
import sqlite3
from sqlite3 import Error


def sql_connection():
    try:
        con = sqlite3.connect(':memory:')
        return con
    except Error:
        print(Error)

def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")
    con.commit()

def sql_insert(con, entities):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)
    con.commit()

def sql_fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM employees')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)

con = sql_connection()
sql_table(con)
sql_insert(con, (1, 'Andrew', 800, 'IT', 'Tech', '2018-02-06'))
sql_insert(con, (2, 'Ricky', 1500, 'HR', 'Manager', '2017-05-09'))
sql_insert(con, (3, 'Dora', 2000, 'Finance', 'Manager', '2018-10-17'))
sql_insert(con, (4, 'Martha', 800, 'Admin', 'HR', '2018-07-23'))
sql_insert(con, (5, 'John', 800, 'IT', 'Tech', '2018-02-06'))
sql_insert(con, (6, 'Peter', 1500, 'HR', 'Manager', '2017-05-09'))
sql_insert(con, (7, 'Kate', 2000, 'Finance', 'Manager', '2018-10-17'))
sql_insert(con, (8, 'Marta', 800, 'Admin', 'HR', '2018-07-23'))
sql_fetch(con)

