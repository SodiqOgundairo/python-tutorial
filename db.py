import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')
c.close()
conn.commit()
conn.close()