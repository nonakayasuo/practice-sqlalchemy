from sqlalchemy.sql import update
from models import engine, customers
import pandas as pd

conn = engine.connect()
query = (
    update(customers)
    .where(customers.c.customer_id == "2")
    .values(customer_name="顧客B", customer_unit_price=3000)
)

conn.execute(query)

query = "SELECT * FROM customers"
df = pd.read_sql(query, conn)
print(df)

conn.close()
