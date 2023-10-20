import os
from fastapi import FastAPI, HTTPException
from typing import Union
import json
from db.models_example import Item, ModelName



app = FastAPI()


@app.get("/")
async def health():
    return {
        'status_code': 200
    }

@app.get("/items/me")
async def get_my_items():
    return {
        'item_id': 1
    }

@app.get("/items/{item_id}")
async def get_item(item_id: int, q: Union[str, None] = None):
    return {
        'item_id': item_id, 'q': q
    }

@app.put("/items/{item_id}")
def put_item(item_id: int, item: Item):
    return {
        'item_name': item.name, 'item_id': item_id, 'item_is_offer': item.is_offer
    }

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/files/{file_path:path}")
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
    
