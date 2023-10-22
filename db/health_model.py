from typing import Union
from pydantic import BaseModel
from enum import Enum


class HealthEnum(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class HealthItemModel(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    is_offer: Union[bool, None] = None