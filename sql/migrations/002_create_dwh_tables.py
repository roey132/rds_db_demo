from yoyo import step

__depends__ = {'001_create_stg_tables'}

steps = [
    step(
        """
        CREATE TABLE IF NOT EXISTS dim_customer (
            customer_id TEXT PRIMARY KEY,
            customer_unique_id TEXT,
            customer_zip_code_prefix TEXT,
            customer_city TEXT,
            customer_state TEXT
        );

        CREATE TABLE IF NOT EXISTS dim_seller (
            seller_id TEXT PRIMARY KEY,
            seller_zip_code_prefix TEXT,
            seller_city TEXT,
            seller_state TEXT
        );

        CREATE TABLE IF NOT EXISTS dim_product (
            product_id TEXT PRIMARY KEY,
            product_category_name TEXT,
            product_name_length INT,
            product_description_length INT,
            product_photos_qty INT,
            product_weight_g INT,
            product_length_cm INT,
            product_height_cm INT,
            product_width_cm INT
        );

        CREATE TABLE IF NOT EXISTS dim_date (
            date_id DATE PRIMARY KEY,
            year INT,
            month INT,
            day INT,
            day_of_week TEXT
        );

        CREATE TABLE IF NOT EXISTS fact_orders (
            order_id TEXT PRIMARY KEY,
            customer_id TEXT REFERENCES dim_customer(customer_id),
            order_status TEXT,
            order_purchase_timestamp TIMESTAMP,
            order_approved_at TIMESTAMP,
            order_delivered_carrier_date TIMESTAMP,
            order_delivered_customer_date TIMESTAMP,
            order_estimated_delivery_date TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS fact_order_items (
            order_id TEXT REFERENCES fact_orders(order_id),
            order_item_id INT,
            product_id TEXT REFERENCES dim_product(product_id),
            seller_id TEXT REFERENCES dim_seller(seller_id),
            shipping_limit_date TIMESTAMP,
            price NUMERIC,
            freight_value NUMERIC,
            PRIMARY KEY (order_id, order_item_id)
        );
        """,
        """
        DROP TABLE IF EXISTS fact_order_items;
        DROP TABLE IF EXISTS fact_orders;
        DROP TABLE IF EXISTS dim_date;
        DROP TABLE IF EXISTS dim_product;
        DROP TABLE IF EXISTS dim_seller;
        DROP TABLE IF EXISTS dim_customer;
        """
    )
]
