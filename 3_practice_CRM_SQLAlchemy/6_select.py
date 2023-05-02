from models import engine, customers

conn = engine.connect()
query = customers.select()

result = conn.execute(query)
print(result.fetchall())
conn.close()
