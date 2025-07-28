from yoyo import step

__depends__ = {'004_add_payments_table'}

steps = [
    step(
        """
        CREATE INDEX IF NOT EXISTS idx_stg_order_payments_order_id
        ON stg_order_payments (order_id);
        """,
        """
        DROP INDEX IF EXISTS idx_stg_order_payments_order_id;
        """
    )
]
