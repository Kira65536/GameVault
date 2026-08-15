GameVault

GameVault - это веб-приложение для собственной коллекции игр.  Пользователи могут регистрироваться, входить в аккаунт и изменять только свою коллекцию. 

Ссылка на сайт: https://gamevault-1-dt2g.onrender.com

Технологии: 
- Python
- Flask
- PostgreSQL
- Neon
- Supabase Storage
- HTML
- CSS
- Jinja2
- Gunicorn
- Render
- Git
- GitHub

Возможности: 
- Регистрация 
- Авторизация и выход из аккаунта  
- Личная коллекция для каждого пользователя 
- Добавление игр 
- Редактирование 
- Удаление 
- Загрузка обложек 
- Поиск по названию
- Фильтрация статуса 
- Сортировка по рейтингу, названию и дате добавления 
- Адаптация под телефон 
- Статистика коллекции 

Хранение данных:

Пользователи и игры хранятся в PostgreSQL
Обложки игр хранятся в Supabase Storage

Безопасность:

- Пароли хранятся в виде хешей
- Каждый пользователь имеет доступ только к своим играм
- Секретные ключи хранятся в переменных окружения
- .env не загружается в GitHub

Запуск локально:

bash
git clone https://github.com/Kira65536/GameVault.git
cd GameVault
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py

Для запуска необходимо создать .env с переменными:

env
DATABASE_URL=
SECRET_KEY=
SUPABASE_URL=
SUPABASE_SECRET_KEY=
