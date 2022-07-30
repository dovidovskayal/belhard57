import sqlite3
from CRUD.category import CRUDCategory
from CRUD.article import CRUDArticle
from CRUD.user import CRUDUser
from CRUD.role import CRUDRole

conn = sqlite3.connect("db.db")
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS categories(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    );
""")
cur.execute("""
    CREATE TABLE IF NOT EXISTS roles(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    );
""")
cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        login TEXT UNIQUE NOT NULL,
        password TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        role_id INTEGER NOT NULL,
        FOREIGN KEY (role_id) REFERENCES roles(id)
    );
""")
cur.execute("""
    CREATE TABLE IF NOT EXISTS articles(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        body TEXT UNIQUE NOT NULL,
        category_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (category_id) REFERENCES categories(id),
        FOREIGN KEY (user_id) REFERENCES users(id)
    );
""")
conn.commit()
#CRUDRole.add(name = "user")
#CRUDUser.add(login = "vasya", password = '39fghef', email = 'vasya@gmail.com', role_id = 1)
print(CRUDCategory.get(category_id = 1))
#CRUDArticle.add(title = "bread", body = "morning", category_id = 1, user_id = 1)
