import json 
import sqlite3
from pathlib import Path

#путь к папке
BASE_DIR = Path(__file__).resolve().parent
JSON_FILE = BASE_DIR / "games.json"
#путь к новой бэйз 
DATABASE_FILE = BASE_DIR / "games.db"

#создаем бэйз хехе
def create_database():
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

#таблица для games 
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            genre TEXT NOT NULL,
            rating INTEGER NOT NULL CHECK(rating BETWEEN 0 AND 10),
            status TEXT NOT NULL,
            description TEXT NOT NULL,
            image TEXT NOT NULL
        )
        """
    )


#сохраняем изменения 
    connection.commit()
    connection.close()

def migrate_games():
    if not JSON_FILE.exists():
        print("games.json не найден")
        return
    with JSON_FILE.open(
        "r",
        encoding="utf-8"
    ) as file:
        games = json.load(file)

    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()

   #считаем сколько игр уже находится в базе
    count = cursor.execute(
    "SELECT COUNT(*) FROM games"
).fetchone()[0]
#если игра есть, то не добовляем 
    if count > 0:
        print("Игра уже есть в базе")
        connection.close()
        return
#перебераем игры из json
    for game in games:
        cursor.execute(
            """ 
            INSERT INTO games (
            name,
            genre,
            rating,
            status,
            description,
            image
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                game["name"],
                game["genre"],
                game["rating"],
                game["status"],
                game["description"],
                game["image"]
            )
        )
    connection.commit()
    connection.close()
    print("Игры успешно перенесены")

if __name__ == "__main__":
    create_database()
    migrate_games()
