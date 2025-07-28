-- Truncate in dependency-safe order
TRUNCATE TABLE
    fact_order_items,
    fact_orders,
    dim_product,
    dim_seller,
    dim_customer,
    dim_date
CASCADE;
