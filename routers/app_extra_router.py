from fastapi import APIRouter, status
from typing import Union

from db.extra_model import CarItem, PlaneItem, UserIn, UserInDB, UserOut
from db.database import base_items

app_extra_router = APIRouter()

def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn, ):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")
    print(user_in_db)
    return user_in_db


@app_extra_router.post("/user/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved

@app_extra_router.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem], status_code=status.HTTP_200_OK)
async def read_item(item_id: str):
    return base_items[item_id]

@app_extra_router.get("/keyword-weights/", response_model=dict[str, float], status_code=201)
async def read_keyword_weights():
    return {"foo": 2.3, "bar": 3.4, "asdasd": 10}