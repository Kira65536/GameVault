import sqlite3
from pathlib import Path

BASE_DIR=Path(__file__).resolve().parent
DATABASE_FILE=BASE_DIR/"games.db"

username=input("Введите имя вашего аккаунта: ").strip()

db=sqlite3.connect(DATABASE_FILE)
db.row_factory=sqlite3.Row

user=db.execute(
    "SELECT id FROM users WHERE username=?",
    (username,)
).fetchone()

if user is None:
    print("Такого пользователя нет")
else:
    cursor=db.execute(
        """
        UPDATE games
        SET user_id=?
        WHERE user_id IS NULL
        """,
        (user["id"],)
    )

    db.commit()

    print(f"Привязано игр: {cursor.rowcount}")

db.close()
