import sqlite3

conn = sqlite3.connect('database/users.db')
c = conn.cursor()
c.execute('''
          CREATE TABLE user
          (id INTEGER PRIMARY KEY,
          email TEXT NOT NULL UNIQUE,
          password TEXT NOT NULL)
          ''')
conn.commit()
conn.close()
