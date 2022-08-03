import psycopg2


def create_session(func):
    def wrapper(**kwargs):
        conn = psycopg2.connect('postgresql://liana:belhard@localhost:5432/bh57')
        cur = conn.cursor()
        return func(**kwargs, cur = cur, conn = conn)
    return wrapper

@create_session
def create_table(cur = None, conn = None):
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS categories(
        id INTEGER PRIMARY KEY,
        name VARCHAR(24)
        );
        
        """
    )
    conn.commit()
create_table()
