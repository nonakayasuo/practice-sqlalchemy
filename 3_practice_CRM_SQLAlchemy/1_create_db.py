from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    MetaData,
    create_engine,
    ForeignKey,
    DateTime,
)
import os

main_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(main_path)

engine = create_engine(
    "sqlite:///test.db", echo=True
)  # 接続するデータベース用エンジンを作成 echo = True にしておくと 発行されるSQLがログで出力される
meta = MetaData(engine)

# customersテーブルを定義
customers = Table(
    "customers",
    meta,
    Column("customer_id", String, primary_key=True),
    Column("customer_name", String),
    Column("customer_unit_price", Integer),
)

# itemsテーブルを定義
items = Table(
    "items",
    meta,
    Column("item_id", String, primary_key=True),
    Column("item_name", String),
    Column("item_price", Integer),
)

# purchasesテーブルを定義
purchases = Table(
    "purchases",
    meta,
    Column("purchase_id", Integer, primary_key=True, autoincrement=True),
    Column("item_id", String, ForeignKey("customers.customer_id")),
    Column("date", DateTime),
)

# purchase_detailsテーブルを定義
purchase_details = Table(
    "purchases_details",
    meta,
    Column(
        "purchase_id",
        Integer,
        ForeignKey("purchases.purchase_id"),
        primary_key=True,
    ),
    Column("item_id", String, ForeignKey("items.item_id"), primary_key=True),
    Column("item_quantity", Integer),
)


meta.create_all()  # テーブルを一括で作成
