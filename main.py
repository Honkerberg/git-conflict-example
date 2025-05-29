from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
async def root():
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
