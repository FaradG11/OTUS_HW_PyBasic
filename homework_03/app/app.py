from fastapi import FastAPI

# from users.api import router as users_router

app = FastAPI()
# app.include_router(users_router)


@app.get("/ping/")
def ping():
    return {"message": "pong"}

