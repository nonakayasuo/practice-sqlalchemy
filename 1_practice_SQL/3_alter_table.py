import os
import sqlite3

main_path = os.path.dirname(os.path.abspath(__file__)) # 絶対パス
os.chdir(main_path) # 絶対パスに移動
dbname = "test.db" # データベースを設定
conn = sqlite3.connect(dbname) # データベースに接続
cur = conn.cursor() # SQLiteを操作
query = "ALTER TABLE customers ADD customer_unit_quantity INTGER"
cur.execute(query) # クエリを実行
conn.commit() # トランザクションの結果を確定
conn.close() # 接続を切断