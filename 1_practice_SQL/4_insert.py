import os
import sqlite3
main_path = os.path.dirname(os.path.abspath(__file__)) # 絶対パス
os.chdir(main_path) # 絶対パスに移動
dbname = "test.db"  # データベースを設定
conn = sqlite3.connect(dbname) # データベースに接続
cur = conn.cursor() # SQLiteを操作
query = "INSERT INTO customers(customer_name,customer_unit_price) VALUES('顧客A',1000)"  # customer_name、customer_unit_price列を追加
cur.execute(query) # クエリを実行
conn.commit() # トランザクションの結果を確定
conn.close() # 接続を切断