import uvicorn
import logging
from app.orm.db_setup import database, engine
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.settings import settings
from app.api.partner import partner_api

async def startup():
    await database.connect()
    logger.info("nesos service is up!!!")

async def shutdown():
    await database.disconnect()
    logger.info("shutting down nesos service...")

@asynccontextmanager
async def lifespan(app:FastAPI):
    await startup()
    yield
    await shutdown()

app = FastAPI(title=settings.APP_NAME, lifespan=lifespan)

logger = logging.basicConfig(filename=settings.LOG_FILE)
logger = logging.getLogger(settings.GET_LOGGER)
logger.setLevel(settings.LOG_LEVEL)

app.include_router(partner_api, tags=["Partner"])