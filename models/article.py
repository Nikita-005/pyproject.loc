from services.db import Db

class Article:
    __tablename__ = 'articles'
    id = None
    author_id = None
    name = None
    text = None
    create_at = None

    def find_all(cls):
        db = Db()
        return db.query("SELECT * FROM 'articles'", {}, cls)

    def get_by_id(id, cls):
        db = Db()
        return db.query(f"SELECT * FROM 'articles' WHERE id = {id}", {}, cls)[0]
