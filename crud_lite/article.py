from crud_lite.engine import create_session

class CRUDArticle:

    @staticmethod
    @create_session
    def add(
            title: str,
            body: str,
            category_id: int,
            user_id: int,
            cur=None,
            conn=None) -> None:
        cur.execute("""
                INSERT INTO articles(title, body, category_id, user_id)
                VALUES(?, ?, ?, ?);

            """, (title, body, category_id, user_id))
        conn.commit()

    @staticmethod
    @create_session
    def get(article_id: int, cur=None, conn=None) -> tuple:
        cur.execute("""
                    SELECT * FROM articles
                    WHERE id = ?;
                """, (article_id,))
        return cur.fetchone()

    @staticmethod
    @create_session
    def deleter(
            article_id: int,
            cur=None,
            conn=None) -> None:
        cur.execute("""
                    DELETE FROM articles
                    WHERE id = ?;      
                """, (article_id,))
        conn.commit()

    @staticmethod
    @create_session
    def updater(
            title: str,
            body: str,
            category_id: str,
            user_id: int,
            artical_id: int,
            cur=None,
            conn=None) -> None:
        cur.execute("""
                        UPDATE articles SET (title, body, category_id, user_id) = (?, ?, ?, ?)
                        WHERE id = ?;    
                    """, (title, body, category_id, user_id, artical_id))
        conn.commit()

    @staticmethod
    @create_session
    def get_all(cur=None, conn=None) -> tuple:
        cur.execute("""
                    SELECT * FROM articles;    
                        """)
        return cur.fetchall()
