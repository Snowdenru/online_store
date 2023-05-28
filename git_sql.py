import sqlite3

conn = sqlite3.connect('Github\online_store\products.db')

cursor = conn.cursor()
cursor.execute("""
                CREATE TABLE if not exists Products(
                    id integer PRIMARY KEY,
                    name text,
                    price integer,
                    quantity integer,
                    id_status integer,
                    id_category integer,
                    FOREIGN KEY(id_category) REFERENCES Category(id),
                    FOREIGN KEY(id_status) REFERENCES Status(id)
                    )""")
conn.commit()

cursor.execute("""
               CREATE TABLE if not exists Category(
                   id integer PRIMARY KEY,
                   category text
                   ) """)
conn.commit()

cursor.execute("""
               CREATE TABLE if not exists Status(
                   id integer PRIMARY KEY,
                   status text
                   ) """)
conn.commit()

conn.close()
