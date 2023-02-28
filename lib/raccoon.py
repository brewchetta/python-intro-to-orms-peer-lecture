from . import CONN
from . import CURSOR

class Raccoon:
    def __init__(self, name, trashcan):
        self.id = None
        self.name = name
        self.trashcan = trashcan

    def __repr__(self):
        return f'<Raccoon id={self.id} name={self.name} trashcan={self.trashcan} >'

    @classmethod
    def create_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS raccoons (
                id INTEGER PRIMARY KEY,
                name TEXT,
                trashcan TEXT
            )
        """

        CURSOR.execute(sql)

    @classmethod
    def all(cls):
        sql = """
            SELECT * FROM raccoons
        """

        raccoons = CURSOR.execute(sql)
        all = []
        for row in raccoons:
            song = cls(row[1], row[2])
            song.id = row[0]
            all.append(song)

        return all

    def save(self):
        sql = """
            INSERT INTO raccoons (name, trashcan) VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.trashcan))
        CONN.commit()

        self.id = CURSOR.execute("SELECT * FROM raccoons DESC LIMIT 1").fetchone()[0]
