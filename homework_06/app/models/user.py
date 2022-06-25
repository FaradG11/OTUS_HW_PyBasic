from sqlalchemy import Column, String, Integer

from .database import db


class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True)
    name = Column(String(30))
    email = Column(String(40))

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.name!r}>"
