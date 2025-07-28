from yoyo import step

__depends__ = {'002_create_dwh_tables'}

steps = [
    step(
        """
        CREATE INDEX IF NOT EXISTS idx_fact_orders_customer_id
            ON fact_orders (customer_id);

        CREATE INDEX IF NOT EXISTS idx_fact_order_items_product_id
            ON fact_order_items (product_id);

        CREATE INDEX IF NOT EXISTS idx_fact_order_items_seller_id
            ON fact_order_items (seller_id);

        CREATE INDEX IF NOT EXISTS idx_dim_customer_state
            ON dim_customer (customer_state);

        CREATE INDEX IF NOT EXISTS idx_dim_seller_state
            ON dim_seller (seller_state);

        CREATE INDEX IF NOT EXISTS idx_fact_orders_purchase_date
            ON fact_orders (order_purchase_timestamp);

        CREATE INDEX IF NOT EXISTS idx_fact_order_items_shipping_date
            ON fact_order_items (shipping_limit_date);
        """,
        """
        DROP INDEX IF EXISTS idx_fact_order_items_shipping_date;
        DROP INDEX IF EXISTS idx_fact_orders_purchase_date;
        DROP INDEX IF EXISTS idx_dim_seller_state;
        DROP INDEX IF EXISTS idx_dim_customer_state;
        DROP INDEX IF EXISTS idx_fact_order_items_seller_id;
        DROP INDEX IF EXISTS idx_fact_order_items_product_id;
        DROP INDEX IF EXISTS idx_fact_orders_customer_id;
        """
    )
]
