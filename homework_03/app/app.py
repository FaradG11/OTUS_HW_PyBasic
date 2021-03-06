import os.path
from fastapi import FastAPI
from product.api import router as product_router
from product.db_setup import DB_NAME, logger
from product.db_queries import create_table

app = FastAPI()
app.include_router(product_router)

if os.path.exists(DB_NAME):
    logger.info("DB exists")
else:
    create_table()


@app.get("/ping/")
def ping():
    return {"message": "pong"}

@app.get("/")
def root():
    return {"message": "This web-application is used to "
                       "store information about balance "
                       "of some goods"}
