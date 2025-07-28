import os
from dotenv import load_dotenv
from yoyo import read_migrations, get_backend

load_dotenv(".env")

print(os.getenv("DB_USER"))
print(os.getenv("DB_PASSWORD"))
print(os.getenv("DB_HOST"))
print(os.getenv("DB_PORT"))
print(os.getenv("DB_NAME"))

backend = get_backend(
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

migrations = read_migrations("sql/migrations/")
print(migrations)
with backend.lock():
    backend.apply_migrations(backend.to_apply(migrations))
