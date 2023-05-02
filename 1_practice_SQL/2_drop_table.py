import sqlite3
import os

main_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(main_path)

dbname = "test.db"
conn = sqlite3.connect(dbname)
cur = conn.cursor()

query = "DROP TABLE customers"

cur.execute(query)
conn.commit()
conn.close()