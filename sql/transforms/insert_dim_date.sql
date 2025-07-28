INSERT INTO dim_date (
    date_id,
    year,
    month,
    day,
    day_of_week
)
SELECT DISTINCT
    order_purchase_timestamp::date AS date_id,
    EXTRACT(YEAR FROM order_purchase_timestamp),
    EXTRACT(MONTH FROM order_purchase_timestamp),
    EXTRACT(DAY FROM order_purchase_timestamp),
    TO_CHAR(order_purchase_timestamp, 'Day')
FROM stg_orders
WHERE order_purchase_timestamp IS NOT NULL;
