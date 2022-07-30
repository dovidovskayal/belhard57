from CRUD.engine import create_session

class CRUDUser:

    @staticmethod
    @create_session
    def add(
            login: str,
            password: str,
            email: str,
            role_id: int,
            cur = None,
            conn = None) -> None:
        cur.execute("""
            INSERT INTO users(login, password, email, role_id)
            VALUES(?, ?, ?, ?);
        
        """, (login, password, email, role_id))
        conn.commit()

    @staticmethod
    @create_session
    def get(user_id: int, cur = None, conn = None) -> tuple:
        cur.execute("""
                SELECT * FROM users
                WHERE id = ?;
            """, (user_id,))
        return cur.fetchone()

    @staticmethod
    @create_session
    def deleter(
            user_id: int,
            cur = None,
            conn = None) -> tuple:
        cur.execute("""
                DELETE FROM users
                WHERE id = ?;      
            """, (user_id, ))
        conn.commit()

    @staticmethod
    @create_session
    def updater(
            user_id: int,
            login: str,
            password: str,
            email:str,
            role_id: int,
            cur = None,
            conn = None) -> None:
        cur.execute("""
                    UPDATE users SET (login, password, email, role_id) = (?, ?, ?, ?)
                    WHERE id = ?;    
                """, (login, password, email, role_id, user_id))
        conn.commit()

    @staticmethod
    @create_session
    def get_all(cur = None, conn = None) -> tuple:
        cur.execute("""
                SELECT * FROM users;    
                    """)
        return cur.fetchall()
