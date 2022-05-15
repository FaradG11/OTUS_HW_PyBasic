from sqlalchemy.orm import Session as SessionType
from .db_setup import Base, Productdb, Session, logger
from .schemas import ProductIn, Product


# Dependency for Session closing
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


def create_table():
    Base.metadata.create_all()
    logger.info("Table created")


def query_all_product(session: SessionType) -> list[Productdb]:
    products = session.query(Productdb).all()
    return products


def new_income(session: SessionType, product_in: ProductIn):
    product_db = session.query(Productdb).filter_by(name=product_in.name).one_or_none()
    if product_db:
        logger.info('trying to add amount..')
        product_db.add_amount(product_in.amount)

    else:
        product_db = Productdb(name=product_in.name, amount=product_in.amount)
        session.add(product_db)
        logger.info('Add new product..')
    session.commit()
    product = Product(id=product_db.id, name=product_in.name, amount=product_in.amount)
    session.close()
    return product


