from sqlalchemy.orm import Session as SessionType

from .db_setup import Base, Productdb,Session
from .schemas import ProductIn, Product


def create_table():
    Base.metadata.create_all()
    print('Table created')


def query_all_product() -> list[Productdb]:
    session: SessionType = Session()
    products = session.query(Productdb).all()
    print("received products:", products)
    session.close()
    return products


def new_income(product_in: ProductIn):
    session: SessionType = Session()
    product_db = session.query(Productdb).filter_by(name=product_in.name).one_or_none()
    if product_db:
        print('trying to add amount')
        product_db.add_amount(product_in.amount)

    else:
        product_db = Productdb(name=product_in.name, amount=product_in.amount)
        session.add(product_db)
    session.commit()
    product = Product(id=product_db.id, name=product_in.name, amount=product_in.amount)
    session.close()
    return product


