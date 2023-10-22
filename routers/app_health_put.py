from fastapi import APIRouter

from db.models_example import Item

app_health_put = APIRouter()

@app_health_put.put("/items/{item_id}")
def put_item(item_id: int, item: Item):
    return {
        'item_name': item.name, 'item_id': item_id, 'item_is_offer': item.is_offer
    }