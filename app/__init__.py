from fastapi import FastAPI

from .food import food_router
from .user import user_router
from .db import Base, engine

Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(user_router.router)
app.include_router(food_router.router)