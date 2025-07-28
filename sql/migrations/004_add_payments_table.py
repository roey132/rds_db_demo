from yoyo import step

__depends__ = {'001_create_stg_tables'}

steps = [
    step(
        """
        CREATE TABLE IF NOT EXISTS stg_order_payments (
            order_id TEXT,
            payment_sequential INT,
            payment_type TEXT,
            payment_installments INT,
            payment_value NUMERIC
        );
        """,
        """
        DROP TABLE IF EXISTS stg_order_payments;
        """
    )
]
