import os
import psycopg2
from pathlib import Path
from dotenv import load_dotenv

# === Load environment ===
load_dotenv(".env")

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT", 5432)
)
cursor = conn.cursor()

# === Transformation SQL files ===
sql_dir = Path("sql/transforms")
sql_files = [
    "truncate_all_dims_and_facts.sql",
    "insert_dim_customer.sql",
    "insert_dim_seller.sql",
    "insert_dim_product.sql",
    "insert_dim_date.sql",
    "insert_fact_orders.sql",
    "insert_fact_order_items.sql"
]

# === Execute each transformation ===
for file_name in sql_files:
    sql_path = sql_dir / file_name
    print(f"Executing {file_name}...")
    with open(sql_path, "r", encoding="utf-8") as f:
        sql = f.read()
    try:
        cursor.execute(sql)
        conn.commit()
        print(f"{file_name} executed successfully\n")
    except Exception as e:
        conn.rollback()
        print(f"Error in {file_name}: {e}\n")

# === Cleanup ===
cursor.close()
conn.close()
print("DWH load complete.")
