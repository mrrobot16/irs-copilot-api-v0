from fastapi import APIRouter

from db.health_model import HealthItemModel, HealthOfferModel, HealthImageModel

app_health_post = APIRouter()

@app_health_post.post("/items/")
async def create_item(item: HealthItemModel):
    return item

@app_health_post.post("/items2/{item_id}")
async def create_item(item_id: int, item: HealthItemModel):
    return {"item_id": item_id, **item.model_dump()}


@app_health_post.post("/items/")
async def create_item(item: HealthItemModel):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@app_health_post.post("/offers/")
async def create_offer(offer: HealthOfferModel):
    return offer

@app_health_post.post("/images/multiple/")
async def create_multiple_images(images: list[HealthImageModel]):
    return images