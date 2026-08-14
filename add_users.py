import sqlite3
from pathlib import Path

BASE_DIR=Path(__file__).resolve().parent
DATABASE_FILE=BASE_DIR/"games.db"

db=sqlite3.connect(DATABASE_FILE)
cursor=db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL
)
""")

columns=cursor.execute("PRAGMA table_info(games)").fetchall()
column_names=[column[1] for column in columns]

if "user_id" not in column_names:
    cursor.execute("""
    ALTER TABLE games
    ADD COLUMN user_id INTEGER
    """)

db.commit()
db.close()

print("Таблица users создана")
print("user_id добавлен в games")