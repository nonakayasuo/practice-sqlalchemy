import sqlite3
import os

main_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(main_path)

dbname = "test.db"
conn = sqlite3.connect(dbname)
cur = conn.cursor()

query = "DELETE FROM customers WHERE customer_id=1"
# query = "DELETE FROM items"


cur.execute(query)
conn.commit()
conn.close()