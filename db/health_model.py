from pydantic import BaseModel, Field, HttpUrl, EmailStr
from enum import Enum

class HealthTags(Enum):
    items = "items"
    users = "users"

class HealthEnum(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class HealthImageModel(BaseModel):
    url: HttpUrl
    name: str


    name: str | None = None
    description: str | None = None
    price: float | None = None
    tax: float = 10.5
    tags: list[str] = []
class HealthItemModel(BaseModel):
    # name: str
    name: str | None = None
    # description: str | None = Field(
    #     default=None, title="The description of the item", max_length=300,
    #     examples=["A very nice Item example", "Some other description"]
    # )
    description: str | None = None
    # price: float = Field(gt=0, description="The price must be greater than zero")
    price: float | None = None
    # tax: float | None = None
    tax: float = 10.5
    is_offer: bool | None = None
    # tags: list[str] = []
    # tags: set[str] = set()
    tags: list[str] = []
    images: list[HealthImageModel] | None = None

    # model_config = {
    #     "json_schema_extra": {
    #         "examples": [
    #             {
    #                 "name": "Foo",
    #                 "description": "A very nice Item",
    #                 "price": 35.4,
    #                 "tax": 3.2,
    #             }
    #         ],
    #         "description": "A detailed description of the ItemModel.",
    #         "title": "HealthItem Title"
    #     }
    # }

class HealthOfferModel(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[HealthItemModel]

class HealthUserModel(BaseModel):
    username: str
    full_name: str | None = None
    email: EmailStr

class HealthUserInModel(BaseModel):
    password: str