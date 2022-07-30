import sqlite3


def create_session(func):
    def wrapper(**kwargs):
        conn = sqlite3.connect('/Users/liana/PycharmProjects/belhard57/db.db')
        cur = conn.cursor()
        return func(**kwargs, cur = cur, conn = conn)
    return wrapper
