from fastapi import APIRouter, HTTPException, status

from db.error_handling_model import UnicornException, HorseException, Item

app_error_handling_router = APIRouter()

items = {"foo": "The Foo Wrestlers"}

@app_error_handling_router.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return {"item": items[item_id]}

@app_error_handling_router.get("/items2/{item_id}")
async def read_item(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return {"item_id": item_id}

@app_error_handling_router.get("/items-header/{item_id}")
async def read_item_header(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"X-Error": "There goes my error"},
        )
    return {"item": items[item_id]}

@app_error_handling_router.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}

@app_error_handling_router.get("/horses/{name}")
async def read_unicorn(name: str):
    if name == "yodo":
        raise HorseException(name=name)
    return {"horse_name": name}

@app_error_handling_router.post("/items/")
async def create_item(item: Item):
    return item

@app_error_handling_router.post("/items2/")
async def create_item(item: Item):
    return item