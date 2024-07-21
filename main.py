from typing import *
from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from schemas import *
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Очистка бд")
    await create_tables()
    print("Создание бд")
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)


