from typing import Union
from pydantic import BaseModel
from enum import Enum


class EnumNet(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None