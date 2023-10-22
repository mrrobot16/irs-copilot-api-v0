from typing import Union
from pydantic import BaseModel, Field
from enum import Enum


class HealthEnum(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class HealthItemModel(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None
    is_offer: bool | None = None
    tags: list[str] = []

class HealthUserModel(BaseModel):
    username: str
    full_name: str | None = None