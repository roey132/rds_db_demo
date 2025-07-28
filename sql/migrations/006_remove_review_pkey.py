from yoyo import step

__depends__ = {'005_create_payments_index'}

steps = [
    step(
        # UP: Drop primary key and add index
        """
        ALTER TABLE stg_reviews DROP CONSTRAINT IF EXISTS stg_reviews_pkey;

        CREATE INDEX IF NOT EXISTS idx_stg_reviews_order_id
        ON stg_reviews (order_id);
        """,
        # DOWN: Remove index and re-add primary key (not recommended in prod)
        """
        DROP INDEX IF EXISTS idx_stg_reviews_order_id;

        ALTER TABLE stg_reviews
        ADD CONSTRAINT stg_reviews_pkey PRIMARY KEY (review_id);
        """
    )
]
