from fastapi import APIRouter

from db.health_model import HealthItemModel

app_health_put = APIRouter()

@app_health_put.put("/items/{item_id}")
def put_item(item_id: int, item: HealthItemModel):
    return {
        'item_name': item.name, 'item_id': item_id, 'item_is_offer': item.is_offer
    }