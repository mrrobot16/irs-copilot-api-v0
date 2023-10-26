from fastapi import FastAPI, status

from .crud import get_user

app = FastAPI()

@app.get("/")
async def health():
    return {"status": status.HTTP_200_OK, "sql_app": True}