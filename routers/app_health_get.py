from fastapi import APIRouter, HTTPException, Query, Path, Cookie, Header, Response
from fastapi.responses import JSONResponse, RedirectResponse
from typing import Annotated
import os

from pyparsing import Any

from db.health_model import HealthEnum, HealthItemModel
from db.database import database

app_health_get = APIRouter()

@app_health_get.get("/portal")
async def get_portal(teleport: bool = False) -> Response:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return JSONResponse(content={"message": "Here's your interdimensional portal."})

@app_health_get.get("/teleport")
async def get_teleport() -> RedirectResponse:
    return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")

@app_health_get.get("/")
async def health():
    return {
        'status_code': 200
    }

@app_health_get.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return database[skip : skip + limit]

@app_health_get.get("/items2/")
async def read_items(q: str = Query(default="rick", max_length=50, min_length=3, regex="^fixedquery$")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app_health_get.get("/items3/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app_health_get.get("/items4/")
async def read_items(q: Annotated[list[str] | None, Query(deprecated=True)] = ["foo", "bar"]):
    query_items = {"q": q}
    return query_items

@app_health_get.get("/items-returns/", response_model=list[HealthItemModel])
async def read_items() -> Any:
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]


@app_health_get.get("/items-cookie/")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
    return {"ads_id": ads_id}

@app_health_get.get("/items-header/")
async def read_items(
    strange_header: Annotated[str | None, Header(convert_underscores=False)] = None
):
    return {"strange_header": strange_header}

@app_health_get.get("/items-xtokens/")
async def read_items(x_token: Annotated[list[str] | None, Header()] = None):
    return {"X-Token values": x_token}

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

@app_health_get.get("/items2/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

@app_health_get.get("/items3/{item_id}")
async def read_items(
    q: str, item_id: Annotated[int, Path(title="The ID of the item to get")]
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

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
async def get_model(model_name: HealthEnum):
    if model_name is HealthEnum.alexnet:
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

