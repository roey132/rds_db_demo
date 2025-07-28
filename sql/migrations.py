import os
from dotenv import load_dotenv
from yoyo import read_migrations, get_backend

load_dotenv(".env")

backend = get_backend(
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

migrations = read_migrations("migrations/")
with backend.lock():
    backend.apply_migrations(backend.to_apply(migrations))
