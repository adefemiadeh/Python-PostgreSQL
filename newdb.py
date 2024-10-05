import psycopg2
from psycopg2 import OperationalError

# DB CONNECTION

try:
    conn = psycopg2.connect(
        host='localhost',
        dbname='postgres',
        user='postgres',
        password='',
        port=5432
    )

    print('Database run Successfully')

except OperationalError as e:
    print(f'DB not connect due to {e}')

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS school(
            id INT PRIMARY KEY,
            name VARCHAR(255),
            year INT,
            gender CHAR
            );
""")

cur.execute("""INSERT INTO school(id,name,year,gender) VALUES
            (1,'John',2013,'m'),
            (2,'Kemi',2016,'f'),
            (3,'Smith',2007,'m'),
            (4,'Kate',2015,'f')
""")

cur.execute("""SELECT * FROM school WHERE name = 'John'; 
""")
print(cur.fetchone())

cur.execute("""
            SELECT *
            FROM school
            WHERE year < 2013;
""")
for row in cur.fetchall():
      print (row)
conn.commit()

cur.close()
conn.close()