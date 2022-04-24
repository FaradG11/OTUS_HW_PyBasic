from sqlalchemy import (
    create_engine,
    MetaData,
    Column,
    Integer,
    String,
)

from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    scoped_session
)

DB_NAME = "product-01.db"
DB_URL = "sqlite:///"+DB_NAME
metadata = MetaData()
engine = create_engine(url=DB_URL)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


class Base:
    id = Column(Integer, primary_key=True)


Base = declarative_base(bind=engine, cls=Base)


class Productdb(Base):
    __tablename__ = "product"

    pname = Column(String(20), unique=True)
    amount = Column(Integer)

    def add_amount(self, amount):
        self.amount += amount

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id},"
            f"product={self.pname!r},"
            f"amount={self.amount}"
            ")"
        )

    def __repr__(self):
        return str(self)


