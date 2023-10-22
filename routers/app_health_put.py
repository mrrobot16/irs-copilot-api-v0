from fastapi import APIRouter, Body
from typing import Annotated
from db.health_model import HealthItemModel, HealthUserModel


app_health_put = APIRouter()

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

