from fastapi import APIRouter, Body
from typing import Annotated

from fastapi.encoders import jsonable_encoder
from db.health_model import HealthItemModel, HealthUserModel

fake_db = {

}

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

app_health_put = APIRouter()

@app_health_put.get("/items-json/{item_id}", response_model=HealthItemModel)
async def read_item(item_id: str):
    return items[item_id]

@app_health_put.put("/items-json/{item_id}", response_model=HealthItemModel)
async def update_item(item_id: str, item: HealthItemModel):
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded

@app_health_put.put("/items-json/{id}")
def update_item(id: str, item: HealthItemModel):
    json_compatible_item_data = jsonable_encoder(item)
    # print(json_compatible_item_data)
    fake_db[id] = json_compatible_item_data
    # print(fake_db)
    # return json_compatible_item_data
    return fake_db

@app_health_put.patch("/items/{item_id}", response_model=HealthItemModel)
async def update_item(item_id: str, item: HealthItemModel):
    stored_item_data = items[item_id]
    stored_item_model = HealthItemModel(**stored_item_data)
    update_data = item.dict(exclude_unset=True)
    updated_item = stored_item_model.copy(update=update_data)
    items[item_id] = jsonable_encoder(updated_item)
    return updated_item

@app_health_put.put("/items/{item_id}")
def put_item(item_id: int, item: HealthItemModel):
    return {
        'item_name': item.name, 'item_id': item_id, 'item_is_offer': item.is_offer
    }

@app_health_put.put("/items2/{item_id}")
async def create_item2(item_id: int, item: HealthItemModel, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result

@app_health_put.put("/items3/{item_id}")
async def update_item(item_id: int, item: HealthItemModel, user: HealthUserModel):
    results = {"item_id": item_id, "item": item, "user": user}
    return results

@app_health_put.put("/items4/{item_id}")
async def update_item(
    item_id: int, item: HealthItemModel, user: HealthUserModel, importance: Annotated[int, Body()]
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results

@app_health_put.put("/items5/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: HealthItemModel,
    user: HealthUserModel,
    importance: int = Body(gt=0),
    q: str, # Without Body() it will asume is a parameter argument.
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results

@app_health_put.put("/items6/{item_id}")
async def update_item(item_id: int, item: Annotated[HealthItemModel, Body(embed=True, examples=[
                {
                    "name": "Foo Bar",
                    "description": "A very nice Item223223",
                    "price": 100.2,
                    "tax": 10.2,
                }
            ])]):
    results = {"item_id": item_id, "item": item}
    return results
examples=[
    {
        "name": "Foo",
        "description": "A very nice Item example",
        "price": 35.4,
        "tax": 3.2,
    },
    {
        "name": "Bar",
        "price": "35.4",
    },
    {
        "name": "Baz",
        "price": "thirty five point four",
    },
]
@app_health_put.put("/items7/{item_id}")
async def update_item7(item_id: int, item: Annotated[HealthItemModel, Body(embed=True, examples=examples)]):
    results = {"item_id": item_id, "item": item}
    return results

