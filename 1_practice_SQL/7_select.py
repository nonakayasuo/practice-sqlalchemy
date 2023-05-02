import sqlite3
import os

main_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(main_path)

dbname = "test.db"
conn = sqlite3.connect(dbname)
cur = conn.cursor()

query = "SELECT customer_id, customer_name, customer_unit_price FROM customers WHERE customer_name='顧客A'"

cur.execute(query)
print(cur.fetchall())
# print(cur.fetchone())
# print(cur.fetchmany(3))
conn.commit()
conn.close()