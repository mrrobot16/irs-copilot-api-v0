from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    description: str | None = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        # NOTE: in Pydantic, the orm_mode flag is now replace with from_attributes
        # orm_mode = True
        from_attributes = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        # NOTE: in Pydantic, the orm_mode flag is now replace with from_attributes
        # orm_mode = True
        from_attributes = True