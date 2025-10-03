import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute("""
          CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)
          """)

c.execute("""
          INSERT INTO users VALUES 
          (1, 'Alice', 30),
            (2, 'Bob', 25),
            (3, 'Charlie', 35)
          """)
c.close()
conn.commit()
conn.close()
