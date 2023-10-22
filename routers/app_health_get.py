from fastapi import APIRouter, HTTPException
import os

from db.health_model import EnumNet
from db.database import database

app_health_get = APIRouter()


@app_health_get.get("/")
async def health():
    return {
        'status_code': 200
    }

@app_health_get.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return database[skip : skip + limit]

@app_health_get.get("/items/me")
async def get_my_items():
    return {
        'item_id': 1
    }

@app_health_get.get("/items/{item_id}")
async def get_item(item_id: int, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@app_health_get.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@app_health_get.get("/items-required/{item_id}")
async def read_user_item_required(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item

@app_health_get.get("/models/{model_name}")
async def get_model(model_name: EnumNet):
    if model_name is EnumNet.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@app_health_get.get("/files/{file_path:path}")
async def read_file(file_path: str):
    # Construct an absolute file path within the home directory of the user "samurai"
    absolute_file_path = os.path.join("/Users/samurai/", file_path)
    
    # Check if the file exists
    if os.path.exists(absolute_file_path) and os.path.isfile(absolute_file_path):
        # Read and return the content of the file (ensure the file is a text file)
        with open(absolute_file_path, "r") as file:
            print('file', file)
            content = file.read() # for .txt
            # content = json.loads(file) # for .json
        return {"file_path": absolute_file_path, "content": content}
    else:
        # If the file does not exist, return a 404 error
        raise HTTPException(status_code=404, detail="File not found")

