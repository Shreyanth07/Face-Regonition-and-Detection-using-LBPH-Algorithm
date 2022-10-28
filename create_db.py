

import sqlite3

#creates a database with name usersdatabase.db
conn=sqlite3.connect('usersdatabase.db')

c=conn.cursor()

sql="""
    DROP TABLE IF EXISTS users;
    CREATE TABLE users (
            id integer unique primary key autoincrement,
            name text);
    """
# users table with two columns, id and name.
# use DB Browser for sqlite to view the database.
c.executescript(sql)

conn.commit()

conn.close()
