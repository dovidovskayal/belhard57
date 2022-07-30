from CRUD.engine import create_session

class CRUDRole:

    @staticmethod
    @create_session
    def add(name: str, cur = None, conn = None) -> None:
        cur.execute("""
            INSERT INTO roles(name)
            VALUES(?);
        
        """, (name, ))
        conn.commit()

    @staticmethod
    @create_session
    def get(role_id: int, cur = None, conn = None) -> tuple:
        cur.execute("""
            SELECT * FROM roles
            WHERE id = ?;
        
        """, (role_id, ))
        return cur.fetchone()

    @staticmethod
    @create_session
    def deleter(name: str, role_id: int, cur = None, conn = None) -> None:
        cur.execute("""
            DELETE FROM roles
            WHERE id = ? OR name = ?;
        
        """,(role_id, name))
        conn.commit()

    @staticmethod
    @create_session
    def updater(name: str, role_id: int, cur = None, conn = None) -> None:
        cur.execute("""
            UPDATE roles SET name = ?
            WHERE id = ?;
        
        """,(name, role_id))
        conn.commit()

    @staticmethod
    @create_session
    def get_all(cur = None, conn = None) -> tuple:
        cur.execute("""
            SELECT * FROM roles;
        
        """)
        return cur.fetchall()
