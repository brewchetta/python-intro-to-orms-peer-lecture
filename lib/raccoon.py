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
    def create_table(cls):
        pass

    @classmethod
    def all(cls):
        pass

    @classmethod
    def find_by_id(cls, id):
        pass

    def save(self):
        pass
