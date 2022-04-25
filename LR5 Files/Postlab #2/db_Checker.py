import sqlite3
conn = sqlite3.connect('Solmaris.db')
query = "SELECT * FROM PROPERTY"
cursor = conn.execute(query)

for row in cursor:
    print(row)