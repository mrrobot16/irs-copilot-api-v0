from fastapi import APIRouter

from db.health_model import HealthItemModel

app_health_post = APIRouter()

@app_health_post.post("/items/")
async def create_item(item: HealthItemModel):
    return item

@app_health_post.post("/items2/{item_id}")
async def create_item2(item_id: int, item: HealthItemModel):
    # item_dict = item.dict()
    # item_dict = item.dict()
    # if item.tax:
    #     price_with_tax = item.price + item.tax
    #     item_dict.update({"price_with_tax": price_with_tax})
    # return item
    return {"item_id": item_id, **item.model_dump()}


@app_health_post.post("/items/")
async def create_item(item: HealthItemModel):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict