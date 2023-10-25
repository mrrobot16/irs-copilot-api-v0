from fastapi import APIRouter, Depends, HTTPException, status

from db.error_handling_model import UnicornException, HorseException, Item
from services import verify_key, verify_token

app_dependency_injection = APIRouter(dependencies=[Depends(verify_token), Depends(verify_key)])

@app_dependency_injection.get("/items/")
async def read_items():
    return [{"item": "Foo"}, {"item": "Bar"}]