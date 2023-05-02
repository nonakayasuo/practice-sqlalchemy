from sqlalchemy.sql import insert
from models import engine, customers
import sqlalchemy
import pandas as pd

# customersの値をInsert
customer_values = (
    {
        "customer_id": "1",
        "customer_name": "顧客A",
        "customer_unit_price": 1000,
    },
    {
        "customer_id": "2",
        "customer_name": "顧客B",
        "customer_unit_price": 2000,
    },
)

# Insertする方法1
query = customers.insert().values(customer_values)

# Insertする方法2
query = insert(customers, values=customer_values)

conn = engine.connect()

try:
    result = conn.execute(query)
    if result.is_insert:
        print("insert成功")
        query = "SELECT * FROM customers"
        df = pd.read_sql(query, conn)
        print(df)
except sqlalchemy.exc.IntegrityError:
    print("insert失敗")

conn.close()
