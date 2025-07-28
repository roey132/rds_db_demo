import os
import psycopg2
from dotenv import load_dotenv
from pathlib import Path

# === Load environment variables ===
load_dotenv(".env")

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT", 5432)

# === Connect to PostgreSQL ===
conn = psycopg2.connect(
    host=DB_HOST,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    port=DB_PORT
)
cursor = conn.cursor()

# === CSV to staging table mapping ===
CSV_DIR = Path("data")
csv_to_table = {
    "olist_orders_dataset.csv": "stg_orders",
    "olist_customers_dataset.csv": "stg_customers",
    "olist_order_items_dataset.csv": "stg_order_items",
    "olist_products_dataset.csv": "stg_products",
    "olist_sellers_dataset.csv": "stg_sellers",
    "olist_order_reviews_dataset.csv": "stg_reviews",
    "olist_geolocation_dataset.csv": "stg_geolocation",
    "product_category_name_translation.csv": "stg_category_translation",
    "olist_order_payments_dataset.csv": "stg_order_payments"
}

# === Truncate all staging tables before load ===
tables_to_truncate = list(csv_to_table.values())

print("Truncating staging tables...")
for table in tables_to_truncate:
    try:
        cursor.execute(f"TRUNCATE TABLE {table};")
        print(f"   - {table} truncated")
    except Exception as e:
        print(f"Failed to truncate {table}: {e}")
conn.commit()

print("✅ All staging tables truncated.\n")
# === Load CSVs into staging tables ===
for csv_file, table in csv_to_table.items():
    file_path = CSV_DIR / csv_file
    if not file_path.exists():
        print(f"File not found: {file_path}")
        continue

    print(f"Loading {csv_file} into {table}...")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            cursor.copy_expert(
                f"COPY {table} FROM STDIN WITH CSV HEADER DELIMITER ','",
                f
            )
        conn.commit()
        print(f"Successfully loaded {csv_file} into {table}")
    except Exception as e:
        conn.rollback()
        print(f"Failed to load {csv_file} into {table}: {e}")

# === Clean up ===
cursor.close()
conn.close()
print("All staging tables processed.")
