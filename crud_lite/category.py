from crud_lite.engine import create_session


class CRUDCategory:

    @staticmethod
    @create_session
    def add(name: str, cur = None, conn = None) -> None:
        cur.execute("""
                INSERT INTO categories(name)
                VALUES(?);       
            """, (name, ))
        conn.commit()

    @staticmethod
    @create_session
    def get(category_id: int, cur: object = None, conn: object = None) -> tuple:
        cur.execute("""
            SELECT * FROM categories
            WHERE id = ?;
        """, (category_id, ))
        return cur.fetchone()

    @staticmethod
    @create_session
    def deleter(name: str, category_id: int, cur: object = None, conn: object = None) -> tuple:
        cur.execute("""
            DELETE FROM categories
            WHERE id = ? OR  name = ?;      
        """, (category_id, name ))
        conn.commit()

    @staticmethod
    @create_session
    def updater(name: str, category_id: int, cur: object = None, conn: object = None) -> tuple:
        cur.execute("""
                UPDATE categories SET name = ?
                WHERE id = ?;      
            """, (name, category_id))
        conn.commit()

    @staticmethod
    @create_session
    def get_all(cur: object = None, conn: object = None) -> tuple:
        cur.execute("""
            SELECT * FROM categories;    
                """)
        return cur.fetchall()





