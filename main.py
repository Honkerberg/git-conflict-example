from fastapi import FastAPI
from fastapi.responses import JSONResponse
import logging

logger = logging.getLogger("my_logger")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)


app = FastAPI()


@app.get("/")
async def root():
    logger.info("Root call")
    return JSONResponse(content={"message": "Welcome to FastAPI!"})


@app.get("/user/{user_id}")
async def get_user(user_id: int):
    return JSONResponse(content={"user_id": user_id, "name": "User"})


@app.post("/items/")
async def create_item(item: dict):
    return JSONResponse(content={"item": item, "status": "created"})


@app.get("/status")
async def status():
    return JSONResponse(content={"status": "OK"})
