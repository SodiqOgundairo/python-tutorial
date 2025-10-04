import sqlite3


class Person:
    def __init__(self, id_number=-1, first="", last="", age=-1):
        self.id_number = id_number
        self.first = first
        self.last = last
        self.age = age
        self.conn = sqlite3.connect('mydata.db')
        self.cursor = self.conn.cursor()

    def load_person(self, id_number):
        self.cursor.execute(f"""
               SELECT * FROM persons
               WHERE id = {id_number}
               """)

        results = self.cursor.fetchone()

        self.id_number = id_number
        self.first = results[1]
        self.last = results[2]
        self.age = results[3]


# conn = sqlite3.connect('mydata.db')
# cursor = conn.cursor()

# cursor.execute("""
#                CREATE TABLE IF NOT EXISTS persons (
#                    id INTEGER PRIMARY KEY,
#                    first_name TEXT,
#                    last_name TEXT,
#                    age INTEGER
#                )
#                """)

# cursor.execute("""
#                INSERT INTO persons VALUES
#                (1, 'Yemi', 'Ogundairo', 31),
#                (2, 'Tolu', 'Oguntimehin', 30),
#                (3, 'Ayobami', 'Ogunjobi', 28)
#                 """)


# cursor.execute("""
#                SELECT * FROM persons
#                WHERE last_name = 'Ogundairo'
#                """)

# rows = cursor.fetchall()
# print(rows)
# conn.commit()

# conn.close()


    def insert_person(self):
        self.cursor.execute(f"""
                INSERT INTO persons VALUES
                ({self.id_number}, '{self.first}', '{self.last}', {self.age})
                """)
        self.conn.commit()
        self.conn.close()


p1 = Person()
p1.load_person(1)
print(p1.first)
print(p1.last)
print(p1.age)
print(p1.id_number)


# p2 = Person(7, 'Teewhy', 'Alex', 30)
# p2.insert_person()

p1.load_person(3)
print(p1.last)
